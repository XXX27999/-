// Dashboard web server: serves the SPA, exposes a small REST API over the
// captured logs, and pushes new entries live over SSE. All format-specific
// work is delegated to the adapter chosen per entry (anthropic | openai).

import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { summarize, listSessionsMulti, loadSessionMulti, summarizeSessionMulti, summarizeSessionMultiAsync, readEntryByIdMulti, rmEntriesMulti, rmEntriesMultiFast, rmSessionFast, listSessions, scheduleBlobGc } from "./store.js";
import { getAdapter, detectFormat } from "./formats/index.js";
import { aggregateSessionStats, latencyMs, requestTiming, sessionModels } from "./session-stats.js";
import { diffBlockLists } from "./diff.js";
import { renderExport } from "./export.js";
import { summarizeUsage } from "./usage.js";
import { estimateRequestTokens, estimateResponseTokens } from "./tokens.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WEB_DIR = path.join(__dirname, "..", "web");

const MIME = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css" };

// `store` is present in live (`ccglass claude`) mode; otherwise we read from disk.
export function createServer({ roots, store }) {
  const sseClients = new Set();

  if (store) {
    const push = (rec) => {
      const data = `data: ${JSON.stringify(summarize(rec))}\n\n`;
      for (const res of sseClients) res.write(data);
    };
    store.on("entry", push);
    store.on("update", push);
    // Deletions are broadcast as a dedicated event so open dashboards can drop
    // the row without re-fetching the whole session.
    store.on("delete", (id) => {
      const data = `data: ${JSON.stringify({ deleted: id })}\n\n`;
      for (const res of sseClients) res.write(data);
    });
  }

  return http.createServer(async (req, res) => {
    const url = new URL(req.url, "http://localhost");
    const p = url.pathname;

    try {
      if (p === "/api/sessions") return json(res, apiSessions(roots, store));
      if (p === "/api/requests") return json(res, await apiRequests(roots, store, url));
      if (p === "/api/delete") return apiDelete(roots, store, url, req, res);
      if (p === "/api/delete-batch") return apiDeleteBatch(roots, store, req, res);
      if (p === "/api/session-stats") return json(res, await apiSessionStats(roots, store, url));
      if (p === "/api/usage") return json(res, summarizeUsage(roots, { names: url.searchParams.get("names") === "1" }));
      if (p.startsWith("/api/request/")) return json(res, apiRequest(roots, store, decodeURIComponent(p.slice("/api/request/".length))));
      if (p === "/api/diff") return json(res, apiDiff(roots, store, url));
      if (p === "/api/export") return apiExport(roots, store, url, res);
      if (p === "/api/stream") return stream(res, sseClients);
      return serveStatic(p, res);
    } catch (e) {
      json(res, { error: e.message }, 500);
    }
  });
}

// ---- API handlers --------------------------------------------------------

function getEntry(roots, store, id) {
  if (store) {
    const live = store.get(id);
    if (live) return live;
  }
  return readEntryByIdMulti(roots, id);
}

function apiSessions(roots, store) {
  return { sessions: listSessionsMulti(roots), live: store ? store.sessionId : null };
}

function sessionRecords(roots, store, session) {
  if (store && (!session || session === store.sessionId)) return store.entries;
  if (!session) return [];
  return loadSessionMulti(roots, session);
}

async function apiRequests(roots, store, url) {
  const session = url.searchParams.get("session");
  if (store && (!session || session === store.sessionId)) {
    return { entries: store.entries.map(summarize) };
  }
  if (!session) return { entries: [] };
  // Prefer cached summaries for disk sessions. This endpoint is polled after
  // every deletion; unpacking hundreds of large manifests here is what made
  // delete look broken (the UI waited ~66 s for the refresh).
  return { entries: await summarizeSessionMultiAsync(roots, session) };
}

// ---- deletion ------------------------------------------------------------
// `DELETE /api/delete?id=<session>/<seq>` removes one captured request;
// `DELETE /api/delete?session=<session>` removes a whole capture session.
// Both prune now-orphaned blobs and drop matching live entries from memory.

function apiDelete(roots, store, url, req, res) {
  if (req.method !== "DELETE" && req.method !== "POST") {
    return json(res, { error: "method not allowed" }, 405);
  }
  const id = url.searchParams.get("id");
  const session = url.searchParams.get("session");

  if (id) {
    const parts = id.split("/");
    if (parts.length !== 2 || !parts[0] || !parts[1]) {
      return json(res, { error: "invalid id" }, 400);
    }
    const result = rmEntriesMultiFast(roots, [id]);
    if (!result.removed.length) return json(res, { error: "not found", id }, 404);
    if (store) store.remove(id);
    if (result.touched.length) {
      setImmediate(() => scheduleBlobGc(result.touched, listSessions, (r, s) => path.join(r, s)));
    }
    return json(res, { deleted: id, removed: result.removed.length });
  }

  if (session) {
    if (session !== path.basename(session) || session === "." || session === "..") {
      return json(res, { error: "invalid session" }, 400);
    }
    const result = rmSessionFast(roots, session);
    const removed = result.removed;
    if (store && store.sessionId === session) {
      for (const e of [...store.entries]) store.remove(e.id);
    }
    if (!removed) return json(res, { error: "not found", session }, 404);
    if (result.touched.length) {
      setImmediate(() => scheduleBlobGc(result.touched, listSessions, (r, s) => path.join(r, s)));
    }
    return json(res, { deleted: session, removed });
  }

  return json(res, { error: "id or session required" }, 400);
}

// `POST /api/delete-batch` with body `{"ids":["<session>/<seq>", ...]}`.
// Select-all can cover hundreds of rows; deleting them one request at a time
// would re-run the blob GC scan per row, so this removes every file first and
// reclaims orphaned blobs once. Responds with the ids that were actually found.
function readJsonBody(req, limit = 1_000_000) {
  return new Promise((resolve, reject) => {
    let raw = "";
    req.on("data", (chunk) => {
      raw += chunk;
      if (raw.length > limit) {
        reject(new Error("body too large"));
        req.destroy();
      }
    });
    req.on("end", () => {
      if (!raw) return resolve(null);
      try { resolve(JSON.parse(raw)); } catch { reject(new Error("invalid json")); }
    });
    req.on("error", reject);
  });
}

async function apiDeleteBatch(roots, store, req, res) {
  if (req.method !== "POST" && req.method !== "DELETE") {
    return json(res, { error: "method not allowed" }, 405);
  }
  let body;
  try {
    body = await readJsonBody(req);
  } catch (e) {
    return json(res, { error: e.message }, 400);
  }
  const ids = Array.isArray(body?.ids) ? body.ids : null;
  if (!ids) return json(res, { error: "ids array required" }, 400);
  if (!ids.length) return json(res, { deleted: [], removed: 0 });

  const result = rmEntriesMultiFast(roots, ids);
  const removed = result.removed;
  if (store) for (const id of removed) store.remove(id);
  if (result.touched.length) {
    setImmediate(() => scheduleBlobGc(result.touched, listSessions, (r, s) => path.join(r, s)));
  }
  return json(res, { deleted: removed, removed: removed.length });
}

async function apiSessionStats(roots, store, url) {
  const session = url.searchParams.get("session");
  if (!session) return { error: "session required" };
  const live = store && session === store.sessionId;
  const summaries = !live ? await summarizeSessionMultiAsync(roots, session) : null;
  const model = url.searchParams.get("model") || "all";
  if (summaries) {
    const scoped = model && model !== "all"
      ? summaries.filter((s) => s.usage?.model === model)
      : summaries;
    let totalInput = 0;
    let totalOutput = 0;
    let cacheRead = 0;
    let totalUsd = 0;
    let estTotal = 0;
    let completed = 0;
    const models = new Set();
    for (const s of scoped) {
      if (s.usage?.model) models.add(s.usage.model);
      if (!s.usage || s.error != null) continue;
      totalInput += s.usage.input || 0;
      totalOutput += s.usage.output || 0;
      cacheRead += s.usage.cacheRead || 0;
      totalUsd += s.usage.usd || 0;
      estTotal += (s.usage.estInput || 0) + (s.usage.estOutput || 0);
      completed++;
    }
    return {
      session,
      models: [...models].sort(),
      model: model && model !== "all" ? model : "all",
      completed,
      total: scoped.length,
      totalInput,
      totalOutput,
      estTotal,
      actualTotal: totalInput + totalOutput,
      cacheHitRate: totalInput > 0 ? cacheRead / totalInput : 0,
      totalUsd,
    };
  }
  const records = sessionRecords(roots, store, session);
  return {
    session,
    models: sessionModels(records),
    ...aggregateSessionStats(records, { model }),
  };
}

function apiRequest(roots, store, id) {
  const rec = getEntry(roots, store, id);
  if (!rec) return { error: "not found" };
  const fmt = detectFormat(rec);
  const A = getAdapter(fmt);
  const body = rec.request?.body || {};
  const response = rec.response?.raw ? A.reassemble(rec.response.raw) : rec.response;
  const usage = response?.usage || {};
  const timing = requestTiming(rec, usage);
  // Estimated whole-request tokens: request body (input) + response content
  // (output). Compared against the provider's own usage so the dashboard can
  // show how far the preview estimate drifts from the real bill.
  const estInput = estimateRequestTokens(body);
  const estOutput = estimateResponseTokens(response);
  const actualInput = usage.input_tokens ?? usage.prompt_tokens ?? 0;
  const actualOutput = usage.output_tokens ?? usage.completion_tokens ?? 0;
  return {
    ...rec,
    latencyMs: latencyMs(rec),
    timing,
    format: fmt,
    estimate: {
      input: estInput,
      output: estOutput,
      total: estInput + estOutput,
      actualTotal: actualInput + actualOutput,
    },
    parsed: {
      format: fmt,
      view: A.view(body),
      response,
      estTokens: estInput,
      estOutputTokens: estOutput,
      cost: A.cost(response?.model || body.model, usage),
    },
  };
}

function apiDiff(roots, store, url) {
  const a = getEntry(roots, store, url.searchParams.get("a"));
  const b = getEntry(roots, store, url.searchParams.get("b"));
  if (!a || !b) return { error: "need both a and b" };
  const blocksA = getAdapter(detectFormat(a)).blocks(a.request?.body || {});
  const blocksB = getAdapter(detectFormat(b)).blocks(b.request?.body || {});
  return diffBlockLists(blocksA, blocksB);
}

function apiExport(roots, store, url, res) {
  const id = url.searchParams.get("id");
  const format = url.searchParams.get("format") || "md";
  const rec = getEntry(roots, store, id);
  if (!rec) return json(res, { error: "not found" }, 404);

  const { contentType, ext, body } = renderExport(rec, format);
  res.writeHead(200, { "content-type": contentType, ...attach(id, ext) });
  return res.end(body);
}

// ---- helpers -------------------------------------------------------------

function json(res, obj, code = 200) {
  res.writeHead(code, { "content-type": "application/json; charset=utf-8" });
  res.end(JSON.stringify(obj));
}

function stream(res, clients) {
  res.writeHead(200, { "content-type": "text/event-stream", "cache-control": "no-cache", connection: "keep-alive" });
  res.write(": connected\n\n");
  clients.add(res);
  res.on("close", () => clients.delete(res));
}

function serveStatic(p, res) {
  const file = p === "/" ? "index.html" : p.replace(/^\//, "");
  const full = path.join(WEB_DIR, file);
  if (!full.startsWith(WEB_DIR) || !fs.existsSync(full)) {
    res.writeHead(404).end("not found");
    return;
  }
  res.writeHead(200, { "content-type": MIME[path.extname(full)] || "application/octet-stream" });
  fs.createReadStream(full).pipe(res);
}

function attach(id, ext) {
  return { "content-disposition": `attachment; filename="ccglass-${id.replace(/\//g, "_")}.${ext}"` };
}

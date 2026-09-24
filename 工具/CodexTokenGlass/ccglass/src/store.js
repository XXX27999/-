// Persistence layer: every captured request/response pair is written to
// <root>/<session>/NNNN.json (default ~/.ccglass/sessions/<project-key>/).
// The Store also acts as an event bus so the dashboard server can push new
// entries live.

import fs from "node:fs";
import path from "node:path";
import { EventEmitter } from "node:events";
import { packRecord, unpackRecord, readBlob, gcBlobs, gcBlobsAsync } from "./blobs.js";
import { latencyMs, recordModel } from "./session-stats.js";
import { detectFormat, getAdapter } from "./formats/index.js";
import { estimateRequestTokens, estimateResponseTokens } from "./tokens.js";

const mask = (v) =>
  String(v)
    .replace(/(Bearer\s+\S{6})\S+(\S{4})/g, "$1…REDACTED…$2")
    .replace(/(sk-ant-[\w-]{6})\S+(\S{4})/g, "$1…REDACTED…$2");

const pad = (n) => String(n).padStart(4, "0");

function localSessionId() {
  const d = new Date();
  const p = (n, w) => String(n).padStart(w, "0");
  return `${d.getFullYear()}-${p(d.getMonth()+1,2)}-${p(d.getDate(),2)}T${p(d.getHours(),2)}-${p(d.getMinutes(),2)}-${p(d.getSeconds(),2)}-${p(d.getMilliseconds(),3)}`;
}

export function localTimestamp(ms) {
  const d = ms ? new Date(ms) : new Date();
  const p = (n, w) => String(n).padStart(w, "0");
  return `${d.getFullYear()}-${p(d.getMonth()+1,2)}-${p(d.getDate(),2)}T${p(d.getHours(),2)}-${p(d.getMinutes(),2)}-${p(d.getSeconds(),2)}-${p(d.getMilliseconds(),3)}`;
}

export class Store extends EventEmitter {
  constructor({ root, redact = true, format = "anthropic" }) {
    super();
    this.root = root;
    this.redact = redact;
    this.format = format;
    this.sessionId = localSessionId();
    this.sessionDir = path.join(root, this.sessionId);
    fs.mkdirSync(this.sessionDir, { recursive: true });
    this.entries = [];
    this.seq = 0;
    // Ids deleted while their request was still in flight; update() must not
    // resurrect them on disk or over SSE.
    this.removed = new Set();
  }

  _maskHeaders(h) {
    if (!this.redact || !h) return h;
    const c = { ...h };
    for (const k of Object.keys(c)) {
      const lk = k.toLowerCase();
      if (lk === "authorization" || lk === "x-api-key") c[k] = mask(c[k]);
    }
    return c;
  }

  _file(seq) {
    return path.join(this.sessionDir, `${pad(seq)}.json`);
  }

  // Record a request (response filled in later via update()).
  add({ request }) {
    const seq = ++this.seq;
    const rec = {
      id: `${this.sessionId}/${pad(seq)}`,
      session: this.sessionId,
      seq,
      ts: Date.now(),
      format: this.format,
      request: { ...request, headers: this._maskHeaders(request.headers) },
      response: null,
    };
    this._persist(rec);
    this.entries.push(rec);
    this.emit("entry", rec);
    return rec;
  }

  update(rec) {
    if (this.removed.has(rec.id)) return;
    this._persist(rec);
    this.emit("update", rec);
  }

  // Write the v2 manifest (request content split into content-addressed blobs).
  _persist(rec) {
    // The session directory can be removed from under us (dashboard session
    // delete, external cleanup); recreate it so an in-flight request cannot
    // break the proxy with ENOENT.
    fs.mkdirSync(this.sessionDir, { recursive: true });
    const manifest = packRecord(this.root, rec);
    const body = rec.request?.body || {};
    manifest.metrics = {
      estInput: estimateRequestTokens(body),
      estOutput: rec.response?.raw
        ? estimateResponseTokens(getAdapter(detectFormat(rec)).reassemble(rec.response.raw))
        : estimateResponseTokens(rec.response || null),
      nToolUse: countToolUse(Array.isArray(body.messages) ? body.messages : body.input || []),
    };
    fs.writeFileSync(this._file(rec.seq), JSON.stringify(manifest, null, 2));
  }

  list() {
    return this.entries.map(summarize);
  }

  get(id) {
    return this.entries.find((e) => e.id === id) || readEntryById(this.root, id);
  }

  /** Drop one live entry from memory (the on-disk file is removed separately). */
  remove(id) {
    const i = this.entries.findIndex((e) => e.id === id);
    if (i < 0) return false;
    this.entries.splice(i, 1);
    this.removed.add(id);
    this.emit("delete", id);
    return true;
  }
}

// ---- shared helpers also used by `ccglass view` (no live store) ------------

export function summarize(rec) {
  const b = rec.request?.body || {};
  const items = Array.isArray(b.messages) ? b.messages : Array.isArray(b.input) ? b.input : [];
  const nToolUse = countToolUse(items);
  const ms = latencyMs(rec);
  return {
    id: rec.id,
    session: rec.session,
    seq: rec.seq,
    ts: rec.ts,
    startedAt: rec.startedAt ?? rec.ts ?? null,
    latencyMs: ms,
    format: rec.format || null,
    method: rec.request?.method,
    url: rec.request?.url,
    model: recordModel(rec),
    nMessages: items.length,
    nTools: Array.isArray(b.tools) ? b.tools.length : 0,
    nToolUse,
    status: rec.response?.status ?? null,
    error: rec.response?.error ?? null,
    pending: !rec.response,
    usage: usageSummary(rec),
  };
}

// Count tool calls that actually happened in this request (anthropic tool_use
// blocks, plus openai-style tool_calls), distinct from nTools which is just how
// many tools were offered.
function countToolUse(items) {
  let n = 0;
  for (const m of items) {
    const c = Array.isArray(m?.content) ? m.content : [];
    for (const blk of c) if (blk?.type === "tool_use") n++;
    if (Array.isArray(m?.tool_calls)) n += m.tool_calls.length;
  }
  return n;
}

// Token totals belong to the whole HTTP round-trip. Providers do not bill
// each message or tool step inside that request separately.
function usageSummary(rec) {
  if (!rec?.response) return null;
  try {
    const adapter = getAdapter(detectFormat(rec));
    const resp = rec.response.raw ? adapter.reassemble(rec.response.raw) : rec.response;
    const usage = resp?.usage;
    const hasUsage = usage && (
      usage.input_tokens != null ||
      usage.output_tokens != null ||
      usage.prompt_tokens != null ||
      usage.completion_tokens != null
    );
    if (!hasUsage) return null;
    const model = resp?.model || rec.request?.body?.model || "";
    const cost = adapter.cost(model, usage) || {};
    return {
      model,
      input: cost.totalInput ?? usage.input_tokens ?? usage.prompt_tokens ?? 0,
      output: cost.output ?? usage.output_tokens ?? usage.completion_tokens ?? 0,
      cacheRead: cost.cacheRead ?? 0,
      cacheWrite: cost.cacheWrite ?? 0,
      usd: cost.usd ?? 0,
      estInput: estimateRequestTokens(rec.request?.body || {}),
      estOutput: estimateResponseTokens(resp),
    };
  } catch {
    return null;
  }
}

export function listSessions(root) {
  if (!fs.existsSync(root)) return [];
  return fs
    .readdirSync(root, { withFileTypes: true })
    .filter((d) => d.isDirectory() && d.name !== "blobs")
    .map((d) => d.name)
    .sort()
    .reverse();
}

export function hasCapturedLogs(root) {
  if (!fs.existsSync(root)) return false;
  for (const s of listSessions(root)) {
    const dir = path.join(root, s);
    try {
      if (fs.readdirSync(dir).some((f) => f.endsWith(".json"))) return true;
    } catch {
      /* ignore */
    }
  }
  return false;
}

/** Parse `<session>/<seq>` entry ids; returns null when malformed. */
export function parseEntryId(id) {
  const i = id.indexOf("/");
  if (i <= 0 || i === id.length - 1) return null;
  const session = id.slice(0, i);
  const seq = id.slice(i + 1);
  if (!session || !seq || seq.includes("/")) return null;
  return { session, seq };
}

function shouldReplaceRecord(prev, rec, prevMtime, newMtime) {
  const pts = prev.ts ?? 0;
  const rts = rec.ts ?? 0;
  if (rts > pts) return true;
  if (rts < pts) return false;
  return newMtime > prevMtime;
}

/** Read one capture file; returns null on parse errors. Normalizes id to the path key. */
function readRecordFile(file, id, root) {
  let raw;
  try {
    raw = JSON.parse(fs.readFileSync(file, "utf8"));
  } catch {
    return null;
  }
  if (raw && raw.v === 2) {
    try {
      const rec = unpackRecord(root, raw);
      rec.id = id;
      return rec;
    } catch {
      return null;
    }
  }
  // Legacy full record: hand it back, and opportunistically repack to v2 in place.
  raw.id = id;
  tryMigrate(file, root, raw);
  return raw;
}

// Repack a legacy full record into a v2 manifest on disk. Atomic (temp + rename)
// and best-effort: a read-only root (e.g. a legacy ./.ccglass) is silently skipped
// so migration failure never breaks a read.
function tryMigrate(file, root, rec) {
  try {
    const manifest = packRecord(root, rec);
    const tmp = `${file}.${process.pid}.tmp`;
    fs.writeFileSync(tmp, JSON.stringify(manifest, null, 2));
    fs.renameSync(tmp, file);
  } catch {
    /* read-only root or transient error — keep serving reads */
  }
}

export function listSessionsMulti(roots) {
  const seen = new Set();
  const sessions = [];
  for (const root of roots) {
    for (const s of listSessions(root)) {
      if (!seen.has(s)) {
        seen.add(s);
        sessions.push(s);
      }
    }
  }
  sessions.sort((a, b) => (a > b ? -1 : a < b ? 1 : 0));
  return sessions;
}

// Disk-session summary cache. A long-running Codex session can hold hundreds of
// multi-megabyte manifests; re-reading and unpacking every file for each list
// or stats refresh turns a 600 MB session into ~100 seconds of JSON work and
// can push the collector into its heap limit. Cache one summary per file,
// keyed by mtime+size, and only unpack files that changed.
const SUMMARY_CACHE = new Map();
const SUMMARY_CACHE_MAX_FILES = 20_000;
const TOOL_COUNT_CACHE = new Map();
const METRICS_BACKFILL = new Set();
const METRICS_BACKFILL_QUEUE = [];
let METRICS_BACKFILL_RUNNING = false;

function summaryCacheKey(root, session, file) {
  return `${root}\u0000${session}\u0000${file}`;
}

function toolCount(root, ref) {
  if (!ref) return 0;
  const hit = TOOL_COUNT_CACHE.get(ref);
  if (hit != null) return hit;
  let n = 0;
  try {
    const tools = readBlob(root, ref);
    n = Array.isArray(tools) ? tools.length : 0;
  } catch {
    n = 0;
  }
  TOOL_COUNT_CACHE.set(ref, n);
  return n;
}

// Summarize a v2 manifest without unpacking the message blobs. The list and
// stats views only need metadata, counts, response status and usage; reading
// every conversation blob here is what made a 600 MB session take a minute.
function summarizeManifest(root, manifest, id) {
  if (!manifest || manifest.v !== 2) return null;
  const req = manifest.request || {};
  const meta = req.meta || {};
  const response = manifest.response ?? null;
  const light = {
    format: manifest.format,
    ts: manifest.ts,
    startedAt: manifest.startedAt ?? manifest.ts ?? null,
    request: { method: req.method, url: req.url, body: { model: meta.model } },
    response,
  };
  const estInput = manifest.metrics?.estInput;
  const estOutput = manifest.metrics?.estOutput;
  const usage = usageSummary(light);
  if (usage && estInput != null) {
    usage.estInput = estInput;
    usage.estOutput = estOutput ?? 0;
  }
  return {
    id,
    session: manifest.session,
    seq: manifest.seq,
    ts: manifest.ts,
    startedAt: manifest.startedAt ?? manifest.ts ?? null,
    latencyMs: latencyMs(light),
    format: manifest.format || null,
    method: req.method,
    url: req.url,
    model: response?.model || meta.model || null,
    nMessages: Array.isArray(req.messages) ? req.messages.length : 0,
    nTools: toolCount(root, req.tools),
    nToolUse: manifest.metrics?.nToolUse ?? 0,
    status: response?.status ?? null,
    error: response?.error ?? null,
    pending: !response,
    usage,
  };
}

function readSummaryFile(file, id, root, stat) {
  const key = summaryCacheKey(root, path.dirname(file), path.basename(file));
  const stamp = `${stat.mtimeMs}:${stat.size}`;
  const hit = SUMMARY_CACHE.get(key);
  if (hit && hit.stamp === stamp) return hit.summary;

  let summary = null;
  let manifest = null;
  try {
    manifest = JSON.parse(fs.readFileSync(file, "utf8"));
    summary = manifest?.v === 2
      ? summarizeManifest(root, manifest, id)
      : summarize(readRecordFile(file, id, root));
  } catch {
    summary = null;
  }
  if (manifest?.v === 2 && !manifest.metrics && !METRICS_BACKFILL.has(file)) {
    METRICS_BACKFILL.add(file);
    // Keep only the locator in the queue. Holding the parsed manifest here
    // would pin every large request body in memory until the backfill drains.
    METRICS_BACKFILL_QUEUE.push({ file, id, root });
    setImmediate(runMetricsBackfill);
  }
  if (summary) {
    if (SUMMARY_CACHE.size >= SUMMARY_CACHE_MAX_FILES) {
      const oldest = SUMMARY_CACHE.keys().next().value;
      if (oldest != null) SUMMARY_CACHE.delete(oldest);
    }
    SUMMARY_CACHE.set(key, { stamp, summary });
  }
  return summary;
}

// Async summary reader used by the HTTP list endpoint. A synchronous first
// scan of a 600 MB session monopolizes the event loop, which makes a
// concurrent delete response appear to hang. Read in small batches and yield
// between them; cached files return immediately.
async function readSummaryFileAsync(file, id, root, stat) {
  const key = summaryCacheKey(root, path.dirname(file), path.basename(file));
  const stamp = `${stat.mtimeMs}:${stat.size}`;
  const hit = SUMMARY_CACHE.get(key);
  if (hit && hit.stamp === stamp) return hit.summary;

  let manifest = null;
  let summary = null;
  try {
    manifest = JSON.parse(await fs.promises.readFile(file, "utf8"));
    summary = manifest?.v === 2
      ? summarizeManifest(root, manifest, id)
      : summarize(readRecordFile(file, id, root));
  } catch {
    summary = null;
  }
  if (manifest?.v === 2 && !manifest.metrics && !METRICS_BACKFILL.has(file)) {
    METRICS_BACKFILL.add(file);
    METRICS_BACKFILL_QUEUE.push({ file, id, root });
    setImmediate(runMetricsBackfill);
  }
  if (summary) {
    if (SUMMARY_CACHE.size >= SUMMARY_CACHE_MAX_FILES) {
      const oldest = SUMMARY_CACHE.keys().next().value;
      if (oldest != null) SUMMARY_CACHE.delete(oldest);
    }
    SUMMARY_CACHE.set(key, { stamp, summary });
  }
  return summary;
}

function runMetricsBackfill() {
  if (METRICS_BACKFILL_RUNNING) return;
  const job = METRICS_BACKFILL_QUEUE.shift();
  if (!job) return;
  METRICS_BACKFILL_RUNNING = true;
  setImmediate(() => {
    backfillMetrics(job.file, job.id, job.root);
    METRICS_BACKFILL_RUNNING = false;
    runMetricsBackfill();
  });
}

// Older v2 manifests predate the metrics field. Fill it in once in the
// background so the dashboard can keep serving summaries without unpacking
// history blobs on every request.
function backfillMetrics(file, id, root) {
  try {
    const manifest = JSON.parse(fs.readFileSync(file, "utf8"));
    if (!manifest || manifest.v !== 2 || manifest.metrics) return;
    const rec = unpackRecord(root, manifest);
    const response = rec.response?.raw
      ? getAdapter(detectFormat(rec)).reassemble(rec.response.raw)
      : rec.response || null;
    manifest.metrics = {
      estInput: estimateRequestTokens(rec.request?.body || {}),
      estOutput: estimateResponseTokens(response),
      nToolUse: countToolUse(Array.isArray(rec.request?.body?.messages)
        ? rec.request.body.messages
        : rec.request?.body?.input || []),
    };
    const tmp = `${file}.${process.pid}.metrics.tmp`;
    fs.writeFileSync(tmp, JSON.stringify(manifest, null, 2));
    fs.renameSync(tmp, file);
    const key = summaryCacheKey(root, path.dirname(file), path.basename(file));
    SUMMARY_CACHE.delete(key);
  } catch {
    /* best effort; a read-only root simply keeps the cheap fallback */
  } finally {
    METRICS_BACKFILL.delete(file);
  }
}

/**
 * Lightweight summaries for a whole session without materializing every
 * unpacked record. Prefer the live Store when the session is still active.
 */
export function summarizeSessionMulti(roots, session) {
  const byId = new Map();
  for (const root of roots) {
    const dir = path.join(root, session);
    if (!fs.existsSync(dir)) continue;
    let files;
    try {
      files = fs.readdirSync(dir).filter((f) => f.endsWith(".json")).sort();
    } catch {
      continue;
    }
    for (const f of files) {
      const file = path.join(dir, f);
      let stat;
      try {
        stat = fs.statSync(file);
      } catch {
        continue;
      }
      const seq = f.replace(/\.json$/, "");
      const id = `${session}/${seq}`;
      const summary = readSummaryFile(file, id, root, stat);
      if (!summary) continue;
      const prev = byId.get(id);
      if (!prev || (summary.ts ?? 0) > (prev.ts ?? 0)) byId.set(id, summary);
    }
  }
  return [...byId.values()].sort((a, b) => (a.ts ?? 0) - (b.ts ?? 0));
}

export async function summarizeSessionMultiAsync(roots, session) {
  const byId = new Map();
  const entries = [];
  for (const root of roots) {
    const dir = path.join(root, session);
    let files;
    try {
      files = (await fs.promises.readdir(dir)).filter((f) => f.endsWith(".json")).sort();
    } catch {
      continue;
    }
    for (const f of files) {
      const file = path.join(dir, f);
      let stat;
      try {
        stat = await fs.promises.stat(file);
      } catch {
        continue;
      }
      entries.push({ file, stat, id: `${session}/${f.replace(/\.json$/, "")}`, root });
    }
  }

  const BATCH = 24;
  for (let i = 0; i < entries.length; i += BATCH) {
    const slice = entries.slice(i, i + BATCH);
    const summaries = await Promise.all(
      slice.map(({ file, stat, id, root }) => readSummaryFileAsync(file, id, root, stat))
    );
    for (let j = 0; j < slice.length; j++) {
      const summary = summaries[j];
      if (!summary) continue;
      const prev = byId.get(slice[j].id);
      if (!prev || (summary.ts ?? 0) > (prev.ts ?? 0)) byId.set(slice[j].id, summary);
    }
    await new Promise((resolve) => setImmediate(resolve));
  }
  return [...byId.values()].sort((a, b) => (a.ts ?? 0) - (b.ts ?? 0));
}

export function loadSessionMulti(roots, session) {
  const byId = new Map();
  const fileMtime = new Map();

  for (const root of roots) {
    const dir = path.join(root, session);
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".json")).sort()) {
      const file = path.join(dir, f);
      const seq = f.replace(/\.json$/, "");
      const id = `${session}/${seq}`;
      const st = fs.statSync(file);
      const prev = byId.get(id);

      const rec = readRecordFile(file, id, root);
      if (!rec) continue;

      if (prev) {
        const firstMtime = fileMtime.get(id) ?? 0;
        if (shouldReplaceRecord(prev, rec, firstMtime, st.mtimeMs)) {
          byId.set(id, rec);
          fileMtime.set(id, st.mtimeMs);
        }
        continue;
      }

      byId.set(id, rec);
      fileMtime.set(id, st.mtimeMs);
    }
  }

  return [...byId.values()].sort((a, b) => (a.ts ?? 0) - (b.ts ?? 0));
}

export function readEntryByIdMulti(roots, id) {
  const parts = parseEntryId(id);
  if (!parts) return null;
  const { session, seq } = parts;
  let best = null;
  let bestMtime = 0;
  for (const root of roots) {
    const rec = readEntryById(root, id);
    if (!rec) continue;
    const file = path.join(root, session, `${seq}.json`);
    let mtime = 0;
    try {
      mtime = fs.statSync(file).mtimeMs;
    } catch {
      /* ignore */
    }
    if (!best) {
      best = rec;
      bestMtime = mtime;
      continue;
    }
    const rts = rec.ts ?? 0;
    const bts = best.ts ?? 0;
    if (rts > bts || (rts === bts && mtime > bestMtime)) {
      best = rec;
      bestMtime = mtime;
    }
  }
  return best;
}

export function loadSession(root, session) {
  const dir = path.join(root, session);
  if (!fs.existsSync(dir)) return [];
  const out = [];
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".json")).sort()) {
    const seq = f.replace(/\.json$/, "");
    const rec = readRecordFile(path.join(dir, f), `${session}/${seq}`, root);
    if (rec) out.push(rec);
  }
  return out;
}

export function readEntryById(root, id) {
  const parts = parseEntryId(id);
  if (!parts) return null;
  const file = path.join(root, parts.session, `${parts.seq}.json`);
  if (!fs.existsSync(file)) return null;
  return readRecordFile(file, id, root);
}

/** Delete a session directory under `root`, then GC now-orphaned blobs. */
export function rmSession(root, session) {
  fs.rmSync(path.join(root, session), { recursive: true, force: true });
  gcBlobs(root, listSessions, (r, s) => path.join(r, s));
}

/** Remove whole session directories without waiting for orphaned-blob GC. */
export function rmSessionFast(roots, session) {
  const touched = [];
  let removed = 0;
  for (const root of roots) {
    const dir = path.join(root, session);
    if (!fs.existsSync(dir)) continue;
    fs.rmSync(dir, { recursive: true, force: true });
    touched.push(root);
    removed++;
  }
  return { removed, touched };
}

/**
 * Delete one capture file (`<session>/<seq>.json`) under `root`, then GC blobs
 * that no remaining manifest references. Returns false when the file was
 * already absent.
 */
export function rmEntry(root, session, seq) {
  const file = path.join(root, session, `${seq}.json`);
  if (!fs.existsSync(file)) return false;
  fs.rmSync(file, { force: true });
  gcBlobs(root, listSessions, (r, s) => path.join(r, s));
  return true;
}

/** Delete `<session>/<seq>` from every read root. Returns how many roots held it. */
export function rmEntryMulti(roots, id) {
  const parts = parseEntryId(id);
  if (!parts) return 0;
  let removed = 0;
  for (const root of roots) {
    if (rmEntry(root, parts.session, parts.seq)) removed++;
  }
  return removed;
}

/**
 * Delete many `<session>/<seq>` ids in one pass. Files are removed first and
 * orphaned blobs are reclaimed once per affected root: going through `rmEntry`
 * per id would re-scan every manifest on disk for each row, which turns a
 * select-all delete of a few hundred rows into minutes of work.
 * Returns the ids that actually existed on disk.
 */
export function rmEntriesMulti(roots, ids) {
  const removed = [];
  const touched = new Set();
  for (const id of ids) {
    const parts = parseEntryId(id);
    if (!parts) continue;
    let hit = false;
    for (const root of roots) {
      const file = path.join(root, parts.session, `${parts.seq}.json`);
      if (!fs.existsSync(file)) continue;
      fs.rmSync(file, { force: true });
      hit = true;
      touched.add(root);
    }
    if (hit) removed.push(id);
  }
  for (const root of touched) gcBlobs(root, listSessions, (r, s) => path.join(r, s));
  return removed;
}

// Remove many ids without waiting for orphaned-blob GC. Used by the dashboard:
// file deletion is fast, while GC scans every manifest in the root and can take
// many seconds on a large capture directory. GC is scheduled after the HTTP
// response so the UI sees the deletion immediately.
export function rmEntriesMultiFast(roots, ids) {
  const removed = [];
  const touched = new Set();
  for (const id of ids) {
    const parts = parseEntryId(id);
    if (!parts) continue;
    let hit = false;
    for (const root of roots) {
      const file = path.join(root, parts.session, `${parts.seq}.json`);
      let exists = false;
      try {
        exists = fs.existsSync(file);
      } catch {
        exists = false;
      }
      if (!exists) continue;
      try {
        fs.rmSync(file, { force: true });
        hit = true;
        touched.add(root);
      } catch {
        /* leave the id out of the response when removal failed */
      }
    }
    if (hit) removed.push(id);
  }
  return { removed, touched: [...touched] };
}

export function scheduleBlobGc(roots, listSessions, sessionDir) {
  for (const root of roots) {
    gcBlobsAsync(root, listSessions, sessionDir).catch(() => {});
  }
}

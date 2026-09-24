// ccglass dashboard SPA. Vanilla JS, no build step.

const $ = (s) => document.querySelector(s);
const el = (tag, props = {}, ...kids) => {
  const n = Object.assign(document.createElement(tag), props);
  for (const k of kids) n.append(k);
  return n;
};
const esc = (s) => String(s ?? "").replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
const fmt = (n) => (n == null ? "—" : n.toLocaleString());
const fmtMs = (ms) => {
  if (ms == null) return "—";
  if (ms < 1000) return `${ms}ms`;
  if (ms < 60_000) return `${(ms / 1000).toFixed(ms >= 10_000 ? 1 : 2)}s`;
  return `${(ms / 60_000).toFixed(1)}m`;
};
const fmtTps = (n) => {
  if (n == null || !Number.isFinite(n)) return "—";
  if (n >= 100) return `${Math.round(n)} Token/秒`;
  if (n >= 10) return `${n.toFixed(1)} Token/秒`;
  return `${n.toFixed(2)} Token/秒`;
};

// Mirrors src/tokens.js estimateTokens: CJK about 1.12 token/char, others about
// 4.6 chars/token, calibrated 2026-09-24 against captured Codex traffic.
// Labelled ≈ because the upstream bill is only attached to the whole response.
// Keep these two numbers in step with src/tokens.js.
const ESTIMATE_CJK_WEIGHT = 1.12;
const ESTIMATE_ASCII_CHARS_PER_TOKEN = 4.6;
function estimateTokens(text) {
  if (!text) return 0;
  const s = String(text);
  const cjk = (s.match(/[㐀-鿿豈-﫿぀-ヿ]/g) || []).length;
  const rest = s.length - cjk;
  return Math.ceil(cjk * ESTIMATE_CJK_WEIGHT + rest / ESTIMATE_ASCII_CHARS_PER_TOKEN);
}

function messageTokenTag(text) {
  const n = estimateTokens(text);
  return `<span class="tag est" title="这条消息正文的粗估，不是上游账单。中文约 1.12 token/字，其余约 4.6 字符/token。">≈ ${fmt(n)}</span>`;
}

function statusClass(status) {
  if (status == null) return "pending";
  if (status < 400) return "ok";
  if (status < 500) return "4xx";
  return "5xx";
}

function groupRetries(entries, windowMs = 60_000) {
  const out = [];
  for (const e of entries) {
    const g = out[out.length - 1];
    const lastTs = g?.retries?.at(-1)?.ts ?? g?.ts;
    if (g && g.url === e.url && g.model === e.model && g.nMessages === e.nMessages && (e.ts - lastTs) < windowMs) {
      g.retries.push(e);
    } else {
      out.push({ ...e, retries: [] });
    }
  }
  return out;
}

const LIVE = "__live__"; // sentinel value for state.selected meaning "live stream view"

const state = {
  session: null, live: null, entries: [], sessionStats: null, sessionModels: [],
  modelFilter: "all",
  selected: null, tab: "overview", diff: false, picks: [], errorsOnly: false,
  summary: false, summaryTab: "byModel", usage: null,
  // Left-history management: checkbox mode + rows ticked for batch delete
  manage: false, checks: new Set(),
  // Live-stream state — populated only while #detail shows the live timeline
  liveSeen: new Map(),     // stepKey -> true (dedup across entries)
  liveToolRows: new Map(), // callId -> DOM element of the tool_use row
  livePinned: true,        // auto-scroll to bottom unless user scrolled up
};

function entryModel(e) {
  return e.model ?? null;
}

function entriesForModelFilter(entries, modelFilter = state.modelFilter) {
  if (!modelFilter || modelFilter === "all") return entries;
  return entries.filter((e) => entryModel(e) === modelFilter);
}

/** Union of models from live entries and last API snapshot (entries win for SSE). */
function collectSessionModels() {
  const set = new Set(state.sessionModels);
  for (const e of state.entries) {
    const m = entryModel(e);
    if (m) set.add(m);
  }
  return [...set].sort();
}

function visibleEntries() {
  let visible = entriesForModelFilter(state.entries);
  if (state.errorsOnly) {
    visible = visible.filter((e) => {
      const sc = statusClass(e.status);
      return sc === "4xx" || sc === "5xx" || e.error != null;
    });
  }
  return visible;
}

function clearDetailIfHidden() {
  if (!state.selected) return;
  if (state.selected === LIVE) return; // Live view always remains valid
  if (visibleEntries().some((e) => e.id === state.selected)) return;
  state.selected = null;
  state.picks = [];
  $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
}

function sessionStatsQuery() {
  const q = new URLSearchParams({ session: state.session });
  if (state.modelFilter && state.modelFilter !== "all") q.set("model", state.modelFilter);
  return q.toString();
}

async function api(path) {
  const r = await fetch(path, { cache: "no-store" });
  return r.json();
}

// ---- sessions + list -----------------------------------------------------

async function refreshSessions({ initial = false } = {}) {
  const { sessions, live } = await api("/api/sessions");
  const previousLive = state.live;
  const previousSession = state.session;
  const followLive = initial || state.selected === LIVE || !state.session || state.session === previousLive;
  state.live = live;
  const sel = $("#session");
  sel.innerHTML = "";
  for (const s of sessions) {
    sel.append(el("option", { value: s, textContent: s + (s === live ? "  (实时)" : "") }));
  }
  if (followLive && live) state.session = live;
  else if (!state.session || !sessions.includes(state.session)) state.session = sessions[0] || null;
  if (state.session) sel.value = state.session;
  $("#live").classList.toggle("off", !live);
  if (initial || state.session !== previousSession) await loadList();
}

async function loadSessions() {
  await refreshSessions({ initial: true });
  // Default the dashboard to the Live stream view on first load — most users
  // want to watch traffic, not pick from a list of HTTP rounds.
  if (!state.selected) onPick(LIVE);
}

async function loadList() {
  if (!state.session) return;
  const session = encodeURIComponent(state.session);
  const [{ entries }, stats] = await Promise.all([
    api("/api/requests?session=" + session),
    api("/api/session-stats?" + sessionStatsQuery()),
  ]);
  state.entries = entries;
  applySessionStats(stats);
  renderModelFilter();
  renderSessionStats();
  renderLatencyTrend();
  renderList();
}

function applySessionStats(stats) {
  if (stats.error) {
    state.sessionStats = null;
    state.sessionModels = [];
    return;
  }
  state.sessionStats = stats;
  state.sessionModels = stats.models || [];
}

function renderModelFilter() {
  const sel = $("#modelFilter");
  const models = collectSessionModels();
  if (!models.length) {
    sel.hidden = true;
    state.modelFilter = "all";
    return;
  }
  const prev = state.modelFilter || "all";
  sel.innerHTML =
    `<option value="all">全部模型</option>` +
    models.map((m) => `<option value="${esc(m)}">${esc(m)}</option>`).join("");
  sel.value = prev !== "all" && models.includes(prev) ? prev : "all";
  if (sel.value !== state.modelFilter) state.modelFilter = sel.value;
  sel.hidden = false;
}

function renderSessionStats() {
  const box = $("#sessionStats");
  const s = state.sessionStats;
  if (!s || !state.session) {
    box.hidden = true;
    box.innerHTML = "";
    return;
  }
  box.hidden = false;
  const pct = Math.round((s.cacheHitRate || 0) * 100);
  const scope =
    state.modelFilter !== "all"
      ? `<span class="scope">${esc(state.modelFilter)}</span>`
      : "";
  box.innerHTML =
    scope +
    `<span><b>≈${fmt(s.estTotal)}</b> 预估合计</span>` +
    `<span><b>${fmt(s.actualTotal ?? s.totalInput + s.totalOutput)}</b> 实际合计</span>` +
    `<span><b>${fmt(s.totalInput)}</b> 输入</span>` +
    `<span><b>${fmt(s.totalOutput)}</b> 输出</span>` +
    `<span><b>${pct}%</b> 缓存</span>` +
    `<span><b>$${(s.totalUsd || 0).toFixed(4)}</b></span>`;
}

function renderLatencyTrend() {
  const box = $("#latencyTrend");
  const scoped = entriesForModelFilter(state.entries);
  const done = scoped.filter((e) => e.latencyMs != null);
  if (!done.length && !scoped.some((e) => e.pending)) {
    box.hidden = true;
    box.innerHTML = "";
    return;
  }
  const max = Math.max(...done.map((e) => e.latencyMs), 1);
  const avg = done.length ? done.reduce((a, e) => a + e.latencyMs, 0) / done.length : 0;
  const bars = scoped.map((e) => {
    const h = e.latencyMs != null ? Math.max(4, Math.round((e.latencyMs / max) * 100)) : 8;
    const title = e.latencyMs != null
      ? `#${e.seq} ${esc(e.model || "?")} ${fmtMs(e.latencyMs)}`
      : `#${e.seq} ${esc(e.model || "?")} 进行中`;
    const cls = e.latencyMs != null ? "bar" : "bar pending";
    return `<div class="${cls}" style="height:${h}%" title="${title}"></div>`;
  }).join("");
  const modelNote =
    state.modelFilter !== "all" ? ` · ${esc(state.modelFilter)}` : "";
  box.hidden = false;
  box.innerHTML =
    `<div class="title">延迟趋势${modelNote}</div>` +
    `<div class="bars">${bars}</div>` +
    `<div class="meta">平均 ${fmtMs(Math.round(avg))} · 最大 ${fmtMs(max)} · ${done.length}/${scoped.length} 已完成</div>`;
}

function updateErrorsBtn() {
  const pool = entriesForModelFilter(state.entries);
  const count = pool.filter((e) => {
    const sc = statusClass(e.status);
    return sc === "4xx" || sc === "5xx" || e.error != null;
  }).length;
  const btn = $("#errorsBtn");
  btn.textContent = `错误 (${count})`;
  btn.classList.toggle("on", state.errorsOnly);
}

// ---- left-history deletion ----------------------------------------------

// A collapsed retry row stands for its head plus every retry child, so ticking
// (or deleting) it must cover the whole chain — otherwise the hidden retries
// survive and reappear as new rows.
function rowIds(e) {
  return [e.id, ...(e.retries || []).map((r) => r.id)];
}

// Every id the current list view can reach: head rows plus their retry chains.
function selectableIds() {
  return groupRetries(visibleEntries()).flatMap(rowIds);
}

function updateManageControls() {
  const manageBtn = $("#manageBtn");
  manageBtn.textContent = "管理：" + (state.manage ? "开启" : "关闭");
  manageBtn.classList.toggle("on", state.manage);

  const ids = selectableIds();
  // Only rows that actually render a checkbox may stay ticked; retry children
  // and rows filtered out of the list are dropped so the count always matches
  // what the user can see.
  const selectable = new Set(ids);
  for (const id of [...state.checks]) if (!selectable.has(id)) state.checks.delete(id);

  const allChecked = ids.length > 0 && ids.every((id) => state.checks.has(id));

  const selectAll = $("#selectAllBtn");
  selectAll.hidden = !state.manage;
  selectAll.disabled = ids.length === 0;
  selectAll.textContent = `${allChecked ? "取消全选" : "全选"} (${ids.length})`;
  selectAll.classList.toggle("on", allChecked);

  const invertBtn = $("#invertBtn");
  invertBtn.hidden = !state.manage;
  invertBtn.disabled = ids.length === 0;

  const delSelected = $("#deleteSelectedBtn");
  delSelected.hidden = !state.manage;
  delSelected.disabled = state.checks.size === 0;
  delSelected.textContent = `删除选中 (${state.checks.size})`;

  const delSession = $("#deleteSessionBtn");
  delSession.hidden = !state.manage;
  delSession.disabled = !state.session;
}

// Tick every listed request, or clear them all when everything is already
// ticked, so the button behaves as a single toggle.
function toggleSelectAll() {
  const ids = selectableIds();
  if (!ids.length) return;
  const allChecked = ids.every((id) => state.checks.has(id));
  for (const id of ids) {
    if (allChecked) state.checks.delete(id);
    else state.checks.add(id);
  }
  renderList();
}

// Invert the tick state of every listed request.
function invertSelection() {
  const ids = selectableIds();
  if (!ids.length) return;
  for (const id of ids) {
    if (state.checks.has(id)) state.checks.delete(id);
    else state.checks.add(id);
  }
  renderList();
}

async function deleteEntry(id, chain = [id]) {
  const label = String(id).split("/").slice(-1)[0];
  const extra = chain.length - 1;
  const what = extra > 0 ? `请求 #${label}（含 ${extra} 条重试）` : `请求 #${label}`;
  if (!window.confirm(`删除${what}？该抓包记录会从磁盘移除，且无法撤销。`)) return false;
  const r = await fetch("/api/delete-batch", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ ids: chain }),
  });
  const body = await r.json().catch(() => ({}));
  if (!r.ok) { window.alert("删除失败：" + (body.error || r.status)); return false; }
  const gone = new Set(body.deleted || []);
  const removedEntries = state.entries.filter((e) => gone.has(e.id));
  for (const gid of gone) state.checks.delete(gid);
  state.entries = state.entries.filter((e) => !gone.has(e.id));
  state.checks.clear();
  if (state.selected && gone.has(state.selected)) {
    state.selected = null;
    $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
  }
  renderList();
  refreshAfterDelete(gone, removedEntries);
  if (state.summary) loadUsage();
  return true;
}

async function deleteSelected() {
  const ids = [...state.checks];
  if (!ids.length) return;
  if (!window.confirm(`删除已勾选的 ${ids.length} 条请求？该操作无法撤销。`)) return;

  // One batch request: the server removes every file and reclaims orphaned
  // blobs once. Deleting row-by-row would re-scan the whole store per row,
  // which is minutes of work for a select-all on a large session.
  let removed = [];
  let failed = 0;
  try {
    const r = await fetch("/api/delete-batch", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ ids }),
    });
    const body = await r.json().catch(() => ({}));
    if (!r.ok) {
      window.alert("删除失败：" + (body.error || r.status));
      return;
    }
    removed = body.deleted || [];
    failed = ids.length - removed.length;
  } catch (e) {
    window.alert("删除失败：" + e.message);
    return;
  }

  const gone = new Set(removed);
  const removedEntries = state.entries.filter((e) => gone.has(e.id));
  state.entries = state.entries.filter((e) => !gone.has(e.id));
  for (const id of gone) state.checks.delete(id);
  if (state.selected && gone.has(state.selected)) state.selected = null;

  if (failed) window.alert(`${failed} 条未找到或已删除，其余已删除。`);
  if (!state.selected) $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
  renderList();
  refreshAfterDelete(gone, removedEntries);
  if (state.summary) loadUsage();
}

// Deleting files is immediate; recomputing a large session's stats is not.
// Fold the removed summaries out of the current header first, then refresh in
// the background so the list never appears to "undo" a successful deletion.
function refreshAfterDelete(gone, removedEntries) {
  if (state.sessionStats) {
    const removedUsage = (removedEntries || []).filter((e) => e.usage);
    if (removedUsage.length) {
      const s = state.sessionStats;
      let totalInput = s.totalInput || 0;
      let totalOutput = s.totalOutput || 0;
      let totalUsd = s.totalUsd || 0;
      let estTotal = s.estTotal || 0;
      let completed = s.completed || 0;
      for (const e of removedUsage) {
        totalInput = Math.max(0, totalInput - (e.usage.input || 0));
        totalOutput = Math.max(0, totalOutput - (e.usage.output || 0));
        totalUsd = Math.max(0, totalUsd - (e.usage.usd || 0));
        estTotal = Math.max(0, estTotal - (e.usage.estInput || 0) - (e.usage.estOutput || 0));
        completed = Math.max(0, completed - 1);
      }
      state.sessionStats = { ...s, totalInput, totalOutput, totalUsd, estTotal, completed,
        actualTotal: totalInput + totalOutput };
      renderSessionStats();
    }
  }
  setTimeout(() => loadSessionStatsQuiet().catch(() => {}), 0);
}

async function deleteSession() {
  const session = state.session;
  if (!session) return;
  if (!window.confirm(`删除整个会话 ${session} 及其全部请求？该操作无法撤销。`)) return;
  const r = await fetch("/api/delete?session=" + encodeURIComponent(session), { method: "DELETE" });
  const body = await r.json().catch(() => ({}));
  if (!r.ok) { window.alert("删除失败：" + (body.error || r.status)); return; }
  state.checks.clear();
  state.entries = [];
  state.selected = null;
  $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
  await refreshSessions();
  await loadList();
  if (state.summary) loadUsage();
}

function renderList() {
  updateErrorsBtn();
  updateManageControls();
  const list = $("#list");
  list.innerHTML = "";
  // Sticky "Live" entry — always at top, opens the streaming timeline.
  const liveRow = el("div", { className: "live-entry" + (state.selected === LIVE ? " sel" : "") + (state.live ? "" : " off") });
  liveRow.append(
    el("div", { className: "top" },
      el("span", { className: "dot" }),
      el("span", { textContent: state.live ? "实时流" : "流式视图（离线）" })),
    el("div", { className: "sub", textContent: state.live ? "所有轮次会按发生顺序追加" : "从顶部到底部回放已保存轮次" })
  );
  liveRow.onclick = () => onPick(LIVE);
  list.append(liveRow);
  const visible = visibleEntries();
  const grouped = groupRetries(visible);
  for (const e of grouped) {
    const sc = e.error ? "5xx" : statusClass(e.status);
    const rowClass = ["row", sc === "4xx" ? "status-4xx" : sc === "5xx" ? "status-5xx" : ""].filter(Boolean).join(" ");
    const row = el("div", { className: rowClass });
    if (e.id === state.selected) row.classList.add("sel");
    if (state.picks.includes(e.id)) row.classList.add("pick");
    const statusTxtClass = sc === "4xx" ? "status-txt-4xx" : sc === "5xx" ? "status-txt-5xx" : (e.pending ? "pending" : "");
    const statusText = e.error ? "传输错误" : (e.pending ? "进行中..." : "HTTP " + e.status);
    const sub = el("div", { className: "sub" },
      el("span", { className: "time", textContent: e.ts ? new Date(e.ts).toLocaleTimeString() : "" }),
      e.latencyMs != null ? el("span", { className: "latency", textContent: ` ${fmtMs(e.latencyMs)}` }) : null,
      usageBits(e.usage) ? el("span", { className: "latency", textContent: " " + usageBits(e.usage) + " · " }) : null,
      el("span", { textContent: ` ${e.format ? e.format + " · " : ""}${e.nMessages} 条消息 · ${e.nTools} 个工具 · ` }),
      el("span", { className: statusTxtClass, textContent: statusText }));
    if (e.nToolUse) sub.append(el("span", { className: "toolcalls", title: "本请求中的工具调用数", textContent: ` 🔧${e.nToolUse}` }));
    if (e.retries.length) sub.append(el("span", { className: "retry-badge", textContent: ` 已重试 ×${e.retries.length}` }));
    row.append(
      el("div", { className: "top" },
        el("span", { className: "seq", textContent: "#" + e.seq }),
        el("span", { textContent: e.model || "—" }),
        state.manage
          ? el("input", {
              type: "checkbox", className: "row-check",
              title: e.retries.length
                ? `勾选以批量删除（含 ${e.retries.length} 条重试）`
                : "勾选以批量删除",
              checked: rowIds(e).every((id) => state.checks.has(id)),
              onclick: (ev) => {
                ev.stopPropagation();
                for (const id of rowIds(e)) {
                  if (ev.target.checked) state.checks.add(id);
                  else state.checks.delete(id);
                }
                updateManageControls();
              },
            })
          : null,
        state.manage
          ? el("button", {
              className: "row-del danger", textContent: "删除",
              title: e.retries.length ? `删除这条请求（含 ${e.retries.length} 条重试）` : "删除这条请求",
              onclick: (ev) => { ev.stopPropagation(); deleteEntry(e.id, rowIds(e)); },
            })
          : null),
      sub
    );
    row.onclick = () => { if (!state.manage) onPick(e.id); };
    list.append(row);
  }
}

function onPick(id) {
  if (state.summary) {
    state.summary = false;
    updateSummaryBtn();
  }
  if (state.diff && id !== LIVE) {
    state.picks = state.picks.includes(id) ? state.picks.filter((x) => x !== id) : [...state.picks, id].slice(-2);
    if (state.picks.length === 2) renderDiff();
    renderList();
    return;
  }
  state.selected = id;
  renderList();
  if (id === LIVE) renderLive();
  else loadDetail(id);
}

// ---- detail --------------------------------------------------------------

async function loadDetail(id) {
  const rec = await api("/api/request/" + encodeURIComponent(id));
  state.detail = rec;
  renderDetail();
}

const TABS = ["overview", "flow", "system", "messages", "tools", "response", "headers"];
const TAB_LABELS = {
  overview: "概览",
  flow: "流程",
  system: "系统",
  messages: "消息",
  tools: "工具",
  response: "响应",
  headers: "请求头",
};

function renderDetail() {
  const rec = state.detail;
  const d = $("#detail");
  d.innerHTML = "";
  const tabs = el("div", { className: "tabs" });
  for (const t of TABS) {
    const tab = el("div", { className: "tab" + (t === state.tab ? " on" : ""), textContent: TAB_LABELS[t] || t });
    tab.onclick = () => { state.tab = t; renderDetail(); };
    tabs.append(tab);
  }
  d.append(tabs);
  const pane = el("div", { className: "pane" });
  pane.innerHTML = paneHtml(rec, state.tab);
  const curlBtn = pane.querySelector("[data-copy-curl]");
  if (curlBtn) curlBtn.onclick = () => copyCurl(rec, curlBtn);
  d.append(pane);
}

const CURL_SKIP_HEADERS = new Set([
  "connection", "keep-alive", "proxy-connection", "transfer-encoding",
  "upgrade", "te", "trailers", "accept-encoding", "content-length", "host",
]);

function resolveRequestUrl(req) {
  const raw = req?.url || "/";
  if (/^https?:\/\//i.test(raw)) return raw;
  const headers = req?.headers || {};
  const host = headers.host || headers.Host;
  if (!host) return raw;
  const h = String(Array.isArray(host) ? host[0] : host);
  const proto = /^(127\.|localhost|\[::1\])/i.test(h) ? "http" : "https";
  return `${proto}://${h}${raw.startsWith("/") ? raw : `/${raw}`}`;
}

function shellQuote(s) {
  return `'${String(s).replace(/'/g, `'\\''`)}'`;
}

function buildCurl(rec) {
  const req = rec.request || {};
  const method = (req.method || "GET").toUpperCase();
  const parts = [`curl -sS -X ${method}`, shellQuote(resolveRequestUrl(req))];
  for (const [k, v] of Object.entries(req.headers || {})) {
    if (CURL_SKIP_HEADERS.has(k.toLowerCase())) continue;
    const val = Array.isArray(v) ? v.join(", ") : v;
    if (val == null || val === "") continue;
    parts.push(`-H ${shellQuote(`${k}: ${val}`)}`);
  }
  if (req.body != null && method !== "GET" && method !== "HEAD") {
    const body = typeof req.body === "string" ? req.body : JSON.stringify(req.body);
    parts.push(`-d ${shellQuote(body)}`);
  }
  return parts.join(" \\\n  ");
}

async function copyCurl(rec, btn) {
  const text = buildCurl(rec);
  try {
    await navigator.clipboard.writeText(text);
    const prev = btn.textContent;
    btn.textContent = "已复制";
    setTimeout(() => { btn.textContent = prev; }, 1200);
  } catch {
    window.prompt("复制 cURL：", text);
  }
}

function paneHtml(rec, tab) {
  const parsed = rec.parsed || {};
  const view = parsed.view || { system: [], messages: [], tools: [] };
  if (tab === "overview") return overviewHtml(rec, parsed, view);
  if (tab === "flow") return flowHtml(rec);
  if (tab === "system") return blocksHtml(view.system);
  if (tab === "messages") return messagesHtml(view.messages);
  if (tab === "tools") return toolsHtml(view.tools);
  if (tab === "response") return responseHtml(parsed.response);
  if (tab === "headers") return blockEl("请求头", JSON.stringify(rec.request?.headers || {}, null, 2));
  return "";
}

function overviewHtml(rec, parsed, view) {
  const c = parsed.cost || {};
  const u = parsed.response?.usage || {};
  const est = rec.estimate || {};
  const t = rec.timing || {};
  const body = rec.request?.body || {};
  const status = rec.response?.status ?? null;
  const sc = statusClass(status);
  const dlLabels = { raw: "原始", md: "Markdown", json: "JSON", har: "HAR" };
  const dl = (f) => `<a class="dl" href="/api/export?id=${encodeURIComponent(rec.id)}&format=${f}">⬇ ${dlLabels[f] || f}</a>`;
  const lat = rec.latencyMs != null ? fmtMs(rec.latencyMs) : "—";
  const ttft = t.ttftMs != null ? fmtMs(t.ttftMs) : "—";
  const gen = t.genMs != null ? fmtMs(t.genMs) : "—";
  const statusCardCls = sc === "5xx" ? "err-card" : sc === "4xx" ? "warn-card" : "";
  const statusCardVal = status != null ? "HTTP " + status : "—";
  const errBody = parsed.response?.error ?? rec.response?.error ?? null;
  const errHtml = errBody
      ? `<div class="block" style="border-color:var(--del)"><div class="h" style="color:var(--del)">错误</div><pre style="color:var(--del)">${esc(typeof errBody === "string" ? errBody : JSON.stringify(errBody, null, 2))}</pre></div>`
    : "";
  return `
    <div class="overview-section">延迟</div>
    <div class="cards">
      ${card("总耗时", lat, undefined, "timing-card")}
      ${card("首字延迟", ttft, "首字节", "timing-card")}
      ${card("生成耗时", gen, "流式窗口", "timing-card")}
      ${card("输入速度", fmtTps(t.inTps), "首字节前", "timing-card")}
      ${card("输出速度", fmtTps(t.outTps), "首字节后", "timing-card")}
    </div>
    <div class="overview-section">请求</div>
    <div class="cards">
      ${statusCardCls ? card("状态", statusCardVal, undefined, statusCardCls) : ""}
      ${card("格式", parsed.format || rec.format || "—")}
      ${card("模型", body.model || "—")}
      ${card("预估合计", "≈" + fmt(est.total ?? parsed.estTokens), "输入+输出 Token")}
      ${card("实际合计", fmt(est.actualTotal ?? ((u.input_tokens || 0) + (u.output_tokens || 0))), "输入+输出 Token")}
      ${card("实际输入", fmt(u.input_tokens), "Token")}
      ${card("实际输出", fmt(u.output_tokens), "Token")}
      ${card("缓存读取", fmt(c.cacheRead), (Math.round((c.cacheHitRate || 0) * 100)) + "% 命中")}
      ${card("缓存写入", fmt(c.cacheWrite), "Token")}
      ${card("费用", "$" + (c.usd || 0).toFixed(5))}
      ${card("停止原因", parsed.response?.stop_reason || "—")}
    </div>
    ${errHtml}
    <div class="export-row">${dl("raw")}${dl("md")}${dl("json")}${dl("har")}<button type="button" class="dl copy-curl" data-copy-curl>复制 cURL</button></div>
    <div class="block"><div class="h">请求行</div><pre>${esc(rec.request?.method)} ${esc(rec.request?.url)}</pre></div>
    <p style="color:var(--muted)">${view.system.length} 个系统块 · ${view.messages.length} 条消息 · ${view.tools.length} 个工具</p>`;
}

function card(k, v, sub, cls = "") {
  return `<div class="card${cls ? " " + cls : ""}"><div class="k">${esc(k)}</div><div class="v">${esc(v)}${sub ? ` <small>${esc(sub)}</small>` : ""}</div></div>`;
}

function usageBits(usage) {
  if (!usage) return "";
  const input = usage.input ?? usage.input_tokens;
  const output = usage.output ?? usage.output_tokens;
  if (input == null && output == null) return "";
  const cache = usage.cacheRead ?? usage.cache_read_input_tokens ?? 0;
  let text = "输入 " + fmt(input || 0) + " · 输出 " + fmt(output || 0);
  if (cache) text += " · 缓存 " + fmt(cache);
  return text;
}

function usageFromParsed(rec) {
  const u = rec.parsed?.response?.usage;
  if (!u || (u.input_tokens == null && u.output_tokens == null)) return null;
  return {
    input: u.input_tokens,
    output: u.output_tokens,
    cacheRead: rec.parsed?.cost?.cacheRead ?? u.cache_read_input_tokens ?? 0,
  };
}

function requestUsageCards(rec) {
  const u = rec.parsed?.response?.usage;
  const c = rec.parsed?.cost || {};
  const input = u?.input_tokens;
  const output = u?.output_tokens;
  if (input == null && output == null) return "";
  return '<div class="overview-section">本轮 Token</div><div class="cards">' +
    card("输入", fmt(input), "Token") +
    card("输出", fmt(output), "Token") +
    card("缓存读取", fmt(c.cacheRead), "Token") +
    card("费用", "$" + Number(c.usd || 0).toFixed(5)) +
    "</div>";
}

function blockEl(label, text, tags = "") {
  return `<div class="block"><div class="h"><span>${esc(label)}</span><span>${tags}</span></div>${preBody(text)}</div>`;
}

function blocksHtml(blocks) {
  if (!blocks.length) return `<p style="color:var(--muted)">无</p>`;
  return blocks.map((b) => blockEl(b.label, b.text, b.cache ? '<span class="tag cache">缓存 1 小时</span>' : "")).join("");
}

// A short, stable hue from a tool-call id so a tool_use and its matching
// tool_result share the same colored stripe and id chip.
function idHue(id) {
  let h = 0;
  for (const ch of String(id)) h = (h * 31 + ch.charCodeAt(0)) % 360;
  return h;
}

// Long bodies fold into a <details> toggle so the history stays scannable.
// The summary reports the line count; CSS swaps "▸ show N lines" ⇄ "▾ hide"
// as it opens/closes — a plain show/hide toggle, no JS wiring needed.
function preBody(text) {
  const t = text || "";
  const lines = t.split("\n").length;
  const long = t.length > 800 || lines > 18;
  if (!long) return `<pre>${esc(t)}</pre>`;
  return `<details class="fold"><summary><span class="more show">▸ 展开 ${lines} 行</span><span class="more hide">▾ 收起</span></summary><pre>${esc(t)}</pre></details>`;
}

function messagesHtml(messages) {
  if (!messages.length) return `<p style="color:var(--muted)">无</p>`;
  return messages.map((m) => {
    const tags = [];
    if (m.cache) tags.push('<span class="tag cache">缓存 1 小时</span>');
    if (m.type === "tool_use") tags.push(`<span class="tag tool">🔧 ${esc(m.name || "tool_use")}</span>`);
    else if (m.type === "tool_result") tags.push(`<span class="tag ${m.isError ? "err" : "result"}">↳ ${m.isError ? "错误" : "结果"}</span>`);
    else if (m.type && m.type !== "text" && m.type !== "message") tags.push(`<span class="tag tool">${esc(m.type)}</span>`);
    const paired = m.type === "tool_use" || m.type === "tool_result";
    if (paired && m.callId) {
      const hue = idHue(m.callId);
      tags.push(`<span class="tag id" style="background:hsl(${hue} 60% 28%);color:hsl(${hue} 70% 82%)">${esc(String(m.callId).slice(-8))}</span>`);
    }
    const stripe = paired && m.callId ? ` style="border-left:3px solid hsl(${idHue(m.callId)} 60% 45%)"` : "";
    return `<div class="block"${stripe}><div class="h"><span>${esc(m.label)}</span><span>${tags.join("")}</span></div>${preBody(m.text)}</div>`;
  }).join("");
}

function toolsHtml(tools) {
  if (!tools.length) return `<p style="color:var(--muted)">无</p>`;
  return tools.map((t) =>
    `<div class="block"><div class="h"><span>${esc(t.name)}</span></div>` +
    preBody(`${t.description || ""}\n\n— schema —\n${JSON.stringify(t.schema || {}, null, 2)}`) +
    `</div>`
  ).join("");
}

function responseHtml(r) {
  if (!r) return `<p style="color:var(--muted)">未捕获到响应</p>`;
  let html = blockEl("用量", JSON.stringify(r.usage || {}, null, 2), r.streamed ? '<span class="tag tool">流式</span>' : "");
  for (const b of r.content || []) {
    const label = b.type === "tool_use" ? `tool_use: ${b.name}` : b.type;
    const text = b.type === "tool_use" ? JSON.stringify(b.input, null, 2) : (b.text ?? b.thinking ?? JSON.stringify(b));
    html += blockEl(label, text);
  }
  if (r.error) html += blockEl("错误", JSON.stringify(r.error, null, 2));
  return html;
}

// ---- flow: conversation-level sequence diagram ---------------------------
// Reconstructs the agent loop from the parsed messages[] (the full history the
// model was sent) plus this request's response (the model's latest decision,
// not yet folded back into messages). Each tool_use is paired with its
// tool_result by call_id and shares a color, so you can read: model picks a
// tool → CLI executes it locally → result is sent back → model picks again.

const FLOW_ICON = {
  user: "▸", assistant: "✎", thinking: "✻",
  tool_use: "⚙", skill: "🧩", tool_result: "↳", stop: "■",
  system: "▣", tools: "🛠",
};

function oneLine(t, n = 100) {
  const s = String(t ?? "").replace(/\s+/g, " ").trim();
  return s.length > n ? s.slice(0, n) + "…" : s;
}

// A Skill tool_use input is { skill, args } — pull the skill name out of it.
function skillName(text) {
  try { const o = JSON.parse(text); return o.skill || o.name || ""; } catch { return ""; }
}

// `request: true` includes everything else the client sent — system prompt
// blocks and the tools array — in prompt order (system → tools → messages),
// so the live stream reflects the full request, not just the conversation.
function flowSteps(rec, { request = false, requestMessages = true, requestToolResults = requestMessages } = {}) {
  const parsed = rec.parsed || {};
  const steps = [];
  if (request) {
    for (const s of parsed.view?.system || []) {
      steps.push({ kind: "system", label: s.label, text: s.text || "" });
    }
    const tools = parsed.view?.tools || [];
    if (tools.length) {
      steps.push({
        kind: "tools",
        count: tools.length,
        text: tools.map((t) => t.name + (t.description ? " — " + oneLine(t.description, 120) : "")).join("\n"),
      });
    }
  }
  if (requestMessages || requestToolResults) {
    for (const m of parsed.view?.messages || []) {
      if (m.type === "tool_result") {
        // A tool_result is a tool/function OUTPUT (OpenAI function_call_output
        // shows up on the *next* request), not prompt context — keep it even
        // when the request side is suppressed (Codex) so it can merge into the
        // prior turn's pending tool row and reveal the command output.
        if (!requestToolResults) continue;
        steps.push({ kind: "tool_result", callId: m.callId, isError: m.isError, text: m.text });
        continue;
      }
      if (!requestMessages) continue;
      if (m.type === "tool_use") {
        const isSkill = m.name === "Skill";
        steps.push({ kind: isSkill ? "skill" : "tool_use", name: isSkill ? skillName(m.text) || "skill" : m.name, callId: m.callId, text: m.text });
      } else if (m.type === "thinking") {
        steps.push({ kind: "thinking", text: m.text });
      } else {
        steps.push({ kind: m.role === "assistant" ? "assistant" : "user", text: m.text });
      }
    }
  }
  // The reply to THIS request lives in the response, not yet in messages[].
  const r = parsed.response;
  let emittedResponse = false;
  if (r && Array.isArray(r.content)) {
    for (const b of r.content) {
      if (b.type === "tool_use") {
        const isSkill = b.name === "Skill";
        steps.push({ kind: isSkill ? "skill" : "tool_use", name: isSkill ? (b.input?.skill || "skill") : b.name, callId: b.id, text: JSON.stringify(b.input ?? {}, null, 2), latest: true });
      } else if (b.type === "thinking") {
        steps.push({ kind: "thinking", text: b.thinking ?? "", latest: true });
      } else {
        steps.push({ kind: "assistant", text: b.text ?? "", latest: true });
      }
      emittedResponse = true;
    }
    if (r.stop_reason) { steps.push({ kind: "stop", text: r.stop_reason }); emittedResponse = true; }
  }
  // A failed turn carries no content array (API error body, or a non-2xx with
  // nothing to reassemble). Emit a terminal row so the turn stays visible —
  // critical in the live view, where the request side may be suppressed (Codex)
  // and the entry would otherwise disappear entirely.
  if (!emittedResponse) {
    const status = rec.response?.status;
    const err = r?.error;
    if (err || (status && status >= 400)) {
      const msg = err?.message || err?.type || (typeof err === "string" ? err : "");
      // callId keys this row per-turn so two turns that fail with the *same*
      // error aren't deduped into one (which would re-hide the second failure).
      steps.push({ kind: "stop", callId: "resp-error|" + (rec.id ?? rec.seq ?? ""), text: `错误${status ? " " + status : ""}${msg ? ": " + oneLine(msg, 140) : ""}` });
    }
  }
  return steps;
}

function flowHtml(rec) {
  const steps = flowSteps(rec);
  if (!steps.length) return `<p style="color:var(--muted)">没有消息</p>`;
  const tools = rec.parsed?.view?.tools || [];
  const menu = tools.length
    ? `<details class="fold toolmenu"><summary><span class="more show">🛠 提供给模型的 ${tools.length} 个工具</span><span class="more hide">🛠 收起工具菜单</span></summary><pre>${esc(tools.map((t) => t.name).join("\n"))}</pre></details>`
    : "";

  const rows = steps.map((s) => {
    const paired = s.kind === "tool_use" || s.kind === "skill" || s.kind === "tool_result";
    const hue = s.callId ? ` style="--hue:${idHue(s.callId)}"` : "";
    const tags = [];
    if (s.kind === "skill") tags.push('<span class="tag skill">技能</span>');
    if (s.kind === "tool_result") tags.push(`<span class="tag ${s.isError ? "err" : "result"}">${s.isError ? "错误" : "成功"}</span>`);
    if (s.callId) tags.push(`<span class="tag id">${esc(String(s.callId).slice(-6))}</span>`);
    if (s.kind === "user" || s.kind === "assistant") tags.push(messageTokenTag(s.text));
    if (s.latest) tags.push('<span class="tag latest">本轮</span>');
    const title =
      s.kind === "tool_use" ? `工具调用 → <b>${esc(s.name || "")}</b>` :
      s.kind === "skill" ? `技能调用 → <b>${esc(s.name || "")}</b>` :
      s.kind === "tool_result" ? "工具结果 ↩ 已在本地执行" :
      s.kind === "stop" ? `停止原因：${esc(s.text)}` :
      s.kind === "thinking" ? "思考" :
      s.kind === "user" ? "用户" :
      s.kind === "assistant" ? "助手" :
      s.kind === "system" ? "系统" :
      s.kind === "tools" ? "工具" : s.kind;
    const body = s.kind === "stop" ? "" :
      `<details class="fold step-body"><summary><span class="prev">${esc(oneLine(s.text))}</span></summary><pre>${esc(s.text)}</pre></details>`;
    return `<div class="step ${s.kind}${paired ? " indent" : ""}"${hue}>` +
      `<span class="dot">${FLOW_ICON[s.kind] || "•"}</span>` +
      `<div class="node"><div class="lead">${title}${tags.join("")}</div>${body}</div></div>`;
  }).join("");

  return `<div class="flow">${requestUsageCards(rec)}${menu}<div class="timeline">${rows}</div></div>`;
}

// ---- diff ----------------------------------------------------------------

async function renderDiff() {
  const [a, b] = state.picks;
  const diff = await api(`/api/diff?a=${encodeURIComponent(a)}&b=${encodeURIComponent(b)}`);
  const d = $("#detail");
  d.innerHTML = "";
  const pane = el("div", { className: "pane" });
  if (diff.error) { pane.innerHTML = `<p>${esc(diff.error)}</p>`; d.append(pane); return; }
  const c = diff.counts;
  pane.innerHTML =
    `<div class="cards">
      ${card("新增", "+" + c.added, "块")}
      ${card("删除", "−" + c.removed, "块")}
      ${card("未变化", c.common, "块")}
      ${card("B 中命中缓存", c.cachedInB, "块")}
     </div>
     <p style="color:var(--muted)">正在对比 <b>${esc(a)}</b> → <b>${esc(b)}</b>（后一次请求 B 对比早一次请求 A）</p>` +
    `<div class="diff-section add">＋ B 中新增（本轮新上下文）</div>` +
    (diff.added.map((x) => diffBlock(x, "add")).join("") || `<p style="color:var(--muted)">没有新增内容</p>`) +
    `<div class="diff-section del">− 相比 A 删除</div>` +
    (diff.removed.map((x) => diffBlock(x, "del")).join("") || `<p style="color:var(--muted)">没有删除内容</p>`);
  d.append(pane);
}

function diffBlock(x, kind) {
  const tag = x.cache ? '<span class="tag cache">缓存</span>' : "";
  return `<div class="block diff-${kind}"><div class="h"><span>${esc(x.label)}</span><span>${tag}</span></div><pre>${esc((x.text || "").slice(0, 4000))}</pre></div>`;
}

// ---- summary: cross-session usage rollup ---------------------------------
// Renders /api/usage (totals + per-model + per-session) as a takeover in
// #detail, peer to the Diff view. Scoped to the current project's roots — see
// readRoots() in src/paths.js — so it rolls up every capture under this cwd,
// not other ccglass projects.

const usd = (n) => "$" + Number(n || 0).toFixed(4);
const pct = (r) => Math.round((r || 0) * 100) + "%";

async function loadUsage() {
  let next;
  try {
    // Names require scanning the agent's transcripts, so only ask for them on
    // the tab that shows them (by session). The default by-model and the
    // by-timestamp tabs skip the scan entirely.
    const q = state.summaryTab === "bySession" ? "?names=1" : "";
    next = await api("/api/usage" + q);
  } catch (err) {
    next = { error: String(err?.message || err) };
  }
  // Race guard: user may have toggled Summary off mid-fetch. Drop the result
  // so we don't clobber #detail with stale rollup data.
  if (!state.summary) return;
  state.usage = next;
  renderSummary();
}

function renderSummary() {
  const d = $("#detail");
  d.innerHTML = "";
  const u = state.usage;
  if (!u) { d.innerHTML = '<div class="empty">正在加载...</div>'; return; }
  if (u.error) { d.innerHTML = `<div class="empty">加载用量失败：${esc(u.error)}</div>`; return; }
  if (!u.sessionCount) { d.innerHTML = '<div class="empty">当前项目还没有捕获到会话。</div>'; return; }

  const t = u.totals;
  const range = [u.range?.from, u.range?.to].filter(Boolean).map((s) => new Date(s).toLocaleString()).join(" \u2192 ") || "\u2014";
  const unmeasured = u.unmeasured ? `${u.unmeasured} 条未计量` : undefined;
  // Estimated total vs the provider's own bill. `actualTotal` counts gross input
  // (uncached + cached + cache write) plus output, so it is the number the
  // estimate should track.
  const deviation = Number(t.estDeviation || 0);
  const deviationText = (deviation >= 0 ? "+" : "") + (deviation * 100).toFixed(1) + "%";
  const estSub = `实际 ${fmt(t.actualTotal)} · 偏差 ${deviationText}`;
  const cardsHtml = `
    <div class="overview-section">共 ${fmt(u.sessionCount)} 个会话的合计</div>
    <div class="cards">
      ${card("会话数", fmt(u.sessionCount))}
      ${card("请求数", fmt(u.requestCount), unmeasured)}
      ${card("预估合计", "≈" + fmt(t.estTotal), estSub)}
      ${card("实际合计", fmt(t.actualTotal), "输入+输出 Token")}
      ${card("实际输入", fmt(t.totalInput), "含缓存 Token")}
      ${card("实际输出", fmt(t.output), "Token")}
      ${card("缓存读取", fmt(t.cacheRead), pct(t.cacheHitRate) + " 命中")}
      ${card("缓存写入", fmt(t.cacheWrite), "Token")}
      ${card("费用", usd(t.usd))}
    </div>
    <p style="color:var(--muted)">时间范围：${esc(range)}</p>`;

  const subTabs = [["byModel", "按模型"], ["bySession", "按会话"], ["byTimestamp", "按时间"]];
  const tabsHtml = `<div class="tabs">` + subTabs.map(([id, label]) =>
    `<div class="tab${id === state.summaryTab ? " on" : ""}" data-stab="${id}">${label}</div>`
  ).join("") + `</div>`;

  // by session: name + timestamp id; by timestamp: raw id only (mirrors the
  // CLI's --by-session vs --by-timestamp).
  const body = state.summaryTab === "bySession"
    ? bySessionHtml(u.bySession)
    : state.summaryTab === "byTimestamp"
      ? bySessionHtml(u.bySession, { showName: false })
      : byModelHtml(u.byModel);

  d.innerHTML = `${tabsHtml}<div class="pane">${cardsHtml}<div class="summary-body">${body}</div></div>`;
  d.querySelectorAll(".tab[data-stab]").forEach((node) => {
    node.onclick = () => {
      state.summaryTab = node.dataset.stab;
      renderSummary();
      // Names are fetched lazily; pull them when the user opens the by-session
      // tab (other tabs render from the already-loaded rollup).
      if (state.summaryTab === "bySession") loadUsage();
    };
  });
}

function byModelHtml(rows) {
  if (!rows?.length) return `<p style="color:var(--muted)">没有可计量的请求</p>`;
  const head = `<tr><th>模型</th><th class="n">请求</th><th class="n">预估合计</th><th class="n">实际合计</th><th class="n">输入</th><th class="n">输出</th><th class="n">缓存命中</th><th class="n">费用</th></tr>`;
  const body = rows.map((r) =>
    `<tr><td>${esc(r.model)}</td><td class="n">${fmt(r.requests)}</td><td class="n">≈${fmt(r.estTotal)}</td><td class="n">${fmt(r.actualTotal)}</td><td class="n">${fmt(r.totalInput)}</td><td class="n">${fmt(r.output)}</td><td class="n">${pct(r.cacheHitRate)}</td><td class="n">${usd(r.usd)}</td></tr>`
  ).join("");
  return `<table class="usage-table"><thead>${head}</thead><tbody>${body}</tbody></table>`;
}

function bySessionHtml(rows, { showName = true } = {}) {
  if (!rows?.length) return `<p style="color:var(--muted)">没有会话</p>`;
  const nameHead = showName ? `<th>名称</th>` : "";
  const head = `<tr>${nameHead}<th>会话</th><th class="n">请求</th><th class="n">预估合计</th><th class="n">实际合计</th><th class="n">输入</th><th class="n">输出</th><th class="n">缓存命中</th><th class="n">费用</th></tr>`;
  const body = rows.map((r) => {
    const nameCell = showName ? `<td>${esc(r.name || "—")}</td>` : "";
    return `<tr>${nameCell}<td>${esc(r.session)}</td><td class="n">${fmt(r.requests)}</td><td class="n">≈${fmt(r.estTotal)}</td><td class="n">${fmt(r.actualTotal)}</td><td class="n">${fmt(r.totalInput)}</td><td class="n">${fmt(r.output)}</td><td class="n">${pct(r.cacheHitRate)}</td><td class="n">${usd(r.usd)}</td></tr>`;
  }).join("");
  return `<table class="usage-table"><thead>${head}</thead><tbody>${body}</tbody></table>`;
}

function updateSummaryBtn() {
  const btn = $("#summaryBtn");
  btn.textContent = "汇总：" + (state.summary ? "开启" : "关闭");
  btn.classList.toggle("on", state.summary);
}

// SSE-driven entries arrive while Summary is open; reload the rollup
// (debounced) so totals don't go stale during a live session.
let usageReloadTimer = null;
function scheduleUsageReload() {
  if (!state.summary) return;
  clearTimeout(usageReloadTimer);
  usageReloadTimer = setTimeout(() => { if (state.summary) loadUsage(); }, 500);
}

// ---- live stream view ----------------------------------------------------
// Single-column timeline rendered into #detail. Non-Codex entries include the
// client request in prompt order (system, tools, messages); Codex entries show
// only the model response so the live pane does not echo the in-flight request.
// Steps are deduped across entries by callId/length+prefix, and tool_use rows
// merge with matching tool_result rows when both sides are present.

function smartSummary(step) {
  if (step.kind === "tool_result") {
    let inner = String(step.text || "");
    try {
      const o = JSON.parse(inner);
      if (Array.isArray(o)) inner = o.map((x) => typeof x === "string" ? x : (x?.text ?? JSON.stringify(x))).join("\n");
      else if (typeof o === "object" && o) inner = o.text ?? JSON.stringify(o);
    } catch { /* not JSON */ }
    return oneLine(inner, 140);
  }
  if (step.kind === "stop") return step.text || "";
  if (step.kind === "tool_use" || step.kind === "skill") {
    let input = {};
    try { input = JSON.parse(step.text); } catch { /* not JSON */ }
    const name = step.name || "";
    if (name === "Bash") return oneLine(input.command, 140);
    if (name === "Read") {
      const loc = input.file_path || "";
      const rng = input.offset != null ? `:${input.offset}${input.limit ? `-${input.offset + input.limit}` : ""}` : "";
      return loc + rng;
    }
    if (name === "Edit" || name === "Write" || name === "NotebookEdit") return oneLine(input.file_path, 140);
    if (name === "Grep") return [input.pattern && `"${input.pattern}"`, input.path].filter(Boolean).join(" 于 ");
    if (name === "Glob") return input.pattern || "";
    if (name === "WebFetch" || name === "WebSearch") return oneLine(input.url || input.query, 140);
    if (name === "Skill") return input.skill || input.name || "";
    if (name === "TaskCreate" || name === "TaskUpdate") return oneLine(input.subject || input.description, 140);
    if (name === "AskUserQuestion") return oneLine(input.questions?.[0]?.question, 140);
    if (/sql|query|exec/i.test(name)) return oneLine(input.sql || input.query || input.statement, 140);
    const firstScalar = Object.values(input).find((v) => typeof v === "string" || typeof v === "number");
    if (firstScalar != null) return oneLine(firstScalar, 140);
    return oneLine(step.text, 140);
  }
  if (step.kind === "tools") return `向模型提供了 ${step.count} 个工具`;
  return oneLine(step.text, 200);
}

function liveStepKey(s) {
  if (s.callId) return s.kind + "|" + s.callId;
  // Length is part of the key so a block that changes anywhere (not just in
  // its first 200 chars) re-appears in the stream instead of being deduped.
  const t = String(s.text || "");
  return s.kind + "|" + t.length + "|" + t.slice(0, 200);
}

// Tool name → category (file/shell/search/web/task/agent/plan/q&a/cron/notify/mcp)
function toolCategory(name) {
  if (!name) return null;
  if (name.startsWith("mcp__")) return "mcp";
  if (/^(Read|Edit|Write|MultiEdit|NotebookEdit)$/.test(name)) return "file";
  if (/^(Bash|BashOutput|KillShell)$/.test(name)) return "shell";
  if (/^(Grep|Glob|LS)$/.test(name)) return "search";
  if (/^(WebFetch|WebSearch)$/.test(name)) return "web";
  if (/^Task(Create|Update|Get|List|Output|Stop)$/.test(name)) return "task";
  if (/^Agent$/.test(name)) return "agent";
  if (/^Skill$/.test(name)) return "skill";
  if (/^(EnterPlanMode|ExitPlanMode)$/.test(name)) return "plan";
  if (/^AskUserQuestion$/.test(name)) return "ask";
  if (/^(ScheduleWakeup|CronCreate|CronDelete|CronList)$/.test(name)) return "cron";
  if (/^PushNotification$/.test(name)) return "notify";
  if (/^TodoWrite$/.test(name)) return "task";
  return null;
}

// Recognize common envelope patterns in flow steps and return pattern tags.
// These are passive labels — they don't filter, just classify, so you can scan
// the stream and see "ah, this user row is a system-reminder, not a real input".
const PAT_DETECTORS = [
  // ---- user-side text envelopes ----------------------------------------
  { kinds: ["user"], match: (t) => /^<command-name>|^<command-message>|^<command-args>/m.test(t), tag: "slash" },
  { kinds: ["user"], match: (t) => /<local-command-stdout>/.test(t), tag: "cmd-out" },
  { kinds: ["user"], match: (t) => /<user-prompt-submit-hook>|<session-start-hook>|<post-tool-use-hook>|<stop-hook>/.test(t), tag: "hook" },
  { kinds: ["user"], match: (t) => /<system-reminder>/.test(t), tag: "reminder" },
  { kinds: ["user"], match: (t) => /Caveat: The messages below were generated/i.test(t), tag: "caveat" },
  { kinds: ["user"], match: (t) => /\[Image #\d+\]|image_path=|<channel source="(imessage|telegram)"/.test(t), tag: "image" },
  { kinds: ["user"], match: (t) => /Contents of \/.+CLAUDE\.md|Codebase and user instructions are shown below|# auto memory|# currentDate|# userEmail/.test(t), tag: "memory" },
  { kinds: ["user"], match: (t) => /Previous Conversation Compacted|This session is being continued|<auto-compact-summary>|stepped away and is coming back|Recap in under \d+ words|recap.*1-2 plain sentences/i.test(t), tag: "recap" },
  // Skill invocation/return — appears as user-role text in Claude Code
  { kinds: ["user"], match: (t) => /^Launching skill:|^Base directory for this skill:/m.test(t), tag: "skill-load" },
  // ---- assistant-side text -----------------------------------------------
  { kinds: ["assistant"], match: (t, s) => s.text && s.text.length === 0, tag: "empty" },
];

function detectPatterns(step) {
  const out = [];
  const t = String(step.text || "");
  for (const d of PAT_DETECTORS) {
    if (!d.kinds.includes(step.kind)) continue;
    try { if (d.match(t, step)) out.push(d.tag); } catch { /* skip */ }
  }
  if (step.kind === "tool_use" || step.kind === "skill") {
    const cat = toolCategory(step.name);
    if (cat) out.push(cat);
  }
  return out;
}

// Rich tag metadata. `headline` is shown as the popover title; `desc` is a 2-4
// sentence explanation rendered in the popover body. `doc` adds an "Open docs"
// footer link. The popover replaces the native title tooltip entirely.
const TAG_INFO = {
  // ---- pattern tags: user-side envelopes -------------------------------
  reminder: {
    headline: "system-reminder",
    desc: "这是一个 <system-reminder> 块：CLI 向用户消息位置注入了引导内容来影响模型（例如“考虑使用任务工具”“保持简洁”“自动模式已启用”）。这不是用户输入的，而是客户端框架的插桩信息。模型会被训练为重视这类提示，因此它们虽然正常聊天界面里看不到，却会影响行为。",
  },
  hook: {
    headline: "钩子输出",
    desc: "来自 Claude Code 钩子的输出：用户配置的 Shell 命令会在生命周期事件触发时执行（会话开始、提交用户提示、每次工具调用后、停止时等）。钩子打印到标准输出的内容会作为合成的用户角色消息注入。模型会把它当作用户输入，因此行为异常的钩子可能实际影响智能体的走向。",
    doc: "https://docs.claude.com/en/docs/claude-code/hooks",
  },
  slash: {
    headline: "斜杠命令",
    desc: "用户输入了类似 /skill-name、/clear 或 /help 的斜杠命令。CLI 在发送给模型前会把它解析成结构化封套（<command-name>、<command-message>、<command-args>），正文里看到的就是这个封套。",
    doc: "https://docs.claude.com/en/docs/claude-code/slash-commands",
  },
  "cmd-out": {
    headline: "本地命令输出",
    desc: "用户通过 ! 前缀内联执行的本地 Shell 命令的标准输出（例如 `!ls`）。CLI 会把它包进 <local-command-stdout> 标签，再作为用户角色上下文回传给模型。",
  },
  caveat: {
    headline: "来源提示",
    desc: "当内容来自旁路工具（例如通过 /edit 修改文件）而不是助手时，CLI 会在前面加上“Caveat: The messages below were generated by the user while running local commands”。它标记了内容来源的边界。",
  },
  memory: {
    headline: "记忆上下文",
    desc: "CLI 自动加载的上下文：CLAUDE.md 文件（项目级与用户级）、环境信息（当前目录、操作系统、Git 分支）、当前日期、用户邮箱等。它会引导每个会话，通常放在第一条用户消息里，这也解释了为什么第一轮会很大。",
    doc: "https://docs.claude.com/en/docs/claude-code/memory",
  },
  recap: {
    headline: "回顾摘要",
    desc: "一条合成消息，要求模型压缩或复述此前的状态。常见触发有两种：(1) 自动压缩：CLI 触及上下文窗口上限，把较早轮次浓缩成摘要，模型随后基于摘要而非完整历史继续；(2) 用户离开后又回来，客户端框架注入“回顾当前进度”的提示，帮助模型重新定位。",
  },
  image: {
    headline: "附带图片",
    desc: "用户附加了图片（截图、聊天频道照片、拖放文件等）。正文显示周边文字，图片本身会作为独立内容块一并发送。",
  },
  "skill-load": {
    headline: "技能已加载",
    desc: "某个技能的完整说明被放入对话中。加载后，技能内容会在本轮（有时更久）充当额外的系统级引导。通常会先有一次斜杠命令调用。",
    doc: "https://docs.claude.com/en/docs/claude-code/skills",
  },
  empty: {
    headline: "空内容块",
    desc: "一个不含任何字符的文本内容块。通常无害，属于模型输出的小异常。",
  },
  // ---- pattern tags: tool categories ------------------------------------
  file: {
    headline: "文件操作",
    desc: "Read / Edit / Write / MultiEdit / NotebookEdit：模型正在读写磁盘文件。成功调用后，正文会显示文件内容。",
  },
  shell: {
    headline: "Shell 命令",
    desc: "Bash：模型在本地执行了一条 Shell 命令。标题显示命令，正文显示标准输出（和标准错误）以及退出码。",
  },
  search: {
    headline: "代码库搜索",
    desc: "Grep（按正则搜索文件内容）或 Glob（按文件名模式匹配）。模型正在浏览代码库，输出通常是带行号的少量匹配结果。",
  },
  web: {
    headline: "网络访问",
    desc: "WebFetch（加载 URL 并总结）或 WebSearch（查询搜索引擎）。模型通过外部网络获取上下文。",
  },
  task: {
    headline: "任务跟踪",
    desc: "TaskCreate / TaskUpdate / TaskList / TodoWrite：模型正在为多步骤工作管理自己的待办列表。可在 CLI 的加载动画中看到。",
  },
  agent: {
    headline: "子智能体",
    desc: "通过 Agent 工具派生了专用子智能体。子智能体在独立上下文中运行，最后只返回一条摘要消息，适合并行探索且不污染主上下文。",
    doc: "https://docs.claude.com/en/docs/claude-code/sub-agents",
  },
  skill: {
    headline: "技能",
    desc: "通过 Skill 工具调用了某个 Claude 技能。技能说明会被加载，模型随后按该工作流执行。",
    doc: "https://docs.claude.com/en/docs/claude-code/skills",
  },
  plan: {
    headline: "规划模式",
    desc: "EnterPlanMode / ExitPlanMode：模型处于先规划模式，必须先给出实施方案并得到用户同意，然后才能写代码。复杂功能中很常见。",
  },
  ask: {
    headline: "用户提问",
    desc: "AskUserQuestion：模型暂停执行，向用户提出选择题。用户回答前，对话无法继续。",
  },
  cron: {
    headline: "定时任务",
    desc: "CronCreate / CronDelete / CronList / ScheduleWakeup：模型安排了一条未来提示。到点后客户端框架会重新触发该提示，恢复执行循环。",
  },
  notify: {
    headline: "通知",
    desc: "PushNotification：模型发送桌面端或手机端通知以提醒用户，通常用于长时间任务或受阻等待。",
  },
  mcp: {
    headline: "MCP 工具",
    desc: "Model Context Protocol：模型调用了外部 MCP 服务器提供的工具（例如 mcp__github__*、mcp__filesystem__*）。MCP 是 Claude Code 接入数据库、API、IDE 的方式。",
    doc: "https://docs.claude.com/en/docs/claude-code/mcp",
  },
  // ---- operational tags -------------------------------------------------
  ok: {
    headline: "成功",
    desc: "工具调用成功返回。正文显示模型收到的原始输出文本，模型接下来会基于它继续推理。",
  },
  err: {
    headline: "错误",
    desc: "工具报告了错误（非零退出码、异常、校验失败、拒绝执行等）。正文显示模型看到的错误文本，模型可能换一种方式重试，或把失败反馈给用户。",
  },
  pending: {
    headline: "等待中",
    desc: "模型请求了这次工具调用，但 tool_result 还没返回。可能是工具仍在本地运行（Shell 命令、网络请求），也可能这是所捕获链路中的最后一个动作，CLI 尚未发送下一次请求。",
  },
  latest: {
    headline: "本轮",
    desc: "这一步属于最近一次 HTTP 往返中助手的响应。之前的行来自历史对话的重建，这一行则是刚刚从网络传输中收到的。",
  },
  id: {
    headline: "调用 ID",
    desc: "模型请求工具时分配的调用 ID。ccglass 用它把 tool_use 行和对应的 tool_result 配对，两者共用同一条彩色左边条，便于横向对照阅读。",
  },
};

// Visible Chinese labels for tag keys. Protocol field names stay unchanged in
// TAG_INFO keys and data-tag-key; only the chip text is translated.
const TAG_LABELS = {
  reminder: "系统提醒",
  hook: "钩子输出",
  slash: "斜杠命令",
  "cmd-out": "命令输出",
  caveat: "来源提示",
  memory: "记忆上下文",
  recap: "回顾摘要",
  image: "图片",
  "skill-load": "技能加载",
  empty: "空块",
  file: "文件",
  shell: "Shell",
  search: "搜索",
  web: "网络",
  task: "任务",
  agent: "子智能体",
  skill: "技能",
  plan: "规划",
  ask: "提问",
  cron: "定时",
  notify: "通知",
  mcp: "MCP",
  ok: "成功",
  err: "错误",
  pending: "等待中",
  latest: "本轮",
  id: "调用ID",
};

// Render a tag chip. `name` is the lookup key in TAG_INFO; `label` is the
// visible text (defaults to the Chinese label, then the key). Popover content
// comes from TAG_INFO via data-tag-key — no native title attribute, so the
// rich popover is the only hover affordance.
function tagChip(name, extraClass = "", label = null) {
  const cls = "tag " + (extraClass ? extraClass + " " : "");
  const text = label ?? TAG_LABELS[name] ?? name;
  return `<span class="${cls}" data-tag-key="${esc(name)}">${esc(text)}</span>`;
}

// ---- tag popover ---------------------------------------------------------
// A single shared popover element shown on hover over any [data-tag-key].
// Body-level positioning means it works whether the tag is in the live pane,
// the classic detail, or anywhere else. Hovering the popover itself keeps it
// open so users can click the docs link.

(function setupTagPopover() {
  const el = document.createElement("div");
  el.className = "tag-popover";
  el.hidden = true;
  document.body.appendChild(el);

  let showT = null, hideT = null, current = null;

  function scheduleHide() {
    clearTimeout(hideT);
    hideT = setTimeout(() => { el.hidden = true; current = null; }, 150);
  }

  function show(target) {
    clearTimeout(hideT);
    if (current === target) return;
    clearTimeout(showT);
    showT = setTimeout(() => {
      const key = target.dataset.tagKey;
      const info = TAG_INFO[key];
      if (!info) return;
      el.innerHTML =
        `<div class="pop-head">${esc(info.headline || key)}</div>` +
        `<div class="pop-body">${esc(info.desc || "")}</div>` +
        (info.doc ? `<div class="pop-doc"><a href="${esc(info.doc)}" target="_blank" rel="noopener">查看文档 ↗</a></div>` : "");
      el.hidden = false;
      position(target);
      current = target;
    }, 200);
  }

  function position(target) {
    const r = target.getBoundingClientRect();
    // Reset to measure natural size
    el.style.left = "-9999px";
    el.style.top = "0px";
    const pr = el.getBoundingClientRect();
    let left = r.left;
    let top = r.bottom + 6;
    if (left + pr.width > window.innerWidth - 8) left = window.innerWidth - pr.width - 8;
    if (left < 8) left = 8;
    if (top + pr.height > window.innerHeight - 8) top = Math.max(8, r.top - pr.height - 6);
    el.style.left = left + "px";
    el.style.top = top + "px";
  }

  el.addEventListener("mouseenter", () => clearTimeout(hideT));
  el.addEventListener("mouseleave", scheduleHide);

  // Event delegation — any element with data-tag-key triggers
  document.addEventListener("mouseover", (e) => {
    const t = e.target.closest("[data-tag-key]");
    if (!t) return;
    show(t);
  });
  document.addEventListener("mouseout", (e) => {
    const t = e.target.closest("[data-tag-key]");
    if (!t) return;
    scheduleHide();
  });
  // Escape closes immediately
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") { el.hidden = true; current = null; } });
})();

function liveStepEl(step, { latestEntry = false } = {}) {
  const paired = step.kind === "tool_use" || step.kind === "skill" || step.kind === "tool_result";
  const hasBody = step.kind !== "stop" && (step.text != null && String(step.text).length > 0);

  const root = document.createElement(hasBody ? "details" : "div");
  root.className = "flowrow " + step.kind + (paired ? " paired" : "");
  // thinking/system/tools start collapsed — bulky, repeated context
  if (hasBody) root.open = !["thinking", "system", "tools"].includes(step.kind);
  if (step.callId) {
    root.style.setProperty("--hue", idHue(step.callId));
    root.dataset.callId = step.callId;
  }

  const tags = [];
  // Pattern tags first (left-most) — classify what kind of envelope this row is
  for (const p of detectPatterns(step)) tags.push(tagChip(p, `pat pat-${p}`));
  if (step.kind === "skill") tags.push(tagChip("skill", "skill"));
  if (step.kind === "tool_result") tags.push(tagChip(step.isError ? "err" : "ok", step.isError ? "err" : "ok"));
  if (step.callId) {
    const short = esc(String(step.callId).slice(-6));
    tags.push(`<span class="tag id" data-tag-key="id">${short}</span>`);
  }
  if (latestEntry && step.latest) tags.push(tagChip("latest", "latest", "本轮"));
  if (step.kind === "user" || step.kind === "assistant") tags.push(messageTokenTag(step.text));
  if (step.kind === "tool_use" || step.kind === "skill") {
    tags.push(`<span class="tag pending" data-tag-key="pending">等待中…</span>`);
  }

  const titleHtml =
    step.kind === "tool_use" ? `<b>${esc(step.name || "工具")}</b>` :
    step.kind === "skill" ? `<b>/${esc(step.name || "技能")}</b>` :
    step.kind === "tool_result" ? `<span style="color:var(--muted)">结果</span>` :
    step.kind === "stop" ? `<span style="color:var(--muted)">停止原因</span>` :
    step.kind === "thinking" ? `<span style="color:var(--muted)">思考</span>` :
    step.kind === "user" ? `<b>用户</b>` :
    step.kind === "assistant" ? `<b>助手</b>` :
    step.kind === "system" ? `<b>系统</b>` :
    step.kind === "tools" ? `<b>工具</b>` : `<span style="color:var(--muted)">${esc(step.kind)}</span>`;

  const sumText = smartSummary(step);
  const summaryHtml = (step.kind !== "stop" && sumText) ? `<span class="summary">${esc(sumText)}</span>` : "";
  const inlineHtml = step.kind === "stop" ? `<span class="inline">${esc(step.text || "")}</span>` : "";
  const toggleHtml = hasBody ? `<span class="toggle" aria-hidden="true"></span>` : "";

  const headHtml =
    `<span class="dot">${FLOW_ICON[step.kind] || "•"}</span>` +
    `<span class="lead">${titleHtml}${summaryHtml}${inlineHtml}${tags.join("")}${toggleHtml}</span>`;

  if (hasBody) {
    root.innerHTML = `<summary>${headHtml}</summary><pre class="body input-body">${esc(step.text || "")}</pre>`;
    if (step.kind === "tool_use" || step.kind === "skill") root.dataset.input = step.text || "";
  } else {
    root.innerHTML = headHtml;
  }
  return root;
}

function liveMergeResult(toolRow, resultStep) {
  toolRow.classList.add("has-output"); // CSS keeps the title-line summary visible (command/path) since it's now distinct from the body (output)
  const lead = toolRow.querySelector(".lead");
  if (lead) {
    const pending = lead.querySelector(".tag.pending");
    if (pending) pending.remove();
    const okErrKey = resultStep.isError ? "err" : "ok";
    const okErr = document.createElement("span");
    okErr.className = "tag " + okErrKey;
    okErr.textContent = okErrKey;
    okErr.dataset.tagKey = okErrKey;
    const tog = lead.querySelector(".toggle");
    if (tog) lead.insertBefore(okErr, tog); else lead.appendChild(okErr);
  }
  const oldBody = toolRow.querySelector(":scope > .body");
  if (oldBody) oldBody.remove();
  const output = document.createElement("pre");
  output.className = "body output-body";
  output.textContent = resultStep.text || "";
  toolRow.appendChild(output);
  const inputText = toolRow.dataset.input || "";
  if (inputText && inputText.trim() !== "{}" && inputText.length > 4) {
    const inputFold = document.createElement("details");
    inputFold.className = "input-fold";
    inputFold.innerHTML = `<summary>查看输入</summary><pre>${esc(inputText)}</pre>`;
    toolRow.appendChild(inputFold);
  }
}

function liveTurnSepEl(meta) {
  const div = document.createElement("div");
  div.className = "turn-sep";
  const errClass = meta.status && meta.status >= 400 ? " err" : "";
  const clock = meta.ts ? new Date(meta.ts).toTimeString().slice(0, 8) : "";
  div.innerHTML =
    `<span class="meta">` +
      `<b>第 ${meta.seq ?? ""} 轮</b>` +
      (meta.model ? `<span>${esc(meta.model)}</span>` : "") +
      (meta.latencyMs != null ? `<span>${fmtMs(meta.latencyMs)}</span>` : "") +
      (usageBits(meta.usage) ? `<span>${esc(usageBits(meta.usage))}</span>` : "") +
      (meta.status != null ? `<span class="${errClass.trim()}">${meta.status}</span>` : "") +
      (clock ? `<span>${clock}</span>` : "") +
    `</span>`;
  return div;
}

function liveBodyEl() {
  return $("#detail .live-pane .live-body");
}

function isCodexRecord(rec) {
  const model = rec.parsed?.response?.model || rec.request?.body?.model || rec.model || "";
  if (String(model).toLowerCase().includes("codex")) return true;
  // Codex CLI (codex_cli_rs) stamps its own user-agent/originator. That client
  // signature — not merely a /v1/responses URL — is what tells real Codex
  // traffic apart from a generic OpenAI Responses client, so we don't suppress
  // the latter's request side (prompt, tools, function-call outputs).
  const h = rec.request?.headers || {};
  const ua = String(h["user-agent"] || h.originator || "").toLowerCase();
  return ua.includes("codex");
}

function liveFlowSteps(rec) {
  const showRequest = !isCodexRecord(rec);
  // For Codex, hide prompt/system/tool-call context but keep tool_result rows:
  // the function_call_output arrives on the NEXT request and is what merges into
  // the prior turn's pending tool row, so dropping it would leave that row stuck
  // at "pending…" and hide the command/function output.
  return flowSteps(rec, { request: showRequest, requestMessages: showRequest, requestToolResults: true });
}

function liveAppendEntry(rec, { flash = false } = {}) {
  const body = liveBodyEl();
  if (!body) return;
  const steps = liveFlowSteps(rec);
  let appendedAny = false;
  for (const s of steps) {
    // tool_result: merge into existing tool_use row instead of new row
    if (s.kind === "tool_result" && s.callId && state.liveToolRows.has(s.callId)) {
      const mergeKey = "merged|" + s.callId;
      if (state.liveSeen.has(mergeKey)) continue;
      state.liveSeen.set(mergeKey, true);
      liveMergeResult(state.liveToolRows.get(s.callId), s);
      continue;
    }
    const k = liveStepKey(s);
    if (state.liveSeen.has(k)) continue;
    state.liveSeen.set(k, true);
    if (!appendedAny) {
      body.appendChild(liveTurnSepEl({
        seq: rec.seq, model: rec.parsed?.view?.model || rec.model,
        latencyMs: rec.latencyMs, status: rec.response?.status, ts: rec.ts ?? rec.startedAt,
        usage: rec.usage || usageFromParsed(rec),
      }));
      appendedAny = true;
    }
    const row = liveStepEl(s, { latestEntry: true });
    if (flash) row.classList.add("flash");
    body.appendChild(row);
    if ((s.kind === "tool_use" || s.kind === "skill") && s.callId) {
      state.liveToolRows.set(s.callId, row);
    }
  }
  if (state.livePinned) {
    const pane = $("#detail .live-pane");
    if (pane) {
      // Mark this as programmatic so the scroll handler doesn't mis-interpret
      // the follow-up scroll event as the user scrolling away from bottom.
      state.programmaticScrollAt = Date.now();
      pane.scrollTop = pane.scrollHeight;
    }
  }
}

async function renderLive() {
  state.liveSeen.clear();
  state.liveToolRows.clear();
  state.livePinned = true;

  const d = $("#detail");
  d.innerHTML =
    `<div class="live-pane">` +
      `<div class="live-toolbar">` +
        `<label><input type="checkbox" id="liveAutoScroll" checked /> 自动滚动</label>` +
        `<button id="liveExpandAll">全部展开</button>` +
        `<button id="liveCollapseAll">全部收起</button>` +
        `<span class="spacer"></span>` +
        `<span class="muted">轮次会实时追加 · 点击左侧请求可查看单次调用详情</span>` +
      `</div>` +
      `<div class="live-body"></div>` +
    `</div>`;

  const pane = $("#detail .live-pane");
  pane.addEventListener("scroll", () => {
    // Ignore scroll events fired by our own scrollTop assignment during
    // rapid appends — only react to genuine user scrolls.
    if (Date.now() - (state.programmaticScrollAt || 0) < 200) return;
    const nearBottom = pane.scrollHeight - pane.clientHeight - pane.scrollTop < 40;
    state.livePinned = nearBottom;
    const cb = $("#liveAutoScroll");
    if (cb) cb.checked = nearBottom;
  });
  $("#liveAutoScroll").onchange = (e) => { state.livePinned = e.target.checked; };
  $("#liveExpandAll").onclick = () => { for (const r of pane.querySelectorAll("details.flowrow")) r.open = true; };
  $("#liveCollapseAll").onclick = () => { for (const r of pane.querySelectorAll("details.flowrow")) r.open = false; };

  // Walk every entry in order, fetch its full record, append flow steps.
  const entries = entriesForModelFilter(state.entries).slice().sort((a, b) => (a.seq || 0) - (b.seq || 0));
  for (const e of entries) {
    try {
      const rec = await api("/api/request/" + encodeURIComponent(e.id));
      if (rec && !rec.error) liveAppendEntry(rec);
    } catch { /* skip on error */ }
  }
  if (state.livePinned) {
    state.programmaticScrollAt = Date.now();
    pane.scrollTop = pane.scrollHeight;
  }
}

// ---- live + wiring -------------------------------------------------------

let streamRetryTimer = null;

function connectStream() {
  const es = new EventSource("/api/stream");
  es.onmessage = async (ev) => {
    const s = JSON.parse(ev.data);
    // A deletion broadcast from another dashboard (or another tab) drops the
    // row locally instead of waiting for the next full session reload.
    if (s.deleted) {
      state.entries = state.entries.filter((e) => e.id !== s.deleted);
      state.checks.delete(s.deleted);
      if (state.selected === s.deleted) {
        state.selected = null;
        $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
      }
      renderList();
      loadSessionStatsQuiet();
      if (state.summary) scheduleUsageReload();
      return;
    }
    if (s.session !== (state.session || state.live)) {
      // A service restart creates a new capture session. Refresh the selector
      // before deciding whether this event belongs to the current view.
      try { await refreshSessions(); } catch { /* retry on the next poll */ }
      if (s.session !== (state.session || state.live)) return;
    }
    const i = state.entries.findIndex((e) => e.id === s.id);
    if (i >= 0) state.entries[i] = s;
    else state.entries.push(s);
    renderModelFilter();
    renderLatencyTrend();
    renderList();
    clearDetailIfHidden();
    if (state.selected === LIVE) {
      try {
        const rec = await api("/api/request/" + encodeURIComponent(s.id));
        if (rec && !rec.error) liveAppendEntry(rec, { flash: true });
      } catch { /* ignore */ }
    } else if (!state.summary && s.id === state.selected) {
      loadDetail(s.id);
    }
    if (!s.pending) loadSessionStatsQuiet();
    if (state.summary && !s.pending) scheduleUsageReload();
  };
  es.onerror = () => {
    es.close();
    if (streamRetryTimer) return;
    streamRetryTimer = setTimeout(() => {
      streamRetryTimer = null;
      connectStream();
    }, 1500);
  };
}

async function loadSessionStatsQuiet() {
  if (!state.session) return;
  const stats = await api("/api/session-stats?" + sessionStatsQuery());
  applySessionStats(stats);
  renderModelFilter();
  renderSessionStats();
}

$("#session").onchange = async (e) => {
  state.session = e.target.value;
  state.picks = [];
  state.modelFilter = "all";
  await loadList();
  if (state.selected === LIVE) renderLive();
};
$("#modelFilter").onchange = (e) => {
  state.modelFilter = e.target.value;
  loadSessionStatsQuiet();
  renderLatencyTrend();
  renderList();
  clearDetailIfHidden();
  if (state.selected === LIVE) renderLive();
};
$("#errorsBtn").onclick = () => { state.errorsOnly = !state.errorsOnly; renderList(); };
$("#manageBtn").onclick = () => {
  state.manage = !state.manage;
  if (!state.manage) state.checks.clear();
  renderList();
};
$("#selectAllBtn").onclick = () => { toggleSelectAll(); };
$("#invertBtn").onclick = () => { invertSelection(); };
$("#deleteSelectedBtn").onclick = () => { deleteSelected(); };
$("#deleteSessionBtn").onclick = () => { deleteSession(); };
$("#diffBtn").onclick = (e) => {
  state.diff = !state.diff;
  state.picks = [];
  e.target.textContent = "对比：" + (state.diff ? "请选择 2 条" : "关闭");
  e.target.classList.toggle("on", state.diff);
  // Diff and Summary both swap #detail \u2014 only one can be active.
  if (state.diff && state.summary) {
    state.summary = false;
    updateSummaryBtn();
    // Summary HTML is still in #detail; restore the per-request view (or
    // empty state) so the user isn't left staring at a stale rollup.
    if (state.selected === LIVE) renderLive();
    else if (state.selected) loadDetail(state.selected);
    else $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
  }
  renderList();
  if (!state.diff && state.selected) {
    if (state.selected === LIVE) renderLive();
    else loadDetail(state.selected);
  }
};
$("#summaryBtn").onclick = () => {
  state.summary = !state.summary;
  if (state.summary) {
    // Mirror image of the Diff toggle: turning Summary on cancels Diff.
    if (state.diff) {
      state.diff = false;
      state.picks = [];
      const db = $("#diffBtn");
      db.textContent = "对比：关闭";
      db.classList.remove("on");
      renderList();
    }
    updateSummaryBtn();
    // Drop the prior payload so renderSummary() falls through to "Loading…"
    // instead of flashing yesterday's totals before the fetch lands.
    state.usage = null;
    renderSummary();
    loadUsage();
  } else {
    updateSummaryBtn();
    if (state.selected === LIVE) renderLive();
    else if (state.selected) loadDetail(state.selected);
    else $("#detail").innerHTML = '<div class="empty">请选择一条请求，或开始在 Codex 中对话。</div>';
  }
};

const themeCtl = window.ccglassTheme?.initTheme?.();
const themeSelect = $("#themeSelect");
if (themeCtl && themeSelect) {
  themeSelect.value = themeCtl.getMode();
  themeSelect.onchange = () => themeCtl.setMode(themeSelect.value);
}

loadSessions().then(() => {
  connectStream();
  // Keep the session selector current even when the collector is restarted
  // while this dashboard page remains open.
  setInterval(() => refreshSessions().catch(() => {}), 2000);
});

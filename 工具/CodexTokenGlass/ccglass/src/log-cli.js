import fs from "node:fs";
import path from "node:path";
import { legacyRoot } from "./paths.js";
import { listSessions, hasCapturedLogs, readEntryByIdMulti, rmSession, rmEntryMulti, loadSession } from "./store.js";
import { renderExport } from "./export.js";
import { summarizeUsage } from "./usage.js";

export function exportEntry(id, opts) {
  if (!id) {
    process.stderr.write("ccglass export: missing entry id. Usage: ccglass export <session>/<seq>\n");
    process.exit(1);
  }
  const rec = readEntryByIdMulti(opts.readRoots, id);
  if (!rec) {
    process.stderr.write(`ccglass: no entry ${id}\n`);
    process.exit(1);
  }
  process.stdout.write(renderExport(rec, opts.format || "raw").body + "\n");
}

export function migrate(opts) {
  const cwd = process.cwd();
  const src = path.resolve(legacyRoot(cwd));
  const dest = path.resolve(opts.dir);

  if (!fs.existsSync(src)) {
    process.stderr.write(`ccglass migrate: no ./.ccglass in ${cwd}\n`);
    process.exit(1);
  }

  if (!hasCapturedLogs(src)) {
    process.stderr.write(`ccglass migrate: no .json logs in ./.ccglass (only empty session folders?)\n`);
    process.exit(1);
  }

  fs.mkdirSync(dest, { recursive: true });
  let files = 0;

  for (const session of listSessions(src)) {
    const srcDir = path.join(src, session);
    const destDir = path.join(dest, session);
    fs.mkdirSync(destDir, { recursive: true });
    for (const f of fs.readdirSync(srcDir)) {
      if (!f.endsWith(".json")) continue;
      const destFile = path.join(destDir, f);
      if (fs.existsSync(destFile)) continue;
      fs.copyFileSync(path.join(srcDir, f), destFile);
      files++;
    }
  }

  if (!files) {
    process.stderr.write(
      `ccglass migrate: no new files to copy (dest already has every ./.ccglass log from this project)\n` +
      `  dest: ${dest}\n`
    );
    process.exit(0);
  }

  process.stderr.write(
    `ccglass migrate: copied ${files} file(s) from ./.ccglass (${cwd}) → ${dest}\n` +
    `  (only logs under the current project's ./.ccglass; other directories are untouched.)\n`
  );
}

// `ccglass repack [session]` — force-migrate legacy records to v2 by reading them
// (reads auto-migrate in place). With no session, repacks every session.
export function repack(opts) {
  for (const root of opts.readRoots) {
    const sessions = listSessions(root);
    for (const s of sessions) {
      if (opts.session && s !== opts.session) continue;
      loadSession(root, s); // side effect: rewrites legacy files as v2
    }
  }
  process.stdout.write("ccglass: repack complete\n");
}

// `ccglass usage` — token + USD rollup across every captured session. Pretty-prints
// totals, top models by spend, and per-session breakdown. With `--format json`, emits
// the raw aggregator output for piping into jq.
export function usageCmd(opts) {
  // Resolve session names only for the `--by-session` table (not --by-timestamp,
  // which deliberately shows raw ids, and not the totals-only default view).
  const s = summarizeUsage(opts.readRoots, { names: opts.bySession && !opts.byTimestamp });

  if (opts.format === "json") {
    process.stdout.write(JSON.stringify(s, null, 2) + "\n");
    return;
  }

  if (!s.sessionCount) {
    process.stderr.write("ccglass usage：未找到已捕获的会话。\n");
    process.exit(1);
  }

  const fmt = (n) => Number(n || 0).toLocaleString();
  const usd = (n) => `$${Number(n || 0).toFixed(4)}`;
  const pct = (r) => `${Math.round((r || 0) * 100)}%`;
  const range = [s.range.from, s.range.to].filter(Boolean).join(" → ") || "—";

  const out = [];
  out.push(`ccglass 用量汇总 — ${s.sessionCount} 个会话，已计量 ${fmt(s.requestCount)} 个请求` +
    (s.unmeasured ? `（${s.unmeasured} 个未计量）` : ""));
  out.push(`  时间范围：${range}`);
  out.push("");
  out.push("合计：");
  const dev = (s.totals.estDeviation >= 0 ? "+" : "") + (s.totals.estDeviation * 100).toFixed(1) + "%";
  out.push(`  预估合计      ${fmt(s.totals.estTotal)}  （实际 ${fmt(s.totals.actualTotal)}，偏差 ${dev}）`);
  out.push(`  实际合计      ${fmt(s.totals.actualTotal)}`);
  out.push(`  输入          ${fmt(s.totals.input)}`);
  out.push(`  输出          ${fmt(s.totals.output)}`);
  out.push(`  输入(含缓存)  ${fmt(s.totals.totalInput)}`);
  out.push(`  缓存读取      ${fmt(s.totals.cacheRead)}  （命中率 ${pct(s.totals.cacheHitRate)}）`);
  out.push(`  缓存写入      ${fmt(s.totals.cacheWrite)}`);
  out.push(`  费用          ${usd(s.totals.usd)}`);

  if (s.byModel.length) {
    out.push("");
    out.push("按模型（按费用降序）：");
    const w = Math.max(8, ...s.byModel.map((m) => m.model.length));
    // Header uses fixed ASCII fields so the columns line up with the rows below;
    // the Chinese meaning of each column is given in the legend line.
    out.push("  （列：模型 请求数 输入 输出 缓存读取 缓存写入 费用）");
    out.push(`  ${"model".padEnd(w)}  ${"req".padStart(6)}  ${"input".padStart(10)}  ${"output".padStart(10)}  ${"cacheR".padStart(10)}  ${"cacheW".padStart(10)}  ${"cost".padStart(10)}`);
    for (const m of s.byModel) {
      out.push(`  ${m.model.padEnd(w)}  ${fmt(m.requests).padStart(6)}  ${fmt(m.input).padStart(10)}  ${fmt(m.output).padStart(10)}  ${fmt(m.cacheRead).padStart(10)}  ${fmt(m.cacheWrite).padStart(10)}  ${usd(m.usd).padStart(10)}`);
    }
  }

  if (opts.bySession && s.bySession.length) {
    out.push("");
    out.push("按会话（最新在前）：");
    // `--by-timestamp` shows only the raw timestamp id. Otherwise prepend a
    // `name` column (the agent's session title) while keeping the timestamp id
    // column, so sessions that share a title — e.g. ccglass restarted in the
    // same Claude conversation — stay distinguishable and remain usable with
    // `ccglass rm`/`export`. Cap names so a long first-prompt fallback can't
    // blow out the column (the full name stays in --format json).
    const showName = !opts.byTimestamp;
    const cap = (str) => (str.length > 48 ? str.slice(0, 47) + "…" : str);
    const nameOf = (x) => (x.name ? cap(x.name) : "—");
    const wId = Math.max(7, ...s.bySession.map((x) => x.session.length));
    const wName = showName ? Math.max(4, ...s.bySession.map((x) => nameOf(x).length)) : 0;
    // Left columns vary by mode; the numeric tail is identical for header + rows.
    const lead = (name, id) => (showName ? `${name.padEnd(wName)}  ${id.padEnd(wId)}` : id.padEnd(wId));
    const tail = (req, input, output, cacheR, cacheW, cost) =>
      `  ${req.padStart(6)}  ${input.padStart(10)}  ${output.padStart(10)}  ${cacheR.padStart(10)}  ${cacheW.padStart(10)}  ${cost.padStart(10)}`;
    out.push("  （列：名称 会话 请求数 输入 输出 缓存读取 缓存写入 费用）");
    const headerLead = showName ? `${"name".padEnd(wName)}  ${"session".padEnd(wId)}` : "session".padEnd(wId);
    out.push(`  ${headerLead}${tail("req", "input", "output", "cacheR", "cacheW", "cost")}`);
    for (const x of s.bySession) {
      out.push(`  ${lead(nameOf(x), x.session)}${tail(fmt(x.requests), fmt(x.input), fmt(x.output), fmt(x.cacheRead), fmt(x.cacheWrite), usd(x.usd))}`);
    }
  }

  process.stdout.write(out.join("\n") + "\n");
}

// `ccglass rm <session>` — delete a session across read roots and GC orphan blobs.
export function rmCmd(session, opts) {
  if (!session) {
    process.stderr.write("ccglass rm: usage: ccglass rm <session>\n");
    process.exit(1);
  }
  if (session !== path.basename(session) || session === "." || session === "..") {
    process.stderr.write(`ccglass rm: invalid session: ${session}\n`);
    process.exit(1);
  }
  let removed = 0;
  for (const root of opts.readRoots) {
    if (fs.existsSync(path.join(root, session))) { rmSession(root, session); removed++; }
  }
  if (!removed) {
    process.stderr.write(`ccglass rm: session not found: ${session}\n`);
    process.exit(1);
  }
  process.stdout.write(`ccglass: removed ${session}\n`);
}

// `ccglass rm-entry <session>/<seq> [...]` — delete individual captured requests
// across read roots, then GC orphaned blobs. Used by the dashboard's per-row and
// batch delete; exposed on the CLI so the same cleanup is scriptable.
export function rmEntryCmd(ids, opts) {
  if (!ids.length) {
    process.stderr.write("ccglass rm-entry: usage: ccglass rm-entry <session>/<seq> [...]\n");
    process.exit(1);
  }
  let removed = 0;
  let missing = 0;
  for (const id of ids) {
    if (rmEntryMulti(opts.readRoots, id)) {
      removed++;
      process.stdout.write(`ccglass: removed ${id}\n`);
    } else {
      missing++;
      process.stderr.write(`ccglass rm-entry: not found: ${id}\n`);
    }
  }
  process.stdout.write(`ccglass: removed ${removed} entr${removed === 1 ? "y" : "ies"}` +
    (missing ? `, ${missing} not found` : "") + "\n");
  // Signal failure to scripts when nothing was actually deleted (all ids
  // missing or malformed) so callers do not treat a no-op as success.
  if (!removed) process.exitCode = 1;
}

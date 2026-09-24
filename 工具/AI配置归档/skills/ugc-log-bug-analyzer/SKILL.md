---
name: ugc-log-bug-analyzer
description: Analyze the latest Oasis UGCRepository client, DS, and Tag logs by the auto-selected DebugID to find likely runtime bugs from printed evidence. Use when the user asks to analyze the latest logs, locate client or server errors, compare client and DS behavior, or infer the most likely root cause from UGCRepository logs.
---

# UGC Log Bug Analyzer

Use this skill for Oasis UGCRepository log triage.

## Default Workflow

1. Run `scripts/analyze_ugc_logs.ps1` with no arguments unless the user explicitly names a different log root path.
2. The script always auto-selects the newest session by `LastWriteTime` and uses a bounded per-file tail scan by default so large `FullLog` files do not time out.
3. Review the returned JSON and present the diagnosis in this order:
   - 会话概览
   - 高优先级问题
   - 关键证据
   - 疑似根因
   - 修复建议
   - 建议补充日志
4. Treat explicit Lua/runtime errors as highest priority.
5. Treat repeated `UGCLog.Log()` output, missing follow-up logs, and client/DS mismatch as suspicious signals rather than final proof.
6. If the result depends on API behavior, lifecycle, replication, or client/DS authority, query `oasis-combined-mcp` before finalizing the recommendation.
7. If the user names a subsystem or the default result is too broad, rerun with `-FocusKeyword` and a smaller `-MaxBytesPerFile` to collect focused evidence without scanning the entire `FullLog`.

## Script Behavior

- Default log root: `D:/WeGameApps/rail_apps/OasisEraEditor(2001776)/ShadowTrackerExtra/Saved/Logs/UGCRepository`
- Auto-detects the relevant `DebugID`; do not pass a DebugID manually
- Reads every matching `Clientlog/TagLog`, `Clientlog/LuaLog`, `Clientlog/FullLog`, and `DSlog/FullLog` file for the selected `DebugID`, but defaults to the newest 8 MiB window per file
- Use `-MaxBytesPerFile <bytes>` to widen or shrink the scan window; use `-FullScan` only when a complete scan is worth the time cost
- Reports `signals.scan_policy`, `scanned_bytes`, and `truncated` so the answer can state when evidence came from a tail window rather than a full file
- In truncated files, evidence uses `scan_line` plus `scan_start_offset`; absolute `line` is only present when the full file was scanned
- Supports `-FocusKeyword` for subsystem triage, such as passive equipment logs, while still reporting critical errors and warning/error evidence
- Clusters adjacent error keywords so one traceback is reported as one bug signal instead of several duplicate findings
- Reports partial-log sessions clearly when only one side is present and surfaces scanned-file coverage
- Adds `requires_mcp_confirmation` and `mcp_query_hints` when conclusions may depend on Oasis API, lifecycle, replication, or client/DS behavior
- Falls back to suspicious patterns and logging advice when no hard error is visible

## Command Examples

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1
```

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1 -Root 'D:\Custom\Logs\UGCRepository' -ContextLines 6
```

Focused scan for passive equipment evidence:

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1 -FocusKeyword '被动','装备','Passive','Equip' -MaxBytesPerFile 4194304
```

Full scan when the bounded window is insufficient:

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1 -FullScan
```

## Interpretation Rules

- Do not say “没问题” when no clear error is found; report the strongest suspicious patterns instead.
- Treat Lua exceptions, nil access, stack tracebacks, and script stack blocks as the highest-priority evidence.
- Treat shutdown / exit / teardown warnings as low-priority noise unless they line up with the user-visible bug time.
- When log lines are repeated in a tight loop, prefer state-transition logs over more copies of the same print.
- When the result points to API misuse or lifecycle mismatch, confirm the engine-side rule with `oasis-combined-mcp`.
- Keep logging advice narrow and practical: `require("Script.UGCLog")` plus `UGCLog.Log()` around entry, branch choice, return values, and state transitions.

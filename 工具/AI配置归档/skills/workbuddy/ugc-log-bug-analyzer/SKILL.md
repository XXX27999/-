---
name: ugc-log-bug-analyzer
description: Analyze Oasis UGCRepository client, DS, and Tag logs by DebugID, with targeted script-plus-function log lookup to minimize context. Use when the user asks to analyze latest logs, locate client or server errors, search a Lua/Blueprint script function's printed evidence, compare client and DS behavior, or infer likely runtime causes.
agent_created: true
---

# UGC Log Bug Analyzer

Use this skill for Oasis UGCRepository log triage.

## Default Workflow

1. If the user gives a script/function target, run targeted mode first with `-ScriptFunction 'ScriptName+FunctionName'`; do not open or paste the full log.
2. If the script/function target is unknown, identify it from project code or a small unique-tag search, then rerun targeted mode. Use the broad analyzer only when no target can be identified.
3. The script always auto-selects the newest session by `LastWriteTime` and uses a bounded per-file tail scan by default so large `FullLog` files do not time out.
4. Review the returned JSON and present the diagnosis in this order:
   - 会话概览
   - 高优先级问题
   - 关键证据
   - 疑似根因
   - 修复建议
   - 建议补充日志
5. Treat explicit Lua/runtime errors as highest priority.
6. Treat repeated `UGCLog.Log()` output, missing follow-up logs, and client/DS mismatch as suspicious signals rather than final proof.
7. If the result depends on API behavior, lifecycle, replication, or client/DS authority, query `oasis-combined-mcp` before finalizing the recommendation.
8. If the user names a script/function, keep `-ContextLines 0` or `1` unless surrounding state is required; return only the targeted samples, counts, timestamps, and scan policy.
9. If the user names a subsystem but no script/function, rerun with `-FocusKeyword` and a smaller `-MaxBytesPerFile` to collect focused evidence without dumping the entire `FullLog`.

## Script Behavior

- Default log root is inferred from the current workspace: `.../UGCProjects/<ProjectName>` maps to `.../Saved/Logs/<ProjectName>`.
- Run the analyzer with the target Oasis project as the working directory. Use `-Root` only to override automatic project-name resolution.
- Auto-detects the relevant `DebugID`; do not pass a DebugID manually
- Reads every matching `Clientlog/TagLog`, `Clientlog/LuaLog`, `Clientlog/FullLog`, and `DSlog/FullLog` file for the selected `DebugID`, but defaults to the newest 8 MiB window per file
- Use `-MaxBytesPerFile <bytes>` to widen or shrink the scan window; use `-FullScan` only when a complete scan is worth the time cost
- Supports `-ScriptFunction 'ScriptName+FunctionName'` (repeatable) for exact `【脚本名+函数名】` log targeting; `.lua` suffix and outer brackets are normalized
- Targeted mode returns only matching log samples, counts, timestamps, files, and scan policy; it skips global error/tag aggregation to keep output small
- Never use `Get-Content -Raw` or paste a complete `FullLog`; use targeted mode or bounded script searches instead
- Use `-ContextLines 0` for exact matching lines only; use `1` or `2` only when adjacent state transitions are needed
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

Targeted script/function scan (preferred):

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1 -ScriptFunction 'Pet+StatusChange' -ContextLines 0 -FullScan
```

Multiple targets can be passed in one call:

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1 -ScriptFunction 'Pet+StatusChange','CF_FWDRPC+ClientOpenFirstAdoptPet' -ContextLines 1 -FullScan
```

Full scan when the bounded window is insufficient:

```powershell
powershell -ExecutionPolicy Bypass -File .\skills\ugc-log-bug-analyzer\scripts\analyze_ugc_logs.ps1 -FullScan
```

## Interpretation Rules

- Do not say “没问题” when no clear error is found; report the strongest suspicious patterns instead.
- Treat Lua exceptions, nil access, stack tracebacks, and script stack blocks as the highest-priority evidence.
- In targeted mode, treat absence of a matching `【脚本名+函数名】` line as missing execution evidence, not proof that the function did not run; check spelling, DebugID, and scan truncation.
- Treat shutdown / exit / teardown warnings as low-priority noise unless they line up with the user-visible bug time.
- When log lines are repeated in a tight loop, prefer state-transition logs over more copies of the same print.
- When the result points to API misuse or lifecycle mismatch, confirm the engine-side rule with `oasis-combined-mcp`.
- Keep logging advice narrow and practical: `require("Script.UGCLog")` plus `UGCLog.Log()` around entry, branch choice, return values, and state transitions.

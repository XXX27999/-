---
name: oasis-ai-config-archive
description: 把《和平精英》绿洲起源开发用到的 AI 能力资产（技能包、插件清单、MCP 配置、全局提示词）分层归档到知识库 `D:\知识库\和平精英绿洲起源\工具\AI配置归档\`，并做 SHA256 校验与登记。用于「备份/存档技能与 MCP 配置」「后续新增技能、插件、MCP 存到知识库」「换机或客户端重装后恢复技能与 MCP」「软件调用版全局提示词重建」等场景。
agent_created: true
---

# 绿洲 AI 配置归档

把 AI 工具链能力从客户端私有目录搬进知识库，做到**可恢复、可移植、可追溯、可持续**。

归档根固定为：`D:\知识库\和平精英绿洲起源\工具\AI配置归档\`

## 何时使用

- 用户要求「备份 / 存档 / 归档」技能、插件、MCP 配置或全局提示词。
- 新增或改建了技能、插件、MCP，需要按约定落库登记。
- 客户端重装、技能被市场覆盖、配置丢失后需要恢复。
- 需要重建或更新「软件调用版全局提示词」。

## 一、源清单（先枚举，不要凭记忆）

| 资产 | 来源绝对路径 | 归档子目录 |
| --- | --- | --- |
| WorkBuddy 技能 | `C:\Users\Administrator\.workbuddy\skills` | `skills\workbuddy\` |
| Codex 技能 | `C:\Users\Administrator\.codex\skills` | `skills\codex\` |
| 共享技能源 | `C:\Users\Administrator\.cc-switch\skills` | `skills\shared_cc-switch\` |
| 绿洲仓库技能 | `D:\oasis-skill-plus\skills` | `skills\repo_oasis-skill-plus\` |
| WorkBuddy MCP | `…\.workbuddy\mcp.json`、`…\.workbuddy\connectors\default\mcp.json`、`…\.workbuddy\connectors\<uid>\mcp.json` | `mcp\workbuddy\` |
| Codex MCP | `C:\Users\Administrator\.codex\config.toml`（`[mcp_servers.*]`） | `mcp\codex\` |
| 插件 | `…\.workbuddy\settings.json`、`…\.workbuddy\plugins\installed_plugins.json`、`known_marketplaces.json`、`…\.workbuddy\models.json` | `plugins\workbuddy\` |
| 全局提示词原件 | `…\.workbuddy\rules\oasis-global.md`、`…\.workbuddy\rules\island-auction-king-config.md`、`…\.workbuddy\CODEBUDDY.md`、`C:\Users\Administrator\.codex\AGENTS.md` | `全局提示词\` |

**枚举命令**（用 PowerShell，本机 Git Bash 缺 coreutils；PowerShell 输出需写文件后再读）：

```powershell
$o=@()
Get-ChildItem 'C:\Users\Administrator\.workbuddy\skills' -Force | ForEach-Object { $o += ("{0} | {1} | {2}" -f $_.Name,$_.LinkType,($_.Target -join ';')) }
# 目录体量
Get-ChildItem 'C:\Users\Administrator\.workbuddy\skills' -Directory | ForEach-Object {
  $f=Get-ChildItem $_.FullName -Recurse -File -Force -EA SilentlyContinue
  $o += ("{0} files={1} bytes={2}" -f $_.Name,$f.Count,(($f|Measure-Object Length -Sum).Sum)) }
$o | Set-Content "$env:TEMP\_probe.txt" -Encoding UTF8
```

## 二、镜像（robocopy，退出码 1 = 成功）

```powershell
$root = 'D:\知识库\和平精英绿洲起源\工具\AI配置归档'
robocopy 'C:\Users\Administrator\.workbuddy\skills' "$root\skills\workbuddy" /E /XD __pycache__ /XF *.pyc /NFL /NDL /NJH /NJS /NP /R:1 /W:1
robocopy 'C:\Users\Administrator\.cc-switch\skills' "$root\skills\shared_cc-switch" /E /XD __pycache__ /XF *.pyc /NFL /NDL /NJH /NJS /NP /R:1 /W:1
robocopy 'D:\oasis-skill-plus\skills' "$root\skills\repo_oasis-skill-plus" /E /XD __pycache__ /XF *.pyc /NFL /NDL /NJH /NJS /NP /R:1 /W:1
```

- Codex 侧按技能名单逐个 `robocopy`（避免把 `hatch-pet`、`.system` 等无关目录带进来）。
- 单文件配置用 `Copy-Item -Force` 并用 `01_`、`02_` 前缀编号命名，保留原扩展名。
- **排除项**：`__pycache__`、`*.pyc`（会破坏哈希稳定性）；`plugins\cache` 内置插件正文（市场可重装）；`workbuddy.db`、`*.sqlite`（会话历史）。

## 三、生成与回校 SHA256

**两个硬性技术点**（都是实测踩过的）：① 必须 UTF-8 **无 BOM** 写入，`Set-Content -Encoding UTF8` 会加 BOM，违反知识库约定；② 校验行解析**不能**用 `-split '\s+'` 取 `$p[1]`——归档里有 `20414_UGCAskQ MCP 使用说明.md` 这类**含空格**的路径，会切错。统一用带命名组的正则。

```powershell
$ErrorActionPreference='Stop'
$root = 'D:\知识库\和平精英绿洲起源\工具\AI配置归档'
$out  = Join-Path $root '归档记录\校验清单_SHA256.txt'
$files = Get-ChildItem -LiteralPath $root -Recurse -File | Where-Object { $_.FullName -ne $out }
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add('# 归档校验清单 SHA256  ——  生成时间 YYYY-MM-DD')
$lines.Add('# 覆盖范围：AI配置归档目录下全部文件（不含本清单自身）')
$lines.Add('# 格式：SHA256  相对路径  字节数')
foreach ($f in $files) {
  $rel = $f.FullName.Substring($root.Length + 1)
  $h = (Get-FileHash -LiteralPath $f.FullName -Algorithm SHA256).Hash
  $lines.Add("$h  $rel  $($f.Length)")
}
# 无 BOM 落盘
[System.IO.File]::WriteAllLines($out, $lines, (New-Object System.Text.UTF8Encoding($false)))

# 回校（正则解析，容忍路径含空格）
$rows = Get-Content -LiteralPath $out -Encoding UTF8 | Where-Object { $_ -and (-not $_.StartsWith('#')) }
$re = '^(?<h>[0-9A-F]{64})\s{2}(?<p>.+?)\s{2}(?<s>\d+)$'
$ok=0; $bad=0; $miss=0
foreach ($l in $rows) {
  $m = [regex]::Match($l, $re)
  if (-not $m.Success) { $bad++; continue }
  $p = Join-Path $root $m.Groups['p'].Value
  if (-not (Test-Path -LiteralPath $p)) { $miss++; continue }
  if ((Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash -eq $m.Groups['h'].Value) { $ok++ } else { $bad++ }
}
"entries=$($rows.Count) ok=$ok bad=$bad missing=$miss"
# 三项必须同时成立：bad=0、missing=0、清单无 BOM
```

清单**不含自身**，条目数等于「归档文件总数 − 1」；回校必须 `bad=0 missing=0`（即 `ALL OK`）。

**改过归档内任何文件后必须重建清单**；清单以外的页面只写近似体量（见第七节第 7 条）。

## 四、登记（缺一不可）

在 `…\AI配置归档\归档记录\<YYYYMMDD>_<主题>.md` 追加登记项，字段固定：

资产类型 / 归档绝对路径 / 来源绝对路径 / 部署目标绝对路径 / 关联实体 / 用途 / 调用入口 / 输入输出 / 依赖 / 版本 / 证据状态 / 生命周期 / 更新时间。

同时更新 `…\AI配置归档\000_归档索引.md` 的技能矩阵或 MCP 表格行，并补 `wiki\000_索引.md` 更新日志。

## 五、恢复

```powershell
robocopy 'D:\知识库\和平精英绿洲起源\工具\AI配置归档\skills\workbuddy' "$env:USERPROFILE\.workbuddy\skills" /E /XD __pycache__ /XF *.pyc
Copy-Item 'D:\知识库\和平精英绿洲起源\工具\AI配置归档\mcp\workbuddy\01_workbuddy_mcp.json' "$env:USERPROFILE\.workbuddy\mcp.json" -Force
```

- Codex `config.toml` **只合并 `[mcp_servers.*]` 段，禁止整文件覆盖**（会丢 `[projects.*]` 信任列表与 `[windows] sandbox`）。
- 恢复后重启客户端，并用 `$oasis-mcp-port-discover` 只读**确认服务在线**：UGCAskQ 在本机使用**固定端口** `127.0.0.1:12463/sse`（官方 Wiki 默认 `33444`、可在 MCP Server 控制面板修改，本机不使用默认值），**无需重新发现端口**；仅换机 / 重装编辑器 / 改过控制面板 Port 时才重走完整发现流程。

## 六、软件调用版全局提示词

位置：`…\AI配置归档\全局提示词\软件调用版_绿洲全局提示词.md`

维护规则：

1. 指令正文**沿用原件措辞**，只做编号结构化，不做同义改写。
2. 路径全部集中在第 2 节「运行环境上下文」，正文只用 `{{...}}` 符号引用。
3. 客户端专属内容（Codex 线程派发、具体模型名、本地代理端口）一律进第 0.3 节「可选模块」，**不得**写进第 3 节指令主体。
4. 原件更新后同步第 8 节版本表并升版本号。

## 七、易踩的坑

1. **不要只存一份技能**。实测四个宿主目录已有字节级漂移（如 `oasis-prompt-optimize` 26,125 vs 25,399），必须分层保留。
2. **软链要识别**。`~\.codex\skills\oasis-official-docs` 是指向 `~\.cc-switch\skills\oasis-official-docs` 的 SymbolicLink，`Get-ChildItem | Select LinkType,Target` 先看清再复制。
3. **不要用 Bash 跑本流程**。本机 Git Bash 缺 `ls`/`dirname`，会静默失败；统一用 PowerShell，且输出先写文件再读（本机 PowerShell 直接回显偶发丢失）。
4. **相对链接层级要算对**。`工具\AI配置归档\` 下的文件引用 `raw\` 需 `../../../raw/`；而 `AI配置归档\` 根下只需 `../../raw/`。
5. **归档内禁止** `__pycache__`、`*.pyc`、临时脚本、`.uasset`、`.lua`。
6. **每次改动后重建清单**，否则校验会 FAIL。
7. **不要在被统计的集合内部记录该集合的精确字节总数（自指数值）**。归档页面每写一次「合计 `26,406,554 B`」，归档体积就变一次，下一轮必然对不上。页面只写近似值（`≈26.41 MB`），精确值以 `归档记录\校验清单_SHA256.txt` 内各条字节数之和为准。
8. **声称「某文件已订正」前，必须先在目标文件内回读确认**。实测出现过「`mcp\000_MCP清单.md` 已声明技能表述订正，而 `oasis-mcp-port-discover\SKILL.md` 正文其实未改」的不一致；凡写「已订正」，先把目标文件 grep 一遍再落笔。
9. **归档副本必须与运行副本逐字节一致**。发现上游技能自带缺陷（例：`sq-skill\docs\community\000_索引.md` 大量链接指向不存在的 `threads\` 目录，实际目录是 `lists\` / `replies\`）时，**不得在归档侧单方面修好**，否则哈希与运行副本分叉；只记录到「已知缺口」并告知用户。
10. **文档类订正也要走一遍校验闭环**：改完归档内 `.md` → 重建清单 → 回校 `bad=0 missing=0` → 检查无 BOM → 检查归档自建 `.md` 的相对链接（排除 `skills\` 子树，那里是上游内容，断链属其自身状态）。

## 相关页面

- `D:\知识库\和平精英绿洲起源\工具\AI配置归档\000_归档索引.md`
- `D:\知识库\和平精英绿洲起源\工具\AI配置归档\存放约定_新增技能插件MCP.md`
- `D:\知识库\和平精英绿洲起源\raw\知识\通用\工具与流程\AI配置归档与软件调用全局提示词.md`

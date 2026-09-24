---
name: oasis-ai-config-dedup
description: 审计并清理 AI 客户端（WorkBuddy / Codex / cc-switch / 绿洲仓库）中重复注册或重复安装的技能（skills）、插件（plugins）与 MCP server。用于「技能/插件/MCP 是不是装重了」「同名冲突该留哪份」「清理客户端缓存释放磁盘空间」「哪个 mcp.json 才是生效的」等场景。
agent_created: true
---

# AI 客户端配置重复项审计与清理

目标：找出**同名或同功能重复、在多个位置重复注册/重复安装**的条目，每类只留一份可正常加载的配置。

## 何时使用

- 用户要求检查 / 去重 / 清理技能、插件、MCP 配置。
- 怀疑「同一个 MCP 配了两遍」「两个技能叫一个名字」。
- 要释放客户端缓存占用的磁盘空间。

## 一、只读清单（先扫，不许先删）

四个技能/配置宿主 + 三类资产，逐层枚举（本机 Git Bash 缺 coreutils，**一律用 PowerShell**，输出先写 TEMP 文件再读）：

| 宿主 | 路径 | 说明 |
| --- | --- | --- |
| WorkBuddy | `~\.workbuddy\skills`、`~\.workbuddy\mcp.json`、`~\.workbuddy\connectors\`、`~\.workbuddy\plugins\` | 主力客户端 |
| Codex | `~\.codex\skills`、`~\.codex\config.toml`、`~\.codex\plugins\` | `[mcp_servers.*]` 用正则 `^\[mcp_servers\.(?<n>[^\]]+)\]` 提取 |
| cc-switch | `~\.cc-switch\skills` | 与 codex 常为同内容副本 |
| 绿洲仓库 | `D:\oasis-skill-plus\skills` | 官方/自研仓库 |

WorkBuddy 一处要额外看 `~\.workbuddy\connectors\skills\`（连接器提供的技能）与 `~\.workbuddy\plugins\cache\<marketplace>\<plugin>\<version>\skills\`（插件内置技能）。

## 二、三条判定规则（本流程的核心）

1. **技能名以 SKILL.md 的 frontmatter `name:` 为准，不要用目录名。**
   插件技能层级是 `<plugin>\<version>\skills\<skill>\`，取目录名会得到 `skills` / `experts` / 版本号等容器名，产生几十条假阳性。用
   `[regex]::Match($t,'(?m)^name:\s*(?<n>.+?)\s*$')` 取权威名，再按名聚合找冲突。

2. **MCP「哪个文件生效」靠三证据交叉，不能只看文件存在：**
   - 产品文档规定的用户级入口（WorkBuddy 是 `~\.workbuddy\mcp.json`）；
   - **谁在被客户端持续写**：比较 mtime，被更新的那个才是活的（实测 `connectors\<uid>\mcp.json` 天天更新，`connectors\default\mcp.json` 停更且旁边有 `.bak-*` → 陈旧副本）；
   - **会话里工具是否真的可用**（`ue_read`/`ue_py` 能调即证据）。
   补充：产品目录里带凭据与 `README-DO-NOT-DELETE.txt` 的那个目录才是连接器主目录。

3. **同名不同内容时，保留「能正常加载的那份」：**
   - 看 `disable: true` / `enabledPlugins` 开关，被禁用的那份是被冲裁者；
   - 插件缓存里的副本**不删**（客户端自愈，删了会重下，无持久收益），只在插件级别关开关；
   - 用户级技能 vs 连接器提供的同名技能 → 保留用户级。

## 三、清理执行（本机两条硬约束）

1. **回收站 API 不可用**：`Add-Type` 与 `[Reflection.Assembly]::LoadWithPartialName(...)` 都会被安全策略拦截（报 "compiles and loads .NET code at runtime"）。
   → 用 `Move-Item` 移到隔离目录，**不要直接 `Remove-Item`**。隔离目录放知识库备份下：
   `D:\知识库\和平精英绿洲起源\备份\AIConfig\<YYYYMMDD>_清理隔离\`，事后由用户决定是否永久删除。
2. **改客户端配置文件前先探测换行风格**。`[System.IO.File]::WriteAllLines` 会把 LF 改成 CRLF——实测一个 1367 行的 JSON 因此**从 38,475 B 涨到 39,591 B**，制造巨大 diff。
   正确做法：`ReadAllText` → `-replace "\`r\`n","\`n"` → `WriteAllBytes`（保留原 LF + 无 BOM）。
3. 改 JSON 配置优先**按行精确摘除**（定位 `"key": {` → 找到同缩进的 `}` → 删除区间 → 去掉上一项尾随逗号），不要整体 `ConvertTo-Json` 回写（PS 5.1 会转义 `<>'` 等字符）。
4. 大目录逐项处理并**每处理一项就写一次日志**：一次批量 `Move-Item` 若中途失败，日志不会落盘，无法判断哪些已移动。

## 四、回校（缺一不可）

- 生效配置仍在（例：根 `mcp.json` 仍有 `ugcaskq`）；被改的 JSON 能 `ConvertFrom-Json`、条目数符合预期、无 BOM、换行风格未变。
- 被删条目已不存在；**同名冲突保留的那份仍在**（用 `Test-Path` 逐条确认）。
- 在用的运行时目录完好（例：`.codex\plugins\.plugin-appserver` 的 exe 还在，被删的是 `.staging-*`）。
- MCP 服务端点仍在 LISTEN（`Get-NetTCPConnection -LocalPort <port> -State Listen`）。
- 脚本类删除要**先 grep 引用者**：`patchschema.py` 与 `patch_automation_schema.py` 内容完全相同，但两个 `.cmd` 引用的是后者，删反了会让 `.cmd` 失效。

## 五、归档同步（按既有约定）

改动落到 `D:\知识库\和平精英绿洲起源\工具\AI配置归档\`：
1. 把改后的配置文件拷回对应归档位（例 `mcp\workbuddy\03_connectors_default_mcp.json`），并校验 `Get-FileHash` 两侧一致；
2. 更新 `mcp\000_MCP清单.md` 与 `000_归档索引.md` 的对应行，关闭已查清的「待查证」项（保留原问法 + 加删除线 + 写证据）；
3. **重建 `归档记录\校验清单_SHA256.txt` 并回校 `bad=0 missing=0`**（无 BOM 写入）。

## 六、易踩的坑

1. `Select-String` 全目录搜关键词会命中 `logs/`、`traces/`、`file-history/`、`projects/` 等运行目录，噪音几百条甚至撑爆日志文件；先用 `-notlike` 排除，或直接比对 JSON 键集合（`-like`/集合差集）而不是搜文本。
2. 统计目录体积时别把**会话数据库**当重复项：`.codex\thread_history_1.sqlite`（约 300 MB）、`logs_2.sqlite`（约 110 MB）是历史数据，不是重复，不要动。
3. 跨宿主的同名技能**不一定是重复**：按用户约定「技能分四层来源，不可合并成单份」，workbuddy / codex / cc-switch / repo 四层镜像都要保留。
4. 判断文件名时认准**伪装成相对路径的目录名**，如 `.codex\plugins\..plugin-appserver.staging-koMSUc`（`..` 是文件名的前两个字符，不是父目录）。

## 相关页面

- `D:\知识库\和平精英绿洲起源\工具\AI配置归档\000_归档索引.md`
- `D:\知识库\和平精英绿洲起源\工具\AI配置归档\mcp\000_MCP清单.md`
- `D:\知识库\和平精英绿洲起源\工具\AI配置归档\存放约定_新增技能插件MCP.md`

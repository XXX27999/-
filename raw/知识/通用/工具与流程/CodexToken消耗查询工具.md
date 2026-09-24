# CodexTokenGlass —— Codex Token 消耗查询工具

> 类型：通用知识
> 主题：把开源抓包工具 ccglass 封装成 Windows 桌面软件并中文化，用于查询 Codex 的 Token 消耗、缓存命中、耗时与费用
> 适用范围：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\`（`CodexTokenGlass.exe` + `runtime\node.exe` + `ccglass\` + `StartService.cmd`）；链路 `Codex -> 9911 -> 8787 -> 上游`
> 证据状态：项目实测（2026-09-23 冷启动、请求抓取、用量汇总、窗口关闭后服务存活、二次启动复用均实测通过；2026-09-24 历史删除与 Token 估算口径实测通过）
> 来源：上游仓库 https://github.com/jianshuo/ccglass ；封装源码 `C:\Users\Administrator\Documents\Codex\2026-09-23\https-github-com-jianshuo-ccglass-https\work\CodexTokenGlass`；配置备份 `C:\Users\Administrator\.codex\backups\ccglass\`
> 更新时间：2026-09-24（补充：左侧历史单条/批量/整会话删除；估算规则改为整包估算并重新标定 CJK 权重）
> 关联主题：工具与流程 / Codex 上下文与用量 / 本地中转代理
> 排除范围：不涉及 UGC 工程内 Lua、蓝图、UI 资产或任何 PIE 逻辑；不改动 `raw/docs/`
> 官方依据：`ccglass` 的 `proxy`/`usage` 子命令与 `/api/usage`、`/api/sessions` 行为来自上游源码 `src/cli.js`、`src/server.js`、`src/log-cli.js`；本工具为本地封装，无官方 API 约束

## 背景与需求

需要在不改变既有 Codex 中转链路的前提下，看到每次请求的 Token 消耗（输入 / 输出 / 缓存读写）、首字延迟、生成耗时和费用，并且做成可直接双击的 Windows 软件、界面全中文、放在知识库工具目录。

## 核心结论

1. **ccglass 必须以「代理」模式常驻，而不是「包装客户端」模式。** 桌面端 Codex 自己拉起进程，`ccglass codex ...` 那种「由 ccglass 启动客户端」的用法不适用；必须用 `ccglass proxy --provider codex` 常驻抓包，再由 `config.toml` 把 Codex 指过来。
2. **端口分工**：`9911` = ccglass 抓包代理（Codex 的实际出口）；`9912` = 中文看板；`8787` = 既有 schema 中转代理，保持不变。链路为 `Codex -> 9911 -> 8787 -> 57321/apihub`。
3. **`config.toml` 是唯一开关，而且只对重新加载配置之后的对话生效。** 使用 `model_provider = "custom"` 时，`[model_providers.custom].base_url` 必须是 `http://127.0.0.1:9911/v1`；使用 `model_provider = "openai"` 时，根级 `openai_base_url` 也必须是该地址。已经打开的对话会继续用它启动时的上游地址，改文件不会把这条对话改道到 `9911`。当前版本程序启动时自动检查只覆盖 `[model_providers.custom].base_url`，改写前把原文件备份到 `.codex\backups\ccglass\config.toml.bak_<时间戳>`。
4. **关闭窗口不关服务**：窗口只关看板 UI，`9911`/`9912` 保持运行，避免关闭看板时打断正在进行的对话；再次双击 exe 会复用已在运行的服务，不会抢端口。
5. **npm 上的 `ccglass@1.1.2` 缺少新版 `proxy` 子命令**，需从 GitHub HEAD 源码安装；本工具内置的是 GitHub HEAD 版本源码，并附带 `node_modules`。
6. **计费口径**：费用按上游源码内置的模型单价估算，`usage` 中会区分「已计量」与「未计量」请求；无 usage 字段的请求不计入 Token 与费用。
7. **Token 粒度是「一次 HTTP 请求」，不是流程里的某一步。** 上游只在整次响应上返回 `usage`（`input_tokens` / `output_tokens` / 缓存）。流程时间线里的用户消息、思考、工具调用、工具结果都是这次请求的内容拆解，没有各自的账单。2026-09-23 已把这一次请求的输入、输出、缓存和费用显示在「流程」页顶部、左侧请求行和实时流的轮次分隔上。
8. **流程里每条用户消息和助手消息另有正文粗估。** 标签写成 `≈`，公式与 `src/tokens.js` 的 `estimateTokens` 相同：中文约 1.12 token/字，其余约 4.6 字符/token。它只估这条消息的正文，不是上游账单，也不覆盖思考、工具调用和工具结果。实时流里出现的用户/助手行用同一标签。
9. **看板页面会话列表必须动态刷新。** 原实现只在首次打开时读取 `/api/sessions`，SSE 只处理当前已选会话；服务重启产生新采集会话后，旧页面会看不到新会话，即使新请求已经写入 `%USERPROFILE%\\.ccglass\\codex-desktop`。2026-09-23 已在 `工具\\CodexTokenGlass\\ccglass\\web\\app.js` 增加 `no-store` 会话轮询、实时视图跟随新会话和 SSE 断线重连；保留用户手动选中的历史会话。
10. **左侧历史支持单条、批量、全选/反选与整会话删除（2026-09-24 新增，同日补充全选/反选）。** 看板顶栏「管理」按钮切换管理模式，每个历史请求行出现复选框和单条删除按钮；「全选 (n)」一键勾选当前列出的全部请求（已全选时变为「取消全选 (n)」），「反选」把当前勾选状态取反，「删除选中 (n)」批量删除已勾选请求，「删除本会话」删除当前会话的全部抓包。所有删除都先弹确认框，且不可撤销。
    - **勾选按重试链展开**：左侧把同一请求的多次重试折叠成一行（显示「已重试 ×N」），勾选该行会连带勾选它的全部重试子条目。因此「全选 (n)」的 n 是**条目总数**，通常大于左侧可见行数；例如 472 行对应 500 条目。这样做是为了避免只删掉行首、把隐藏的重试条目留在磁盘上又冒出来。
    - **删除接口分两个**：单条走 `DELETE /api/delete?id=<session>/<seq>`，整会话走 `DELETE /api/delete?session=<name>`；批量（含全选/反选后删除）走 `POST /api/delete-batch`，body 为 `{"ids":["<session>/<seq>", ...]}`，返回 `{"deleted":[...],"removed":N}`，只列出真正存在于磁盘上的 id。
    - **为什么批量要单独一个接口**：`rmEntry` 每删一条都会全量重扫所有清单来回收 `blobs/`，实测单条删除约 430 ms；全选几百条若逐条删除，累计要数分钟。`rmEntriesMulti` 先删完全部清单、再对受影响的 root 只做一次 GC，实测 564 条 665 ms、浏览器内 498 条 1.15 s。
    - 删除后回收不再被引用的 `blobs/` 分片，并通过 SSE `delete` 事件同步到其他已打开的看板。命令行等价入口为 `ccglass rm-entry <session>/<seq> [...]`（仍按单条语义，逐条处理）。
11. **合计口径区分「预估合计」与「实际合计」，且估算改为整包估算（2026-09-24 重标定）。** 「实际合计」= 总输入（未缓存 + 缓存读取 + 缓存写入）+ 输出，直接取自上游 `usage`，与账单一致；「预估合计」= 对**整个请求 JSON**（system、messages、`function_call` / `function_call_output` / `reasoning`、`tools`）加响应正文的字符估算，而不是只估某条消息正文。这样两者在同一量纲上可比，面板同时显示偏差百分比。2026-09-24 在真实抓包上网格搜索标定：`ESTIMATE_CJK_WEIGHT = 1.12`、`ESTIMATE_ASCII_CHARS_PER_TOKEN = 4.6`；随数据增长复算（167 → 347 → 369 条），合计偏差稳定在 ±1% 内。`web\\app.js` 内有一份同值常量，改动时必须与 `src\\tokens.js` 同步。

## 可执行步骤

### 启动与查看

1. 双击 `D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\CodexTokenGlass.exe`。
2. 程序自动：检查 `9912` 是否已就绪 → 未就绪则拉起内置 `runtime\node.exe` 运行 `ccglass\bin\ccglass.js proxy` → 打开中文看板。
3. 看板地址 `http://127.0.0.1:9912`，数据目录 `%USERPROFILE%\.ccglass\codex-desktop`。

### 命令行用量汇总（中文化后）

```powershell
& "D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\runtime\node.exe" `
  "D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\ccglass\bin\ccglass.js" `
  usage --dir "$env:USERPROFILE\.ccglass\codex-desktop"
```

输出中的「预估合计」与「实际合计」并排显示，并给出偏差百分比；脚本通过
`src\tokens.js` 的整包估算器得到预估侧，通过响应 `usage` 得到实际侧。

### 看板删除历史抓包（含全选/反选）

1. 点顶栏「管理：关闭」切换为「管理：开启」，左侧每行出现复选框与「删除」按钮。
2. 「全选 (n)」勾选当前列出的全部请求；再点一次（此时按钮显示「取消全选 (n)」）全部取消。
   「反选」把当前勾选状态取反，适合「留下少数几条、删掉其余」的场景。
3. 「删除选中 (n)」批量删除已勾选请求，「删除本会话」删除当前会话的全部抓包。

> `n` 是条目总数（含折叠的重试子条目），所以通常大于左侧可见行数。

### 命令行删除历史抓包

```powershell
& "D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\runtime\node.exe" `
  "D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\ccglass\bin\ccglass.js" `
  rm-entry "2026-09-24T11-08-38-398/0001" "2026-09-24T11-08-38-398/0002" `
  --dir "$env:USERPROFILE\.ccglass\codex-desktop"
```

一次可传多个 `<session>/<seq>`；单个 id 不存在时输出 `not found: <id>` 但继续处理其余 id，
全部 id 都未命中（不存在或格式非法）时进程以非零码退出，便于脚本判定。
删除只移除 `NNNN.json` 清单并按引用回收 `blobs/`，不触碰 `raw\docs\`。

### 开机自启

计划任务 `CodexTokenGlass`（登录时触发，最高权限）指向 `StartService.cmd`，登录后自动拉起 `9911`/`9912`，不打开看板也会持续统计。

### 彻底停止

```powershell
Get-NetTCPConnection -LocalPort 9911 -State Listen |
  Select-Object -ExpandProperty OwningProcess -Unique |
  ForEach-Object { Stop-Process -Id $_ -Force }
```

停止前需先把 `config.toml` 的 `base_url` 改回 `http://127.0.0.1:8787/v1`，否则 Codex 断链。

## 关键实现点

| 问题 | 处理 |
| --- | --- |
| 单文件发布把 `runtime\node.exe` 打进 exe，导致 `AppContext.BaseDirectory\runtime\node.exe` 找不到 | csproj 中给 `runtime\**` 与 `ccglass\**` 加 `ExcludeFromSingleFile="true"`，保持 exe 旁散落文件 |
| 重定向 stdout/stderr 的管道会随窗口关闭而断开，后台代理被杀 | 改用 `cmd.exe /c ... >> service.log 2>&1` 由 cmd 持有日志，不用 `RedirectStandardOutput` |
| 关闭窗口杀掉服务导致 Codex 断链 | 移除 `OnClosed` 里的 `Kill`，窗口只关 UI |
| 二次启动与已运行实例抢 `9911` | 先探 `9912/api/sessions`，未就绪再探 `9911` 是否在监听，是则等待而非再拉一个 |
| 启动时自动改配置有风险 | 改写前按时间戳备份原 `config.toml`；已是 `9911` 则完全不改 |
| 中文界面在若干处残留英文 | 全量替换 `web\app.js`、`index.html`、`stream.css` 与 `src\log-cli.js` 中用户可见文案，保留 `tool_use`/`tool_result`/`cacheR` 等协议字段名与表格列头（另给出中文列名说明行） |
| 删除历史后 `blobs/` 留下孤儿分片 | `src\store.js` 的 `rmEntry` / `rmSession` 删除清单后调用 `gcBlobs`，按剩余清单引用回收未再被引用的分片 |
| 删除正在进行的请求后它又“复活” | `Store` 增加 `removed` 集合，`update()` 命中已删除 id 时直接返回，不再落盘或广播 |
| 删除实时会话目录后代理写盘 ENOENT | `Store._persist` 在写入前 `fs.mkdirSync(this.sessionDir, { recursive: true })`，目录被删也能自愈重建 |
| 删除只对当前标签页生效 | `DELETE /api/delete` 成功后向所有 SSE 客户端广播 `{"deleted":"<id>"}`，其他看板按 id 就地移除行 |
| 全选后逐条删除慢到不可用 | 单条删除每次都要全量重扫清单回收 blob（实测约 430 ms/条，几百条要几分钟）；新增 `rmEntriesMulti` + `POST /api/delete-batch`，先删完文件再对每个 root 只 GC 一次，564 条实测 665 ms |
| 重试折叠行删不干净 | 左侧折叠的重试子条目也属于同一行，勾选/删除都按 `rowIds` 展开整条重试链，避免只删行首、隐藏重试残留后重新冒出来 |
| 顶栏按钮文字被拆成两行 | `select, button` 加 `white-space: nowrap`、`header` 加 `flex-wrap: wrap`，按钮保持单行、装不下时整行折到第二排 |
| 长会话页面出现横向滚动条 | 延迟趋势图 `.bar` 有 `min-width: 3px`，几百个柱子会把页面撑宽；给 `.latency-trend .bars` 加 `overflow: hidden`（既有问题，2026-09-24 一并修复） |
| 估算口径与账单对不上 | 估算从「只估单条消息正文」改为「整包估算」：`estimateRequestTokens` 对完整请求 JSON 计数，`estimateResponseTokens` 计响应正文，再与 `usage` 的总输入+输出同框对比 |

## 生效方式

- **前端（`ccglass\web\` 下的 `app.js` / `index.html` / `style.css`）**：由服务按请求从磁盘读取，
  直接刷新看板页面即可生效，不需要重启服务。
- **后端（`ccglass\src\` 下的 `tokens.js` / `usage.js` / `store.js` / `server.js` / `session-stats.js` /
  `log-cli.js` / `cli.js` / `formats\openai.js`）**：必须重启 `9911`/`9912` 采集服务才会加载，
  重启会让 Codex 流量中断数秒。实测判据：重启前 `GET /api/delete` 返回 `404`（旧路由不存在），
  重启后返回 `405`（路由存在但不接受 GET）；`/api/usage` 的 `totals` 出现 `estTotal` /
  `actualTotal` / `estDeviation` 三个字段。

重启命令见上文「彻底停止」；重新执行 `StartService.cmd` 或双击 `CodexTokenGlass.exe` 即可拉起。

## 估算常数的标定方法

`src\tokens.js` 里只有两个可调常数：`ESTIMATE_CJK_WEIGHT`（每个中日韩字符折算多少 token）
与 `ESTIMATE_ASCII_CHARS_PER_TOKEN`（多少个非 CJK 字符折算 1 token）。两者都是经验拟合值，
不是官方 tokenizer，因此换了模型、语种比例或上下文长度后需要重新标定。

标定步骤（2026-09-24 实测流程）：

1. 遍历 `%USERPROFILE%\.ccglass\codex-desktop` 下所有会话清单，取出同时具备请求体与
   `usage` 的条目；对每条算出「请求 JSON 字符数 + 响应正文字符数」中的 CJK 与非 CJK 计数，
   以及真值 `input_tokens + output_tokens`（含缓存时按面板口径用总输入 + 输出）。
2. 在 `CJK 权重 0.6~1.4`、`每 token 字符数 3.0~6.5` 上做网格搜索，对每个组合计算
   估算合计 / 实际合计 的比值与逐条 MAPE。
3. 先筛出「合计比值落在 ±0.5%」的组合，再在其中挑逐条 MAPE 最小的那个，避免为了凑总
   比例而把单条误差放大。
4. 用时间对半切分做留出校验（旧半段拟合、新半段验证），确认常数不是只贴合某一段数据。

2026-09-24 的结果：167 条已计量请求时 `w=1.12`、`4.6` 的合计偏差约 -0.4%；
当天数据增长到 347 条后复算，偏差约 -0.7%，仍在 ±1% 内，因此常数无需再改。
同一批数据上旧的 `w=1.0`、`4.6` 偏差达 -3.3%，说明只估正文会系统性偏低。
注意：网格里存在一条「平坦脊线」（例如 `1.36/4.9` 也能把合计凑到接近 0），
这类组合只是把总比例凑对、逐条误差反而更大；选常数时应以逐条 MAPE 为主要依据。

## 常见错误

- **看板一直没有数据**：`base_url` 没指向 `9911`，或改了配置后没重启 Codex。已经打开的对话不会改道。
- **删了历史但合计没变**：删除后看板会重新拉 `/api/usage`；若仍显示旧值，确认改动的是当前看板指向的数据目录（默认 `%USERPROFILE%\.ccglass\codex-desktop`），并刷新页面。
- **管理按钮不见了**：顶栏「管理：关闭」按钮是切换入口；关闭状态下复选框与删除按钮都会隐藏，这是预期行为。
- **「全选 (n)」的 n 比左侧行数大**：正常现象。左侧把重试折叠成一行，`n` 统计的是含重试子条目的条目总数。
- **点「删除选中」弹出「删除失败：404」**：说明看板服务还是旧代码，没有 `POST /api/delete-batch` 路由，请求落到静态文件处理返回 404。重启 `9911`/`9912` 采集服务后恢复；重启前请先把 `config.toml` 的 `base_url` 改回 `8787`。
- **合计口径读不懂**：`实际合计` 是账单侧真值（总输入含缓存 + 输出），`预估合计` 是字符估算。两者偏差在 ±5% 内属正常；偏差长期偏大说明抓包语种结构变化，需要重新标定。
- **实时会话是空的，但这条对话其实在别的地址上**：2026-09-23 14:38 重启 ccglass 后，看板默认选中的实时会话 `2026-09-23T14-38-38-406` 请求数为 0。当前对话线程 `01a0cca1-4a68-7170-a910-a17335ef2bf2` 从 13:55 起一直请求 `https://www.mcgrox.top/v1/responses`（经 Clash `127.0.0.1:7897` 出去）。`config.toml` 在 14:29:53 已写成 `http://127.0.0.1:9911/v1`，但该线程的 HTTP 客户端日志里对 `9911` 的请求数是 0，8787 代理日志在 14:31:22 之后也没有新的 `/v1/responses`。ccglass 只能看到打进 `9911` 的流量，所以这条对话不会出现。同一时段另一条线程 `01a0ccf5-76ae-74f0-b34c-1ddc69a9da65` 走了 `9911`，数据在会话 `2026-09-23T14-12-07-119`，不要把它当成当前这条。

- **`ccglass proxy` 报未知子命令**：装的是 npm 上的 `1.1.2`，缺 `proxy`；改用 GitHub HEAD 源码。
- **提示缺少 Node 运行时 / ccglass 服务文件**：解压不完整，`runtime\` 与 `ccglass\` 必须与 exe 同级。
- **关掉窗口后 Codex 报错**：说明用的是会杀服务的旧版 exe，请用本目录版本。
- **端口被占用**：统计服务已在运行，属正常现象，程序会自动复用。
- **`custom.base_url` 已指向 `9911` 但新对话仍没有数据**：检查实际 `model_provider`。若为 `openai`，还要将根级 `openai_base_url` 改为 `http://127.0.0.1:9911/v1`，然后完整重启 Codex；本机 `57321` 仍作为 `9911 -> 8787` 的上游中继保留。
- **服务已运行但旧看板看不到新对话**：先刷新看板页面；本版本 `app.js` 会每 2 秒刷新会话列表，并在 SSE 断线后自动重连。验证 `/api/sessions` 的 `live` 是否变化、对应 `/api/requests?session=<live>` 是否有新条目；若无条目，再检查当前对话是否已重新加载指向 `9911` 的配置。
- **9911 能看到请求但对话仍无法完成**：检查 `C:\Users\Administrator\.codex\apihub_schema_proxy.log`。本机 2026-09-23 实测，`8787` 若直连 `https://apihub.veletis.com` 会返回 `401 invalid_api_key`，表现为 `9911` 中出现 `/v1/responses` 但全部失败；已将 `C:\Users\Administrator\.codex\apihub_schema_proxy.py` 的上游恢复为 `http://127.0.0.1:57321`，并验证 `57321`、`8787`、`9911` 的 `/v1/models` 均返回 `200`。修复后必须完整重启 Codex Desktop，让已打开会话重新加载 `http://127.0.0.1:9911/v1`；旧失败记录不会自动变成成功。

## 相关页面

- [Codex 上下文超限排障](./Codex上下文超限排障.md)
- [AI 配置归档与软件调用全局提示词](./AI配置归档与软件调用全局提示词.md)
- [Codex Sol 与 Luna 分工模式](./Codex-Sol与Luna分工模式.md)
- **工具目录**：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\`

## 待查证

1. 上游 `ccglass` 后续版本是否会提供更多 provider 的自动配置（当前 Codex 走 `--provider codex` 手动指定）。
2. 「未计量请求」的具体成因未逐条核对（上游对无 usage 字段响应的处理口径未逐一验证）。
3. 上游内置单价表是否覆盖本机实际使用的全部模型，未逐模型比对账单。

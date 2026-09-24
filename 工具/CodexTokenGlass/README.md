# Codex Token 消耗查询（CodexTokenGlass）

基于开源工具 [ccglass](https://github.com/jianshuo/ccglass) 封装的 Windows 桌面程序，用于查看 Codex 每次请求的 Token 消耗、缓存命中、耗时和费用，界面已完整中文化。

## 一、直接使用

1. 双击本目录下的 `CodexTokenGlass.exe`。
2. 程序会自动检查并启动本地统计服务，然后在内置窗口中打开中文看板。
3. 看板地址：`http://127.0.0.1:9912`

首次启动如果提示缺少 Node 运行时或服务文件，说明解压不完整，请确认 `runtime\node.exe` 与 `ccglass\` 目录与本文件在同一层。

## 二、它能统计什么

- 每个会话、每次请求的输入 / 输出 Token 数
- 缓存读取与缓存写入 Token 数、缓存命中率
- 首字延迟、生成耗时、总耗时、输入 / 输出速度
- 按模型、按会话、按时间的费用汇总（美元，按模型单价估算）
- 完整的请求与响应内容、系统提示词、工具列表、流式时间线
- 两条请求的上下文差异对比，便于排查上下文膨胀原因
- 「实际合计」与「预估合计」并排显示：实际侧取自上游 `usage`（总输入含缓存 + 输出），
  预估侧对整包请求与响应做字符估算，并给出偏差百分比

> 「预估合计」只是字符估算，不是官方 tokenizer。若换了模型或语种比例变化导致偏差长期偏大，
> 需按 `src\tokens.js` 顶部的说明重新标定 `ESTIMATE_CJK_WEIGHT` 与
> `ESTIMATE_ASCII_CHARS_PER_TOKEN`（`ccglass\web\app.js` 内有同值常量，必须同步修改）。

> 2026-09-24 修复：大会话删除后界面长时间无响应。根因是删除成功后仍全量重拉 627 MB 会话，
> 列表/统计接口约 60~100 秒。现在列表与统计走按文件版本缓存的摘要，删除先落盘、后台回收
> blob，删除响应不再等待统计刷新。实测大会话列表热态约 303 ms、统计约 335 ms，并发删除约 119 ms。
> 单条删除与整会话删除同样改为先返回、后台回收；旧清单的 Token 回填队列只保存文件路径，不再持有大清单正文。

## 三、删除历史抓包

左侧历史支持单条 / 批量 / 整会话删除：

1. 点看板顶栏「管理：关闭」切换为「管理：开启」。
2. 左侧每个历史请求行会出现复选框和单条删除按钮：
   - 单条：点该行的删除按钮。
   - 全选：点「全选 (n)」勾选当前列出的全部请求；再点一次（按钮变为「取消全选 (n)」）全部取消。
   - 反选：点「反选」把当前勾选状态取反，适合只留少数几条。
   - 批量：勾选多条后点「删除选中 (n)」。
   - 整会话：点「删除本会话」删除当前会话的全部抓包。
3. 每次删除都会弹确认框，删除不可撤销。

> `n` 是条目总数：左侧会把同一请求的多次重试折叠成一行，勾选该行会连带勾选它的
> 全部重试子条目，所以 `n` 通常大于左侧可见行数。

删除只移除该请求的清单文件，并按引用回收不再使用的 `blobs\` 分片；其他已打开的看板
会通过 SSE 同步移除对应行。命令行等价入口：

```powershell
& ".\runtime\node.exe" ".\ccglass\bin\ccglass.js" rm-entry "<会话>/<序号>" --dir "$env:USERPROFILE\.ccglass\codex-desktop"
```

一次可传多个 `<会话>/<序号>`；全部 id 都未命中时进程以非零码退出。

## 四、工作原理

```
Codex  ->  ccglass 代理 127.0.0.1:9911  ->  本地中转代理 127.0.0.1:8787  ->  既有中继 127.0.0.1:57321  ->  上游 API
                     |
                     +->  中文看板 127.0.0.1:9912
```

- `9911`：ccglass 抓包代理端口，Codex 的实际出口。
- `9912`：看板端口，本程序内置窗口打开的就是它。
- `8787`：本地 schema 代理，负责请求改写后转发到既有 `57321` 中继；不要让它直连 `https://apihub.veletis.com`，否则可能因缺少中继鉴权返回 `401 invalid_api_key`。
- `57321`：既有本地中继，负责上游账号鉴权。

程序启动时会自动检查 `C:\Users\<用户名>\.codex\config.toml` 里 `[model_providers.custom]` 的 `base_url`：

- 如果已经是 `http://127.0.0.1:9911/v1`，不做任何改动。
- 如果不是，会自动改为该地址，并在改动前把原文件备份到：
  `C:\Users\<用户名>\.codex\backups\ccglass\config.toml.bak_<时间戳>`

如果当前配置使用 `model_provider = "openai"`，Codex 实际读取的是根级 `openai_base_url`；此时也必须将它设为 `http://127.0.0.1:9911/v1`，并重启 Codex。当前版本的自动检查只覆盖 `[model_providers.custom].base_url`，不会自动改写 `openai_base_url`。

## 五、关闭与后台运行

- 关闭窗口只关闭看板界面，后台统计服务会继续运行在 `9911` / `9912`。
- 这样关闭看板不会中断 Codex 正在进行的对话。
- 再次双击 `CodexTokenGlass.exe` 会直接复用已在运行的服务，不会重复启动。

如需彻底停止统计服务（同时 Codex 将无法再走 `9911`，需要先把 `base_url` 改回 `8787`）：

```powershell
Get-NetTCPConnection -LocalPort 9911 -State Listen |
  Select-Object -ExpandProperty OwningProcess -Unique |
  ForEach-Object { Stop-Process -Id $_ -Force }
```

## 六、日志与数据位置

| 内容 | 路径 |
| --- | --- |
| 抓包数据目录 | `%USERPROFILE%\.ccglass\codex-desktop` |
| 服务运行日志 | `%USERPROFILE%\.ccglass\codex-desktop\service.log` |
| 配置备份 | `%USERPROFILE%\.codex\backups\ccglass\` |
| 内置窗口缓存 | `%LOCALAPPDATA%\CodexTokenGlass\WebView2` |

命令行查看用量汇总：

```powershell
& ".\runtime\node.exe" ".\ccglass\bin\ccglass.js" usage --dir "$env:USERPROFILE\.ccglass\codex-desktop"
```

## 七、目录说明

| 目录 / 文件 | 说明 |
| --- | --- |
| `CodexTokenGlass.exe` | 桌面主程序（自带 .NET 运行时，单文件） |
| `StartService.cmd` | 仅启动后台统计服务的脚本，供开机自启任务使用 |
| `runtime\node.exe` | 内置 Node 运行时 |
| `ccglass\` | ccglass 源码与依赖（含中文化后的 `web\` 看板） |
| `ccglass\web\` | 看板前端，中文界面在这里 |

开机自启任务 `CodexTokenGlass` 指向 `StartService.cmd`，登录后自动拉起 `9911` / `9912`，
这样即使不打开看板窗口，Codex 的流量也会被持续统计。

## 八、常见问题

**看板没有数据？**
确认 Codex 的 `config.toml` 中 `base_url` 为 `http://127.0.0.1:9911/v1`，然后重启 Codex 使配置生效。只有经过 `9911` 的请求才会被统计。

**提示端口被占用？**
说明统计服务已在运行，程序会自动复用；如果看板打不开，先查看 `service.log`。

**需要恢复成直连？**
把 `config.toml` 中 `base_url` 改回 `http://127.0.0.1:8787/v1`，或直接从 `backups\ccglass\` 取回备份文件。

## 九、上游与许可

- 上游项目：https://github.com/jianshuo/ccglass
- 本工具仅做 Windows 桌面封装与中文化，未修改 ccglass 的抓包与计费逻辑。
- 许可遵循上游仓库的 LICENSE。

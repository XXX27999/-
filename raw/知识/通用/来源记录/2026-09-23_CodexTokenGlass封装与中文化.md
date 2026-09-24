# 2026-09-23 CodexTokenGlass 封装与中文化

> 类型：来源记录
> 主题：把 ccglass 封装为中文化 Windows 桌面工具，接入 Codex Token 消耗查询
> 适用范围：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\`
> 证据状态：项目实测（本机 2026-09-23 全流程验证通过）
> 来源：用户需求「制作成一个软件并完成中文化，存放于知识库工具中」；上游 https://github.com/jianshuo/ccglass
> 更新时间：2026-09-23
> 关联主题：[CodexTokenGlass 正文](../工具与流程/CodexToken消耗查询工具.md)
> 排除范围：不改 UGC 工程蓝图 / Lua / UI 资产；未触碰 `raw/docs/`
> 官方依据：无官方文档；ccglass 行为来自其源码 `src/cli.js`、`src/server.js`、`src/log-cli.js`

## 需求

1. 查看 https://github.com/jianshuo/ccglass 并按其方式接入 Codex Token 消耗查询。
2. 明确「ccglass 的打开软件在哪」。
3. 制作成软件、完成中文化，存放于 `D:\知识库\和平精英绿洲起源\工具` 下。

## 实施

### 1. 接入方式

- 采用 `ccglass proxy --provider codex` 常驻模式（不是 `ccglass codex` 客户端包装模式），因为 Codex 桌面端自己拉起进程。
- 端口：`9911` ccglass 代理、`9912` 看板、`8787` 保持既有 schema 中转不变。
- `C:\Users\Administrator\.codex\config.toml` 中 `[model_providers.custom]` 的 `base_url` 改为 `http://127.0.0.1:9911/v1`。
- 原配置备份：`C:\Users\Administrator\.codex\backups\ccglass\config.toml.bak_20260923_130938`。

### 2. 桌面封装

- 工程：`C:\Users\Administrator\Documents\Codex\2026-09-23\https-github-com-jianshuo-ccglass-https\work\CodexTokenGlass`。
- 技术：.NET 8 WPF + WebView2，单文件自包含发布（`CodexTokenGlass.exe` 约 71.99 MB）。
- 内置 `runtime\node.exe`（复制自 `C:\Program Files\nodejs\node.exe`）与 `ccglass\`（含 `node_modules`，来源 `C:\Users\Administrator\AppData\Local\ccglass\app`，GitHub HEAD 版本）。

### 3. 中文化范围

- `ccglass\web\index.html`：标题、实时状态、主题、错误、对比、汇总、空状态。
- `ccglass\web\app.js`：会话列表、模型筛选、会话统计、延迟趋势、请求概览、耗时 / Token / 缓存 / 费用卡片、汇总页、按模型 / 按会话 / 按时间表格、实时流工具栏、请求详情页签与流程视图标签、`TAG_INFO` 全部弹窗说明、`TAG_LABELS` 中文标签、diff 视图文案、导出标签。
- `ccglass\web\stream.css`：展开 / 收起切换文案。
- `ccglass\src\log-cli.js`：`usage` 命令行汇总输出（合计、按模型、按会话，表格列头保留 ASCII 对齐并附中文列名说明行）。
- 保留不译：`tool_use` / `tool_result` / `cacheR` 等协议字段名、JSON 字段名、模型名。

### 4. 关键坑

| 现象 | 根因 | 处理 |
| --- | --- | --- |
| exe 启动报缺少内置 Node | 单文件发布把 `runtime\node.exe` 打进 exe，`AppContext.BaseDirectory` 下没有该文件 | csproj 给 `runtime\**`、`ccglass\**` 加 `ExcludeFromSingleFile="true"` |
| 关窗后 Codex 断链 | `RedirectStandardOutput` 的管道随窗口关闭断开，且 `OnClosed` 里 `Kill` 了服务 | 日志改由 `cmd /c ... >> service.log 2>&1` 持有，移除 `Kill` |
| 二次启动抢端口 | 两个实例同时尝试绑定 `9911` | 启动前探 `9912/api/sessions`，未就绪再探 `9911` 监听，是则等待复用 |
| `ccglass proxy` 报未知子命令 | npm 上 `ccglass@1.1.2` 缺 `proxy` | 改用 GitHub HEAD 源码 |

## 验证记录（实测）

| 项目 | 结果 |
| --- | --- |
| 冷启动部署版 exe | `9911` / `9912` 由 `D:\知识库\...\runtime\node.exe` 监听，`/api/sessions` 返回 200 |
| 真实请求抓取 | `POST http://127.0.0.1:9911/v1/responses` 返回 200，`requestCount` 2→3、`usd` 0.048424→0.049118 |
| 关窗存活 | 结束 exe 进程后，`9911/9912` 仍由同一 node 进程（PID 35476）持有 |
| 二次启动复用 | 重新启动 exe 后仍只有 1 个内置 node 进程，未抢端口 |
| 中文 CLI | `usage --dir %USERPROFILE%\.ccglass\codex-desktop` 输出中文汇总 |
| 中文看板 | 截图确认标题、页签、卡片、按钮、工具栏均为中文；`app.js` 内含「正在对比 / 等待中 / 查看文档 / 向模型提供了 / Token/秒」等替换 |
| 开机自启 | 计划任务 `CodexTokenGlass` 指向 `StartService.cmd`，登录触发，最高权限 |

## 交付路径

- 工具：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\`
- 说明：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\README.md`
- 后台启动：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\StartService.cmd`
- 桌面快捷方式：`C:\Users\Administrator\Desktop\ccglass Token 看板.lnk`
- 开始菜单快捷方式：`C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ccglass Token 看板.lnk`

## 待查证

1. 上游是否需要为不同 provider 做自动配置改写。
2. 「未计量请求」成因未逐条核对。
3. 内置模型单价表与实际账单的逐模型偏差未比对。

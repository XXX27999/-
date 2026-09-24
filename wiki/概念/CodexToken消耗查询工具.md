# Codex Token 消耗查询工具

> 类型：概念索引
> 来源：[2026-09-23 CodexTokenGlass 封装与中文化](../../raw/知识/通用/工具与流程/CodexToken消耗查询工具.md)
> 正文位置：[CodexTokenGlass 正文](../../raw/知识/通用/工具与流程/CodexToken消耗查询工具.md)
> 最近更新：2026-09-24

## 索引摘要

把开源工具 ccglass 封装成 Windows 桌面软件并完整中文化，用于查询 Codex 每次请求的 Token 消耗、缓存命中、耗时与费用，放在知识库工具目录下，可直接双击使用。

要点：

1. **入口**：`D:\知识库\和平精英绿洲起源\工具\CodexTokenGlass\CodexTokenGlass.exe`（双击打开中文看板；内置 `runtime\node.exe` 与 `ccglass\`，无需另装 Node）。
2. **链路**：`Codex -> 127.0.0.1:9911（ccglass 抓包）-> 127.0.0.1:8787（既有中转）-> 上游`；看板在 `127.0.0.1:9912`。
3. **开关**：`C:\Users\<用户名>\.codex\config.toml` 的 `[model_providers.custom]` `base_url` 必须为 `http://127.0.0.1:9911/v1`，改完重启 Codex；程序启动会自动检查并备份改写。
4. **常驻语义**：关闭窗口只关看板，`9911`/`9912` 继续运行，不打断 Codex 对话；计划任务 `CodexTokenGlass` 登录自启后台服务。
5. **数据位置**：`%USERPROFILE%\.ccglass\codex-desktop`（含 `service.log`）；配置备份 `.codex\backups\ccglass\`。
6. **已打开的对话不改道**：`base_url` 改成 `9911` 后，必须重新打开对话才会被看板统计。2026-09-23 当前线程仍直连 `https://www.mcgrox.top/v1/responses`，所以实时会话是空的。
7. **流程消息粗估**：每条用户/助手消息旁显示 `≈` Token，只估正文，不是上游账单。
8. **历史删除（2026-09-24）**：顶栏「管理」开关后，左侧历史每行出现复选框与单条删除按钮，支持「全选 (n)」/「反选」/「删除选中 (n)」批量删除与「删除本会话」；勾选按重试链展开，故 n 是含重试子条目的总数。后端单条 `DELETE /api/delete?id=<session>/<seq>`、整会话 `DELETE /api/delete?session=<name>`、批量 `POST /api/delete-batch`（一次 GC，几百条秒级），删除后回收 `blobs/` 孤儿分片并经 SSE 同步到其他看板；CLI 等价入口 `ccglass rm-entry`。
9. **合计口径（2026-09-24）**：「实际合计」= 总输入（含缓存）+ 输出，取自 `usage`；「预估合计」= 整个请求 JSON 加响应正文的字符估算。常数已重新标定为中文 `1.12` token/字、其余 `4.6` 字符/token，随数据增长复算偏差稳定在 ±1% 内。`web\app.js` 内同值常量必须与 `src\tokens.js` 同步。

- **Raw 正文**：[CodexTokenGlass 正文](../../raw/知识/通用/工具与流程/CodexToken消耗查询工具.md)
- **工具目录**：[CodexTokenGlass](../../工具/CodexTokenGlass/)
- **相关概念**：[Codex 上下文超限排障](./Codex上下文超限排障.md)、[AI 配置归档与软件调用全局提示词](./AI配置归档与软件调用全局提示词.md)

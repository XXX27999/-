# PIE 调试非法字符校验失败

> 类型：概念索引
> 来源：[Raw PIE 非法字符校验正文](../../raw/知识/通用/工具与流程/PIE调试非法字符校验失败.md)
> 最近更新：2026-09-24

## 索引摘要

PIE 上传 `CheckName` 会拦截 `%`、中文、空格、过长路径、非英文字母开头的文件名，以及 `$` 开头文件；脚本路径也不能含 `.` 或 `-`。弹窗常见为 `{filename} must begin with an alphabetic character.` 或 `{path} may contain the following characters: .-`，对应官方 `upload file name validation failed`。2026-09-24 实测：PowerShell `>$null` / `2>$null` 误落成的 0 字节 `$null` 会触发 `Content=$null may contain the following characters: $`、`CheckUploadFileNameFailed Result 10001` 并中断 PIE。后续复现确认，并发 Codex 会话在 `shell:"bash"` 下被按 `cmd.exe` 语义执行 `2>$null`，会先生成工程根 `$null`；PIE 再将其递归复制到 `Saved\UGCLinuxDebug\<项目名>\`。规则已加载不等于命令会自动合规，清理必须同时覆盖源文件与上传副本。

- **Raw 正文**：[PIE 调试非法字符校验失败](../../raw/知识/通用/工具与流程/PIE调试非法字符校验失败.md)
- **官方条目**：[20391 PIE调试失败原因与解决方案](../../raw/docs/wiki/常见问题/20391_PIE调试失败原因与解决方案.md)
- **内容层目录**：[工具与流程内容目录](../../raw/知识/通用/工具与流程/000_目录.md)
- **调试备份**：[调试备份存放](./调试备份存放.md)

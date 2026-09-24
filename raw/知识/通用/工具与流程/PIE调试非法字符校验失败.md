# PIE 调试非法字符校验失败

> 内容层：PIE 工程物理路径与上传文件名校验的实测排错记录
> 类型：通用知识
> 主题：PIE / 文件名校验 / 非法字符
> 适用范围：全局通用；项目具体文件名只作为案例
> 证据状态：官方确认（20391 文件名校验失败条目）+ 项目实测（`%` 路径、下划线开头文件名、pycache 点号连字符、`$null`、并发 Codex 会话命令触发）
> 来源：`raw/docs/wiki/常见问题/20391_PIE调试失败原因与解决方案.md`；IslandAuctionKing 编辑器日志 2026-08-26、2026-08-28、2026-09-04、2026-09-24；Codex 会话 `C:\Users\Administrator\.codex\sessions\2026\09\24\rollout-2026-09-24T14-25-07-01a0d216-d64a-7db3-ac18-ed5e2f9512f4.jsonl`
> 更新时间：2026-09-24
> 关联主题：PIE调试与热更新边界
> 排除范围：本页不覆盖 Lua 语法错误、非法 API、DS 崩溃；`lua file validation failed` 若紧跟 CheckName 失败，先当文件名问题处理
> 官方依据：`D:\知识库\和平精英绿洲起源\raw\docs\wiki\常见问题\20391_PIE调试失败原因与解决方案.md`

## 核心结论

PIE 复制工程到上传目录后会执行 `CheckName`。官方条目是 `PIE debug failed: upload file name validation failed`：工程中含特殊字符（如中文、空格）或路径过长时会失败，需改为仅含英文、数字和下划线的短文件名。

项目实测补充：文件名还不能以非英文字母开头。下划线、数字、`%`、连字符开头都会触发弹窗 `{filename} must begin with an alphabetic character.`，然后中断调试。隐藏目录（以 `.` 开头）是否完全排除，需按当前编辑器版本复核。

同一轮中断后，编辑器还可能再打 `PIE debug failed: lua file validation failed, debug interrupted`。官方把该条解释为 Lua 语法或逻辑错误；若它紧跟 CheckName 弹窗出现，先修文件名，不要直接当脚本语法问题。

## 可执行步骤

1. 在编辑器 Output Log / `ShadowTrackerExtra.log` 搜索 `must begin with an alphabetic character`、`may contain the following characters`、`CheckUploadFileNameFailed`、`上传文件名验证失败`。UGC 客户端/DS 运行日志通常没有这条。
2. 使用绝对路径扫描工程根目录，确认问题路径确实在项目目录内。
3. 对含 `%` 的路径使用 `-LiteralPath` 或等价安全 API 检查、重命名；禁止在 CMD 中直接执行会展开 `%SystemDrive%` 的删除命令。
4. 对备份和临时文件检查连字符、下划线、数字或特殊字符开头的名称；需要时改为英文字母开头。不要把 `_tmp_*.py`、`_mcp_tmp`、`__pycache__` 留在 UGC 工程。必须移到知识库备份目录 `D:\知识库\和平精英绿洲起源\备份\<项目名>\<YYYYMMDD>_<主题>\`，不能放进工程内 Backup/。
5. 专项检查 `$` 开头文件，尤其是 `$null`。PowerShell 的 `>$null` / `2>$null` 在工程目录被当成路径时会生成 0 字节 `$null`；工程根与上传副本 `Saved\UGCLinuxDebug\<项目名>\` 都要删净。
6. 先删工程根源文件，再删上传副本。若上传副本的创建时间晚于工程根文件，PIE 只是复制者，根因仍在工程根或外部命令。
7. 递归扫描处理结果，确认 `%`、下划线开头文件、`$null` 等非法名不再存在，再重新 PIE。
8. 若路径阶段通过但 PIE 仍失败，转查编辑器日志和客户端 LuaLog，不要把不同阶段的错误混为一谈。

## 常见错误

- 将项目内名为 `%SystemDrive%` 的目录当成真实系统盘路径操作。
- 在 CMD 中执行 `rmdir /s /q "%SystemDrive%"`，导致变量展开风险；必须使用绝对路径和字面量操作。
- 误以为 `Backup`、`Preview` 等非 Asset 目录不会参与工程路径检查。
- 将连字符、下划线开头等命名问题与蓝图或 Lua 逻辑错误混淆。
- 看到跟随出现的 `lua file validation failed` 就去改 Lua，忽略前面的 CheckName 弹窗。
- 在工程目录内用 `2>$null` 丢输出，生成 0 字节 `$null`，直到 PIE 上传校验失败才发现。
- 认为规则已经写入 `AGENTS.md` 或全局提示词后就不会再生成 `$null`。规则只约束后续命令，不会自动改写已发出的错误命令，也不会清理已经落盘的文件。
- 未确认执行 shell 就混用 PowerShell 重定向语法。`shell:"bash"` 在 Windows 包装层被按 `cmd.exe` 语义执行时，`2>$null` 会创建真实文件 `$null`。

## 2026-08-28 项目实测

- 项目根目录存在 `%SystemDrive%/ProgramData/Microsoft/Windows/Caches/cversions.2.db`。
- 在确认目录属于项目根目录后，保留目录内容并可逆重命名为 `SystemDriveCache_20260828`；随后递归扫描未发现 `%` 路径。
- 路径错误消失后，PIE 又因基础客户端 Lua 校验错误 `client/module/module_event.lua:124: attempt to index a nil value (global 'UpdateNoticeInGameUI')` 中断。该错误与非法路径问题独立。

## 2026-09-04 项目实测

- IslandAuctionKing 弹窗：`_tmp_lua_balance.py must begin with an alphabetic character.`
- 编辑器日志：`CheckUploadFileNameFailed, Result: 10001`，`PIE 调试失败：上传文件名验证失败`。
- 随后出现 `lua file validation failed, debug interrupted`，但 UGC 运行日志中没有该文件名。
- 证据页：`raw/IslandAuctionKing/日志证据/2026-09-04_PIE上传文件名校验失败.md`

- 同日 11:02 弹窗：`_mcp_tmp/__pycache__/patch_lua.cpython-312.pyc may contain the following characters: .-`
- 结论：脚本路径/文件名不能包含 `.` 或 `-`；Python `__pycache__` 与 `*.pyc` 必须移出工程后再 PIE。
- 证据页：`raw/IslandAuctionKing/日志证据/2026-09-04_PIE上传文件名校验失败.md`

## 2026-09-24 项目实测：`$null`

- 工程根与 `Saved\UGCLinuxDebug\IslandAuctionKing\` 各出现 1 个 0 字节 `$null`。
- 编辑器日志：`Content=$null may contain the following characters: $` → `CheckUploadFileNameFailed, Result: 10001` → `上传文件名验证失败`；随后 `CheckLua ... Result: 10001, Parent: CancelDebug`，但 luacheck `ReturnCode: 0`。
- 根因：PowerShell 的 `>$null` / `2>$null` 未被正确解析时被当成真实重定向文件名；在工程根两次复现（11:49、11:56:53）。
- 处理：删除两处 `$null` 后复扫工程，再重新 PIE；随后 `CheckUploadFileName Result 0`、`lua file validation passed`、`DS Ready`。
- 证据页：`raw/IslandAuctionKing/开发记录/2026-09-24_轮次详情角色技能底板可见性修复.md`
- 强制约束：工程内禁止创建或残留 `$null`；禁止在会落到工程目录的命令里写 `>$null` / `2>$null`；丢输出用 `2>&1 | Out-Null`、`| Select-Object -Last N` 或 `-ErrorAction SilentlyContinue`；收尾必须递归复扫 `$null` 为 0。

### 14:26 再次出现：并发会话命令与 PIE 复制

- 并发 Codex 会话 `01a0d216-d64a-7db3-ac18-ed5e2f9512f4` 已在会话开头加载了禁止 `$null` 的规则，但仍在工程工作目录发出 5 条含 `2>$null` 的命令。
- 2026-09-24 14:26:17，第一条违规命令以 `shell:"bash"` 发出：

```powershell
rg -n --hidden -S "匹配|补位|人机|机器人|Match|match|bot|Bot|Robot|20" Script Saved _JsonOutput 2>$null | Select-Object -First 400
```

- 该次输出为 `'Select-Object' is not recognized as an internal or external command`，进程码 `255`，符合 Windows `cmd.exe` 解析语义；同秒工程根出现 0 字节 `$null`。
- 14:26:31 同一命令改用 `shell:"powershell"` 重试并正常返回；因此文件由前一次 `shell:"bash"` 调用生成，不是 PowerShell 正常丢弃输出。
- 14:26:49，PIE 将工程内容递归复制到 `Saved\UGCLinuxDebug\IslandAuctionKing\`，上传副本出现第二个 0 字节 `$null`。上传副本晚于工程根文件 32 秒，证明 PIE 不是源头。
- 原会话只删除了工程根 `$null`，未确认上传副本；后续复扫发现上传副本仍在，删除后工程根、上传目录及整个 `ShadowTrackerExtra` 复扫为 0。
- 项目证据页：`raw/IslandAuctionKing/日志证据/2026-09-24_null文件再次出现与并发命令根因.md`

## 待查证

- 编辑器是否计划增加对 `Backup` 或其他自定义目录的打包排除配置。
- 当前编辑器版本对隐藏目录和所有特殊字符的完整扫描边界。
- 目录名以 `_` 开头（如 `_Backup`、`_JsonOutput`）是否与文件名同样失败；当前实测只确认文件名 `_tmp_lua_balance.py` 失败。
- `UpdateNoticeInGameUI` 缺失问题需要按基础客户端模块和启动环境继续排查。

## 相关页面

- [PIE 调试与热更新边界](./PIE调试与热更新边界.md)
- [绿洲通用 UI 编辑规范与排错](../UI与交互/绿洲通用UI编辑规范与排错.md)
- [调试备份存放](./调试备份存放.md)

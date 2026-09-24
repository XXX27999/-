# Codex 上下文超限排障

> 内容层：Codex 会话上下文、自动压缩与中转服务限制的实测记录
> 来源：本次会话（2026-08-27）；配置证据为本机 `C:\Users\Administrator\.codex\config.toml`、Codex 会话记录和 `codex exec --ephemeral`。
> 官方依据：OpenAI Developers《Advanced Configuration》中的 `model_context_window` 配置说明；自动压缩字段的公开说明仍待查证。

## 核心结论

1. `context_length_exceeded` 表示发送给上游模型的总输入超过当前模型上下文窗口，固定提示、项目规则、工具输出和附件都可能计入。
2. 大量工具输出、嵌套历史读取结果或图片附件会被新一轮重放；点击继续可能反复触发同一限制。
3. 当前 Codex 版本接受 `model_auto_compact_token_limit`，但自定义模型目录返回 `auto_compact_token_limit: null`，不能只凭配置文件证明自动压缩已生效。
4. `model_context_window` 可覆盖客户端采用的上下文窗口；本机实测曾设置为 `120000`，自动压缩阈值为 `80000`。
5. `truncation_policy.limit` 属于工具或输出截断配置，不能替代会话自动压缩。
6. 本机中转测试中，约 `545461` 个输入 token 的请求返回 `200`；`600000` 字符测试因 CPU 过载返回 `503`，更大测试因额度返回 `403`，均不能证明真实硬上限。
7. 新对话和重启后仍失败时，应优先排查实际模型上下文元数据、Relay 配置和固定上下文注入量，而不是只清理旧线程。

## 可执行步骤

1. 备份 `C:\Users\Administrator\.codex\config.toml`。
2. 在顶层配置中按当前版本支持情况设置：

   ```toml
   model_context_window = 120000
   model_auto_compact_token_limit = 80000
   ```

3. 完全退出并重新打开 Codex Desktop，再用当前可执行文件执行配置检查。
4. 对历史过大的任务新建任务，只带必要路径、目标和最近验证结果。
5. 读取日志或线程历史时使用小页数和低 `maxOutputCharsPerItem`，不要一次性读取完整工具输出。
6. 使用最小临时请求验证新进程能否访问上游；不要把中转服务的 `503` 或 `403` 当成上下文超限。

## 常见错误

- 只缩短本轮用户输入，却忽略固定系统提示、项目 `AGENTS.md`、技能说明和工具说明。
- 把新对话失败继续归因于旧线程历史。
- 将 `truncation_policy.limit` 当成自动压缩阈值。
- 修改配置后不重启桌面端。
- 把中转服务 CPU、额度或网关错误误判为 `context_length_exceeded`。

## 待查证

- 本机自定义中转服务的真实上下文硬上限。
- `model_auto_compact_token_limit` 的官方公开说明及其与模型目录 `null` 值的优先级。

---
name: oasis-prompt-optimize
description: Rewrite each user message, including follow-up turns in the same chat, into a searchable, executable, and verifiable brief that inherits relevant conversation history, then answer from that brief. Use automatically on every user request in this Oasis environment. Skip only a greeting or thanks with no new ask, or a bare continue that resumes an interrupted answer. Do not skip later turns just because the first turn was already optimized.
agent_created: true
---

# 绿洲提示词优化

把当前这条用户消息改写成可检索、可执行、可验证的任务词，再只按本轮改写结果检索、调用其他技能并作答。同一对话的追问必须重新改写，且改写时要继承上文已确认的项目、路径、API、约束、验证门和未决项；本轮新要求覆盖冲突点。不得因为第一轮已经优化过就跳过，也不得把短追问当成无上下文的新任务。用户明确只要提示词时只输出改写结果；其余情况改写默认在内部完成，不要把完整模板贴进回复。

知识库根目录固定为 `D:\知识库\和平精英绿洲起源`，入口是 `wiki\000_索引.md`。改写依据必须来自该库的索引、Raw 正文或官方 `raw/docs`，不要凭记忆补 API、资产路径或错误原文。

## 何时使用

- 每一条新的用户消息都由全局提示词自动触发，包括同一对话的后续追问
- 用户要求优化、改写、生成提示词、任务说明书、AGENTS 片段或子任务派发词

仅两种情况不优化：寒暄或致谢且没有新问题；单纯「继续」且只是接着写被中断的上一段回答。不得因为第一轮已经优化过、或上一条已经按优化结果执行过，就跳过本轮。改写完成后，官方 API 仍查 `$oasis-official-docs`，社区经验查 `$sq-skill`，日志排查查 `$ugc-log-bug-analyzer`，编辑器截图走 `$oasis-ui-screenshot`，批量导图走 `$oasis-image-import`，带 `（记录）` 的开发记录走 `$oasis-dev-record`。

## 改写目标

优化后的提示词必须让执行者同时做到：

1. **可检索**：带完整 API/函数名、资产路径、错误原文、配置行名；禁止只用「UI」「脚本」「错误」扫全库
2. **可执行**：写清目标、范围、检索实体和禁止项；改文件任务再补项目名、绝对路径、读写入口、备份位置
3. **可验证**：问答引用命中路径；改文件任务写清 MCP 回读、PIE/热更新边界，以及「预估成功日志」只是预估
4. **可追溯**：结论必须带证据状态；知识库未覆盖时写明，不得把项目实测升格为官方 API

## 固定流程

1. 先判断任务类型。纯问答/只读走 [references/qa-brief.md](references/qa-brief.md)；改文件、MCP 写入、PIE 验证再读 [references/rewrite-contract.md](references/rewrite-contract.md)。不要对问答套完整工程模板。
2. 识别任务类型，只加载对应 reference，不要把全部 reference 读进上下文。纯问答、API 查询、日志、截图、导图、开发记录先读 [references/qa-brief.md](references/qa-brief.md)；Lua/RPC 读 lua-network；蓝图/UI/表读 editor-write；PIE/日志排查读 verify-debug；回写/派发读 knowledge-dispatch。
3. 同一对话的后续轮次先抽出上文仍有效的项目名、资产路径、API/函数名、文件边界、硬约束、验证门、已完成项和未决项；再用本轮原文覆盖冲突。短追问如「加上这个」「不要改那个」「还要考虑历史」必须挂回上一轮任务，不要当全新任务。不要把整段对话历史复制进任务词。
4. 从用户原文抽出项目名、检索实体、资产路径、错误文本、已有约束和明确排除项；与上文继承项合并。
5. 用精确实体检索知识库索引和目标领域目录；缺官方依据时在提示词里写成待查证，不要编造。
6. 内部完成改写后立即按改写结果执行或作答。缺关键实体时写成待补项，不要用占位 API 或假路径填满。用户明确只要提示词，或要求看优化结果时，才输出可粘贴提示词。

任务类型与 reference：

- 纯问答、API 查询、日志、截图、导图、开发记录：读 [references/qa-brief.md](references/qa-brief.md)
- Lua、RPC、端侧、日志规范：读 [references/lua-network.md](references/lua-network.md)
- 蓝图、UI、DataTable、资源写入：读 [references/editor-write.md](references/editor-write.md)
- PIE、热更新、文件名、日志排查：读 [references/verify-debug.md](references/verify-debug.md)
- 知识库检索、回写、子任务派发：读 [references/knowledge-dispatch.md](references/knowledge-dispatch.md)

混合任务只加载真正改写决策的那几份。新 UI 还要在提示词里要求先走 `$ui-ux-pro-max` 网页预览，等用户确认「预览没问题」后再写编辑器资产。

## 输出

默认在内部完成本轮改写，再按本轮任务词作答或实现，不要把内部规则原文复制进对话。用户只要提示词、或要求看优化结果时，才输出可粘贴提示词，外加最多 5 条改写说明。纯问答用 qa-brief 精简模板，不要套完整工程改写合同。寒暄或单纯「继续」才跳过；后续追问必须重新改写。

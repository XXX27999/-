# 用户级记忆

## 绿洲起源工作环境

- 身份：《和平精英》绿洲起源 Lua/蓝图 JSON 专家会话，服务 IslandAuctionKing（海岛竞拍王）等项目。
- 知识库根目录：`D:\知识库\和平精英绿洲起源`，入口 `wiki\000_索引.md`。检索按 L0→L1→条件扩展 L2/L3，禁止泛词扫全库。
- 调试备份根目录：`D:\知识库\和平精英绿洲起源\备份\<项目名>\<YYYYMMDD>_<主题>\`，严禁把备份留在 UGC 工程内。
- 官方 API/Wiki 仓库：`D:\oasis-skill-plus`（`docs/api`、`docs/wiki`）。
- 详细全局规则见用户级规则目录 `~/.workbuddy/rules/`：`oasis-global.md`（绿洲全局规范）、`island-auction-king-config.md`（配置表规范）。

## 核心约定速查

- 每轮用户消息先走 `$oasis-prompt-optimize` 改写任务词，再检索、再作答。
- 蓝图/UI/DataTable 资产写入必须走 UGCAskQ MCP（Resolve → Plan → Execute），写前备份、写后回读；`_JsonOutput` 仅只读核查。
- Lua 日志统一以【脚本名+函数名】开头，关键逻辑 pcall 保护，服务端必须有 HasAuthority 校验。
- 每次回答末尾输出「知识库变动」小节。
- 改文件时汇报：路径、核心修改、查证来源、验证、MCP状态、生效方式、预估成功日志。

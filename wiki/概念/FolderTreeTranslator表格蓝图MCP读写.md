# FolderTreeTranslator 表格蓝图 MCP 读写（概念索引）

> 本页只做导航，**完整正文、代码与验证记录在 Raw**：
> [FolderTreeTranslator 表格蓝图 MCP 读写](../../raw/知识/通用/工具与流程/FolderTreeTranslator表格蓝图MCP读写.md)

工具 `D:\知识库\和平精英绿洲起源\工具\FolderTreeTranslator` 从 1.4.0 起自带 DataTable 读写：
Python 直连 UGCAskQ MCP，按路径 / 表名定位表格，读取行数据，编辑后经 Plan → Execute 回写。

## 要点

- 定位走编辑器 `ue.resolve_asset`（返回 `load_path`；表的 `asset_class` 是 `UAEDataTable`），禁止拼路径。
- 写入流程：本地校验 → 写前备份 → `ue_plan_submit` → `ue_py(plan_id)` → 保存 → 回读比对。
- `data_table_add_row` 成功返回 `None`，**回读是唯一判据**。
- 配置表改动需重新 PIE 生效。
- **界面卡住不是 MCP 慢**：tkinter 工具的工作线程禁止直调 `after`（抛
  `RuntimeError: main thread is not in main loop`，线程静默死亡 → 界面假死），
  必须走「队列 + 主线程轮询」；1.5.1 起等待期显示「已等待 N 秒」并提供「中止」按钮。
- **1.5.2 布局与单例**：工具区改 `PanedWindow` 可上下拖拽（工具区 300~580、数据区 ≥120），
  数据树 / 编辑字段 / 变更队列按内容自动显隐横纵滚动条；表格窗口**单例**（重复打开复用同一窗口）。
- **行名规则（1.5.2 更正）**：行名是 DataTable 的 **FName 行键，不是文件名**，
  不受 UGC 工程文件命名规则约束，本地**只校验非空**；
  1.5.1 及之前的 `^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z0-9_]+)*$` 已废弃（中文 / 空格 / 连字符行名全部放行）。

## 相关

- [UGCAskQ MCP 能力矩阵](UGCAskQ-MCP能力矩阵.md)
- [蓝图与 MCP 写入流程](蓝图与MCP写入流程.md)
- [配置表驱动开发](配置表驱动开发.md)
- 来源：[2026-09-15 FolderTreeTranslator 表格 MCP 读写落地](../../raw/知识/通用/来源记录/2026-09-15_FolderTreeTranslator表格MCP读写落地.md)
- 来源：[2026-09-15 FolderTreeTranslator 表格窗口卡住修复](../../raw/知识/通用/来源记录/2026-09-15_FolderTreeTranslator表格窗口卡住修复.md)
- 来源：[2026-09-16 FolderTreeTranslator 表格窗口布局与交互修复](../../raw/知识/通用/来源记录/2026-09-16_FolderTreeTranslator表格窗口布局与交互修复.md)

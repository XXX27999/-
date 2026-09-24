# 2026-09-03 AuctionTestUI 仓库格缩小与预估价回标题行

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 仓库格子与预估价
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：用户仓库裁切图、UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionGlobalConfigTable
> 更新时间：2026-09-03
> 关联主题：UCanvasPanelSlot、AuctionTestUI 绿框情报红框仓库收敛、AuctionInfoPanelPresentationService.ApplyEstimatedHeadline
> 排除范围：不覆盖玩法仓库生成算法、结算仓库、PIE 运行态藏品刷新截图；未改 GridWidth/GridHeight=6
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md；ESlateVisibility Visible=0、Collapsed=1。知识库未覆盖仓库暗槽到格子的官方换算公式。

## 问题

用户截图显示 6x6 藏品格仍顶出仓库暗槽，标题行预估价消失。MCP 回读确认 `EstimatedValueText` 为 Collapsed，运行时估价写入 `WarehouseText`，但该控件叠在第一行格子上。

## 官方确认

Canvas 槽位通过 `UCanvasPanelSlot.SetPosition` / `SetSize` 写入。可见性使用 `ESlateVisibility`。DataTable 单字段修改使用 `data_table_modify_row(行名, 字段, 值)`。

## 项目实测

当前 `WarehousePanel=(1257.184,131.246,647.775x800.824)`。按上一轮有效 5 行网格相对面板比例重排：

- `CellButton01=(1286.091,209.104,89.572x80.082)`
- `CellButton06=(1786.506,209.104)`
- `CellButton36=(1786.506,654.004)`
- 第 6 行底边 734.086，位于页脚说明之上、面板底边 932.070 之内。

预估价：

- 运行时目标控件是 `WarehouseText`，不是折叠的 `EstimatedValueText`。
- 写入后 `WarehouseText=(1520.000,149.042,300.000x33.368)`，`Visible`，ZOrder=40，设计态文案 `-- 金币`，右对齐，避开右上角橙标。

配置表回读：

- `UI.TestWarehouse.StartX=1286.091`
- `UI.TestWarehouse.CellStep=100.083`
- `UI.TestWarehouse.CellSize=89.572`
- `UI.TestWarehouse.CellStepY=88.980` 未改

Lua `AuctionTestUIService.lua` 回退值已同步。`luaparse` 通过。

截图：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_WarehouseCellShrink_after3.png`

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_WarehouseCellShrink\`

## 生效

重新调试 PIE。本轮截图是编辑器设计态证据，不等同于 PIE 运行证据。
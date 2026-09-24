# 2026-09-03 AuctionTestUI 竞拍仓库网格收回暗槽

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 仓库网格
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：用户截图、UGCAskQ MCP 回读写入、FlaUI 设计态截图、源图 右侧竞拍仓库.png
> 更新时间：2026-09-03
> 关联主题：UCanvasPanelSlot、AuctionTestUI 网页预览红框美化、AuctionGlobalConfigTable
> 排除范围：不覆盖玩法仓库生成算法、结算仓库、PIE 运行态藏品刷新截图；未改 GridWidth/GridHeight=6
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md；ESlateVisibility 由 ue_read enum:ESlateVisibility 确认 Visible=0、Collapsed=1。知识库未覆盖源图暗槽到 UMG 的官方换算公式。

## 问题

用户截图显示右侧「唯一仓库」最后一行 6 格掉到页脚说明文字上方，左侧另有绿色方块覆盖。

## 官方确认

Canvas 槽位通过 `UCanvasPanelSlot.SetPosition` / `SetSize` 写入。可见性使用 `ESlateVisibility.Collapsed=1`。`compile_blueprint` 官方返回 None。DataTable 单字段修改使用 `data_table_modify_row(行名, 字段, 值)`。

## 项目实测

`WarehousePanel=(1322.667,131.246,584.296,800.824)`。源图 `右侧竞拍仓库.png` 为 519x754，主仓暗区约 y=96..637，页脚从 y=637 开始。

写入前：

- `CellButton01..30` 已按 5 行铺在暗槽内，步长约 X=90.275、Y=88.980，单格 80.794x80.082。
- `CellButton31..36` 落在 `(1334/1423/1512/1601/1690/1779, 715)`，越过页脚。
- 18 个 `CollectibleImage/Button` 设计态叠在 `(1334,270)` 且 `CollectibleImage.Visibility=1`，对应左侧绿块。

写入后 MCP 回读：

- `CellButton01=(1348.741,209.104)`，`CellButton31=(1348.741,654.004)`，`CellButton36=(1800.116,654.004)`，第 6 行底边 734.086，仍在面板底边 932.070 之内、页脚说明之上。
- `CollectibleImage/Button01-18` 移到 `(-2000,-2000)` 且 `Collapsed`，运行时仍由 `AuctionTestUIService.RefreshWarehouse` 按格子包围盒重新放置。

配置表 `AuctionGlobalConfigTable` 回读：

- `UI.TestWarehouse.StartX=1348.741`
- `UI.TestWarehouse.StartY=209.104`
- `UI.TestWarehouse.CellStep=90.275`
- `UI.TestWarehouse.CellStepY=88.980`（新增）
- `UI.TestWarehouse.CellSize=80.794`

Lua `AuctionTestUIService.GetTestUIConfig` 增加 `warehouseCellStepY`，藏品包围盒高度改用纵向格距。

截图：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_WarehouseGridFit_after.png`

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_WarehouseGridFit\`

## 生效

重新调试 PIE。本轮截图是编辑器设计态证据，不等同于 PIE 运行证据。

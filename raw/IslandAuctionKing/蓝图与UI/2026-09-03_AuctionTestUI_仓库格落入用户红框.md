# 2026-09-03 AuctionTestUI 仓库格落入用户红框

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 仓库 6x6 格子
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：用户红框裁切图、UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionGlobalConfigTable、AuctionTestUIService.lua
> 更新时间：2026-09-03
> 关联主题：UCanvasPanelSlot、AuctionTestUI 仓库格缩小与预估价回标题行、AuctionTestUI 绿框情报红框仓库收敛
> 排除范围：不覆盖玩法仓库生成算法、结算仓库、PIE 运行态藏品刷新截图；未改 WarehousePanel / 标题行 / 页脚；未改 GridWidth/GridHeight=6
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md；ESlateVisibility Visible=0、Collapsed=1。知识库未覆盖用户红框到画布的官方换算公式。

## 问题

用户仓库裁切图要求 6x6 藏品格全部落入红框。上一轮格子仍越过红框上沿和右沿：CellButton01.y=209.104，CellButton06 右缘=1876.078。页脚“未选择藏品 / 藏品图鉴”保持在红框下方。

## 官方确认

Canvas 槽位通过 `UCanvasPanelSlot.SetPosition` / `SetSize` 写入。可见性使用 `ESlateVisibility`。DataTable 单字段修改使用 `data_table_modify_row(行名, 字段, 值)`。

## 项目实测

用户红框（裁切像素）约 `(13.5,64.5)-(438.5,484.5)`。以 CellButton02 / CellButton07 未裁切井口为锚点换算到画布后，红框约 `(1293.430,236.329)-(1860.567,794.114)`。

MCP 写入后回读：

- `WarehousePanel=(1257.184,131.246,647.775x800.824)` 未改
- `WarehouseTitleText=(1300,176)`、`WarehouseText=(1460,176,"-- 金币")` 未改
- `CellButton01=(1295.5,238.5,85.2x85.2)`
- `CellButton06=(1772.5,238.5)` 右缘 1857.7
- `CellButton31=(1295.5,706.0)`
- `CellButton36=(1772.5,706.0)` 底缘 791.2
- `inside_red` 左/上/右/下均为 true；格子在标题行之下、页脚 SelectedText.y=816 之上
- `CollectibleImage01` / `CollectibleButton01` 仍为 Collapsed / `(-2000,-2000)`
- `EstimatedValueText` 仍为 Collapsed

配置表回读：

- `UI.TestWarehouse.StartX=1295.5`
- `UI.TestWarehouse.StartY=238.5`
- `UI.TestWarehouse.CellStep=95.4`
- `UI.TestWarehouse.CellStepY=93.5`
- `UI.TestWarehouse.CellSize=85.2`

Lua 回退值已同步到 `AuctionTestUIService.lua`。本机未安装 luaparse；脚本仅改 5 个默认数值，`function`/`end` 计数仍为 49/49。

截图：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_WarehouseCellFitRedBox_after.png`

参照图：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_WarehouseRedBox_ref.png`

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_WarehouseCellFitRedBox\`

## 生效

重新调试 PIE。本轮截图是编辑器设计态证据，不等同于 PIE 运行证据。

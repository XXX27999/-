# 2026-09-03 AuctionTestUI 绿框情报面板与红框仓库收敛

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 中间情报面板与右侧仓库尺寸
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：用户绿框/红框标注图、UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionGlobalConfigTable
> 更新时间：2026-09-03
> 关联主题：UCanvasPanelSlot、AuctionTestUI 仓库网格收回暗槽、AuctionInfoPanelPresentationService
> 排除范围：不覆盖玩法仓库生成算法、结算仓库、PIE 运行态藏品刷新截图；未改 GridWidth/GridHeight=6；未改左侧席位
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md；ESlateVisibility 由 ue_read enum:ESlateVisibility 确认 Visible=0、Collapsed=1。知识库未覆盖截图像素到 1920x1080 画布的官方换算公式。

## 问题

用户标注图要求：中间竞拍情报收到绿色框，右侧唯一仓库收到红色框，区域内控件不得越界。此前只重排了仓库格子，面板本身仍偏宽，情报卡右缘和仓库格仍越过素材边界。

## 官方确认

Canvas 槽位通过 `UCanvasPanelSlot.SetPosition` / `SetSize` 写入。可见性使用 `ESlateVisibility.Collapsed=1`。`compile_blueprint` 官方返回 None。DataTable 单字段修改使用 `data_table_modify_row(行名, 字段, 值)`。

## 项目实测

用户标注图 `codex-clipboard-5b28bb1a-c02f-4a2e-9a62-6c9a67b7ebd9.png` 为 1928x1048。按描边色 `145,211,0` / `250,81,81` 得到：

- 绿框截图像素 `(633.5,240.5)-(1137.5,842.5)`
- 红框截图像素 `(1155.5,239.5)-(1631.5,842.5)`

用顶栏橙框 `x=214..1633` 对应画布 `10.667..1906.963` 换算后：

- `RightDetailPanel=(571.259,131.246,673.526x800.824)`
- `WarehousePanel=(1268.851,131.246,636.108x800.824)`

MCP 回读写入后：

- `IntelCardBackground01-05=(601.676,*,612.691x75.633)`，右缘 1214.367，绿框右缘 1244.785 之内。
- `RoundProgressDot05=(1161.933,184.000,34x8)` 仍在绿框内。
- `CellButton01=(1297.237,209.104,87.958x80.082)`，`CellButton36=(1788.637,654.004)`，第 6 行底边 734.086，红框底边 932.070 之内。
- `CollectibleImage/Button01-18` 设计态仍在 `(-2000,-2000)` 且 `Collapsed`。

配置表 `AuctionGlobalConfigTable` 回读：

- `UI.TestWarehouse.StartX=1297.237`
- `UI.TestWarehouse.CellStep=98.280`
- `UI.TestWarehouse.CellSize=87.958`
- `UI.InfoCard.Left=580`
- `UI.InfoCard.Width=621`
- `UI.InfoCard.IndexLeft=594`
- `UI.InfoCard.TextLeft=646`
- `UI.InfoCard.TextWidth=522`
- `UI.InfoCard.WrapUnits=70`

Lua 回退值已同步：`AuctionTestUIService.lua`、`AuctionInfoPanelPresentationService.lua`。`luaparse` 语法检查通过。

截图：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_GreenRedPanelFit_after.png`

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_GreenRedPanelFit\`

## 生效

重新调试 PIE。本轮截图是编辑器设计态证据，不等同于 PIE 运行证据。
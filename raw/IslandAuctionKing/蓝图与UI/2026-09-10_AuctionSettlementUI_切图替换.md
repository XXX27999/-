# 2026-09-10 AuctionSettlementUI 切图替换

> 类型：项目蓝图与 UI 记录
> 主题：AuctionSettlementUI 按用户结算参考图替换切图，删除“正在展示”文本控件
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionSettlementUI`、`Script/Function/AuctionSettlementUIService.lua`、`UIConfigTable` 的 `UI.Settlement.*` 行、贴图目录 `/IslandAuctionKing/Asset/TuPian/AuctionUI/Settlement`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；未截设计态；未启动 PIE
> 来源：用户参考图与切图 `C:\Users\Administrator\Desktop\素材\竞拍\结算`；用户明确跳过网页预览并要求删除“正在展示什么藏品”文字控件
> 更新时间：2026-09-11
> 关联主题：[2026-09-04_结算仓库名称框溢出修复](./2026-09-04_结算仓库名称框溢出修复.md)、[2026-09-04_结算放大镜灰块与估价文本修复](./2026-09-04_结算放大镜灰块与估价文本修复.md)、[资源导入与路径规范](../../知识/通用/配置与数据/资源导入与路径规范.md)
> 排除范围：未改 AuctionHouseSelectUI / AuctionPropSelectUI / AuctionTestUI / ZhuJieMian
> 官方依据：`D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md`；`D:\oasis-skill-plus\docs\api\class\Others\UImage.md`（`SetBrushFromTexture`）；`D:\oasis-skill-plus\docs\api\class\Others\UGCTweenSystem.md`

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_SettlementArt\`

含 `AuctionSettlementUI.uasset`、`AuctionSettlementUI.lua`、`AuctionSettlementUIService.lua`、`UIConfigTable.uasset`、英文切图副本、MCP 计划与 Python 载荷。

## 二、贴图导入

plan_id：`plan_16806676_2c4a9079`

20 张 PNG 导入到 `/IslandAuctionKing/Asset/TuPian/AuctionUI/Settlement`。回读抽样 `SettlementPanel` / `SettlementTitle` / `SettlementSkipButton` / `SettlementConfirmText` 五项属性均为 `(LODGroup, MipGenSettings, CompressionSettings, CompressionQuality, SRGB) = (16, 13, 0, 5, True)`。

## 三、蓝图绑定

plan_id：`plan_16806831_23344a28`

- 删除 `CurrentCollectibleTip` / `TipHBox` / `TipNameText` / `TipValueText`
- 折叠 `TitleBackgroundText`（AUCTION ENDED）与 `MainTitleText`
- 新增切图控件：`SettlementTitleImage`、`LabelFinalPriceImage`、`LabelItemValueImage`、`LabelProfitImage`、`LabelExpImage`、`LabelWarehouseValueImage`、`SkipTextImage`、`ConfirmTextImage`、`AvatarFrameImage`、`PortraitFrameImage`
- 底板 `SettlementBackground` 绑 `SettlementPanel`，左右面板绑左右切图，跳过/确认钮绑灰色/红色按钮切图，按钮文字用切图而不是文本框

回读坐标：

- `SettlementBackground` 141,60 / 1639x960，画刷 `SettlementPanel`
- `LeftPanel` 161,80 / 871x828，画刷 `SettlementLeftPanel`
- `RightPanel` 1052,80 / 704x825，画刷 `SettlementRightPanel`
- `SkipButton` 841,936 / 254x68
- `CloseButton` 1107,936 / 261x68
- `CurrentCollectibleTip` / `TipNameText` / `TipValueText` = missing

## 四、配置表

plan_id：`plan_16777825_ff222dda`

`UIConfigTable` 新增 `UI.Settlement.Texture.*` 与 `UI.SettlementWarehouse.OriginOffsetX=36`、`OriginOffsetY=250`。回读 `UI.Settlement.Texture.Panel` 路径正确。

## 五、Lua

`AuctionSettlementUIService.lua`：删除展示提示条依赖；动态金额只写 `￥` 数字并上金色；仓库覆盖层兜底坐标改为 RightPanel `1052,80`。`luaparser` 语法通过。按钮仍走 `AuctionUIMotionService.PlayPress`，打开仍走 `PrepareFadeIn` / `PlayFadeIn`。

## 六、待查证

- 未启动 PIE。动态金额、仓库格子与头像立绘需重新调试 PIE 验证。
- 已打开的 UI 编辑器页签需要关闭后重新打开才能看到切图。
- 仓库格子切图 `SettlementGrid` 已导入，但运行时仓库格仍读 `ImageMaterialTable` 的“格子”行，未改该表。

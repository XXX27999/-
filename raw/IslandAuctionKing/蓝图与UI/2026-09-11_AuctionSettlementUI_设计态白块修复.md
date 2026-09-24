# 2026-09-11 AuctionSettlementUI 设计态白块修复

> 类型：项目蓝图与 UI 记录
> 主题：AuctionSettlementUI 1920×1080 设计态白条/白头像
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionSettlementUI`、`Script/Function/AuctionSettlementUIService.lua`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；设计态截图未刷新；未启动 PIE
> 来源：用户 1920×1080 结算参照图 `C:\Users\Administrator\Desktop\素材\竞拍\结算\参考图.png`；用户编辑器现状截图 `C:\Users\ADMINI~1\AppData\Local\Temp\codex-clipboard-958ed9e3-2e64-40b1-b1c1-3bd972fd7cc4.png`；MCP 回读 `plan_16798125_26953c2a`
> 更新时间：2026-09-11
> 关联主题：[2026-09-10_AuctionSettlementUI_切图替换](./2026-09-10_AuctionSettlementUI_切图替换.md)、[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)
> 排除范围：未改 AuctionHouseSelectUI / AuctionPropSelectUI / AuctionTestUI / ZhuJieMian；未改结算切图资产
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md`（`SetPosition` / `SetSize`）；`D:\oasis-skill-plus\docs\api\class\Others\UImage.md`（`SetBrushFromTexture`）；`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md`（Collapsed=1，HitTestInvisible=3）

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_SettlementWhiteFix`

含 `AuctionSettlementUI_before.uasset`、`AuctionSettlementUI.lua`、`AuctionSettlementUIService.lua`、MCP 计划与写入脚本。

## 二、对照结论

桌面参照图已是 1920×1080。附件旧参照仍是 1639×960，不能再硬拉切图。用户最新编辑器截图里底板已经铺满 1920 舞台，但还有两处设计态白块：

1. 左右头像框内部白矩形：`PlayerAvatarImage` / `CharacterPortraitImage` 的 `Brush.ResourceObject=None`，`Visibility=HitTestInvisible(3)`。
2. 右栏「竞拍仓库」标题下白条：`AssetTitleText` 当时是 `1067,28 / 825x72`，盖住整个右栏顶带；`RightVBox` 里还留着空的 `AssetPanelHeader` / `ValueHBox`。

空 `UImage` 在设计态会画成白矩形，这是项目实测，不是官方 API 保证。

## 三、蓝图写入

plan_id：`plan_16798125_26953c2a`

回读：

- `PlayerAvatarImage` / `CharacterPortraitImage`：`Visibility=Collapsed(1)`，空画刷保留给运行时贴图
- `RightVBox` / `AssetPanelHeader` / `ValueHBox` / `WarehouseFrame` / `LeftVBox`：`Collapsed(1)`
- `AssetTitleText`：`1288,36 / 380x48`，`Visibility=HitTestInvisible(3)`
- `SettlementBackground` 仍是 `0,0 / 1920x1080`，画刷 `SettlementPanel`
- `LeftPanel` `23,23 / 1020x931`，`RightPanel` `1067,23 / 825x928`
- 头像框切图 `AvatarFrameImage` / `PortraitFrameImage` 仍可见

## 四、Lua

`AuctionSettlementUIService.lua`：打开结算时先折叠空头像；只有 `AvatarTexture` / `CharacterTexture` 存在才 `SetBrushFromTexture` 并设为 `HitTestInvisible`。`luaparser` 语法通过。

## 五、截图

FlaUI `--list` 枚举不到提权的 `ShadowTrackerExtraUGCEditor`。`PrintWindow` 抓到的窗口矩形是白图，不能当设计态验收。已打开的 UI 编辑器页签需要关闭后重新打开才能看到本次折叠结果。

## 六、待查证

- 未启动 PIE。运行时头像/立绘有贴图时应重新出现。
- 右栏切图 `SettlementRightPanel` 已烘焙「竞拍仓库」字，`AssetTitleText` 是否还要叠一层待对照关页签后的设计态。

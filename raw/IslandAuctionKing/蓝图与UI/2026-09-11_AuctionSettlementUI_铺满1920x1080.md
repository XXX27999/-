# 2026-09-11 AuctionSettlementUI 铺满 1920x1080

> 类型：项目蓝图与 UI 记录
> 主题：AuctionSettlementUI 按编辑器 1920×1080 基准铺满舞台
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionSettlementUI`、`Script/Function/AuctionSettlementUIService.lua`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；未刷新设计态截图；未启动 PIE
> 来源：用户纠正「不是要已1920*1080为基准吗」；用户现状 `C:\Users\ADMINI~1\AppData\Local\Temp\codex-clipboard-c274d2c1-947c-452d-8803-65f0a8077c96.png`；MCP 回读 `plan_16803991_65372dc2`
> 更新时间：2026-09-11
> 关联主题：[2026-09-11_AuctionSettlementUI_切图原尺寸居中](./2026-09-11_AuctionSettlementUI_切图原尺寸居中.md)、[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)
> 排除范围：未改 AuctionHouseSelectUI / AuctionPropSelectUI / AuctionTestUI / ZhuJieMian
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md`（`SetPosition` / `SetSize`）；`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md`

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_SettlementFill1920`

## 二、纠正

上一轮把 `SettlementBackground` 写成 `141,60 / 1639x960`，结算底板缩在 1920 虚线框中间，标题和经验文字溢到框外。用户纠正：编辑器 UI 修改基准是 1920×1080。本轮覆盖居中方案。

切图原像素仍是 1639×960，铺满 1920 会拉伸。这是用户明确要求的编辑器基准，不是切图原生比例。重复的烘焙标题图和空头像继续折叠，避免再画出框外白块。

## 三、蓝图写入

plan_id：`plan_16803991_65372dc2`

回读：

- `RootSizeBox` 1920×1080
- `SettlementBackground` `0,0 / 1920x1080`，画刷 `SettlementPanel`
- `LeftPanel` `23,23 / 1020x931`
- `RightPanel` `1067,23 / 825x928`
- `SkipButton` `900,985 / 298x77`，`CloseButton` `1215,985 / 306x77`
- `AssetTitleText` / `SettlementTitleImage` / 空头像：`Collapsed(1)`
- 动态名/称号/角色文本仍在左板上

## 四、Lua

`RIGHT_PANEL_DESIGN_X/Y` 改回 `1067,23`。`luaparser` 语法通过。

## 五、待查证

- 已打开的结算页签必须关掉再开。
- 未启动 PIE。铺满后切图会被拉伸，这是 1920 基准和 1639 切图的比例差，不是控件没铺满。

# 2026-09-11 AuctionSettlementUI 切图原尺寸居中

> 类型：项目蓝图与 UI 记录
> 主题：AuctionSettlementUI 按 1639×960 切图原尺寸居中到 1920×1080 舞台
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionSettlementUI`、`Script/Function/AuctionSettlementUIService.lua`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；编辑器页签截图未刷新；未启动 PIE
> 来源：用户第二张参照图 `C:\Users\ADMINI~1\AppData\Local\Temp\codex-clipboard-7c9d6908-4175-4be9-8467-34b0352922fc.png`（1639×960）；用户现状 `C:\Users\ADMINI~1\AppData\Local\Temp\codex-clipboard-8b52ce1e-9c19-4756-a3b8-eb511d6fad66.png`；MCP 回读 `plan_16802023_96246791`
> 更新时间：2026-09-11
> 关联主题：[2026-09-10_AuctionSettlementUI_切图替换](./2026-09-10_AuctionSettlementUI_切图替换.md)、[2026-09-11_AuctionSettlementUI_设计态白块修复](./2026-09-11_AuctionSettlementUI_设计态白块修复.md)、[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)
> 排除范围：未改 AuctionHouseSelectUI / AuctionPropSelectUI / AuctionTestUI / ZhuJieMian；未改结算切图资产
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md`（`SetPosition` / `SetSize`）；`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md`

## 一、写前备份

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_SettlementNativeCenter`

## 二、对照结论

用户明确以第二张参照图为准。该图是 1639×960，和 `SettlementPanel.png` 同尺寸。上一轮把底板硬拉满 1920×1080 后：

1. 左右头像框被拉成白块
2. 「竞拍仓库」下出现白条
3. 「跳过展示 / 确认结算」压进底板

知识库已写明：1639×960 参考图不能硬拉满 1920×1080。本轮改回切图原像素，居中到 1920 舞台：`x=(1920-1639)/2=141`，`y=(1080-960)/2=60`。左右面板切图已烘焙标题字，所以折叠重复的 `SettlementTitleImage`、`AssetTitleText`、标签图和空头像图。

## 三、蓝图写入

plan_id：`plan_16802023_96246791`

回读：

- `SettlementBackground` `141,60 / 1639x960`，画刷 `SettlementPanel`
- `LeftPanel` `161,80 / 871x828`，画刷 `SettlementLeftPanel`
- `RightPanel` `1052,80 / 704x825`，画刷 `SettlementRightPanel`
- `SkipButton` `841,936 / 254x68`，`CloseButton` `1107,936 / 261x68`
- `AssetTitleText` / `SettlementTitleImage` / `AvatarFrameImage` / 空头像图：`Collapsed(1)`
- `RootSizeBox` 仍 1920×1080

切图合成对照：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_SettlementNativeCenter\native_center_preview.jpg`

## 四、Lua

`RIGHT_PANEL_DESIGN_X/Y` 从 `1067,23` 改回 `1052,80`，与 RightPanel 回读一致。`luaparser` 语法通过。空头像仍是有贴图才显示。

## 五、截图

FlaUI 枚举不到提权编辑器。`PrintWindow` 仍是白图，不能当设计态验收。已打开的结算页签必须关掉再开。

## 六、待查证

- 未启动 PIE。
- 动态金额文字相对切图卡槽的像素还需关页签后目视微调。

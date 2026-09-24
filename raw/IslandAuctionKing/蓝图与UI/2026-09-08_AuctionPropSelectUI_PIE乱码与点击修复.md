# 2026-09-08 AuctionPropSelectUI PIE 乱码与点击修复

> 类型：项目蓝图与 UI 记录
> 主题：AuctionPropSelectUI PIE 标题/关闭/确认显示「字」占位；条目名 UTF-8 字节截断；组卡点击被装饰层挡住
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI`，以及 `Script/Function/AuctionPropSelectUIService.lua`、`UIConfigTable` 的 `UI.PropSelect.*` 行
> 证据状态：项目实测（UGCAskQ MCP 写入 + 独立回读）+ 官方 API/枚举依据；未在本轮重新 PIE
> 来源：用户 PIE 截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\AuctionPropSelectUI_pie.png`；UGCAskQ MCP `ue_plan_submit` / `ue_py`；大厅对照 `ZhuJieMian.GoldValueText`
> 更新时间：2026-09-08
> 关联主题：[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)、[2026-09-07_AuctionPropSelectUI_对齐网页预览仪器组合层](./2026-09-07_AuctionPropSelectUI_对齐网页预览仪器组合层.md)
> 排除范围：未改 AuctionCharacterSelectUI / AuctionHouseSelectUI / ZhuJieMian / AuctionHubUIService / AuctionGameService
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md`（SetText）；`D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateFontInfo.md`（FontObject/TypefaceFontName/Size）；`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md`（HitTestInvisible=3）。禁止整段回写 `widget.Font` 为项目实测。

## 现象

PIE 打开仪器组合层后：

- 标题、右侧标题、确认钮显示「字」占位
- 关闭钮显示带 A 的方块
- 左侧组名、剩余、金币正常
- 条目名出现「微型??」「鉴仪器」这类截断
- 点组卡/确认无完整刷新或关闭

## 根因（MCP 回读）

事务 `InspectPropSelectGarbledFonts` / `ListPropSelectAllFonts`：

| 控件 | Text | FontObject | Size |
| --- | --- | --- | --- |
| TitleText | 仪器组合 | None | 24 |
| CloseLabel | X | None | 22 |
| ConfirmLabel | 确认 | None | 20 |
| PropHeadingText | 内含下列仪器 | None | 18 |
| GroupName01 / GoldChipText / ItemName01 | 完整中文或 30,000 | `/Engine/EngineFonts/Roboto.Roboto` Bold | 20/22/18 |

对照 `ZhuJieMian.GoldValueText`：Roboto Bold 22。缺 FontObject 的控件才会出「字」占位。

Lua `iconText:SetText(string.sub(itemName, 1, 6))` 按字节截 UTF-8 中文，会得到「微型??」。

组卡 `GroupTop/GroupBand/GroupName` 盖在 `PropButton` 上且为 Visible，点击落不到按钮。

## 修改

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\Prop\`

蓝图 plan_id：`plan_16788950_32073dd5`，事务 `FixPropSelectGarbledFonts`。

只对 Font 结构体 `set_field("FontObject"/"TypefaceFontName"/"Size")`，不整段回写 `widget.Font`：

- TitleText / CloseLabel / ConfirmLabel / PropHeadingText → Roboto Bold，字号 24/22/20/18
- CloseLabel `bIsVariable=true`

Lua：

- 新增 `TakeUtf8Chars`，图标二字按 UTF-8 字符截 2 个
- 组卡装饰层与条目文字 `SetVisibility(3)`（HitTestInvisible），点击落到 `PropButton` / 不挡条目
- `SelectGroup` / `Confirm` 仍走原确认 RPC 并关闭面板

独立回读 `VerifyPropSelectGarbledFonts`：`TitleText=仪器组合`、`ConfirmLabel=确认`、`ItemName01=微型品鉴仪器`、四控件 FontObject 均为 Roboto Bold。

## 第二轮（用户仍见 PIE「字」占位后）

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\Prop\AuctionPropSelectUI_beforeRound2.uasset` 及同目录 Lua / `UIConfigTable_beforeRound2.uasset`。

独立回读 `InspectPropSelectGarbledRound2` / `VerifyPropSelectGarbledFontsRound2`：设计态已是完整中文 + Roboto Bold，但 Refresh 未写 CloseLabel，配置缺 `UI.PropSelect.CloseText`。

蓝图 plan_id：`plan_16793050_e39e5834`，事务 `FixPropSelectGarbledFontsRound2`。仍只 `set_field(FontObject/TypefaceFontName/Size)`，不整段回写 Font。

配置 plan_id：`plan_16793182_9781a15d`，事务 `WritePropSelectCloseText`。只新增 `UI.PropSelect.CloseText=X`，未改 Character/House 行。

Lua：`GetLayout` 读 `UI.PropSelect.CloseText`；`Refresh` 写 Title/Heading/Confirm/CloseLabel；图标二字继续 `TakeUtf8Chars`，禁止 `string.sub` 按字节截。`SelectGroup` / `Confirm` 仍走原确认 RPC 并关闭面板。

独立回读 `VerifyPropSelectGarbledFontsRound2`：

| 控件 | Text | FontObject | Typeface | Size |
| --- | --- | --- | --- | --- |
| TitleText | 仪器组合 | `/Engine/EngineFonts/Roboto.Roboto` | Bold | 24 |
| CloseLabel | X | `/Engine/EngineFonts/Roboto.Roboto` | Bold | 22 |
| ConfirmLabel | 确认 | `/Engine/EngineFonts/Roboto.Roboto` | Bold | 20 |
| PropHeadingText | 内含下列仪器 | `/Engine/EngineFonts/Roboto.Roboto` | Bold | 18 |
| ItemName01 | 微型品鉴仪器 | `/Engine/EngineFonts/Roboto.Roboto` | Bold | 18 |

`UI.PropSelect.CloseText`：ValueType=string，Value=X。

luacheck：`All lua file num=66, fileErrNum=0, allErrNum=0`

## 待查证

必须重新调试 PIE。上一轮编辑器回读已是完整中文，但用户 PIE 截图仍是「字」占位，不能把 MCP 回读当成运行时证据。

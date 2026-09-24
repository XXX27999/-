# 2026-09-08 AuctionHouseSelectUI PIE 乱码与点卡选场

> 类型：项目蓝图与 UI 记录
> 主题：AuctionHouseSelectUI 按角色/道具层同源「字」方块处理；点卡/点名称胶囊选场并关闭；金币不足 LOCKED 生效
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionHouseSelectUI`，以及 `Script/Blueprint/Prefabs/UI/AuctionHouseSelectUI.lua`、`Script/Function/AuctionHouseSelectUIService.lua`
> 证据状态：项目实测（UGCAskQ MCP 写入 + 独立回读）+ 官方枚举/字体结构体依据；本轮未重新 PIE
> 来源：用户对照截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\AuctionCharacterSelectUI_pie.png`、`AuctionPropSelectUI_pie.png`；UGCAskQ MCP `ue_plan_submit` / `ue_py`；大厅对照 `ZhuJieMian.GoldValueText`
> 更新时间：2026-09-08
> 关联主题：[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)、[2026-09-07_拍卖场选择UI对齐网页预览](./2026-09-07_拍卖场选择UI对齐网页预览.md)、[2026-09-08_AuctionPropSelectUI_PIE乱码与点击修复](./2026-09-08_AuctionPropSelectUI_PIE乱码与点击修复.md)
> 排除范围：未改 AuctionCharacterSelectUI / AuctionPropSelectUI / ZhuJieMian / AuctionHubUIService / AuctionGameService；未改 `UI.HouseSelect.*` 行值；未按网页 CSS 覆盖已回读坐标
> 官方依据：`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md`（Visible=0，Collapsed=1，HitTestInvisible=3）；`D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateFontInfo.md`（FontObject / TypefaceFontName / Size）；`D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md`（SetText / Font）；`D:\oasis-skill-plus\docs\api\class\Others\UWidget.md`（SetIsEnabled / SetVisibility）；`D:\oasis-skill-plus\docs\api\class\Others\UButton.md`（OnClicked）。Font 写入方式为项目实测，禁止整段回写 `widget.Font`

## 现象

本轮没有单独的拍卖场 PIE 截图。角色/道具层顶栏、关闭、确认显示「字」方块；拍卖场层同源复制，按同样缺 `FontObject` 处理。

必须检查：资产条、关闭钮、三张场卡名称、kv 行、底部 hint、LOCKED 是否「字」方块或空；点卡/点名称胶囊能否选场并关闭；金币不足 LOCKED 是否生效。

## 写前 MCP 回读

事务 `InspectHouseSelectFontsRound4` / `InspectHouseSelectGeometryRound4`：

| 控件 | Text | FontObject | Size | 几何 |
| --- | --- | --- | --- | --- |
| SubtitleText | 我的资产 30,000 | `/Engine/EngineFonts/Roboto.Roboto` Bold | 20 | 1376,174 / 280x48 |
| CloseLabel | X | Roboto Bold | 22 | CloseButton 1672,168 / 46x46 |
| StatusText | 请选择一个拍卖场 | Roboto Bold | 18 | 220,758 / 1480x30 |
| CharacterLabel01-03 | 海岛集装仓 / 山地军械库 / 空投绝密库 | Roboto Bold | 20 | 名称胶囊 236/738/1240,672 / 442x48 |
| HouseNeedLabel/Value、HouseFeeLabel/Value | 资产需求 / 5,000 等 | Roboto Bold | 18 | 未改坐标 |
| HouseLocked01-03 | LOCKED | Roboto Bold | 48 | 设计态 Collapsed |
| ZhuJieMian.GoldValueText | 30,000 | Roboto Bold | 22 | -250,36 / 200x44 |

控件数写前 44。三张场卡 220/722/1224,256 / 474x480。装饰层 Visible，名称胶囊 z=5 低于插画/kv，点卡会被挡住。`CreateAndShow` 已不再调用 `ApplyLayout`。

## 修改

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\House\before_round4\`

蓝图 plan_id：`plan_16791429_7be4d0b1`，事务 `FixHouseSelectGarbledFontsRound4`。

只对 Font 结构体 `set_field("FontObject"/"TypefaceFontName"/"Size")`，不整段回写 `widget.Font`：

- 资产条 / 关闭 / hint / 三场名 / kv 标签与数值 / LOCKED → Roboto Bold，字号 20/22/18/20/18/48
- 装饰文本与行 `Visibility=3`（HitTestInvisible）
- 新增透明整卡按钮 `HouseHit01-03`，几何等于现有场卡，z=7，`BackgroundColor` alpha=0，`bIsVariable=true`
- 现有板子/场卡/名称胶囊/关闭钮坐标未改

Lua：

- `AuctionHouseSelectUI.lua` / `AuctionHouseSelectUIService.lua` 解析 `HouseHit01-03`
- `Refresh` 仍写场名、资产需求、入场费用、资产条、LOCKED 文案与显隐；金币不足时 `SetIsEnabled(false)` 同时作用于名称胶囊和整卡点击层
- `CreateAndShow` 绑定 `HouseHit` 与名称胶囊 `OnClicked` → `SelectHouse`，选中后 `Hide` 并 `AuctionHubUIService.Refresh`；金币不足直接返回不关层
- 继续不调用 `ApplyLayout`

独立回读 `VerifyHouseSelectGarbledFontsRound4`：`SubtitleText=我的资产 30,000`、`CloseLabel=X`、`StatusText=请选择一个拍卖场`、`CharacterLabel01=海岛集装仓`、`HouseNeedLabel01=资产需求`、`HouseNeedValue01=5,000`、`HouseFeeLabel01=入场费用`、`HouseLocked01=LOCKED`；FontObject 均为 Roboto Bold。`HouseHit01-03` 回读 220/722/1224,256 / 474x480，bg alpha=0。控件数 47。

luacheck：`All lua file num=66, fileErrNum=0, allErrNum=0`

## 待查证

本轮写入后未重新 PIE。必须重新调试 PIE 才能确认「字」占位消失、点卡/点名称胶囊能选场关闭、金币不足 LOCKED 生效。

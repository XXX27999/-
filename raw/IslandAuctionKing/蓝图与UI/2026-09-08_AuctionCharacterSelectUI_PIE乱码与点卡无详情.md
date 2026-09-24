# 2026-09-08 角色选择 UI PIE 乱码与点卡无详情

> 类型：项目证据
> 主题：AuctionCharacterSelectUI PIE 标题/关闭/确认显示「字」方块；点卡不填定位/技能；肖像透出水印
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionCharacterSelectUI`，及其 Lua `Script/Blueprint/Prefabs/UI/AuctionCharacterSelectUI.lua`、`Script/Function/AuctionCharacterSelectUIService.lua`，以及 `UIConfigTable` 的 `UI.CharacterSelect.*` 行
> 证据状态：项目实测（UGCAskQ MCP 写入 + 独立回读）+ 官方 API 依据；乱码是否消失必须重新 PIE 才能验证
> 来源：用户 PIE 截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\AuctionCharacterSelectUI_pie.png`；UGCAskQ MCP `ue_plan_submit` / `ue_py`；[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)
> 更新时间：2026-09-08
> 关联主题：[2026-09-07_AuctionCharacterSelectUI_对齐网页预览](./2026-09-07_AuctionCharacterSelectUI_对齐网页预览.md)、[ZhuJieMian大厅头像名称金币加载](./2026-09-08_ZhuJieMian大厅头像名称金币加载.md)
> 排除范围：未修改 AuctionHouseSelectUI、AuctionPropSelectUI、ZhuJieMian 布局、AuctionHubUIService、AuctionGameService、AuctionConfig.lua
> 官方依据：`D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateFontInfo.md`（FontObject/Size/TypefaceFontName）、`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md`（HitTestInvisible=3）、`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateBrushDrawType.md`（Box=1）、`D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md`（SetText）、`D:\oasis-skill-plus\docs\api\class\Others\UButton.md`（SetBackgroundColor/SetIsEnabled）、`D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`（Background/BrushColor/SetBrushFromTexture）、`D:\oasis-skill-plus\docs\api\class\Others\UUserWidget.md`（GetWidgetFromName）

## 现象

PIE 打开角色选择层后：

1. 顶栏四个「字」方块，不是「角色选择」。
2. 关闭钮带 A 的方块，不是 X。
3. 右侧大标题也是「字」；定位盒停在「角色定位」，技能盒停在「技能描述」，点卡不填正文。
4. 确认钮「字字」，看起来未启用。
5. 六张卡底部中文名正常（战术勘察员等）。
6. 肖像区透出开发者水印。

## 查证

MCP 只读回读（事务 `InspectCharacterSelectGarbledFontsNow`），对照 `ZhuJieMian.GoldValueText`：

| 控件 | Text | Size | FontObject | 结论 |
| --- | --- | --- | --- | --- |
| GoldValueText | 30,000 | 22 | `/Engine/EngineFonts/Roboto.Roboto` Bold | 大厅对照 |
| TitleText | 角色选择 | 24 | Roboto Bold | 文案在，字体已恢复 |
| CloseLabel | X | 22 | Roboto Bold | 同上 |
| ConfirmLabel | 确认 | 20 | Roboto Bold | 同上 |
| PropHeadingText | 未选择 | 36 | Roboto Bold | 右侧姓名控件，不是独立 CharacterNameText |
| CharacterName01 | 战术勘察员 | 18 | Roboto Bold | 卡底中文能显示 |
| CharacterArt01 写入前 | — | — | Background.DrawAs=Box(1)，ResourceObject=None | 空画刷仍可能透出水印 |

项目实测根因：上一轮整段回写 Font 会把 `FontObject` 清成 None。绿洲默认缺字体对象时用「字」占位。点卡无详情是肖像/名称/锁定层 Visible 挡住按钮。空 `ResourceObject` 的 Image/Box 画刷会透出开发者水印。

社区档案 `C:\Users\Administrator\.codex\skills\sq-skill\docs\community\manifest.json` 快照 2026-05-31，无 FontObject=None 显示「字」的可用结论。

## 修改

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_SelectUIGarbledPIE\Character\`

蓝图 plan_id：`plan_16793011_ba77ffb0`（used_count=1，decision=pass），事务 `FixCharacterSelectArtSolidMask`。

配置表 plan_id：`plan_16793012_90c1a345`（used_count=1，decision=pass），事务 `WriteCharacterSelectTitleCloseConfirmRows`。

1. 不整段回写 Font。四个乱码控件保持 Roboto Bold，文案「角色选择 / X / 确认 / 未选择」。
2. `CharacterArt01-06.Background.ResourceObject=/Engine/EngineResources/WhiteSquareTexture`，`DrawAs=Box(1)`，`Visibility=HitTestInvisible(3)`，保留原 BrushColor。
3. Lua Refresh 选中后写姓名/定位/技能，确认钮 `SetIsEnabled(true)` 并改米色；遮罩保持 HitTestInvisible。确认仍走 `playerController.RequestSelectAuctionCharacter`。
4. `UIConfigTable` 新增 `UI.CharacterSelect.TitleText=角色选择`、`CloseText=X`、`ConfirmText=确认`。Lua Construct/ApplyLayout/Refresh 函数内读取。

独立回读（事务 `VerifyCharacterSelectGarbledFontsIndependent`）：

- TitleText=`角色选择` Size=24 Roboto Bold
- CloseLabel=`X` Size=22 Roboto Bold
- ConfirmLabel=`确认` Size=20 Roboto Bold
- PropHeadingText=`未选择` Size=36 Roboto Bold
- CharacterArt01-06 ResourceObject=`WhiteSquareTexture` DrawAs=1 vis=3
- 三行配置 Value 回读为「角色选择 / X / 确认」

Lua 关键字配对检查：`AuctionCharacterSelectUI.lua` / `AuctionCharacterSelectUIService.lua` depth=0。本机无 luac。

## 待查证

乱码是否消失、点卡是否填定位/技能、确认钮是否可点、肖像水印是否被实色遮罩盖住，必须重新调试 PIE 才能验证。已打开的设计器页签需要关闭后重开。

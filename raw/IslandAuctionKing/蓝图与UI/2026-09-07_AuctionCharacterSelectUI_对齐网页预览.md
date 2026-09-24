# 2026-09-07 角色选择 UI 对齐网页预览

> 类型：项目蓝图与 UI 记录
> 主题：AuctionCharacterSelectUI 按已确认网页预览 `#characterOverlay` 重建，删除测试页残留
> 适用范围：IslandAuctionKing 项目的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionCharacterSelectUI`，及其 Lua `Script/Blueprint/Prefabs/UI/AuctionCharacterSelectUI.lua`、`Script/Function/AuctionCharacterSelectUIService.lua`，以及 `UIConfigTable` 的 `UI.CharacterSelect.*` 行
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；未启动 PIE，运行态未验证；设计态截图因 FlaUI 枚举不到提权编辑器窗口而未完成
> 来源：网页预览 `C:\Users\Administrator\.codex\visualizations\2026\09\04\zjm-hub-preview\index.html`（`#characterOverlay` / `.sheet-mid`）；用户设计态截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260907_SelectUIFixRound2\AuctionCharacterSelectUI_current.png`；UGCAskQ MCP `ue_plan_submit` / `ue_py` 回读
> 更新时间：2026-09-07
> 关联主题：[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)、[绿洲通用UI编辑规范与排错](../../知识/通用/UI与交互/绿洲通用UI编辑规范与排错.md)、[AuctionPropSelectUI 删除角色残留控件](./2026-09-07_AuctionPropSelectUI_删除角色残留控件.md)、[拍卖场选择UI对齐网页预览](./2026-09-07_拍卖场选择UI对齐网页预览.md)
> 排除范围：未修改 AuctionHouseSelectUI、AuctionPropSelectUI、CharacterPropSelectTestUI、AuctionTestUI、ZhuJieMian、CollectibleCodex、AuctionConfig.lua 及其他配置行
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md`（SetPosition/SetSize）、`D:\oasis-skill-plus\docs\api\class\Others\UWidget.md`（SetIsEnabled/SetVisibility）、`D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md`（SetText）

## 一、预览几何换算（1920x1080 设计舞台）

| 预览元素 | CSS / 计算 | 设计舞台坐标 |
| --- | --- | --- |
| `.sheet-mid` 中板 | 1380x760 居中 | x=270, y=160, 1380x760 |
| `.head` 顶栏 | 高 64，背景 #c47a20 | x=270, y=160, 1380x64 |
| 标题 | 「角色选择」 | x=294, y=172, 420x40 |
| 关闭钮 | 42x42 | x=1584, y=171 |
| 左列 3x2 | 卡片 242x228，gap 14 | 294/550/806 x 248/490 |
| 上图 / 下名 | 176 / 52 | 卡内上图 242x176，名称 242x52 |
| 右列 | 宽 558 | x=1068, y=248 |
| 姓名 / 定位 / 技能 / 确认 | 52 / 90 / 250 / 52 | y=248 / 316 / 420 / 694 |

## 二、删除与保留

必须 `widget_remove` 的测试页残留（不能只 Collapsed）：`CharacterPanel`、`PropGroupPanel`、`FooterPanel`、`SubtitleText`（CHARACTER / PROP-GROUP TEST）、`CharacterHeadingText`、`CharacterCounterText`、`PropCounterText`、`PropButton01-06`、`PrevPageButton`、`PageText`、`NextPageButton`、`SummaryText`、`StatusText`、`ResetButton`。

保留并重建：`ScreenBackground`、`TopPanel`/`TitleText`/`CloseButton`、六张 `CharacterButton`、右侧 `PropHeadingText`/`PropDetailText`/`CharacterDetailText`/`ConfirmButton`。新增：`SheetBorder`、`CharacterPosBox`、`CharacterSkillBox`、`CharacterSkillTitle`、`CharacterArt01-06`、`CharacterName01-06`、`CharacterLock01-06`。

写后 MCP 回读：`leftoverHits=[]`，六卡坐标 294/550/806 × 248/490，确认钮 1068,694/558x52，标题「角色选择」。

## 三、配置表

`UIConfigTable` 新增 37 行 `UI.CharacterSelect.*`，4 列结构：`ValueType` / `Value` / `Description` / `ModificationNotes`。回读 `SlotCount=6`、`SheetWidth=1380`、`CardWidth=242`、`RightX=1068`、`LockedText=LOCKED` 均通过。`AuctionConfig.lua` 未改，仍由已注册的 `UIConfigTable` 加载。

## 四、Lua

- `AuctionCharacterSelectUI.lua`：Construct 设标题「角色选择」，绑定右侧姓名/定位/技能别名。
- `AuctionCharacterSelectUIService.lua`：函数内读 `UI.CharacterSelect.*`，`Slot:SetPosition/SetSize` 摆放，Refresh 填姓名/定位/技能/锁定态与确认钮 `SetIsEnabled`。HasAuthority 校验改为显式日志，不再静默 return。

LuaCheck：`All lua file num=65, fileErrNum=0, allErrNum=0`。

## 五、MCP 与备份

- 写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260907_SelectUIFixRound2\AuctionCharacterSelectUI\`
- 蓝图 plan_id：`plan_16792163_6b56372d`（used_count=2，decision=pass）
- 配置表 plan_id：`plan_16792406_cb01f7ec`（used_count=1，decision=pass）
- `objed_open_asset('AuctionCharacterSelectUI','UI')` 返回 True；FlaUI `--list` 只枚举到 ChatGPT / 资源管理器 / 微信 / WPS，枚举不到 `ShadowTrackerExtraUGCEditor`，因此不把其他窗口截图当作设计态证据。

## 六、待查证

- 已打开的设计器页签可能仍显示旧树，需要关闭后重新打开 `AuctionCharacterSelectUI` 才能看到删除结果。
- 本轮未启动 PIE，运行态选中态、锁定态与确认钮灰底需重新调试 PIE 验证。

# 2026-09-07 AuctionPropSelectUI 对齐网页预览仪器组合层

> 类型：项目蓝图与 UI 记录
> 主题：AuctionPropSelectUI 删除 CharacterPropSelectTestUI 测试壳，按 zjm-hub-preview `#propOverlay` / `.sheet-prop` 重建米色仪器组合层
> 适用范围：IslandAuctionKing 的 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionPropSelectUI`，以及 `Script/Blueprint/Prefabs/UI/AuctionPropSelectUI.lua`、`Script/Function/AuctionPropSelectUIService.lua`、`UIConfigTable` 的 `UI.PropSelect.*` 行
> 证据状态：项目实测（UGCAskQ MCP 写入 + 回读）+ 官方 API 依据；未启动 PIE，运行态未验证
> 来源：网页预览 `C:\Users\Administrator\.codex\visualizations\2026\09\04\zjm-hub-preview\index.html`（`#propOverlay`）；用户设计态截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260907_SelectUIFixRound2\AuctionPropSelectUI_current.png`；UGCAskQ MCP `ue_plan_submit` / `ue_py`
> 更新时间：2026-09-07
> 关联主题：[绿洲编辑器控件位置与尺寸准确性](../../知识/通用/UI与交互/绿洲编辑器控件位置与尺寸准确性.md)、[蓝图与 MCP 写入流程](../../知识/通用/工具与流程/蓝图与MCP写入流程.md)、[2026-09-07_AuctionPropSelectUI_删除角色残留控件](./2026-09-07_AuctionPropSelectUI_删除角色残留控件.md)
> 排除范围：未改 AuctionCharacterSelectUI / AuctionHouseSelectUI / CharacterPropSelectTestUI / AuctionTestUI / ZhuJieMian / CollectibleCodex / AuctionConfig.lua
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md`（`SetPosition`/`SetSize`）；知识库未覆盖绿洲设计器对 Collapsed 无贴图 Border 的渲染公式，该点以项目实测为准

## 一、预览几何（1920x1080）

| 元素 | 设计舞台坐标 |
| --- | --- |
| `.sheet-prop` 米色底板 | 320,160 / 1280x760 |
| `.head` 橙色顶栏 | 320,160 / 1280x64，文案「仪器组合」 |
| 关闭钮 | 1534,171 / 42x42 |
| 左列组卡 | 338,240 起，400x118，间距 12，5 张可见 |
| 右侧标题 | 772,242，「内含下列仪器」 |
| 右侧条目 | 772,282 起，806x86，图标 58x58 |
| 金币胶囊 | 772,850 / 220x52 |
| 确认钮 | 1298,850 / 280x52 |

## 二、MCP 写入

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260907_SelectUIFixRound2\AuctionPropSelectUI\`

蓝图 plan_id：`plan_16791955_e0b3069a`（`RebuildPropSelectSheet`，used_count=2）
配置表 plan_id：`plan_16792287_3e42b331`（`AddPropSelectConfigRows`，used_count=1）

删除（`widget_remove`，返回 None）：`PropGroupPanel`、`FooterPanel`、`SubtitleText`、`PropCounterText`、`PrevPageButton`、`PageText`、`NextPageButton`、`SummaryText`、`StatusText`、`ResetButton`、`PropDetailText`、`PropButton06`。

新增并回读存在：`SheetPanel` 320,160/1280x760；`TopPanel` 320,160/1280x64；`TitleText`「仪器组合」；`GroupName01`「初级泛用仪器组」；`ItemName01`「微型品鉴仪器」；`GoldChipText`「30,000」；`ConfirmLabel`「确认」。

回读确认测试残留：`leftoverPresent=[]`。`UI.PropSelect.*` 共 43 行，抽样 `SheetX=320`、`SheetWidth=1280`、`TitleText=仪器组合`、`ConfirmWidth=280`。

## 三、Lua

- `AuctionPropSelectUI.lua`：`Construct` 读取 `UI.PropSelect.TitleText`，默认「仪器组合」。
- `AuctionPropSelectUIService.lua`：函数内 `GetLayout()` 读 `UI.PropSelect.*`；`ApplyLayout` 用 `Slot:SetPosition/SetSize`；`Refresh` 填组名/色带/条目/金币；保留 HasAuthority 校验与完整 ugcprint。不再绑定分页/重置。

## 四、待查证

- FlaUI 无法枚举提权编辑器窗口，本轮未截到写入后的设计态画面。已打开的 UI 编辑器页签需要关闭后重新打开才能看到清理结果。
- 未启动 PIE，运行态金币与组表刷新未验证。

## 相关页面

- [AuctionPropSelectUI 删除角色残留控件](./2026-09-07_AuctionPropSelectUI_删除角色残留控件.md)
- [拍卖场选择UI对齐网页预览](./2026-09-07_拍卖场选择UI对齐网页预览.md)

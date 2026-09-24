# AuctionTestUI 初始打开价格输入与道具面板

> 类型：项目证据
> 主题：AuctionTestUI / BidKeypadPanel / PropPanel / 初始可见性
> 适用范围：IslandAuctionKing
> 证据状态：项目实测（代码核对）；修复后需重新 PIE 验证
> 来源：`Script/Function/AuctionTestUIService.lua`、`Script/Function/AuctionRoundHistoryUIService.lua`
> 更新时间：2026-09-04
> 关联主题：AuctionTestUI 价格输入面板设计态贴图绑定, AuctionTestUI 道具栏对齐左侧席位红框
> 排除范围：不覆盖结算 UI、图鉴、角色选择 UI
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UWidget.md` 的 `SetVisibility`；`D:\oasis-skill-plus\docs\api\cppenum\E\ES\ESlateVisibility.md` 的 `Collapsed=1`

## 结论

跳进竞拍主界面时价格输入面板和道具使用面板会露出来，不是玩家点开的。蓝图设计态默认可见，而 `AuctionTestUIService.Initialize` 原先只折叠轮次详情/表情/说明，没有折叠 `BidKeypadPanel` 和 `PropPanel`。`RefreshPublicState` 也只在 `AuctionBidKeypadOpen==true` 时才收键盘，首次进入该标志为假，所以设计态 Visible 会一直留下。

`OnPropIntel` 里的 `OpenPropPanel` 只在已有私有道具情报时才会打开道具面板，不是这次初始双面板同时出现的必要条件。

## 修改

`AuctionTestUIService.HideSecondaryPanels` 在初始化刷新状态前把 `BidKeypadPanel`、`PropPanel` 和可选 `SkillPanel` 设为 `ESlateVisibility.Collapsed`。不可报价时无条件折叠报价键盘。写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260904_AuctionTestUI_HideSecondaryPanels`。

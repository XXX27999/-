# 2026-09-08 AuctionPropSelectUI 确认后大厅乐观写入组名

> 类型：项目证据
> 主题：Lua / 大厅反馈 / 道具选择确认
> 适用范围：IslandAuctionKing 的 `AuctionPropSelectUIService.Confirm` 关闭后大厅右槽文案
> 证据状态：项目实测（静态代码）；官方确认（`UTextBlock:SetText`）；未启动 PIE
> 来源：本轮会话 2026-09-08；写前备份 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubAnchorsCountdown\Prop\`
> 更新时间：2026-09-08
> 关联主题：AuctionPropSelectUIService、AuctionHubUIService.Refresh、ZhuJieMian.PropTitleText、ZhuJieMian.PropSummaryText
> 排除范围：未改 AuctionHubUIService.lua、ZhuJieMian.uasset、Character/House 选择 UI、AuctionGameService、UGCPlayerController；未改坐标；未整段回写 Font
> 官方依据：[UTextBlock.SetText](../../docs/api/class/Others/UTextBlock.md)

## 现象

`AuctionPropSelectUI` 确认后，主界面右槽仍显示「点击选择道具组」，没有已选仪器组名称。

## 根因

`AuctionHubUIService.Refresh` 读 `privateState.SelectedPropGroup or privateState.MatchPropGroup`。Confirm 虽已 `RequestSelectAuctionPropGroup` 并立刻 `Refresh`，但私有状态此时仍可能为空，Refresh 会把 `PropTitleText` 写成「未选择」，把 `PropSummaryText` 写成「点击选择道具组」。

文件边界禁止改 `AuctionHubUIService.lua`，因此只能在道具选择 Confirm 成功后乐观写入大厅可见文案。

## 项目改动

写前备份：

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubAnchorsCountdown\Prop\`

- 新增 `ApplyOptimisticHubPropTexts(hubWidget, groupName)`：用 `UTextBlock:SetText` 把大厅 `PropTitleText` 和 `PropSummaryText` 写成已选组名。
- `Confirm` 成功后顺序固定为：乐观写入 → `AuctionHubUIService.Refresh` → 再次乐观回写 → `Hide`。第二次写入用于覆盖 Refresh 读到空 `SelectedPropGroup` 时回填的占位文案。
- `AuctionPropSelectUI.lua` 本轮未改。

未改：`AuctionHubUIService.lua`、`ZhuJieMian.uasset`、Character/House 选择 UI、`AuctionGameService`、`UGCPlayerController`。MCP 未调用。

## 验证

- Lua 关键字平衡检查：`function/if/for/while` 与 `end` 匹配，`balance_ok=true`。
- 未启动 PIE。大厅右槽是否显示组名必须重新 PIE 后目视确认。

## 预估成功日志

```
【AuctionPropSelectUIService+Confirm】入口
【AuctionPropSelectUIService+Confirm】关键数据 requestOK=true name=<已选组名>
【AuctionPropSelectUIService+ApplyOptimisticHubPropTexts】入口 groupName=<已选组名>
【AuctionPropSelectUIService+ApplyOptimisticHubPropTexts】出口 success=true
【AuctionHubUIService+Refresh】关键数据 prop=未选择
【AuctionPropSelectUIService+ApplyOptimisticHubPropTexts】出口 success=true
【AuctionPropSelectUIService+Confirm】关键数据 optimisticBeforeOK=true hubRefreshOK=true optimisticAfterOK=true
【AuctionPropSelectUIService+Confirm】出口 success=true
```

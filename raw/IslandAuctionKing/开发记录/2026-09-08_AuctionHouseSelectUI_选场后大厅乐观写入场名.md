# 2026-09-08 AuctionHouseSelectUI 选场后大厅乐观写入场名

> 类型：项目证据
> 主题：Lua / 大厅反馈 / 拍卖场选择
> 适用范围：IslandAuctionKing 的 `AuctionHouseSelectUIService.SelectHouse` 关闭后大厅会场区 `VenueNameText`
> 证据状态：项目实测（静态代码）；官方确认（`UTextBlock:SetText`、`UUserWidget:GetWidgetFromName`）；未启动 PIE
> 来源：本轮会话 2026-09-08；写前备份 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubAnchorsCountdown\House\`
> 更新时间：2026-09-08
> 关联主题：AuctionHouseSelectUIService、AuctionHubUIService.Refresh、ZhuJieMian.VenueNameText、[2026-09-08_AuctionHouseSelectUI_PIE乱码与点卡选场](../蓝图与UI/2026-09-08_AuctionHouseSelectUI_PIE乱码与点卡选场.md)
> 排除范围：未改 AuctionHubUIService.lua、ZhuJieMian.uasset、Character/Prop 选择 UI、AuctionGameService、UGCPlayerController；未改坐标；未整段回写 Font
> 官方依据：[UTextBlock.SetText](../../docs/api/class/Others/UTextBlock.md)、[UUserWidget.GetWidgetFromName](../../docs/api/class/Others/UUserWidget.md)

## 现象

`AuctionHouseSelectUI` 点卡选场关闭后，主界面会场区仍显示「未选择拍卖场」，没有已选场名反馈。

## 根因

`AuctionHubUIService.Refresh` 读 `publicState.AuctionHouse.Name`。`SelectHouse` 虽已 `RequestSelectAuctionHouse` 并立刻 `Refresh`，但公共状态此时仍可能为空，Refresh 会把 `VenueNameText` 写成「未选择拍卖场」。旧顺序还是先 `Hide` 再 `Refresh`，选层关掉后大厅立刻被空状态刷回占位文案。

文件边界禁止改 `AuctionHubUIService.lua` 和 `ZhuJieMian` 坐标，因此只能在选场成功后乐观写入大厅已有 `VenueNameText`。MatchLabel Z 高于 VenueNameText 的叠层问题本轮不改坐标，只写文案。

金币不足 LOCKED 仍直接返回，不请求、不写大厅、不关层。

## 项目改动

写前备份：

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubAnchorsCountdown\House\`

- 新增 `ApplyOptimisticVenueName(hub, houseName)`：解析大厅 `VenueNameText`（字段缺失时走 `GetWidgetFromName`），用 `UTextBlock:SetText` 写成「当前：场名」。
- `SelectHouse` 成功后顺序固定为：乐观写入 → `AuctionHubUIService.Refresh` → 再次乐观回写 → `Hide`。第二次写入用于覆盖 Refresh 读到空 `AuctionHouse` 时回填的「未选择拍卖场」。
- `requestOK=false`、金币不足、配置缺失均不写大厅。
- `AuctionHouseSelectUI.lua` 本轮未改。

未改：`AuctionHubUIService.lua`、`ZhuJieMian.uasset`、Character/Prop 选择 UI、`AuctionGameService`、`UGCPlayerController`。MCP 未调用。

## 验证

- `luacheck.exe -cmd 0`：`All lua file num=66, fileErrNum=0, allErrNum=0`
- 未启动 PIE。大厅会场区是否显示「当前：场名」必须重新 PIE 后目视确认。

## 预估成功日志

```
【AuctionHouseSelectUIService+SelectHouse】入口 index=1 houseKey=IslandContainer HasAuthority=false
【AuctionHouseSelectUIService+SelectHouse】关键数据 requestOK=true error=nil
【AuctionHouseSelectUIService+ApplyOptimisticVenueName】入口 houseName=海岛集装仓
【AuctionHouseSelectUIService+ApplyOptimisticVenueName】出口 success=true
【AuctionHubUIService+Refresh】关键数据 house=未选择拍卖场 houseReady=false
【AuctionHouseSelectUIService+ApplyOptimisticVenueName】出口 success=true
【AuctionHouseSelectUIService+SelectHouse】关键数据 wroteAfterRefresh=true
【AuctionHouseSelectUIService+SelectHouse】出口
```

# ZhuJieMian 主界面点击层与大厅功能接入

> 类型：项目 UI 蓝图修改与 Lua 功能接入
> 主题：ZhuJieMian 设计态只有贴图和文案，AuctionHubUIService 需要的可点按钮缺失；补透明点击层并接入三个选择层、仓库图鉴、帮助与未开放提示
> 适用范围：IslandAuctionKing，`ZhuJieMian` 主界面大厅（等待阶段）
> 证据状态：项目实测；UGCAskQ MCP 写入后回读通过；Lua 语法检查通过；未启动 PIE
> 来源：用户编辑器截图 `codex-clipboard-35d8a874-*.png`、网页预览 `C:\Users\Administrator\.codex\visualizations\2026\09\04\zjm-hub-preview\index.html`、UGCAskQ MCP `ue_plan_submit` / `ue_py`
> 更新时间：2026-09-08
> 关联主题：AuctionHubUIService、AuctionHouseSelectUI、AuctionCharacterSelectUI、AuctionPropSelectUI、CollectibleCodexUIService、UIConfigTable、[大厅头像名称金币加载](./2026-09-08_ZhuJieMian大厅头像名称金币加载.md)
> 排除范围：未实现装扮/签到/商城/邮件/在线奖励/保底金的完整玩法，仅接入官方 `ShowTipsUI` 提示；未改三个选择层蓝图；未启动 PIE；FlaUI 仍枚举不到提权编辑器，没有拿错窗口当设计态证据
> 官方依据：[UButton](../../../docs/api/class/Others/UButton.md)、[UCanvasPanelSlot](../../../docs/api/class/Others/UCanvasPanelSlot.md)、[UWidget.SetIsEnabled](../../../docs/api/class/Others/UWidget.md)、[UGCWidgetManagerSystem.ShowTipsUI](../../../docs/api/class/和平全局接口/UI%20界面/UGCWidgetManagerSystem.md)、[ESlateVisibility](../../../docs/api/cppenum/E/ES/ESlateVisibility.md)

## 现象

用户截图是绿洲 UI 编辑器中的 `编辑 ZhuJieMian`。画面已有顶部仓库/装扮/签到/商城/邮件、右上金币、会场框、道具/角色槽、在线奖励/帮助/保底金、左下头像和玩家名称，但：

1. 会场框、道具槽、角色槽和开始匹配区没有可点 `UButton`。
2. `AuctionHubUIService.BindEvents` 要求 `OpenHouseButton` / `OpenPropButton` / `OpenCharacterButton` / `MatchButton`，缺失时直接 `error(...)`，大厅初始化失败。
3. 仓库、帮助、保底金只是装饰图，没有点击入口。

MCP 只读回读（写入前）控件数 29：全部为 Image/TextBlock，没有 Button。

## 修改记录

写前备份：

`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_ZhuJieMianHub\`

目标资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`

蓝图计划：`plan_16779644_8cad97bc`，事务 `WriteZhuJieMianHubButtons`，`decision=pass`，`used_count=1`。

新增透明点击层（`BackgroundColor` alpha=0，`bIsVariable=true`）：

| 控件 | 坐标 | 尺寸 | 作用 |
| --- | --- | --- | --- |
| OpenHouseButton | 792,100 | 448x420 | 打开拍卖场选择层 |
| OpenPropButton | 792,528 | 218x132 | 打开道具选择层 |
| OpenCharacterButton | 1022,528 | 218x132 | 打开角色选择层 |
| MatchButton | 792,668 | 448x58 | 开始匹配门禁 |
| WarehouseButton | 86,28 | 128x54 | 打开藏品图鉴 |
| Dress/Checkin/Shop/MailButton | 顶部页签 | 128x54 | 未开放提示 |
| OpenReward/OpenHelp/OpenGuaranteeButton | 1487/1606/1718,900 | 约 164x168 | 奖励未开放 / 帮助 / 保底金未开放 |
| MatchLabel | 792,668 | 448x58 | 文案「开始匹配」，HitTestInvisible |
| PropKindText / PropSummaryText | 道具槽内 | 小标题与摘要 | HitTestInvisible |

配置表计划：`plan_16780140_7156e354`，事务 `WriteHubConfigRows`。`UIConfigTable` 新增 19 行 `UI.Hub.*`，回读类型和值与写入一致。

Lua：

- `AuctionHubUIService.lua`：函数内读 `UI.Hub.*`，`ApplyLayout` 摆放会场点击层；绑定四个必选按钮和八个可选按钮；仓库走 `CollectibleCodexUIService.CreateAndShow`；帮助与未开放功能走官方 `UGCWidgetManagerSystem.ShowTipsUI`；三项已确认后提示等待全员开局。
- `ZhuJieMian.lua`：补齐新增控件的 `---@field` 声明。

## 验证

- MCP 回读：四个必选按钮存在且 `var=true`，`OpenHouseButton=792,100 / 448x420`，`MatchLabel=开始匹配`，`PropSummaryText=点击选择道具组`。
- 配置表 19 行逐项回读通过。
- `luaparser`：`AuctionHubUIService.lua` 与 `ZhuJieMian.lua` SYNTAX OK。
- 工程内无本轮临时 `.py` / `__pycache__`。
- 未启动 PIE。已打开的 `编辑 ZhuJieMian` 页签需要关掉再开才能看到新按钮。
- 后续只读回读：用户已手动摆正，估算坐标不再作为写入基线。见 [2026-09-08_ZhuJieMian用户摆正后布局回读](./2026-09-08_ZhuJieMian用户摆正后布局回读.md)。

## 生效方式

重新调试 PIE。蓝图新增控件和配置表行都不能热更新。

## 预估成功日志

```
【ZhuJieMian+Construct】入口
【AuctionHubUIService+GetLayout】关键数据 HouseX=792 HouseY=100 HouseWidth=448 HouseHeight=420
【AuctionHubUIService+ApplyLayout】出口 success=true
【AuctionHubUIService+BindEvents】出口 success=true
【AuctionHubUIService+Refresh】关键数据 gold=... houseReady=false selectionReady=false
【AuctionHubUIService+Initialize】出口 success=true
【AuctionHubUIService+OpenHouse】出口 success=true
```

# AuctionTestUI 价格输入面板设计态贴图绑定

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI BidKeypadPanel
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionFunctionalPreview.html、PriceInput.png
> 更新时间：2026-09-03
> 关联主题：AuctionTestUI 二级面板按网页预览与素材回收、AuctionTestUI 说明面板设计态贴图绑定、绿洲编辑器控件位置与尺寸准确性
> 排除范围：未改席位/仓库/轮次详情/说明/道具列表；未启动 PIE
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UBorder.md、D:\oasis-skill-plus\docs\api\class\Others\UButton.md、D:\oasis-skill-plus\docs\api\cppstruct\F\FB\FButtonStyle.md。知识库未覆盖“按钮 DrawAs=None 后运行时点击热区”的官方保证，点击仍走原 UButton OnClicked。

## 问题

用户截图中报价键盘是深蓝空底，标题 `输入暗标报价` 盖住数字 1，`当前轮次秒杀倍数` 溢出到右侧仓库，`清除` 叠在取消/确认之间。

MCP 回读：

- `BidKeypadPanel=(708.5,267.5,503x545)` 已对齐网页 `.price-modal`
- `Background.ResourceObject=None`
- 数字键已用 `AuctionUI_BottomButton` 再画一层，盖住 `PriceInput` 格子
- `ClearBidButton=(416,365.9,149.3x95.7)` 超出 503×545
- `BidKeyCancelButton` 折叠在第四列清除格
- `BidKeypadTitle` 宽 534.5，大于面板

网页预览键位：左 27 顶 35，数字 86×86，宽键 126×86，底栏显示 26,452,296×68，确认 350,452,126×68。第四列最后一格是 `清除`，没有独立取消键；关闭用右上透明叉。

## 写入

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_BidKeypadArtBind\`

MCP：

- `plan_16800442_131c228d` 绑 PriceInput、透明按键、收回清除、折叠旧标题
- `plan_16800747_e7d35293` 将秒杀标签缩短为 `秒杀倍数`

回读：

- `BidKeypadPanel.Background=PriceInput` DrawAs=Image
- 数字/宽键/确认/清除 `DrawAs=0 (NoDrawType)`，只保留点击
- `ClearBidButton=(351,329,126x86)` 落入第四列底格
- `BidKeyCancelButton=(433,10,52x52)` 文案 `×`，作为右上关闭
- `BidKeypadTitle` Collapsed 并移到 `(-2000,-2000)`
- `BidKeyMultiplierLabel=秒杀倍数`

## 截图

- 用户对照：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_BidKeypad_user_before.png`
- 绑定后：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_BidKeypadArtBind_after.png`
- 二次截图被编辑器 `Could not write to .../AuctionTestUI` 弹窗挡住，不能作为视觉证据。

FlaUI PID 15852。设计态截图不能代替 PIE。

## 生效

重新调试 PIE。

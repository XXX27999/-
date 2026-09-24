# 2026-09-03 AuctionTestUI 二级面板按网页预览与素材回收

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 轮次详情、报价键盘、说明、道具列表
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：AuctionFunctionalPreview.html、已导入 AuctionUI 贴图、UGCAskQ MCP 回读写入、FlaUI 设计态截图
> 更新时间：2026-09-03
> 关联主题：绿洲编辑器控件位置与尺寸准确性、AuctionTestUI 轮次详情素材导入与对齐、AuctionTestUI 编辑器设计态与网页预览对比
> 排除范围：未改主界面席位/情报/仓库；未启动 PIE；表情弹窗仍为预览占位；设计态二级面板保持 Collapsed
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md。网页预览主界面存在非等比 CSS scale，弹窗按素材原尺寸居中，不跟随该 scale。

## 问题

主界面舞台已切到 1920×1080 后，二级面板仍沿用被放大的旧坐标：`PropPanel=616x734`、`BidKeypadPanel=596x606`、`HelpPanel=616x506`、`RoundDetailPanel=814x668`，大于网页预览和导入素材像素。

## 项目实测

MCP `plan_16795547_e94e97ba` 写入后回读（设计态 Collapsed）：

- `PropPanel=(700,210,520x660)` 对齐 `.item-modal` / `SkillPanel`
- `BidKeypadPanel=(708.5,267.5,503x545)` 对齐 `.price-modal` / `PriceInput`；`BidKeyButton01=(27,35,86x86)`
- `HelpPanel=(700,312.5,520x455)` 对齐 `.info-modal` / `InfoPanel`；`HelpPrevButton=(163,389,58x48)`
- `RoundDetailPanel=(616.5,239.5,687x601)` 对齐轮次详情参考弹窗；关闭钮 `(595,20,65x50)` 对齐 `RoundDetailClose` 65×50
- `UseSelectedPropButton=(174,577,170x58)`

运行时贴图仍由 `AuctionUITextureReplacementService` 绑定：`PropPanel=AuctionSkillPanel`，`HelpPanel=AuctionInfoPanel`，`BidKeypadPanel=AuctionUI_BidKeypad`，轮次详情五张 Image 走 `SetBrushFromTexture`。

截图：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_SecondaryPanelsFit_after.png`

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_SecondaryPanelsFit\`

## 生效

重新调试 PIE。设计态截图因面板 Collapsed 只能证明主界面未破坏，不能代替打开弹窗后的运行态验证。

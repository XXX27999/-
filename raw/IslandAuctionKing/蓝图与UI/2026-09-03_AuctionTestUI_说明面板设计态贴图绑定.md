# AuctionTestUI 说明面板设计态贴图绑定

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI HelpPanel
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionFunctionalPreview.html、UIConfigTable
> 更新时间：2026-09-03
> 关联主题：AuctionTestUI 二级面板按网页预览与素材回收、AuctionTestUI 轮次详情设计态贴图绑定、MCP UI 编辑与高保真还原知识库
> 排除范围：未改席位/仓库/轮次详情/报价键盘/道具列表；未启动 PIE
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UBorder.md、D:\oasis-skill-plus\docs\api\class\Others\UImage.md、D:\oasis-skill-plus\docs\api\class\Others\UTextBlock.md、D:\oasis-skill-plus\docs\api\class\Others\UTextLayoutWidget.md。知识库未覆盖 TextBlock 把字面 `\\n` 当换行的官方保证。

## 问题

用户截图中说明弹窗为深蓝底加白矩形：翻页钮左右各一块白方、正文把 `\\n\\n` 当字符显示。MCP 回读确认 `HelpPanel=(700,312.5,520x455)` 已对齐网页预览 `.info-modal`，但：

- `HelpPanel.Background.ResourceObject=None`
- `HelpPrevButton` / `HelpNextButton` 四态 `ResourceObject=None`
- `HelpRulesText` 默认文案含字面 `\\n\\n`，`AutoWrapText=true`

已导入贴图：`InfoPanel` 687×601、`InfoArrowLeft/Right` 71×56。网页预览把 `InfoPanel.png` 拉伸到 520×455，箭头用 contain。

## 写入

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_HelpPanelArtBind\`

MCP：

- `plan_16799300_a0efdfdc` 绑定 HelpPanel 画刷并写入真实换行正文
- `plan_16799301_ad6d1d89` 新增 UIConfigTable 箭头路径

回读：

- `HelpPanel.Background=InfoPanel:Texture2D`，尺寸仍 520×455
- `HelpPrevButton.Normal=InfoArrowLeft`
- `HelpNextButton.Normal=InfoArrowRight`
- `HelpRulesText` 为真实换行，`AutoWrapText=true`
- `UI.Texture.AuctionInfoArrowLeft/Right` 已新增并回读

Lua：

- `AuctionUITextureReplacementService` 增加 `HelpPrevButton`/`HelpNextButton` 四态绑定
- `AuctionUITexturePathService` 增加箭头路径回退

## 截图

- 用户对照：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_HelpPanel_user_before.png`
- 绑定后：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_HelpPanelArtBind_after.png`

FlaUI PID 15852。设计态截图不能代替 PIE。

## 生效

重新调试 PIE。

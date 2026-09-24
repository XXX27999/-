# AuctionTestUI 道具栏顶部详情绑定 SkillBar

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI PropPanel 顶部详情
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionFunctionalPreview.html item-summary、导入 SkillBar/SkillEmptySlot
> 更新时间：2026-09-03
> 关联主题：AuctionTestUI 道具栏对齐左侧席位红框、绿洲编辑器控件位置与尺寸准确性
> 排除范围：未改席位/仓库/轮次详情/说明/报价键盘几何；未启动 PIE
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UImage.md（Brush、SetBrushFromTexture、GetBrush）。知识库未覆盖“红框截图到画布”的官方换算公式。

## 问题

用户红框圈住道具栏标题下详情区。当时只有 Collapsed 的 `PropIntelText`，没有查看已导入的 `SkillBar` 底图和左侧道具图。

网页预览 `.item-summary`：`SkillBar.png` 底图 + 72px 道具图 + 右侧说明。

## 写入

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_PropSummaryArt\`

MCP：`plan_16803628_dd76f58f`

回读：

- `PropSummaryBar=(39.84,94.643,465.504x99.496)` Brush=`SkillBar` DrawAs=Image
- `PropSummaryImage=(51.84,106.647,75.487x75.487)` Brush=`SkillEmptySlot`
- `PropIntelText=(139.327,104.643,354.017x79.496)` Visible=HitTestInvisible，文字收到图标右侧
- 三个控件均落入 `PropPanel` 545.185x800.824

Lua：

- `AuctionUITextureReplacementService` 增加 `AuctionSkillBar` / `AuctionSkillEmptySlot` 运行时绑定
- `AuctionPropSelectionUIService.Refresh` 选中槽后把 `PropImageXX` 贴图复制到 `PropSummaryImage`
- `AuctionTestUIService` 契约增加 `PropSummaryBar` / `PropSummaryImage`

## 截图

- 用户对照：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_PropSummary_user_before.png`
- 绑定后：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_PropSummaryArt_after.png`

FlaUI PID 15852。设计态占位图是 SkillEmptySlot；选中真实道具图需重新 PIE。

## 生效

重新调试 PIE。

## 脚本健康检查（同日追加）

静态核对后发现 `IMAGE_BINDINGS` 使用 `AuctionSkillBar` / `AuctionSkillEmptySlot`，但 `DEFAULT_BINDING_KEYS` 与 `AuctionUITexturePathService.DEFAULT_TEXTURE_PATHS` 最初未登记这两个键。`AuctionConfig.GetString` 会拿到空绑定键，`Initialize` 会把 `PropSummaryBar/Image` 记入 `imageFailureCount`，尽管 UI 仍会继续。

已补代码回退路径，并让顶部图标优先读 `AuctionImageMaterialTextures`，`GetBrush.ResourceObject` 仅作第二来源。`GetBrush` 官方存在，返回值字段未写明；`FSlateBrush.ResourceObject` 官方确认为 `UObject*`。本轮未启动 PIE。

# AuctionTestUI 道具栏对齐左侧席位红框

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI PropPanel
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP 回读写入、FlaUI 设计态截图、用户红框对照图、LeftPlayerPanel 几何
> 更新时间：2026-09-03
> 关联主题：AuctionTestUI 二级面板按网页预览与素材回收、AuctionTestUI 价格输入面板设计态贴图绑定、绿洲编辑器控件位置与尺寸准确性
> 排除范围：未改席位/仓库/轮次详情/说明/报价键盘；未启动 PIE；未改 Lua 运行时贴图绑定
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md。知识库未覆盖“红框截图到画布”的官方换算公式；本轮以 MCP 回读的 LeftPlayerPanel 作为未裁切内部锚点。

## 问题

用户红框圈住左侧竞拍席位整列（标题到 P4，不含底部侦察仪器/说明/表情）。当时 PropPanel 仍在画面中央 `(700,210,520x660)`，Background.ResourceObject 为空，设计态显示白底。

## 写入

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_PropPanelRedBox\`

MCP：`plan_16802431_9683dd2e`

回读：

- `LeftPlayerPanel=(10.667,131.246,545.185x800.824)`
- `PropPanel` 同位置同尺寸，`ZOrder=200`，`Background=SkillPanel`，`DrawAs=Image(3)`
- 标题/关闭/摘要/列表/确定使用均落入新父容器
- `PropRow01/08` 与 `PropButton`/`PropImage` 图片层和点击层同格对齐
- `UseSelectedPropButton.Normal=SkillOption`
- `PropButton01.Normal=SkillBar`
- `PropImage01.Brush=SkillEmptySlot`

## 截图

- 用户对照：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_PropPanel_user_before.png`
- 绑定后：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_PropPanelRedBox_after.png`

FlaUI PID 15852。设计态截图不能代替 PIE。底部入口仍在红框外，符合对照图。

## 生效

重新调试 PIE。

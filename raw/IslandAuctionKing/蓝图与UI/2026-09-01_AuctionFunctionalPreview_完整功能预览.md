# IslandAuctionKing 竞拍 UI 完整功能网页预览

> 类型：项目 UI 预览与交互验证记录  
> 主题：`AuctionTestUI` 红框区域的功能恢复前网页预览  
> 适用范围：`IslandAuctionKing` 项目 `Preview/`，用于确认 UI 布局与交互；蓝图对齐结果另见 [素材导入与网页预览对齐](./2026-09-01_AuctionTestUI_素材导入与网页预览对齐.md)
> 证据状态：项目实测（浏览器预览）；用户已确认预览，AuctionTestUI 已通过 MCP 写入并回读设计态
> 来源：项目文件、现有 `Preview/assets/items/*.png`、UI/UX Pro Max 交互检索结果  
> 更新时间：2026-09-01  
> 关联主题：[第二张参照图对齐](./2026-09-01_AuctionTestUI_第二张参照图对齐.md)、[删除角色技能入口](./2026-09-01_AuctionTestUI_删除角色技能入口.md)、[MCP UI 编辑与高保真还原知识库](../../知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)  
> 排除范围：本记录不证明 PIE 当前所有蓝图功能已恢复；网页中的交互状态需要后续映射回编辑器控件和 Lua 事件。

## 预览文件

- 页面：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Preview\AuctionFunctionalPreview.html`
- 服务脚本：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Preview\previewServer.js`
- 地址：`http://127.0.0.1:7391/AuctionFunctionalPreview.html`
- 素材：复用项目现有 `Preview\assets\items\*.png` 藏品图片；未修改原始素材。
- 新增预览素材目录：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Preview\assets\auction\`
- 道具栏素材：`SkillPanel.png`、`SkillBar.png`、`SkillSelected.png`、`SkillEmpty.png`、`SkillOption.png`、`SkillSlider.png`、`SkillTransparentBar.png`。
- 价格输入素材：`PriceInput.png`，来源为 `C:\Users\Administrator\Desktop\素材\竞拍\价格输入.png`；技能素材来源为 `C:\Users\Administrator\Desktop\素材\竞拍\技能\`。
- 游戏说明素材：`InfoPanel.png`、`InfoArrowLeft.png`、`InfoArrowRight.png`，来源为 `C:\Users\Administrator\Desktop\素材\竞拍\说明\`；`InfoPanel.png` 当前改用新增的干净底图 `说明.png`，避免旧参考图自带箭头和页码占位符与网页控件重叠。

## 已实现的预览交互

1. 四个竞拍席位，每个席位保留五轮可点击槽位和收益显示；所有卡片移除会遮挡道具栏的底部状态文字，仅保留标题行状态。
2. 每个玩家的五个轮次格增加历史出价预览，示例值按玩家分别显示在轮次格底部，并保留轮次选择交互。
3. 中央竞拍情报面板保留等待态，并支持侦察仪器、说明、表情弹窗。
4. 右侧唯一仓库按原有展示逻辑使用 6x5 共 30 格，前 12 格加载现有藏品图片，其余为空；藏品图片可点击并更新详情，藏品图鉴入口可打开预览信息。
5. 底部报价支持数字键盘输入、确认报价和锁定暗标；按参照图移除“刷新”和“清空”两个控件及其网页事件。
6. 按用户要求不显示角色技能入口。
7. 顶部品牌文字移动到蓝框对应的下方区域；红框区域改为当前拍卖场名称，当前预览显示“当前拍卖场名称”。
8. 交互状态包含悬停、按下和锁定反馈。
9. “侦察仪器”入口打开道具栏预览：12 个道具选项、顶部道具图片、详情、选定状态和“确定使用”按钮均可操作。
10. 报价键盘使用价格输入底图，提供 1-9、0/00/000、删除、当前轮次秒杀倍数、上轮出价、清除和确定报价，按键文字居中。
11. 道具栏列表限制在底部确认按钮上方，移除绿色选定框和“已选定”文字，避免最后一行道具卡与底栏重叠。
12. “说明”入口使用说明底图，包含竞拍流程、报价规则、道具与藏品三页内容，左右箭头可循环翻页，右上角关闭按钮可关闭。

## 验证证据

- HTTP：`Invoke-WebRequest http://127.0.0.1:7391/AuctionFunctionalPreview.html` 返回 `200`，正文长度 `18181` 字节。
- 页面关键入口存在：`侦察仪器`、`说明`、`表情`、`锁定暗标`、`藏品图鉴`；`刷新`、`清空`不存在。
- 浏览器布局：1280x720 视口下页面无横向/纵向滚动溢出，舞台按 1620x971 比例居中缩放。
- 浏览器 DOM：历史出价节点 `20` 个，席位重复状态文字节点 `0` 个；仓库为 `30` 个格子，其中 `12` 个图片节点。
- 浏览器交互：轮次格可选中；仓库 `藏品 1` 可选中并更新详情；道具栏可切换至“老式军用罗盘”并确认使用；价格键盘输入 `7` 后主界面报价更新为 `7`；刷新/清空按钮不存在。
- 素材回读：道具栏背景命中 `SkillPanel.png`，价格键盘背景命中 `PriceInput.png`，价格按键 `16` 个且 `text-align=center`。
- 道具栏回读：列表底部 `506.82`、确认按钮顶部 `543.15`，存在安全间距；选定文字节点 `0`、绿色选定边框 `false`。
- 说明弹窗回读：背景命中 `InfoPanel.png`，左右翻页按钮 `2` 个，初始页码 `1/3`。
- 说明重叠复核：新底图不含旧的箭头/页码叠加，说明内容区、翻页导航和页码分别位于独立区域。
- 代码检查：`node --check Preview/previewServer.js` 通过。

## 后续生效边界

本轮已按用户确认继续使用 UGCAskQ MCP 对 `AuctionTestUI` 执行 Resolve → Plan → Execute，导入素材、同步 UIConfigTable、恢复设计态文字/入口/历史出价占位并完成 MCP 回读。最终网页对齐后按用户要求未重新 PIE；涉及蓝图、配置表和资源的修改，下一次正式生效仍需重新调试 PIE。



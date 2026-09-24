# AuctionTestUI 素材导入与网页预览对齐

> 类型：项目事实 / 蓝图与 UI
> 主题：竞拍道具栏、价格输入、游戏说明素材导入及 `AuctionTestUI` 设计态对齐
> 适用范围：`IslandAuctionKing` 项目
> 证据状态：MCP 实测；素材与蓝图写入已回读；最终对齐后未重新 PIE（按本轮要求）
> 来源：UGCAskQ MCP PRV 计划与回读、项目网页预览、项目脚本、官方资源导入与 UMG API 文档
> 更新时间：2026-09-01
> 关联主题：[完整功能网页预览](./2026-09-01_AuctionFunctionalPreview_完整功能预览.md)、[第二张参照图对齐](./2026-09-01_AuctionTestUI_第二张参照图对齐.md)、[MCP UI 编辑与高保真还原知识库](../../知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)
> 排除范围：本页不证明本次最终蓝图几何调整已经通过 PIE 运行截图；不修改 `_JsonOutput`，不把 JSON 当作蓝图写入接口。

## 备份

本轮写入前已备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_ImportAssets_And_ModifyAuctionUI\`

包含 `AuctionTestUI.uasset`、`UIConfigTable.uasset` 及本轮涉及的 UI Lua 文件副本。

## 素材导入

用户素材来源：

- `C:\Users\Administrator\Desktop\素材\竞拍\技能\`：8 张技能/道具栏素材
- `C:\Users\Administrator\Desktop\素材\竞拍\说明\`：4 张说明素材
- `C:\Users\Administrator\Desktop\素材\竞拍\价格输入.png`：1 张价格输入底图

导入目标：

- `/IslandAuctionKing/Asset/TuPian/AuctionUI/Skill/`
- `/IslandAuctionKing/Asset/TuPian/AuctionUI/Info/`
- `/IslandAuctionKing/Asset/TuPian/AuctionUI/Price/`

13 张资源均由 UGCAskQ `py:import_asset` 经独立 PRV 计划导入并回读成功。对应计划 ID：

`plan_16793501_0a6a6a90`、`plan_16793501_f2fd0d7d`、`plan_16793501_9cb439b8`、`plan_16793501_6dd9ee68`、`plan_16793501_caeb4db6`、`plan_16793501_c085b44a`、`plan_16793501_7a49a3d5`、`plan_16793501_a7ffcc73`、`plan_16793501_ddbe97af`、`plan_16793501_d0ffdd79`、`plan_16793501_2d52775c`、`plan_16793501_ff376a17`、`plan_16793501_ddbcf1e5`。

每张 Texture2D 的回读属性一致：`CompressionSettings=0`、`LODGroup=16`、`MipGenSettings=13`、`SRGB=True`。

## 配置与运行时绑定

配置资产：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Asset\Data\Table\Customized\UI\UIConfigTable.uasset`

已回读的关键行：

- `UI.ReferenceBlankMode=false`
- `UI.Texture.AuctionSkillPanel=/IslandAuctionKing/Asset/TuPian/AuctionUI/Skill/SkillPanel.SkillPanel`
- `UI.Texture.AuctionInfoPanel=/IslandAuctionKing/Asset/TuPian/AuctionUI/Info/InfoPanel.InfoPanel`
- `UI.Texture.AuctionPriceInput=/IslandAuctionKing/Asset/TuPian/AuctionUI/Price/PriceInput.PriceInput`
- `UI.Texture.AuctionUI_BidKeypad=/IslandAuctionKing/Asset/TuPian/AuctionUI/Price/PriceInput.PriceInput`
- `UI.Texture.AuctionUI_DescriptionPanel=/IslandAuctionKing/Asset/TuPian/AuctionUI/Info/InfoPanel.InfoPanel`

运行时绑定脚本：

- `Script/Function/AuctionUITexturePathService.lua`
- `Script/Function/AuctionUITextureReplacementService.lua`
- `Script/Function/AuctionTestUIService.lua`

`PropPanel` 使用 `AuctionSkillPanel`，`HelpPanel` 使用 `AuctionInfoPanel`。素材导入后的 PIE 日志已回读 `ApplyBorderTexture` 成功、`borderAppliedCount=11`、`buttonAppliedCount=13`、`failureCount=0`，并确认新技能底图和说明底图加载成功。

## 蓝图写入

目标资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

已执行并回读的 PRV 计划：

1. `plan_16795017_395fe7bb`：隐藏 `RefreshButton`、`ClearBidButton` 及其文字；弹窗初始折叠；恢复主界面功能入口可见。
2. `plan_16795159_2490dda3`：使用 `CanvasPanelSlot.SetPosition/SetSize` 修复顶部品牌与拍卖场名称的零尺寸 Slot。回读为 `BrandEyebrowText (24,53,270,45)`、`TitleText (300,20,360,45)`。
3. `plan_16796114_d464f75b`：将设计态同步到网页预览的 1620×971 画布。

最终回读确认：

- 顶部：品牌、当前拍卖场名称、暗标竞价、`00:53`、参赛人数、我的金币均为可见并已设置预览文案。
- 玩家区：P1-P4、玩家名称、累计净收益、五轮序号及 `--` 出价占位可见；`PlayerSubText01-04` 折叠，避免重复的等待加入文字覆盖道具栏。
- 底部：侦察仪器、说明、表情、我的当前报价、锁定暗标及藏品图鉴入口可见。
- 初始弹窗：`PropPanel`、`BidKeypadPanel`、`HelpPanel`、`EmotePanel`、`RoundDetailPanel`、`SkillPanel` 均为 `Collapsed`，由现有 Lua 事件按需打开。
- 已删除控件：刷新、清空及对应文字均为 `Collapsed`。
- 仓库：保留项目既有 6×6 `GridSlots=36` 玩法逻辑，没有为了网页 30 格示意图修改服务端仓库尺寸。

## 设计态画刷边界

当前 UE4.18 `UBorder.Background` 虽在反射 Schema 中可见，但标记为 `BPReadOnly`；本轮通过 MCP 尝试写入 `FSlateBrush.ResourceObject` 后立即回读仍为 `None`，因此没有把失败写入当作蓝图贴图成功。技能栏、说明、价格输入的实际贴图绑定由 `AuctionUITextureReplacementService` 在运行时使用已验证的 `SetBrushFromTexture` 路径完成。

官方依据：

- `D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md`
- `D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`
- `D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateBrush.md`
- `D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\MCP-UI编辑与高保真还原知识库.md`

本轮最终蓝图对齐后按用户要求未启动 PIE；涉及蓝图、配置和资源的改动，下一次正式生效仍需重新调试 PIE。

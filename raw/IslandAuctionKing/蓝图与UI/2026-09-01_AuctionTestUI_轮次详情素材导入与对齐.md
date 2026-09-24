# AuctionTestUI 轮次详情素材导入与对齐

> 类型：项目事实 / 蓝图与 UI
> 主题：玩家轮次详情素材导入、`RoundDetailContent` 视觉层与动态文本布局
> 适用范围：`IslandAuctionKing` 项目
> 证据状态：MCP 实测；资源导入、蓝图写入、配置表写入均已回读；本轮未启动 PIE
> 来源：UGCAskQ MCP Resolve → Plan → Execute、用户素材目录、轮次详情参考图、项目 Lua
> 更新时间：2026-09-01
> 关联主题：[素材导入与网页预览对齐](./2026-09-01_AuctionTestUI_素材导入与网页预览对齐.md)、[MCP UI 编辑与高保真还原知识库](../../知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)、[竞拍 UI 贴图导入与运行时替换](../资产清单/2026-08-31_竞拍UI贴图导入与运行时替换.md)
> 排除范围：`轮次详情参考图.png` 仅作视觉参考，没有导入为运行时整屏贴图；本页不证明 PIE 中最终像素效果。

## 素材来源与导入

用户素材目录：

`C:\Users\Administrator\Desktop\素材\竞拍\轮次详情`

导入目标：

`/IslandAuctionKing/Asset/TuPian/AuctionUI/RoundDetail/`

参考截图 `轮次详情参考图.png` 未作为运行时贴图导入。实际导入五张组件素材，并将中文文件名转换为合法英文资产名：

| 原文件 | 编辑器资产 | 用途 | 尺寸 |
| --- | --- | --- | --- |
| `大透明底.png` | `RoundDetailPanel` | 道具详细作用信息块 | 368×143 |
| `小透明底.png` | `RoundDetailInfoFrame` | 玩家、报价、使用道具、轮次状态信息块 | 168×129 |
| `名称格.png` | `RoundDetailNameFrame` | 五个橙色标题框 | 145×50 |
| `玩家头像格.png` | `RoundDetailPlayerFrame` | 左侧玩家/道具图片框 | 228×231 |
| `退出叉号.png` | `RoundDetailClose` | 关闭图标 | 65×50 |

五张 Texture2D 已通过独立 UGCAskQ 导入计划写入并回读。最终导入参数均为：`LODGroup=16`、`MipGenSettings=13`、`CompressionSettings=0`、`SRGB=True`。

## 蓝图写入

写入前备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-01_RoundDetailAssets_And_UI\`

目标蓝图：

`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

本轮使用 MCP 计划 `plan_16797800_10d780f3`，写入并回读以下内容：

- `RoundDetailContent` 新增 11 个 Image 视觉层和 5 个 TextBlock 标题层。
- `RoundDetailPanel` 调整为 `(466,177,687,601)`，与 687×601 参考弹窗比例一致。
- 左侧 `RoundDetailPlayerFrameImage` 使用 `RoundDetailPlayerFrame`，现有 `RoundDetailPropImage` 保留动态道具图片功能。
- 四个数据块使用 `RoundDetailInfoFrameImage`，底部说明块使用 `RoundDetailDescriptionFrameImage`。
- 五个标题使用 `RoundDetailNameFrameImage`，默认文案为“玩家”“本轮报价”“使用道具”“轮次状态”“道具详细作用”。
- 新增 `RoundDetailCloseImage` 使用 `RoundDetailClose`，设置 `HitTestInvisible`，原有 `RoundDetailCloseButton` 和 Lua `OnClicked` 回调保留。
- 背景层 `ZOrder=-10/-5`，动态文字层 `ZOrder=2/5`；轮次详情文字已设置水平、垂直居中。
- `RoundDetailSubtitleText` 与 `RoundDetailSecurityText` 设计态折叠，避免旧说明占位与新素材重叠；动态安全提示代码仍保留。

MCP 回读确认：`RoundDetailContent` 共 26 个子控件；新增 Image 的 `BrushImage` 均为真实 `Texture2D`，关闭图标也是 `Texture2D`；新标题控件、动态文字和关闭图层存在，坐标与 ZOrder 已保存。

## Lua 与配置

更新文件：

- `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Script\Function\AuctionRoundHistoryUIService.lua`
- `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Script\Function\AuctionUITexturePathService.lua`
- `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Script\Function\AuctionUITextureReplacementService.lua`

`AuctionRoundHistoryUIService` 现在将动态数据写入独立数据控件，不再把标题与数据拼成旧的换行文本。贴图替换服务新增 `IMAGE_BINDINGS`，运行时使用 `UImage:SetBrushFromTexture` 绑定五类轮次详情素材，并保留关闭按钮原点击入口。

`UIConfigTable` 新增并回读：

- `UI.Texture.AuctionRoundDetailDescriptionFrame`
- `UI.Texture.AuctionRoundDetailInfoFrame`
- `UI.Texture.AuctionRoundDetailNameFrame`
- `UI.Texture.AuctionRoundDetailPlayerFrame`
- `UI.Texture.AuctionRoundDetailClose`

配置表路径：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Asset\Data\Table\Customized\UI\UIConfigTable.uasset`

## 验证边界

- MCP 蓝图编译、保存和 `widget_inspect` 回读通过。
- MCP 配置表保存后五行路径、类型和值回读通过。
- 五张贴图加载及导入参数回读通过。
- `node --check Preview/previewServer.js` 通过。
- 本机没有 `luaparse` 或 `luac`，Lua 语法解析未执行，不能把静态检查说成 Lua 解析通过。
- 按用户要求本轮未启动 PIE；蓝图、配置表、资源和初始化绑定的最终运行效果需下次重新调试 PIE 验证。

官方依据：

- `D:\oasis-skill-plus\docs\wiki\新手入门\资源管理与编辑\277_资源导入.md`
- `D:\oasis-skill-plus\docs\api\class\Others\UBorder.md`
- `D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateBrush.md`
- `D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\MCP-UI编辑与高保真还原知识库.md`

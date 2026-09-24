# AuctionTestUI 轮次详情设计态贴图绑定

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI RoundDetailPanel 设计态画刷
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP 回读写入、FlaUI 设计态截图、AuctionUITextureReplacementService IMAGE_BINDINGS
> 更新时间：2026-09-03
> 关联主题：AuctionTestUI 轮次详情素材导入与对齐、AuctionTestUI 二级面板按网页预览与素材回收、MCP UI 编辑与高保真还原知识库、绿洲编辑器控件位置与尺寸准确性
> 排除范围：未改席位/仓库/报价键盘/说明/道具列表；未启动 PIE；表情弹窗仍为预览占位
> 官方依据：D:\oasis-skill-plus\docs\api\class\Others\UImage.md、D:\oasis-skill-plus\docs\api\class\Others\UBorder.md、D:\oasis-skill-plus\docs\api\cppstruct\F\FS\FSlateBrush.md。知识库未覆盖“编辑器设计器对 Collapsed 控件的预览规则”。

## 问题

用户截图中 `RoundDetailPanel` 设计态为深蓝底加白矩形：左侧头像格、2x2 信息块、底部说明块、右上关闭方块均为空白 `UImage`。标题旁仍露出 `玩家轮次与道具详情` 与底部 `仅展示当前端可见的轮次数据`。

MCP 只读回读确认几何已是 `(616.5, 239.5, 687x601)`，但所有 RoundDetail Image 的 `Brush.ResourceObject=None`，`RoundDetailPanel.Background.ResourceObject=None`。运行时贴图由 `AuctionUITextureReplacementService` 绑定，设计态不会显示。

## 写入

备份：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_RoundDetailArtBind\`

MCP 计划：

- `plan_16797087_873dfe23` 绑定画刷
- `plan_16797701_c9bbd069` 收起旧文案
- `plan_16797844_8e677ae1` 恢复道具图槽位

回读结果：

- `RoundDetailPanel.Background=AuctionUI_DescriptionPanel` 687x601
- `RoundDetailPlayerFrameImage=RoundDetailPlayerFrame` 228x231
- 四个 InfoFrame=`RoundDetailInfoFrame` 168x129
- 四个 NameFrame=`RoundDetailNameFrame` 145x50
- `RoundDetailDescriptionFrameImage=RoundDetailPanel` 368x143
- `RoundDetailCloseImage` 与 `RoundDetailCloseButton` 四态=`RoundDetailClose` 65x50
- `RoundDetailSubtitleText` / `RoundDetailSecurityText` Collapsed 并移到 `(-2000,-2000)`
- `RoundDetailPropImage` 仍在 `(42,111,204x194)`，设计态 `DrawAs=None`、透明度 0、Collapsed；运行时由 Lua `SetBrushFromTexture`

Lua：`AuctionRoundHistoryUIService.OpenRoundDetail` 打开弹窗时继续折叠副标题和安全说明。

## 截图

- 用户对照：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_RoundDetail_user_before.png`
- 绑定后：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_RoundDetailArtBind_after.png`
- 收起旧文案后：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_RoundDetailArtBind_after2.png`

FlaUI 窗口 PID 15852，全窗 1936x1056。设计态截图不能代替 PIE。

## 生效

重新调试 PIE。

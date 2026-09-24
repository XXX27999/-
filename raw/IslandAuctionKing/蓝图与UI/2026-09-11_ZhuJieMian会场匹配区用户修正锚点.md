# 2026-09-11 ZhuJieMian 会场匹配区用户修正后锚点回读

> 类型：项目证据
> 主题：ZhuJieMian 红框会场/匹配簇用户手动修正后的点锚点
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian` 红框会场匹配区
> 证据状态：项目实测；UGCAskQ MCP 只读回读通过；本轮未改 `.uasset` / Lua / 配置表
> 来源：用户设计器截图 `codex-clipboard-65e9df9e`；备份 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_ZhuJieMianVenueAnchorLearn\venue_redbox_user_fix.png`；MCP 事务 `ReadZhuJieMianVenueAnchorsAfterUserFix`
> 更新时间：2026-09-11
> 关联主题：UCanvasPanelSlot、FAnchors、FAnchorData、[绿洲 UMG 文字、透明点击层与贴边锚点摆放](../../知识/通用/UI与交互/绿洲UMG文字透明点击层与贴边锚点摆放.md)
> 排除范围：本轮取消继续改主界面；不改顶栏、左下身份、右下三按钮、金币条、ScaleBox 根；不把本页像素升格为所有项目默认值
> 官方依据：[UCanvasPanelSlot](../../../docs/api/class/Others/UCanvasPanelSlot.md)、[FAnchors](../../../docs/api/cppstruct/F/FA/FAnchors.md)、[FAnchorData](../../../docs/api/cppstruct/F/FA/FAnchorData.md)

通用规则见 [绿洲 UMG 文字、透明点击层与贴边锚点摆放](../../知识/通用/UI与交互/绿洲UMG文字透明点击层与贴边锚点摆放.md)。

## 任务边界

用户明确：取消上一轮主界面编辑；只回读红框内控件锚点；学习并记录。用户已手动修正，MCP 只读，`has_mutation=false`。

红框视觉：会场底图、未选择拍卖场、点击选择角色/道具组、未选择、开始匹配。对照件：右上金币 `(1,0)`，右下在线奖励/帮助/保底金 `(1,1)`。

## MCP 状态

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
- 工具：UGCAskQ `ue_py` 只读
- 事务：`ReadZhuJieMianVenueAnchorsAfterUserFix`
- 根：`CanvasPanel_0_Wrapper_Wrapper` ScaleBox；业务父级 `CanvasPanel_0`
- 控件树 46 个节点；焦点 20 个
- 原始回读：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_ZhuJieMianVenueAnchorLearn\ue_py_read_venue_anchors.json`

## 红框会场簇（用户修正后）

全部 `Min=Max=(1.0, 0.5)`，`Alignment=(0,0)`，点锚点 Offsets 是 `(X,Y,W,H)`。X 为负，相对父级右边缘；Y 相对父级垂直中线，上负下正。

| 控件 | 类 | Anchors | Offsets L,T / W x H | Z | 文案 |
| --- | --- | --- | --- | --- | --- |
| Image_160 | Image | (1, 0.5) | -404, -233.5 / 350 x 397.41 | 0 | 会场底图 |
| OpenHouseButton | Button | (1, 0.5) | -386.89, -220.47 / 318.74 x 190 | 30 | 会场热区 |
| VenueNameText | TextBlock | (1, 0.5) | -388, -65.5 / 320 x 36 | 32 | 未选择拍卖场 |
| OpenCharacterButton | Button | (1, 0.5) | -388.18, -15.06 / 160.77 x 104.22 | 30 | 角色热区 |
| PropKindText | TextBlock | (1, 0.5) | -388, -5.5 / 162.41 x 97.15 | 31 | 点击选择角色 |
| CharacterTitleText | TextBlock | (1, 0.5) | -388, 26.5 / 158.33 x 59.81 | 32 | 未选择 |
| OpenPropButton | Button | (1, 0.5) | -210.78, -11.35 / 144.3 x 95.89 | 30 | 道具热区 |
| PropSummaryText | TextBlock | (1, 0.5) | -208, -4.83 / 142.96 x 97.62 | 31 | 点击选择道具组 |
| PropTitleText | TextBlock | (1, 0.5) | -208, 22.5 / 140 x 62.59 | 32 | 未选择 |
| MatchButton | Button | (1, 0.5) | -393.93, 93.46 / 336.52 x 63.56 | 30 | 匹配热区 |
| MatchLabel | TextBlock | (1, 0.5) | -388, 98.5 / 325.78 x 61.7 | 31 | 开始匹配 |

文字 `Visibility=3`（HitTestInvisible）。底图 Z=0，按钮 Z=30，文案 Z=31/32。

## 对照：附近两组不是同一锚点

| 分组 | Anchors | 代表 | Offsets 特征 |
| --- | --- | --- | --- |
| 右上金币 | (1, 0) | 金币UI / 金币 / GoldValueText | X 负，Y 相对顶边 |
| 红框会场簇 | (1, 0.5) | Image_160 及覆盖层 | X 负，Y 相对垂直中线 |
| 右下工具 | (1, 1) | 每日任务 / 帮助 / 保底金及三按钮 | X、Y 都为负 |

## 与 2026-09-10 写入的冲突

[2026-09-10_ZhuJieMian会场匹配区右上锚点](./2026-09-10_ZhuJieMian会场匹配区右上锚点.md) 当时把会场簇写成 `(1, 0)`，理由是“视觉靠右上，参照金币条”。用户手动修正后，垂直锚点是 `0.5` 不是 `0`。

项目实测：会场簇夹在金币条和右下三按钮之间，分辨率变高时要跟着右边缘，垂直方向停在中线附近，不能跟顶边走。`(1, 0)` 只复制了金币条的顶边，Y 仍相对顶；父级变高后簇会贴顶或与底栏间距失调。

本页回读覆盖 2026-09-10 的会场簇锚点结论。2026-09-10 的写入过程仍可作为“抄错参照组”的反例，像素不再当基线。

## 经验（可迁移，像素不可当默认）

1. 点锚点按“父级哪条边变化时控件该跟着走”选，不按“现在看起来靠近哪个角”。
2. 同一视觉组的底图、透明按钮、文字必须同一组 `Min=Max`。会场簇 11 个控件全部 `(1, 0.5)`。
3. 附近组不能当模板。金币 `(1, 0)`、会场 `(1, 0.5)`、工具 `(1, 1)` 是三组。
4. `Alignment` 保持 `(0,0)` 配负 X；未回读前不要改成 `(1, 0.5)` 或 `(1, 1)`。
5. 用户手动摆正并保存后，MCP 回读是新基线。禁止用 `X-1920` 或金币条 Y 回写。
6. 官方 `GetOffsets` 随锚点变化。`(1, 0.5)` 时 Left 是到右边缘的距离，Top 是到垂直中线的距离，Right/Bottom 仍是宽高。

## 验证

- MCP 只读 `success=true`，`has_mutation=false`，`modified_assets=[]`
- 本轮未改工程文件，无 PIE / 热更新
- 工程内无本轮临时 `.py`

## 待查证

- 官方 API 确认 `FAnchors.Minimum/Maximum` 可取 `0.5`，未单独示范“右中点锚点”页面。`(1, 0.5)` 是项目实测，不是官方示例。
- 本页未启动 PIE，未验证换分辨率后与金币条、右下三按钮的间距。

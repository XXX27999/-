# ZhuJieMian 用户摆正后布局回读

> 类型：项目证据
> 主题：ZhuJieMian 设计态手动摆正后的 Slot 几何
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
> 证据状态：项目实测；UGCAskQ MCP 只读回读通过；本轮未改 `.uasset` / `.lua` / 配置表
> 来源：用户设计态截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubLayoutAvatarRematch\ZhuJieMian_redboxes.png`；MCP `ue_py` 事务 `ReadZhuJieMianLayoutOnly`；上一轮估算记录 [2026-09-08_ZhuJieMian主界面点击层与大厅功能接入.md](./2026-09-08_ZhuJieMian主界面点击层与大厅功能接入.md)
> 更新时间：2026-09-08
> 关联主题：AuctionHubUIService.ApplyLayout、UCanvasPanelSlot、透明点击层
> 排除范围：本页不修改头像/名称/金币加载，不做二次匹配，不把这些像素升格为通用默认值
> 官方依据：[UCanvasPanelSlot](../../../docs/api/class/Others/UCanvasPanelSlot.md)、[FAnchorData](../../../docs/api/cppstruct/F/FA/FAnchorData.md)、[FAnchors](../../../docs/api/cppstruct/F/FA/FAnchors.md)

通用规则见 [绿洲 UMG 文字、透明点击层与贴边锚点摆放](../../知识/通用/UI与交互/绿洲UMG文字透明点击层与贴边锚点摆放.md)。

## MCP 状态

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
- 工具：UGCAskQ `ue_py`，只读，无 PRV plan
- 事务：`ReadZhuJieMianLayoutOnly`
- `success=true`，`has_mutation=false`，`modified_assets=[]`
- 控件数 44，根节点 `CanvasPanel_0`
- 原始回读：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubLayoutAvatarRematch\LayoutKnowledge\ue_py_read_zjm_layout_result.json`
- 节点表：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubLayoutAvatarRematch\LayoutKnowledge\ZhuJieMian_layout_nodes.json`
- 对照截图红框是要求 2 的头像/名称/金币范围，本页只当视觉对照，不改加载逻辑

`GetPosition/GetSize` 对点锚点等于 `LayoutData.Offsets` 的 `(Left,Top,Right,Bottom)`。`Min=Max=(0,1)` 时单独 `GetOffsets()` 可能把 Top/Right/Bottom 打成 0，下表一律用 `LayoutData`。

## 锚点分组

贴边底图和对应文字已经用边锚点；上一轮新增的透明按钮仍全部是左上角 `(0,0)`。

| 分组 | Anchors Min=Max | 控件 |
| --- | --- | --- |
| 铺满 | `(0,0)-(1,1)` | 参考图 |
| 左下 | `(0,1)` | 头像框、玩家名称底图、服务器剩余时间 |
| 右上 | `(1,0)` | 金币UI、金币图标、GoldValueText |
| 右下 | `(1,1)` | 每日任务/帮助/保底金及其上方条，以及「在线奖励/帮助/保底金」文字 |
| 左上绝对 | `(0,0)` | 顶部UI、顶部五字、会场框 Image_160、玩家名称文字、会场/道具/角色/匹配按钮和新增文字 |

## 顶部页签：文字对底图内容，不对按钮中心

上一轮估算把五个透明按钮写成 `86/214/342/470/598,28`、统一 `128x54`。用户摆正后，文字仍在顶栏内容带 `Y=32`，按钮略缩进到各页签斜切区内。差值说明：不能按网页预览的等距 `left` 去写字。

| 文案 | 文字控件 | 文字 Pos/Size | 透明按钮 | 按钮 Pos/Size | 相对上一轮按钮估算 |
| --- | --- | --- | --- | --- | --- |
| 仓库 | TextBlock_133 | 104,32 / 65x36.43 | WarehouseButton | 64.7,21.52 / 119.67x55.85 | 估算 86,28 128x54；ΔX=-21.3 ΔY=-6.5 ΔW=-8.3 ΔH=+1.9 |
| 装扮 | TextBlock_226 | 232,32 / 56.48x29.81 | DressButton | 212.15,21.52 / 101.15x55.85 | 估算 214,28；ΔX=-1.9 ΔY=-6.5 ΔW=-26.9 |
| 签到 | TextBlock_287 | 360,32 / 100x40 | CheckinButton | 337.37,22.44 / 100.22x52.15 | 估算 342,28；ΔX=-4.6 ΔY=-5.6 ΔW=-27.8 |
| 商城 | TextBlock_406 | 484,32 / 55.56x32.59 | ShopButton | 463.52,22.44 / 99.3x53.07 | 估算 470,28；ΔX=-6.5 ΔY=-5.6 ΔW=-28.7 |
| 邮件 | TextBlock_469 | 608,32 / 100x40 | MailButton | 587.81,21.52 / 117.81x54 | 估算 598,28；ΔX=-10.2 ΔY=-6.5 ΔW=-10.2 |

顶部UI 底图本身是 `(0,0)` 锚点、Pos `44,-212`、Size `675x523.33`。负 Top 表示贴图像素比可见页签条高，可见文字带大约在 `Y=32`。以后补字应落在这条带上，而不是按按钮中心或 CSS `top:28`。

## 会场 / 道具 / 角色 / 匹配

上一轮按网页预览把会场热区写成 `792,100 448x420`，匹配文字写成 `792,668`，道具摘要写成 `812,536`。用户摆正后，匹配和道具文字上移到会场框内部，不再落在 668/536 那条错误带上。

| 控件 | 当前 Pos | 当前 Size | Z | 上一轮估算 | 差值 |
| --- | --- | --- | --- | --- | --- |
| Image_160 会场底图 | 794.89,101.67 | 350x397.41 | 0 | 无（原底图） | 内容框约 795,102 |
| OpenHouseButton | 800.33,103.70 | 338.74x203.33 | 30 | 792,100 / 448x420 | ΔX=+8.3 ΔY=+3.7 ΔW=-109.3 ΔH=-216.7 |
| OpenCharacterButton | 809.04,322.44 | 162.44x104.22 | 30 | 1022,528 / 218x132 | 估算把角色槽写到右下；现与左槽对齐。ΔX=-213 ΔY=-206 |
| OpenPropButton | 986.44,326.15 | 147.63x95.89 | 30 | 792,528 / 218x132 | 估算把道具槽写到左下。ΔX=+194 ΔY=-202 |
| MatchButton | 804.96,430.96 | 333.19x63.56 | 30 | 792,668 / 448x58 | ΔX=+13.0 ΔY=-237.0 ΔW=-114.8 ΔH=+5.6 |
| MatchLabel「开始匹配」 | 808.67,431.89 | 325.78x61.70 | 31 | 792,668 / 448x58 | ΔX=+16.7 ΔY=-236.1 |
| PropKindText「道具」 | 808.30,326.74 | 165.19x99.93 | 31 | 812,536 | ΔX=-3.7 ΔY=-209.3 |
| PropSummaryText「点击选择道具组」 | 987.00,325.93 | 144.81x101.70 | 31 | 道具槽内估算 | 现与 OpenPropButton 重合，不再跟 536 |
| VenueNameText「未选择拍卖场」 | 810,450 | 320x36 | 21 | 无 | 落在匹配条内，Z 低于 MatchLabel |
| PropTitleText / CharacterTitleText「未选择」 | 805,555 / 986,555 | 149x70 | 21 | 无 | Y=555，在会场框下方；本轮不改加载，只记录 |

会场透明按钮现在只盖上半展示窗 `203px` 高，不再用 `448x420` 整块盖住道具/角色/匹配。文字层 Z=31，按钮 Z=30，底图 Z=0，符合“点击层盖底图、文字独立且更高”。

OpenPropButton 与 OpenCharacterButton 相对上一轮左右对调：当前左槽是角色点击层+「道具」文案，右槽是道具点击层+「点击选择道具组」。这是摆正后的真实状态，本轮不改逻辑，只作为新基线记录。

## 右下工具：底图用右下锚点，透明按钮却写成左上角

底图和标题字是 `Min=Max=(1,1)`，X/Y 为负，相对父级右下角。上一轮透明按钮按 `1487/1606/1718,900` 左上角绝对坐标写入；用户摆正后它们仍停在 `(0,0)` 锚点，Pos 变成 `802/921/1036,516`，已经离开右下三图标。

| 视觉 | 底图 Image Pos/Size（右下锚点） | 标题文字 Pos/Size | 透明按钮 Pos/Size（左上锚点） |
| --- | --- | --- | --- |
| 在线奖励 | 每日任务 -433.17,-168 / 169.17x167.5；上方条 -396,-159 / 95.42x28.39 | TextBlock_533 -380,-155 / 100x40 | OpenRewardButton 801.83,515.67 / 102.33x124.67 |
| 帮助 | 帮助 -314.17,-167.83 / 164.17x167.5；上方条 -277.92,-158.75 / 93.75x29.58 | TextBlock_616 -248,-155 / 32.5x17.5 | OpenHelpButton 921.39,517.81 / 96.04x118.93 |
| 保底金 | 保底金 -163,-136.67 / 102.5x100.83；上方条 -159.17,-158.75 / 94.17x30 | TextBlock_715 -136,-155 / 69.64x25.36 | OpenGuaranteeButton 1036.5,516 / 103.5x123.5 |

标题字已经对齐上方条，可复用。透明按钮没有复制 `(1,1)`，不能和底图 Pos 直接做减法。后续若要修点击热区，应把按钮锚点改成 `(1,1)` 再按底图 Offsets 内缩，而不是继续用 1487,900。

## 右上金币与左下头像（只记录，不改加载）

截图红框对应下列控件。本轮不改头像、名称、金币的运行时加载。

| 控件 | Anchors | Pos | Size | Z | 说明 |
| --- | --- | --- | --- | --- | --- |
| 金币UI | (1,0) | -424,-56 | 390x206.25 | 0 | 右上贴边底图 |
| 金币 | (1,0) | -328,24 | 68.75x65.62 | 0 | 金币图标 |
| GoldValueText | (1,0) | -250,36 | 200x44 | 20 | 文案「30,000」；与图标同一锚点 |
| 头像框 | (0,1) | 47,-172.57 | 153.57x154.29 | 0 | 左下贴边 |
| 玩家名称 底图 | (0,1) | 60,-235 | 585x318.75 | -1 | 底图很高，可见胶囊只是其中一条 |
| PlayerNameText | (0,0) | 191,588 | 303x40 | 20 | 文案「玩家名称」；文字未用左下锚点 |
| TextBlock_73 | (0,0) | 190.67,588 | 303.33x40 | 0 | 与 PlayerNameText 几乎重叠的设计态字 |

PlayerNameText 仍是左上角绝对坐标，底图却是左下锚点。这是红框范围的既有状态，不是本轮修改目标。

## 与运行时脚本的冲突（只记录）

只读 `AuctionHubUIService.GetLayout/ApplyLayout`：初始化仍会把 `OpenHouseButton` 写成配置默认 `792,100 / 448x420`。用户摆正后的设计态是 `800.33,103.70 / 338.74x203.33`。本任务按文件边界不改 Lua 和配置表；若重新 PIE，会场点击层可能被旧估算值盖回。文字控件本轮没有被 `ApplyLayout` 写坐标，MatchLabel/PropKindText/PropSummaryText 的设计态基线可保留。

## 本轮明确不做

- 不改任何 `.lua`、`.uasset`、`UIConfigTable`
- 不二次匹配
- 不改头像 / 名称 / 金币加载
- 不把上表像素写进通用知识当默认值

## 验证

- MCP 只读回读成功，无写入
- 工程内无本轮临时 `.py` / `__pycache__`
- 知识回写与备份均在知识库目录，不在 UGC 工程内

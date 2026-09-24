# 2026-09-10 ZhuJieMian 会场匹配区右上锚点

> 类型：项目证据
> 主题：ZhuJieMian 会场/匹配簇从左上点锚点改为右上点锚点
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
> 证据状态：项目实测；UGCAskQ MCP 写入与独立回读通过；本轮未启动 PIE
> 来源：用户设计器截图 `codex-clipboard-1f631eac` / `29886764` / `efd4dc96`；MCP `plan_16790873_b4143cd6`；对照底图 [保底金/帮助/在线奖励](./2026-09-08_ZhuJieMian用户摆正后布局回读.md)
> 更新时间：2026-09-11（会场簇锚点结论已被用户修正覆盖）
> 关联主题：UCanvasPanelSlot.SetAnchors / SetMinimum / SetMaximum、FAnchors、AuctionHubUIService.ApplyLayout
> 排除范围：未改右下三按钮、左下头像名称倒计时、顶栏页签、金币条；未再包裹 ScaleBox/SizeBox；未改 Lua 运行时坐标
> 官方依据：[UCanvasPanelSlot](../../../docs/api/class/Others/UCanvasPanelSlot.md)、[FAnchors](../../../docs/api/cppstruct/F/FA/FAnchors.md)、[FAnchorData](../../../docs/api/cppstruct/F/FA/FAnchorData.md)

通用规则见 [绿洲 UMG 文字、透明点击层与贴边锚点摆放](../../知识/通用/UI与交互/绿洲UMG文字透明点击层与贴边锚点摆放.md)。

## 写入前状态（项目实测）

用户三张设计器截图：

- `2560x1080`：右下保底金/帮助/在线奖励贴边正常，会场匹配区仍按左上绝对坐标停在画布中部偏右。
- `1116x1039`：会场框冲出右边界，金币条与顶栏页签重叠；右下三按钮仍贴在右下角。
- `1946x600`：多分辨率对照，右下三按钮始终贴边，会场簇不跟着右边缘走。

独立只读回读 `InspectZhuJieMianAllAnchorsNow`：

| 分组 | Anchors Min=Max | 代表控件 |
| --- | --- | --- |
| 右下工具（用户指定参照） | `(1,1)` | 保底金 / 帮助 / 每日任务、OpenGuarantee/OpenHelp/OpenRewardButton |
| 右上金币 | `(1,0)` | 金币UI / GoldValueText |
| 左下身份 | `(0,1)` | 头像框 / 玩家名称 / CountdownText |
| 会场匹配区（问题簇） | `(0,0)` | Image_160、OpenHouse/Character/Prop/MatchButton、Venue/Character/Prop 文案 |

官方确认：`UCanvasPanelSlot.GetOffsets` 随锚点变化，点锚点 Offsets 是 `(X,Y,W,H)`。右下三按钮是 `Alignment=(0,0)` 配负 Offsets，不是 `(1,1)` 对齐。

## MCP 状态

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
- 工具：UGCAskQ `ue_plan_submit` → `ue_py`
- plan_id：`plan_16790873_b4143cd6`
- 事务：`WriteZhuJieMianRightAnchors`
- 独立回读：`VerifyZhuJieMianRightAnchorsIndependent`，`has_mutation=false`
- 写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_ZhuJieMianCornerAnchors\ZhuJieMian_before.uasset`

未包裹 ScaleBox。上一轮把 ScaleBox 当根会撑破设计器，见 [2026-09-08_ZhuJieMian锚点恢复与服务器倒计时](./2026-09-08_ZhuJieMian锚点恢复与服务器倒计时.md)。

## 写入规则

会场匹配区视觉上靠右上，参照金币条而不是右下三按钮的 `(1,1)`。复制同一套点锚点写法：

1. `Slot.SetMinimum/SetMaximum` 写成 `Min=Max=(1,0)`
2. `SetAlignment(0,0)`
3. `SetPosition(X-1920, Y)`，宽高 ZOrder 保持回读值

`1920` 只用于把当前左上坐标换到右上坐标系，1920 设计台上的相对位置不变。

## 独立回读结果

| 控件 | Anchors | Offsets (L,T,W,H) | Z |
| --- | --- | --- | --- |
| Image_160 | (1,0) | -1125.11, 101.67 / 350x397.41 | 0 |
| OpenHouseButton | (1,0) | -1119.67, 103.7 / 338.74x203.33 | 30 |
| OpenCharacterButton | (1,0) | -1110.96, 322.44 / 162.44x104.22 | 30 |
| OpenPropButton | (1,0) | -933.56, 326.15 / 147.63x95.89 | 30 |
| MatchButton | (1,0) | -1115.04, 430.96 / 333.19x63.56 | 30 |
| VenueNameText | (1,0) | -1110, 270 / 320x36 | 32 |
| CharacterTitleText | (1,0) | -1110.96, 362.22 / 158.33x59.81 | 32 |
| PropTitleText | (1,0) | -930, 358.52 / 140x62.59 | 32 |
| MatchLabel | (1,0) | -1111.33, 431.89 / 325.78x61.7 | 31 |
| PropKindText | (1,0) | -1108.92, 329.52 / 162.41x97.15 | 31 |
| PropSummaryText | (1,0) | -931.15, 333.34 / 142.96x94.29 | 31 |

未改对照：

| 控件 | Anchors | Offsets |
| --- | --- | --- |
| 保底金 | (1,1) | -163, -136.67 / 102.5x100.83 |
| 帮助 | (1,1) | -314.17, -167.83 / 164.17x167.5 |
| 每日任务 / 在线奖励底图 | (1,1) | -433.17, -168 / 169.17x167.5 |
| OpenGuaranteeButton | (1,1) | -160, -130 / 100x95 |
| OpenHelpButton | (1,1) | -300, -155 / 140x130 |
| OpenRewardButton | (1,1) | -418, -155 / 140x130 |
| GoldValueText | (1,0) | -250, 36 / 200x44 |
| 头像框 | (0,1) | 47, -172.57 / 153.57x154.29 |
| WarehouseButton | (0,0) | 64.7, 21.52 / 119.67x55.85 |

根仍是 `CanvasPanel_0`。`AuctionHubUIService.ApplyLayout` 仍跳过运行时 `SetPosition/SetSize`。

## 验证

- MCP 写入 `success=true`，`used_count=1`。
- 独立回读 11 个目标控件全部 `Min=Max=(1,0)`，Alignment `(0,0)`。
- 右下三按钮与左下身份区数值与写入前一致。
- 本轮未启动 PIE。已打开的「编辑 ZhuJieMian」页签必须关掉再开。

## 待查证

- 极窄预览（约 1116 宽）上，会场簇会跟着右边缘左移；顶栏仍是左上点锚点，和右上金币在过窄画布上仍可能靠近。这是 1920 设计宽与点锚点混用的结果，官方 20269 ScaleBox 方案因设计器包围盒问题已撤回，不能把本页像素升格为通用默认值。

## 2026-09-11 结论覆盖

用户手动修正后，会场簇垂直锚点是 `0.5` 不是 `0`。本页 `(1,0)` 像素不再当基线。见 [2026-09-11_ZhuJieMian会场匹配区用户修正锚点](./2026-09-11_ZhuJieMian会场匹配区用户修正锚点.md)。

## 2026-09-10 会场簇平移到金币列

用户第二张目标图要求：1920×1080 设计台上会场框帖在右上金币正下方、右下三按钮上方。上一轮只把锚点改成 `(1,0)`，X 仍是左列 `-1125`，所以 1920 画布仍停在左侧。

- plan_id：`plan_16793859_81ef5f1a`
- 事务：`WriteZhuJieMianVenueRightColumn`
- 独立回读：`VerifyZhuJieMianVenueRightColumnIndependent`，`has_mutation=false`
- 写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_ZhuJieMianCornerAnchors\ZhuJieMian_before_venue_right_column.uasset`
- 平移：`DX=+701.11`，`Image_160.Left` 从 `-1125.11` 改到 `-424`，与 `金币UI.Left` 对齐。Y/W/H/Z 与锚点不变。

| 控件 | Anchors | Offsets (L,T,W,H) |
| --- | --- | --- |
| Image_160 | (1,0) | -424, 101.67 / 350x397.41 |
| OpenHouseButton | (1,0) | -418.56, 103.7 / 338.74x203.33 |
| OpenCharacterButton | (1,0) | -409.85, 322.44 / 162.44x104.22 |
| OpenPropButton | (1,0) | -232.45, 326.15 / 147.63x95.89 |
| MatchButton | (1,0) | -413.93, 430.96 / 333.19x63.56 |
| VenueNameText | (1,0) | -408.89, 270 / 320x36 |
| CharacterTitleText | (1,0) | -409.85, 362.22 / 158.33x59.81 |
| PropTitleText | (1,0) | -228.89, 358.52 / 140x62.59 |
| MatchLabel | (1,0) | -410.22, 431.89 / 325.78x61.7 |
| PropKindText | (1,0) | -407.81, 329.52 / 162.41x97.15 |
| PropSummaryText | (1,0) | -230.04, 333.34 / 142.96x94.29 |

未改：金币条、右下三按钮、左下头像名称、顶栏页签。已打开的「编辑 ZhuJieMian」页签必须关掉再开。生效：重新调试 PIE。

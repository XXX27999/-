# 2026-09-08 ZhuJieMian 锚点恢复与服务器倒计时

> 类型：项目证据
> 主题：ZhuJieMian 贴边锚点恢复、左下服务器倒计时、选择完成后大厅回写
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
> 证据状态：项目实测；UGCAskQ MCP 写入与独立回读通过；本轮未启动 PIE
> 来源：用户截图 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubAnchorsCountdown\ZhuJieMian_redbox_countdown.png`；MCP `plan_16796638_fd1f1447`；用户摆正基线 [2026-09-08_ZhuJieMian用户摆正后布局回读.md](./2026-09-08_ZhuJieMian用户摆正后布局回读.md)
> 更新时间：2026-09-08
> 关联主题：UCanvasPanelSlot、FAnchors、AuctionHubUIService.ApplyCountdown、三个选择层确认回写
> 排除范围：不把本页像素升格为通用默认值；里层点锚点像素仍只对 IslandAuctionKing 有效
> 官方依据：[UCanvasPanelSlot](../../../docs/api/class/Others/UCanvasPanelSlot.md)、[FAnchors](../../../docs/api/cppstruct/F/FA/FAnchors.md)、[20269_UI自适应屏幕](../../../docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md)、[AGameStateBase.GetServerWorldTimeSeconds](../../../docs/api/class/Others/AGameStateBase.md)

通用规则见 [绿洲 UMG 文字、透明点击层与贴边锚点摆放](../../知识/通用/UI与交互/绿洲UMG文字透明点击层与贴边锚点摆放.md)。

## 写入前状态（项目实测）

独立回读 `InspectZhuJieMianAnchorsCountdown` 显示：头像框、玩家名称底图、服务器剩余时间、金币UI、会场按钮、仓库按钮被改成 `Anchors Min=(0,0) Max=(1,1)`。`WarehouseButton` Offsets 变成约 `64.7,21.5 / 1015x598`，几乎铺满屏幕。`VenueNameText` / `CharacterTitleText` / `PropTitleText` / `MatchLabel` Font.Size=0、FontObject=None。这能解释“选择完成后主界面没有反馈”：文案控件存在，但字号为 0 且被拉伸热区挡住。

用户摆正基线仍以 [2026-09-08_ZhuJieMian用户摆正后布局回读.md](./2026-09-08_ZhuJieMian用户摆正后布局回读.md) 为准。

## MCP 状态

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
- 配置表：`/IslandAuctionKing/Asset/Data/Table/Customized/UI/UIConfigTable`
- 工具：UGCAskQ `ue_plan_submit` → `ue_py`
- plan_id：`plan_16796638_fd1f1447`
- 事务：`RestoreZhuJieMianAnchorsCountdown`
- 独立回读：`VerifyZhuJieMianAnchorsCountdownIndependent`，`has_mutation=false`
- 写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260908_HubAnchorsCountdown\`

本轮未对根画布做官方 `ScaleBox + SizeBox` 包裹，避免一次改树把用户摆正坐标冲掉。自适应层次结构仍是待查证，下轮可单独做。

## 写入结果（独立回读）

| 控件 | Anchors Min=Max | Offsets | Font |
| --- | --- | --- | --- |
| 头像框 | (0,1) | 47,-172.57 / 153.57x154.29 | - |
| 玩家名称 底图 | (0,1) | 60,-235 / 585x318.75 | - |
| 服务器剩余时间 | (0,1) | 100,-215 / 397.22x195.56 | - |
| PlayerNameText | (0,1) | 191,-95.75 / 303.43x56.25 | Roboto Bold 22 |
| CountdownText | (0,1) | 186.85,-128.56 / 208.33x30.44 | Roboto Bold 20，文案 `--:--` |
| 金币UI | (1,0) | -424,-56 / 390x206.25 | - |
| GoldValueText | (1,0) | -250,36 / 200x44 | Roboto Bold 22，文案 `30,000` |
| WarehouseButton | (0,0) | 64.7,21.52 / 119.67x55.85 | - |
| OpenHouseButton | (0,0) | 800.33,103.7 / 338.74x203.33 | - |
| OpenCharacterButton | (0,0) | 809.04,322.44 / 162.44x104.22 | - |
| OpenPropButton | (0,0) | 986.44,326.15 / 147.63x95.89 | - |
| VenueNameText | (0,0) | 810,270 / 320x36 | Roboto Bold 18，文案「未选择拍卖场」 |
| CharacterTitleText | (0,0) | 809.04,340 / 150x70 | Roboto Bold 18，文案「未选择」 |
| PropTitleText | (0,0) | 990,340 / 140x70 | Roboto Bold 18，文案「未选择」 |
| OpenRewardButton | (1,1) | -418,-155 / 140x130 | 透明点击层 |

新增配置行：`UI.Hub.Countdown.EmptyText=--:--`、`WaitingText=等待开局`、`ColorR/G/B/A=1`。

## Lua

- `AuctionHubUIService.ApplyLayout` 不再 `SetPosition/SetSize`，保留设计态坐标。
- `ApplyCountdown` 读 `GameState:GetAuctionServerTime()`。`PhaseEndTime>0` 显示 `mm:ss`；Waiting 且无截止显示「等待开局」。
- `Refresh` 每秒节流调用倒计时刷新。
- 三个选择层确认后乐观写大厅文案，再 Refresh，再 Hide。详见：
  - [2026-09-08_角色选择确认后大厅无反馈.md](./2026-09-08_角色选择确认后大厅无反馈.md)
  - [2026-09-08_AuctionPropSelectUI_确认后大厅乐观写入组名.md](../开发记录/2026-09-08_AuctionPropSelectUI_确认后大厅乐观写入组名.md)
  - [2026-09-08_AuctionHouseSelectUI_选场后大厅乐观写入场名.md](../开发记录/2026-09-08_AuctionHouseSelectUI_选场后大厅乐观写入场名.md)

## 验证

- MCP 写入 success=true，独立回读 CountdownText 存在、Roboto Bold 20、左下锚点。
- Lua 关键字配对 depth=0。本机 luacheck 因缺 outputDir 未出汇总。
- 工程内无 `_tmp_*.py` / `__pycache__`。
- 本轮未启动 PIE。已打开的「编辑 ZhuJieMian」页签需关闭后重开。

## 2026-09-10 官方自适应包裹

用户 PIE 两张不同分辨率截图里，会场框、右下三按钮、左下名称条相对位置漂了；第三张 UI 编辑器 1920×1080 才是目标视觉。根因是 ZhuJieMian 当时仍是裸 `CanvasPanel_0`，点锚点跟着屏幕走。

按 [20269_UI自适应屏幕](../../../docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md) 与本项目 `AuctionTestUI` 实测，MCP 包裹为：

`CanvasPanel_0_Wrapper_Wrapper_Wrapper`（外画布）→ `CanvasPanel_0_Wrapper_Wrapper`（ScaleBox，Stretch=2/ScaleToFit，StretchPc=2，UsePcParams=False，Anchors 0,0-1,1 Offsets 0）→ `CanvasPanel_0_Wrapper`（SizeBox 1920×1080，两个 Override=True）→ 原 `CanvasPanel_0`（业务点锚点未改）。

- plan_id：`plan_16778672_20d386f0`（包裹）、`plan_16779025_8fa3ec14`（外层四向拉伸）
- 独立回读：`VerifyZhuJieMianScaleIndependent`。头像框仍 `(0,1) 47,-172.57 / 153.57x154.29`，GoldValueText 仍 `(1,0) -250,36 / 200x44`，OpenHouseButton 仍 `800.33,103.7 / 338.74x203.33`。
- `ue.FAnchors` 绑定不存在。外层四向拉伸必须 `LayoutData.clone()` 后 `Anchors.set_field(Minimum/Maximum, FVector2D)`，再 `slot.set_property('LayoutData', ld)`。
- 已打开的「编辑 ZhuJieMian」页签需关闭后重开。生效：必须重新 PIE，换分辨率对照第三张编辑器布局。

## 待查证

- ScaleToFit 在非 16:9 上会留黑边。若用户要求铺满无留白，需在 ScaleToFit 与 Fill 之间再取舍，不能 silently 改成 Fill。

## 2026-09-10 设计器缩成一团的修复

用户重新打开「编辑 ZhuJieMian」后，绿色 1920×1080 SizeBox 里大厅缩到中间一小块，与原布局不符。独立回读确认控件 Offsets 没被改小，是多包了一层外画布当 RootWidget，设计器把整页 HUD 当成小内容来缩。

对照 `AuctionTestUI`：根就是 ScaleBox。本轮把 `CanvasPanel_0_Wrapper_Wrapper` 提成 RootWidget，去掉空的外画布。当前树：

`ScaleBox`（根，Stretch=2/ScaleToFit，StretchPc=2）→ `SizeBox` 1920×1080（居中）→ 原 `CanvasPanel_0`（内层 Fill）。

- plan_id：`plan_16780690_1e27b0d2`
- 独立回读：头像框仍 `(0,1) 47,-172.57 / 153.57x154.29`，GoldValueText 仍 `(1,0) -250,36 / 200x44`，OpenHouseButton 仍 `800.33,103.7 / 338.74x203.33`。
- 已打开的页签需关闭后重开。生效：重新打开 ZhuJieMian 设计器，并重新 PIE。

## 2026-09-10 设计器仍缩小：Stretch=None

用户关闭页签再打开后，1920×1080 舞台里大厅仍缩在中间。根因不是坐标被改小，而是根 ScaleBox 的 `Stretch=ScaleToFit(2)` 把 1920×1080 SizeBox 再缩进设计器预览区。

本轮把设计态改为 `Stretch=None(0)` / `StretchPc=0`，SizeBox 仍 1920×1080，内层点锚点未改。PIE 由 `AuctionHubUIService.CreateAndShow` 对根 ScaleBox `SetStretch(2)`。

- plan_id：`plan_16781306_263b10e3`
- 独立回读：`Stretch=0`，头像框仍 `(0,1) 47,-172.57`，GoldValueText 仍 `(1,0) -250,36`，OpenHouseButton 仍 `800.33,103.7`。
- 已打开的「编辑 ZhuJieMian」页签必须关掉再开，否则仍显示旧的 ScaleToFit 预览。

## 2026-09-10 撤回 ScaleBox 根

用户反馈设计器仍缩小，且控件画出 1920 画布。项目实测：把 ScaleBox/SizeBox 当根后，设计器按贴边控件的包围盒计算 DesiredSize，负 Offsets 的左下/右上件会把舞台撑出 1920×1080，预览再整体缩小。

本轮撤回包裹：`CanvasPanel_0` 重新作为 RootWidget，ScaleBox/SizeBox 已不在树上。内层点锚点未改。CreateAndShow 里的运行时 SetStretch 已删除。

- plan_id：`plan_16781995_bda947a0`
- 独立回读：root=`CanvasPanel_0`，hasScale=false，hasSize=false；头像框仍 `(0,1) 47,-172.57`，GoldValueText 仍 `(1,0) -250,36`，OpenHouseButton 仍 `800.33,103.7`。
- 必须关掉「编辑 ZhuJieMian」页签再打开。官方 20269 自适应不再走蓝图根包裹，避免设计器被包围盒放大。

## 2026-09-10 运行时视口等比适配

用户两张 PIE 图仍显示：会场框相对左上绝对坐标，金币/右下工具贴边锚点，分辨率一变就挤在一起。官方 `UUserWidget.AddToViewport` 会铺满屏幕，点锚点和绝对坐标会拆开。ScaleBox 不能再当 ZhuJieMian 根，设计器会被包围盒撑爆。

本轮蓝图保持 `CanvasPanel_0` 根和编辑器 1920×1080 点锚点。运行时 `AuctionHubUIService.ApplyViewportFit`：`SetDesiredSizeInViewport(1920,1080)`，读 `UGCWidgetManagerSystem.GetViewportSize` 或 `PlayerController:GetViewportSize`，按 `min(viewW/1920, viewH/1080)` `SetRenderScale`，再 `SetPositionInViewport` 居中。

- 配置：`UI.Hub.DesignWidth=1920`、`UI.Hub.DesignHeight=1080`，plan_id `plan_16786970_377e92e3`
- Lua 可热更新；视口锁定必须重新 PIE。
- 预估日志：`【AuctionHubUIService+ApplyViewportFit】关键数据 design=1920x1080 view=... scale=...`

## 2026-09-10 视口铺满取消小卡片缩放

用户 PIE 宽窗露 3D、窄窗裁切、编辑器占比更大。日志确认 `view=1280x720 scale=0.67`。本轮 `ApplyViewportFit` 改为四向拉伸铺满，详见 [2026-09-10_ZhuJieMian视口铺满与占比修复](./2026-09-10_ZhuJieMian视口铺满与占比修复.md)。

## 2026-09-10 设计器多分辨率对照缩小

用户设计器对照 2560/3840 时 1920 舞台停在左上角。本轮按 AuctionTestUI 包 ScaleBox 根，Stretch=ScaleToFill(5)，详见 [2026-09-10_ZhuJieMian_ScaleToFill铺满大分辨率](./2026-09-10_ZhuJieMian_ScaleToFill铺满大分辨率.md)。

## 2026-09-10 ScaleToFill 裁切

用户设计器截图显示顶栏和会场被裁出白框。设计态改回 Stretch=None，PIE SetStretch(ScaleToFit)，详见 [2026-09-10_ZhuJieMian设计态None运行时ScaleToFit](./2026-09-10_ZhuJieMian设计态None运行时ScaleToFit.md)。

## 2026-09-11 HUD 超出 1920 画布

Stretch=None 后贴边负偏移把包围盒撑大，1920 SizeBox 缩成中间虚线框。SizeBox/Canvas 开 ClipToBoundsAlways，详见 [2026-09-11_ZhuJieMian_HUD收回1920画布](./2026-09-11_ZhuJieMian_HUD收回1920画布.md)。

## 2026-09-10 会场匹配簇改成右上点锚点

后续用户设计器截图仍显示会场框跟左上绝对坐标溢出。已改成 `Min=Max=(1,0)`，详见 [2026-09-10_ZhuJieMian会场匹配区右上锚点](./2026-09-10_ZhuJieMian会场匹配区右上锚点.md)。

# 2026-09-03 AuctionTestUI 席位1-3对齐席位4

> 类型：项目证据
> 主题：蓝图与 UI / AuctionTestUI 玩家席位控件布局
> 适用范围：IslandAuctionKing
> 证据状态：项目实测
> 来源：UGCAskQ MCP 回读与写入、FlaUI 编辑器截图、用户提供的 P1-P4 对照图
> 更新时间：2026-09-03
> 关联主题：2026-09-02_AuctionTestUI_网页预览红框美化、UCanvasPanelSlot
> 排除范围：不覆盖 Lua 业务、配置表、RPC、PIE 运行态
> 官方依据：`D:\oasis-skill-plus\docs\api\class\Others\UCanvasPanelSlot.md`；知识库整理结论 `D:\知识库\和平精英绿洲起源\raw\知识\通用\来源记录\2026-08-26_UGCAskQ_MCP实测记录.md`

## 问题

用户反馈玩家席位 1-3 的控件位置与席位 4 不一致。对照图显示：席位 4 的序号贴在道具槽左上、出价贴在槽底；席位 1-3 的序号、图片和出价相对标题偏下。

## 官方确认

- `UCanvasPanelSlot.SetPosition(FVector2D)` 与 `SetSize(FVector2D)` 是 Canvas 槽位位置/尺寸写入接口。
- `ue.compile_blueprint` 官方返回 `None`，只能记录“已调用编译并保存”，不能把 `None` 写成布尔成功。
- `widget_slot` 实测只支持 `ZOrder` / `bAutoSize`，位置尺寸不能走该接口。

## 项目实测

目标资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionTestUI`

修正前相对标题偏移：

- P1：`img_dy=71.605`，`idx_dy=72.149`，`bid_dy=172.149`，`btn_dy=51.605`
- P2：`img_dy=53.388`，`idx_dy=53.932`，`bid_dy=153.932`，`btn_dy=33.388`
- P3：`img_dy=53.389`，`idx_dy=53.933`，`bid_dy=153.933`，`btn_dy=33.389`
- P4：`img_dy=23.456`，`idx_dy=24.0`，`bid_dy=124.0`，`btn_dy=3.456`

第一次错误写入：直接给 `LayoutData.Offsets.Top` 赋值，以及用 `unreal_engine.structs.Vector2D` 构造参数，导致 P1-P3 共 60 个槽位控件 `GetPosition=(0,0)`。P4 未被改动。

纠正写入：使用 `from unreal_engine import FVector2D`，对 P1-P3 的 `RoundHistoryImage / RoundIndexText / RoundHistoryBidText / RoundHistoryButton` 调用 `Slot.SetPosition` 与 `Slot.SetSize`，按 P4 同行控件复制 X/尺寸，并把 Y 设为 `titleY + P4相对标题偏移`。P4 标题与 P4 槽位保持不变。

最终回读：

- P1 标题 `y=192.0`，R1 图片 `(43.852,215.456,88.178,60.062)`
- P2 标题 `y=378.167`，R1 图片 `(43.852,401.623,88.178,60.062)`
- P3 标题 `y=546.117`，R1 图片 `(43.852,569.573,88.178,60.062)`
- P4 标题 `y=744.0`，R1 图片 `(43.852,767.456,88.178,60.062)`
- 四席相对偏移全部为 `img_dy=23.456`、`idx_dy=24.0`、`bid_dy=124.0`、`btn_dy=3.456`
- 20 组槽位相对 P4 几何 `mismatch_count=0`

MCP 计划：`plan_16779639_08df86d4`。写入前备份：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\_Backup\2026-09-03_AuctionTestUI_Seat123AlignToP4\AuctionTestUI_before_Seat123AlignToP4.uasset`

截图：

`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing\Screenshots\20260903_AuctionTestUI_Seat123AlignToP4.png`

FlaUI 捕获唯一窗口 `ShadowTrackerExtraUGCEditor` PID `15852`，PNG `1936x1056`、`858785` 字节校验通过。设计态可见 P1-P4 序号贴槽顶、出价贴槽底，相对关系一致。该截图是编辑器设计态证据，不是 PIE 运行证据。

## 经验归纳

绿洲 Python 中必须使用 `unreal_engine.FVector2D` / `from unreal_engine import FVector2D`。`unreal_engine.structs.Vector2D` 虽能 import，但不能作为 `CanvasPanelSlot.SetPosition` 的有效参数。

后续席位3绿框红框纠正见 [2026-09-03_AuctionTestUI_席位3绿框红框对齐](./2026-09-03_AuctionTestUI_席位3绿框红框对齐.md)。

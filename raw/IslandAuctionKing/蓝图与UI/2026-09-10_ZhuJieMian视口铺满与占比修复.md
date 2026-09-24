# 2026-09-10 ZhuJieMian 视口铺满与占比修复

> 类型：项目证据
> 主题：ZhuJieMian 运行时不再锁成 1920x1080 小卡片，改为四向拉伸铺满视口
> 适用范围：IslandAuctionKing，`Script/Function/AuctionHubUIService.lua`
> 证据状态：项目实测日志 + 官方 API 确认；本轮未启动 PIE
> 来源：用户 PIE 截图窄窗裁切 / 宽窗露 3D / 编辑器占比对照；客户端 LuaLog `dkck7pgf7nuy5b`
> 更新时间：2026-09-10
> 关联主题：UUserWidget.AddToViewport、SetAnchorsInViewport、SetOffsetsInViewport、SetRenderScale、UWidgetLayoutLibrary.GetViewportSize
> 排除范围：未再包裹 ScaleBox/SizeBox；未改 ZhuJieMian 里层点锚点；未改三个选择层
> 官方依据：[UUserWidget](../../../docs/api/class/Others/UUserWidget.md)、[UWidget.SetRenderScale](../../../docs/api/class/Others/UWidget.md)、[UWidgetLayoutLibrary.GetViewportSize](../../../docs/api/class/Others/UWidgetLayoutLibrary.md)、[UGCWidgetManagerSystem.GetViewportSize](../../../docs/api/class/和平全局接口/UI 界面/UGCWidgetManagerSystem.md)

## 写入前状态

用户三张对照：

1. 窄 PIE：右上金币和会场框被裁出窗口。
2. 宽 PIE：大厅四周露出 3D 场景，控件相对编辑器更小。
3. 编辑器 1920x1080：HUD 铺满白底舞台，会场框在金币正下方。

项目实测日志（`2026.09.10-16.05.36_client__dkck7pgf7nuy5b_1.log`）：

```text
【AuctionHubUIService+ReadViewportSize】分支 UGCWidgetManagerSystem不可用 ok=true value=ud_struct[Vector2D ...]
【AuctionHubUIService+ReadViewportSize】分支 PlayerController width=1280 height=720
【AuctionHubUIService+ApplyViewportFit】关键数据 design=1920x1080 view=1280x720 scale=0.66666666666667 pos=0.0,0.0
```

官方确认：`UUserWidget.AddToViewport` “fills the entire screen, unless SetDesiredSizeInViewport is called to explicitly set the size.” 上一轮把大厅锁成 1920x1080 再 `SetRenderScale(0.67)`，所以窗口一大就变成小卡片。`UGCWidgetManagerSystem.GetViewportSize` 返回 userdata，旧代码只认 table，于是落到 PlayerController 的 1280x720。

社区帖 2186 建议 Wiki 的 ScaleBox+SizeBox。项目实测把 ScaleBox 当 ZhuJieMian 根会撑破设计器，本轮不走蓝图包裹。

## 修改

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_ZhuJieMianViewportFill\AuctionHubUIService_before.lua`

1. `ParseViewportSizeValue` 同时解析 table 与 userdata 的 `X/Y`。
2. `ReadViewportSize` 顺序：`UGCWidgetManagerSystem.GetViewportSize` → `UWidgetLayoutLibrary.GetViewportSize(widget)` → `PlayerController:GetViewportSize`。
3. `ApplyViewportFit` 改为四向拉伸铺满：
   - `SetAnchorsInViewport(Min=0,0 Max=1,1)`
   - `SetOffsetsInViewport(0,0,0,0)`
   - `SetAlignmentInViewport(0,0)`
   - `SetRenderScale(1,1)`
   - `SetPositionInViewport(0,0)`
   - 不再调用 `SetDesiredSizeInViewport(1920,1080)`
4. `CreateAndShow` 与 `Refresh` 都会调用；同一 `fitKey` 不重复写。

Lua 平衡检查：`AuctionHubUIService.lua depth 0`。

## 验证

本轮未启动 PIE。需要重新调试 PIE，拉宽/拉窄窗口对照编辑器占比。

预估成功日志：

```lua
ugcprint("【AuctionHubUIService+ApplyViewportFit】入口 ... source=CreateAndShow")
ugcprint("【AuctionHubUIService+ReadViewportSize】分支 UGCWidgetManagerSystem width=... height=... rawType=userdata")
ugcprint("【AuctionHubUIService+ApplyViewportFit】关键数据 mode=FillViewport view=...x... sizeSource=UGCWidgetManagerSystem fitKey=...")
ugcprint("【AuctionHubUIService+ApplyViewportFit】出口 success=true")
```

若仍走 PlayerController 的 1280x720，但 `mode=FillViewport` 且 `SetRenderScale=1`，大厅仍应铺满当前视口，不再缩成 0.67 小卡片。

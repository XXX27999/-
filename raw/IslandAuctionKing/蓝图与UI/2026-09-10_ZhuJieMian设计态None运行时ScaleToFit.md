# 2026-09-10 ZhuJieMian 设计态 Stretch=None 运行时 ScaleToFit

> 类型：项目证据
> 主题：ScaleToFill 把 1920 HUD 放大裁切；设计态改 None，PIE 对根 ScaleBox SetStretch(ScaleToFit)
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian` 与 `AuctionHubUIService.ApplyViewportFit`
> 证据状态：项目实测；UGCAskQ MCP 写入与独立回读通过；Lua 平衡检查通过；本轮未启动 PIE
> 来源：用户设计器截图 `codex-clipboard-7c72e4e7`；上一轮 ScaleToFill 包裹
> 更新时间：2026-09-10
> 关联主题：UScaleBox.SetStretch、EStretch.None、EStretch.ScaleToFit、UUserWidget.WidgetTree
> 排除范围：未撤回 ScaleBox 根；未改里层点锚点；未再使用 ScaleToFill
> 官方依据：[UScaleBox.SetStretch](../../../docs/api/class/Others/UScaleBox.md)、[EStretch](../../../docs/api/cppenum/E/ES/EStretch.md)、[UUserWidget.WidgetTree](../../../docs/api/class/Others/UUserWidget.md)

## 写入前状态

用户设计器截图：`ScaleToFill(5)` 把 1920 舞台放大铺满当前预览区，顶栏左侧、会场框右侧、底栏都被裁出白框。左下状态是 `1855 x 1410`。

独立回读写入前：根 `CanvasPanel_0_Wrapper_Wrapper` ScaleBox `Stretch=5` / `StretchPc=5`。

项目实测：设计器预览区小于或宽高比不等于 16:9 时，ScaleToFill 按较大边放大，较小边被裁。这不是点锚点漂了。

## MCP / Lua

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_ZhuJieMianStretchNone\`

1. 蓝图：根 ScaleBox `Stretch=0` / `StretchPc=0` / `UsePcParams=False`。SizeBox 仍 1920×1080。里层点锚点未改。
   - plan_id：`plan_16805313_98564093`
   - 事务：`WriteZhuJieMianStretchNone`
   - 独立回读：`VerifyZhuJieMianStretchNoneIndependent`，`Stretch=0`，头像框仍 `(0,1) 47,-172.57`，GoldValueText 仍 `(1,0) -250,36`
2. Lua：`ApplyViewportFit` 读 `widget.WidgetTree.RootWidget`，失败再 `GetWidgetFromName("CanvasPanel_0_Wrapper_Wrapper")`，对根 ScaleBox `SetStretch(2)` / `StretchPc=2`。视口仍铺满，`SetRenderScale(1,1)`，不再二次缩小。
   - Lua 平衡：`AuctionHubUIService.lua depth 0`

## 验证

- 已打开的「编辑 ZhuJieMian」页签必须关掉再开，否则仍显示 ScaleToFill 裁切。
- 生效：重新调试 PIE。设计器应看到完整 1920 舞台；PIE 由根 ScaleBox ScaleToFit 等比适配，非 16:9 会留边，不再裁切顶栏和会场。

预估成功日志：

```lua
ugcprint("【AuctionHubUIService+ApplyViewportFit】分支 WidgetTree.RootWidget class=...")
ugcprint("【AuctionHubUIService+ApplyViewportFit】关键数据 mode=ScaleToFit view=...x... scaleBox=...")
ugcprint("【AuctionHubUIService+ApplyViewportFit】出口 success=true")
```

## 待查证

- 运行时 `widget.WidgetTree.RootWidget` 在绿洲 Lua 里是否始终可写。若日志出现 `按名取缩放框 found=false` 且没有 `SetStretch`，PIE 会保持设计态 None，大厅不再放大。
- ScaleToFit 在超宽屏会留左右黑边。若用户要铺满无黑边，再评估 Fill，不能 silently 改回 ScaleToFill。

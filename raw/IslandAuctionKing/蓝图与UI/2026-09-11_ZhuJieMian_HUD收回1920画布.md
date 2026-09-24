# 2026-09-11 ZhuJieMian HUD 收回 1920 画布

> 类型：项目证据
> 主题：设计器里 1920 SizeBox 缩成中间虚线框，贴边 HUD 画到更大白边上；给 SizeBox/Canvas 开 ClipToBoundsAlways
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
> 证据状态：项目实测；UGCAskQ MCP 写入与独立回读通过；本轮未启动 PIE
> 来源：用户设计器截图 `codex-clipboard-f6c3f242`；上一轮 Stretch=None
> 更新时间：2026-09-11
> 关联主题：UWidget.SetClipping、EWidgetClipping.ClipToBoundsAlways、USizeBox
> 排除范围：未改里层点锚点；未改运行时 ScaleToFit；未撤回 ScaleBox 根
> 官方依据：[UWidget.SetClipping](../../../docs/api/class/Others/UWidget.md)、[EWidgetClipping](../../../docs/api/cppenum/E/EW/EWidgetClipping.md)

## 写入前状态

用户 1920×1080 设计器截图：中间虚线框是 SizeBox 1920 舞台，金币、会场、底栏、顶栏都在框外更大的白边上。

独立回读：

| 层 | Stretch / Size | Clipping | 对齐 |
| --- | --- | --- | --- |
| 根 ScaleBox | Stretch=0 | 0 Inherit | - |
| SizeBox | 1920×1080 | 0 Inherit | ScaleBoxSlot 2/2 居中 |
| CanvasPanel_0 | - | 0 Inherit | SizeBoxSlot 0/0 |

贴边件仍有负 Offsets：顶部UI `44,-212`，金币UI `-424,-56`，玩家名称 `-235`。`Stretch=None` 时设计器按包围盒算 DesiredSize，负偏移把白边撑出 1920，虚线框停在中间。

## MCP

写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260911_ZhuJieMianInsideCanvas\ZhuJieMian_before.uasset`

- plan_id：`plan_16779251_24e9a52b`
- 事务：`WriteZhuJieMianInsideCanvas`
- 独立回读：`VerifyZhuJieMianInsideCanvasIndependent`

写入：

1. SizeBox / CanvasPanel_0 `SetClipping(3)` ClipToBoundsAlways
2. SizeBox ScaleBoxSlot 对齐改为 Fill `0/0`，铺满 ScaleBox
3. 根 Stretch 保持 None；SizeBox 仍 1920×1080
4. 里层点锚点未改

独立回读后：SizeBox `clip=3` 对齐 `0/0`；Canvas `clip=3`；头像框仍 `(0,1) 47,-172.57`，GoldValueText 仍 `(1,0) -250,36`。

## 验证

- 已打开的「编辑 ZhuJieMian」页签必须关掉再开。
- 生效：重新打开设计器。1920 白底应与虚线舞台重合，贴边 HUD 不再画到框外。PIE 仍由 `ApplyViewportFit` 对根 ScaleBox `SetStretch(2)`。
- 顶部UI 贴图本身比可见页签条高（Top=-212），硬裁剪后透明边会被切掉，可见页签应仍在画布内。

## 待查证

- 设计器是否仍按未裁剪包围盒画外框。若关页签后白边还在，再评估把顶部UI/金币UI/名称底图收到 1920 内，而不是继续加裁剪。

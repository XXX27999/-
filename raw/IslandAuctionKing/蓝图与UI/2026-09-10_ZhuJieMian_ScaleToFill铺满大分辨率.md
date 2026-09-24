# 2026-09-10 ZhuJieMian ScaleToFill 铺满大分辨率

> 类型：项目证据
> 主题：ZhuJieMian 根改为 ScaleBox+SizeBox 1920x1080，Stretch=ScaleToFill(5)，大分辨率不再把 1920 布局缩在左上角
> 适用范围：IslandAuctionKing，`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
> 证据状态：项目实测；UGCAskQ MCP 写入与独立回读通过；本轮未启动 PIE
> 来源：用户设计器多分辨率对照截图 `codex-clipboard-a8259120` / `2d852d82`；对照 `AuctionTestUI` 根结构
> 更新时间：2026-09-10
> 关联主题：UScaleBox.SetStretch、EStretch.ScaleToFill、USizeBox.WidthOverride、widget_wrap
> 排除范围：未改里层点锚点；未改三个选择层；未把 ScaleToFit 写回
> 官方依据：[UScaleBox](../../../docs/api/class/Others/UScaleBox.md)、[EStretch](../../../docs/api/cppenum/E/ES/EStretch.md)、[USizeBox](../../../docs/api/class/Others/USizeBox.md)、[20269_UI自适应屏幕](../../../docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md)

## 写入前状态

用户两张设计器多分辨率对照：白色虚线框是 1920 舞台，叠在 `2560x1080` / `3840x2160` 蓝块左上角，整页 HUD 看起来很小。

独立只读回读：

| 资产 | 根 | 缩放 |
| --- | --- | --- |
| ZhuJieMian | `CanvasPanel_0` | 无 ScaleBox，DesiredSize 跟 1920 点锚点走 |
| AuctionTestUI | `ScaleBox_0` | Stretch=2/ScaleToFit，SizeBox 1920x1080，SizeBoxSlot 对齐 2/2 |

官方 `AddToViewport` 会铺满。裸画布的 DesiredSize 仍是 1920，设计器对照图按 1:1 像素叠大屏，所以 1920 盒子停在 3840 的角落。上一轮 Lua `FillViewport` 不能改设计器对照。

上一轮用 ScaleToFit 当根时，设计器预览区小于 1920 会再缩一次。本轮改 `ScaleToFill(5)`：按较大边放大铺满，而不是整页缩小放进预览。

## MCP 状态

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`
- plan_id：`plan_16803752_9a40e533`
- 事务：`WrapZhuJieMianScaleToFill`
- 独立回读：`VerifyZhuJieMianScaleToFillIndependent`，`has_mutation=false`
- 写前备份：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260910_ZhuJieMianScaleToFill\ZhuJieMian_before.uasset`

## 写入结果

树：

`ScaleBox`（根，Stretch=5/ScaleToFill，StretchPc=5，UsePcParams=False）
→ `SizeBox` 1920×1080（ScaleBoxSlot 对齐 2/2）
→ 原 `CanvasPanel_0`（SizeBoxSlot 对齐 0/0，里层点锚点未改）

独立回读：

| 控件 | 结果 |
| --- | --- |
| 根 | `CanvasPanel_0_Wrapper_Wrapper` ScaleBox Stretch=5 StretchPc=5 |
| SizeBox | 1920x1080，两个 Override=True，对齐 2/2 |
| 头像框 | (0,1) 47,-172.57 / 153.57x154.29 |
| GoldValueText | (1,0) -250,36 / 200x44 |
| 保底金 | (1,1) -163,-136.67 / 102.5x100.83 |
| OpenHouseButton | (1,0) -418.56,103.7 / 338.74x203.33 |

`AuctionHubUIService.ApplyViewportFit` 仍是 `SetRenderScale(1,1)` 铺满视口，不再二次缩小。运行时由根 ScaleBox 把 1920 舞台放大铺满。

## 验证

- MCP `success=true`，`used_count=1`，独立回读无写入。
- 已打开的「编辑 ZhuJieMian」页签必须关掉再开。
- 生效：重新调试 PIE；设计器在「屏幕尺寸」里切到 2560×1080 / 3840×2160 看是否铺满。
- 多分辨率对照蓝块按控件 DesiredSize 叠图。根 ScaleBox 的 DesiredSize 仍可能是 1920，对照图里的小白框不一定消失；以切换屏幕尺寸和 PIE 为准。

## 待查证

- ScaleToFill 在非 16:9 上会裁切上下或左右。若用户要完整看见 1920 舞台、接受黑边，再改回 ScaleToFit，不能 silently 改。
- 设计器 1920 舞台若再次缩成一团，再把设计态 Stretch 改成 None，PIE 保持 ScaleToFill。

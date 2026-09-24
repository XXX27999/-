# 绿洲 UMG 设计态缩放裁剪与白块排错

> 类型：概念索引
> 来源：[绿洲 UMG 设计态缩放裁剪与白块排错正文](../../raw/知识/通用/UI与交互/绿洲UMG设计态缩放裁剪与白块排错.md)、[2026-09-11 项目记录 UI 编辑经验提炼](../../raw/知识/通用/来源记录/2026-09-11_项目记录UI编辑经验提炼.md)、[2026-09-15 AuctionGuaranteeGoldUI 画刷 ResourceObject 与 Slot 对齐修复](../../raw/IslandAuctionKing/蓝图与UI/2026-09-15_AuctionGuaranteeGoldUI_画刷ResourceObject与Slot对齐修复.md)
> 官方依据：[20269_UI自适应屏幕](../../raw/docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md)、[UScaleBox](../../raw/docs/api/class/Others/UScaleBox.md)、[UWidget](../../raw/docs/api/class/Others/UWidget.md)、[EStretch](../../raw/docs/api/cppenum/E/ES/EStretch.md)、[EWidgetClipping](../../raw/docs/api/cppenum/E/EW/EWidgetClipping.md)
> 最近更新：2026-09-15

## 索引摘要

本页只提供导航。设计态用 Stretch=None 看完整 1920 舞台，PIE 再 ScaleToFit；切图按原像素居中，不要硬拉满；空画刷和复制残留会在设计器画白块；MCP 写完必须关页签再开。

设计舞台包裹层还有两个易漏点：`ScaleToFit(2)` 取 `min(sx,sy)`、`ScaleToFill(5)` 取 `max(sx,sy)` 且裁较长边（等比，非拉伸）；`SizeBox.WidthOverride/HeightOverride` 必须连 `bOverride_*` 一起写，漏开关则运行时不生效、内容被放大出界。运行时缩放可用「实测间距 ÷ 设计间距」取证。

- **Raw 正文**：[绿洲 UMG 设计态缩放裁剪与白块排错正文](../../raw/知识/通用/UI与交互/绿洲UMG设计态缩放裁剪与白块排错.md)
- **相关页面**：[绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)、[绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)、[绿洲 UMG 文字、透明点击层与贴边锚点摆放](./绿洲UMG文字透明点击层与贴边锚点摆放.md)、[绿洲编辑器 UI 截图与验证](./绿洲编辑器UI截图与验证.md)

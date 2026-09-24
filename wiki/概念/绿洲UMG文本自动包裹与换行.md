# 绿洲 UMG 文本自动包裹与换行

> 类型：概念索引
> 来源：[绿洲 UMG 文本自动包裹与换行正文](../../raw/知识/通用/UI与交互/绿洲UMG文本自动包裹与换行.md)、[2026-09-10 UI 文本自动包裹](../../raw/知识/通用/来源记录/2026-09-10_UI文本自动包裹.md)
> 官方依据：[UTextLayoutWidget](../../raw/docs/api/class/Others/UTextLayoutWidget.md)、[UTextBlock](../../raw/docs/api/class/Others/UTextBlock.md)、[ETextWrappingPolicy](../../raw/docs/api/cppenum/E/ET/ETextWrappingPolicy.md)
> 最近更新：2026-09-10

## 索引摘要

本页只提供导航。长文本要换行必须打开 `AutoWrapText`（编辑器：自动包裹文本），并给文本框确定宽度；默认关闭时文本单行画出框。
MCP 走 `ue_py` 直接赋布尔属性，没有专用 setter；`widget_set_property` 未实测该字段。

- **Raw 正文**：[绿洲 UMG 文本自动包裹与换行正文](../../raw/知识/通用/UI与交互/绿洲UMG文本自动包裹与换行.md)
- **相关页面**：[绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)、[MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)、[绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)

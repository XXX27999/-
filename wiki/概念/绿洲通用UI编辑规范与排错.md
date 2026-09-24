# 绿洲通用 UI 编辑规范与排错

> 类型：概念索引
> 来源：[通用 UI 编辑规范与排错正文](../../raw/知识/通用/UI与交互/绿洲通用UI编辑规范与排错.md)、[MCP UI 编辑与高保真还原知识库](../../raw/知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)、[2026-08-28 图鉴 UI 蓝图 MCP 高保真迭代](../../raw/知识/通用/来源记录/2026-08-28_图鉴UI蓝图MCP高保真迭代.md)
> 官方 API 依据：[UWidget](../../raw/docs/api/class/Others/UWidget.md)、[UTextBlock](../../raw/docs/api/class/Others/UTextBlock.md)、[UImage](../../raw/docs/api/class/Others/UImage.md)、[UBorder](../../raw/docs/api/class/Others/UBorder.md)、[UButton](../../raw/docs/api/class/Others/UButton.md)、[UScrollBox](../../raw/docs/api/class/Others/UScrollBox.md)、[UScaleBox](../../raw/docs/api/class/Others/UScaleBox.md)、[USizeBox](../../raw/docs/api/class/Others/USizeBox.md)
> 最近迁移：2026-08-28

## 索引摘要

本页只提供导航；控件配置、MCP 操作步骤、已验证案例、FAQ 与待验证项均位于 Raw 内容层。

- **Raw 正文**：[绿洲通用 UI 编辑规范与排错正文](../../raw/知识/通用/UI与交互/绿洲通用UI编辑规范与排错.md)
- **画布 ZOrder 与裁切实测（2026-09-22）**：[本引擎 UMG 画布 ZOrder 与裁切实测](../../raw/知识/通用/UI与交互/2026-09-22_本引擎UMG画布ZOrder与裁切实测.md) —— `SetZOrder/GetZOrder` 完全生效且默认参与排序；本引擎 **无** `bExplicitCanvasChildZOrder`；`EWidgetClipping` 五值语义与排查顺序。
- **内容层目录**：[UI 与交互内容目录](../../raw/知识/通用/UI与交互/000_目录.md)
- **相关页面**：[MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)、[蓝图与 MCP 写入流程](./蓝图与MCP写入流程.md)、[PIE 调试与热更新边界](./PIE调试与热更新边界.md)、[绿洲 UMG 文字、透明点击层与贴边锚点摆放](./绿洲UMG文字透明点击层与贴边锚点摆放.md)、[绿洲 UMG 文本自动包裹与换行](./绿洲UMG文本自动包裹与换行.md)、[绿洲 UMG 设计态缩放裁剪与白块排错](./绿洲UMG设计态缩放裁剪与白块排错.md)、[绿洲 UI 动效与 Tween](./绿洲UI动效与Tween.md)

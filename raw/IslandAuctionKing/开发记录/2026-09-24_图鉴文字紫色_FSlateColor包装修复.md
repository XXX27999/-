# 2026-09-24 图鉴文字紫色：TextBlock 颜色入参必须为 FSlateColor

- 类型：项目实测 + 官方 API 依据
- 主题：`CollectibleCodexUIService.lua` 图鉴文本颜色统一紫色/品红；`UTextBlock.SetColorAndOpacity` 入参类型
- 适用范围：IslandAuctionKing 藏品图鉴主界面与图鉴条目
- 证据状态：官方确认（API 参数类型）+ 项目代码核对 + 蓝图 CDO 只读回读
- 来源：
  - `D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UTextBlock.md` 第 40 行：`SetColorAndOpacity(InColorAndOpacity: FSlateColor)`
  - `D:\知识库\和平精英绿洲起源\raw\知识\通用\UI与交互\2026-09-16_文本与图片SetColorAndOpacity入参类型差异.md`
  - 工程文件：`Script/Function/CollectibleCodexUIService.lua`
  - UGCAskQ MCP 只读回读：`CollectibleCodexUI_C` / `CollectibleCodexItemUI_C` 的 `ForegroundColor`
- 更新时间：2026-09-24
- 关联主题：[2026-09-24_结算仓库藏品点击图鉴](./2026-09-24_结算仓库藏品点击图鉴.md)、[文本与图片 SetColorAndOpacity 入参类型差异](../../知识/通用/UI与交互/2026-09-16_文本与图片SetColorAndOpacity入参类型差异.md)
- 排除范围：图片控件 `UImage.SetColorAndOpacity`（其入参为 `FLinearColor`，本页不改变该用法）；蓝图设计态文字颜色编辑
- 官方依据：有（`UTextBlock.SetColorAndOpacity` 参数为 `FSlateColor`）

## 一、现象

图鉴主界面与图鉴条目中的文字整体显示为紫色/品红，包括标题、进度、详情字段、藏品名称和收集状态。代码里写入的是金色、白色、灰色或绿色，并非紫色。

## 二、根因

`CollectibleCodexUIService.lua` 中 10 处 TextBlock 颜色写入直接把 `FLinearColor` 形状的表传给 `SetColorAndOpacity`：

```lua
textBlock:SetColorAndOpacity({R = 1.0, G = 0.7, B = 0.28, A = 1.0})
```

`UTextBlock.SetColorAndOpacity` 的官方入参类型是 `FSlateColor`，直接传 `{R,G,B,A}` 时：

- slua 不抛异常，`pcall` 返回成功；
- 颜色解析失败后引擎回退到默认前景色；
- 本项目两个图鉴 Widget 的默认 `ForegroundColor` 均为 `ColorUseRule=2`、`SpecifiedColor=(1.0, 0.0, 1.0, 1.0)`，即品红占位色；
- 最终视觉表现就是“文字都是紫色”，且日志没有错误。

## 三、修复

在 `CollectibleCodexUIService.lua` 增加统一封装 `ApplyCodexTextColor(textWidget, color, context)`：

```lua
local linearColor = color or {R = 1.0, G = 1.0, B = 1.0, A = 1.0}
local slateColor = {SpecifiedColor = linearColor}
local colorOK, colorError = pcall(textWidget.SetColorAndOpacity, textWidget, slateColor)
```

并替换以下文本颜色写入：

- `TitleText`
- `ProgressText`
- `DetailTitleText`
- `DetailTypeQualityText`
- `DetailShapeText`
- `DetailValueText`
- `DetailIncomeText`
- `DetailStateText`
- `ItemNameText`
- `CollectionStateText`

图片 `ItemImage` 的 `SetColorAndOpacity` 保持 `FLinearColor` 写法，未做改动。

## 四、验证

- `luaparser` 解析 `CollectibleCodexUIService.lua` 通过；
- `git diff --check` 通过；
- 文件 UTF-8 无 BOM；
- `ApplyCodexTextColor` 调用点共 11 处（1 处定义引用统计口径内，含封装内部）；
- 工程内未新增临时 `.py` / `.pyc`；
- UGCAskQ MCP 只读回读确认两个 Widget 的默认前景色为品红，但所有关键 TextBlock 自身使用指定颜色规则，故不写 `.uasset`，只修 Lua。

**未启动 PIE**：本轮只改普通 Lua 函数体，可按热更新路径验证。

## 五、待观察

若热更新后仍有个别文本发紫，说明该文本没有走 `ApplyCodexTextColor`，需要单独补颜色写入；此时再考虑把两个 Widget 的默认 `ForegroundColor` 从品红改为白色，并必须走 UGCAskQ MCP 写入与回读。

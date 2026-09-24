# 绿洲 UMG 文本自动包裹与换行

> 类型：通用知识
> 主题：UI / TextBlock Wrapping / AutoWrapText
> 适用范围：全局通用（绿洲 UMG 文本控件）
> 证据状态：官方确认 + 编辑器面板实测归纳
> 来源：[UTextLayoutWidget](../../../docs/api/class/Others/UTextLayoutWidget.md)、[UTextBlock](../../../docs/api/class/Others/UTextBlock.md)、[ETextWrappingPolicy](../../../docs/api/cppenum/E/ET/ETextWrappingPolicy.md)、[2026-09-10 UI 文本自动包裹](../来源记录/2026-09-10_UI文本自动包裹.md)
> 更新时间：2026-09-10（增补：MCP 可写 AutoWrapText 属性，但无专用 setter，且 widget_set_property 未实测该字段）
> 关联主题：UTextLayoutWidget、UTextBlock、WrapTextAt、WrappingPolicy、AutoEllipsisText、绿洲通用UI编辑规范与排错、MCP-UI编辑与高保真还原知识库
> 排除范围：不覆盖字体字号/描边、网页预览 CSS 折行细节、玩法文案内容；不把 IslandAuctionKing 的控件名和像素当成所有项目默认值
> 官方依据：`D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UTextLayoutWidget.md`；`D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UTextBlock.md`；`D:\知识库\和平精英绿洲起源\raw\docs\api\cppenum\E\ET\ETextWrappingPolicy.md`。官方 Wiki 检索「自动包裹文本」「WrapText」无命中，属知识库未覆盖。

## 来源与官方依据

| 证据 | 状态 | 结论边界 |
| --- | --- | --- |
| `UTextLayoutWidget.AutoWrapText` | 官方确认 | `bool`。官方说明：True if we're wrapping text automatically based on the computed horizontal space for this widget. |
| `UTextLayoutWidget.WrapTextAt` | 官方确认 | `float`。文本长度超过该宽度时换行；值为 0 或负数时不按该宽度换行。 |
| `UTextLayoutWidget.WrappingPolicy` | 官方确认 | 类型为 `ETextWrappingPolicy`。 |
| `ETextWrappingPolicy` | 官方确认 | `DefaultWrapping=0`，`AllowPerCharacterWrapping=1`。官方页无中文说明。 |
| `UTextBlock` 继承 `UTextLayoutWidget` | 官方确认 | 静态文本框使用上述换行字段。 |
| `UTextBlock.SetWrapTextAt` | 官方确认 | 运行时可写 `WrapTextAt`。参数 `InWrapTextAt: float`。 |
| `SetAutoWrapText` | 知识库未覆盖 | 本地官方 API 无此函数。不能写成 Lua 标准接口。 |
| 编辑器细节面板 Wrapping | 编辑器面板实测 | 中文名「自动包裹文本」对应 `AutoWrapText`。官方 Wiki 未覆盖该中文标签。 |
| UGCAskQ MCP 写入路径 | 经验归纳 | 走 `ue_py` 直接赋 `txt.AutoWrapText = True`，再 `compile_blueprint` + `save_package`。无 `SetAutoWrapText`。`widget_set_property` 仅实测 `Text`/`ToolTipText`/`Visibility`，未回读 `AutoWrapText`。 |

## 核心结论

需要完整显示、并可能超过文本框宽度的文案，必须打开 `AutoWrapText`（编辑器中文：自动包裹文本）。该开关默认关闭时，文本按单行排版，不会按控件宽度换行，会画出文本框。

三条必须同时成立：

1. **打开自动包裹**：`AutoWrapText = true`。官方语义是按该控件已计算出的水平空间自动换行。
2. **给文本框确定宽度**：Canvas Slot 的 `Size.X`、父容器宽度或 `WrapTextAt > 0` 必须有一个有效水平边界。没有宽度约束时，打开开关也不会出现可见换行。
3. **不要和省略号混用，除非明确要截断**：单行省略走 `AutoEllipsisText`；多行省略走 `MutiEllipsisText` + `MutiEllipsisLine`。完整展示长文案时关闭省略号。

`WrapTextAt` 与 `AutoWrapText` 不是同一个开关：

- `AutoWrapText=true`：按控件计算宽度换行。
- `WrapTextAt>0`：按指定宽度换行。
- `WrapTextAt<=0`：官方说明为不按该宽度换行。编辑器「包裹文本处」显示 `0.0` 时，必须依赖 `AutoWrapText` 和控件宽度，不能指望 `0.0` 自己换行。

长串连续英文、数字、无空格路径撑破容器时，还要把 `WrappingPolicy` 设为 `AllowPerCharacterWrapping(1)`。`DefaultWrapping(0)` 只在空格/CJK 等默认可断点处换行。

## 可执行步骤

### 编辑器手工设置

1. 打开 UI 蓝图，选中目标 `TextBlock`。
2. 细节面板找到 **Wrapping** 分组。
3. 勾选 **自动包裹文本**（`AutoWrapText`）。
4. **包裹文本处**（`WrapTextAt`）保持 `0.0` 时，确认该控件 Slot 宽度已经是最终显示宽度。
5. **包裹规则** 默认用 **默认包裹**（`DefaultWrapping`）；长串英文/数字改为允许按字符换行。
6. 完整展示时关闭 **自动省略文本**、**多省略号文本**。
7. 保存并编译蓝图。该属性属于蓝图控件，必须重新调试 PIE，不能只热更新 Lua。

### MCP 写入

可以走 MCP，但没有专用函数。官方字段是 `UTextLayoutWidget.AutoWrapText`（`bool`），本地官方 API 和 UGCAskQ 都没有 `SetAutoWrapText`。

| 写法 | 证据状态 | 是否采用 |
| --- | --- | --- |
| `txt.AutoWrapText = True` 后 compile/save，再重新 `load_object` 读 `txt.AutoWrapText` | 经验归纳（与 `bIsVariable` 等布尔字段同一 Python 属性写入模式） | 采用 |
| `ue.widget_set_property(wbp, "Name", "AutoWrapText", True)` | 知识库未覆盖 | 不作为已验证入口。该 API 只实锤 `Text`/`ToolTipText`/`Visibility` |
| Lua/`ue_py` 调 `SetAutoWrapText` | 知识库未覆盖 | 禁止。官方 API 无此函数 |
| 只看 `widget_inspect` 树字符串 | 项目实测：inspect 含类型/名称/父容器/Pos/Size | 不够。必须直接读 `AutoWrapText`/`WrapTextAt`/`WrappingPolicy` |

```python
txt = [c for c in wbp.WidgetTree.AllWidgets if c.get_name() == "DescText"][0]
txt.AutoWrapText = True
txt.WrapTextAt = 0.0
txt.WrappingPolicy = 0
txt.AutoEllipsisText = False
txt.MutiEllipsisText = False
ue.compile_blueprint(wbp)
wbp.save_package()
ue.log(ue.widget_inspect(wbp, "DescText"))
```

长串英文/数字改为：

```python
txt.WrappingPolicy = 1  # AllowPerCharacterWrapping
```

写入后必须回读 `AutoWrapText`、`WrapTextAt`、`WrappingPolicy`。MCP 写入 API 成功也返回 `None`，不能凭返回值声称已换行。

### Lua 运行时

本地官方 API 确认 `UTextBlock:SetWrapTextAt(InWrapTextAt)` 存在，未确认 `SetAutoWrapText`。需要运行时改换行时：

1. 优先在设计态打开 `AutoWrapText`，Lua 只 `SetText`。
2. 若必须指定折行宽度，调用 `SetWrapTextAt`，并打印入参和控件名。
3. 不要把不存在的 `SetAutoWrapText` 写进脚本。

## 常见错误

- **只改了文案，没开自动包裹**：长文本继续单行画出框。先勾选「自动包裹文本」，再检查 Slot 宽度。
- **打开自动包裹但 Slot 宽度是 Autosize 或跟随内容**：控件被文本撑开，看起来像没换行。先固定宽度，再换行。
- **靠字符串里塞 `\n` 当换行**：设计态若写成字面 `\\n` 会显示反斜杠 n。换行应交给 `AutoWrapText` 或写入真实换行符。
- **省略号和自动包裹同时开着**：结果可能是截断而不是完整换行。完整展示时关掉 `AutoEllipsisText` / `MutiEllipsisText`。
- **长 ID、路径、无空格英文仍溢出**：`WrappingPolicy` 仍是 `DefaultWrapping`。改为 `AllowPerCharacterWrapping`。
- **改完蓝图只热更新 Lua**：Wrapping 在控件资产上，必须重新 PIE。

## 相关页面

- [绿洲通用 UI 编辑规范与排错](./绿洲通用UI编辑规范与排错.md)
- [MCP-UI编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)
- [绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)
- [绿洲 UMG 文字、透明点击层与贴边锚点摆放](./绿洲UMG文字透明点击层与贴边锚点摆放.md)
- [绿洲 UI 枚举与结构体速查](./绿洲UI枚举与结构体速查.md)
- 项目证据：[AuctionCharacterSelectUI CharacterDetailText 自动包裹](../../../IslandAuctionKing/蓝图与UI/2026-09-10_AuctionCharacterSelectUI_CharacterDetailText自动包裹.md)

## 待查证

1. 官方 Wiki 无「自动包裹文本」操作页；中文面板名与 `AutoWrapText` 的对应关系来自编辑器 Wrapping 分组，不是官方 Wiki 词条。
2. `SetAutoWrapText` 在本地官方 API 中不存在。运行时能否直接写 Lua 属性 `TextBlock.AutoWrapText` 未验证。
3. `AutoWrapText=true` 且 `WrapTextAt>0` 同时生效时，以控件计算宽度还是指定宽度为准，官方未写优先级。
4. `AutoEllipsisText` / `MutiEllipsisText` / `MutiEllipsisLine` 仍无官方 ToolTip，截断与换行的互相覆盖关系需 PIE 验证。
5. `txt.AutoWrapText = True` 尚未对生产控件做 compile/save 后重新 load_object 回读。采用前必须回读该布尔值，不能只看 widget_inspect 或 API 返回 None。

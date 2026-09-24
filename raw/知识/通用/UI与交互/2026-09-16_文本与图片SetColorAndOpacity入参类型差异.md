# 文本与图片 SetColorAndOpacity 入参类型差异（文本必须传 FSlateColor）

- 类型：官方确认 + 项目实测排错
- 主题：`UTextBlock.SetColorAndOpacity` 与 `UImage/UButton.SetColorAndOpacity` 的入参类型差异；Lua 侧表构造写法；静默失败特征
- 适用范围：和平精英绿洲起源 UGC（slua 绑定层，Lua 调 UMG 接口）
- 证据状态：官方确认（API 文档参数类型）+ 项目实测（结算 UI、主界面大厅）
- 来源：
  - `D:\知识库\和平精英绿洲起源\raw\docs\api\class\Others\UTextBlock.md` 第 40 行：`SetColorAndOpacity(InColorAndOpacity: FSlateColor)`
  - `raw\docs\api\class\Others\UButton.md` 第 68 行：`SetColorAndOpacity(InColorAndOpacity: FLinearColor)`
  - `raw\docs\api\class\Others\UEditableText.md` 第 125 行：`SetColorAndOpacity(Color: FSlateColor)`
  - 项目实测：AuctionSettlementUIService（2026-09-16 金色文字）、AuctionHubUIService（2026-09-16 主界面三处白字）
- 更新时间：2026-09-16
- 关联主题：[绿洲UI枚举与结构体速查](./绿洲UI枚举与结构体速查.md)、[2026-09-15_UMG控件Lua取名可达性与配置表读取类型判定](./2026-09-15_UMG控件Lua取名可达性与配置表读取类型判定.md)
- 排除范围：蓝图侧 `ColorAndOpacity` 属性编辑（MCP 写入路径不同）；RichText/描边材质
- 官方依据：有（API 文档参数类型明确）

## 一、结论

| 控件 | 官方入参类型 | Lua 正确写法 |
| --- | --- | --- |
| `UTextBlock` | `FSlateColor` | `{ SpecifiedColor = { R = 1, G = 1, B = 1, A = 1 } }` |
| `UEditableText` | `FSlateColor` | 同上 |
| `UImage` | `FLinearColor` | `{ R = 1, G = 1, B = 1, A = 1 }` |
| `UButton` | `FLinearColor` | 同上 |

**给文本上色时，`SpecifiedColor` 才是真正的颜色字段。** 直接把 `{R,G,B,A}` 传给 TextBlock，slua 不会按 FSlateColor 解析。

## 二、最大的坑：失败是静默的

- `pcall(textBlock.SetColorAndOpacity, textBlock, {R=1,G=1,B=1,A=1})` **返回 success**（不抛异常），但颜色不生效；
- 引擎会退回默认色绘制（本项目实测表现为**粉色/品红**），
- 所以日志里**看不到任何报错**，只能靠截图/肉眼发现。上一轮主界面三处文本 `goldOK/nameOK/countdownOK=true` 全绿，实际颜色却是错的，就是这个原因。

**排错要点**：文本颜色不对时，先查入参包装，而不是查配置值或控件引用。

## 三、推荐写法（带兜底）

```lua
local linearColor = { R = r, G = g, B = b, A = a }
local slateColor  = { SpecifiedColor = linearColor }   -- FSlateColor 包装
local ok, err = pcall(textBlock.SetColorAndOpacity, textBlock, slateColor)
if not ok then
    pcall(textBlock.SetColorAndOpacity, textBlock, linearColor)  -- 兜底直传
end
```

## 四、与配置表配合

颜色分量应按功能域登记进配置表（本项目 `UIConfigTable`）：

- `UI.Hub.Gold.ColorR/G/B/A`
- `UI.Hub.PlayerName.ColorR/G/B/A`
- `UI.Hub.Countdown.ColorR/G/B/A`

取值全部为 `1` 即纯白。改色只需改表，不改代码；**但若不修 FSlateColor 包装，改表也不会生效**——这两件事必须同时确认。

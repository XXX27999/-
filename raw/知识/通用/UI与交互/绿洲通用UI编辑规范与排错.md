# 绿洲通用 UI 编辑规范与排错

> 内容层：通用 UI 编辑规范、MCP 操作流程与已验证排错经验
> 来源：[MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)、[蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)、[资源导入与路径规范](../配置与数据/资源导入与路径规范.md)、[PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)、[2026-08-28 图鉴 UI 蓝图 MCP 高保真迭代](../来源记录/2026-08-28_图鉴UI蓝图MCP高保真迭代.md)
> 官方 API 依据：[UWidget](../../../docs/api/class/Others/UWidget.md)、[UTextBlock](../../../docs/api/class/Others/UTextBlock.md)、[UImage](../../../docs/api/class/Others/UImage.md)、[UBorder](../../../docs/api/class/Others/UBorder.md)、[UButton](../../../docs/api/class/Others/UButton.md)、[UScrollBox](../../../docs/api/class/Others/UScrollBox.md)、[UCanvasPanel](../../../docs/api/class/Others/UCanvasPanel.md)、[UScaleBox](../../../docs/api/class/Others/UScaleBox.md)、[USizeBox](../../../docs/api/class/Others/USizeBox.md)、[FSlateBrush](../../../docs/api/cppstruct/F/FS/FSlateBrush.md)
> 证据边界：控件属性和 MCP 写入流程来自本地官方 API 快照与真实编辑器回读；具体项目尺寸、颜色、素材路径属于 `IslandAuctionKing` 案例，不能直接当作所有项目的默认值。

## 1. 核心概念与应用场景

- **定义/作用**：绿洲 UI 由 `UserWidget`、`WidgetTree`、Panel 控件和叶子控件组成。Panel 决定子控件的布局边界，`CanvasPanelSlot` 决定画布子控件的位置、尺寸、锚点、对齐和 ZOrder。
- **适用场景**：菜单、图鉴、筛选面板、信息卡、按钮组、滚动列表以及需要在不同屏幕尺寸下保持结构稳定的玩法 UI。
- **核心原则**：网页预览中的尺寸、颜色、层级和间距必须映射到 UMG 的具体属性；蓝图写入后必须回读控件树和布局，运行时行为必须再通过 PIE 验证。
- **控件职责**：`CanvasPanel` 适合固定设计稿布局；`ScrollBox` 负责列表滚动；`Button` 负责输入；`TextBlock` 负责文本；`Image` 负责贴图；`Border` 负责背景、边框或内容包裹；`ScaleBox`、`SizeBox` 负责尺寸约束和缩放。

## 2. 详细操作规范与流程

### 2.1 新建或检查 UI 控件树

1. 打开 UI 蓝图编辑器，在 **Designer -> Hierarchy/控件树** 中确认根节点、容器和叶子控件的父子关系。
2. 对固定布局优先建立 `CanvasPanel -> 业务控件`；对列表建立 `ScrollBox -> 内容容器 -> 条目 Widget`，子项必须通过容器的 `AddChild` 关系挂入。
3. 对需要屏幕适配的主界面采用：`CanvasPanel -> ScaleBox -> SizeBox -> CanvasPanel -> 业务控件` 的结构，并确认外层缩放和内层布局的职责没有混用。
4. 为需要被 Lua 或可视化脚本访问的控件使用稳定、唯一、英文开头的名称，并确认对应控件可被脚本引用。

### 2.2 通过 UGCAskQ MCP 修改蓝图

1. **Resolve**：使用 `ue_read` 查询编辑器上下文、蓝图能力和属性；使用 `ue_py` 的 `ue.widget_inspect` 回读目标蓝图控件树。资产路径必须使用 `/<ProjectName>/Asset/...`，不能使用 `/Game/`。
2. **备份**：写入前复制目标 `.uasset` 到 `D:\知识库\和平精英绿洲起源\备份\<ProjectName>\<YYYYMMDD>_<Theme>\`，并记录该绝对路径。禁止写入 UGC 工程。
3. **Plan**：用 `ue_plan_submit` 提交目标资产、修改属性、调用 API 和 `pre_write_snapshot: true`。
4. **Execute**：用绑定的 `plan_id` 调用 `ue_py`。位置和尺寸**不能**用 `CanvasPanelSlot.SetPosition/SetSize`（实测不可用），正确写法见 [2.5 写入 Slot 坐标尺寸](#25-写入-slot-坐标尺寸实测唯一可用写法)；`widget_slot` 只用于已验证支持的 `ZOrder`、`bAutoSize` 等字段。
5. **保存与编译**：调用 `ue.compile_blueprint`，再调用蓝图对象的 `save_package()`。
6. **回读**：重新加载蓝图，用 `ue.widget_inspect` 和布局属性回读层级、Pos、Size、Anchors、Alignment、ZOrder、Visibility、画刷和字体属性。
7. **截图**：每轮成功写入后立即用 FlaUI 截取编辑器画面，与网页基准比较；不得在未截图和未回读时连续盲改。
8. **运行验证**：蓝图、组件、事件、初始化和配置修改必须重新 PIE；普通 Lua 函数体修改才适合使用热更新。

### 2.3 手工属性面板配置路径

1. 选中 **Hierarchy -> 目标控件**。
2. 在 **Details/属性面板 -> Slot -> Canvas Panel Slot** 配置 `Position`、`Size`、`Anchors`、`Alignment`、`ZOrder` 和 `bAutoSize`。
3. 在 **Details/属性面板 -> Appearance/外观** 配置 `Visibility`、`Color and Opacity`、`Brush`、字体和阴影。
4. 对 `TextBlock` 检查字体大小、颜色、对齐、自动省略、换行和阴影；对 `Image` 检查 `Brush`；对 `Border` 检查 `Background`。
5. 保存并编译蓝图后，再通过截图检查文字是否重叠、素材是否被错误 Tint、控件是否被前后层遮挡。

### 2.4 动态刷新与脚本通信

1. 蓝图负责稳定的控件树、默认尺寸、默认画刷和可访问控件名称。
2. Lua 服务负责运行时数据绑定，例如根据 DataTable 行设置名称、图片、品质颜色、估值、收益和收集状态。
3. 动态图片流程应先判断资源是否存在，再设置 `Image.Brush` 或对应的贴图设置函数、恢复原色并切换 `Visibility`；设计态占位图不能替代运行时资源。
4. 刷新结束后输出入口、关键数据、分支结果和出口日志；加载资源或更新 UI 的关键调用使用 `pcall` 保护。
5. UI 事件绑定的具体事件节点、委托签名和端侧通信方式在本次对话中没有完整验证，见“待补充/待验证”。

### 2.5 写入 Slot 坐标尺寸（实测唯一可用写法）

`CanvasPanelSlot.SetPosition/SetSize`、`ue.widget_slot(Position/Size/Offsets/Anchors/Alignment/LayoutData)`
、`slot.set_property("LayoutData", ...)` 三种写法**全部失败或破坏数据**（后者会把值写成 0）。

唯一可靠写法是只 `set_field`、**绝不回写整个 struct**：

```python
slot = w.Slot                              # CanvasPanelSlot
ld   = slot.get_property("LayoutData")     # UScriptStruct 'AnchorData'
ofs  = ld.get_field("Offsets")             # 嵌套 UScriptStruct 'Margin'
ofs.set_field("Left",   float(x))          # Anchors 为左上对齐时：
ofs.set_field("Top",    float(y))          #   L/T = Position
ofs.set_field("Right",  float(w))          #   R/B = Size
ofs.set_field("Bottom", float(h))
# 就地生效，立即回读 slot.get_property("LayoutData") 即可验证
```

同一铁律适用于所有 UScriptStruct 字段（如 `Font.Size`）：`set_field` 后**不要**
再 `w.set_property(整个struct)`，否则值被写成 0。

### 2.6 控件平铺化：把控件从自动布局容器移到 CanvasPanel

**目标**：让每个控件都能在设计器里手动拖拽调位置和大小，不被 VBox/HBox/WrapBox 的自动布局锁死。

**流程**：

1. **先查 Lua 契约再动手**。grep 项目 `Script/` 目录，确认待处理容器名不在
   `REQUIRED_WIDGET_NAMES` 里，也没有被服务脚本引用。契约内控件（缺失会 `error` 或直接
   取不到引用）必须保留，例如 `AuctionSettlementUI` 的 `WarehouseGrid`。
2. **先备份** `.uasset`，记录 MD5。
3. **记录原坐标**：设计态下 `GetDesiredSize()` 恒返回 `(0,0)`、拿不到自动布局的计算结果，
   所以需要**先用编辑器截图 + 画布标定**（把截图里设计画布区域缩放到 1920×1080 设计坐标）
   量测控件当前实际位置，再按量测值写绝对坐标。这样平铺后视觉位置不变。
4. **换父容器**：`ue.widget_move(wbp, 控件名, "ContentCanvas")`。
5. **写绝对坐标**：接第 4 步之后立即用 2.5 的写法写 `Offsets`。
6. **恢复可见性**：`widget_move` 会把 `Visibility` 重置为 `Collapsed`，必须重新
   `ue.widget_set_property(wbp, 控件名, "Visibility", "3")`（HitTestInvisible）。
7. **清容器**：子控件搬空后，`ue.widget_remove(wbp, 容器名)` 删除纯布局容器。
   注意 `widget_unwrap` 对空容器会报 `RuntimeError: 'X' empty`，删空容器只能用 `widget_remove`。
8. **保存 + 重建预览**：`objed_save_asset` → `close_editor_for_asset` → `open_editor_for_asset`。
   （这一步还会显著释放内存，实测 9.34 GB → 5.13 GB。）
9. **截图复验**：平铺后的截图应与平铺前一致（位置未变）；若整屏变暗（mean 约 29、
   非黑像素约 58%）说明窗口未重绘，隔一次再截，正常为 mean 约 63、非黑约 91%。

**哪些容器应当保留**（不必强行拆分，需在改动说明里注明原因）：

| 保留对象 | 原因 |
| :--- | :--- |
| `ScrollBox` / 可滚动区域 | 滚动能力依赖容器本身 |
| Lua 契约引用的容器（如 `WarehouseGrid`） | 缺失会导致运行时 `error` 或取不到引用 |
| `Button` 内的文字 Label | 按钮文字属正常结构，拆开反而失去按钮语义 |
| 带背景画刷的 `Border` 装饰容器 | 拆掉会丢失视觉背景；且内部无子控件时不影响手动拖拽 |
| 无法可靠还原绝对坐标的装饰容器 | 用估算坐标强行移出会造成错位，违反「不错位」要求 |

> **2026-09-14 补充（实测修正）**：上表第 4、5 行需谨慎——
> **空壳装饰 Border（0 子控件）其实可以安全移出**，代价只是变成设计器里的普通画布控件。
> 判断"是否安全"的依据不是"是不是 Border"，而是**「移动前后是否都是 `Collapsed`」**：
> 不可见且无画刷的 Border 移动后不可能改变渲染输出，属零视觉风险。
> 反过来，**`Visible` 且有画刷的 Border（面板底图）必须保留在原位或单独复刻画刷**，
> 否则会丢失视觉背景。详见 2.7。

### 2.7 深度平铺：把装饰 Border / 卡片也移出容器（2026-09-14 实测）

当项目要求「**所有控件都可在设计器里直接拖拽**」时，2.6 的"保留装饰 Border"
策略就不够了。此时按下述判据做深度平铺。

**核心判据：看 `Visibility` 和画刷，而不是看控件类型**

| 对象状态 | 处理方式 | 依据 |
| :--- | :--- | :--- |
| `Collapsed` 且无画刷（`Brush` 属性不存在或 `ResourceObject` 为 None） | **可以移出**，移出后保持 `Collapsed` | 不可见 → 移动不改变任何像素，零视觉风险 |
| `Visible` 且有画刷（面板底图、背景） | **保留**，或单独管理其画刷 | 移出易丢背景，且底图本身就该铺满、无需拖拽 |
| Lua 契约引用的控件（`REQUIRED_WIDGET_NAMES`） | **保留原名原位置** | 缺失会导致 `error` |
| `WrapBox` 这类运行时容器 | **可移到画布上**，只改父不改类型 | 运行时 `ClearChildren()` / 逐格定位仍生效 |

**关键操作顺序**：先移子，再删父（**自底向上**）

```
MetricsHBox(0子) → LeftVBox(0子) → RightVBox(0子)   # 这个顺序才对
RightVBox → LeftVBox → MetricsHBox                  # ❌ 会因父非空而 SKIP
```

**落位坐标怎么定**（无投影工具时的实用做法）

1. 用只读脚本读取画布上**所有控件**的现有绝对坐标
   （逐个 `slot.get_property("LayoutData").get_field("Offsets")`）。
2. 对每个待移装饰卡片，找出它语义上**应该覆盖哪些控件**（从命名和层级判断，
   例如 `FinalPriceCard` 覆盖 `LabelFinalPriceImage` + `FinalPriceText`）。
3. 取这些被覆盖控件的坐标包围盒，外扩 8~16 px 作为装饰卡片的落位。
4. 用 2.5 的写法写 `Offsets`。

这样即使不还原"原来在 VBox 里被算出来的尺寸"，落位也语义正确、
不会与任何控件错位（因为卡片本身不可见，不存在视觉重叠问题）。

**删容器前必须逐个校验 `len(w.Slots) == 0`**，非空就 SKIP 并报告——
误删父容器会连带其子树一起消失。

**验证方式分两层**：

1. **机制层**（首选，成本低且确定）：移动前后都是 `Collapsed` → 渲染输出不可能变化。
2. **像素层**：截图比对。⚠️ 见 2.8 的取景陷阱。

### 2.8 截图比对取景陷阱（2026-09-14 踩坑）

**窗口尺寸相同 ≠ 取景相同。** 两次截图之间用户可能滚轮缩放/平移画布，
或拖宽左侧面板栏。直接逐像素比对会得到巨大 MAE（实测 27.0，changed 36.8%），
把取景差异误读成「UI 被改坏了」。

**正确流程**：

1. 先标定：扫描画布橙色外框，得到画框像素范围与 `scale`
   （本项目 `calib.py` 可复用；判据为 1920/(x_max-x_min)）。
2. **`scale` 不一致 → 必须先归一化到 1920×1080 设计坐标再比**。
   实测两图 `scale` 1.5035 vs 2.6630（放大 1.77×）。
3. 归一化后若残留差异集中在**所有形状的边缘轮廓**（细线状），
   那是重采样残影，不是偏移；若差异是**整块位移**才是真问题。
4. 输出三联图（改动前 / 改动后 / 差异×3 增强）肉眼确认。

**验证结论（本项目 `AuctionSettlementUI`）**：归一化后 MAE 21.08，
差异仅剩边缘残影，卡片边界/文字/品质点全部重合，无结构性偏移。

**判断技巧**：先统计各容器子控件数（`len(w.Slots)`）。**0 子控件的容器里没有控件可移**，
真正需要处理的只有「有子控件」的自动布局容器；空壳容器要么删除（纯 VBox/HBox），
要么保留（可能带背景的 Border）。

## 3. 核心配置与参数说明

| 配置项/参数名 | 作用说明 | 推荐值/注意事项 |
| :--- | :--- | :--- |
| `CanvasPanelSlot.Position` | 控件左上角位置 | `Slot.LayoutData.Offsets` 的 `Left`/`Top`，用 `set_field` 写入；`SetPosition` 与 `widget_slot Position` 实测均不可用。 |
| `CanvasPanelSlot.Size` | 控件分配尺寸 | `Slot.LayoutData.Offsets` 的 `Right`/`Bottom`（Anchors 左上对齐时即 Size）；文字和图片必须预留最坏内容边界。 |
| `Anchors` | 相对父容器的锚点 | 贴边控件按目标边缘设置；固定设计稿控件应结合缩放容器验证。 |
| `Alignment` | 控件相对锚点的对齐基准 | 居中、贴边和角标需分别验证，不能只看 Position。 |
| `ZOrder` | 同一 Panel 内的绘制顺序 | 背景低、内容中、状态/装饰高；必须结合截图确认。 |
| `Visibility` | `Visible`、`Collapsed` 等显示状态 | 设计态占位控件可 `Collapsed`；运行时若有正式资源必须恢复为 `Visible`。 |
| `UImage.Brush` | Image 实际绘制的 `FSlateBrush` | 修改贴图应写 `Brush`；`BrushImage` 不是本次验证的替代字段。 |
| `UBorder.Background` | Border 背景画刷 | Border 使用 `Background`，不能套用 Image 的字段名。 |
| `DrawAs` | 画刷绘制方式 | 框体类素材通常使用九宫格/可拉伸方式，但具体边距需按素材检查。 |
| `ColorAndOpacity` / `BrushColor` | 控件或画刷 Tint | 使用原色素材时保持白色；深色 Tint 会与贴图颜色相乘。 |
| `UTextBlock.Font.Size` | 文本字号 | 以最长文本和最窄布局验证；项目图鉴案例为 `14/13/14/14/12`，仅是案例值。 |
| `UTextBlock.Justification` | 文本水平对齐 | 数值或收益列可右对齐；标题和类型列按网页基准选择。 |
| `ShadowOffset` / `ShadowColorAndOpacity` | 文本阴影 | 阴影透明度为 0 时不绘制；避免用阴影掩盖布局错误。 |
| `ScaleBox` | 内容缩放 | 常规主 UI 使用统一缩放结构；PC 端需同时核对带 `Pc` 后缀的缩放字段。 |
| `SizeBox.WidthOverride/HeightOverride` | 固定设计尺寸 | 1920×1080 是本项目采用的设计基准；同时确认对应 Override 开关。 |
| `UWidget.Clipping` | 内容裁剪 | 文本优先考虑 `OnDemand`；硬边界才使用强制裁剪，过度裁剪会增加绘制开销。 |
| `TextureGroup` | 贴图 LOD 分组 | UI 贴图使用 `TEXTUREGROUP_UI`，本地反射值为 `16`。 |
| `MipGenSettings` | Mip 生成策略 | UI 贴图使用 `TMGS_NoMipmaps`，本地反射值为 `13`。 |
| `CompressionSettings` / `CompressionQuality` | 贴图压缩 | UI 基线为 `TC_Default=0`、`TCQ_Highest=5`。 |
| `SRGB` | 颜色空间 | UI 颜色贴图保持 `True`，导入后必须回读。 |

### 控件位置与尺寸准确性

固定布局必须先确认设计舞台、锚点和父容器，再写 Position/Size。完整测量顺序、误差来源和检查清单见 [绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)。

### 已验证案例：图鉴藏品格子

`CollectibleCodexItemUI` 的网页对齐案例为：根条目 `256×268`；`ItemArt` 为 `(10,12,236,182)`；藏品图为 `(44,46,168,168)`；名称、类型、估值、收益和收集状态分别位于 `(14,12)`、`(14,204)`、`(14,232)`、`(134,232)`、`(158,162)`。该案例证明固定尺寸、独立文本行和明确 ZOrder 可以解决文字重叠，但这些数值不应直接复制到其他 UI。

## 4. 常见问题与解决方案 (FAQ)

- **问题现象**：用户只框了一格或一席，改完后其余同类格子/席位仍错位。
  **原因分析**：把标注对象当成唯一写入目标，或用画布绝对坐标复制到原点不同的兄弟卡。
  **解决办法**：把被框实例当模板，计算相对父卡/标题/行容器的偏移，复制到同名序号全族；回读首个、标注个、末个。详见 [绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)。

- **问题现象**：图片已经对齐，名称、报价或选中勾仍和参照席不一致。
  **原因分析**：图片层、点击层、文本层、状态叠加层是独立 Slot；只改一层不会带动其他层。选中勾若写成整行按钮尺寸，会叠在左侧图标上。
  **解决办法**：四层分开量、一起验收。叠加层先移位再按选中态显隐，不要先删除。

- **问题现象**：设计态已经绑了导入图，运行时仍显示品质色块或白块。
  **原因分析**：设计态空画刷会白块；运行时 Lua 用品质占位表覆盖；DataTable object 列内部名带 GUID 后缀，脚本没读到。
  **解决办法**：设计态写 Brush/Background；运行时优先表格贴图，空值才回退占位图。

- **问题现象**：多个文本重叠或横向溢出。  
  **原因分析**：默认字号过大、文本控件共用同一行、父容器没有最大边界，或设计态旧文本缓存仍在绘制。  
  **解决办法**：按最长文案重新分配 Slot；为类型、估值、收益拆分独立行/列；设置自动省略或明确裁剪；清空无效旧 TextBlock 的默认 Text 后重新编译、保存、刷新并截图。

- **问题现象**：长文本画出文本框，不换行。
  **原因分析**：`UTextLayoutWidget.AutoWrapText` 默认关闭；编辑器 Wrapping 分组里的「自动包裹文本」未勾选，或 Slot 没有确定宽度。
  **解决办法**：勾选自动包裹文本，并固定文本框宽度。完整步骤见 [绿洲 UMG 文本自动包裹与换行](./绿洲UMG文本自动包裹与换行.md)。

- **问题现象**：Image 显示白色方块或名称栏白底遮挡素材。  
  **原因分析**：`Brush` 未绑定正式贴图，或设计器默认占位绘制仍可见。  
  **解决办法**：先检查 Texture2D 类型和尺寸，再设置 `UImage.Brush` 或 `UBorder.Background`；设计态无运行时资源时将占位 Image 设为透明并 `Collapsed`，运行时有资源时恢复白色 Tint 和 `Visible`。

- **问题现象**：按钮贴图颜色过暗。  
  **原因分析**：贴图已经带颜色，又叠加了深灰 `BackgroundColor` 或 `ColorAndOpacity`，产生乘色。  
  **解决办法**：原色显示时保持白色 Tint；只有确实需要染色时才设置非白颜色，并通过截图比对。

- **问题现象**：设置了 `widget_slot Position` 或直接重写 `LayoutData`，但位置被清零或没有生效。  
  **原因分析**：当前 UGCAskQ MCP 实测中 `widget_slot` 不支持位置尺寸写入，Canvas Slot 的布局数据也不能用未经验证的字段直接替换。  
  **解决办法**：使用 `Slot.SetPosition`、`Slot.SetSize`、`SetAnchors`、`SetAlignment`、`SetZOrder` 等已验证函数；写后立即回读。

- **问题现象**：`widget_add` 后找不到新控件或操作到旧对象。  
  **原因分析**：旧的 `WidgetTree.AllWidgets` 缓存没有包含新节点。  
  **解决办法**：刷新蓝图对象后重新获取句柄，再通过控件迭代器和 `widget_inspect` 验证层级。

- **问题现象**：PIE 报 `may contain the following characters: %`。  
  **原因分析**：工程根目录或普通子目录存在包含 `%` 的物理路径，例如项目内误生成的 `%SystemDrive%` 目录；编辑器会在 PIE 上传前校验工程路径。  
  **解决办法**：先用绝对路径确认目标确实位于项目根目录，再使用 `-LiteralPath` 或等价的安全重命名方式处理，禁止让命令行展开 `%SystemDrive%` 后操作真实系统盘；处理后递归扫描特殊字符，再重新 PIE。

- **问题现象**：非法路径修复后 PIE 仍因 Lua 校验失败中断。  
  **原因分析**：路径校验与运行时/基础客户端 Lua 校验是不同阶段。当前项目实测的独立错误为 `client/module/module_event.lua:124` 对缺失全局 `UpdateNoticeInGameUI` 的空值访问。  
  **解决办法**：按当前编辑器版本检查基础客户端模块和启动环境；不要把该错误直接归因于图鉴蓝图。修复后重新启动 PIE，并检查客户端 TagLog、LuaLog 和编辑器日志。

- **问题现象**：蓝图改完后 PIE 中仍显示旧 UI。  
  **原因分析**：蓝图、组件、初始化和事件修改不属于普通 Lua 函数体热更新范围。  
  **解决办法**：保存并编译蓝图，停止旧 PIE，重新启动 PIE；不要仅执行 Lua 热加载判断蓝图修改是否生效。

## 5. 优化建议与注意事项

- 统一使用“网页预览 -> 用户确认 -> MCP 写入 -> MCP 回读 -> 截图 -> PIE”的闭环；截图和回读分别验证视觉结果与资产落盘状态。
- 任何 UI 写入前先备份；任何成功返回 `None` 的 MCP 写入 API 都不能仅凭返回值判定成功。
- 固定设计基准与弹性呈现分离：设计尺寸用于布局推导，屏幕适配交给 `ScaleBox`、`SizeBox`、锚点和安全区方案。
- 文本先按最长内容、最大字号、最窄屏幕验证；不要用 `min-width` 或无限绝对定位堆叠主内容。
- 列表优先使用 `ScrollBox`，并约束滚动区域高度；避免同一方向嵌套两层滚动容器。
- UI 贴图导入后立即核对 `TextureGroup`、Mip、压缩、SRGB 等属性；当前对话没有验证完整的图集打包流水线，不能直接宣称图集一定降低 DrawCall。
- 裁剪会影响 Slate 合批；只在确需边界控制的容器上启用，不要把所有控件都设置为硬裁剪。
- 触控目标尺寸、完整事件委托绑定、动效时间线和跨分辨率 PIE 矩阵在当前对话中没有完整实测，投入生产前需要单独验证。

## 6. 相关页面

- [MCP UI 编辑与高保真还原知识库](./MCP-UI编辑与高保真还原知识库.md)
- [蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [UI 页面切换与 Widget 生命周期](./UI页面切换与Widget生命周期.md)
- [绿洲编辑器 UI 截图与验证](../../../../wiki/概念/绿洲编辑器UI截图与验证.md)
- [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)
- [PIE 调试非法字符校验失败](../../../../wiki/概念/PIE调试非法字符校验失败.md)
- [绿洲 UMG 文字、透明点击层与贴边锚点摆放](./绿洲UMG文字透明点击层与贴边锚点摆放.md)
- [绿洲 UMG 文本自动包裹与换行](./绿洲UMG文本自动包裹与换行.md)
- [绿洲 UMG 设计态缩放裁剪与白块排错](./绿洲UMG设计态缩放裁剪与白块排错.md)

## 7. 待补充/待验证

- 官方 Wiki [20269_UI自适应屏幕](../../../docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md) 已覆盖 1920×1080 尺寸框 + 缩放框层次；异形屏安全区与 `ScaleBySafeZone` 语义仍待查证。设计态 Stretch 与白块见 [绿洲 UMG 设计态缩放裁剪与白块排错](./绿洲UMG设计态缩放裁剪与白块排错.md)。
- UI 事件绑定的完整菜单路径、事件节点名称、委托参数和 Lua/蓝图双向通信样例尚未在当前对话中完整验证。
- 图集打包、DrawCall 统计、动效时间线规范、内存预算和多分辨率自动化截图矩阵尚未形成可复现的实测记录。
- `UpdateNoticeInGameUI` 缺失导致的基础客户端 Lua 校验失败尚未修复；它与图鉴蓝图布局修改属于不同问题。

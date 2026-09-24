---
类型: 通用知识（实测结论）
主题: 本引擎 UMG 画布 ZOrder、裁切、可见性枚举与控件取名可达性
适用范围: 绿洲起源 UGC 编辑器（ShadowTrackerExtraUGCEditor，UE 4.18.1-0+++UE4+Release-4.18）全部 UMG 界面
证据状态: 项目实测（IslandAuctionKing，双客户端 PIE 活体探针）
来源: `raw/IslandAuctionKing/日志证据/2026-09-22_仓库藏品遮挡第四轮_裁切方案证伪.md`、`raw/IslandAuctionKing/日志证据/2026-09-22_仓库藏品遮挡第五轮_真凶ItemArt锁定.md`、`raw/IslandAuctionKing/日志证据/2026-09-22_仓库藏品遮挡第六轮_像素级取证与ZOrder失效定论.md`
更新时间: 2026-09-22
关联主题: UWidget.Clipping、EWidgetClipping、UCanvasPanelSlot.ZOrder、UScrollBox、ESlateVisibility、bIsVariable、UUserWidget.GetWidgetFromName、ESlateBrushDrawType、绘制顺序
排除范围: 未实测的其他引擎版本；本引擎 CanvasPanel「真实绘制顺序由什么决定」尚未定论
官方依据: `raw/docs/api/class/Others/UWidget.md`、`raw/docs/api/cppenum/E/EW/EWidgetClipping.md`、`raw/docs/api/class/Others/UScrollBox.md`
---

# 本引擎 UMG 画布 ZOrder、裁切、可见性枚举与控件取名可达性（实测）

> **五条高价值速查**（每条都有实测支撑，详见下文）：
> 1. `ESlateVisibility` **对调**：本引擎 `Collapsed=1 / Hidden=2`（标准 UE 反过来）→ 判读 `Visibility` 必须按本表。
> 2. `GetWidgetFromName` **只挂 `UUserWidget` 根控件**，UMG 原生控件（`CanvasPanel`/`Border`/`Button`/`Image`）上 `property not exist`。
> 3. 控件能否被 Lua 按名字取到，**唯一开关是蓝图里的 `bIsVariable`**；没勾就是 `nil`，任何路径都够不着。
> 4. `Slot:SetZOrder/GetZOrder` 的**数值读写完全生效**，但 **ZOrder 不驱动实际绘制顺序**（第六轮定论，见第一节）。**不要再靠抬 ZOrder 解决遮挡。**
> 5. `ESlateBrushDrawType` 本引擎序号 **不是**标准值：`NoDrawType=0 / Image=3 / Box=1 / Border=2`。判读画刷 `DrawAs` 必须按本表。

## 一、【第六轮定论·纠错】ZOrder 数值生效，但**不驱动绘制顺序**

> ⚠️ **本节结论已推翻本文件早前版本的第一节**。早前据「z 升序排列（首 10 → 末 40）」
> 推断「ZOrder 默认参与排序、抬 z 即可压住底下控件」——**该推断错误**。
> 第六轮用**受控变量实验 + 像素级截图**直接证伪。

### 1.1 数值层面确实生效（不变）

- 覆盖层 `CollectibleImage01/02`、`CollectibleButton01` 写 `SetZOrder(40)` → 回读 **40**
- 内容画布**首个子控件**（底格）回读 **10**
- 内容画布**末尾子控件**（覆盖层）回读 **40**
- 写多少读回多少，子控件确实按 z 值升序排列在容器里。

### 1.2 但绘制顺序与 z 无关（四次受控实验）

场景：`WarehouseContentCanvas` 内 84 个背景格（z=10）+ 64 个藏品覆盖层（z=40），
所有覆盖层可见性/画刷/透明度均**正确**（详见 §十）。屏幕表现：**覆盖层被格子完全盖住。**

| # | 操作 | 结果 | 推论 |
|---|---|---|---|
| ① | 基线不动 | 覆盖层被遮挡 | 复现现象 |
| ② | 84 格全部 `SetVisibility(Collapsed)` | **覆盖层立即显现** | 格子是遮挡源 |
| ③ | 覆盖层 z 由 40 改为 **5**（低于格子 10） | **仍然被遮挡** | **z 值与遮挡无关** |
| ④ | 84 格 `ItemButton` 背景 `A` 改为 0 | 整片暗方格**整体消失** | 格按钮背景即不透明遮挡层 |

补充实验 D：把覆盖层 `RemoveFromParent` 后重新 `AddChildToCanvas`（真正追加到末尾）→ **仍被遮挡**。
→ 本引擎绘制顺序**也不是**简单的「子控件插入顺序」。

### 1.3 结论

- **`Slot:SetZOrder` 不能用来解决跨控件遮挡**（在本引擎实测无效）。
- 同理 `RaiseOverlays`（摘除重挂到末尾）**也无效**。
- 遇到遮挡，应从**遮挡源本身的不透明度/可见性**入手（本工程即「底格 `ItemButton` 背景 `A=0.92`」），
  而不是调整层级。
- **本引擎 CanvasPanel 真实绘制顺序规则仍未定论**（见 §八）。

## 一·补、ZOrder 数值可读写（原始实测记录，保留供对照）

**实测（2026-09-22，双客户端 PIE 活体探针）**：

- 对覆盖层 `CollectibleImage01/02`、`CollectibleButton01` 调 `Slot:GetZOrder()` → 全部读到 **`40`**
- 内容画布**首个子控件** `Slot:GetZOrder()` → **`10`**（底格）
- 内容画布**末尾子控件** `Slot:GetZOrder()` → **`40`**（覆盖层）

### 纠错：不存在 `bExplicitCanvasChildZOrder`

UE 新版本有 `UCanvasPanel::bExplicitCanvasChildZOrder`（开启后 Slot ZOrder 才参与排序）。
**本引擎（UE 4.18.1）的 `CanvasPanel` 没有这个属性**。客户端日志明确：

```
LuaExtend_GetProp: Lua_GetPropertyValue Failed:
  Object [CanvasPanel ...WarehouseContentCanvas]
  PropName [bExplicitCanvasChildZOrder]: property not exist
```

四个候选字段名（`bExplicitCanvasChildZOrder` / `ExplicitCanvasChildZOrder` /
`bExplicitChildZOrder` / `bExplicitZOrder`）**在 Lua 侧全部探不到（`nil`）**。

→ 因此「ZOrder 不生效是因为没开显式 ZOrder」这类推论在本引擎**不成立**；
反过来，**不要**为了「让 ZOrder 生效」去写这个不存在的字段（会刷一堆
`property not exist` 的 LuaException 日志）。

## 二、`EWidgetClipping` 取值与语义（官方原文）

| 值 | 名称 | 官方定义 |
|---|---|---|
| 0 | `Inherit` | This widget does not clip children, it and all children inherit the clipping area of the last widget that clipped. |
| 1 | `ClipToBounds` | clips content the bounds of this widget. It intersects those bounds with any previous clipping area. |
| 2 | `ClipToBoundsWithoutIntersecting` | clips content the bounds of this widget. It does NOT intersect with any existing clipping geometry, **it pushes a new clipping state**. |
| 3 | `ClipToBoundsAlways` | clips content to the bounds of the widget. Ignores the inherited clip rect. |
| 4 | `OnDemand` | clips to bounds, only if the inherited clipping rect is smaller than the widget bounds. |

官方 `UWidget.Clipping` NOTE：

> **Elements in different clipping spaces can not be batched together**, and so there is a performance cost to clipping.

**要点**：取值 `2` 会**新建**裁切空间（而非继承），若是想「统一到同一裁切空间」，
应该用 `Inherit(0)`，**不是** `ClipToBoundsWithoutIntersecting(2)`。

## 三、典型滚动链路实测值（参考基线）

`WarehouseScrollBox → WarehouseContentSizeBox → WarehouseContentCanvas → 148 子控件`：

| 控件 | `Clipping` 实测 |
|---|---|
| `ScrollBox` | `1`（`ClipToBounds`）|
| `SizeBox` | `0`（`Inherit`）|
| `ContentCanvas` | `0`（`Inherit`）|
| `ScrollBox` 直接子控件数 | `1`（只挂 SizeBox）|
| `SizeBox` 尺寸 | `562.2 x 1300.7` |
| `ScrollBox` 滚动偏移 | 初始 `0.0` |

**判读**：滚动链路里 **只有 ScrollBox 一层裁切空间**，中间层都是 `Inherit`。
所以「中间层引入多余裁切空间导致 ZOrder 失效」这类假设，在本工程实测**不成立**，
改 `SizeBox`/`ContentCanvas` 的 `Clipping` 是**无效改动**（写前写后都是 0）。

## 五、`ESlateVisibility` 枚举与标准 UE4 **对调**（2026-09-22 第五轮实测）

活体枚举实测（客户端探针）：

```
ESlateVisibility: Visible=0  Collapsed=1  Hidden=2  HitTestInvisible=3  SelfHitTestInvisible=4  ESlateVisibility_MAX=5
```

| 名称 | 本引擎 | 标准 UE4 | 差异 |
|---|---|---|---|
| `Visible` | **0** | 0 | 同 |
| `Collapsed` | **1** | 2 | **对调** |
| `Hidden` | **2** | 1 | **对调** |
| `HitTestInvisible` | 3 | 3 | 同 |
| `SelfHitTestInvisible` | 4 | 4 | 同 |

**影响**：任何「读 `Visibility` 返回值判状态」的代码，按标准 UE 序号判读会
**把 `Collapsed` 误判成 `Hidden`**（例如把 `1` 读成「仅隐藏、仍占布局」，实际是「已折叠、不占布局也不绘制」）。

**注意**：枚举**名**（`ESlateVisibility.Collapsed`）仍可正常使用，只是数值是 1 而非 2。
**写入**时优先用枚举名，**判读**时必须按上表。

## 六、`GetWidgetFromName` 只挂 `UUserWidget` 根控件（2026-09-22 第五轮实测）

| 调用对象 | 结果 |
|---|---|
| `AuctionTestUIWidget:GetWidgetFromName('CollectibleCodexItemUI_C_0')` | ✅ 返回活体控件 |
| `AuctionTestUIWidget:GetWidgetFromName('WarehouseContentCanvas')` | ✅ 返回画布 |
| `AuctionTestUIWidget:GetWidgetFromName('ItemArt')` | ❌ `nil`（非本控件成员）|
| `CanvasPanel:GetWidgetFromName(...)` | ❌ `property not exist` |
| `Button:GetWidgetFromName(...)` | ❌ `property not exist` |

引擎日志原文：

```
LuaExtend_GetProp: LuaExtend::Lua_GetPropertyValue Failed:
Object [CanvasPanel ...WarehouseContentCanvas] PropName [GetWidgetFromName]: property not exist
```

**推论**：
1. 「按名查找子控件」**只能从 UI 根控件发起**，不能从任意 UMG 原生控件（`CanvasPanel` / `Border` / `Button` / `Image`）发起。
2. 根控件只能查**自己的直接成员名**，查不到孙控件（如 `ItemArt` 属于 `CollectibleCodexItemUI_C`，不属于 `AuctionTestUI`）。
3. 因此「对动态创建的子控件做递归按名查找」在本引擎**不可行**；
   必须让目标控件在它**自己的蓝图里勾选 `bIsVariable`**，才能被 Lua 按字段名取到。

### 配套：`bIsVariable` 是 Lua 可达性的唯一开关

蓝图导出 JSON 里，控件若**没有 `bIsVariable: True`**（字段缺失即未勾选），
Lua 侧 `widget.控件名` 恒为 `nil`，且上述 `GetWidgetFromName` 路径也够不着它。
→ **排查「某控件 Lua 取不到」时，第一步查蓝图 JSON 里该控件的 `bIsVariable`**，不必等 PIE。

## 七、排查建议顺序

遇到「A 被 B 盖住 / 滚出视口后被盖住」时：

1. **先取像素级证据**：截图（`ctypes.EnumWindows` 找 PIE 窗口 + `PIL.ImageGrab.grab(bbox)`），
   别用纯推理代替观察。像素是最硬的证据。
2. **先确认探针对象是自己以为的那个**：读日志里 `ud_object[...]` 的**完整路径**，别只看变量名。
   （实测踩坑：`AuctionCellButtons[1]` 存的是单格里的 `ItemButton`，不是单格本身。）
3. **做「排除法实验」定位遮挡源**：把怀疑的控件 `SetVisibility(Collapsed)`，
   若被遮物**立即显现**，即锁定遮挡源。
4. **改嫌疑遮挡层的不透明度**（背景刷 `A`）：若屏幕上的遮挡物**整体消失**，
   即确证它就是屏幕上看到的那一层。
5. **不要靠调 ZOrder / 重挂控件解决遮挡** —— 本引擎实测无效（见 §一）。
6. **逐项排除被遮物自身的问题**（可见性/`RenderOpacity`/`ColorAndOpacity`/`Brush.ResourceObject`/`Brush.DrawAs`），
   确认它「本来应该能画出来」。
7. **读 `Visibility` 时按第五节的枚举表判读**；对取不到的控件，**回蓝图 JSON 查 `bIsVariable` 与 `BrushColor.A`**。
8. **最后才怀疑绘制顺序重排**：`ScrollBox` 在 `ClipToBounds` 下滚动时是否重排子控件 draw order，
   需在**滚动过程中**采样验证（本工程仍未实测）。

## 八、未决

- **本引擎 CanvasPanel 的真实绘制顺序由什么决定**（**未定论**）。
  已排除：`Slot.ZOrder`（实验③）、子控件插入顺序（实验 D）。
  待查：是否与控件类型（`UUserWidget` vs 原生控件）、`AddChildToCanvas` 的引擎内部分类、
  或布局 pass 重排有关。
- `ScrollBox` 滚动时是否重排子控件绘制顺序（**未实测**，需滚动中采样）。

## 十、`ESlateBrushDrawType` 本引擎序号（2026-09-22 第六轮实测）

```
ESlateBrushDrawType: NoDrawType=0  Image=3  Box=1  Border=2
```

| 名称 | 本引擎 | 标准 UE4 | 差异 |
|---|---|---|---|
| `NoDrawType` | 0 | 0 | 同 |
| `Image` | **3** | 1 | **不同** |
| `Box` | **1** | 0 | **不同** |
| `Border` | **2** | 2 | 同 |

**影响**：读画刷 `brush.DrawAs` 判读显示方式时，若按标准 UE 序号，
会把 `Image(3)` 误读成 `Box/Border`，进而误判「画刷类型错误导致不显示」。
**写入**时优先用枚举名，**判读**时必须按上表。
（实测：`CollectibleImage01.brush.DrawAs = 3` 是正确的 `Image`，非异常。）

### 附：覆盖层「配置全对但不出像素」的逐项核查表

排查「某 `UImage` 明明设置了却看不见」时，逐项确认（本工程实测全部为正常值）：

| 检查项 | 正常值样例 | 取法 |
|---|---|---|
| `Visibility` | `3`（HitTestInvisible，仍绘制） | `img.Visibility` |
| `RenderOpacity` | `1.0` | `img.RenderOpacity` |
| `ColorAndOpacity` | `(1,1,1,1)` | `img.ColorAndOpacity.A` |
| `brush.ResourceObject` | 有效 `Texture2D` | `img.brush.ResourceObject` |
| `brush.ImageSize` | 非 0 | `img.brush.ImageSize.X` |
| `brush.DrawAs` | `3`（= `Image`） | `img.brush.DrawAs` |
| 父链各层 `Visibility` | `0` / `4`（均可绘制） | 逐层读 |
| `Slot` 位置/尺寸 | 落在视口内 | `slot:GetPosition()/GetSize()` |

**若以上全部正常却仍无像素 → 遮挡源在别处，去查同层其他控件的背景不透明度。
不要继续在被遮物自身上找原因。**

## 九、方法学（踩坑）

1. `doluastring` 的代码**不能用 `\n` 换行**：控制台按单行处理 `dostring content:`，含换行只回显不执行。
2. **片段过长会被静默丢弃**：只回显、无输出、无报错。探针须拆小（每段 1–3 个取值）。
3. `doluastring` 返回 `{}` **不等于执行成功**，必须回读客户端日志确认 `LogUGCClient: [TagLog]`。
4. 用 `pcall` 逐个字段包裹，避免一个不存在字段把整段输出吞掉。
5. **探针先确认对象是谁再读值**。本轮两次探针选错对象（`CellButton01` 是遗留 Button、
   `AuctionCellButtons[1]` 是 `ItemButton`），得到「9 项全 NIL」的假象，白走一轮推断。
6. **「按字段名 + 按接口名」两路都失败时，先查蓝图导出 JSON 里该成员是否存在，再下「无效」结论。**
7. **凡涉及引擎枚举，先活体取枚举值，不要套用通用 UE 认知。**
   （`ESlateVisibility` 对调、`ESlateBrushDrawType` 序号不同，都是典型反例。）
8. **「对象属性全对但屏幕上没有」时，一定是别的东西盖住了它** —— 用排除法（折叠嫌疑物）定位，
   不要继续在被遮物自身上加检查项。第六轮四次实验即按此方法一次定位。
9. **截图取证优于纯推理**：`ctypes.EnumWindows` 按 `PIEPlayer_T1_10001` 标题取 `hwnd`，
   `GetWindowRect` 拿 bbox，`PIL.ImageGrab.grab(bbox, all_screens=True)` 截图；
   网格这类细节区再 `crop + resize(2x, LANCZOS)` 放大看。
10. **截图前先 `SetForegroundWindow` 并 `sleep ~1s`**，否则可能抓到被遮挡的窗口内容。


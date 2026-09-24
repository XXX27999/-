# 2026-09-15 AuctionGuaranteeGoldUI：画刷 ResourceObject 存成 UPackage + Slot Alignment 漏写导致「UI 超出画布、贴图未被使用」

> 类型：项目证据（蓝图与 UI / 设计态渲染 + MCP 写入）
> 主题：`AuctionGuaranteeGoldUI` 保底金弹窗报「UI 超出画布、图片素材并未使用、与网页预览不同」的三个真因定位与修复
> 适用范围：仅 `IslandAuctionKing` 项目；写入手法与排障顺序可推广到同项目其他 UMG 蓝图
> 证据状态：项目实测（UGCAskQ MCP 回读 + 设计器截图 + 彩色探针像素量测 + 子控件坐标扫描拟合 + **PIE 运行时截图与缩放下标量测**）
> 更新时间：2026-09-15
> 官方依据：`raw/docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md`（根 ScaleBox → SizeBox(1920×1080) → CanvasPanel 层次）
> 关联主题：[2026-09-15_PIE主界面不铺满_根ScaleBoxStretch修复](./2026-09-15_PIE主界面不铺满_根ScaleBoxStretch修复.md)、[2026-09-11_AuctionSettlementUI_铺满1920x1080](./2026-09-11_AuctionSettlementUI_铺满1920x1080.md)、[2026-09-15_PIE主界面不铺满_根ScaleBoxStretch修复#整屏 UI 自适应](./2026-09-15_PIE主界面不铺满_根ScaleBoxStretch修复.md)
> 排除范围：`ZhuJieMian` 根 ScaleBox `Stretch=0` 的复原状态（用户明确要求保留），本轮未触碰；本页不讨论保底金玩法逻辑

---

## 一、结论（三个真因，互相独立）

| # | 真因 | 现象 | 修复 |
| --- | --- | --- | --- |
| 1 | 面板的 `CanvasPanelSlot.LayoutData.Alignment` 是 **(0.5,0.5)** 而不是 (0,0) | 控件左上角 = `(401,31) − 0.5×(1117,1018) = (−157.5,−478)`，金框顶部/左侧跑出画布、内容挤到画布左上角 → **「UI 超出画布」** | `ld.set_field("Alignment", ue.FVector2D(0.0,0.0))` |
| 2 | 画刷 `ResourceObject` 里存的是 **`UPackage`**，不是 `Texture2D` | Slate 取不到贴图 → **回落默认纯白贴图**；叠加残留 `BrushColor`（面板深橙、数据条近黑）后显示为纯色块 → **「图片素材并未使用」** | 用 `ue.load_object(ue.find_class('Texture2D'), path)` 重取对象后写入（13 处） |
| 3 | 面板**没有**根包裹层（缺 ScaleBox/SizeBox） | 坐标 = 裸视口像素，1117×1018 在 1280×720 下必然超出 | 补成与 `AuctionSettlementUI` 同构的 `ScaleBox → SizeBox(1920×1080) → CanvasPanel` |

真因 1 与 2 是「数据看着全对、渲染却不对」的典型：`widget_inspect` 打印的 `Pos: 401,31, Size: 1117,1018` 完全正确，`ResourceObject` 回读也有合法资产路径 —— 只有把 **Alignment 值** 和 **对象的 `UClass`** 单独读出来才暴露。

---

## 二、真因 1：Slot Alignment 漏写

### 2.1 现场数据（`ue_py` 只读枚举）

| 控件 | Anchors | Alignment | Offsets(L,T,R,B) |
| --- | --- | --- | --- |
| `RootScaleBox` | (0,0)-(1,1) | (0.000,0.000) | 0,0,0,0 |
| `ScreenScrim` | (0,0)-(1,1) | (0.000,0.000) | 0,0,0,0 |
| **`PanelBorder`** | (0,0)-(0,0) | **(0.500,0.500)** ← 异常 | 401,31,1117,1018 |
| `TitleText` / `CloseButton` / 4×Row / Label / Value / StatusText / ClaimButton | (0,0)-(0,0) | (0.000,0.000) | 各自正确 |

### 2.2 机制

`FAnchorData` 的几何计算：非拉伸锚点下

```
Position           = Anchors.Minimum × ParentSize + Offsets.Left/Top
Widget.TopLeft     = Position − Alignment × Offsets.Right/Bottom(Size)
```

- Anchors=(0.5,0.5)、Alignment=(0.5,0.5)、Offsets=(0,0,1117,1018) → 面板**居中**（`AuctionSettlementUI` 等居中弹窗用的就是这套）。
- Anchors 改成 (0,0) 而 Alignment 仍留 (0.5,0.5) → 位置基准从「父容器中心」变成「父容器左上 (401,31)」，**再减掉半个自身尺寸** → 左上角变成 (−157.5,−478)，即面板整体左上移位。

### 2.3 为什么同批写入里只有它中招

`RootScaleBox` / `ScreenScrim` 用的是**四向拉伸锚点 (0,0)-(1,1)**，Slate 在这种锚点下**直接忽略 Alignment**（几何 = min..max，Offsets 当四边距）。
所以「写了一批控件，只有非拉伸的那个偏移」是**可预期的**，不是随机的。

### 2.4 教训

> `widget_add` / `widget_move` 新建或重建的 `CanvasPanelSlot`，`Alignment` 默认值是 **(0.5,0.5)**（引擎默认，不是 (0,0)）。
> 只按惯例写 `Anchors` + `Offsets` 而不写 `Alignment`，只要锚点是非拉伸的，控件就会被向左上偏移半个自身尺寸。

---

## 三、真因 2：`ResourceObject` 存成 `UPackage`

### 3.1 铁证（回读 repr）

```
== brush ResourceObject ==
   repr = <unreal_engine.UObject '/IslandAuctionKing/Asset/TuPian/AuctionUI/GuaranteeGold/GuaranteeGoldPanel'
           (0x00000003C68B21C0) UClass 'Package' (refcnt: 4)>
   class = Package          ← 不是 Texture2D
   path = /IslandAuctionKing/Asset/TuPian/AuctionUI/GuaranteeGold/GuaranteeGoldPanel
```

13 处全部如此：`PanelBorder` + 4 条数据条 + `ClaimButton`/`CloseButton` 各 4 个状态。

### 3.2 为什么肉眼看不出来

- 路径字符串完全正确，`get_path_name()` 也正确 → 单纯读路径会误判「已绑定」。
- 写进去**不报错**，`set_field('ResourceObject', obj)` 对任何 UObject 都成功。
- Slate 侧拿不到有效贴图资源时**回落默认白贴图**（`DrawAs=Image` + 空/无效资源 = 白色实心），
  所以症状是「纯白/纯 `BrushColor` 色块」，而不是「什么都没有」。

### 3.3 正确取法

```python
import unreal_engine as ue
T2D = ue.find_class('Texture2D')           # Widget 蓝图类名则要 ue.find_class('UGCWidgetBlueprint')
tex = ue.load_object(T2D, '/IslandAuctionKing/Asset/TuPian/AuctionUI/GuaranteeGold/GuaranteeGoldPanel')

br = w.get_property('Background')          # Border 用 Background；Image 才是 Brush
br.set_field('ResourceObject', tex)
br.set_field('DrawAs', 3)                  # 3 = Image
```

校验（写入后必须做）：

```python
ro = br.get_field('ResourceObject')
print(ro.get_class().get_name())           # 必须 == 'Texture2D'
```

### 3.4 附带的 `BrushColor` 残留

原占位设计用纯色当底，导入贴图后 `BrushColor` 没重置：

| 控件 | `BrushColor`（修复前） | 修复后 |
| --- | --- | --- |
| `PanelBorder` | (0.768, 0.323, 0.010, 1.0) 深橙 | (1,1,1,1) |
| 4 × GoldRow | (0.0116, 0.0144, 0.0203, 1.0) 近黑 | (1,1,1,1) |
| `ScreenScrim` | (0,0,0,0.58) ← 有意保留的遮罩 | 不变 |

> `ScreenScrim` 的黑色半透明是弹窗遮罩，**不要**一起洗成白色。

---

## 四、真因 3：补根包裹层（项目弹窗标准层次）

修复后的层次（与 `AuctionSettlementUI` 同构）：

```
CanvasPanel_0
└── RootScaleBox   ScaleBox  Anchors (0,0)-(1,1) / Offsets 0
    │              Stretch=5, StretchDirection=0, StretchPc=5, StretchDirectionPc=0
    └── RootSizeBox  SizeBox  WidthOverride=1920, HeightOverride=1080
        └── ContentCanvas  CanvasPanel
            ├── ScreenScrim  Border  Anchors (0,0)-(1,1) / Offsets 0   （遮罩，铺满设计画布）
            └── PanelBorder  Border  Anchors (0,0)-(0,0) / Alignment (0,0) / Offsets 401,31,1117,1018
                └── PanelCanvas  CanvasPanel
                    └── TitleText / CloseButton / 4×GoldRow(+Label+Value) / StatusText / ClaimButton
```

- `(401,31) = ((1920−1117)/2, (1080−1018)/2)` → 面板在 1920×1080 设计画布内**居中**。
- 16:9 视口下 ScaleBox 缩放恒为 `视口宽/1920`：1280×720 → 0.667（面板呈现 745×679，完整可见）；1920×1080 → 1.0（1117×1018）。
- `Stretch=5`（ScaleToFill）与 `AuctionSettlementUI` 一致；16:9 下与 `ScaleToFit` 等效，非 16:9 下 ScaleToFill 会裁切较长边（弹窗场景若需绝对不裁切应改 2）。

### 4.1 包裹层生效的自证：彩色探针

把 `ScreenScrim.BrushColor` 临时设为**不透明红**、`PanelBorder` 设为**不透明绿**，截图后量测：

```
RED(scrim/ContentCanvas): bbox=(627,234,1744,861) w=1118 h=628 aspect=1.7803 (设计 1920/1080 = 1.7778) ✓
GREEN(panel):             bbox=(627,234,1291,557) w=665  h=324 aspect=2.0525
```

- 红区宽高比 **1.7803 ≈ 16:9** → 说明 `ContentCanvas` 确实已是一个 16:9 设计空间，包裹层生效。
- 绿区锚在红区左上角 `(0,0)` 而非 `(401,31)` → **正是真因 1 的直接证据**（面板被 Alignment 拉到左上）。
- 量测脚本：`备份\IslandAuctionKing\20260915_保底金UI\measure_probe.py`。

> 探针用完必须**恢复原色**（`ScreenScrim=(0,0,0,0.58)`、`PanelBorder=(1,1,1,1)`），本轮已恢复并回读确认。

---

## 五、其余修复与验证

### 5.1 按钮四状态贴图

`ClaimButton` / `CloseButton` 的 `WidgetStyle` 原本只有 `Normal` 有贴图，`Hovered`/`Pressed` 是 `DrawAs=1(Box)` + `ResourceObject=None`、`Disabled` 是 `DrawAs=0` → **鼠标悬停/按下时贴图消失**。
已把四个状态统一写成同一张贴图 + `DrawAs=3`。

### 5.2 设计器截图验收

`备份\IslandAuctionKing\20260915_保底金UI\capture\editor_fixed_01.png`：
金框（顶部渐变带 + 左上/右上/右下「///」斜纹）、4 条数据条（当前金币 8,000 / 底价阈值 10,000 / 可领金额 2,000 / 今日剩余 3/3）、
状态文案「低于底价，领取后金币补到阈值」、确认领取按钮、右上 ✕ 全部正确渲染，面板整体落在画布内。

### 5.3 子控件坐标扫描拟合

沿 x=1064 竖扫（`备份\...\scan_bar.py`）：

```
顶部金带 237..300；4 条数据条深蓝区 308..398 / 422..512 / 536..626 / 650..740（间距 114px）
状态文案洋红 753..768；按钮金区 785..891；底部金带 906..955（被设计器横向滚动条截断）
```

按 `rendered = 179.2 + 0.844 × design` 反算：条间距 135×0.844 = 114 ✓、条 4 底边 671→740 ✓、状态文案 675..705→749..774 ✓、按钮 709..859→777..904 ✓。
→ **面板内部排布为等比正确**。

---

## 六、排障顺序（可复用）

数据正确但渲染不对时，按此顺序读值，不要先怀疑坐标：

1. **`LayoutData.Alignment`** —— `widget_add`/`widget_move` 后默认 (0.5,0.5)；非拉伸锚点下必查。
2. **`ResourceObject.get_class().get_name()`** —— 必须 `Texture2D`；`Package` 即绑定无效（表现为纯白贴图）。
3. **`BrushColor` / `ColorAndOpacity`** —— 占位纯色是否残留把贴图调制成了纯色。
4. **父链是否有 `ScaleBox → SizeBox(1920×1080)`** —— 缺则坐标即裸视口像素。

读值写法：

- **必须用 `%s` 格式化**：`'%s' % w.BrushColor` 得到 `{'r':0.768,...}` 字典式 repr；`%r` / `repr()` 只给 `<FLinearColor object at 0x...>`，会被误判成「读不到值」。
- `w.get_editor_property('BrushColor')` 可能抛异常 → 回退 `getattr(w, 'BrushColor')`。
- 结构体字段写入一律 `get_field(...).set_field(...)`，**不要**回写整条 struct。

---

## 七、未决与生效方式

- 本轮改的是**蓝图资产**（层次 + 画刷 + Slot），运行中的 PIE 会话持有旧生成类 → **必须重新调试 PIE** 才能看到运行时表现；
  保底金面板为弹窗，需触发 `AuctionGuaranteeGoldUIService` 的创建流程（或从大厅入口进入保底金逻辑）。
- **运行时复验已补完（同日第二轮）**：重启 PIE 并用 Lua 主动调 `AuctionGuaranteeGoldUIService.CreateAndShow(UGCGameSystem.GetGameState())` 拉出面板，客户端绘制区截图 + 行间距量测确认面板完整落在画布内。第二轮还查出并修掉了一个只在运行时暴露的新真因（尺寸框重载开关未打开），见第九节。
- 本资产没有任何 Lua 侧 `SetRenderScale` / `SetPositionInViewport`：`AuctionUIMotionService` 的淡入只写 `SetRenderOpacity`，所以运行时几何问题只能来自 UMG 层次与 Slot 数据，不能归因于动效服务。

## 八、证据与产物路径

| 类别 | 绝对路径 |
| --- | --- |
| 写前备份 | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_保底金UI\写入前备份\AuctionGuaranteeGoldUI_before_rootwrap.uasset`（52,090 B，MD5 `3F800E8358ADCEA72F4BE472F532F9DF`） |
| 素材原图 | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_保底金UI\素材原图\` |
| 彩色探针截图 | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_保底金UI\capture\probe_colored.png` |
| 修复后设计器截图 | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_保底金UI\capture\editor_fixed_01.png` |
| 量测脚本 | `...\20260915_保底金UI\measure_probe.py`、`measure_final.py`、`measure_consistency.py`、`scan_bar.py`、`crop_zoom.py` |
| MCP 计划 id | `plan_16786920_b9c88024`（同一资产复用 9 次调用） |
| 第二轮写前备份 | `备份\IslandAuctionKing\20260915_保底金UI\写入前备份\AuctionGuaranteeGoldUI_before_sizebox_override.uasset`（56,555 B，MD5 `82068AB5EC97DBCAD787DDA210CF824B`） |
| 第二轮写入后 | 56,660 B，MD5 `6F6ACFAAF484C25CBEEA8EB316C7D64E`，13:25:14 |
| 运行时截图（修复前/后） | `...\capture\pie_client_01.png`（放大出界）、`pie_client_fixed.png`（完整在画布内） |
| 运行时量测输出 | `...\capture\pie_client_measure.txt` / `pie_client_measure_fixed.txt` / `row_check.txt` |
| 设计态截图（第二轮后） | `...\capture\editor_after_sizebox_fix.png` |

---

## 九、第二轮（同日）：运行时被放大 1.264 倍并裁切 —— 尺寸框重载开关未打开

### 9.1 现象

第一轮修完后重启 PIE，面板虽然用上了贴图，但**依然超出画布**：金框右侧贴近屏幕右缘、底部被裁，面板整体比设计大一圈。

### 9.2 运行时取证

| 项目 | 值 |
| --- | --- |
| PIE 客户端绘制区（`GetClientRect` + `ClientToScreen`） | **1920×1009**，宽高比 1.9029（不是 16:9） |
| 数据条行间距（设计基准 135 px） | 实测 **170.67 px** → 运行时缩放 = **1.2642** |
| 修复后同一量测 | 实测 **126.33 px** → 运行时缩放 = **0.9358**（预测 `1009/1080 = 0.9343`，偏差 0.16%） |

> 量测脚本：`备份\IslandAuctionKing\20260915_保底金UI\measure_client.py`（抓绘制区 + 扫描线）、`measure_rows.py`（行间距 → 反算缩放下标量）。

### 9.3 真因

`RootSizeBox` 回读：

```
WidthOverride=1920.0 | HeightOverride=1080.0 | bOverride_WidthOverride=False | bOverride_HeightOverride=False
```

**重载值写了，但 `bOverride_*` 约束开关没打开** —— `WidthOverride` / `HeightOverride` 是受 `EditCondition` 约束的属性，开关不开，运行时不生效。后果链条：

1. 尺寸框期望尺寸退化为内容自然尺寸 = `ContentCanvas` 的包围盒 = `401+1117=1518` 宽、`31+1018=1049` 高（`ScreenScrim` 是四向拉伸锚点，不贡献期望尺寸）。
2. 根 ScaleBox `Stretch=5`。本轮用 `ue_read enum:EStretch` 拿到官方枚举元数据语义：`ScaleToFill(5)` = 等比放大「直到四边都达到或超过区域」并裁掉较长边，即 **`scale = max(sx, sy)`**（**等比**，不是 X/Y 各自拉伸）。
3. `scale = max(1920/1518, 1009/1049) = max(1.2648, 0.9619) = 1.2648` → 内容整体放大 1.26 倍，横向刚好铺满、**纵向被裁** → 面板偏右且底部出界。

横向对照三个同级蓝图，`bOverride_*` 全为 True，只有本资产是 False：

| 资产 | 根 ScaleBox `Stretch`/`StretchPc` | SizeBox `1920×1080` 数值 | `bOverride_*` |
| --- | --- | --- | --- |
| `ZhuJieMian` | 0 / 0（用户要求保留） | 1920 / 1080 | **True / True** |
| `AuctionSettlementUI` | 5 / 5 | 1920 / 1080 | **True / True** |
| `AuctionTestUI` | 2 / 1 | 1920 / 1080 | **True / True** |
| `AuctionGuaranteeGoldUI`（修复前） | 5 / 5 | 1920 / 1080 | **False / False** ← 缺陷 |
| `AuctionGuaranteeGoldUI`（修复后） | 2 / 2 | 1920 / 1080 | **True / True** |

### 9.4 修复（EditCondition 两阶段写）

```python
# 阶段1：先打开约束开关
sz.bOverride_WidthOverride = True
sz.bOverride_HeightOverride = True
# 阶段2：再写数值与拉伸模式
sz.WidthOverride = 1920.0
sz.HeightOverride = 1080.0
sb.Stretch = 2        # ScaleToFit：等比装入，非 16:9 视口不裁切
sb.StretchPc = 2      # PC PD3D_SM5 取这一套
sb.StretchDirection = 0
sb.StretchDirectionPc = 0
```

回读：`WidthOverride=1920.0 HeightOverride=1080.0 ovW=True ovH=True | Stretch=2 StretchPc=2 Dir=0 DirPc=0`，`bp.save_package()` 与 `ue.objed_save_asset('AuctionGuaranteeGoldUI','UI')=True`。

> **`Stretch=5 → 2` 的理由**：视口 1920×1009 宽高比 1.9029 ≠ 16:9。`ScaleToFill(5)` 得 `scale = max(1.0, 0.9343) = 1.0`，设计舞台下沿 `1049` 超出视口 `1009`，弹窗底部会被裁 ~40 px；`ScaleToFit(2)` 得 `0.9343`，整套 1920×1080 完整装入并居中，弹窗必然完整可见。

### 9.5 修复后复验（PIE，DebugID 重启后新会话）

- Lua 主动创建：`CreateAndShow ok=true zOrder=520 bindOK=true`；`GetWidgetFromName` 能取到 `RootScaleBox`/`RootSizeBox`/`ContentCanvas`。
- 预测面板矩形（`scale=0.9343`，水平居中余量 `(1920-1794)/2=63`）：`x 437.7..1481.4`、`y 29.0..980.1`。
- 实测金色框体 `bbox=(447,42,1428,966)`、竖扫在 `y≈836` 命中按钮金色 `(245,158,29)`、`y≈977` 命中底框 `(81,63,54)` —— 与预测的 `y 29..980` 吻合（金框图形本身比外框内缩约 13 px）。
- 截图 `capture\pie_client_fixed.png`：金框（含底部斜纹装饰）、右上 ✕、标题「领取保底金」、4 条数据（当前金币 30,000 / 底价阈值 10,000 / 可领金额 0 / 今日剩余 3/3）、状态文案「已达保底阈值，当前不可领取。」、金色「已达保底」按钮 —— **全部完整可见，面板在画布内居中**。
- 修复前同口径截图 `capture\pie_client_01.png` 作为对照（面板放大出界）。

### 9.6 教训

1. `WidthOverride` / `HeightOverride` 必须连 `bOverride_*` 一起写并一起回读；只回读数值会漏掉本类缺陷。
2. 运行时「被放大」而不是「被缩小」，是根缩放基准小于视口的指纹；先量 `实测间距 / 设计间距` 得到实际 scale，再与 `min/max(视口/设计)` 对账，不要先改锚点。
3. 量测要抓**客户端绘制区**（`GetClientRect`+`ClientToScreen`），整窗截图会把标题栏与边框算进去。
4. 蓝图资产改动无法热更新到运行中的 PIE，必须重启 PIE 复验；Lua 侧可用 `CreateAndShow(UGCGameSystem.GetGameState())` 主动拉起弹窗做可视验证。

# 2026-09-15 ZhuJieMian 主界面：自适应铺满 + 控件保持原始尺寸的方案要点

> 类型：项目方案（蓝图与 UI / 自适应）
> 主题：在「整屏铺满」的同时让「UI 控件不随分辨率缩放」的定位与适配策略
> 适用范围：`IslandAuctionKing` 主界面 `Asset/Blueprint/Prefabs/UI/ZhuJieMian`；通用原则见 [绿洲 UMG 设计态缩放裁剪与白块排错](../../知识/通用/UI与交互/绿洲UMG设计态缩放裁剪与白块排错.md)
> 证据状态：控件树、锚点、几何为**项目实测**（MCP 只读 ROI，2026-09-15，43 个控件全量导出）；Slate 底层排布细节为**推断**，需编辑器实测复核
> 设计基准：1920 × 1080
> 更新时间：2026-09-15

---

## 一、核心结论：铺满与「控件不缩放」是一对互斥目标，必须拆成两套机制

用根 `ScaleBox` 的 `Stretch` 做适配时，只有三种结果，**没有一种能同时满足两个目标**：

| Stretch | 铺满 | 控件尺寸 | 判定 |
| --- | --- | --- | --- |
| `2` ScaleToFit | 铺满一边 | `设计尺寸 × min(视口宽/1920, 视口高/1080)`；1280×720 视口下缩至 **0.667 倍** | ✗ 控件变小 |
| `5` ScaleToFill | 双向铺满 | 非 16:9 时**非等比拉伸变形** | ✗ 控件变形 |
| `0` None | ✗ 不铺满（内容保持设计像素，越界被裁） | 设计尺寸原样 | ✗ 不铺满 |

⇒ **「容器是否铺满」与「控件多大」必须解耦**：

- **容器铺满** → 由**锚点拉伸**负责（`Anchors` 张开 + `Offsets` 内缩为 0）；
- **控件尺寸** → 由**固定 `Offsets`** 负责（非拉伸锚点下 `Offsets.Right/Bottom` 即宽高，单位是设计像素）。

根 `ScaleBox` 因此**不再承担适配职责**，只保留为极端分辨率下的兜底降级手段（见第五节）。

---

## 二、定位与缩放策略

### 2.1 三个决定落点的量

非拉伸锚点（`Anchors.Minimum == Anchors.Maximum`）下：

```
控件的屏幕 X = 视口宽 × Anchors.Minimum.X + Offsets.Left
控件的屏幕 Y = 视口高 × Anchors.Minimum.Y + Offsets.Top
控件的宽    = Offsets.Right
控件的高    = Offsets.Bottom
```

- `Anchors` 决定「贴在屏幕的哪个位置」，取值 `0.0`（左/上）、`0.5`（中）、`1.0`（右/下）；
- `Offsets.Left/Top` 是**相对锚点**的偏移，锚在右侧/下方时通常取负值；
- `Offsets.Right/Bottom` 是**宽高**，不是右/下边界——这是与「拉伸锚点」语义的分界点。

### 2.2 拉伸锚点（`Minimum != Maximum`）

```
左边距 = 视口宽 × Min.X + Offsets.Left
右边距 = 视口宽 × (1 − Max.X) + Offsets.Right
宽度   = 视口宽 × (Max.X − Min.X) − Offsets.Left − Offsets.Right
```

宽度随视口变化，用于「跟手」的横条/背景。四向拉伸即 `(0,0)–(1,1)` 且四边 `Offsets` 全 0。

### 2.3 `Alignment` 不可忽略

`CanvasPanelSlot.Alignment` 默认 `(0,0)`，此时 `Offsets.Left/Top` 是该**角**的坐标。若为 `(0.5,0.5)`，控件会再向左上偏移**半个自身尺寸**——新建控件的默认值即为 `(0.5,0.5)`，是「布局数据正确但画面偏移」的首要排查项。

---

## 三、分辨率适配方式：四类锚点分工

| 元素类型 | Anchors | Offsets | 分辨率变化时的表现 |
| --- | --- | --- | --- |
| 全屏背景 / 遮罩 | `(0,0)–(1,1)` | 四边 0 | 四向拉伸，始终铺满 |
| 顶栏 / 底栏 / 分隔条 | `(0,0)–(1,0)` 或 `(0,1)–(1,1)` | 左右为 0，`Top` 与高固定 | 横向铺满，**厚度不变** |
| 边角按钮组 / 信息块 | 单点锚点 `(0/1, 0/1)` | `Left/Top` 为相对偏移，`Right/Bottom` 为宽高 | 吸附对应角，**尺寸不变** |
| 居中弹窗 | `(0.5, 0.5)` | `Right/Bottom` 为宽高 | 始终居中，**尺寸不变** |

**层次建议**：根容器必须能真正吃满视口。官方默认层次是「外层画布 → 缩放框 → 尺寸框 1920×1080 → 画布」，其中尺寸框会把内容**钉死在 1920×1080**，与「跟随视口」的目标冲突——因此本方案需去掉尺寸框的固定宽高约束（或改为不重载），让内层画布直接获得视口尺寸。

> **根因与候选修法（需编辑器实测复核）**：`ScaleBox` 在 `Stretch=0` 时把子节点按**子节点的期望尺寸**摆放；`SizeBox` 重载 1920×1080 后，期望尺寸恒为 1920×1080，于是内层 `CanvasPanel` 永远拿不到视口尺寸——这才是「不铺满」的机制根因（`CanvasPanel` 自身期望尺寸为 0，去掉 SizeBox 也不会自动变大）。
>
> 因此**有效修法只有一条**：让 `CanvasPanel_0` 直接成为根控件，由视口给它尺寸。候选实现：
> 1. `WidgetTree.RootWidget = CanvasPanel_0`（`ScaleBox`/`SizeBox` 保留在树里但不参与布局，或一并删除）；
> 2. 确认 `参考图` 的四向拉伸锚点在新根下仍铺满；确认 `CanvasPanel_0` 的 43 个子控件槽位不变。
>
> 反面候选（**不采用**）：把 `ScaleBox.Stretch` 改为 `1 (Fill)` —— 非等比缩放会连同子控件一起拉伸变形，与「控件不缩放」直接冲突。

---

## 四、控件尺寸约束

1. **宽高即 `Offsets.Right/Bottom`**：这是「不缩放」的落点。改分辨率不改这两个值，控件像素尺寸就恒定。
2. **`SizeBox` 用于硬约束**：需要「至少/至多 N 像素」时使用。注意 `WidthOverride` / `HeightOverride` 受 `bOverride_WidthOverride` / `bOverride_HeightOverride` 的 EditCondition 门控，**只写数值不开开关会静默失效**，必须两阶段写（先置开关为真，再写数值）并回读四个字段。
3. **最小支持分辨率**：像素恒定的代价是小屏上控件相对占比变大。应约定一个下限（如 1280×720），低于它时控件会相互重叠，此时才启用兜底缩放。
4. **越界裁切**：贴边装饰图允许越出画布，由父容器裁掉；交互控件必须完整落在视口内。

---

## 五、横竖屏与窗口尺寸变化

1. **锚点方案自动响应**。Slate 每帧按 `Anchors + Offsets` 重排，分辨率/窗口变化**无需 Lua 参与**——这是锚点方案相对手写缩放的核心优势。
2. **严禁在 Lua 里手写 `SetRenderScale` / `SetPositionInViewport` / `SetDesiredSizeInViewport`**。这三者绕开 Slate 布局：窗口变化时不会自动跟随，且会与容器自身的缩放**叠加**，产生「整屏再缩一次」的双重缩小（本项目已实测：1280×720 下主界面只铺满 0.825）。
3. **横竖屏需要重排，锚点解决不了**。从「横排四角」变为「竖排上下堆叠」属于布局结构变化，锚点只能吸附位置、不能改变排列方式。做法：用 `WidgetSwitcher` 按视口宽高比（`vw/vh < 1`）切换两套布局页，或另做竖屏版本资产。
4. **兜底降级**：当视口小于最小支持分辨率时，才让根 `ScaleBox` 由 `Stretch=0` 切到 `2`（ScaleToFit）。切换必须同时写移动端与 PC 双字段（`Stretch`+`StretchDirection` / `StretchPc`+`StretchDirectionPc`），只写无后缀一套在 PC（PCD3D_SM5）不生效。

---

## 六、ZhuJieMian 现状对照（MCP 全量实测，43 个控件）

### 6.1 已具备的基础

- **锚点已成体系**，四角分布完整：
  - `(0,0)` 左上 10 个：`WarehouseButton`、`DressButton`、`CheckinButton`、`ShopButton`、`MailButton`、`TextBlock_133/226/287/406/469`（顶栏）；
  - `(0,1)` 左下 5 个：`头像框`、`玩家名称`、`服务器剩余时间`、`PlayerNameText`、`CountdownText`；
  - `(1,0)` 右上 14 个：`金币UI`、`金币`、`GoldValueText`、`Image_160`、`VenueNameText`、`OpenHouseButton`、`OpenPropButton`、`OpenCharacterButton`、`MatchButton`、`MatchLabel`、`PropKindText`、`PropSummaryText`、`PropTitleText`、`CharacterTitleText`；
  - `(1,1)` 右下 12 个：`每日任务`、`帮助`、`保底金`、`每日任务上方UI`、`帮助上方UI`、`保底金上方UI`、`TextBlock_533/616/715`、`OpenRewardButton`、`OpenHelpButton`、`OpenGuaranteeButton`。
- **背景层已用四向拉伸**：`参考图` 锚点 `(0,0)–(1,1)`。
- **全部 `Alignment = (0,0)`**，无「偏移半个自身尺寸」问题。

⇒ **控件侧几乎不需要改锚点**，这是本方案改动量很小的根本原因。

### 6.2 三个待处理项

| # | 现象 | 处理 |
| --- | --- | --- |
| 1 | `CanvasPanel_0_Wrapper`（SizeBox）强制 1920×1080，内容被钉死、无法跟随视口 | 去掉宽高重载（或整体移出层次），让内层画布吃满视口 |
| 2 | Lua `AuctionHubUIService.ApplyViewportFit` 手写 `SetRenderScale` / `SetPositionInViewport` / `SetDesiredSizeInViewport` | 删除三项，改由 Slate 布局负责 |
| 3 | 3 个控件越出 1920×1080 画布：`顶部UI` y[−212..311]、`金币UI` y[−56..150]、`玩家名称` y[845..1164] | 按「贴边裁切」处理（超出部分由父容器裁掉）；若设计要求完整可见，则下调高度/改锚点 |

### 6.3 落地顺序

沿用项目既有规范：先在网页预览中验证锚点行为与各分辨率下的落点，确认后再写入编辑器资产。

---

## 七、验收判据（确定性量测）

1. **铺满**：抓 PIE 客户端绘制区，用 `V_EDGE`（右侧 0.60–0.98 区间竖直边缘能量峰值列 ÷ 视口宽）度量，应 ≈ `1.0`。现状基线：`0.8250`（未铺满），`Stretch=2` 修复版为 `0.9641`。
2. **控件尺寸不缩放**：同一控件在 `1280×720` 与 `1920×1080` 两个视口下的**渲染像素尺寸应相同**。例如 `OpenRewardButton` 的设计宽高为 `140 × 130`，两个视口下都应为 140 × 130 物理像素（而非 1280 视口下变成 93 × 87）。
3. **布局合理**：任一支持分辨率下，交互控件不得互相重叠，且全部完整落在视口内。
4. **量测纪律**：`edge_corr`（归一化边缘相关系数）由 3D 场景背景主导，**不可**作为 UI 判据；PIE 启动后需等主界面渲染稳定（实测约 15 s）再量，否则首帧会落在 `0.70` 附近造成误判。

---

## 八、方案预览页（写入资产前的确认件）

路径：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_主界面自适应方案\ZhuJieMianAdaptivePreview.html`

- **数据源为实测**：43 个控件的 `Anchors` / `Offsets` / `Alignment` 由 UGCAskQ 只读导出，页面内按 2.1 的布点公式复算，非示意图。
- **三态对照**：`A 现状（Stretch=0 + Lua 手写缩放）` / `B 仅改 Stretch=2` / `C 本方案（锚点填充 + 固定像素）`。
- **七档视口**：1920×1080、2560×1440、1600×900、1366×768、1280×720、1024×768、竖屏 1080×1920。
- **深链**：`#vp=1280x720&mode=C`、`#vp=1080x1920&mode=C` 可直接定位。
- 已用无头 Chrome 逐档校验：**数量与几何均与实测一致**（43 个控件全部落位）。

**校验输出（`OpenRewardButton`，设计尺寸 140 × 130）**：

| 视口 | A 现状 | B Stretch=2 | C 本方案 |
| --- | --- | --- | --- |
| 1920 × 1080 | 116 × 108 | 140 × 130 | **140 × 130** |
| 1280 × 720 | 77 × 72 | 93 × 87 | **140 × 130** |
| 竖屏 1080 × 1920 | 65 × 61 | 79 × 73 | **140 × 130** |

⇒ 方案 C 在任何视口下都保持 140 × 130 物理像素，「控件不缩放」可量化验收；A / B 两态则随视口线性缩小。

同批校验得到的视口占比：A = 82.8%（不铺满，四周留空）；B = 宽方向铺满、另一方向留黑边（等比）；C = 100%（铺满）。

---

## 九、2026-09-15 实测定稿：根因不是 Stretch，而是「像素 vs Slate 布局单位」的混用（★本项目实测）

> 本节**推翻**第三节 +75 / 第五节 ·2 中的推断。原推断认为「根 ScaleBox/SizeBox 把内容钉死在 1920×1080」是不铺满的机制；实测表明真正的机制是 `SetDesiredSizeInViewport` 被喂了**窗口像素**，而它吃的是 **Slate 布局单位**。
> 证据等级：官方确认（API 语义，见 `docs/api/class/Others/UUserWidget.md`、`UGCWidgetManagerSystem.md`）+ 本项目实测（运行时日志 + PIE 客户端像素量测）。

### 9.1 单位真相（三条硬数据）

| API | 单位 | 1280×720 窗口实测值 |
| --- | --- | --- |
| `UGCWidgetManagerSystem.GetViewportSize()` | **窗口像素** | `1280.0 × 720.0` |
| `UGCWidgetManagerSystem.GetViewportScale()` | 布局单位 → 像素 的比例 | `0.826` |
| `GetLocalSize(GetViewportWidgetGeometry())` | **Slate 布局单位** | `1549.64 × 871.67` |

- 校验：`1549.64 × 0.826 = 1280`、`871.67 × 0.826 = 720` —— 精确吻合；
- 换算倍率：`1 / 0.826 ≈ 1.211`（**本机值**，随 DpiScale 变化，不可写死）；
- 把像素直接喂给 `SetDesiredSizeInViewport` → 画布只有 `1056 × 594`，也就是**只占视口 0.825** —— 这正是历史现象「主界面只铺满 0.825」的全部机制，与设计基准、锚点、`Stretch` 都无关。

### 9.2 两条反面尝试（实测无效，勿再试）

1. **`SetAnchorsInViewport` 写成四向拉伸 `Minimum=(0,0) / Maximum=(1,1)`** → 仍是 0.825。原因：`AddToViewport` 的槽位由 `UGCWidgetManagerSystem` 托管，Lua 侧读 `widget.Slot` 为 `nil`、也无 `GetCachedGeometry`，**锚点改动落不到实际槽位上**。
2. **完全不调 `SetDesiredSizeInViewport`** → 依赖「`AddToViewport` 默认铺满」不可靠：一旦该 widget 曾被写入过 DesiredSize，同实例内不会被自动撤销，且 `Refresh` 的去重键会把它锁住。

⇒ 结论：**显式写，且写对单位**才是唯一可靠路径。这也是对第五节 ·2「严禁手写 `SetDesiredSizeInViewport`」的修正——可以写，但只能写**布局单位**；`SetRenderScale` 仍固定写 `1`，不参与适配。

### 9.3 最终实现（`Script/Function/AuctionHubUIService.lua`，mode = `LayoutUnitsFill`）

```
ReadViewportLayoutSize()                                  -- 新增，取布局单位
  ① GetLocalSize(GetViewportWidgetGeometry())             -- 首选（官方，Slate 单位）
  ② 回退 GetViewportScale()：像素 ÷ scale                 -- 次选
  ③ 再回退：像素（明知会缩，可观测而不静默失败）
↓
ApplyViewportFit()
  SetAnchorsInViewport   Minimum=(0,0) Maximum=(0,0)      -- 非拉伸锚点：DesiredSize 即字面尺寸
  SetAlignmentInViewport (0,0)
  SetPositionInViewport  (0,0), true
  SetRenderScale         (1,1)                            -- 恒 1，不做适配
  SetDesiredSizeInViewport(layoutWidth, layoutHeight)     -- ★布局单位
  去重键 = 策略版本 + round(布局单位尺寸)                 -- 几何滞后时下一次 Refresh 自纠正
```

配套：`ZhuJieMian.uasset` 已把包裹层（`ScaleBox → SizeBox 1920×1080`）解包，`CanvasPanel_0` 直挂为 `WidgetTree.RootWidget`（运行时 `root=CanvasPanel_0`，44 个控件），保证 Lua 写的画布尺寸**直达承载所有控件的画布**。

### 9.4 验收数据（PIE 客户端客户区抓图 + 金色主色 `~ (245,163,59)` 像素剖面）

| 视口（客户区） | 金色像素右缘占比 | 金色像素下缘占比 | 判据 |
| --- | --- | --- | --- |
| 1280 × 720 | 0.9781 | **0.9986** | 铺满 ✓ |
| 1600 × 900 | 0.9781 | **0.9989** | 铺满 ✓ |
| 1920 × 1000 | 0.9812 | **0.9920** | 铺满 ✓ |
| 历史基线（喂像素） | 0.8250 | 0.8250 | 不铺满 ✗ |

- 右缘稳定在 `0.978` 而非 1.0：最右侧金色装饰自身带约 2% 设计边距，**不是**没铺满；
- 运行时日志无报错，`LayoutUnitsFill` 每档视口各写入 1 次，去重键命中 69 次（不逐秒抖动）；
- `1920×1000` 时 `layout=2560×1333`，宽高比 1.92 与视口一致 ✓。

### 9.5 两个量测陷阱（务必规避）

1. **窗口必须整个落在屏幕内**：本机 `SM_CYSCREEN=1080` 但 `SM_CYFULLSCREEN=1009`。把 PIE 客户区调到 `1920×1080` 时，下部 84 px 跑到屏外，截图底部 16 行**纯黑**、下缘假读成 `0.9222`，极易误判为「没铺满」。最大可用客户区高度为 **1009**；脚本应固定窗口到左上角并增加「底部 16 行纯黑占比」自检项。
2. **别匹配错窗口**：`find_pie()` 必须按标题含 `PIEPlayer` 定位真实 PIE 客户端；按 `ShadowTrackerExtra` 会命中编辑器主窗（`1936×1048 @ -8,-8`），得到的是无关画面（历史上曾据此得出错误的「顶栏宽=303」）。

### 9.6 遗留说明

- `参考图`、`OpenRewardButton` 等控件的渲染像素是否跨视口恒定，本次**未**用控件级几何复测；三档截图的结构栅格几乎重合，说明观感比例稳定，但「控件原尺寸」的严格验收仍建议补一次控件级量测（成本：读取 `GetCachedGeometry`，Lua 侧当前不可用，需另找通道）。

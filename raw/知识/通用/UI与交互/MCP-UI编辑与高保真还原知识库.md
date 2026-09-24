# MCP UI 编辑与高保真还原知识库

> 来源：[2026-08-26 UGCAskQ MCP 编辑器修改能力实测](../来源记录/2026-08-26_UGCAskQ_MCP实测记录.md)、[2026-08-26 UI 画刷与控件样式官方查证](../来源记录/2026-08-26_UI画刷与样式官方查证.md)、[2026-08-26 图鉴 UI 优化](../来源记录/2026-08-26_图鉴UI优化.md)、[2026-08-26 UI 资产修正与画刷基线导出](../来源记录/2026-08-26_UI资产修正与画刷基线导出.md)、项目证据：[IslandAuctionKing UI 贴图批量修正 MCP 回读](../../../IslandAuctionKing/日志证据/2026-08-26_UI贴图批量修正MCP回读.md)、`raw/docs/ai/20260824_图鉴UI素材批量导入与视觉优化.md`、项目实战产物 `<IslandAuctionKing>/Preview/CollectibleCodexReferencePreview.html`、`<IslandAuctionKing>/docs/Settlement_UI_Progressive_Display_Standards.md`
> 官方依据：`raw/docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md`、`raw/docs/wiki/进阶内容/UI系统/357_异形屏适配.md`、`raw/docs/api/class/Others/UScaleBox.md`、`raw/docs/api/class/Others/USizeBox.md`、`raw/docs/api/class/Others/UTextLayoutWidget.md`、`raw/docs/api/class/Others/UTextBlock.md`、`raw/docs/api/class/Others/UWidget.md`、`raw/docs/wiki/新手入门/资源管理与编辑/277_资源导入.md`、`raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md`、`raw/docs/api/cppstruct/F/FS/FSlateBrush.md`、`raw/docs/api/cppstruct/F/FB/FButtonStyle.md`、`raw/docs/api/cppstruct/F/FS/FSlateFontInfo.md`、`raw/docs/api/cppenum/`（画刷/裁剪/拉伸/贴图组枚举）
> 枚举与结构体整数值速查：[绿洲 UI 枚举与结构体速查](绿洲UI枚举与结构体速查.md)（2026-08-26 已用 `ue_read enum:` / `schema:?level=full` 与官方 md 双向核对）
> 社区依据：sq-skill 归档帖 2233（技能自带归档 `<CODEX_HOME>/skills/sq-skill/docs/community/replies/2233.md`，不在本仓库 `raw/` 下；官方「绿洲启妹」答复 iOS 两侧安全区由引擎层处理，开发者用标准缩放自适应方案覆盖其余适配）；sq-skill 归档帖 2193（`<CODEX_HOME>/skills/sq-skill/docs/community/replies/2193.md`，ScrollBox / WrapBox 等容器的子控件必须通过 `AddChild` 挂入，直接改 `Slot` 或子控件数组无效）
> 适用场景：本项目 UI 交付链路是**网页预览 → 用户确认"预览没问题" → UGCAskQ MCP 写入 UMG → 回读核对**。本页因此按"双轨"组织：Web 侧 CSS/HTML 规范与绿洲 UMG 侧对应物一一对齐。

---

## 一、核心结论：核心设计原则 (Core Principles)

1. **双轨等价原则**：网页预览不是草图，而是 UMG 的等价描述。预览里每一个可测量量（颜色、间距、圆角、字号、行高、容器尺寸）都必须能映射到 UMG 的具体属性或 `CanvasPanelSlot` 调用，否则该视觉决策无法落地，属于无效预览。
2. **固定设计基准 + 弹性呈现**：设计基准锁定 1920×1080（16:9），与官方 `20269_UI自适应屏幕.md` 的尺寸框重载值一致；呈现层一律用比例/弹性单位，禁止把基准像素直接当成呈现像素。
3. **容器负责边界，内容负责流动**：任何可能装载未知长度内容的容器，必须先声明自己的最大边界（`max-width` / `SizeBox` 的 `MaxDesiredWidth`），再让内部内容换行、截断或滚动。顺序反了就必然溢出。
4. **零 Magic Number**：颜色进 CSS 变量、UMG 侧进配置表（`Asset/Data/Table/Customized/UI/UIConfigTable`），尺寸坐标不得硬编码在 Lua 里。参见 [配置表驱动开发](../配置与数据/配置表驱动开发.md)。
5. **写入即回读**：MCP 多个写入 API 成功时返回 `None`，不能以"没报错"判定成功；UI 结构改动后必须 `widget_inspect` 回读树与 Pos/Size。参见 [UGCAskQ MCP 实测陷阱清单](../工具与流程/UGCAskQ-MCP实测陷阱清单.md)。
6. **文本优先做最坏假设**：所有文本控件按"最长可能内容 + 最大字号 + 最窄屏幕"三重最坏情况设计，而不是按示例文案设计。
7. **重复槽位以一格示例为全族模板**：用户只框一格并写“其余按这个示例”时，写入对象是整个同名序号控件族。按相对父卡偏移复制，并分开验收图片、点击、文本、叠加四层。详见 [绿洲编辑器控件位置与尺寸准确性](./绿洲编辑器控件位置与尺寸准确性.md)。

---

## 二、技术规范与最佳实践 (Technical Specifications)

### 1. 视觉高保真还原

**规范要点**

- **颜色系统必须变量化**：所有颜色集中声明在 `:root`，组件内只引用变量，禁止在组件里写裸 hex。UMG 侧同一色值以 `FLinearColor` 归一化分量登记进配置表（如金橙 `#FF9C2B` = `{R=1.00,G=0.62,B=0.16,A=1.00}`，未选深灰 `#2B2D31` = `{R=0.18,G=0.20,B=0.22,A=1.00}`，出自 `raw/docs/ai/20260824_图鉴UI素材批量导入与视觉优化.md`）。
- **间距栅格化**：间距只允许取 4px 基数栅格（4/8/12/16/24/32），用 `--sp-1 … --sp-8` 变量表达；UMG 侧对应 `FMargin`（`UTextLayoutWidget.Margin`）与 Slot 的 Offsets。
- **圆角与阴影同样 token 化**：`--radius-sm/md/lg`、`--shadow-1/2`。UMG 侧文本阴影用 `UTextBlock.ShadowOffset` + `ShadowColorAndOpacity`（`SetShadowOffset` / `SetShadowColorAndOpacity`），阴影不透明度为 0 时不绘制。
- **组件化思维**：同类卡片/按钮抽成一个 class（UMG 侧抽成独立 WidgetBlueprint，如本项目 `CollectibleCodexItemUI` 作为 `CollectibleCodexUI` 的条目组件），改一处生效全局。
- **贴图属性统一（官方出处已确认）**：UI 贴图按 `raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md` 第 2 节「UI贴图设置」配置 —— `Texture Group = TEXTUREGROUP_UI (LODGroup=16)`、`Mip Gen Settings = TMGS_NoMipmaps (MipGenSettings=13)`、`Compression Quality = TCQ_Highest (CompressionQuality=5)`、`Compression Settings = TC_Default (CompressionSettings=0)`、`SRGB=True`，否则 UI 会出现糊图或多余 Mip 采样。
  > **订正**：`raw/docs/ai/20260824_图鉴UI素材批量导入与视觉优化.md` 第 12 行把 `TMGS_NoMipmaps` 记为 `MipGenSettings=2`，**该整数值有误**——`2` 实为 `TMGS_Sharpen0`，`TMGS_NoMipmaps` 是 **13**（`raw/docs/api/cppenum/T/TE/TextureMipGenSettings.md` 与编辑器反射一致）。`raw/` 为只读原始资料不作改动，以本页为准。实测项目内 `Codex_*` 系列贴图确为 `MipGen=13`，命名与语义无误，仅原记录的数字标注错误。
  > **导入不会自动归 UI 组**：实测本项目 `Asset/TuPian/ZhuJieMian/ZJM1–ZJM11` 全部落在 `LODGroup=0 (TEXTUREGROUP_World)`，`ZJM8` 的 `MipGenSettings` 还是 `0 (FromTextureGroup)`，`TuJian/Codex_*` 12 张的 `CompressionQuality` 全为 `0 (TCQ_Default)`。2026-08-26 已分三批走 MCP Resolve → Plan → Execute 全部修正，23 张跨对象回读 `ALL_23_COMPLIANT=True`（五项全为 `16/13/0/5/True`）。**新贴图导入后必须立刻按五项核查**，不要指望默认值正确。导入格式与目录规则见 [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)，before/after 见 [ZhuJieMian 画刷现状基线表](ZhuJieMian画刷现状基线表.md)。

**代码示例 / 最佳实践（Web 侧）**

```css
:root{
  /* 色板：与 UMG 配置表一一对应 */
  --bg:#f2f0ec; --panel:#575757; --panel-deep:#25282a; --panel-mid:#3f4142;
  --accent:#f5a33b; --accent-hi:#ffb847; --line:#1c2021;
  --text:#f5f5f2; --muted:#bec1c1;
  /* 间距栅格 */
  --sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-6:24px; --sp-8:32px;
  /* 圆角与阴影 */
  --radius-sm:4px; --radius-md:8px; --radius-lg:14px;
  --shadow-1:0 1px 2px rgb(0 0 0 / .18);
  --shadow-2:0 6px 18px rgb(0 0 0 / .28);
}
.card{ background:var(--panel-mid); border:1px solid var(--line);
       border-radius:var(--radius-md); padding:var(--sp-3); box-shadow:var(--shadow-1); }
```

**代码示例 / 最佳实践（UMG 侧，MCP 写入）**

```python
import unreal_engine as ue
from unreal_engine.classes import Blueprint
from unreal_engine.structs import FVector2D

wbp = ue.load_object(Blueprint, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexUI')
w = [c for c in wbp.WidgetTree.AllWidgets if c.get_name() == 'ItemTitle'][0]
# 坐标与尺寸必须走 UFunction，widget_slot 写不进 Position/Size
w.Slot.SetPosition(FVector2D(40, 300))
w.Slot.SetSize(FVector2D(260, 40))
ue.compile_blueprint(wbp)
wbp.save_package()
# 回读核对
ue.log(ue.widget_inspect(wbp, 'ItemTitle'))
```

> `widget_slot` 实测**只支持 `ZOrder` / `bAutoSize`**，`Position` / `Offsets` / `Anchors` / `Alignment` 全部写入失败；`CanvasPanelSlot` 可编辑属性只有 `LayoutData`(FAnchorData: Offsets/Anchors/Alignment) / `bAutoSize` / `ZOrder` / `bAntiAdaptation`，其余必须调 `SetPosition/SetSize/SetAnchors/SetAlignment/SetOffsets/SetZOrder/SetAutoSize/SetAntiAdaptation`。

---

### 2. 多端自适应适配

**规范要点**

- **绿洲 UMG 侧唯一标准层次结构**（官方 `20269_UI自适应屏幕.md`，由外到内）：
  `画布面板 → 缩放框(ScaleBox) → 尺寸框(SizeBox) → 画布面板 → 业务控件`。
  包裹顺序是：画布面板 →包裹→ 尺寸框 →包裹→ 缩放框 →包裹→ 画布面板。
  参数：缩放框 `锚点=四向拉伸`，偏移左/顶/右/底全部 = 0；尺寸框 `宽度重载=1920`、`高度重载=1080`；内层画布面板 `水平对齐=水平对齐填充`、`垂直对齐=垂直居中填充`。
  - **居中型控件**（道具弹窗等不贴边）：尺寸框 `水平对齐=水平对齐居中`、`垂直对齐=垂直居中对齐`。
  - **贴边型控件**（按钮贴边）：尺寸框 `水平对齐=水平右对齐`、`垂直对齐=垂直居中对齐`。
  本项目 `AuctionTestUI` 实测控件树根即 `ScaleBox_0 → SizeBox_0 → CanvasPanel_0 → …`，说明该方案已落地，新建 UI 必须沿用。
- **异形屏**：调整层次结构后在 `Construct` 调用（`AdaptionPanel` 需勾选 `Is Variable`）：
  `UICommonFunctionLibrary.SetAdaptation(self.AdaptionPanel, self)`；官方注意事项是**所有主 UI 都要适配一遍**。iOS 两侧安全区由引擎层已处理（社区帖 2233 官方答复），开发者只需保证标准缩放结构正确。
- **`UICommonFunctionLibrary` 的真实身份（已查证）**：它**不是 C++ 类**，而是引擎侧蓝图函数库 `BlueprintGeneratedClass /Game/UMG/UI_BP/Common/UICommonFunctionLibrary.UICommonFunctionLibrary_C`，因此 `raw/docs/api` 里没有独立类文档，MCP 侧 `ue.find_class('UICommonFunctionLibrary')` 也查不到。实测定位与签名提取方式见 [UGCAskQ MCP 实测陷阱清单](../工具与流程/UGCAskQ-MCP实测陷阱清单.md)。共 14 个函数，其中适配相关 9 个（`__WorldContext` 为蓝图库隐式世界上下文，Lua 调用时传 `self`）：
  | 函数 | 参数 | 用途推断 |
  | --- | --- | --- |
  | `SetAdaptation` | `Widget`, `__WorldContext` | 官方异形屏适配入口，`357_异形屏适配.md` 唯一示例 |
  | `SetUnAdaptation` | `Widget`, `__WorldContext` | 取消适配 |
  | `SetAdaptation_ScreenHole` | `widget`（小写 w）, `__WorldContext` | 挖孔屏适配 |
  | `SetAdaptation_Lobby` | `Widget`, `__WorldContext` | 大厅适配 |
  | `SetAdaptation_Lobby_IPX` | `Widget`, `__WorldContext` | 大厅 iPhone X 类机型适配 |
  | `SetAndroidPhoneAdaptation` | `Panel`, `__WorldContext` | 安卓机型适配（参数名是 `Panel`） |
  | `GetUIRectOffset_WithSetting` | `__WorldContext`, `RealOffset`(输出) | 取安全区偏移量 |
  | `SetSquareFixedScslr` | `Widget`, `__WorldContext` | 方屏固定缩放 |
  | `SetTabStyle` | `isCheck`, `Text`, `icon`, `onColor`, `offColor`, `__WorldContext` | 页签选中/未选中样式切换 |
  只有 `SetAdaptation` 有官方 Wiki 示例，其余 8 个仅确认了签名，**语义属推断，未经 PIE 验证**（见「待查证」）。
- **`CanvasPanelSlot.bAntiAdaptation` 中文名是「贴边反适配」**（编辑器反射 DisplayName，Category `Layout|Canvas Slot`，`BlueprintReadOnly`）。它与官方异形屏方案的配合关系仍无文档说明，改动前先在 PIE 对比。
- **`UScaleBox` 有两套并行缩放字段**：`Stretch/StretchDirection/UserSpecifiedScale/UserSpecifiedScaleBias/IgnoreInheritedScale`（Category `Stretching`）与后缀 `Pc` 的同名字段（Category `StretchingPC`）。只改无后缀的一套，PC 端可能仍走 `*Pc`，多端表现会不一致。`UserSpecifiedScale` 官方注明仅在 `Stretch=UserSpecified(7)` 时生效。`EStretch` 含 `ScaleBySafeZone(6)`，与安全区相关，具体行为见「待查证」。
- **Web 侧强制流式布局**：主布局用 Flexbox / CSS Grid，绝对定位只用于装饰性徽标、角标等脱离文档流且不影响可读性的元素。禁止用绝对定位堆叠主内容——那是 UMG 画布思维带进网页的常见错误，一旦缩放就重叠。
- **标准断点**（移动优先）：`≥480px` 大屏手机、`≥768px` 平板、`≥1024px` 桌面、`≥1440px` 宽屏。断点只用来改**列数与方向**，不用来堆叠一整套新样式。
- **弹性单位优先级**：`clamp()` > `min()/max()` > `%`/`fr` > `rem` > `vw/vh` > 固定 `px`。固定 px 只允许用于 1px 描边、图标尺寸、`min-height:44px` 这类不应缩放的量。
- **触控可用性**：可点区域最小 44×44px，相邻触控目标间距 ≥8px（ui-ux-pro-max Touch 规则，Severity High）。UMG 侧按钮 Slot 尺寸换算到设计基准 1920×1080 后不得小于等效 44px。

**代码示例 / 最佳实践**

```css
/* 舞台：锁定设计宽高比，但宽度弹性——等价于 UMG 的 ScaleBox+SizeBox */
.stage{ width:min(1280px, 96vw); aspect-ratio:16/9; margin-inline:auto; }

/* 流式网格：列数随屏宽自适应，无需断点 */
.gallery{
  display:grid; gap:var(--sp-3);
  grid-template-columns:repeat(auto-fill, minmax(min(220px,100%), 1fr));
}

/* 字号弹性：最小 14px，最大 20px，随视口平滑变化 */
.title{ font-size:clamp(14px, 1.2vw + 8px, 20px); }

/* 断点只改结构方向 */
.panel{ display:flex; flex-direction:column; gap:var(--sp-3); }
@media (min-width:768px){ .panel{ flex-direction:row; } }
@media (min-width:1024px){ .gallery{ gap:var(--sp-4); } }
```

> `minmax(min(220px,100%), 1fr)` 是防溢出关键写法：单列宽度不足 220px 时退化为 100%，避免 `minmax(220px,1fr)` 在 320px 窄屏顶出横向滚动条。

---

### 3. 防溢出与边界控制

**规范要点**

- **全局盒模型**：`*, *::before, *::after { box-sizing:border-box; }`。这是 padding/border 不撑破 `width:100%` 的前提。
- **根级兜底**：`html, body { max-width:100%; overflow-x:hidden; }`，同时**禁止对 body 或主容器设 `min-width`**。本项目预览页 `CollectibleCodexReferencePreview.html` 里的 `body{min-width:920px}` 就是反例，窄屏必现横向滚动条。
- **媒体资源**：`img, video, canvas, svg { max-width:100%; height:auto; display:block; }`。
- **Flex / Grid 子项必须显式 `min-width:0`**（纵向布局用 `min-height:0`）。Flex 子项默认 `min-width:auto`，内部长文本会把容器顶宽，这是"控件被挤压变形 / 横向溢出"的头号原因。
- **overflow 使用场景界定**：
  - `overflow:hidden`：用于**已知固定尺寸**的装饰容器（卡片图片区、渐变遮罩），且已确认无内容需要被看到。
  - `overflow-y:auto` + 明确高度约束（`max-height` / `min-height:0` / `flex:1`）：用于列表滚动区。没有高度约束的 `overflow-y:auto` 等于没写。
  - `overflow-x:auto`：仅表格类必须保留横向浏览的内容使用，并包在独立 wrapper 上，不要挂到页面根。
  - **禁止**在同一滚动方向上嵌套两层滚动容器，会产生双滚动条与滚动劫持。
- **UMG 侧对应物**：
  - 硬边界用 `SizeBox` 的 `WidthOverride/HeightOverride`（需同时置 `bOverride_WidthOverride`/`bOverride_HeightOverride`），弹性边界用 `MinDesiredWidth/MaxDesiredWidth/MinDesiredHeight/MaxDesiredHeight`。
  - 裁剪用 `UWidget.Clipping`（`SetClipping`）。官方枚举 ToolTip 明确：**Slate 无法跨裁剪区合批**，两个开了裁剪的控件树内部绘制永不合批，会增加 GPU 开销。按用途选值，不要一律 `ClipToBounds`：
    | 值 | 名称 | 适用 |
    | --- | --- | --- |
    | 0 | `Inherit` | 默认，不裁剪，继承祖先裁剪区 |
    | 1 | `ClipToBounds` | 裁剪到自身边界并与已有裁剪区求交 |
    | 2 | `ClipToBoundsWithoutIntersecting` | 不求交、压入新裁剪状态，可渲染到会裁剪的父级之外（仍无法忽略 `Always`） |
    | 3 | `ClipToBoundsAlways` | 不可被忽略的硬边界，适合「动画/特效绝不允许越界」的区域 |
    | 4 | `OnDemand` | 仅当期望尺寸大于分配尺寸时才裁剪；**官方注明此模式主要为文本添加**，避免给每个可能装文本的容器都强开裁剪而毁掉合批 |
    → **文本溢出优先用 `OnDemand(4)`**，硬边界用 `ClipToBoundsAlways(3)`，`ClipToBoundsWithoutIntersecting(2)` 仅用于需要故意画到父级之外的浮层。
  - 内容缩放适配用 `ScaleBox` 的 `Stretch`（`None(0)/Fill(1)/ScaleToFit(2)/ScaleToFitX(3)/ScaleToFitY(4)/ScaleToFill(5)/ScaleBySafeZone(6)/UserSpecified(7)`）与 `StretchDirection`（`Both(0)/DownOnly(1)/UpOnly(2)`）。`UserSpecifiedScale` 官方注明**仅在 `UserSpecified(7)` 下生效**；`IgnoreInheritedScale` 会对父级缩放取逆再应用本地缩放。注意还有一套 `*Pc` 字段（`StretchPc` 等）单独控制 PC 端，改缩放行为必须两套一起核对。
  - 列表用 ScrollBox，不要用绝对定位模拟滚动条（预览页 `.scroll` 的做法只适合静态示意，不可作为 UMG 实现依据）。

**代码示例 / 最佳实践**

```css
*,*::before,*::after{ box-sizing:border-box; }
html,body{ max-width:100%; overflow-x:hidden; margin:0; }
img,video,svg,canvas{ max-width:100%; height:auto; display:block; }

/* Grid 单元防挤压三件套 */
.grid{ display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:var(--sp-3); }
.grid > *{ min-width:0; }

/* 可滚动列表：高度必须被约束 */
.list-wrap{ display:flex; flex-direction:column; min-height:0; flex:1; }
.list{ flex:1; min-height:0; overflow-y:auto; overscroll-behavior:contain; }
```

```python
# UMG：给容器加硬边界并开启裁剪
sb = [c for c in wbp.WidgetTree.AllWidgets if c.get_name() == 'ContentSizeBox'][0]
sb.SetWidthOverride(677.0)
sb.SetHeightOverride(276.0)
sb.SetClipping(3)   # EWidgetClipping.ClipToBoundsAlways：不可忽略的硬边界；文本类改用 4 (OnDemand)
ue.compile_blueprint(wbp); wbp.save_package()
```

---

### 4. 文本安全排版

**规范要点**

- **编码**：HTML 首行 `<meta charset="UTF-8">` 必须在任何文本内容之前；文件本身保存为 **UTF-8 无 BOM**。中文乱码九成来自"文件编码非 UTF-8"或"charset 声明晚于内容"，不是字体问题。
- **字体族与 fallback**：中文场景使用 `"Microsoft YaHei", "PingFang SC", "Noto Sans SC", Arial, sans-serif`；数字/货币符号密集处避免只依赖单一字体，`￥` 在部分字体缺字会显示为方框。
- **行高**：正文 `line-height:1.5`（ui-ux-pro-max Typography 规则建议 1.5–1.75）。**禁止 `line-height:1` 或 `normal` 用于多行文本**——字号被 `clamp()` 放大后立刻重叠。单行截断元素可用固定 px 行高（预览页 `.card-title{line-height:17px}` 属正确用法，因为已配合 `nowrap+ellipsis`）。
- **折行控制三选一，不可混用**：
  - 需要完整展示 → `white-space:normal; overflow-wrap:anywhere; word-break:break-word;`
  - 需要单行截断 → `overflow:hidden; white-space:nowrap; text-overflow:ellipsis;`（父级必须有确定宽度或 `min-width:0`）
  - 需要多行截断 → `display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;`
- **行长**：正文单行 65–75 字符，用 `max-width:60ch` 之类约束，避免宽屏满屏文字。
- **对比度**：正文对背景对比度 ≥4.5:1，禁止灰字叠灰底。
- **UMG 侧对应物**（`UTextLayoutWidget` / `UTextBlock`）：
  | 需求 | UMG 属性 |
  | --- | --- |
  | 自动换行 | `AutoWrapText = true` |
  | 指定换行宽度 | `WrapTextAt = <宽度>`（≤0 表示不换行） |
  | 换行策略 | `WrappingPolicy`（`ETextWrappingPolicy`：`DefaultWrapping=0` / `AllowPerCharacterWrapping=1`，长串英文数字用 `1`，等价于 Web 的 `overflow-wrap:anywhere`） |
  | 行高缩放 | `LineHeightPercentage` |
  | 单行省略号 | `UTextBlock.AutoEllipsisText = true` |
  | 多行省略号 | `MutiEllipsisText = true` + `MutiEllipsisLine = <行数>`（**`MutiEllipsisLine` 的 EditCondition 是 `MutiEllipsisText`，必须先置 True 再写行数**，见下方两遍写入模式） |
  | 最小宽度 | `MinDesiredWidth` / `SetMinDesiredWidth` |
  | 水平/垂直对齐 | `Justification` / `VerticalJustification`，溢出时垂直对齐 `bNeedVerticalJustificationWhenOverflow` |
  | 内边距 | `Margin`（`FMargin`） |
- **字号不要靠放大解决（官方硬约束）**：`FSlateFontInfo.Size` 的官方 ToolTip 直接给出中文警告——「手机端无法渲染过大的字体图集，且出于内存考虑也不宜将字体设置过大。若有大字体需求，请用小字体+调整 Scale 的方案。See MAXFONTSIZE」。因此 UMG 侧放大标题必须走 `ScaleBox` / `RenderTransform` 缩放，而不是把 `Size` 调大。字号以磅计量，磅→Slate 单位换算在 **96 dpi** 下完成，用 Photoshop 出稿要把默认 72 dpi 改成 96 dpi，否则预览与实机字号不一致。
- **字体描边**用 `FSlateFontInfo.OutlineSettings`（`FFontOutlineSettings`：`OutlineSize` / `OutlineMaterial` / `OutlineColor` / `bSeparateFillAlpha`），官方注明 `OutlineSize` 在 1.0 字体缩放下单位即像素；这是描边而非 Web 的 `text-shadow`，与 `UTextBlock.ShadowOffset` 是两套机制。
- **本项目文本格式硬约束**（`<IslandAuctionKing>/docs/Settlement_UI_Progressive_Display_Standards.md`）：结算文案统一 `"标签 ￥数值"` 格式（"估值"与"￥"之间一个空格），**禁止使用 `\n` 换行符**，标签与数值必须同行。换行需求一律通过 UMG 的 `AutoWrapText` / 多控件布局实现，不靠字符串里塞 `\n`。

**代码示例 / 最佳实践**

```html
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body{ font-family:"Microsoft YaHei","PingFang SC","Noto Sans SC",Arial,sans-serif;
        font-size:16px; line-height:1.5; }
  .prose{ max-width:60ch; overflow-wrap:anywhere; word-break:break-word; }
  .one-line{ min-width:0; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; }
  .two-line{ display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
</style>
</head>
```

```python
# UMG：长文本安全设置
txt = [c for c in wbp.WidgetTree.AllWidgets if c.get_name() == 'DescText'][0]
txt.AutoWrapText = True
txt.WrapTextAt = 640.0
txt.LineHeightPercentage = 1.2
txt.AutoEllipsisText = False
ue.compile_blueprint(wbp); wbp.save_package()
ue.log(ue.widget_inspect(wbp, 'DescText'))
```

---

### 5. 画刷与控件样式（FSlateBrush / FButtonStyle）

> 本节全部结论来自 2026-08-26 在 `IslandAuctionKing` 一次性副本（`MCPBrushProbe` / `MCPStyleProbe`）上的真实写入实测，均已「编译 → 保存 → 跨对象重新加载」回读验证并删除副本，生产资产未被改动。

**规范要点：改样式改的是「画刷」，不是「画刷图像」**

编辑器细节面板的 Appearance 下有两个容易混淆的入口：

| 面板显示 | 真实属性 | 作用 | 该不该改 |
| --- | --- | --- | --- |
| 画刷 图像 | `UImage.BrushImage`（`UObject*`，Category `Appearance`，**仅 `Edit`，无 ToolTip，非 BlueprintVisible**） | 项目自定义的图像引用字段，实测不参与 `FSlateBrush` 的渲染配置 | ❌ 改它不改变样式 |
| 画刷（展开后有 图片/源命名/图像大小/着色/绘制为/平铺） | `UImage.Brush`（`FSlateBrush`，Category `Appearance`，官方 ToolTip **`Image to draw`**） | Slate 真正用于渲染的画刷 | ✅ **改这里** |

> 判据来自编辑器反射（`schema:UImage?level=full&filter=Brush,BrushImage`）：只有 `Brush` 带官方 ToolTip「Image to draw」并展开为 `SlateBrush { FVector2D ImageSize, FMargin Margin, FSlateColor TintColor, ... }`；`BrushImage` 无任何官方描述。同 Category 下还有 `BrushMaterialParamNames`（DisplayName `Material Paramters`），官方 ToolTip：「可被皮肤覆盖的材质参数名(多参数可用|分隔，皮肤上修改的话要一一对应，该功能暂时只支持 PC 上的 Float 参数修改，有需要再另外添加)」——即**材质参数的皮肤覆盖当前只在 PC 端生效且仅限 Float**，移动端不要依赖。

- **Image 控件改样式** → 写 `Image.Brush.*`（`ResourceObject` / `ImageSize` / `TintColor` / `Margin` / `DrawAs` / `Tiling` / `Mirroring`）。
- **Button 控件改样式** → 写 `Button.WidgetStyle`（`FButtonStyle`）下的**四态画刷**，对应面板中文名：
  | 面板中文 | 字段 | 触发时机 |
  | --- | --- | --- |
  | 法线 | `Normal` | 常态 |
  | 已悬停 | `Hovered` | 鼠标悬停 |
  | 已按下 | `Pressed` | 按下持续状态 |
  | 已禁用 | `Disabled` | `bIsEnabled=false` |
  `FButtonStyle` 官方字段（`raw/docs/api/cppstruct/F/FB/FButtonStyle.md`，官方描述「Represents the appearance of an SButton」）：`Normal / Hovered / Pressed / Disabled / NormalPadding / PressedPadding / PressedSlateSound / HoveredSlateSound` + 两个已废弃 `FName`（`PressedSound_DEPRECATED` / `HoveredSound_DEPRECATED`）。四态各自是一个独立完整的 `FSlateBrush`，**必须四态分别设置**。
  官方 ToolTip 给出的两条硬结论：
  - **`Disabled` 默认被设为无效资源，此时引擎使用默认禁用绘制**。所以「不设 `Disabled`」不等于「禁用时保持常态图」，而是回落到引擎默认样式，视觉必然突变——这正是「只设 Normal」踩坑的根因。
  - `NormalPadding` 是用于抵消按钮背景图边框的内边距，应用后内容与边框齐平，**未按下时使用**；`PressedPadding` 同义但**按下时使用**，用于让内容跟随按钮边框图的「位移」。两者配合才有按下下沉的手感，不要用移动子控件坐标来模拟。
  - `PressedSlateSound` / `HoveredSlateSound` 是 `FSlateSound`，只有一个字段 `ResourceObject`（`UObject*`，指向 `USoundBase`），官方注明由 `FSlateSoundStructCustomization` 编辑。
- **Border 控件改背景** → 写 `Border.Background`（同样是 `FSlateBrush`）。
- `FSlateBrush` 官方共 14 个字段（`raw/docs/api/cppstruct/F/FS/FSlateBrush.md`，官方描述「An brush which contains information about how to draw a Slate element」），实例 `fields()` 可见 13 个（`Tint_DEPRECATED` 不出现，`bHasUObject_DEPRECATED` 显示为 `bHasUObject`）：

  | 字段 | 官方说明 | 使用建议 |
  | --- | --- | --- |
  | `ImageSize` | 资源在 Slate 单位下的尺寸 | 面板「图像大小」 |
  | `Margin` | **Box 与 Border 模式下使用的边距** | `DrawAs=Image` 时官方明确忽略 |
  | `TintColor` | 应用于图像的着色 | 需 `TintColor.ColorUseRule=0 (UseColor_Specified)` 才认 `SpecifiedColor` |
  | `ResourceObject` | 本画刷渲染的图像，**可为 UTexture 或 UMaterialInterface 或实现 AtlasedTextureInterface 的对象** | 面板「图片」 |
  | `ResourceName` | 渲染资源名 | 会残留引擎默认路径，可写 `'None'` |
  | `UVRegion` | 可选 UV 区域，有效时**覆盖资源代理里指定的 UV 区域** | 图集裁切用，未 PIE 验证 |
  | `DrawAs` | 如何绘制图像 | `Box(1)`/`Border(2)`/`Image(3)`/`RoundedBox(4)` |
  | `Tiling` | **Image 模式**下如何平铺 | 非 Image 模式无效 |
  | `Mirroring` | Image 模式下如何镜像；官方注明**通常只用于源纹理来自摄像头等硬件设备的动态画刷** | 普通 UI 不要动 |
  | `ImageType` | 图像类型 | `NoImage(0)/FullColor(1)/Linear(2)/Vector(3)` |
  | `bUseImageSizeAsTextureSize` | **官方无描述** | 语义未确认，见「待查证」 |
  | `bIsDynamicallyLoaded` | 画刷路径是否为指向 UObject 的路径 | 一般不手改 |
  | `bHasUObject_DEPRECATED` | 画刷是否有 UTexture 资源 | **已废弃**，实例里名为 `bHasUObject`，不要写 |
  | `Tint_DEPRECATED` | 应用于图像的着色 | **已废弃**，用 `TintColor` |

  完整枚举整数值见 [绿洲 UI 枚举与结构体速查](绿洲UI枚举与结构体速查.md)。
- `ResourceObject` 接受 `UTexture2D` **与** `UMaterialInterface`（实测 `MaterialInstanceConstant` 可直接赋值成功），官方 ToolTip 也写明可为 UTexture / UMaterialInterface / 实现 AtlasedTextureInterface 的对象。
- **`DrawAs` 决定 `Margin` 是否起作用**：`Box(1)` / `Border(2)` 才使用 `Margin` 做九宫格拉伸；`Image(3)` 忽略 `Margin`。按钮底图、面板背景应用 `Box` + `Margin≈0.25`，图标类用 `Image`。
- `FSlateBrush` 是**引用语义**：`img.Brush` 取回后就地改字段即生效，无需「取出→改→整体回写」。嵌套的 `TintColor`（`FSlateColor`：`SpecifiedColor` / `ColorUseRule`）与 `Margin`（`FMargin`：`Left/Top/Right/Bottom`）同理可就地写。
- **整体替换 struct 会清空未显式赋值的字段**：`btn.WidgetStyle = ButtonStyle()` 后只设了 `Normal`，实测 `Hovered.ResourceObject` 变为 `None`。**优先就地改字段**，需要整体替换时必须四态全部填齐。
- `ResourceName` 会残留引擎默认路径（如 `.../UGCEditor/Resources/Slate/Common/Button.png`），即使已换 `ResourceObject` 也不自动清空；可显式写 `'None'` 清理。

**代码示例：Image 画刷**

```python
import unreal_engine as ue
from unreal_engine.classes import Blueprint, Texture2D

wbp = ue.load_object(Blueprint, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian')

def find_widget(w, name):
    if w.get_name() == name:
        return w
    try:
        n = w.GetChildrenCount()
    except Exception:
        return None
    for i in range(n):
        r = find_widget(w.GetChildAt(i), name)
        if r:
            return r
    return None

img = find_widget(wbp.WidgetTree.RootWidget, '地图UI')
tex = ue.load_object(Texture2D, '/IslandAuctionKing/Asset/TuPian/TuJian/Codex_CardFrame')

img.Brush.ResourceObject = tex                                    # 面板「画刷 → 图片」
img.Brush.ImageSize = ue.FVector2D(128, 128)                      # 面板「图像大小」
img.Brush.DrawAs = 1                                              # 0=None 1=Box 2=Border 3=Image 4=RoundedBox
img.Brush.Margin.Left = 0.25                                      # DrawAs=Box/Border 时的九宫格边距
img.Brush.TintColor.SpecifiedColor = ue.FLinearColor(1, .62, .16, 1)   # 面板「着色」
img.Brush.Tiling = 0                                              # 0=NoTile 1=H 2=V 3=Both

ue.compile_blueprint(wbp)
wbp.save_package()
```

**代码示例：Button 四态样式**

```python
btn = find_widget(wbp.WidgetTree.RootWidget, 'ItemButton')
style = btn.WidgetStyle          # FButtonStyle，引用语义

STATE_TEX = {
    'Normal':   'Codex_FilterButton',    # 法线
    'Hovered':  'Codex_FilterPanel',     # 已悬停
    'Pressed':  'Codex_TopBar',          # 已按下
    'Disabled': 'Codex_Close',           # 已禁用
}
for state, name in STATE_TEX.items():
    brush = getattr(style, state)
    brush.ResourceObject = ue.load_object(Texture2D,
        '/IslandAuctionKing/Asset/TuPian/TuJian/' + name)
    brush.DrawAs = 1                                  # Box：底图九宫格拉伸
    brush.ImageSize = ue.FVector2D(64, 64)
    for side in ('Left', 'Top', 'Right', 'Bottom'):
        setattr(brush.Margin, side, 0.25)
    brush.ResourceName = 'None'                       # 清掉引擎默认 png 残留

style.NormalPadding.Left = 4.0                        # 常态内边距
style.PressedPadding.Left = 6.0                       # 按下位移感

ue.compile_blueprint(wbp)
wbp.save_package()

# 回读：widget_inspect 不返回画刷，必须自己读
for state in STATE_TEX:
    b = getattr(btn.WidgetStyle, state)
    ue.log(state + ' -> ' + str(b.ResourceObject) + ' DrawAs=' + str(b.DrawAs))
```

**`widget_set_property` 的支持边界（实测）**

| 属性路径 | 结果 |
| --- | --- |
| `Brush` / `Brush.ResourceObject` | ❌ `failed to set ... on '<控件名>'` |
| `WidgetStyle` / `WidgetStyle.Normal.ResourceObject` / `Normal` | ❌ 同上 |
| `Background.ResourceObject`（Border） | ❌ 同上 |
| `BrushImage`（UImage） | ⚠️ 返回 `None` 且回读有变化，但写进去的对象 class 是 **`Package`** 而非 `Texture2D`，属**假成功** |
| `BackgroundColor`（Button）/ `BrushColor`（Border） | 返回 `None`，需回读确认 |
| `Text` / `ToolTipText` / `Visibility` | ✅ 可用 |

结论：**画刷与样式一律用 Python 直接属性赋值，不要用 `widget_set_property`**。它不解析点号路径、不接受 struct，且对 `UObject*` 属性会把路径字符串解析成 `UPackage` 塞进去。

**EditCondition 两遍写入模式（UI 侧已确认的门控字段）**

部分 UI 属性带 `EditCondition` 门控，门控布尔为 `False` 时写被门控字段无效。必须**先开门 → 再写值 → 编译保存 → 回读**：

| 被门控字段 | 门控（EditCondition） | 编辑器 DisplayName |
| --- | --- | --- |
| `UTextBlock.MutiEllipsisLine`（int32） | `MutiEllipsisText`（bool） | — |
| `UButton.bUseCustomSettings`（bool） | `IsImgAlphaBtn`（bool） | 是否采用用户自定义设置 |
| `UButton.CustomHitAreaTexture`（`UTexture2D*`） | `bUseCustomSettings` | 自定义点击区域透明贴图 |
| `UButton.CustomHitAreaAlpha`（int32） | `bUseCustomSettings` | 自定义点击区域透明度阙值 |

`UButton.IsImgAlphaBtn` 的 DisplayName 是「是否异形按钮」——即让按钮的点击区域跟随贴图 alpha 而非矩形边界。它是**三层链式门控**：`IsImgAlphaBtn → bUseCustomSettings → CustomHitAreaTexture/CustomHitAreaAlpha`，必须自外向内依次开启。

```python
btn = find_widget(wbp.WidgetTree.RootWidget, 'ItemButton')

# 第一遍：自外向内开门
btn.IsImgAlphaBtn = True             # 是否异形按钮
btn.bUseCustomSettings = True        # 是否采用用户自定义设置

# 第二遍：写被门控的值
btn.CustomHitAreaTexture = ue.load_object(Texture2D,
    '/IslandAuctionKing/Asset/TuPian/TuJian/Codex_FilterButton')
btn.CustomHitAreaAlpha = 128         # 透明度阙值

ue.compile_blueprint(wbp); wbp.save_package()
ue.log('alpha_btn=%s custom=%s tex=%s thr=%s' % (
    btn.IsImgAlphaBtn, btn.bUseCustomSettings,
    btn.CustomHitAreaTexture, btn.CustomHitAreaAlpha))
```

同一模式适用于文本多行省略号：`txt.MutiEllipsisText = True` 之后再写 `txt.MutiEllipsisLine = 2`，顺序颠倒则行数写不进去。

**术语区分：UI 画刷 ≠ 地表材质「画刷贴图」**

`raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md` 末段提到「地表材质当前仅支持一种材质的修改，修改方法是修改画刷贴图」，那里的「画刷」指**地形绘制笔刷**，属场景/地表材质范畴，与本节的 `FSlateBrush`（Slate UI 画刷）**毫无关系**。检索官方文档时不要把两者混为一谈。

---

## 三、常见 Bug 避坑指南 (Anti-Patterns & Troubleshooting)

| 常见问题 | 产生原因 | 正确解决方案 |
| :--- | :--- | :--- |
| 页面出现横向滚动条 | 主容器设了 `min-width`（如 `body{min-width:920px}`）；`grid-template-columns:repeat(4,220px)` 固定列宽；子元素 `width:100%` 又带 padding 但无 `border-box` | 去掉 `min-width`；改 `minmax(min(220px,100%),1fr)`；全局 `box-sizing:border-box`；根级 `max-width:100%; overflow-x:hidden` 兜底 |
| 移动端文字重叠 | `line-height:1`/`normal` 配合 `clamp()` 放大字号；用绝对定位按基准像素堆叠文本块 | 正文 `line-height:1.5`；文本改用 Flex/Grid 流式排列；UMG 侧用 `LineHeightPercentage` 与 AutoWrapText 代替坐标堆叠 |
| 控件在小屏下被挤压变形 | Flex/Grid 子项默认 `min-width:auto`，长内容顶宽兄弟节点；图片未设 `height:auto` | 子项统一 `min-width:0`（纵向 `min-height:0`）；关键控件 `flex:0 0 auto` + `min-height:44px`；图片 `max-width:100%;height:auto` |
| 动态超长文本撑破卡片 | 只按示例短文案设计，未做最坏假设 | 容器先定 `max-width`/`SizeBox.MaxDesiredWidth`，再选定折行策略（换行 / 单行 ellipsis / `-webkit-line-clamp`）；UMG 用 `AutoEllipsisText` 或 `MutiEllipsisText+MutiEllipsisLine` |
| 出现双滚动条 / 滚动劫持 | 同一方向嵌套两层 `overflow:auto`；`overflow-y:auto` 所在容器没有高度约束 | 只保留一层滚动容器；滚动容器链上每层加 `min-height:0`/`flex:1`/`max-height`；加 `overscroll-behavior:contain` |
| 内容被 `overflow:hidden` 意外裁掉 | 为"防溢出"无脑全局加 hidden | hidden 只用于确定尺寸的装饰容器；需要浏览的内容用 `overflow:auto`；UMG 侧慎开 `Clipping`（官方注明不同裁剪空间无法合批，有性能代价） |
| 中文/￥ 显示为方框或乱码 | 文件非 UTF-8 或带 BOM；`<meta charset>` 位置太晚；字体族无中文 fallback | 文件存 UTF-8 无 BOM；charset 放 `<head>` 首行；字体族补 `"Microsoft YaHei","PingFang SC","Noto Sans SC"` |
| 结算/数值文本换行错乱 | 文案里写死 `\n` | 按项目规范禁止 `\n`，统一 `"标签 ￥数值"` 单行格式，换行交给 `AutoWrapText` 或拆控件 |
| Tailwind/Bootstrap/AntD 样式被覆盖或反覆盖 | 自定义样式与框架同优先级；靠 `!important` 硬压 | 自定义样式收敛到单一入口层，用 `@layer components`（Tailwind）或提升一级作用域选择器；AntD 用官方 token / ConfigProvider 改主题而非覆盖内部类名；避免 `!important` 与深层后代选择器 |
| 高分屏 1px 边框变粗/消失、图片发虚 | 用 `transform:scale` 或 `border:1px` 在 DPR≥2 下取整偏差；只提供 1x 图 | 边框改用 `box-shadow:inset 0 0 0 1px` 或 `@media (min-resolution:2dppx){ border-width:.5px }`；图片提供 2x/3x 或 `image-set()`；UI 贴图按 `TEXTUREGROUP_UI` + `TMGS_NoMipmaps` 导入避免 Mip 采样发虚 |
| MCP 改了坐标但界面没动 | 用 `widget_slot` 写 `Position`/`Offsets`/`Anchors`（实测全部失败，且成功时也返回 `None`） | 改用 `w.Slot.SetPosition/SetSize/SetAnchors/SetAlignment`，随后 `compile_blueprint` + `save_package`，再 `widget_inspect` 回读 |
| 清理测试控件后布局仍错乱 | `widget_wrap` 生成的 `<原名>_Wrapper` 容器未被 `widget_remove` 删除，残留空容器仍占位 | 删控件后显式删除同名 `_Wrapper`；回读控件树确认层级 |
| 复制 UI 蓝图后资产查不到 | 对 `UGCWidgetBlueprint` 用了 `duplicate_asset`，产出带点号的游离包对象且无法删除 | 必须用 `objed_duplicate_asset(源名, 新名, 'UI')`，并先 `ue.objed_open_editor('UI')` |
| UI 在异形屏被刘海遮挡 | 缺少标准层次结构或未调 `SetAdaptation` | 按官方 `画布面板→缩放框→尺寸框→画布面板` 结构搭建，`AdaptionPanel` 勾 `Is Variable`，`Construct` 中调 `UICommonFunctionLibrary.SetAdaptation`；所有主 UI 逐个适配 |
| 改了「画刷 图像」但样式没变 | 误改 `UImage.BrushImage`，它不是 Slate 渲染用的画刷 | 改 `UImage.Brush.*`（`ResourceObject`/`ImageSize`/`TintColor`/`Margin`/`DrawAs`/`Tiling`） |
| 按钮悬停/按下时贴图突变回默认样式 | 只设了 `WidgetStyle.Normal`，`Hovered`/`Pressed`/`Disabled` 仍是引擎默认 png | 四态（法线/已悬停/已按下/已禁用）必须**分别**设置完整 `FSlateBrush` |
| 按钮九宫格底图被拉伸变形 | `DrawAs=Image(3)` 时 `Margin` 被忽略 | 底图/面板用 `DrawAs=Box(1)` + `Margin≈0.25`，图标才用 `Image(3)` |
| 整体替换 `WidgetStyle` 后其他状态贴图消失 | `ButtonStyle()` 新实例未赋值的字段为空，整体赋值会覆盖全部四态 | 优先就地改字段；必须整体替换时四态全部填齐 |
| UI 贴图导入后仍发虚 / 内存异常 | `MipGenSettings` 被写成 `2`（`raw/docs/ai/20260824_...` 原记录数字有误，`2` 实为 `TMGS_Sharpen0`）；或 `LODGroup` 仍是 `0 (TEXTUREGROUP_World)`——导入默认就是 World 组 | 按官方「UI贴图设置」写 `LODGroup=16` / `MipGenSettings=13` / `CompressionQuality=5` / `CompressionSettings=0` / `SRGB=True`，写后跨对象重新 `load_object` 回读五项 |
| 批量改贴图属性后只有最后一张生效 | 循环外只调了一次 `save_package()`；它是**对象方法**，只落盘自身所在 package | 循环内**逐张** `o.save_package()`，改完再核磁盘 `mtime`/字节数 |
| 跨目录批量写入时 PRV 校验不通过 | `ue_plan_submit` 的 `asset_path` 只接受**单个**路径 | 一个目录一个 plan_id，分次提交分次执行 |
| 反复重跑批量脚本导致资产体积/时间戳抖动 | 无条件写入 + 无条件 `save_package()` | 先读 before，值已正确则跳过写入与保存（幂等） |
| 写了 `Brush.TintColor.SpecifiedColor` 但颜色没变 | `TintColor.ColorUseRule` 不是 `UseColor_Specified(0)`，颜色由前景色/样式决定 | 先写 `Brush.TintColor.ColorUseRule = 0`，再写 `SpecifiedColor`，然后回读两个字段 |
| 写了 `MutiEllipsisLine` 但多行省略号不生效 | 该字段 EditCondition 为 `MutiEllipsisText`，门未开时写入无效 | 两遍写入：先 `MutiEllipsisText=True`，再写行数；异形按钮同理 `IsImgAlphaBtn → bUseCustomSettings → CustomHitArea*` |
| 手机端大字号标题不显示或内存暴涨 | 直接把 `FSlateFontInfo.Size` 调大；官方明确手机端无法渲染过大字体图集 | 用小字号 + `ScaleBox`/`RenderTransform` 放大；Photoshop 出稿按 96 dpi 而非 72 dpi |
| 开裁剪后 UI 掉帧 | 给每层容器都设 `ClipToBounds`，跨裁剪区无法合批 | 文本用 `OnDemand(4)`，硬边界用 `ClipToBoundsAlways(3)`，其余保持 `Inherit(0)` |
| PC 端与移动端缩放表现不一致 | 只改了 `ScaleBox.Stretch`，没改 `StretchPc` | 两套字段（`Stretch*` 与 `Stretch*Pc`）一并设置并回读 |
| `ue.find_class('UICommonFunctionLibrary')` 查不到 | 它是蓝图函数库 `UICommonFunctionLibrary_C`，不是 C++ 类 | 用 `ue.all_classes()` 找 `_C` 后缀类；签名用 `ue.find_object('<类路径>:<函数名>').properties()` 过滤 `CallFunc_`/`K2Node_`/`Temp_` |
| 读到 `Slot.GetSize()` 为 `(0,0)` 误判控件异常 | 锚点为四向拉伸（Anchors Min==0、Max==1）时 Offsets 语义变为四边留白，Size 不参与计算 | 先读 `Slot.LayoutData.Anchors`：Min==Max 才按 `(X,Y,W,H)` 解释 Offsets，拉伸态按 `(L,T,R,B)` 留白解释 |
| 改了 `Brush.ImageSize` 显示尺寸没变 | `DrawAs=Image(3)` 且 Slot 给了显式尺寸时，显示尺寸由 Slot Offsets 决定 | 改显示尺寸走 `Slot.SetSize()`；`ImageSize` 只在 `bAutoSize=True` 或依赖期望尺寸时生效 |
| 换一张贴图却影响了多个控件 | 同一 `Texture2D` 被多个 Image 的 `ResourceObject` 复用（实测 `ZJM1` 被 3 个控件共用） | 改前先全量导出画刷对照表确认复用关系，需差异化时先复制出独立贴图资产 |
| 搜「画刷」搜到地表材质文档 | 官方文档里「地表材质修改画刷贴图」指地形笔刷，与 `FSlateBrush` 无关 | 检索 UI 画刷时用 `FSlateBrush` / `Brush` 属性名定位，不用中文「画刷」 |
| `widget_set_property` 写画刷「成功」却不渲染 | 该 API 不解析点号路径；写 `BrushImage` 时把路径解析成 `UPackage` 而非 `Texture2D` | 画刷与样式一律用 Python 直接赋值，写后回读并校验 `get_class().get_name()` |
| 换了贴图但 `ResourceName` 仍指向引擎默认 png | `ResourceObject` 与 `ResourceName` 是两个独立字段，不联动 | 显式写 `brush.ResourceName = 'None'` 清理残留 |
| `WidgetTree.AllWidgets` 遍历不到任何控件 | `load_object` 后该数组长度为 0（实测） | 从 `WidgetTree.RootWidget` 起用 `GetChildrenCount()`/`GetChildAt(i)` 递归 |
| 往 `ScrollBox`/`WrapBox` 里塞控件后界面不显示 | 直接改容器的 `Slot` 或子控件数组，未走容器 API | 统一 `container.AddChild(widget)`（社区帖 2193），再 `compile_blueprint` + `widget_inspect` 回读层级 |
| `data_table_find_row()` 抛异常 | 该 API 只接受 `str` 行名，传入非字符串直接失败 | 行名一律先 `str()`；批量读用 `data_table_get_all_rows()`（返回行结构体实例列表，**不是行名**） |
| 调 `data_table_get_all_rows_name()` 报不存在 | 该方法在绿洲 Python 绑定中**不存在** | 行名需另行维护，或按 `data_table_get_all_rows()` 的顺序对齐 |
| 预览页用 `file://` 打不开 | in-app browser 策略拦截本地文件协议 | 起本地 HTTP 服务（`127.0.0.1`）再 `tab.goto`；用户自己的浏览器可直开 `file://` |
| 预览服务莫名 `ERR_CONNECTION_REFUSED` | node REPL 里挂在 `globalThis` 上的 server 会随 cell 间 session 重置而丢失 | 把服务写成独立 `.js` 脚本，用 `exec_command` 前台常驻并配 `yield_time_ms`（`Start-Process` 会被策略拒绝） |
| 想在预览页里跑 JS 做 DOM 断言 | `tab` 对象**无 `evaluate`/`content`** 方法（仅 `goto/back/forward/reload/close/screenshot/title/url/getJsDialog/markHandoff/markDeliverable/requestManualHandoff/nameSession`） | 断言逻辑前置到生成数据的 node 侧；页面侧只做截图目视核对 |
| 声称素材已落位但预览全是占位图 | 数据文件缺贴图名字段，模板取值为 `undefined`，N 个请求折叠成同一个 404 | 落盘后强制自检：文件数等于表行数、无 `undefined.png`、生成时输出 `missingPng` 且为空数组 |

---

## 四、AI UI 生成指令模板 (System Prompt Extension)

```text
【UI 生成硬约束】
1. HTML 必须 <meta charset="UTF-8"> 位于 head 首行 + viewport meta，文件存 UTF-8 无 BOM。
2. 全局 *,*::before,*::after{box-sizing:border-box}；html,body{max-width:100%;overflow-x:hidden}；
   禁止对 body 或主容器设置 min-width。
3. 颜色/间距/圆角/阴影一律用 :root CSS 变量；间距取 4px 栅格；禁止组件内裸 hex 与 Magic Number。
4. 布局只用 Flexbox / CSS Grid；绝对定位仅限装饰元素。所有 Flex/Grid 子项加 min-width:0
   （纵向 min-height:0）；网格列用 minmax(min(Npx,100%),1fr) 或 auto-fill。
5. 尺寸优先 clamp()/min()/max()/%/fr/rem；固定 px 仅用于 1px 描边、图标、min-height:44px。
   断点：480/768/1024/1440，断点只改列数与方向。
6. img/video/svg/canvas 一律 max-width:100%;height:auto;display:block。
7. 正文 font-size≥16px、line-height:1.5、行长 max-width:60ch、对比度≥4.5:1；
   字体族 "Microsoft YaHei","PingFang SC","Noto Sans SC",Arial,sans-serif。
8. 文本三选一：完整展示(white-space:normal;overflow-wrap:anywhere) /
   单行截断(overflow:hidden;white-space:nowrap;text-overflow:ellipsis) /
   多行截断(-webkit-line-clamp)；不得混用；不得在文案里写 \n。
9. 滚动容器只保留一层，且其祖先链必须有高度约束(min-height:0/flex:1/max-height)；
   overflow:hidden 仅用于确定尺寸的装饰容器。
10. 触控目标 ≥44×44px，相邻间距 ≥8px。
11. 用 320px / 768px / 1440px 三档自检：无横向滚动条、无文字重叠、无控件溢出后才算交付。

【绿洲 UMG 落地约束】
12. 设计基准 1920×1080；UI 蓝图层次必须为 画布面板→缩放框→尺寸框→画布面板→业务控件；
    缩放框锚点=四向拉伸且偏移全 0；尺寸框宽/高重载 1920/1080；内层画布面板 水平填充+垂直居中填充。
13. 主 UI 在 Construct 调 UICommonFunctionLibrary.SetAdaptation(self.AdaptionPanel, self)。
14. 坐标尺寸改动必须走 Slot 的 SetPosition/SetSize/SetAnchors/SetAlignment，
    不要用 widget_slot 写 Position/Offsets/Anchors。
15. 所有可调 UI 数值（尺寸、坐标、槽位数、贴图路径）登记进
    Asset/Data/Table/Customized/UI/UIConfigTable，Lua 侧函数内经 AuctionConfig.Get* 读取并带默认回退。
16. 每次 MCP 写入后 compile_blueprint + save_package，并 widget_inspect 回读核对（写入 API 成功也返回 None）。
17. Image 控件改样式写 Brush（不是 BrushImage）；Button 改样式写 WidgetStyle 的
    Normal/Hovered/Pressed/Disabled 四态，每态独立完整设置；Border 改 Background。
18. 画刷与样式禁止用 widget_set_property，一律 Python 直接属性赋值；就地改字段而非整体替换 struct；
    底图用 DrawAs=Box(1)+Margin，图标用 Image(3)；回读时校验对象 class 为 Texture2D/MaterialInterface。
19. 枚举属性一律按整数赋值，数值必须查《绿洲 UI 枚举与结构体速查》或 ue_read enum:XXX，禁止凭名称顺序猜。
    改着色须同时写 TintColor.ColorUseRule=0；Clipping 文本用 4(OnDemand)、硬边界用 3(ClipToBoundsAlways)。
20. 带 EditCondition 的字段两遍写入：先置门控布尔为 True 再写值（MutiEllipsisText→MutiEllipsisLine；
    IsImgAlphaBtn→bUseCustomSettings→CustomHitAreaTexture/CustomHitAreaAlpha）。
21. 放大文字禁止调大 FSlateFontInfo.Size（官方：手机端无法渲染过大字体图集），改用小字号+ScaleBox/RenderTransform。
22. UI 贴图按官方设置：LODGroup=16、MipGenSettings=13(TMGS_NoMipmaps，不是 2)、CompressionQuality=5、
    CompressionSettings=0、SRGB=True；导入默认不是 UI 组，必须显式修正，写后跨对象回读五项。
    批量改贴图：一个目录一个 plan_id、循环内逐张 save_package()、先读 before 做幂等、结束打 ALL_xx_COMPLIANT 断言日志。
23. 改 ScaleBox 缩放行为时 Stretch* 与 Stretch*Pc 两套字段一并设置，否则 PC 与移动端表现不一致。
```

---

---

## 七、2026-09-14 补充：MCP 控件蓝图创建实测（端到端验证）

**适用范围**：从零创建控件蓝图资产 → 搭建控件树 → 设置属性 → 保存 → 回读的完整链路。
**证据状态**：项目实测（IslandAuctionKing 装扮 UI，`AuctionDressUI`，70→73 控件）。

### 1. 控件蓝图的类句柄获取（高频阻塞点）

`from unreal_engine.classes import WidgetBlueprint` **不可用**，报
`ImportError: cannot import name 'WidgetBlueprint'`。原因是 `unreal_engine.classes`
模块不暴露类名（实测 `total_classes = 0`，`sample_ucg` / `sample_user` / `sample_bp` 均为空）。

正确姿势（官方 `py:resolve_asset` 文档给出的标准 recovery 模式）：

```python
cls = ue.find_class('UGCWidgetBlueprint')          # 控件蓝图类名 = UGCWidgetBlueprint
wbp = ue.load_object(cls, '/Project/Asset/.../X.X')  # load_object 至少 2 参：class, path
```

注意 `find_class` 只按**短名**查找且只能找到已加载的类；`WidgetBlueprint` /
`UserWidgetBlueprint` / `UGCUserWidget` 等候选名**均不存在**，逐个试探会得到
`unable to find class123 <name>`，唯一有效名是 `UGCWidgetBlueprint`。

### 2. `ue_plan_submit` 的 mutations 结构（易错）

`mutations` 必须是**对象列表** `[{property, value, gate?}]`，传字符串列表会报：

```
PRV_PLAN_INVALID: PRV plan incomplete, missing/invalid: mutations|scene_ops (at-least-one-required)
```

即"字段存在但类型不符"仍被判定为缺失，错误信息不提示类型问题。另：YAML 内**避免中文全角
引号/括号**，会干扰解析。`scene_ops` 的 op 仅支持 actor 相关
（`actor_spawn` / `actor_modify` / `actor_destroy` / `actor_set_folder`），
**不适用于 UI 控件树**，UI 侧一律用 `mutations`。

### 3. 保存 API 名称

`ue.save_package` **不存在**（`module 'unreal_engine' has no attribute 'save_package'`）。
正确入口为 **`ue.objed_save_asset(asset_name, editor_type='')`**，静默保存、返回 bool。
同一分类下还有 `objed_create_asset(editor_type, asset_type, template_name, asset_name, sub_dir='')`，
控件蓝图对应 `objed_create_asset('UI', '元件', '用户控件模板', 'AssetName')`。

### 4. DataTable 读取是对象方法

`ue.data_table_as_dict(dt)` **不存在**。正确形式是**对象方法调用**：

```python
tbl = ue.load_object(ue.find_class('DataTable'), '/Project/Asset/.../Table')
d = tbl.data_table_as_dict()   # 返回 {行名: UScriptStruct}
```

同类：`data_table_get_all_rows` / `data_table_add_row` / `data_table_find_row` 等在
`py:list datatable` 分类下（共 10 个）。注意 `data_table_find_row` 查不存在的行会**抛异常**，
必须包在 try/except。

**行值访问**：`data_table_as_dict()` 返回的值是 `UScriptStruct`，**不支持 `.get()`**
（`'unreal_engine.UScriptStruct' object has no attribute 'get'`），需用属性访问
`v.MaterialName` / `v.MaterialSource`，且每个字段都要单独 try/except（字段可能不存在）。

### 5. `widget_slot` 的布局限制（再次确认）

`ue.widget_slot(wbp, name, 'Position'|'Size', ...)` 实测报
`failed to set 'Position' on '<Name>'`。与本页第二节结论一致：坐标与尺寸**必须走 Lua 运行时
UFunction**（`Slot:SetPosition` / `SetSize`），设计态用 `widget_slot` 只能稳定写
`ZOrder` / `bAutoSize`。因此"蓝图控件树 + Lua 运行时布局"是唯一可靠分工。

### 6. 控件树批量搭建的可行批次

`widget_add(wbp, type_str, name, parent_name)` 单次调用即创建一个控件。实测单批
**32 个控件（16 Button + 16 TextBlock）可一次执行完成**，耗时约 4 ms，未见超时。
推荐批次：容器骨架 7 个 → 一级按钮 10 个 → 二级按钮 20 个 → 三级按钮 32 个。

**控件层级约束**：`Button` 的子级只能是单个 `TextBlock`（`widget_add(..., 'TextBlock', label, buttonName)`），
`VerticalBox` 可直接容纳多个同层控件。回读用 `ue.widget_inspect(wbp)`，输出树形字符串，
格式为 `[类型] 名称 {Slot 摘要}`，缩进表示层级。

### 7. 验证闭环（写后必做）

创建/写入后**必须**以下三项联合回读，缺一不可：

1. `ue.resolve_asset('AssetName')` — 确认资产存在及 `load_path` / `disk_size`（尺寸显著增长即已落盘内容）
2. `ue.widget_inspect(wbp)` — 确认控件树结构与命名
3. 控件名与 Lua 契约做**双向 diff**（期望名逐个 `in` 实际名集合），要求 `missing == []`

本轮实测：蓝图 70 控件、Lua 契约 68 项、`MISSING=[]`、`MATCH=True`。

### 8. 【重要】结构体属性（Padding / Size）的写入路径（2026-09-14 第二轮）

**问题**：`VerticalBoxSlot` 的 `Padding` / `Size` 无法通过任何字符串入口写入。

**报错清单（全部实测）**：

| 尝试 | 结果 |
|---|---|
| `ue.widget_slot(wbp, name, 'Padding', '0,0,0,8')` | `failed to set 'Padding' on '<Name>'` |
| `slot.set_property('Padding', '0,0,0,8')` | `unable to set property Padding` |
| `slot.set_property('Padding', {'Left':0,...})` | `unable to set property Padding` |
| `slot.SetPadding('0,0,0,8')` | `unable to convert pyobject to property InPadding (StructProperty)` |
| `slot.SetPadding(ue.FVector(0,0,8))` | 同上（类型仍不匹配） |
| `slot.SetPadding(ue.FLinearColor(...))` | 同上 |
| `ue.function_call(slot,'SetPadding', margin)` | 同字符串错误 |

**根因**：`padding` 是 `StructProperty`，必须传入真正的 **`Margin` 结构体实例**；
字符串与向量类都无法隐式转换为 `Margin`。

**`Margin` 结构体的正确构造链**（关键：`new_object` 要传 `UClass` 而非 `UScriptStruct`）：

```python
import unreal_engine as ue

# ✅ 关键三步
ms  = ue.find_struct('Margin')                 # 返回 UObject，UClass = 'ScriptStruct'
m   = ue.new_object(ms.get_class())            # ⚠️ 必须 get_class()；直接传 ms 报 "uobject is not a UClass"
# 此时 m.properties() == []（空），字段赋值只能走 set_field，不能走 set_property
m.set_field('Left', 0.0)
m.set_field('Top', 0.0)
m.set_field('Right', 0.0)
m.set_field('Bottom', 6.0)
print(m.as_dict())   # {'Left':0.0,'Top':0.0,'Right':0.0,'Bottom':6.0}

# ✅ 写入 Slot：必须用 call_function，不能用 SetPadding 直接调用
slot.call_function('SetPadding', m)
print(slot.get_property('Padding').as_dict())   # Bottom 已变为 6.0
```

**`SlateChildSize`（高度）同理**：

```python
s = slot.get_property('Size').clone()   # 或 ue.new_object(ue.find_struct('SlateChildSize').get_class())
s.set_field('Value', 52.0)
s.set_field('SizeRule', 0)              # 0 = Automatic（按期望尺寸）
slot.call_function('SetSize', s)
```

**`UScriptStruct` 对象的可用方法**（`dir()` 实测，与 `py:list uscriptstruct` 的 8 项一致）：
`as_dict` / `clone` / `fields` / `get_field` / `get_field_array_dim` / `get_struct` / `ref` / `set_field`。

> 注意：`ue.new_struct` / `ue.make_struct` / `ue.construct_struct` **均不存在**；
> `ue.new_object` 是唯一实例化入口，但**参数必须是 `UClass`**。
> `uscriptstruct` 分类的 `py:guide` 只给分组标题（"实例化/创建结构体实例"），
> **不给具体方法名**，实际方法名必须靠 `dir()` 探测。

**`ESlateSizeRule` 枚举值**（`enum:ESlateSizeRule` 官方反射确认）：
`Automatic = 0`（按控件期望尺寸）、`Fill = 1`（按 Value 比例贪婪填充）、`_MAX = 2`。
因此固定高度场景应写 `SizeRule=0 + Value=<像素高>`；JSON 里零值不落属性，
UAssetGUI 导出的 `Size` 结构体会**看不到 `SizeRule` 字段**，这是正常现象不是写入失败。

**`CanvasPanelSlot` 的坐标回读方式（与写入不对称，易错）**：
`CanvasPanelSlot` 的可编辑属性只有 `LayoutData`(FAnchorData) / `bAutoSize` / `ZOrder` / `bAntiAdaptation`。
回读坐标**不能用 `get_property('Position')`**（报 `unable to find property Position`），必须：

```python
offs = slot.get_property('LayoutData').as_dict()['Offsets']
x, y, w, h = offs['Left'], offs['Top'], offs['Right'], offs['Bottom']
```

即 CanvasPanelSlot 采用 `(Left, Top, Right, Bottom)` 表示 `(x, y, width, height)`（非右边界）。
写入侧仍走 UFunction `SetPosition` / `SetSize`（`ue.FVector2D(x, y)`，注意 **`FVector2D` 在
`unreal_engine` 顶层**，`unreal_engine.structs` 里没有）。

**本轮端到端验收**：适配层 `CanvasPanel_0 → DressScaleBox → DressSizeBox → DressCanvas`；
容器 8/8 坐标回读一致；三级列表 30/30（一级 4×52、二级 10×52、三级 16×40，下间距 6，末项 0）；
UAssetGUI 导出 JSON 独立核对：`VerticalBoxSlot` 30 个、`CanvasPanelSlot` 9 个、
`ScaleBoxSlot`/`SizeBoxSlot` 各 1 个，均与设计一致。

> **`widget_inspect` 的 Slot 摘要可作快速验证**：`[Button] UIButton01 {VerticalBox (Padding: 0,0,0,6)}`
> —— 直接读出 `Padding`，无需解析结构体。

### 9. 【重要】适配层 ScaleBox 未铺满画布（2026-09-14 第三轮修复）

**症状**：整棵控件树被压缩在画布左上角一小块（约 105×50 px），其余区域全空。

**根因**：`widget_add` 把 `ScaleBox` 挂到根 `CanvasPanel_0` 下时，**Slot 继承的是
`CanvasPanelSlot` 默认值** —— 锚点 `Min = Max = (0,0)`、偏移 `100 × 30`。
于是 ScaleBox 只有 100×30 大，内部所有内容再被 ScaleBox 等比缩放到那个小方块里。

**诊断**（一条命令即可确认）：

```python
sl = by['DressScaleBox'].Slot
print(sl.get_class().get_name())          # CanvasPanelSlot ← 关键
ld = sl.get_property('LayoutData').as_dict()
print(ld['Anchors']['Minimum'].as_dict()) # {'x': 0.0, 'y': 0.0}   ← 应为 (0,0)
print(ld['Anchors']['Maximum'].as_dict()) # {'x': 0.0, 'y': 0.0}   ← 应为 (1,1)
print(ld['Offsets'])                      # {'Left':0,'Top':0,'Right':100.0,'Bottom':30.0}
```

**修复**（四向拉伸 + **四个偏移全部归零**）：

```python
V2 = ue.FVector2D
sl.call_function('SetMinimum', V2(0.0, 0.0))     # 锚点左上
sl.call_function('SetMaximum', V2(1.0, 1.0))     # 锚点右下 → 四向拉伸
sl.call_function('SetPosition', V2(0.0, 0.0))    # 偏移左/上 = 0
sl.call_function('SetSize', V2(0.0, 0.0))        # 偏移右/下 = 0  ← 必须是 0，不是设计基准尺寸
sl.call_function('SetAlignment', V2(0.0, 0.0))
```

回读验证：`MIN=(0,0) MAX=(1,1) OFF={0,0,0,0}` ✅

> ⚠️ **`SetSize(1920, 1080)` 是错的**（本库 2026-09-14 第三轮曾误记为正确解，第四轮已被截图证伪）。
> 拉伸态下 `Offsets` 走的是**四边留白语义**（见下方第 10 节），
> `Right=1920 / Bottom=1080` 等于在右侧留白 1920、下侧留白 1080，
> 缩放框宽度被压成 `父宽 − 0 − 1920`（负值），内容因此被挤到左上角一小块 —— 与"未铺满"症状同源。
> `SetSize` 的正确定位是：**先把设计基准写在尺寸框的宽/高重载上，缩放框只负责拉满并留白 0**。

**`CanvasPanelSlot` 完整 setter 清单**（`functions()` 实测 22 个）：

- 几何：`SetPosition` / `SetSize` / `SetOffsets` / `SetAnchors` / `SetMinimum` /
  `SetMaximum` / `SetAlignment` / `SetLayout`
- 其他：`SetZOrder` / `SetAutoSize` / `SetAntiAdaptation`
- 对应 getter：`GetPosition` / `GetSize` / `GetOffsets` / `GetAnchors` /
  `GetAlignment` / `GetZOrder` / `GetAutoSize` / `GetAntiAdaptation` / `GetLayout`

**`SetMinimum` / `SetMaximum` 才是写锚点的正确入口**。`SetAnchors` 虽存在，但它要求传入完整的
`Anchors` 结构体，而 `ld.as_dict()['Anchors']` 返回的是**普通 `dict`**（不是 `UScriptStruct`），
无法 `clone()` 或 `set_field()`；`SetOffsets` 同样因 `InOffset` 为 `StructProperty` 而
拒绝 `FVector2D` / `Margin` / 字符串所有形态。**用 `SetPosition` + `SetSize` 间接完成偏移写入即可**。

**其他 Slot 类型无锚点概念**：`ScaleBoxSlot` / `SizeBoxSlot` / `VerticalBoxSlot` 的
`properties()` 只有 `Padding` / `HorizontalAlignment` / `VerticalAlignment` / `Parent` / `Content`，
访问 `LayoutData` 会报 `unable to find property LayoutData`，这是正常的，不要误判为缺失。

**`Margin` 构造的上下文差异（易踩）**：

| 场景 | 可用构造方式 |
|---|---|
| 独立构造 | `ue.new_object(ue.find_struct('Margin').get_class())` → `UScriptStruct`，有 `set_field` |
| **某些上下文** | 上面写法返回 `UObject`（**无 `set_field`**），必须改用 `slot.get_property('Padding').clone()` |

因为 `VerticalBoxSlot` 场景下 `new_object` 方式可用、而 `ScaleBoxSlot`/`SizeBoxSlot` 场景下
不可用，**稳妥写法是优先 `clone()` 现有值**：

```python
p = sl.get_property('Padding').clone()   # 必定返回 UScriptStruct
p.set_field('Left', 0.0); p.set_field('Top', 0.0)
p.set_field('Right', 0.0); p.set_field('Bottom', 0.0)
sl.call_function('SetPadding', p)
```

**`FVector2D` 属性名是小写 `x` / `y`**（不是 `X` / `Y`）：`v.x` / `v.y`；
`v.as_dict()` 返回 `{'x': .., 'y': ..}`。`as_dict()` 对嵌套结构体会把内层也转成 `dict`，
所以 `ld.as_dict()['Anchors']['Minimum']` 是 `dict` 而非结构体对象。

**本类问题与 `AuctionTestUI` / `CollectibleCodexUI` 的差异**：那两个蓝图的根直接就是
`ScaleBox` 或 `CanvasPanel → ScaleBox`，天然继承正确的拉伸语义；
`AuctionDressUI` 是先建 `CanvasPanel_0` 当根、再往里挂 ScaleBox，才会踩到这个默认 Slot 陷阱。
**新建适配层时，挂完 ScaleBox 必须立刻设置四向拉伸**，不要依赖默认值。

---

### 10. 【必背】适配层三项参数清单与「拉伸态偏移」语义（2026-09-14 第四轮定论）

官方文档 `docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md` 给出唯一权威做法。
层次结构（外→内）：**画布面板(根) → 缩放框 → 尺寸框 → 画布面板(业务)**。

三项参数**必须同时满足**，缺一项都会导致"未铺满 / 比例失控"：

| 序号 | 控件 | 类型 | 参数 | 通过 API 写入方式 |
|---|---|---|---|---|
| ① | 缩放框 | `ScaleBox`（其 Slot 为 `CanvasPanelSlot`） | 锚点四向拉伸 + **四个偏移全 0** | `SetMinimum(FVector2D(0,0))`、`SetMaximum(FVector2D(1,1))`、`SetPosition(FVector2D(0,0))`、`SetSize(FVector2D(0,0))` |
| ② | 尺寸框 | `SizeBox`（其 Slot 为 `ScaleBoxSlot`） | **宽度重载 1920 / 高度重载 1080** | `SetWidthOverride(1920.0)`、`SetHeightOverride(1080.0)` |
| ③ | 业务画布 | `CanvasPanel`（其 Slot 为 `SizeBoxSlot`） | 水平对齐填充 / 垂直对齐填充（枚举值 `0`） | `SetHorizontalAlignment(0)`、`SetVerticalAlignment(0)` |

**关键语义（本轮定论，与第 7 节第 458 行互为印证）**：

- `CanvasPanelSlot.Offsets` 的含义**随锚点模式切换**：
  - `Anchors.Minimum == Anchors.Maximum`（角锚点）→ Offsets 按 `(X, Y, W, H)` 解释，
    此时 `SetSize(1920,1080)` 表示"控件就是 1920×1080"。
  - `Anchors.Minimum ≠ Anchors.Maximum`（拉伸态）→ Offsets 按 **`(Left, Top, Right, Bottom)` 四边留白**解释，
    控件宽度 = `父宽 − Left − Right`。**此时 `SetSize(1920,1080)` 会写出 `Right=1920 / Bottom=1080` 的留白，
    把控件宽度压成负值** —— 这就是"内容挤在左上角一小块"的真正机理。
  - **结论：拉伸态的偏移必须是 `(0,0,0,0)`**，用 `SetPosition(0,0)` + `SetSize(0,0)` 即可写到。

- **尺寸框重载不设 = 适配链断裂**。`SizeBox` 的 `WidthOverride` / `HeightOverride` 默认都是 `0.0`，
  且带独立位域开关 `bOverride_WidthOverride` / `bOverride_HeightOverride`（默认 `False`）。
  **只写数值不写开关无效**；`SetWidthOverride()` / `SetHeightOverride()` 会同时置位数值与开关，
  是唯一可靠入口（直接 `set_property('WidthOverride')` 不会置位 `bOverride_*`）。
  不设重载时，缩放框只能按子控件**聚合期望尺寸**（很小）算缩放比 → 比例彻底失控。

- `ScaleBox` 的正确取值：`Stretch = 2`（`EStretch::ScaleToFit`，等比缩放并留边）、
  `StretchDirection = 0`（`EStretchDirection::Both`，允许放大也允许缩小）。这两个值本身就是默认值，无需改。

**缩放比自证公式**（`ScaleToFit`）：`scale = min(屏宽 / 1920, 屏高 / 1080)`。

| 屏幕 | 缩放比 | 渲染尺寸 | 结果 |
|---|---|---|---|
| 1920×1080（16:9 基准） | 1.000 | 1920×1080 | 满屏 |
| 1280×720（16:9 设计器预览） | 0.667 | 1280×720 | 满屏 |
| 2560×1080（21:9） | 1.000 | 1920×1080 | 左右留边 |
| 1024×768（4:3） | 0.533 | 1024×576 | 上下留边 |

**诊断命令**（一次性核对三项）：

```python
by = {str(c.get_name()): c for c in list(wbp.WidgetTree.AllWidgets)}
sl = by['DressScaleBox'].Slot
ld = sl.get_property('LayoutData').as_dict()
print(ld['Anchors']['Maximum'].as_dict())   # 期望 {'x':1.0,'y':1.0}
print(ld['Offsets'])                        # 期望 全 0（零值不序列化，可能打印 {}）
sb = by['DressSizeBox']
print(sb.get_property('WidthOverride'), sb.get_property('bOverride_WidthOverride'))   # 期望 1920.0 True
print(sb.get_property('HeightOverride'), sb.get_property('bOverride_HeightOverride')) # 期望 1080.0 True
```

**文件级复核（UAssetGUI 导出 JSON 后）**：`SizeBox` 的四个字段
`WidthOverride` / `HeightOverride` / `bOverride_WidthOverride` / `bOverride_HeightOverride`
会作为普通属性出现在 Export 数据里，可直接断言；而拉伸态下已归零的 `Offsets`
在 JSON 中表现为 `{"Right": "+0", "Bottom": "+0"}`（`Left`/`Top` 零值省略）。

**设计器观感提示**：`设计师 → 屏幕尺寸` 默认可能是 `1280×720`。按官方建议改为
`1920×1080 (16:9)` 后，设计器内所见即为设计基准尺寸，便于逐控件对位（此设置只影响编辑器预览，不影响运行时）。

---

## 八、相关页面

- [图鉴 UI 高保真还原](图鉴UI高保真还原.md)
- [绿洲 UI 枚举与结构体速查](绿洲UI枚举与结构体速查.md)
- [ZhuJieMian 画刷现状基线表](ZhuJieMian画刷现状基线表.md)
- [UI 页面切换与 Widget 生命周期](UI页面切换与Widget生命周期.md)
- [3D UI 挂载方案](../程序与网络/3DUI挂载方案.md)
- [蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)
- [UGCAskQ MCP 能力矩阵](../工具与流程/UGCAskQ-MCP能力矩阵.md)
- [UGCAskQ MCP 实测陷阱清单](../工具与流程/UGCAskQ-MCP实测陷阱清单.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [配置表驱动开发](../配置与数据/配置表驱动开发.md)
- [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)
- 来源：[2026-08-26 UGCAskQ MCP 编辑器修改能力实测](../来源记录/2026-08-26_UGCAskQ_MCP实测记录.md)
- 来源：[2026-08-26 UI 画刷与控件样式官方查证](../来源记录/2026-08-26_UI画刷与样式官方查证.md)
- 来源：[2026-08-26 图鉴 UI 优化](../来源记录/2026-08-26_图鉴UI优化.md)
- [绿洲 UMG 文本自动包裹与换行](./绿洲UMG文本自动包裹与换行.md)

---

## 九、待查证

**本轮（2026-08-26）已查证并移入正文的原待查证项**：画刷/裁剪/拉伸/换行/贴图组等 12 个枚举整数值（`raw/docs/api/cppenum/`，并与编辑器 `enum:` 反射双向核对）；`FSlateBrush` / `FButtonStyle` / `FSlateFontInfo` / `FFontOutlineSettings` / `FSlateColor` / `FSlateSound` / `FMargin` 全字段与官方说明；`UICommonFunctionLibrary` 的真实类型与 9 个适配函数签名；官方 UI 贴图四项设置；`bAntiAdaptation` 中文名「贴边反适配」；`MutiEllipsisLine` 与异形按钮的 EditCondition 门控链；`MipGenSettings` 正确值为 13。

以下条目**仍未**在 `raw/docs` 官方 API 或 Wiki 中找到直接依据，仅作待验证项，不得当作结论使用：

1. `UICommonFunctionLibrary` 除 `SetAdaptation`（`raw/docs/wiki/进阶内容/UI系统/357_异形屏适配.md` 有官方示例）外，其余 8 个函数（`SetUnAdaptation` / `SetAdaptation_ScreenHole` / `SetAdaptation_Lobby` / `SetAdaptation_Lobby_IPX` / `SetAndroidPhoneAdaptation` / `GetUIRectOffset_WithSetting` / `SetSquareFixedScslr` / `SetTabStyle`）**仅确认了参数签名**，用途为按命名推断，官方无文档，需在 PIE 中逐个验证后才可写成结论。
2. `raw/docs/wiki/开发者须知/271_字体规范.md` 正文**仅有一行图片引用**（`raw/docs/wiki/_assets/images/285b0fde_LDD02.864755c6[1].png`，1731×3712 px）。本轮已切图并读取前两段，图内为大幅纯色/渐变设计稿，**未能提取到可读的字号/字重/行高数值**。因此绿洲官方字体规范的具体数值仍需人工打开原图确认；本页字体族与 fallback 结论来自 Web 通行实践与项目预览页写法，UMG 侧唯一可引用的官方硬结论是 `FSlateFontInfo.Size` 的中文警告（小字体 + 调 Scale，已写入正文）。
3. `UTextBlock` 的 `AutoEllipsisText` / `MutiEllipsisText` / `MutiEllipsisLine` **三者均无官方 ToolTip**（编辑器反射也只给出类型与 Category `Wrapping`、EditCondition 关系）。语义按命名与 UMG 惯例推断，单行/多行省略号的实际截断行为需在 PIE 中验证。
4. `FSlateBrush.bUseImageSizeAsTextureSize` 官方 md 与编辑器反射**均无描述文字**，语义未确认，不要依赖。
5. `FSlateBrush.UVRegion` 用于图集裁切的实际效果未在 PIE 中验证，只有官方字段描述「有效时覆盖资源代理里指定的 UV 区域」。
6. `ResourceObject` 赋 `UMaterialInterface`（实测 `MaterialInstanceConstant` 可写入成功）后的**运行时渲染表现未经 PIE 验证**；`UImage.BrushMaterialParamNames` 官方注明皮肤覆盖材质参数「暂时只支持 PC 上的 Float 参数修改」，移动端行为未验证。
7. `EStretch.ScaleBySafeZone(6)` 与官方异形屏适配方案（`SetAdaptation`）的关系、以及 `CanvasPanelSlot.bAntiAdaptation`（贴边反适配）与该方案如何配合，官方均无说明。
8. `UScaleBox.UserSpecifiedScaleBias` 的官方 ToolTip 只有 `#if UMG_SCALE_BIAS`（宏残留），实际含义未确认。
9. `ESlateBrushImageType` 各值（`FullColor` / `Linear` / `Vector`）的渲染差异官方无描述；`TEXTUREGROUP_LobbyUI(43)` 与 `TEXTUREGROUP_UI(16)` 在绿洲工程内的适用边界亦无说明。
10. Web 侧 `-webkit-line-clamp`、`aspect-ratio`、`overscroll-behavior` 在编辑器内置浏览器/预览环境的支持情况未实测。
11. 社区帖 2233 关于「iOS 两侧安全区引擎层已处理」的答复来自社区归档快照（`syncedAt: 2026-05-31`），未在官方 Wiki 找到对应正式表述。
12. `raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md` 中「Compression Settings：默认使用 TCQ_Default」的 `TCQ_` 前缀与枚举定义不符（`CompressionSettings` 属 `TextureCompressionSettings`，应为 `TC_Default`；`TCQ_` 属 `CompressionQuality`）。本页按枚举定义推断，官方勘误未见，若官方更新需复核。

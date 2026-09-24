# 2026-09-15 AuctionDressUI 装扮UI优化写入与验收

> 类型：项目证据（蓝图与UI · MCP 回读产物）
> 主题：AuctionDressUI 布局/样式/交互视觉优化落地，以及写入后的回读验收
> 适用范围：仅 IslandAuctionKing 项目该资产的本次写入；不含玩法逻辑变更
> 证据状态：**实测**（`ue_py` 回读输出 + 磁盘 MD5 双证）；未证项已单列
> 来源：本轮对话实写；取证目录 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260915_装扮UI优化\`
> 更新时间：2026-09-15
> 关联主题：[MCP-UI编辑与高保真还原知识库](../../知识/通用/UI与交互/MCP-UI编辑与高保真还原知识库.md)、[2026-09-15 装扮UI优化 MCP 写入与截图核验](../../知识/通用/来源记录/2026-09-15_装扮UI优化MCP写入与截图核验.md)、[绿洲UMG设计态缩放裁剪与白块排错](../../知识/通用/UI与交互/绿洲UMG设计态缩放裁剪与白块排错.md)
> 排除范围：装扮业务逻辑（级联选择/材质套用/状态字段）本轮**未改**；结算与保底金 UI 不属本页
> 官方依据：`raw/docs` 中的 UMG/ScaleBox/SizeBox 相关条目（本页结论以实测为准）

---

## 一、写入对象与前置

- 资产：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/AuctionDressUI`
- 绑定脚本：`Script/Blueprint/Prefabs/UI/AuctionDressUI.lua`、`Script/Function/AuctionDressUIService.lua`
  —— **69 个契约控件名不可改**（按名绑定）
- 表：`Asset/Data/Table/Customized/Dress/{DressConfigTable,DressControlTable,DressMaterialTable}`（本轮未改表）
- 写入脚本：`备份\IslandAuctionKing\20260915_装扮UI优化\dress_ui_rewrite.py`（6 个 step，**每次 `ue_py` 只调一个**）
- PRV：`plan_id = plan_16792485_3a4adc98`（TTL 3600s）
- 写前备份：`...\20260915_装扮UI优化\before\AuctionDressUI.uasset`
  - MD5 `A301849B3AEC0984BD9958B522548356`，90,248 B
  - 写入前复算一致 → 备份有效

## 二、写前基线（只读回读）

| 项 | 基线值 |
| --- | --- |
| 控件总数 | 73（`CanvasPanel_0` + `DressScaleBox` + `DressSizeBox` + `DressCanvas` + `DressPanel` + 69 契约） |
| 容器类 | `CanvasPanel_0`/`DressCanvas`/`DressPanel` = CanvasPanel；`UIColumn`/`RegionColumn`/`StyleColumn` = VerticalBox；`DressScaleBox` = ScaleBox；`DressSizeBox` = SizeBox |
| Slot 类 | DressPanel/UIColumn/TitleText/StatusText/CloseButton/PreviewImage = CanvasPanelSlot；UIButton01 = **VerticalBoxSlot** |
| `DressScaleBox` | `Stretch=2 StretchDirection=0 StretchPc=0 StretchDirectionPc=0` ← **PC 端不缩放** |
| `DressSizeBox` | `Width=1920 Height=1080 bOverride_WidthOverride=True bOverride_HeightOverride=True` |
| `UIButton01` 槽位 | `Size={Value:52.0, SizeRule:0}`（Automatic 忽略 Value → 行高失效）、`Padding.Bottom=6` |
| `DressPanel` | `LayoutData.Offsets=(32,96,1856,900)` |

## 三、写入内容

1. **新增 13 个装饰/文案控件**（全部新增，不改名、不删除任何既有控件）
   `ScreenScrim` `PanelBorder` `HeaderLine` `FooterLine` `NavCard` `PreviewCard` `StyleCard` `PreviewWell`（Border）
   `UISectionTitle` `RegionSectionTitle` `PreviewCaptionText` `StyleSectionTitle` `PreviewHintText`（TextBlock）
2. **21 个控件几何**（1920×1080 设计基准；`Anchors` 收为 (0,0)-(0,0)、`Alignment` 显式 (0,0)、左上锚点下 `Offsets.Right/Bottom` 即 Size）
   画布级：`ScreenScrim(0,0,1920×1080)` `PanelBorder(80,40,1760×1016)` `HeaderLine(128,148,1664×2)` `FooterLine(128,1008,1664×1)`
   `TitleText(128,76,460×52)` `StatusText(128,1016,1664×34)` `DressPanel(128,176,1664×824)` `CloseButton(1752,74,56×56)`
   面板级：`NavCard(0,0,388×824)` `PreviewCard(412,0,796×824)` `StyleCard(1232,0,432×824)`
   `UISectionTitle(24,24,160×32)` `RegionSectionTitle(196,24,168×32)` `UIColumn(24,64,160×224)` `RegionColumn(196,64,168×560)`
   `PreviewCaptionText(436,24,748×32)` `PreviewWell(428,56,764×437)` `PreviewImage(436,64,748×421)` `PreviewHintText(436,524,748×60)`
   `StyleSectionTitle(1256,24,384×32)` `StyleColumn(1256,64,384×750)`
3. **样式**：8 个 Border 底色（`scrim #060810/0.74`、`panel #1A1E25/0.97`、`card/0.92`、`divider 白/0.10`、`well #040608/0.92`）；
   7 条静态文案（`TitleText 装扮 32 号金`、4 个列标题 20 号金、`StatusText` 20 号灰并开 `AutoEllipsisText`、`PreviewHintText` 18 号灰开 `AutoWrapText` + `WrapTextAt=748` + `LineHeightPercentage=1.5`）；
   48 个列表按钮四态 TintColor（Normal `45,50,58`、Hovered `64,71,82`、Pressed `79,87,100`、Disabled 金色 `245,163,59/0.26` 作选中态）+ `NormalPadding(2,2,2,2)`/`PressedPadding(2,3,2,1)`；
   48 个行标签字号 22 + 白字 + `AutoEllipsisText`；`CloseLabel` 24 号；`CloseButton` 四态；`PreviewImage` 着色为不透明白
4. **槽位度量**：三列 30 行 `VerticalBoxSlot.Size` 由 `SizeRule=0` 改 **1(Fill)** + `Value=1.0`（`StyleColumn` 末位空槽 `Value=0.0`）；`Padding.Bottom` = 8/8/6（行间距）
5. **适配修复**：`DressScaleBox` `Stretch/StretchPc` 同写 2(ScaleToFit)、`StretchDirection/StretchDirectionPc` 同写 0
   —— PC（`PCD3D_SM5`）取 `*Pc`，原 `StretchPc=0` 使缩放框在 PC 端完全不缩放

## 四、验收（`step4_verify` 全量回读 + 磁盘双证）

| 检查 | 结果 |
| --- | --- |
| 控件总数 | **86**（73 → 86） |
| 21 项几何 vs 设计期望（容差 0.6） | `GEOM_BAD=[]`，逐项 `off/anc/align` 精确命中 |
| 三列槽位抽查 | `SizeRule=1`；`UIButton01/02/04`、`RegionButton01/05/10`、`MaterialButton01/08` `Value=1.0`；`MaterialButton16` `Value=0.0`；`Padding.Bottom` 8/8/6 |
| 契约控件名 | `contract=69 missing=[]` |
| `DressSizeBox` | `1920×1080 ovW/ovH=True`（EditCondition 两阶段保持开启） |
| `DressScaleBox` | `(Stretch, Dir, StretchPc, DirPc) = (2, 0, 2, 0)`，期望一致 |
| 前端写入错误 | `step2 errors=0`、`step3 errors=0` |
| 磁盘（本轮写入后） | `AuctionDressUI.uasset` **90,248 → 179,869 B**；MD5 `A301849B3AEC0984BD9958B522548356` → `A363269184E67FED3FDB6434392569AA` |
| 磁盘（当前态，含 30 个文本 `bIsVariable` 写入 + `compile_blueprint` + `save_package`） | **190,208 B**；MD5 `A7CE78813D7F48108F647559C79A904E` |

## 五、未证项与生效方式

- **未证项（推断）**：画刷 `DrawAs=Box` + `ResourceObject=None` + `TintColor.ColorUseRule=0` 是否真按 `SpecifiedColor` 渲染色。
  机制上成立（该组合在现状下回落纯白底已实测，白 × tint = tint），但本次**截图未命中目标画面**（见下），故无像素级证据。
- **截图核验未通过**：`FlaUiCapture.exe --list` 列出了编辑器窗口；主窗抓图 1936×1048/均值亮度 73.6/白 7.4%，但设计金色 `(245,163,59)` **命中 0 px**；另一候选窗「调试游戏」为 1000×600/亮度 251.75/**95.8% 纯白**（空白占位窗）。
  两图改名留证：`capture_fail_leveleditor_frame.png`、`capture_fail_blank_1000x600.png`。判定方法见 [2026-09-15 着装UI优化 MCP 写入与截图核验](../../知识/通用/来源记录/2026-09-15_装扮UI优化MCP写入与截图核验.md) 第四节。
- **本轮未改**（用户「保持装扮功能逻辑不变」约束）：`Refresh` 不回收多余槽位、`SelectUI` 不恢复分区域状态、`GetLayout/ApplyLayout` 为 no-op。
- **生效方式**：**必须重新调试 PIE**（涉及蓝图结构与控件树变更，不可热更新）。

## 六、复用资产

- 写入脚本 `备份\IslandAuctionKing\20260915_装扮UI优化\dress_ui_rewrite.py`：`step0_preflight()`（只读预检）/ `step1_add(lo,hi)` / `step1_place(lo,hi,save)` / `step2_style()` / `step3_slot_metrics()` / `step5_fix_scalebox_pc()` / `step4_verify()`
- 可运行网页预览 `备份\IslandAuctionKing\20260915_装扮UI优化\AuctionDressPreview.html`（优化后/现状对照 + 5 档视口 + 品质色块/网格叠加）
- 写前备份 `...\20260915_装扮UI优化\before\`（含 6 个 Dress 表资产）

## 七、运行时复验（PIE 实测，2026-09-15 14:38 起两轮会话）

### 7.1 通过项（运行时实测，均来自 PIE 客户端日志与控件级回读）

| 项 | 实测结果 |
| --- | --- |
| 层可实例化 | `CreateAndShow` → `viewportOK=true`、`fadeOK=true`，实例 `AuctionDressUI_C_0/_1` |
| 按钮按名可达 | `BindEvents` 逐条绑定 31 个按钮（`UIButton01-04`/`RegionButton01-10`/`MaterialButton01-16`/`CloseButton`），无「缺失」分支 |
| 材质列表行数 | **15 行**（修正前恒 0） |
| 列表文案写入 | `UIText01=主界面`、`UIText03=结算界面`、`RegionText01=玩家头像`、`MaterialText01=未知品质`、`MaterialText15=金品质已知轮廓`、`StatusText=已选择：主界面 / 玩家头像   材质：未选择` |
| 未用槽位折叠 | `UIButton04=1 ;RegionButton04=1 ;RegionButton10=1 ;MaterialButton16=1`（1=Collapsed），日志 `槽位折叠 uiUsed=3 regionUsed=3 materialUsed=15` |
| 控件总数 | `WidgetTree.AllWidgets=86`；递归实测 `TOTAL=86`，`TARGET_MISSING=[]` |
| 30 个文本 `bIsVariable` | `TARGET_VAR_TRUE=30`；未置 True 的仅 `UIText04`（对应未使用的第 4 个界面槽，已 Collapsed，Lua 不写） |
| 关键属性 | `DressScaleBox (2,0,2,0)`；`DressSizeBox 1920×1080 ovW/ovH=True`；`DressPanel off=(128,176,1664,824)` |
| 三列行槽位 | `UIButton01/RegionButton01/MaterialButton01` 均为 `VerticalBoxSlot SizeRule=1(Fill) Value=1.0`，`Padding.Bottom=8/8/6` |

### 7.2 本轮修复的三处缺陷（写前备份见 `before\`）

1. **材质列表恒 0 行** — 根因：`LoadImageMaterials` 用 `type(x)=="table"` 判定表格与行对象，而 `UGCGameSystem.GetTableData` 返回的 `TableStruct`/`TableDataStruct` 在 Lua 侧恒为 **userdata**，可 `pairs()` 遍历但 `type()` 不为 `table` → 整表被静默跳过。改为非空判定后恢复 15 行。
2. **未使用槽位仍可见** — `Refresh` 只写 `1..#used` 的文案，不清空多余槽位 → 切换界面后残留上一界面的行名。新增 `KeepSlots`（纯展示层，`SetVisibility(Visible/Collapsed)`），不改玩法逻辑。
3. **30 个列表文本 Lua 取名不可达** — 该 30 个 `TextBlock` 的 `bIsVariable=False` → `widget["UIText01"]` 取不到对象，`SetText` 未执行。经 MCP 全量置 `True` + `compile_blueprint` + `save_package`，回读 `still_false=NONE`、`btn_bad=NONE`。

## 八、未结项：30 个「按钮内文案」运行时无可见字形

**现象**：`UIText01` 等 30 个文本控件位于 `VerticalBox → 按钮 → ButtonSlot.Content`，运行时文案已写入（见 7.1）但画面上不出现字形；同为文本、直接挂在 `DressPanel`/`DressCanvas` 下的表头/提示/状态/标题则正常绘制。

### 8.1 双侧证据（本轮实测）

| 侧 | 项 | 实测值 |
| --- | --- | --- |
| 资产侧（ue_py 回读） | `Font` | `Roboto` / `TypefaceFontName=Bold` / `Size=22`（表头同为 Roboto/Bold，`Size=20`） |
| 资产侧 | `ColorAndOpacity` | 行标签 `(0.929,0.929,0.937,1)`；表头 `(0.961,0.639,0.231,1)`；均 `ColorUseRule=0` |
| 资产侧 | `Visibility/RenderOpacity/Justification/AutoWrapText` | `0 / 1.0 / 0(左) / False`，与表头同构 |
| 资产侧 | 行按钮四态画刷 | `DrawAs=1(Box)`、`ResourceObject=None`、`Normal TintColor=(0.176,0.196,0.227,0.96)`、`Disabled=金色(0.961,0.639,0.231,0.26)` |
| 资产侧 | 按钮自定义图层属性 | `bIsLayerPlus/bUseCustomSettings/bStyleHidding/bStyleRemove/bStyleInsertInvBox/bStyleInsertRetainerBox=False`，`ZValue=AreaTypeFlags=UsedLayerPolicy=PreservedLayerNum=FixedLayerPolicy=FixedLayerNum=0`，`Clipping=0` |
| 资产侧 | `ButtonSlot` | `Padding=(4,2,4,2)`、`HorizontalAlignment=2(Center)`、`VerticalAlignment=2(Center)` —— **与正常绘制的 `CloseLabel` 完全一致** |
| 像素侧（`pie_dress_final.png` 1280×720） | 左列整列 `x101..208,y160..310` | 亮像素(>150) **0**（max=123） |
| 像素侧 | 区域列整列 `x216..328,y160..533` | 亮像素(>150) **53**（且集中在 x320..327 右缘，非字形分布） |
| 像素侧 | 样式列整列 `x923..1179,y160..660` | 亮像素(>150) **497**（若干 14×14 小块，集中在列左缘） |
| 像素侧（对照，均正常） | `UISectionTitle` / `CloseButton` / `StatusText` / `PreviewHintText` | 亮像素 **208 / 99 / 1478 / 2021**，且呈连续字形行分布（如 `StatusText` 占 `x87..416 × y679..695`） |

**判据**：行标签字色为近白（亮度 ≈237），若绘制则必然在行区内产生大量 >150 的像素。实测左列整列亮像素为 0 → **该 30 个标签确实未绘制字形**，而非「绘制了但对比度低」。

### 8.2 已排除（逐项实测）

文案内容（`GetText()` 非空）、颜色与 `ColorUseRule`、字号/字面/字体资产（与可正常绘制的表头同字体同字面）、`Visibility`、`RenderOpacity`、`RenderTransform`、`ButtonSlot` 内边距与对齐（与 `CloseLabel` 逐字段相同）、行按钮四态画刷与 `NormalPadding/PressedPadding`、自定义图层属性（全为默认 0/False）、槽位度量（`SizeRule=1 + Value=1.0`）、`GetContent()` 归属（为真）。

### 8.3 剩余候选与判据（未执行）

1. **排布层假设**：该 30 个标签位于 `VerticalBox → 按钮 → ButtonSlot`，而所有可正常绘制的文本都挂在 Canvas 槽位（包括 `CloseButton` 内的 `CloseLabel`）。建议先做**不改资产的运行时颜色探针**（`doluastring` 把行标签临时置为纯红）——若红色字形出现，则为颜色/层级问题（属纯样式改，可直接落地）；若仍无字形，则需把标签改为行按钮的**兄弟节点**（Canvas 槽位）承载，属控件树组合变更。
2. **验证方式**：每次改动后重抓 PIE 客户端绘制区并按 8.1 的像素判据复测；`GetDesiredSize()` 在本引擎设计态与运行时**恒返回 (0,0)**（含可见控件），不可作为几何判据。

### 8.4 本轮工具事实（可复用）

- **模板态递归必须走 `Slots`**：对 `Button`/`Border`/`Image` 直接访问 `.Content` 会抛 `'UObject' object has no attribute 'Content'` → 漏掉整棵子树（本轮首测据此误得 `TOTAL=55`）。统一用 `for s in w.Slots: walk(s.Content, ...)` 后得 `TOTAL=86`。
- 模板态 `GetText()` 返回 **str**（运行时返回 FText），写成 `t.ToString()` 会抛 `'str' object has no attribute 'ToString'`。
- `st.get_field('Normal')` 取到的 `FSlateBrush` 上，`get_field('TintColor')` 返回 `UScriptStruct(SlateColor)`，需再 `get_field('ColorUseRule')` / `get_field('SpecifiedColor')`；`FButtonStyle` 本身**不支持 `.properties()`**。
- 递归读树**不需要 plan**（纯查询）；`ue_py` 报错时事务自动回滚（`recovery_hint: Transaction was cancelled`）。
- 像素量测法：以设计坐标 × `min(视口/设计)` 反算运行时矩形，再用 `numpy` 统计 `median/p2/p98` 与 `>150` 亮像素计数、并输出亮像素 bbox 与逐行分布 —— 这是「模型不可读图」时判定「某控件是否绘制」的确定性手段。

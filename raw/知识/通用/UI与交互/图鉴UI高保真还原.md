# 图鉴 UI 高保真还原

> 来源：[2026-08-26 图鉴 UI 优化](../来源记录/2026-08-26_图鉴UI优化.md)、项目证据：[IslandAuctionKing UI 贴图批量修正 MCP 回读](../../../IslandAuctionKing/日志证据/2026-08-26_UI贴图批量修正MCP回读.md)、项目实战产物 `<IslandAuctionKing>/Preview/CollectibleCodexOptimizedPreview.html`、`raw/docs/ai/20260824_图鉴UI素材批量导入与视觉优化.md`
> 官方依据：`raw/docs/wiki/进阶内容/UI系统/20269_UI自适应屏幕.md`（1920×1080 设计基准与「画布→缩放框→尺寸框→画布」层级）、`raw/docs/wiki/新手入门/资源管理与编辑/277_资源导入.md`（PNG/JPG/TGA 拖入 Asset 指定目录默认导入）、`raw/docs/api/cppstruct/F/FS/FSlateBrush.md`（画刷字段）
> 社区依据：sq-skill 归档帖 2193（`<CODEX_HOME>/skills/sq-skill/docs/community/replies/2193.md`，ScrollBox 子控件必须 `AddChild`）
> 适用范围：《海岛竞拍王》藏品图鉴（`CollectibleCodexUI` + `CollectibleCodexItemUI`），同时作为「素材驱动的列表型全屏 UI」通用还原契约参考。

---

## 一、核心结论

1. **交付顺序不可颠倒**：`$ui-ux-pro-max` 设计 → 可运行网页预览 → 用户明确回复「预览没问题」 → UGCAskQ MCP 写 UMG → 立即 `widget_inspect` 回读。在用户确认前**不得**改 UMG 与 Lua。
2. **预览页必须与 UMG 1:1**：舞台固定 1920×1080，所有控件绝对定位，HTML `id` 与 UMG 控件名同名，用 `transform: scale()` 自适应。这样预览坐标可直接当作 `Slot.SetPosition/SetSize` 的入参。
3. **素材落位必须机器自检**，不能靠「我复制了」的口头断言。判据：`assets/items/*.png` 数量等于表行数、无 `undefined.png`、数据文件 `missingPng` 为空数组。
4. **所有可调数值先在预览页收敛为 `CFG` 对象，行名直接用未来 DataTable 的点号路径**，落地时可 1:1 搬进 `Asset/Data/Table/Customized/UI/UIConfigTable`，避免二次改名。
5. `file://` 在 in-app browser 被策略拦截，预览验证必须走本地 HTTP；且 HTTP 服务须是独立 `.js` 脚本常驻，不能寄存在 node REPL 的 `globalThis`。

---

## 二、素材映射契约（`Asset/TuPian/TuJian` 11 张）

| 预览页文件 | 像素 | 中文素材语义 | UMG 控件 | 画刷参数 |
| --- | --- | --- | --- | --- |
| `footer_base.png` | 2160×1266 | 背景底 | `Codex_BackgroundBase` / `Codex_FooterFrame` | `DrawAs=Box(1)` + `Margin` |
| `top_bar.png` | 1582×93 | 最顶部 UI | `Codex_TopBar` | `DrawAs=Box(1)` |
| `filter_panel.png` | 383×844 | 左侧 UI 选项 | `Codex_FilterPanel` | `DrawAs=Box(1)` |
| `filter_button.png` | 101×41 | 左侧选项格 | `Codex_FilterButton` | 四态各设 `DrawAs=Box(1)` |
| `gallery_panel.png` | 1181×769 | 右侧图鉴层 | `Codex_GalleryPanel` | `DrawAs=Box(1)` |
| `card_slot.png` | 242×253 | 藏品格子 | `Codex_CardFrame` | `DrawAs=Box(1)` |
| `name_frame.png` | 145×50 | 名称 UI | `Codex_NameFrame` | `DrawAs=Box(1)` |
| `plate_base.png` | 210×52 | 底板 | **UMG 无对应，需新建 Border** | `DrawAs=Box(1)` |
| `scroll_track.png` | 22×743 | 滚轮底 | `Codex_ScrollTrack` | `DrawAs=Box(1)` |
| `scroll_thumb.png` | 22×51 | 滚轮 | `Codex_ScrollThumb` | `DrawAs=Box(1)` |
| `close.png` | 90×69 | 退出叉号 | `Codex_Close` | `DrawAs=Image(3)` |

导入参数按官方 UI 贴图规范五项：`LODGroup=16`（`TEXTUREGROUP_UI`）、`MipGenSettings=13`（`TMGS_NoMipmaps`）、`CompressionSettings=0`（`TC_Default`）、`CompressionQuality=5`（`TCQ_Highest`）、`SRGB=True`。

> **2026-08-26 修正**：这 12 张 `Codex_*` 导入时 `CompressionQuality` 均为 `0 (TCQ_Default)`，不符官方要求，已通过 MCP 批量改为 `5` 并回读通过。详见 [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md) 与 [IslandAuctionKing UI 贴图批量修正 MCP 回读](../../../IslandAuctionKing/日志证据/2026-08-26_UI贴图批量修正MCP回读.md)。

---

## 三、控件坐标契约（1920×1080）

主界面 `CollectibleCodexUI`：

```
BackgroundPanel     0,0      1920×1080
TopBarPanel         24,18    1872×72
  TitlePlate        44,29    236×50     (plate_base + TitleText)
  ProgressPlate     300,29   430×50     (ProgressText + ProgressTrack/ProgressBar)
  SubtitleText      754,36   900×36
  CloseButton       1818,22  64×64
FilterPanel         24,102   448×844
  FilterTitleText   50,124   372×30
  筛选按钮网格      x=50 起，3 列，宽 118 高 36，列距 9 行距 6
    section top = {Status:162, Quality:240, Type:402, Shape:564}
    标题块置于 top，按钮起始 top+34
  ClearFiltersButton 50,764  372×46
  FilterFootNote    50,820   372×40
GalleryPanel        486,102  1410×844
  汇总胶囊 4 个     x=502 起，top=120，宽 268 高 36，间距 8
    CodexResultSummaryText / CodexQualitySummaryText / CodexTypeSummaryText / CodexShapeSummaryText
  SortButton        502+4×276, 120, 宽 274 高 36
  ItemScrollBox     502,168  1378×764   (padding 12/8/14/12)
  ItemWrapBox       grid repeat(5, 256px) gap 14
FooterPanel         24,960   1872×96
  FooterHintText    56,988   900×40
  FooterStatText    1050,988 820×40
ToastText           760,892  400×44
DetailPanel         540,214  840×600    (6 行 meta；dline left=910 宽 456 高 34，top 306→516 步进 42)
  DetailArt         574,300  300×300
```

卡片 `CollectibleCodexItemUI`（**256×268**，原 UMG 为 300×276，本轮建议改窄以容纳 5 列）：

```
QualityBar          0,0      256×6     (品质色)
ItemArt             10,12    236×182   (未收集态 filter: brightness(0) opacity(.34))
  ItemImage          34,7     168×168   (统一展示框；object-fit: contain，保留原始画布比例)
NameFrameImage      8,8      152×34    z-index 1
ItemNameText        14,12    140×26    z-index 2
CollectionStateText right:18, top:162, 高 22, z-index 2
MetaRow             14,204   228×24    grid 56px/1fr/52px → TypeQualityText / DetailHintText / ShapeText
ValueRow            14,232   228×26    grid 1fr/auto     → ValueText / IncomeText
```

配色变量：`--orange:#f6a334`、`--gold:#ffba4b`、`--line:#131516`、`--text:#f8f5ed`、`--muted:#d0cbc1`；
六品质色：`白 #c7cdd4`、`绿 #63d776`、`蓝 #68adff`、`紫 #d081ff`、`金 #ffd15e`、`红 #ff7474`。

---

## 四、CFG 常量清单（13 项，直接对应 UIConfigTable 行名）

| 行名 | 类型 | 值 | 用途 |
| --- | --- | --- | --- |
| `UI.Codex.Columns` | int | 5 | 画廊列数 |
| `UI.Codex.ItemWidth` | int | 256 | 卡片宽 |
| `UI.Codex.ItemHeight` | int | 268 | 卡片高 |
| `UI.Codex.ItemGap` | int | 14 | 卡片间距 |
| `UI.Codex.FilterButtonWidth` | int | 118 | 筛选按钮宽 |
| `UI.Codex.FilterButtonHeight` | int | 36 | 筛选按钮高 |
| `UI.Codex.FilterColumnGap` | int | 9 | 筛选按钮列距 |
| `UI.Codex.FilterRowGap` | int | 6 | 筛选按钮行距 |
| `UI.Codex.SummaryWidth` | int | 268 | 汇总胶囊宽 |
| `UI.Codex.SummaryHeight` | int | 36 | 汇总胶囊高 |
| `UI.Codex.SummaryGap` | int | 8 | 汇总胶囊间距 |
| `UI.Codex.SortButtonWidth` | int | 274 | 排序按钮宽 |
| `UI.Codex.ToastDuration` | float | 2.0 | 提示条驻留秒数 |
| `UI.Codex.ItemImageSize` | int | 168 | 藏品图统一显示框边长 |

落位路径：`Asset/Data/Table/Customized/UI/UIConfigTable`（4 列 `ValueType` / `Value` / `Description` / `ModificationNotes`），并在 `Script/Function/AuctionConfig.lua` 追加注册。Lua 侧**必须在函数内**经 `AuctionConfig.GetNumber` 读取并带默认回退，见 [配置表驱动开发](../配置与数据/配置表驱动开发.md)。

---

## 五、筛选与排序契约

`Script/Function/CollectibleCodexUIService.lua` 第 42-78 行定义了 `SORT_MODES`（4 种）与 `FILTER_BUTTONS`（29 个按钮）。预览页 `GROUPS` / `SORT_MODES` 与之逐项一致。

- `SORT_MODES`：`value-desc`（估值从高到低）/ `value-asc` / `quality`（品质从高到低）/ `name`（名称升序）
- `QUALITY_RANK`：白 1 / 绿 2 / 蓝 3 / 紫 4 / 金 5 / 红 6
- `FILTER_BUTTONS` 分组：Status 3 项、Quality 7 项（含「全部」）、Type 7 项（含「全部」）、Shape 12 项（含「全部」）

**易错点**：Quality/Type/Shape 三组各含一个 `Value = ""` 的「全部」按钮。统计实际筛选值时必须剔除它，否则会得出「Lua 7 类型 vs 表内 6 类型」「Lua 12 形状 vs 表内 11 形状」的假差异。剔除后与 CollectibleTable 完全一致，无缺口。

形状值使用**全角 `×`**（U+00D7），不是小写字母 `x`；`FILTER_BUTTONS` 的控件名却用半角（`Shape1x1Button`），二者不可混用。

---

## 六、可执行步骤：落地顺序

1. **备份**：复制 `Asset/Blueprint/Prefabs/UI/CollectibleCodexUI.uasset` 与 `CollectibleCodexItemUI.uasset` 到 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\<YYYYMMDD>_<Theme>\`，并通知用户该绝对路径。
2. **Resolve**：`ue_read queries=["py:workflow blueprint","schema:UScrollBox","schema:UImage"]` 确认属性路径。
3. **Plan**：`ue_plan_submit`，`asset_path` 用 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexUI`。
4. **Execute**：贴图赋值走 Python 直接属性写入（**禁用 `widget_set_property` 写画刷**），坐标走 `Slot.SetPosition/SetSize/SetAnchors/SetAlignment`（**禁用 `widget_slot` 直写**）。
5. **验证**：`compile_blueprint` → `save_package` → `widget_inspect` 回读控件树与坐标；画刷需自己 Python 读回（`widget_inspect` 不返回画刷）。
6. **Lua**：改 `Script/Function/CollectibleCodexUIService.lua`，把硬编码迁移到 `AuctionConfig.Get*`。
7. **配置表**：新建 `Customized/UI/UIConfigTable`，登记 CFG 13 项，在 `AuctionConfig.lua` 注册路径。
8. **生效方式**：涉及蓝图结构、配置表、初始化 → **重新调试 PIE**。

---

## 七、常见错误

| 现象 | 原因 | 正确做法 |
| --- | --- | --- |
| 预览页藏品图全是占位/404 | 数据文件缺 `tex` 字段，模板里 `it.tex` 为 `undefined`，70 个请求折叠成同一个 `undefined.png` | 生成数据时必须带 `tex`；落盘后跑数量与 `undefined.png` 双重自检 |
| 声称素材已复制但目录为空 | 只做了逻辑不做落盘校验 | 复制后立刻 `Get-ChildItem ... .Count` 与 `missingPng` 断言 |
| 中文素材名匹配不上表内条目 | 素材名与表内 Name 存在人工命名漂移（如「罐装午餐肉」vs「午餐肉罐头」） | 先精确匹配（品质目录 + 归一化名），剩余走人工核定别名表，别名表写进知识库来源页 |
| 统计出「Lua 定义比表数据多一项」 | 把 `Value = ""` 的「全部」按钮计入了筛选值 | 统计前剔除 `Value == ""` 的项 |
| 形状筛选点了没反应 | 全角 `×` 与半角 `x` 混用 | 筛选值统一全角 `×`，控件名保持半角 |
| 卡片按 300×276 排 5 列会溢出 | `ItemScrollBox` 内宽 1378，`5×300+4×14 = 1556 > 1378` | 改卡片为 256 宽：`5×256+4×14 = 1336 ≤ 1378` |
| 横图、竖图在卡片中视觉大小不一致 | 直接以 `ItemArt` 的 236×182 外框等比包含，素材画布比例会改变实际渲染面积 | `ItemImage` 固定为居中的 168×168 展示框，使用 `object-fit: contain`，不拉伸也不裁切 |
| 未收集藏品信息被遮挡 | 未收集态将图片压黑、名称替换为 `？？？`，估值和产出显示为未知 | 未收集态照常显示图片、名称、品质/类型/形状、参考估值、每小时产出，仅保留“尚未收集”状态；点击仍可打开完整详情 |
| `ItemWrapBox` 里 `AddChild` 之外的方式加卡片无效 | ScrollBox/WrapBox 子控件必须走 `AddChild`（社区帖 2193） | 统一 `AddChild` |
| 图鉴滚动条仍是引擎默认样式 | `Codex_ScrollThumb` / `Codex_ScrollTrack` 未应用 | 落地时设置 ScrollBox 的滚动条样式画刷，写后目视比对 |
| 本轮统一藏品图尺寸 | 不同素材的原始画布比例不同，直接等比包含在 `236×182` 外框时视觉面积不一致 | 网页预览 `.ItemImage` 固定为居中 `168×168` 展示框，`object-fit: contain` 保留比例且不拉伸、不裁切 |

---

## 八、相关页面

- [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md)
- [绿洲 UI 枚举与结构体速查](绿洲UI枚举与结构体速查.md)
- [配置表驱动开发](../配置与数据/配置表驱动开发.md)
- [配置表与结构体的 MCP 编辑](../工具与流程/配置表与结构体的MCP编辑.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [UI 页面切换与 Widget 生命周期](UI页面切换与Widget生命周期.md)
- [PIE 调试与热更新边界](../工具与流程/PIE调试与热更新边界.md)
- 来源：[2026-08-26 图鉴 UI 优化](../来源记录/2026-08-26_图鉴UI优化.md)

---

## 九、待查证

1. `Codex_ScrollThumb` / `Codex_ScrollTrack` 应用到 `UScrollBox` 的确切属性路径（疑为 `WidgetBarStyle` 系列）**未经反射确认**，落地前需 `ue_read queries=["schema:UScrollBox"]` 核对。
2. 卡片由 300×276 改为 256×268 是否被产品接受，**未获用户确认**；`SortButton` 去留同样待定。
3. `UIConfigTable` 是新建还是沿用 `AuctionGlobalConfigTable`，**待用户决策**。当前 `Asset/Data/Table/Customized/` 下只有 7 张平铺表，无 `UI/` 子目录。
4. 预览页 `::-webkit-scrollbar` 贴图滚动条与 UMG 原生滚动条的视觉一致性未验证。
5. `plate_base.png`（210×52）在 UMG 中无对应控件，新建 Border 的九宫格 `Margin` 取值未实测。
6. 未收集态在预览中用 CSS `filter: brightness(0) opacity(.34)` 表达，UMG 侧的等价实现（`Brush.TintColor` 压黑 + Alpha，或材质）**未验证**。

---

## 2026-08-28 藏品格子蓝图补充

- 目标子蓝图 `/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/CollectibleCodexItemUI.CollectibleCodexItemUI` 已通过 UGCAskQ MCP 的 Resolve -> Plan -> Execute 写入并回读。
- 卡片基础尺寸固定为 `256x268`；新增 `ItemArt` Border，位置 `(10,12)`、尺寸 `236x182`、ZOrder `0`；`CardBackground` 使用 `Codex_CardFrame`，`NameFrameImage` 使用 `Codex_NameFrame`，均先检查 Texture2D 类型后再写入画刷资源。
- 文字默认字体修正为网页对应值：`ItemNameText=14`、`TypeQualityText=13`、`ValueText=14`、`IncomeText=14`、`CollectionStateText=12`；设计器截图确认不再重叠。
- `ItemImage` 设计态设为 `Collapsed` 且透明，避免无 DataTable 动态贴图时显示白色占位；运行时 `CollectibleCodexUIService.InitializeItemWidget` 在 `row.Texture` 存在时重新设置画刷、白色 Tint 并显示。
- 设计态截图：项目 `Screenshots/FlaUI/collectible_codex_item_round1_20260828.png`、`collectible_codex_item_round2_20260828.png`。运行态截图未完成，原因见 [2026-08-28 图鉴 UI 蓝图 MCP 高保真迭代](../来源记录/2026-08-28_图鉴UI蓝图MCP高保真迭代.md)。

## 2026-08-28 MCP 蓝图迭代补充

- CanvasPanelSlot 的位置和尺寸使用 `Slot.SetPosition(ue.FVector2D(x, y))`、`Slot.SetSize(ue.FVector2D(w, h))`；`widget_slot` 仅用于已验证支持的 `ZOrder` 等字段。
- `widget_add` 后不能继续使用旧的 `WidgetTree.AllWidgets` 缓存查找新增节点；使用 `ue.tobject_iterator(ue.find_class("Widget"))` 获取句柄，再用 `ue.widget_inspect` 回读层级。
- 筛选 Button 使用 `Codex_FilterButton` 画刷时，`BackgroundColor` 应保持白色以显示贴图原色；深灰底色会与画刷 Tint 相乘，导致按钮过暗。
- 左侧分组标题需要橙色条时，优先用 `ue.widget_wrap` 原地包裹现有 TextBlock，再刷新蓝图对象后设置 Border wrapper 的 `BrushColor`；该路径保留原 Canvas Slot，已验证标题无偏移。
- 设计器中旧 TextBlock 可能在 `Collapsed` 回读后仍残留缓存绘制；将其默认 `Text` 清为空格并重新编译、保存、刷新，可消除旧长文本造成的视觉串位。
- 用户指定的顶部筛选结果行素材为 `Codex_FooterFrame.Codex_FooterFrame`（源尺寸 `210x52`），底部 `FooterPanel` 素材为 `Codex_TopBar.Codex_TopBar`（源尺寸 `1582x93`）；使用前应先以 UGCAskQ MCP 回读资源类型与尺寸。

### 可执行验证

1. 备份目标 `.uasset`。
2. 以目标蓝图绝对资产路径提交 PRV Plan。
3. 通过 MCP Python 修改 `Slot.SetPosition/SetSize` 或复制画刷结构，执行 `compile_blueprint`、`save_package`。
4. 用 `ue.widget_inspect` 与布局属性回读，再用 FlaUI 截图比对。

### 常见错误

- 用 `widget_slot` 写 `Position` 或直接重写 `LayoutData`，可能返回成功但把偏移清零。
- 从 `unreal_engine.structs` 导入 `FVector2D`，当前环境会产生 ImportError；使用 `ue.FVector2D`。

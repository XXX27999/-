# ZhuJieMian 画刷现状基线表

> 来源：[2026-08-26 UI 资产修正与画刷基线导出](../来源记录/2026-08-26_UI资产修正与画刷基线导出.md)、项目证据：[IslandAuctionKing UI 贴图批量修正 MCP 回读](../../../IslandAuctionKing/日志证据/2026-08-26_UI贴图批量修正MCP回读.md)（会话日期 2026-08-26，UGCAskQ MCP 纯查询导出 + 第 7 轮批量写入）
> 官方依据：`raw/docs/api/cppstruct/F/FS/FSlateBrush.md`、`raw/docs/api/cppenum/E/ES/ESlateBrushDrawType.md`、`raw/docs/api/cppenum/E/ES/ESlateBrushTileType.md`、`raw/docs/api/cppenum/E/ES/ESlateBrushMirrorType.md`、`raw/docs/api/cppenum/E/ES/ESlateBrushImageType.md`、`raw/docs/api/cppenum/E/ES/ESlateColorStylingMode.md`、`raw/docs/api/cppenum/T/TE/TextureGroup.md`、`raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md`
> 采集对象：`/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian`（`UGCWidgetBlueprint`，**2026-08-26 基线时控件树 23 个控件：1 个 `CanvasPanel` + 14 个 `Image` + 8 个 `TextBlock`；2026-09-14 复采为 46 个控件**，差异见「一·A」节）
> 采集方式：`ue_py` 纯查询（PRV `decision: pass`、`has_mutation: false`），从 `WidgetTree.RootWidget` 递归 `GetChildrenCount()`/`GetChildAt(i)`，逐个读 `Brush` 字段与 `Slot.LayoutData`。**未对该 UI 做任何写入。**
> 用途：改这套主界面画刷前的**回滚基线**与**一致性对照**。改动后可用本页复跑同一段查询代码比对差异。

---

## 核心结论

1. **14 个 Image 全部走 `Brush`，`BrushImage` 全为 `None`** —— 从实际资产层面证实项目里改样式改的是 `Brush`，「画刷 图像」字段在本工程完全未被使用。
2. **画刷参数高度同构**：14 个控件的 `DrawAs` 全为 `Image(3)`、`Tiling`/`Mirroring`/`ImageType` 全为 `0`、`Margin` 全为 0、`TintColor` 全为纯白且 `ColorUseRule=UseColor_Specified(0)`、`ResourceName` 全为 `None`。差异只在 `ResourceObject` 与 Slot 布局。
3. **`ImageSize` 全为默认 `(32,32)` 且不起作用**：`DrawAs=Image(3)` 下实际显示尺寸由 `CanvasPanelSlot` 的 Offsets 决定，`ImageSize` 只在 Slot 用 `bAutoSize` 或未指定尺寸时才参与期望尺寸计算。这套 UI 全部 `bAutoSize=False` 且给了显式尺寸，所以 `(32,32)` 是无害残留值。
4. **`ZJM1` 被三个控件复用**（每日任务/帮助/保底金 的「上方UI」），`ZJM3` 被两个控件复用（玩家名称、服务器剩余时间）。改这两张贴图会同时影响多个控件。
5. **`Margin` 全为 0 是与 `DrawAs=Image` 匹配的**（官方：Image 模式忽略 Margin）。若后续要把某张底图改成九宫格拉伸，必须**同时**把 `DrawAs` 改成 `Box(1)` 并给 `Margin`，只改一个不生效。
6. **贴图属性已全量合规（2026-08-26 第 7 轮修正完成）**：`ZJM1`–`ZJM11` 与 `TuJian/Codex_*` 共 23 张 UI 贴图，现已全部为 `LODGroup=16 / MipGenSettings=13 / CompressionSettings=0 / CompressionQuality=5 / SRGB=True`，与官方「UI贴图设置」逐项一致，回读校验 `ALL_23_COMPLIANT=True`。修正前状态与差异见下「二、贴图侧现状」的 before/after 两列。

---

## 一、画刷现状对照表（14 个 Image，2026-08-26 基线）

统一项（14 个控件完全一致，表中不再重复）：`DrawAs=3 (Image)`、`Tiling=0 (NoTile)`、`Mirroring=0 (NoMirror)`、`ImageType=0 (NoImage)`、`Margin=(0,0,0,0)`、`TintColor.SpecifiedColor=(1,1,1,1)`、`TintColor.ColorUseRule=0 (UseColor_Specified)`、`ResourceName=None`、`BrushImage=None`、`ImageSize=(32,32)`、`Visibility=0`、`Clipping=0 (Inherit)`、`bAutoSize=False`、`bAntiAdaptation=False`、`Alignment=(0,0)`。

| # | 控件名 | `Brush.ResourceObject` | ZOrder | 锚点 Min–Max | Offsets (L,T,R,B) |
| --- | --- | --- | --- | --- | --- |
| 1 | 参考图 | `ZJM2` (Texture2D) → **2026-09-14 实测为 `None`，写入后为 `ZJMBackground`** | **-5** | (0,0)–(1,1) 四向拉伸 | (0,0,0,0) |
| 2 | 地图UI | `ZJM4` (Texture2D) | 0 | (1,0.5)–(1,0.5) 右中 | (-474,-214,496,374) |
| 3 | 头像框 | `ZJM5` (Texture2D) | 0 | (0,1)–(0,1) 左下 | (47,-173,154,154) |
| 4 | 玩家名称 | `ZJM3` (Texture2D) | -1 | (0,1)–(0,1) 左下 | (60,-235,585,319) |
| 5 | 服务器剩余时间 | `ZJM3` (Texture2D) | -1 | (0,1)–(0,1) 左下 | (100,-215,397,196) |
| 6 | 金币UI | `ZJM9` (Texture2D) | 0 | (1,0)–(1,0) 右上 | (-424,-56,390,206) |
| 7 | 金币 | `ZJM8` (Texture2D) | 0 | (1,0)–(1,0) 右上 | (-328,24,69,66) |
| 8 | 顶部UI | `ZJM10` (Texture2D) | 0 | (0,0)–(0,0) 左上 | (44,-212,675,523) |
| 9 | 每日任务 | `ZJM7` (Texture2D) | 0 | (1,1)–(1,1) 右下 | (-433,-168,169,167) |
| 10 | 帮助 | `ZJM6` (Texture2D) | 0 | (1,1)–(1,1) 右下 | (-314,-168,164,168) |
| 11 | 保底金 | `ZJM11` (Texture2D) | 0 | (1,1)–(1,1) 右下 | (-163,-137,102,101) |
| 12 | 每日任务上方UI | `ZJM1` (Texture2D) | -1 | (1,1)–(1,1) 右下 | (-396,-159,95,28) |
| 13 | 帮助上方UI | `ZJM1` (Texture2D) | -1 | (1,1)–(1,1) 右下 | (-278,-159,94,30) |
| 14 | 保底金上方UI | `ZJM1` (Texture2D) | -1 | (1,1)–(1,1) 右下 | (-159,-159,94,30) |

读表要点：

- **锚点非拉伸时**（Min==Max，第 2–14 项），Offsets 语义是 `(X, Y, Width, Height)`；本表 R/B 两列即宽高。
- **锚点四向拉伸时**（第 1 项 参考图），Offsets 语义是 `(Left, Top, Right, Bottom)` 四边留白，全 0 表示铺满父级。这也是 `Slot.GetSize()` 对该控件返回 `(0,0)` 的原因——不是尺寸为零，而是拉伸模式下 Size 不参与计算，**不要据此判断控件异常**。
- `参考图` 的 `ZOrder=-5` 最低，是设计稿垫图；正式交付前应确认它是否需要隐藏或删除。

---

## 一·A、2026-09-14 复采差异（本页上半部分已部分过期）

以 2026-09-14 MCP 反射回读为准（`ZhuJieMian`，46 个控件、其中 14 个 `Image`），第 22 节表格存在三处过期：

| 项 | 2026-08-26 基线 | 2026-09-14 实测 |
| --- | --- | --- |
| 控件树总数 | 23（1 `CanvasPanel` + 14 `Image` + 8 `TextBlock`） | **46**（新增 `ScaleBox`+`SizeBox` 适配层、按钮与更多文本） |
| `参考图.Brush.ResourceObject` | `ZJM2` | 复采时为 **`None`**；本轮写入后为 `ZJMBackground` |
| `地图UI`（`ZJM4`） | 存在，右上锚点 | **已不存在**；同区域现为 `Image_160`（`ZJM12`）；`ZJM4` 当前无人引用 |

未变化：`参考图` 的 `ZOrder=-5`、四向拉伸锚点 `(0,0)-(1,1)`、Offsets 全 0；`ZJM1` 仍被 3 个「上方UI」共用，`ZJM3` 仍被 2 个控件共用（`ZJM12` 现被 `Image_160` 引用）。

2026-09-14 全部 14 个 `Image` 的 `ZOrder` 复采值：`参考图=-5`、`玩家名称=-1`、`服务器剩余时间=-1`、`每日任务上方UI=-1`、`帮助上方UI=-1`、`保底金上方UI=-1`，其余（`头像框`/`金币UI`/`金币`/`顶部UI`/`每日任务`/`帮助`/`保底金`/`Image_160`）为 `0`。

> 采集方式仍为 `ue_py` 纯查询递归 `Slots`→`Content`（本工程 `WidgetTree.AllWidgets` 恒为空，**必须递归**；`w.properties()` 返回属性名而非子控件，不能用于遍历）。
> 项目侧完整证据：[2026-09-14 ZhuJieMian 主界面底图导入与设置](../../../IslandAuctionKing/蓝图与UI/2026-09-14_ZhuJieMian主界面底图导入与设置.md)。

---

## 二、贴图侧现状（同目录 11 张）

目标态（官方「UI贴图设置」，`raw/docs/wiki/新手入门/资源管理与编辑/资源编辑/300_贴图与材质编辑.md` 第 2 节）：`LODGroup=16` / `MipGenSettings=13` / `CompressionSettings=0` / `CompressionQuality=5` / `SRGB=True`。

`/IslandAuctionKing/Asset/TuPian/ZhuJieMian/` 全量 before → after（before 为 2026-08-26 首次采集值，after 为第 7 轮批量修正并回读的值）：

| 贴图 | LODGroup | MipGenSettings | CompressionSettings | CompressionQuality | SRGB | 结果 |
| --- | --- | --- | --- | --- | --- | --- |
| ZJM1 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM2 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM3 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM4 | 0 → **16**（第 6 轮） | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM5 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM6 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM7 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM8 | 0 → **16** | **0 → 13** | 0 | 0 → **5** | True | ✅ 合规（唯一 MipGen 也需改的一张） |
| ZJM9 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM10 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |
| ZJM11 | 0 → **16** | 13 | 0 | 0 → **5** | True | ✅ 合规 |

对照 `/IslandAuctionKing/Asset/TuPian/TuJian/` 的 12 张 `Codex_*`（`Codex_BackgroundBase`、`Codex_CardFrame`、`Codex_Close`、`Codex_FilterButton`、`Codex_FilterPanel`、`Codex_FooterFrame`、`Codex_GalleryPanel`、`Codex_NameFrame`、`Codex_Reference`、`Codex_ScrollThumb`、`Codex_ScrollTrack`、`Codex_TopBar`）：贴图组与 Mip 本就为 `16 / 13`，本轮统一把 `CompressionQuality` 由 `0 → 5`，现全部合规。

**跨对象回读校验结果**：23 张全部 `(LODGroup, MipGenSettings, CompressionSettings, CompressionQuality, SRGB) = (16, 13, 0, 5, True)`，`ALL_23_COMPLIANT=True`。写入与备份细节见 [IslandAuctionKing UI 贴图批量修正 MCP 回读](../../../IslandAuctionKing/日志证据/2026-08-26_UI贴图批量修正MCP回读.md)。

官方 UI 贴图四项要求见 [绿洲 UI 枚举与结构体速查](绿洲UI枚举与结构体速查.md) 与 [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)。

---

## 三、可执行步骤：复跑基线比对

改动画刷后，用同一段代码重新导出并与本页对照：

```python
import unreal_engine as ue
from unreal_engine.classes import Blueprint

wbp = ue.load_object(Blueprint, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian')

def walk(w, out):
    out.append(w)
    try:
        n = w.GetChildrenCount()
    except Exception:
        return
    for i in range(n):
        walk(w.GetChildAt(i), out)

nodes = []
walk(wbp.WidgetTree.RootWidget, nodes)          # AllWidgets 恒为空，必须递归
imgs = [w for w in nodes if w.get_class().get_name() == 'Image']

for w in imgs:
    b, s = w.Brush, w.Slot
    ld = s.LayoutData
    res = b.ResourceObject.get_name() if b.ResourceObject else 'None'
    ue.log('%s | res=%s | drawas=%s | tiling=%s | tint_rule=%s | margin=(%.2f,%.2f,%.2f,%.2f) | anchors=(%.2f,%.2f)-(%.2f,%.2f) | offsets=(%.0f,%.0f,%.0f,%.0f) | brushimage=%s' % (
        w.get_name(), res, b.DrawAs, b.Tiling, b.TintColor.ColorUseRule,
        b.Margin.Left, b.Margin.Top, b.Margin.Right, b.Margin.Bottom,
        ld.Anchors.Minimum.x, ld.Anchors.Minimum.y, ld.Anchors.Maximum.x, ld.Anchors.Maximum.y,
        ld.Offsets.Left, ld.Offsets.Top, ld.Offsets.Right, ld.Offsets.Bottom,
        w.BrushImage))
```

贴图侧一并核查：

```python
from unreal_engine.classes import Texture2D
for i in range(1, 12):
    t = ue.load_object(Texture2D, '/IslandAuctionKing/Asset/TuPian/ZhuJieMian/ZJM%d' % i)
    ue.log('%s | LODGroup=%s | MipGen=%s | Comp=%s | Quality=%s | SRGB=%s' % (
        t.get_name(), t.LODGroup, t.MipGenSettings, t.CompressionSettings, t.CompressionQuality, t.SRGB))
```

以上两段均为**纯查询**，无需提交 PRV plan。写入画刷/样式的做法见 [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md) 第二章第 5 节。

---

## 四、常见错误

| 现象 | 原因 | 正确做法 |
| --- | --- | --- |
| 看到 `参考图` 的 `Slot.GetSize()` 返回 `(0,0)` 就以为控件坏了 | 该控件锚点为四向拉伸，Offsets 语义变为四边留白，Size 不参与计算 | 判断布局要先看 `LayoutData.Anchors`，Min==Max 才按 `(X,Y,W,H)` 读 Offsets |
| 改了 `Brush.ImageSize` 但显示尺寸没变 | `DrawAs=Image(3)` + Slot 给了显式尺寸时，显示尺寸由 Slot Offsets 决定 | 改显示尺寸走 `Slot.SetSize()`；`ImageSize` 只在 `bAutoSize=True` 或依赖期望尺寸时有意义 |
| 只给某张底图设了 `Margin` 想做九宫格，结果整张被拉伸 | 本 UI 全部 `DrawAs=Image(3)`，官方明确 Image 模式忽略 Margin | `DrawAs` 与 `Margin` 必须同改：底图 `Box(1)` + `Margin`，图标保持 `Image(3)` |
| 换了「上方UI」某一个的贴图，另外两个也变了 | `ZJM1` 被 3 个控件共用，`ZJM3` 被 2 个控件共用 | 需要差异化时先复制出独立贴图资产，再分别指向 |
| 导入的 UI 贴图默认落在 `TEXTUREGROUP_World(0)` 却没人发现 | 编辑器导入不会自动归 UI 组；本目录 11 张里曾有 10 张为 `0`，`ZJM8` 的 MipGen 还是 `0 (FromTextureGroup)`（均已于 2026-08-26 修正） | 导入后**立刻**按官方「UI贴图设置」批量核查并修正（`LODGroup=16`、`MipGenSettings=13`、`CompressionQuality=5`、`CompressionSettings=0`、`SRGB=True`），改前备份、走 MCP plan、改后跨对象回读 |
| 批量改贴图属性只在循环最后调一次 `save_package()` | `save_package()` 是**对象方法**，只落盘它自己所在的 package | 循环内**逐张** `o.save_package()`；改完用磁盘 `mtime`/字节数 + 重新 `load_object` 双重确认 |
| 想用 `widget_inspect` 拿画刷 | 该 API 不返回画刷字段 | 用本页的递归 + `w.Brush.<字段>` 直接读 |

---

## 五、相关页面

- [MCP UI 编辑与高保真还原知识库](MCP-UI编辑与高保真还原知识库.md)
- [绿洲 UI 枚举与结构体速查](绿洲UI枚举与结构体速查.md)
- [UGCAskQ MCP 实测陷阱清单](../工具与流程/UGCAskQ-MCP实测陷阱清单.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [UI 页面切换与 Widget 生命周期](UI页面切换与Widget生命周期.md)
- 来源：[2026-08-26 UI 资产修正与画刷基线导出](../来源记录/2026-08-26_UI资产修正与画刷基线导出.md)

---

## 六、待查证

1. `参考图`（`ZJM2`，`ZOrder=-5`）是否为设计稿垫图、正式交付前是否应隐藏或删除，**未与需求方确认**。
   > **2026-09-14 部分闭环**：需求方已明确该控件即「主界面背景图」的落点，并已将被 [AuctionDressUIService 级联定义](../../../IslandAuctionKing/蓝图与UI/2026-09-14_ZhuJieMian主界面底图导入与设置.md)（`Hub → HubBackground`，`Scope=整页底图`，`Target=参考图`）指向的整屏底图 `ZJMBackground` 写入其 `Brush`。**「是否隐藏或删除」的问题不再成立**；该控件保留为运行期底图。
2. `ZJM8` 修正前的 `MipGenSettings=0 (TMGS_FromTextureGroup)` 与其余 10 张的 `13` 不一致，**成因不明**（可能导入时机或导入方式不同）；已统一改为 `13`，但改前是否已造成实机糊图**未在 PIE 前后对比验证**。
3. `ImageSize=(32,32)` 在 `DrawAs=Image(3)` + Slot 显式尺寸下不参与渲染，这条是按官方字段语义与本 UI 配置推断，**未做 A/B PIE 对比验证**。
4. `CompressionQuality` 已全量改为 `TCQ_Highest(5)`，但官方未说明 `TCQ_Default` 与 `TCQ_Highest` 的**实际画质差异幅度与包体/显存代价**；本轮改动后的画质收益与包体增量**未做 PIE / 打包前后量化对比**。
5. 本页为单次静态快照，未覆盖运行时（Lua 侧 `SetBrushFromTexture` 等）对画刷的动态改写；动态改写路径需另行梳理。

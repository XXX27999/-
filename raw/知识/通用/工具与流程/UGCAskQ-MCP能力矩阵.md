# UGCAskQ MCP 能力矩阵

> 来源：[2026-08-26 UGCAskQ MCP 编辑器修改能力实测](../来源记录/2026-08-26_UGCAskQ_MCP实测记录.md)
> 官方依据：`raw/docs/wiki/绿洲编辑器基础内容/20414_UGCAskQ MCP 使用说明.md`

---

## 一、三个工具的职责

| 工具 | 用途 | 是否需要 plan |
| --- | --- | --- |
| `ue_read` | 只读查询：上下文、API 文档、反射 schema、派生类、枚举、行为树节点 | 不需要 |
| `ue_plan_submit` | 提交 PRV 计划，换取 `plan_id` | —— |
| `ue_py` | 执行 Python（`import unreal_engine as ue`） | 写入必需，纯查询不需要 |

`py:index` 实测为 **68 个分类、819 个方法**。UGCAskQ 扩展分类：`asset_browser`、`bb`、`bp_lua`、`bt`、`ga`、`gamemode_config`、`helpers`、`objed`、`persist_skill`、`project`、`scene`、`widget_edit`。

结构化查询类型（`qt:`）共 10 种：`bp / bt / classmember / context / enum / fusion / hierarchy / objed / skilldoc / struct`。

---

## 二、写能力实测结论

| 能力 | 状态 | 推荐入口 |
| --- | --- | --- |
| 建自定义配置表 | 可用 | `objed_open_editor('DataTable')` → `objed_create_asset('DataTable','自定义表格','空表格',名,子目录)` |
| 表列增删 | 可用 | `struct_add_variable(FUGCStructVariableDescription)` / `struct_remove_variable(VarGuid)` |
| 表行增改删 | 可用 | `data_table_empty_row` + `data_table_add_row` / `data_table_modify_row` / `data_table_remove_row` |
| 新建蓝图 | 可用（约 35s） | `create_blueprint(父类, 项目路径)` + `compile_blueprint` |
| 蓝图变量/组件 | 可用 | `blueprint_add_member_variable` / `add_component_to_blueprint` |
| CDO 默认值 | 可用 | 两段式：探门控 → 全开门 → 全写值 → 保存 → 重载回读 |
| UMG 增删控件 | 可用 | `widget_add` / `widget_remove` / `widget_wrap` |
| UMG 控件换父容器 | 可用 | `widget_move(wbp, 控件名, 新父名)`（2026-09-14 实测：把 6 个品质点从 HBox 平铺到 CanvasPanel） |
| UMG 解包容器 | 仅对「有子控件」的容器 | `widget_unwrap(wbp, 容器名)`；**空容器会报 `RuntimeError: 'X' empty`**，删空容器要用 `widget_remove` |
| UMG 控件属性 | 可用 | `widget_set_property`（Text/ToolTipText/Visibility 实测通过）**value 必须传 `str`** |
| UMG Slot 坐标尺寸 | **可用**（2026-09-14 更正） | 见下方「六、Slot 与 struct 字段写入铁律」。旧记录写的「坐标尺寸走 `Slot.SetPosition/SetSize`」不可用 |
| UI 资产复制 | 可用 | `objed_duplicate_asset`（**不要用 `duplicate_asset`**） |
| 资产重命名/删除 | 可用 | `objed_rename_asset` / `objed_delete_asset` / `delete_asset` |
| 场景 Actor 增改删 | 可用 | `actor_spawn` / `RootComponent.Relative*` / `set_actor_label` / `set_folder_path` / `actor_destroy`（**订正**：`ue.world` 属性不存在，实测 `AttributeError`，详见第九·补节） |
| Volume/Brush | 官方推荐 helper | `ue.helpers.actor_spawn_volume`（`BRUSHBUILDER` 控制台命令在 4.18 不存在） |

---

## 三、PRV 机制的实际行为

- **mutation 判定基于代码文本**：代码里出现 `setattr` / `save_package` / `actor_spawn` 等即判为写入，哪怕作用对象是临时 Python 对象。
- **当前为 observe 等级**：无 plan 执行写入返回 `decision: warn_pass` 加告警，不拦截。不能依赖服务端兜底，规范要求仍须提交 plan。
- **plan_id 可复用**：TTL 默认 900 秒（可设 30–3600），同一 plan_id 跨多次 `ue_py` 复用，返回 `used_count` 递增。实测单个 plan_id 复用 10 次正常。
- **plan 路径校验**：`asset_path` 必须是 `/<ProjectName>/...`，`/Game/` 开头被拒。
- **事务保护**：传 `transaction_name` 时整段代码在事务内，中途异常返回 `Transaction was cancelled due to error. No changes were made.`，实测确认无残留。

---

## 四、性能与超时预算

| 操作 | 实测耗时 |
| --- | --- |
| 纯查询（`list_assets` / `data_table_as_dict` / `widget_inspect`） | 数毫秒 ~ 数百毫秒 |
| `objed_create_asset`（含首次 open_editor） | 约 0.7–1.1 秒 |
| `objed_duplicate_asset` | 约 1.8 秒 |
| `objed_rename_asset` | 约 3.6 秒 |
| `objed_delete_asset`（两个资产） | 约 6.4 秒 |
| `create_blueprint` + 变量 + 组件 + 编译 + 保存 | **约 35 秒** |

官方文档标注：`objed_*` 与资产类 API 批量操作**一次不要超过 3 个**，防止工具调用超时。

---

## 六、Slot 与 struct 字段写入铁律（2026-09-14 实测，重要更正）

**旧结论「UMG Slot 坐标尺寸只能手动拖、MCP 写不了」是错的。** 之前失败的原因是用了
`widget_slot` / `Slot.SetPosition` / `set_property` 回写整条 struct，而不是 API 不支持。

### 唯一可靠的写法：只 set_field，绝不回写整个 struct

```python
# 控件在 CanvasPanel 上时的绝对定位（AnchorData：L/T=位置，R/B=尺寸）
slot = w.Slot                                   # CanvasPanelSlot
ld   = slot.get_property("LayoutData")          # UScriptStruct 'AnchorData'
ofs  = ld.get_field("Offsets")                  # 嵌套 UScriptStruct 'Margin'
ofs.set_field("Left",   1288.0)                 # 就地生效，立即回读得到新值
ofs.set_field("Top",      36.0)
ofs.set_field("Right",   380.0)                 # Anchors 为左上对齐时 R/B 即 Size
ofs.set_field("Bottom",   48.0)
```

同一条铁律适用于所有 UScriptStruct 字段，例如字号：

```python
f = w.get_property("Font")
f.set_field("Size", 42)      # ✅ 就地生效
w.set_property("Font", f)    # ❌ 破坏性：把 Size 写成 0
w.set_property("Font.Size", 42)  # ❌ 'unable to find property Font.Size'
```

### 对照表

| 写法 | 结果 |
| --- | --- |
| `struct.set_field(...)` 单独使用 | ✅ 生效 |
| `struct.set_field(...)` + `w.set_property(整个struct)` | ❌ 值被写成 0（破坏性） |
| `w.set_property("A.B", v)` 点路径 | ❌ `unable to find property` |
| `ue.widget_set_property(wbp, n, "A.B", v)` | ❌ `failed to set`（只支持顶层属性） |
| `ue.widget_slot(wbp, n, "Position"/"Size"/"Offsets"/"LayoutData", v)` | ❌ `failed to set` |
| `ue.widget_slot(wbp, n, "ZOrder"/"bAutoSize", v)` | ✅ 可用 |

### 其他坑

- `ue.widget_set_property(wbp, name, prop, value)` 的 **value 必须是 `str`**，
  传 int 报 `TypeError: argument 4 must be str, not int`。
- `ue.widget_move(wbp, name, new_parent)` 移动后 **Visibility 会被重置为 Collapsed**，
  需要重新 `widget_set_property(..., "Visibility", "3")` 恢复。
- 编辑器重启后 `wbp.WidgetTree.AllWidgets` 可能返回 **长度 0**，但控件其实都在
  （`ue.widget_inspect(wbp, name)` 按名字访问正常）。绕法：从
  `wbp.WidgetTree.RootWidget` 递归建索引——Panel 类取 `w.Slots[i].Content`，
  Border/ScaleBox/SizeBox/Button 取 `w.Content` / `w.Child`。实测 57/57 全部拿到。

---

## 七、批量平铺：把控件全部搬出自动布局容器（2026-09-14 实测）

场景：项目要求「所有控件都能在设计器里手动拖拽」，需要把 VBox / HBox 里的控件
全部搬到 `CanvasPanel` 上绝对定位。

### 实测产能

单次 `ue_py` 调用内完成 **7 次「move + 写 4 个 Offsets 字段」**，全部成功，
无超时（`execution_time_ms` < 5 ms/次）。配合 `widget_remove` 删 3 个空容器，
一次会话共 4 个写脚本即完成整树平铺（52 → 49 控件）。

### 安全判据：不看类型，看 `Visibility` + 画刷

| 状态 | 能否移出 |
| --- | --- |
| `Collapsed` 且无画刷（`get_property("Brush")` 抛错或 `ResourceObject` 为 None） | ✅ 可移，移后保持 `Collapsed`，零视觉风险 |
| `Visible` 且有画刷（面板底图 / 背景） | ❌ 保留，移出会丢背景 |
| 在 Lua `REQUIRED_WIDGET_NAMES` 契约内 | ❌ 保留原名 |
| `WrapBox` 等运行时容器 | ✅ 可移到画布，只改父不改类型，运行时逐格定位仍生效 |

### 删容器必须自底向上

```
MetricsHBox(子已清空) → LeftVBox(子已清空) → RightVBox    ✅
RightVBox → LeftVBox → MetricsHBox                        ❌ 父非空会 SKIP
```

删前逐个校验 `len(w.Slots) == 0`，非空 SKIP 并报告。**误删父容器会连带子树一起消失。**

### 落位坐标的实用求法（无投影工具时）

1. 只读脚本读取画布上**所有控件**的现有绝对坐标（遍历 `ContentCanvas.Slots`，
   逐个取 `LayoutData.Offsets`）。
2. 按命名/层级推断每个装饰卡片的**语义覆盖范围**（如 `FinalPriceCard` 对应
   `LabelFinalPriceImage` + `FinalPriceText`）。
3. 取被覆盖控件的坐标包围盒外扩 8~16 px 作为落位，写入 `Offsets`。

设计态 `GetDesiredSize()` 恒返回 `(0,0)`、拿不到自动布局计算结果，
所以**不能**指望还原"原来被 VBox 算出来的尺寸"；按语义覆盖落位即可。

### 验证：机制层优先

移动前后都是 `Collapsed` → 渲染输出不可能变化，这是**确定性证明**，优先于像素比对。
若要做像素比对，**必须先标定画布框**，否则会把编辑器缩放/平移造成的取景差异
误判为 UI 改动（详见 [绿洲通用 UI 编辑规范与排错](../UI与交互/绿洲通用UI编辑规范与排错.md) 2.8）。

---

## 八、设计态数据复原（文本 / 可见性 / 网格）

用于「编辑器预览变空」「预览文本没加回」这类报障。**先分清是运行时问题还是设计态问题**：
设计器只画设计态 `Text`，运行时 `SetText` 的值在设计器里看不到。

### 8.1 金标准来源

`D:\知识库\和平精英绿洲起源\raw\<项目名>\_JsonOutput\Asset\<folder>\<资产>.json`（UAssetAPI 导出）内含每个控件的
设计态 `Text` / `Font.Size` / `Visibility` / 槽位 `LayoutData`，
以及 **Slot 导出的 `Parent` / `Content`**（ObjectIndex → Export 序号），
可据此**重建出完整控件树**：

> 2026-09-16 订正：该目录原位于 `<项目>/_JsonOutput`，已随工具一并迁出 UGC 工程，改由
> [UAsset 转 JSON 工具](./UAsset转JSON工具.md) 默认写入知识库路径；工程内不再生成 `_JsonOutput`。

```python
# 用 Slot 的 Parent/Content 引用还原父子关系
for i, e in enumerate(exp):
    if cls_of(e).endswith("Slot"):
        p = props(e)
        par, con = p["Parent"]["Value"], p["Content"]["Value"]
        child2[exp[con-1]["ObjectName"]] = (exp[par-1]["ObjectName"], cls_of(e))
```

### 8.2 契约控件缺失会整屏静默失效

Lua `ValidateWidgetContract` 遍历 `REQUIRED_WIDGET_NAMES`，**缺失即 `return false` 并中止
`Initialize`** → 数据绑定全部不执行，表现为「设计器只剩占位文本 / 运行时全空」。
排障第一步就是全量核对契约名单，而不是逐段读 Lua。

### 8.3 可见性：Lua 不接管就必须设计态可见

`ue.widget_set_property(wbp, 名称, "Visibility", 码)` 的码是 **ESlateVisibility 0 基原值**：

| 码 | 值 |
| --- | --- |
| `0` | Visible |
| `1` | Collapsed |
| `2` | Hidden |
| `3` | HitTestInvisible |
| `4` | SelfHitTestInvisible |
| `5` | ESlateVisibility_MAX（无效） |

Lua 侧**只 `SetText`、不调 `SetVisibility`** 的控件，若设计态是 `Collapsed`，
运行时也永远不显示。改动前先 `grep 控件名` 确认 Lua 是否接管。

### 8.4 网格重建：WrapBox + SizeBox + Border

- **`Border` 只设 `BrushColor` 即可渲染实色块**（前提 `Background.DrawAs=3`，新控件默认即 3，
  `ResourceObject` 可为 `None`）。**挂真实贴图反而出错**——挂 `SettlementGrid` 会被染成纯黑块。
- `FLinearColor` 在 `ue_py` 中是 **python 值类型，没有 `set_field`**：
  构造 `type(已有FLinearColor对象)(r,g,b,a)`，写入 `w.set_property("BrushColor", obj)`。
- WrapBox 内每格需两层：`SizeBox`(`WidthOverride`/`HeightOverride`=82, `bOverride_*`=True) → `Border`；
  WrapBox 本体需 `WrapWidth`（6 列 × 82 + 5 × 3 = 507 → 取 510）+ `bExplicitWrapWidth=True`
  + `InnerSlotPadding=(3,3)`。
- **子控件被面板底图盖住**是「建好了却看不见」的高频原因：抬高父容器 `ZOrder`（≥7~8）即显形。
- 运行时无副作用：Lua `InitializeWarehouseGrid` 首行 `grid:ClearChildren()`，
  设计态格子会被清掉再挂真实格子。

### 8.5 `widget_add` 后重建索引的铁律

沿用旧索引并对已见名字 `continue`，会**连子节点一起跳过** → 新控件永远索引不到，
症状是 `widget_add` 无报错但紧接着 `KeyError('<新控件名>')`，且控件计数不增（其实已创建）。
正确写法：**始终下探 children，只在写入索引时判重**。

### 8.6 截图验收的绕法

FlaUI `--list` 在本机**会漏掉编辑器窗口**（与 High IL 下 `SetForegroundWindow` 无效同源）。
可靠绕法：`EnumWindows` 按 PID 取 HWND（`UI编辑器` 与
`ShadowTrackerExtra (64 位，PCD3D_SM5) ...` 两个 `UnrealWindow`），
再 `ShowWindow(SW_RESTORE)` + `SetForegroundWindow` + `CopyFromScreen` 落 PNG。
本机 PowerShell 工具**不回传 stdout**，结果一律落盘后 Read。

---

## 九、资产定位 API（2026-09-15 实测）

**不要按目录约定拼路径。** 拼错时编辑器会给出带修复建议的报错：

```
unable to load object '/IslandAuctionKing/Asset/Data/UIConfigTable' (class=DataTable).
  [DIAGNOSIS] Package ... does NOT exist on disk. The path is wrong.
  [CAUSE]     UGC editor uses AssetPathRemapping; on-disk path != display path.
  [FIX]       ue.resolve_asset('<名称>') / ue.list_assets('<已知目录>') / ue.search_game_assets('<关键字>')
              Then use the returned 'load_path' field verbatim.
```

| API | 返回 | 说明 |
| --- | --- | --- |
| `ue.resolve_asset(<名称>)` | `list[dict]` | 权威定位；同目录的 `UserDefinedStruct` 会一并返回，需按 `asset_class` 过滤 |
| `ue.list_assets(<目录>)` | `list[dict]` | 列举目录下资产，结构同上 |
| `ue.search_game_assets(<关键字>)` | `list` | UGC 项目实测返回**空数组**（`/Game` 搜索不适用） |

`list[dict]` 单条字段：`name`、`asset_class`、`load_path`、`object_path`、`package_name`、
`package_path`（或 `category_path`）、`disk_size`。

- **DataTable 的 `asset_class` 是 `UAEDataTable`**，不是 `DataTable`；筛表用 `"DataTable" in asset_class`。
- `load_object(DataTable, path)` 既接受 `.../UIConfigTable`，也接受 `.../UIConfigTable.UIConfigTable`。
- 大表（`data_table_as_dict` 数百行）全量回传有截断风险，导出应让 `ue_py` 写文件到备份目录。
- Windows 侧工具直连 MCP 的端口发现与 SSE 握手细节见
  [FolderTreeTranslator 表格蓝图 MCP 读写](FolderTreeTranslator表格蓝图MCP读写.md)。

---

## 九·补、场景取证与纯查询回传通道（2026-09-17 实测，重要更正）

本轮为定位「iOS 洗澡池马赛克」而系统探测了沙箱在**场景/Actor 只读**与**回传通道**上的能力，
其中第一条与第三节第 39 行的既有表述冲突，以下为准。

### 9·补.1 纯查询回传通道：必须 `print`，`output=` 不回传

`ue_py` 在**纯查询模式**（`prv.decision=pass` / `plan_valid=false`）下：

| 写法 | 回包表现 |
| --- | --- |
| `output = {"a": 1}` | ❌ `"result": null`、`"output": ""`（完全不回传） |
| `print(json.dumps(...))` | ✅ 文本落在回包 **`output`** 字段，行首带 `[Log] ` 前缀 |

对照：带 `plan_id` 的执行型调用（如 DataTable 写入）才会把 `output` 变量映射到 `result`。
排查时用 `print()` 打点，不要依赖返回值。

### 9·补.2 `ue.world` 不存在

实测 `import unreal_engine as ue; ue.world` 直接抛
`AttributeError: module 'unreal_engine' has no attribute 'world'`。
正确的只读入口（`dir(ue)` 实测存在）：

| 目的 | API |
| --- | --- |
| 取大纲视图当前选中 Actor | `ue.editor_get_selected_actors()` → `list[UObject]` |
| 取编辑器世界 | `ue.get_editor_world()`；另有 `ue.all_worlds()` |
| 读对象属性 | `obj.as_dict()`（Actor 实测 151 键、`BrushComponent` 244 键）；另有 `get_property` / `set_property` / `get_field` |
| 资产定位 | `ue.list_assets` / `ue.list_asset_dirs` / `ue.find_assets_by_class` / `ue.resolve_asset`（见第九节） |

### 9·补.3 场景截图通道（比 FlaUI 轻量）

```python
ue.editor_set_view_location(FVector(x, y, z))            # 必须传 FVector，不能传 3 个 float
ue.editor_set_view_rotation(FRotator(roll, pitch, yaw))  # 参数顺序是 (roll, pitch, yaw)
ue.redraw_all_viewports()                                # 可选
path = ue.scene_capture("文件名")                         # 返回 PNG 绝对路径
```

- 落盘位置：`<ShadowTrackerExtra>\Saved\UGCAskqTemp\<文件名>.png`——**在 UGC 工程目录之外**，不污染工程。
- 返回的 PNG 可直接用 Read 多模态读取，用于核对场景外观；8.6 节的 FlaUI 方案退为备选。
- 副作用：会移动**用户当前视口的相机**（非资产改动，PRV 不判为 mutation），执行前应知会用户。

### 9·补.4 资产枚举的两个边界

- `list_assets('/Game/...')` 返回 **`[]`**（官方内容不属 UGC 工程资产域）；但
  `find_assets_by_class('MaterialInstanceConstant', '/Game/Arts_Scenes/Materials/Water')`
  **可以枚举官方材质**（实测列出 `M_Ocean_Inst`、`M_Ocean_DepthOpacity_Inst`、
  `M_swamp_DepthOpacity_SuperHigh_Inst` 等）。
- `ue.list_assets()` **不接受关键字参数**（报 `list_assets() takes no keyword arguments`），
  `recursive` 只能按位置传。

### 9·补.5 BSP 画刷不可读不可写（材质挂载的硬边界）

对 `UClass = Brush` 的 Actor（BSP 画刷）：

| 观察点 | 实测 |
| --- | --- |
| `actor.as_dict()` | 有 `Brush`(UModel) / `BrushComponent` / `BrushType` / `BrushColor` / `PolyFlags` / `BrushBuilder` |
| `Brush`（UModel）`as_dict()` | **键数 = 0**（UModel 属性未暴露） |
| `BrushComponent.as_dict()` | 244 键，材质相关只有 `bReturnMaterialOnMove`（**无 `OverrideMaterials`**） |
| 材质读写 API | `dir(ue)` 中仅 `create_material_instance`，无挂载/读取材质的方法 |

⇒ BSP 画刷的**表面材质只能靠编辑器 UI（表面属性 / 地表材质实例）改**，MCP 读不到也写不了；
这也是官方 FAQ「画刷地表贴图真机被还原成默认材质」类问题无法由 MCP 自动闭环的原因。

### 九·补.6 UMG(UIBP) JSON 的 WidgetTree 静态解析——不打开编辑器即可判定控件尺寸/可见性

MCP 的 `ue_read` 只能读 Actor/资产的属性字典，**读不到控件在 Canvas 上的槽位布局**；
但 `_JsonOutput` 里的 UIBP `.json` 完整保留了 WidgetTree，可直接静态解析，用于回答
「这个按钮是不是铺满全屏」「某控件默认是否 Collapsed」这类只能靠截图猜的问题。

**结构要点**（以 `Asset\UI\AreaPetChoice.json` 实测，541 Exports / 54 Imports）：

| 关系 | 载体 | 说明 |
| --- | --- | --- |
| 控件本体 | 导出项，`ObjectName` = 控件名（如 `Button_836`） | 自身只有 `Slot` 引用 + `bExpandedInDesigner` |
| 槽位 | `CanvasPanelSlot_47` 等导出项 | 布局（`LayoutData` → offsets）+ `Content` 指回控件（**1 基索引**） |
| 反向定位 | 遍历所有导出找 `Content` == 控件 1 基索引 | 即得到该控件的槽位 |

**实测结论示例**：`Button_836` = Export[30]，槽位 `CanvasPanelSlot_47`[128]，
offsets `(Left=1236, Top=760, Right=619.17, Bottom=187.25)` → 右下角 619×187 按钮，
**不是全屏按钮**；全表无 `Anchors=(0,0)-(1,1)` 的槽位 ⇒ 可据此排除「大按钮误触」假设。

**配套判据（同批实测）**：
- **UMG 图内是否有逻辑**：看导出里的 `UGCK2Node_Event_*`，若 `PreConstruct`/`Construct`/`Tick`
  三个节点的 `EnabledState=ENodeEnabledState::Disabled`，则该 UIBP 图内零逻辑，全部行为在 Lua 侧。
- 因此「UMG 没绑事件 + Lua 只有显式点击」= 可静态断言不存在自动触发路径，无需 PIE。

**可复用脚本**：`D:\知识库\和平精英绿洲起源\备份\pet_paradise\20260917_已知缺陷第二批整改\probe_umg_slot.py`
（只读；用法 `python probe_umg_slot.py <json> <out.txt> <控件名>`，输出目标控件全部标量属性、
引用它的槽位、以及全表疑似大尺寸槽位）。**注意**：只读解析，不得据 JSON 反推改写资产。

### 九·补.7 UIBP JSON 控件树解析的准确 schema（2026-09-17 订正）<证据状态：项目实测>

补.6 的方向描述需要订正，且缺少「类名怎么取」「根控件怎么定」两个必用环节；按补.6 直接写解析脚本会取不到结果。

| 环节 | 正确做法 |
| --- | --- |
| 父子方向 | **控件 → 槽位 → 子控件**：控件的 `Slots` 是**数组**属性（不是单引用 `Slot`），每项解析成槽位导出，槽位的 `Content` 才指向子控件 |
| 取类名 | 导出项**没有**直接的类名字符串：`ClassIndex` 是整数，**正数 N → `Exports[N-1]`**，**负数 -N → `Imports[N-1]`**，取目标项的 `ObjectName` |
| 取属性 | 属性在 `Exports[i].Data[]`，每项形如 `{ Name, Value }`；数组属性（`Slots`）的 `Value` 是**属性项列表**，每项再取一次 `Value` 才得到整数引用 |
| 定真树根 | 先找 `class == UGCWidgetBlueprint` 的导出 → 其 `WidgetTree` → `RootWidget`。**不要按名字取 `WidgetTree`**：资产里通常有**两份** WidgetTree 与两套同名控件（蓝图模板 + 生成类），按名字取会拿到错的那份 |
| 判读贴图 | `Image` 的 `Brush`（StructPropertyData）里 `ResourceObject` 同样按整数引用解析，可拿到贴图名（实测 `TouMingDi` = 透明点击区、`TiShi` = 可见气泡），据此区分「透明遮罩」与「可见面板」 |

**Vector2D 有两种序列化形态，解析必须都覆盖**（否则会误判成「数据缺失」）：

- 形态 A：`StructPropertyData` 下挂 `X` / `Y` 子字段（Margin、部分结构）。
- 形态 B：`FAnchors.Minimum/Maximum` 是 `StructPropertyData(StructType=Vector2D, Name=Minimum)`，
  其 `Value` 是**单元素列表**，元素是 `Vector2DPropertyData`，值直接挂在它的 `Value`（dict）或 `X`/`Y` 上，
  **没有 X/Y 子字段**。只按形态 A 写解析会得到 None，易误判为「JSON 里没有 Anchors」。

**默认值省略（重要）**：UAssetAPI 不序列化等于默认值的字段。
`FAnchors` 只出现 `Maximum` 而 `Minimum` 缺省时，`Minimum` 就是 `(0,0)`；
`Margin` 只出现 `Right/Bottom` 时，`Left/Top` 就是 `0`。
⇒ 判「是否全屏拉伸」要看 `Minimum=(0,0) 且 Maximum=(1,1)`，不能因为 `Minimum` 缺失就判为读不到。

**点锚 vs 拉伸锚的 Offsets 语义不同**（据此可反算位置）：

| 锚点 | Offsets 语义 | 计算 |
| --- | --- | --- |
| 点锚（`Minimum == Maximum`） | `L/T` = 相对锚点偏移，`R/B` = **宽/高** | 位置 = 锚点×画布尺寸 + (L, T)；尺寸 = (R, B) |
| 拉伸锚（`Minimum != Maximum`） | `L/T/R/B` = 四边**内缩量** | 全屏判据 `Min=(0,0) Max=(1,1)` 且四边为 0 |

实测（`TiShi`，按 1920×1080 设计画布）：`Image_51` 锚 `(0,0)..(1,1)` 且 Offsets 全 0 ⇒ **全屏**；
`Image_230` 锚 `(0.5,0.5)..(0.5,0.5)` ⇒ 宽高 `1063×71`、位置约 `(432,147)`；
`TextBlock_62` 默认 `(0,0)` 锚 ⇒ 位置 `(436,153)`、尺寸 `1058×55`，正好落在 `Image_230` 内 ⇒ 印证 `Image_230` 是气泡本体。
（画布尺寸未知时只能确定相对关系，绝对坐标需按工程实际设计分辨率换算。）

**单文件转换回退路径（避免全工程重转）**：只为看 1~2 个界面时，不必跑全工程转换，可直连底层工具：

```powershell
$gui = "C:\Program Files (x86)\UAssetGUI.exe"
Start-Process -FilePath $gui -ArgumentList @("tojson", "<src.uasset>", "<dst.json>", "VER_UE4_24") -Wait -PassThru
```

参数与知识库转换工具 `UAssetToJsonConverter` 内部调用完全一致（见 `UAsset转JSON工具.md`）。
输出必须落在知识库备份目录，**不得**产出到 UGC 工程。

**前置校验**：工程内既有 `_JsonOutput` 常常过期（本项目实测 JSON mtime 2026-07-29 vs `.uasset` 2026-09-16），
按「读前必须同步」的约定不能直接采信旧 JSON；单文件**新转换**即是满足该约定的最省时回退。

**可复用脚本**：`D:\知识库\和平精英绿洲起源\备份\pet_paradise\20260917_UI动效接入批次\probe_umg_tree_v2.py`
（只读；用法 `python probe_umg_tree_v2.py <json> [<json>...]`，结果与脚本同目录 `_umg_tree_v2_result.txt`，
输出「控件树 + 每级 Slot 几何 + 每个控件的 Visibility/Text/Brush」）。

### 九·补.8 `ue_py` 写场景的两个必坑参数形式（2026-09-17 实测）<证据状态：项目实测>

执行型 `ue_py`（带 `plan_id`，允许 mutation）里 Actor/资产操作的写法与直觉不同，踩错会报看似无关的错：

| 目的 | ❌ 写法与报错 | ✅ 正确写法 |
| --- | --- | --- |
| 加载资产 | `ue.load_object(None, path)` → `argument is not a UObject` | `from unreal_engine.classes import DataTable` 后 `ue.load_object(DataTable, path)`；**第一个参数必须是类**，不接受 `None` |
| 生成 Actor | `world.actor_spawn(StaticMeshActor, location=CENTER)` → `unable to set property` | **位置参数**：`world.actor_spawn(StaticMeshActor, CENTER)`；该 API 不接受 `location=` 关键字 |
| 遍历场景 Actor | `world.get_all_actors()` → `AttributeError` | `world.all_actors()` |
| 场景截图 | `scene_capture(loc, target, path)` → `takes at most 1 argument` | `scene_capture("文件名")`（与 9·补.3 一致，只接受 1 个参数） |
| 设视角后截图 | 同一次调用里 `set_view_location` → `redraw` → `scene_capture`，拍到的是**上一帧视角**（帧延迟，2026-09-17 实测：设为俯视却拍到旧侧景） | **两步法**：第一次调用只 `set_view_location/set_view_rotation + redraw`，第二次调用单独 `scene_capture`；且编辑器重启后视口通道仍可能不稳定（活动视口被 UI/焦点影响），关键对位以 `get_actor_bounds` 包围盒回读闭环，截图只作参考 |
| 改 StaticMeshActor 缩放 | `K2_GetRootComponent()` 对部分 spawn 出来的 StaticMeshActor 返回 **None**（组件级写法全废）；PascalCase `SetActorScale3D` **静默 no-op**（不报错、值不变） | 用 snake_case `actor.set_actor_scale(FVector)`（同族 `get_actor_scale/set_relative_scale/set_world_scale`）；旋转用 `set_actor_rotation(FRotator(roll,pitch,yaw), sweep)` 实测可用；保存关卡后 **save API 返回值恒为 None，用 `.umap` 文件 mtime 判定是否真落盘**（2026-09-17 实测） |

**场景/资产写入后的标准收尾**：`set_property` 改完 → 逐个 `as_dict()`/`get_property` **回读核验** → 再 `save_package` 关卡或资产 → PRV 才算闭环；
不要跳回读直接判定成功。

**完整样例（关卡改造：新增静态水面 Actor 并隐藏 BSP 画刷）**：见
[2026-09-17 已知缺陷第三轮整改](../../../pet_paradise/开发记录/2026-09-17_已知缺陷第三轮整改.md) 第四节，
含写入值与回读核验项。只读排查优先用 9·补.2 的 `ue.get_editor_world()` + `all_actors()`。

---

### 九·补.9 PIE 运行时日志落点与 `ue_pie` 判据（2026-09-17 实测）<证据状态：项目实测>

**（1）PIE 的 `ugcprint` 不落在 `ShadowTrackerExtra.log`。**
该文件是**编辑器主进程**日志，只记录 `LogPakFile` 文件加载与 `LogNula: DebugLog: UELuaLoader`，
**不含** ugcprint 内容。据此得出「日志里没有 = 代码没跑」是**错误结论**（本轮已撤回一次误判）。

PIE 运行时 Lua 日志真实落点（per-project，按 debug_id 分文件）：

```
ShadowTrackerExtra\Saved\Logs\<项目名>\
    Clientlog\LuaLog\<ts>_client_<debug_id>_1.log     ← ugcprint / LuaLog 落这里
    Clientlog\FullLog\<ts>_client_<debug_id>_1.log
    Clientlog\TagLog\<ts>_client_<debug_id>_1_TagLog.log
    DSlog\LuaLog\<ts>_ds_<debug_id>_lualog.log
    DSlog\FullLog\<ts>_ds_<debug_id>_realtime.log
```

当前会话的确切路径可直接从 MCP 资源 `ugc://pie/session/current` 的
`clients[].log_path` / `dedicated_servers[].log_path` 取到，不必拼路径。

**（2）`doluastring` 成功返回空 JSON 对象 —— 按 `success:true` 判就绪会永远判不出来。**

| 情形 | `tools/call` 返回 |
| --- | --- |
| 派发成功 | `{"affected_count":0,"error":"","outcome":"","success":false}` 之外的**空对象 `{}`** |
| client 未注册 | `{"affected_count":0,"error":"No PIE client window is registered with the Lua console; start PIE first","success":false}` |

正确判据：**响应非空 且 不含 `"success":false`**。
`doluastring` 是**单向派发**，不回传 Lua 输出，结果必须回读上面那批日志（建议代码里打带标记的前缀，如 `ugcprint("[DIAG] ...")`）。

**（3）`reloadlua` 秒级热更，验证是否生效的办法**：在 doluastring 里读一个**本次新增的字段**，
读到新值即证明新代码已进 PIE（比看日志时间戳可靠）。

**（4）PIE client Lua 环境可用的全局（实测）**

| 可用 | 不可用 / 注意 |
| --- | --- |
| `UGCGameSystem.GetLocalPlayerController()` → 返回 `UGCPlayerController_C` 实例 | `UE.UObject` **不存在**（`attempt to index a nil value (field 'UObject')`） |
| `UGCTweenSystem`、`UGCMathUtility`、`EEasingType`（`EEasingType.QuadOut == 2`） | `UGCPlayerControllerSystem.GetLocalPlayerController` 不存在 |
| `require("Script.Common.UI.UIUtils")`（**不是** `Script.Common.Utils.UIUtils`） | `UIUtils` 不是全局变量，必须 require |

---

### 九·补.10 PIE 注入时机与「零副作用运行态验证」（2026-09-17 实测）<证据状态：项目实测>

**（1）`ue_pie start` 返回 ≠ 可以注入 Lua。存在 1～3 分钟的不可注入窗口。**

实测时间线（同一会话）：

| 时刻 | 事件 | `doluastring` / `reloadlua` 结果 |
| --- | --- | --- |
| 17:53:23 | PIE 客户端启动 | — |
| 17:55:52 | DS 启动 | — |
| 17:55:43 | 客户端仍在写初始化日志 | `reloadlua` → `Lua reload was not handled; the PIE client connection may not be ready` |
| 17:56:24 | 客户端已在游戏内（`NetworkEstablished`/`fighting`） | `doluastring` → `No PIE client window is registered with the Lua console; start PIE first` |
| 17:56:45 | 客户端持续写初始化日志 | — |
| **17:56:51** | — | **`doluastring` 成功（返回空对象 `{}`）** |

⇒ 这两条报错都是**时机**问题，不是 MCP 故障。间隔 30～60 s 重试即可，**不要据此判定工具不可用或去"修 MCP"**。
就绪的可靠判据：重试 `doluastring` 打一个带标记前缀的探针，再回读 `Clientlog\LuaLog` 是否出现该前缀。

**（2）`reloadlua` 成功返回也不代表模块真的换了。**
验证方式见 9·补.9(3)：在 doluastring 里读**本次新增的方法/字段**。例：
`PetModule=true | hasRPC_SetSeasonCardFeetOffset=true` 才能证明热更进去了。
本机 Git Bash 无 `sleep`/coreutils，等待不要在 shell 里 sleep，用 Python `time.sleep` 或让两次工具调用自然间隔。

**（3）零副作用运行态验证：用「假对象 + 元表」直接验 RPC/函数契约。**

需要验证某个 RPC 的入参兼容与边界，但**不想触碰真实游戏对象**（用户正在同一 PIE 里游玩，注入宠物/特效会污染其会话）时，
可在 doluastring 里构造假实例调用方法本体：

```lua
local Pet = require("Script.Blueprint.Prefabs.Monsters.Pet")
local fake = setmetatable({}, { __index = Pet })
fake.HasAuthority = function() return false end          -- 覆写端侧判定，走客户端分支
Pet.RPC_SetSeasonCardFeetOffset(fake, "-120.5")          -- 传字符串，验跨端传参兼容
-- 读 fake._SeasonCardFeetOffsetZ 即可看出实际存值与钳制行为
```

实测输出（客户端 LuaLog）：`after_str_neg120_5=-120.5 | after_9000_should_keep=-120.5 | after_abc_should_keep=-120.5`，
一次调用即验证了「字符串→数值」「超限拒绝」「非法值拒绝」三条契约。**纯读、不产生任何组件、不改游戏状态。**

**（4）读者注意**：运行时能验证的只是「代码进去且行为正确」；
凡依赖游戏内状态的路径（要玩家拥有某物、要子关卡已加载、要消耗次数/资源）**不要擅自注入**，
这类验证应留给真实操作触发的那一次。

---

## 十、相关页面

- [UGCAskQ MCP 实测陷阱清单](UGCAskQ-MCP实测陷阱清单.md)
- [MCP UI 编辑与高保真还原知识库](../UI与交互/MCP-UI编辑与高保真还原知识库.md)
- [配置表与结构体的 MCP 编辑](配置表与结构体的MCP编辑.md)
- [蓝图与 MCP 写入流程](蓝图与MCP写入流程.md)
- [PIE 调试与热更新边界](PIE调试与热更新边界.md)

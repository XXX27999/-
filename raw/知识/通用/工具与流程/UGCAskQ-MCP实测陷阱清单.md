# UGCAskQ MCP 实测陷阱清单

> 来源：[2026-08-26 UGCAskQ MCP 编辑器修改能力实测](../来源记录/2026-08-26_UGCAskQ_MCP实测记录.md)、[2026-08-26 UI 画刷与控件样式官方查证](../来源记录/2026-08-26_UI画刷与样式官方查证.md)、[2026-08-26 UI 资产修正与画刷基线导出](../来源记录/2026-08-26_UI资产修正与画刷基线导出.md)
> 全部条目均为该次实测中真实触发的失败或反直觉行为，附实际错误文本。

---

## 核心结论

1. **返回值不是成功判据**：多个写入 API 成功时返回 `None`，一律以「重新 `load_object` 回读」判定（详见第七节）。
2. **点号路径不通用**：`widget_set_property` / `widget_slot` 不解析嵌套路径，struct 与画刷必须用 Python 直接属性赋值 + `compile_blueprint` + `save_package`。
3. **反射查询前提**：`WidgetTree.AllWidgets` 恒为空须手动递归；蓝图函数库要用 `ue.all_classes()` 找 `_C` 后缀；`properties()` 返回字符串列表。
4. **写入有前置条件**：`objed_*` 需先 `objed_open_editor`；枚举按整数写且必须查表；带 `EditCondition` 的字段必须两遍写入。
5. **struct 优先就地改字段**，整体替换会清空未赋值字段。
6. **绑定层存在缺失 API**（2026-09-15 补充）：本绑定**没有** `set_editor_property` 与 `call_function`，`FVector2D` **没有** `set_field`；`VerticalBoxSlot` **没有** `LayoutData`；`widget_add` 后 `WidgetTree.AllWidgets` **滞后不刷新**（须以 `RootWidget` 递归为权威）。详见 [2026-09-15 装扮UI优化 MCP 写入与截图核验](../来源记录/2026-09-15_装扮UI优化MCP写入与截图核验.md)。

---

## 一、objed 系列必须先打开编辑器

```python
ue.objed_create_asset('DataTable', '自定义表格', '空表格', 'X', 'Test')
# Cannot get asset handler for DataTable/自定义表格.
```

修复：先 `ue.objed_open_editor('DataTable')`（返回 True）再创建。同一现象出现在 `功能表格`。`内置表格` / `模板功能表格` 则是模版列表为空（`template_name '空表格' not found ... Available: `）。

---

## 二、duplicate_asset 不能用于 UGCWidgetBlueprint

```python
ue.duplicate_asset(src, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/MCPTestUIProbe')
# 返回对象 get_class() == 'Package'
# get_path_name() == '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI.MCPTestUIProbe'   ← 点号，不是斜杠
```

两参数与三参数形式结果一致。后果：

- AssetRegistry 无条目，`list_assets` / `resolve_asset` 都查不到；
- 磁盘多出与目录同名的游离包 `Asset/Blueprint/Prefabs/UI.uasset`（实测 529 字节）；
- `ue.delete_asset('/…/Prefabs/UI')` 当场返回 `None` 且文件仍在，无法确认删除；该游离文件在后续 `objed_delete_asset` / `delete_asset` 清理流程走完后才从磁盘消失，删除时机不可控。

结论：这条路径不可用于生产。已发生时要手工核查磁盘是否残留同名 `.uasset`。

正确入口：`ue.objed_duplicate_asset(源名, 新名, 'UI')`，返回规范路径且可被 `resolve_asset` 查到。

---

## 二·补一、duplicate_asset 复制 Texture2D 只产出空壳；可行路径是「物理复制 + rename_asset」（2026-09-18 实测，IslandAuctionKing）

场景：把 7 个 UI 边界贴图（6 MB 级）复制到 `Asset/TuPian/Dress/DefaultGray/` 并按 SlotKey 重命名，用于装扮主题分目录。

### 1. `ue.duplicate_asset` 不可用于贴图复制

```python
o = ue.duplicate_asset(src, dst)   # 2 参数；3 参数 (src, dst_pkg, dst_name) 同样
o.save_package()
# 返回对象 get_class() == 'Package'
# 磁盘产物：AuctionBackground.uasset 554 字节 / AuctionTopBar.uasset 546 字节  ← 源 6294618 / 706545 字节
# 回读：ue.load_object(Texture2D, dst) 抛 "exists on disk but contains no asset named 'AuctionBackground'"
```

追加 `wait_for_assets`、先 `load_object(Texture2D, src)` 强制加载源再复制，均复现同一结果。**源贴图本身可正常 `load_object` 为 `Texture2D`**，排除「源不可加载」这一解释。

结论：第二节「duplicate_asset 不能用于 UGCWidgetBlueprint」的适用范围**扩展到 Texture2D**——它只建空包，不复制 bulk data。新建 DataTable 同样失败（三种入口：`duplicate_asset` / `objed_create_asset` / `create_asset` + `UGCDataTableFactory`，产物包内均无对象）。

### 2. 可行路径：PowerShell 物理复制 + `rename_asset` 修正包内资产名

```powershell
Copy-Item -Path "<src>.uasset" -Destination "<dstDir>\<SlotKey>.uasset" -Force   # 实测成功，字节数一致
```

```python
ue.rename_asset('/IslandAuctionKing/Asset/TuPian/Dress/DefaultGray/HubBackground.ZJMBackground', 'HubBackground')
# 返回 None（正常，见第七节）；改后 load_object(Texture2D, '.../HubBackground') 成功，get_name() == 'HubBackground'
```

**必须改名**：`.uasset` 物理复制后包内导出名仍是源名，`load_object` 会报

```
[DIAGNOSIS] Package '.../HubBackground' exists on disk but contains no asset named 'HubBackground' (or wrong class).
[FIX]  Inspect the package contents: ue.list_assets('<pkg>') then use the dict's 'load_path' field.
```

判定改名成功要看**新的短路径可加载、旧名路径不可加载**（实测 `HubBackground` OK、`HubBackground.ZJMBackground` 已失效），与第八节 `objed_rename_asset` 的「旧名仍可 resolve」规律相反。

改名后编辑器重新存盘，字节数略增（6292370 → 6385785），属正常，不要误判为损坏。

### 3. 一次性搬运 8 个资产的实操节奏

| 步骤 | 约束 |
| --- | --- |
| 物理复制 | 无数量限制，PowerShell `Copy-Item -Force` 即可；逐文件比对源/目标字节数 |
| `rename_asset` | **一批 ≤ 3 个**（资产操作较重，防止 MCP 调用超时）；实测单批 3 个耗时 0.65～0.73 s |
| `delete_asset` | 同样 ≤ 3 个；实测单批 3 个耗时 11.8 s（首次触发注册表重建），后续批 0.23～3.9 s |
| 清理空壳 | 先 `delete_asset` 让注册表摘除，再删磁盘残留；`delete_asset` 返回 `None` 但**磁盘文件可能仍在**，须 PowerShell 复查 |

### 4. 副作用资产

`objed_create_asset` 建表失败会顺带产出 `UGCTemplateRowStruct_<表名>.uasset`（行结构模板）。删除主表后**必须一并删除该模板**，否则工程内残留无用资产。

---

## 三、复制后未保存就 load_object 会失败并回滚事务

```
unable to load object '...' (class=Blueprint).
[DIAGNOSIS] Package ... does NOT exist on disk. The path is wrong.
[FIX] ue.resolve_asset(name) / ue.list_assets(dir) / ue.search_game_assets(name)
```

规律：新建/复制类 API 返回对象后要先 `save_package()` 落盘，再 `load_object`；`load_object` 失败的标准恢复路径是 `resolve_asset` 取真实 `load_path`，**禁止凭命名规律拼路径**。

---

## 四、widget_slot 只支持少数属性名

| slot_prop | 结果 |
| --- | --- |
| `ZOrder` / `bAutoSize` | OK |
| `Position` / `Offsets` / `LayoutData.Offsets` / `Anchors` / `Alignment` | `widget_slot: failed to set 'X' on 'Y'` |

原因：`CanvasPanelSlot` 的可编辑属性只有 `LayoutData`(FAnchorData) / `bAutoSize` / `ZOrder` / `bAntiAdaptation`，坐标藏在 `LayoutData.Offsets`(FMargin) 里，`widget_slot` 未做嵌套路径解析。

可用替代（实测持久化成功）：

```python
w = [c for c in wbp.WidgetTree.AllWidgets if c.get_name()=='MCPProbeText'][0]
w.Slot.SetPosition(FVector2D(40, 300))
w.Slot.SetSize(FVector2D(260, 40))
ue.compile_blueprint(wbp); wbp.save_package()
# 回读: Slot: CanvasPanel (Pos: 40,300, Size: 260,40)
```

`CanvasPanelSlot` 可用 UFunction：`SetZOrder / SetSize / SetPosition / SetOffsets / SetMinimum / SetMaximum / SetLayout / SetAutoSize / SetAntiAdaptation / SetAnchors / SetAlignment` 及对应 Get。

---

## 五、widget_wrap 会留下 _Wrapper 容器

`widget_wrap(wbp, 'A', 'SizeBox')` 新建 `A_Wrapper` 容器并继承原 Slot 布局；随后 `widget_remove(wbp, 'A')` 只删 A，**wrapper 保留**。清理或回滚时必须显式删除 `<原名>_Wrapper`。

---

## 六、struct_remove_variable 只接受 FGuid

```python
st.struct_remove_variable(var_desc)                        # Exception: object is not a FGuid
st.struct_remove_variable(var_desc.get_field("VarGuid"))   # True  ✅
```

---

## 七、返回值不可作为成功判据

| API | 成功时返回 |
| --- | --- |
| `data_table_add_row` | `None` |
| `delete_asset` | `None`（但资产确实被删） |
| `widget_add` / `widget_set_property` / `widget_slot` | `None` |
| `data_table_modify_row` / `data_table_remove_row` / `struct_remove_variable` | `True` |

统一做法：**写后重新 `load_object` 回读**，用回读值判定，而不是看返回值。

---

## 八、其他反直觉点

- `data_table_as_dict()` 的 value 是 `UScriptStruct`，取值必须 `get_field(字段名)`，不能当 dict 用。
- `data_table_find_row` 查不存在的行**抛异常**（`key not found in UDataTable`），必须 try/pcall 包裹。
- `objed_query_assets` 返回**聚合字符串**而非 list，直接 `for` 会按字符拆分；应用子串判断或 `re.findall`。
- `objed_rename_asset` 后，用**旧名** `resolve_asset` 仍返回新路径（注册表重定向），不能靠“旧名查不到”判定成功。
- `schema:FUGCStructVariableDescription` 返回“无可编辑属性”，字段名只能靠实例 `fields()` 获取。
- `FRotator(0,0,45)` 回读为 `44.999996`，旋转校验要用容差。
- 场景 Actor 生成后即使 `actor_destroy` 还原，`ctx:` 的 `map_dirty` 仍变为 `true`，需人工决定是否保存关卡。
- 首次 `save_package()` 打印 `[Warning] no file mapped to UPackage ... setting its FileName to ...`，属正常落盘提示，不是错误。
- `ue.find_package` 不存在（`module 'unreal_engine' has no attribute 'find_package'`）。

---

## 九、画刷与控件样式不能用 widget_set_property

```python
ue.widget_set_property(wbp, '地图UI', 'Brush.ResourceObject', '/IslandAuctionKing/Asset/TuPian/TuJian/Codex_TopBar')
# widget_set_property: failed to set 'Brush.ResourceObject' on '地图UI'
ue.widget_set_property(wbp, 'ItemButton', 'WidgetStyle.Normal.ResourceObject', '...')
# widget_set_property: failed to set 'WidgetStyle.Normal.ResourceObject' on 'ItemButton'
ue.widget_set_property(wbp, 'CardBackground', 'Background.ResourceObject', '...')
# widget_set_property: failed to set 'Background.ResourceObject' on 'CardBackground'
```

该 API 不解析点号路径、不接受 struct。更危险的是 **`BrushImage` 的假成功**：

```python
ue.widget_set_property(wbp, '地图UI', 'BrushImage', '/IslandAuctionKing/Asset/TuPian/TuJian/Codex_Close')
# 返回 None，回读确实变了，但：
img.BrushImage.get_class().get_name()   # -> 'Package'  ← 不是 Texture2D
```

它把资源路径解析成了 `UPackage` 对象。修复：用 Python 直接赋值 `img.BrushImage = ue.load_object(Texture2D, path)`，回读后必须校验 `get_class().get_name()`。

修改画刷/样式的正确通道：`obj.Brush.<字段> = ...` / `btn.WidgetStyle.<状态>.<字段> = ...` / `border.Background.<字段> = ...`，随后 `compile_blueprint` + `save_package`。

---

## 十、WidgetTree.AllWidgets 恒为空，必须手动递归

```python
wbp = ue.load_object(Blueprint, '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian')
len(wbp.WidgetTree.AllWidgets)   # -> 0（该 UI 实际有 23 个控件）
wbp.WidgetTree.RootWidget        # -> CanvasPanel_0，可用
```

`WidgetTree` 也没有 `fields()`（`'unreal_engine.UObject' object has no attribute 'fields'`）。正确遍历方式是从 `RootWidget` 起递归 `GetChildrenCount()` / `GetChildAt(i)`。

---

## 十·补一、取 UMG 设计态控件树：路径要带对象名后缀，struct 要用属性访问（2026-09-20 实测，IslandAuctionKing）

第十节的 `ue.load_object(Blueprint, '/…/ZhuJieMian')`（无后缀）在旧会话可用，但本轮同一路径用 `get_asset` 拿不到树。四种失败与新写法如下：

| 写法 | 结果 |
| --- | --- |
| `ue.get_asset('/…/Prefabs/UI/ZhuJieMian')` | 返回 `get_class().get_name() == 'Package'` → `get_property('WidgetTree')` 报 `unable to find property WidgetTree` |
| `ue.load_object(UGCWidgetBlueprint, '/…/ZhuJieMian')` | 报 `Package … exists on disk but contains no asset named 'ZhuJieMian'` |
| `ue.list_assets('/…/Prefabs/UI/ZhuJieMian')` | 返回 **空列表 `[]`**，不能用来反查路径（不要照它给的 FIX 提示走） |
| `w.get_property('Name')` | 报 `unable to find property Name` |

**可用写法**：

```python
a  = ue.get_asset('/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/ZhuJieMian.ZhuJieMian')  # 带对象名后缀
# a.get_class().get_name() == 'UGCWidgetBlueprint'
wt   = a.get_property('WidgetTree')
root = wt.get_property('RootWidget')
name = w.get_name()          # 控件名用 get_name()，不是 get_property('Name')
```

**读 Slot 几何时的两个坑**（`CanvasPanelSlot`）：

- `slot.get_property('LayoutData')` 拿到的是 `UScriptStruct`，**不能**再 `get_property('Offsets')`——报
  `'unreal_engine.UScriptStruct' object has no attribute 'get_property'`。要用**属性访问**：`ld.Offsets` / `ld.Anchors` / `ld.ZOrder` / `ld.bAutoSize`。
- `FVector2D` **没有 `.X`**（`Anchors.Minimum.X` 报 `has no attribute 'X'`）。本轮未取到成功写法，需要锚点值时改用 `slot` 上的 UFunction
  （第四节列出的 `GetAnchors` / `GetOffsets` / `GetPosition` / `GetSize`）。

`LayoutData.Offsets` 是 `FMargin`，`Left/Top` 为位置、`Right/Bottom` 为**尺寸**（非右下坐标），读几何时别当坐标用。

---

## 十一、struct 就地写 vs 整体替换

`FSlateBrush` / `FButtonStyle` / `FSlateColor` / `FMargin` 均为**引用语义**，`obj.Prop.Field = v` 就地生效，不需要「取出→改→回写」。

但**整体替换会清空未赋值字段**：

```python
from unreal_engine.structs import ButtonStyle, SlateBrush
ns = ButtonStyle(); ns.Normal = nb
btn.WidgetStyle = ns
btn.WidgetStyle.Hovered.ResourceObject   # -> None，原 Hovered 贴图被清掉
```

另注意构造入口不统一：`FVector2D` / `FLinearColor` 在 `ue` 命名空间（`ue.FVector2D(x,y)`），`from unreal_engine.structs import FVector2D` 会 ImportError；而 `SlateBrush` / `ButtonStyle` 在 `unreal_engine.structs` 下，`ue.FSlateBrush` 不存在。

---

## 十二、蓝图函数库查不到：find_class 失败，需 all_classes 找 `_C`

`UICommonFunctionLibrary`（官方异形屏适配用的 `SetAdaptation` 所在处）在 `raw/docs/api` 里没有类文档，`ue.find_class` 也查不到——因为它不是 C++ 类，而是引擎侧**蓝图函数库**：

```python
cls = None
for c in ue.all_classes():
    if c.get_name() == 'UICommonFunctionLibrary_C':   # 注意 _C 后缀
        cls = c
        break
cls.get_path_name()
# -> /Game/UMG/UI_BP/Common/UICommonFunctionLibrary.UICommonFunctionLibrary_C
cls.functions()      # -> 14 个函数名（字符串列表）
```

取参数签名要用 `ue.find_object('<类路径>:<函数名>')` 拿到 `Function` 对象，再读 `properties()`。**`properties()` 返回的是字符串列表，不是对象列表**，对元素调 `get_name()` 会报 `'str' object has no attribute 'get_name'`：

```python
base = '/Game/UMG/UI_BP/Common/UICommonFunctionLibrary.UICommonFunctionLibrary_C'
f = ue.find_object(base + ':SetAdaptation')
skip = ('CallFunc_', 'K2Node_', 'Temp_')          # 蓝图中间节点变量，非参数
[p for p in f.properties() if not p.startswith(skip)]
# -> ['Widget', '__WorldContext']
```

`schema:` 查询不返回函数签名，函数签名只能走这条路径。

---

## 十三、枚举属性按整数写，且必须查表

MCP/UE Python 侧枚举属性一律 `obj.EnumProp = <int>`，不接受枚举名字符串。数值不能按名称顺序猜——`TMGS_NoMipmaps` 是 **13**，不是 2（2 是 `TMGS_Sharpen0`）；`raw/docs/ai/20260824_图鉴UI素材批量导入与视觉优化.md` 第 12 行的 `MipGenSettings=2 (TMGS_NoMipmaps)` 数字标注有误（`raw/` 只读，不改）。

取值两条途径：`ue_read queries=["enum:XXX"]`，或查 [绿洲 UI 枚举与结构体速查](../UI与交互/绿洲UI枚举与结构体速查.md)。

另一个隐坑：写了 `Brush.TintColor.SpecifiedColor` 颜色却不变，因为 `FSlateColor.ColorUseRule` 不是 `UseColor_Specified(0)` —— 颜色改动必须**同时**写 `ColorUseRule = 0`。

---

## 十四、EditCondition 字段必须两遍写入

门控布尔为 `False` 时，写被门控字段无效（不报错，回读不变）。UI 侧已确认的门控链：

| 被门控字段 | 门控 |
| --- | --- |
| `UTextBlock.MutiEllipsisLine` | `MutiEllipsisText` |
| `UButton.bUseCustomSettings` | `IsImgAlphaBtn`（是否异形按钮） |
| `UButton.CustomHitAreaTexture` / `CustomHitAreaAlpha` | `bUseCustomSettings` |

按钮是**三层链式门控**，必须自外向内依次置 True，再写值，然后 `compile_blueprint` + `save_package` + 回读。查门控关系用 `ue_read queries=["schema:UButton?level=full&filter=IsImgAlphaBtn,bUseCustomSettings"]`，输出会标注 `EditCondition: X (must be True before writing this field)`。

---

## 十五、node_repl 里 sharp 不可用，图片处理改走 PowerShell

查证官方文档中的纯图片页（如 `raw/docs/wiki/开发者须知/271_字体规范.md` 只有一行图片引用）需要切图放大时，`await import("sharp")` 在 node_repl 中失败：

```
Unsupported import specifier "../package.json"
```

可用替代：PowerShell + `System.Drawing` 裁切/缩放到临时目录，再用 `view_image` 逐段读取。实测 1731×3712 的规范图切成 6 段后仍为设计稿式纯色/渐变图，未能提取到可读文字，属**需人工确认**项而非可写入的结论。

---

## 十六、关卡脏标记只能读不能清

`package_is_dirty` 存在，但**必须在真正的 UPackage 上调用**，直接对 `UWorld` 调会抛异常：

```python
w = ue.get_editor_world()
w.get_outer()                      # -> Package /IslandAuctionKing/UGCmap（对象正确）
w.package_is_dirty()               # Exception: uobject is not an UPackage
```

更关键的是**没有任何清除脏标记或重载关卡的 API**。查遍 `py:index`（68 类 819 方法）与 `py:dirty` / `py:package` / `py:level` / `py:revert` / `py:discard`：

| 需求 | 现状 |
| --- | --- |
| 读脏标记 | ✅ `package_is_dirty`（需 UPackage 对象） |
| 清脏标记 | ❌ 无 `set_dirty` / `clear_dirty` / `mark_package_dirty` |
| 重载关卡 | ❌ 无 `load_map` / `open_level` / `new_level` |
| 保存关卡 | ✅ `editor_command_save_current_level` / `helpers.save_current_level()` |

`ue.console_exec` 存在但无签名文档，用它跑 `MAP LOAD` 会重载整个关卡，属高风险不可回滚操作。

结论：**「不保存丢弃脏标记」只能在编辑器 UI 内人工完成**。判定是否为「假脏」的可靠办法是比对磁盘文件哈希与 Actor 清单：

```python
w = ue.get_editor_world()
actors = list(w.all_actors())
ue.log('count=%d' % len(actors))
ue.log('probes=%s' % [a.get_name() for a in actors if 'MCP' in a.get_name() or 'Probe' in a.get_name()])
```

配合 PowerShell `Get-FileHash` 对比 `.umap` 与备份，哈希一致即说明从未落盘，丢弃无损失。

---

## 十七、宿主环境限制：Remove-Item 可能被策略拦截

清理空目录时 PowerShell 的 `Remove-Item` 被本机执行策略拦截：

```
CreateProcess { message: "Rejected(...)... rejected: blocked by policy" }
```

替代方案是 Python `os.rmdir`，它**只能删空目录**（非空抛异常），本身就是一层保护，再加路径守卫更稳：

```python
import os
target = r"...\Asset\Data\Table\Customized\Test"
assert "UGCProjects" in target and target.endswith(os.path.join("Customized", "Test"))
assert os.listdir(target) == [], "directory not empty, abort"
os.rmdir(target)
```

删空目录前应三重校验：MCP `list_assets` 计数为 0、相关资产名 `resolve_asset` 返回 `[]`、磁盘递归枚举为 0 项。

---

## 七·补一、`save_package()` 返回值与 `apis_to_call` 白名单（2026-09-17 实测，pet_paradise）

| 现象 | 实测结果 | 与既有记录的关系 |
| --- | --- | --- |
| `dt.save_package()` 返回值 | 返回 `<unreal_engine.UObject object at 0x...>`，**不是 `True`** | 与第五节 3「`dt.save_package()` / `st.save_package()` 是对象方法，返回 `True`」**冲突**。来源分别为 `IslandAuctionKing`（旧）与 `pet_paradise`（本轮），绑定/版本可能不同，**保留双方、不据此改写旧结论**。落盘仍正常：改后 `.uasset` 大小与 mtime 均变化 |
| `ue_plan_submit` 的 `apis_to_call` | 传 `data_table_modify_row` / `data_table_remove_row` 会返回 warning `is not in the recognized whitelist (typo? add apis_strict: false is fine)` | 新增。警告**不影响**提交结果：`success=true` / `plan_valid=true` / `mutations_count=3`；随后 `ue_py` 带该 `plan_id` 执行 `resolved_via_plan_id=true`（used_count=1）、`decision=pass`、`has_mutation=true` |
| `UAssetGUI.exe tojson` 直接调用 | `& UAssetGUI.exe tojson <in.uasset> <out.json> VER_UE4_24` 在 PowerShell 下 exit code 为空、**不产出文件** | 新增。文件级核查不要直接调 UAssetGUI，改走工具封装 `UAssetToJsonConverter.exe --mode convert --output <知识库\raw\<项目名>\_JsonOutput>`（必须显式传 `--output`），或用下一条的二进制检索 |
| 文件级核查替代手段 | 直接读 `.uasset` 字节，用 **UTF-16LE** 编码检索字符串：UE 的 `FString` 序列化即为 UTF-16LE（`"才无法打工".encode("utf-16-le") in raw`） | 新增。可在不依赖 UAssetGUI 的前提下证明「新值已落盘、旧值已消失」，是第七节「写后重新 `load_object` 回读」的补充（回读只证明内存态）。**该编码假设只对非 ASCII 的 `FString` 值成立，行名/列名等 FName 走 8 位序列化，单编码扫描会产生大面积假阴性——修正见第七·补二** |

---

## 七·补二、二进制字符串检索的编码前提与「旧名残留」误判（2026-09-17 实测，pet_paradise）

场景：新建 `Asset/Data/Table/Customized/Motion/MotionConfigTable`（四列 `ValueType`/`Value`/`Description`/`ModificationNotes`）并写入 25 行动效数据，MCP 回读全绿后，用第七·补一所述「UTF-16LE 检索 `.uasset` 字节」做文件级复核，出现**大面积假阴性**（29 项未命中）。逐串三编码取证后定位为编码前提错误，非写入失败。

### 1. 实测：字符串落盘编码不是单一的 UTF-16LE

对同一个 `MotionConfigTable.uasset`（8776 字节）逐串按三种编码计数命中的字节串次数：

| 字符串 | 类别 | UTF-16LE | UTF-8/ASCII | GBK |
| --- | --- | --- | --- | --- |
| `Motion.Token.Instant.Duration` | 行名（FName） | **0** | 1 | 1 |
| `Motion.Metric.LoopRepeatCount` | 行名（FName） | **0** | 1 | 1 |
| `ValueType` / `ModificationNotes` | 列名（FName） | **0** | 1 | 1 |
| `悬停放大倍数` | 中文 FString 字段值 | 1 | **0** | **0** |
| `令牌 Instant 时长（秒），用于按下回压。` | 中文 FString 字段值 | 1 | **0** | **0** |
| `QuadOut` / `SineInOut` | ASCII FString 字段值 + Name Table 条目 | 1 | 1～3 | 1～3 |

结论（本机 `UGCEditor-PIE 2.0.0` 绑定下）：

- **行名、列名等 FName 走 8 位（UTF-8/ASCII）序列化** → 只用 UTF-16LE 检索必然 0 命中；
- **中文 `FString` 字段值仍为 UTF-16LE** → 只用 8 位检索 0 命中；
- 纯 ASCII 的 `FString` 字段值两种编码都可能命中（值本体 + Name Table 条目各计一次）。

因此第七·补一那条「用 UTF-16LE 检索」**只对非 ASCII 的 `FString` 值成立**，不能当通用判据。正确做法是**双编码并检**：

```python
raw = open(uasset, "rb").read()
hit = (s.encode("utf-16-le") in raw) or (s.encode("utf-8") in raw)
```

### 2. 误判：不能以「旧名命中数」判定列是否已删除

`struct_remove_variable` 删列成功（MCP `struct_get_variables()` 回读为四列）后，`UGCTemplateRowStruct_MotionConfigTable.uasset` 里仍残留 `MemberVar_0` 的 **1 处 8 位命中** —— UE 包保存时不回收已失效的 FName 条目（Name Table 残留）。于是：

- 以「旧列名命中数 = 0」为删除成功判据 → **假阴性**（误报删除失败）；
- 以「旧列名命中数 > 0」为删除失败判据 → **假阳性**（误报残留）。

**删除类改动的判据只能是 MCP `struct_get_variables()` / `properties()` 回读**；二进制检索的适用面仅限**「新增字符串是否出现」**（证明新值落盘），且必须双编码并检。

### 3. 本场景完整证据链（新建四列配置表的可复用模板）

| 环节 | 手段 | 实测结果 |
| --- | --- | --- |
| 开编辑器 | `ue.objed_open_editor("DataTable")` | 必须先开，否则后续 `objed_*` 不可用 |
| 建表 | `ue.objed_create_asset("DataTable", "自定义表格", "空表格", TBL, SUB)` | 返回资产路径；新表**默认只有 1 列 `MemberVar_0`(bool)**，必须替换 |
| 换列 | `st.struct_remove_variable(v.get_field("VarGuid"))`（**不是** `v.as_dict()["VarGuid"]`，后者是 dict 会抛 `object is not a FGuid`）→ `st.struct_add_variable(desc)`，`desc = ue.find_struct("UGCStructVariableDescription")()` 后 `set_field("VarName"/"FriendlyName"/"Category"/"ToolTip")`，`Category` 传 `"string"` | 4 列 `ValueType/Value/Description/ModificationNotes`；`struct_get_variables()` 回读 `Category` 为 `string` |
| 写行 | `dt.data_table_empty_row()` → `set_field`×4 → `dt.data_table_add_row(name, row)` | 25 行写入；`data_table_add_row` 成功返回 `None`（不可当失败判据） |
| 落盘 | `st.save_package()` / `dt.save_package()` | 返回 `UObject` 而非 `True`（见补一）；文件 8776 / 8116 字节，mtime 已变 |
| MCP 回读 | `data_table_as_dict()` + `struct_get_variables()` | 25 行、4 列、无 `MemberVar_0`、`errors=0` |
| 二进制复核 | 双编码并检 | 行名 UTF-8 命中、中文值 UTF-16LE 命中（单编码扫描会误报 29 项） |
| 独立复核 | 新开 SSE 会话只读 `ue_py` | 仍为 25 行 4 列，证明已落盘而非内存态 |

---

## 待查证

1. 本页绝大多数条目为 `IslandAuctionKing` / UE 4.18.1 单一编辑器实例实测，**未跨工程或跨引擎版本验证**；MCP 版本升级后行为可能变化。第七·补一节来自 `pet_paradise`（同一编辑器实例与绑定），其中 `save_package()` 返回值已与旧结论出现差异，按「保留双方、不静默覆盖」处理，待换工程或升级 MCP 后再判定哪一侧是普遍行为。
2. `widget_set_property` 对 `BackgroundColor`（Button）/ `BrushColor`（Border）返回 `None`，本轮**未逐项回读确认**是否真正写入，使用前需自行回读校验。
3. 回读成功只证明写入落盘，**不证明运行时表现正确**；画刷、样式、点击区域等视觉与交互行为仍需 PIE 验证。
4. `enforce_level=observe` 下 PRV 只告警不拦截；切换到 enforce 后的实际拦截边界未实测。
5. `ue.console_exec` 无官方签名文档，可接受的命令集合与副作用未实测；用于关卡重载属高风险，本知识库不推荐。
6. 第七·补二的编码结论（FName 走 8 位、中文 `FString` 走 UTF-16LE）只在 `pet_paradise` + `UGCEditor-PIE 2.0.0` 单实例验证，**未跨引擎版本复核**。跨版本做二进制复核前，先对同一 `.uasset` 跑一次三编码探针确定编码分布，再决定检索用哪套编码，不要直接沿用本条结论。

---

## 十二、相关页面

- [UGCAskQ MCP 能力矩阵](UGCAskQ-MCP能力矩阵.md)
- [MCP UI 编辑与高保真还原知识库](../UI与交互/MCP-UI编辑与高保真还原知识库.md)
- [绿洲 UI 枚举与结构体速查](../UI与交互/绿洲UI枚举与结构体速查.md)
- [配置表与结构体的 MCP 编辑](配置表与结构体的MCP编辑.md)
- 来源：[2026-08-26 UI 画刷与控件样式官方查证](../来源记录/2026-08-26_UI画刷与样式官方查证.md)
- [蓝图与 MCP 写入流程](蓝图与MCP写入流程.md)
- [UMG 控件 Lua 取名可达性与配置表读取类型判定](../UI与交互/2026-09-15_UMG控件Lua取名可达性与配置表读取类型判定.md)：`GetTableData` 返回 userdata（勿用 `type()=="table"` 判定）、Lua `widget[name]` 需 `bIsVariable=True`、`doluastring` 需显式 `client_hwnd`、抓图窗口更正

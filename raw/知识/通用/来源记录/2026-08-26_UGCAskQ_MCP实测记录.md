# 2026-08-26 UGCAskQ MCP 编辑器修改能力实测

> 记录性质：本页即一手实测记录（`raw/` 为只读同步目录，不写入）
> 实测环境：OasisEraEditor(2001776) / ShadowTrackerExtra / UE 4.18.1-0+++UE4+Release-4.18
> UGC 工程：IslandAuctionKing（挂载点 `/IslandAuctionKing`，启动地图 `/IslandAuctionKing/UGCmap`）

---

## 一、这份资料是什么

在真实编辑器实例上，用 UGCAskQ MCP 的三个工具（`ue_read` / `ue_plan_submit` / `ue_py`）逐项跑通并回读验证编辑器修改能力，覆盖 PRV 机制、DataTable、UserDefinedStruct、蓝图、UMG、场景 Actor、资产增删改名。所有结论均带实际返回值，测试资产已清理。

与既有资料的区别：`raw/docs/wiki/绿洲编辑器基础内容/20414_UGCAskQ MCP 使用说明.md` 是官方能力声明，本页是**同一套 API 在本地工程上的实际行为与失败模式**。

---

## 二、覆盖范围

| 维度 | 实测内容 |
| --- | --- |
| 能力面基线 | `ctx:` / `qt:`（10 类结构化查询）/ `py:index`（68 分类、819 方法） |
| PRV 机制 | 无 plan 的 mutation 告警、plan_id 复用与 TTL、事务回滚 |
| DataTable | 建表、4 列结构改造、行增/改/删、保存回读 |
| UserDefinedStruct | `struct_add_variable` / `struct_remove_variable` 与描述字段 |
| 蓝图 | `create_blueprint`、成员变量、组件、编译、CDO 两段式写入、Lua 绑定路径 |
| UMG | 控件树读写、`widget_slot` 支持范围、`widget_wrap` 语义、资产复制与重命名 |
| 场景 | `actor_spawn` / Transform / Label / Folder / Mesh / `actor_destroy` |
| 只读查询 | `schema:` / `subclasses:` / `enum:` / `bt:nodes` / `resolve_asset` |

---

## 三、提炼出的关键结论

1. PRV 的 mutation 判定是**代码文本静态检测**，不是实际写入目标；当前 `enforce_level=observe`，违规只告警。
2. `objed_*` 系列必须先 `objed_open_editor(<类型>)` 才能拿到 asset handler。
3. `duplicate_asset` 对 `UGCWidgetBlueprint` 会产出游离包对象且删不掉；UI/物编资产必须用 `objed_duplicate_asset`。
4. `widget_slot` 只支持 `ZOrder` / `bAutoSize`；位置尺寸要走 `Slot.SetPosition/SetSize`。
5. 多个写入 API 返回 `None` 也代表成功，**必须回读验证**，不能用返回值判定。

---

## 四、衍生的概念页

- [UGCAskQ MCP 能力矩阵](../工具与流程/UGCAskQ-MCP能力矩阵.md)
- [UGCAskQ MCP 实测陷阱清单](../工具与流程/UGCAskQ-MCP实测陷阱清单.md)
- [配置表与结构体的 MCP 编辑](../工具与流程/配置表与结构体的MCP编辑.md)
- 已回写：[蓝图与 MCP 写入流程](../工具与流程/蓝图与MCP写入流程.md)、[配置表驱动开发](../配置与数据/配置表驱动开发.md)

---

## 五、证据边界

- 全部结论来自单一编辑器实例（IslandAuctionKing / UE 4.18），未在其他工程或版本交叉验证。
- 本地社区归档（`sq-skill`，快照 2026-05-31，1229 帖）以 `unreal_engine` / `MCP` / `编辑器 Python` 检索**无命中**，社区侧无可对照经验。
- 回读成功只证明写入落盘，不证明运行时行为正确；运行行为需 PIE 验证。

---

## 附录：完整实测流水与返回值

以下为逐项实测的原始过程、代码与实际返回值，供复核与复现。

### 附1. 环境与能力面基线（ue_read 只读）

```
ue_read queries=["ctx:", "qt:", "py:index"]
```

- `ctx:` 返回引擎工程目录、UGC 工程名/根目录/Asset/Script 目录、启动地图、`map_dirty`、`world_type`、`is_debug_playing`、已打开资产与物编 Tab、选中 Actor 数。
- `qt:` 结构化查询类型共 10 种：`bp / bt / classmember / context / enum / fusion / hierarchy / objed / skilldoc / struct`。
- `py:index` Python API：**68 个分类、819 个方法**。其中 UGCAskQ 扩展分类：`asset_browser(7) / bb(4) / bp_lua(2) / bt(8) / ga(21) / gamemode_config(2) / helpers(8) / objed(10) / persist_skill(61) / project(8) / scene(1) / widget_edit(9)`。

### 附2. PRV（Plan-Resolve-Verify）机制实测

#### 附2.1 无 plan 执行含写语义代码

代码里只有对临时 Python 对象的 `setattr`，服务端仍判定为 mutation：

```json
"prv": {"decision":"warn_pass","enforce_level":"observe","has_mutation":true,"plan_valid":false}
"warnings": ["[PRV-Observe] [!] VIOLATION: Mutation code executed WITHOUT a valid plan: plan field not provided..."]
```

结论：PRV 的 mutation 判定是**基于代码文本的静态检测**（`setattr`/`save_package`/`actor_spawn` 等关键字），不是基于实际写入目标。当前服务端为 `observe` 等级，违规只告警不拦截。

#### 附2.2 提交 plan 后复用 plan_id

```
ue_plan_submit {plan: <YAML>} -> {"plan_id":"plan_16780598_7571df3e","expires_at_seconds":...,"ttl_seconds":900}
ue_py {code, plan_id:"plan_16780598_7571df3e"}
```

- 同一 plan_id 可跨多次 `ue_py` 复用，返回中 `used_count` 递增（本次实测同一 plan_id 用到 10 次）。
- TTL 默认 900 秒，可用 `ttl_seconds` 调整（区间 [30,3600]）。
- 纯查询代码返回 `prv_phase_hint: "Pure-query code detected; PRV plan not required."`，即使带了 plan_id 也按纯查询处理。
- plan 必须落在 `/<ProjectName>/...`，`/Game/` 开头会被拒绝。

#### 附2.3 事务回滚

`ue_py` 传 `transaction_name` 时整段代码包在事务里。中途抛异常返回：

```json
"recovery_hint": "Transaction was cancelled due to error. No changes were made."
```

实测确认：`duplicate_asset` 后紧接 `load_object` 失败那次，事务回滚，UI 目录未残留资产（后续 `list_assets` 与磁盘 `Get-ChildItem` 双向确认）。

### 附3. DataTable / UserDefinedStruct 写能力

#### 附3.1 创建自定义配置表（objed 必须先 open_editor）

第一次直接调用失败：

```
ue.objed_create_asset('DataTable', '自定义表格', '空表格', 'MCPTestConfigTable', 'Test')
-> "Cannot get asset handler for DataTable/自定义表格."
```

同时试 `功能表格` 报同样的 handler 错误，`内置表格`/`模板功能表格` 报 `template_name '空表格' not found ... Available: `（模版列表为空）。

先打开物编编辑器 Tab 后成功：

```python
ue.objed_open_editor('DataTable')          # -> True
ue.objed_create_asset('DataTable', '自定义表格', '空表格', 'MCPTestConfigTable', 'Test')
# -> '/IslandAuctionKing/Asset/Data/Table/Customized/Test/MCPTestConfigTable'
```

回读目录确认同时生成两个资产：

- `/IslandAuctionKing/Asset/Data/Table/Customized/Test/MCPTestConfigTable`（DataTable）
- `/IslandAuctionKing/Asset/Data/Table/Customized/Test/UGCTemplateRowStruct_MCPTestConfigTable`（UserDefinedStruct）

物编各编辑器 asset_type 与根目录（`objed_query_asset_types`）：

```
DataTable: 内置表格(/Game/表格) / 自定义表格(/Asset/Data/Table/Customized, 模版1) /
           功能表格(/Asset/Data/Table, 模版8) / 模板功能表格(/ExtendResource)
UI:        元件(/Asset/Blueprint/Prefabs/UI, 模版22) / 界面布局(/Asset/Blueprint/Prefabs/WidgetLayout, 模版1)
```

`自定义表格` 唯一模版为 `空表格`（源 `/Game/UGCEditor/UGCConfigAsset/DataTableTemplate/UGCTemplateDataTable`，create_method=Duplicate）。

#### 附3.2 空表格的默认列与 4 列结构改造

新建表的行结构体默认只有一个 bool 列：

```
row_props: ["MemberVar_0_E925F48B4B1EE84561F1309EEE8B57EC"]
FriendlyName=MemberVar_0, Category=bool
```

对照已有 `AuctionGlobalConfigTable`（149 行）的行结构体，4 列描述字段实测取值：

| VarName | FriendlyName | Category | ToolTip |
| --- | --- | --- | --- |
| ValueType | 配置类型 | string | 配置值类型：int、float、bool 或 string。 |
| Value | 配置值 | string | 运行时由 AuctionConfig 读取的具体配置值。 |
| Description | 配置说明 | string | 说明配置用途、默认值和修改注意事项。 |
| ModificationNotes | 修改注意事项 | string | 保存配置修改边界、关联依赖和生效方式。 |

加列代码（实测通过）：

```python
st = ue.load_object(UserDefinedStruct, "/IslandAuctionKing/Asset/Data/Table/Customized/Test/UGCTemplateRowStruct_MCPTestConfigTable")
desc_struct = ue.find_struct('UGCStructVariableDescription')
for var_name, friendly, tip in cols:
    d = desc_struct()
    d.set_field("VarName", var_name)
    d.set_field("FriendlyName", friendly)
    d.set_field("Category", "string")
    d.set_field("ToolTip", tip)
    st.struct_add_variable(d)          # 返回 FGuid
st.save_package()
```

`FUGCStructVariableDescription` 实际字段（`d.fields()`）：

```
VarName, VarGuid, FriendlyName, DefaultValue, Category, SubCategory, SubCategoryObject,
PinValueType, ContainerType, bIsArray, bIsSet, bIsMap, bInvalidMember, bDontEditoOnInstance,
bEnableMultiLineText, bEnable3dWidget, CurrentDefaultValue, ToolTip, MetaDataKeyValues,
ArrayInnerPropertyMetaDataKeyValues, MapKeyPropertyMetaDataKeyValues,
MapValuePropertyMetaDataKeyValues, SetElementPropertyMetaDataKeyValues
```

注意 `schema:FUGCStructVariableDescription` 查不到可编辑属性（返回 `no editable or blueprint-visible properties`），字段名只能靠实例 `fields()` 拿到。

删除默认 bool 列时，入参形式有坑：

```python
st.struct_remove_variable(var_desc)              # -> Exception: "object is not a FGuid"
st.struct_remove_variable(var_desc.get_field("VarGuid"))   # -> True   ✅
```

保存后回读，DataTable 的 `RowStruct.properties()` 同步变为 `["ValueType","Value","Description","ModificationNotes"]`。

#### 附3.3 行增 / 改 / 删

```python
row = dt.data_table_empty_row()
row.set_field("ValueType", "string")
row.set_field("Value", "MCPWriteTest")
dt.data_table_add_row("Test.MCPWriteProbe", row)                        # 返回 None（不是 bool）
dt.data_table_modify_row("Test.MCPWriteProbe", "Value", "MCPWriteTest_Modified")  # 返回 True
dt.data_table_remove_row("Test.MCPRemoveProbe")                          # 返回 True
dt.save_package()
```

保存后重新 `load_object` 回读结果（全部符合预期）：

```json
{"Test.MCPWriteProbe": {"ValueType":"string","Value":"MCPWriteTest_Modified",
 "Description":"UGCAskQ MCP 写能力验证行","ModificationNotes":"测试用一次性行，验证后随资产一并删除"}}
```

- 行名支持点号分层中文/英文混排（`Test.MCPWriteProbe` 正常）。
- `data_table_add_row` 返回 `None` 也代表成功，**不能用返回值判定**，必须回读。
- 查询已删除行：`dt.data_table_find_row(name)` 抛 `key not found in UDataTable`，需 pcall/try 包裹。
- `data_table_as_dict()` 的 value 是 `UScriptStruct` 对象，取值要 `get_field(名)`，不能直接当 dict 用。
- 首次 `save_package()` 会打印 `[Warning] no file mapped to UPackage ... setting its FileName to ...`，属正常落盘提示。

### 附4. 蓝图写能力

#### 附4.1 新建蓝图 + 变量 + 组件 + 编译（耗时 35s）

```python
bp = ue.create_blueprint(Actor, ue.get_project_root() + "/Asset/Blueprint/MCPProbeActor")
ue.blueprint_add_member_variable(bp, 'ProbeSpeed', 'float')   # True
ue.blueprint_add_member_variable(bp, 'ProbeEnabled', 'bool')  # True
ue.add_component_to_blueprint(bp, StaticMeshComponent, 'ProbeMesh')
ue.compile_blueprint(bp)
bp.save_package()
```

回读 CDO：`["ProbeMesh","ProbeSpeed","ProbeEnabled"]` 全部存在。
本次调用 `execution_time_ms = 35441`（约 35 秒），是本轮所有操作中最慢的一次——新建蓝图+编译要留足超时预算。

`bp_lua_get_path` 返回该蓝图对应 Lua 路径（此时文件尚未创建）：

```json
{"exists": false,
 "lua_path": ".../IslandAuctionKing/Script/Blueprint/MCPProbeActor.lua",
 "folder_path": ".../IslandAuctionKing/Script/Blueprint"}
```

对照正式 UI 蓝图 `AuctionTestUI`：`exists=true`，路径 `.../Script/Blueprint/Prefabs/UI/AuctionTestUI.lua`。证实 Asset 目录相对路径 = Script 目录相对路径。

#### 附4.2 CDO 两段式写入

```python
targets = [("ProbeSpeed", 123.5), ("ProbeEnabled", True)]
gates = set()
for p, _ in targets:
    up = cdo.get_uproperty(p)
    if up and up.has_metadata('EditCondition'):
        gates.add(up.get_metadata('EditCondition'))
for g in gates: setattr(cdo, g, True)     # 本例 gates 为空
for p, v in targets: setattr(cdo, p, v)
bp.save_package()
# 重新 load 回读: {"ProbeSpeed":"123.5","ProbeEnabled":"True"}   before: {"0.0","False"}
```

服务端 PRV 识别到两段式检查：`"has_editcondition_check": true, "writes_to_cdo": true`。
蓝图自建的成员变量没有 EditCondition 门控（`gates=[]`）；门控主要出现在引擎内置 CDO 属性（如武器 `bIsAttributeOverride`）。

### 附5. UI / UMG 写能力

#### 附5.1 duplicate_asset 对 UGCWidgetBlueprint 不可用（重要陷阱）

```python
ue.duplicate_asset(src, "/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/MCPTestUIProbe")
# 返回对象: get_class()=='Package', get_path_name()=='/IslandAuctionKing/Asset/Blueprint/Prefabs/UI.MCPTestUIProbe'
```

两参数与三参数形式结果相同：**把资产复制成了目录同名包里的一个对象**，路径变成 `UI.MCPTestUIProbe` 而非 `UI/MCPTestUIProbe`。后果：

- `list_assets` / `resolve_asset` 都查不到它（AssetRegistry 无条目）；
- 磁盘上多出游离文件 `Asset/Blueprint/Prefabs/UI.uasset`（529 字节，与 `UI/` 目录同名）；
- `ue.delete_asset` 对该路径返回 `None`，删不掉。

正确入口是物编专用 API：

```python
ue.objed_duplicate_asset('CollectibleCodexItemUI', 'MCPTestUIProbe', 'UI')
# -> '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/MCPTestUIProbe'
# resolve_asset 可查到 -> '.../MCPTestUIProbe.MCPTestUIProbe'
```

另一处相关陷阱：`duplicate_asset` 之后未保存就 `load_object`，会抛详细诊断异常并回滚事务：

```
unable to load object '...MCPTestUIProbe' (class=Blueprint).
[DIAGNOSIS] Package ... does NOT exist on disk. The path is wrong.
[FIX] ue.resolve_asset('MCPTestUIProbe') / ue.list_assets(...) / ue.search_game_assets(...)
```

#### 附5.2 控件树读写

UI 蓝图类是 `UGCWidgetBlueprint`，但 `ue.load_object(Blueprint, path)` 可正常加载。

```python
ue.widget_inspect(wbp)                      # 树形字符串，含类型/名称/父容器/Pos/Size
ue.widget_add(wbp, 'TextBlock', 'MCPProbeText', 'CanvasPanel_0')
ue.widget_set_property(wbp, 'MCPProbeText', 'Text', 'MCP Probe OK')       # OK
ue.widget_set_property(wbp, 'MCPProbeText', 'ToolTipText', 'MCP tooltip') # OK
ue.widget_set_property(wbp, 'MCPProbeText', 'Visibility', 'Hidden')       # OK
ue.compile_blueprint(wbp); wbp.save_package()
```

保存后回读：`Text="MCP Probe OK"`、`ToolTipText="MCP tooltip"`、`Visibility=2`（inspect 显示 `Hidden`）。

#### 附5.3 widget_slot 只支持部分属性名（实测逐项探测）

| slot_prop | 结果 |
| --- | --- |
| ZOrder | OK |
| bAutoSize | OK |
| Position | failed |
| Offsets | failed |
| LayoutData.Offsets | failed |
| Anchors | failed |
| Alignment | failed |

反射查 Slot 实际结构：`slot.get_class().get_name() == 'CanvasPanelSlot'`，`slot.LayoutData.fields() == ['Offsets','Anchors','Alignment']`（`FAnchorData`），`Offsets` 是 `FMargin`。

可用替代方案（实测生效并持久化）：

```python
w = [c for c in wbp.WidgetTree.AllWidgets if c.get_name()=='MCPProbeText'][0]
w.Slot.SetPosition(FVector2D(40, 300))
w.Slot.SetSize(FVector2D(260, 40))
ue.compile_blueprint(wbp); wbp.save_package()
# 回读: Slot: CanvasPanel (Pos: 40,300, Size: 260,40)
```

`CanvasPanelSlot` 可用 UFunction：`SetZOrder / SetSize / SetPosition / SetOffsets / SetMinimum / SetMaximum / SetLayout / SetAutoSize / SetAntiAdaptation / SetAnchors / SetAlignment` 及对应 Get。

#### 附5.4 wrap / remove 的实际语义

```python
ue.widget_wrap(wbp, 'MCPProbeText', 'SizeBox')   # OK
ue.widget_remove(wbp, 'MCPProbeText')            # OK
```

回读控件树：`MCPProbeText` 消失，但留下 `[SizeBox] MCPProbeText_Wrapper {CanvasPanel (Pos: 40,300, Size: 260,40)}`。
即 `widget_wrap` 会新建名为 `<原名>_Wrapper` 的容器并继承 Slot 布局；`widget_remove` 只删目标控件，**不会连带删除 wrapper**，清理时要显式删 wrapper。

#### 附5.5 重命名

```python
ue.objed_rename_asset('MCPTestUIProbe', 'MCPTestUIProbeRenamed', 'UI')
# -> '/IslandAuctionKing/Asset/Blueprint/Prefabs/UI/MCPTestUIProbeRenamed'
```

重命名后用**旧名**调 `resolve_asset` 仍返回新路径（AssetRegistry 保留重定向），不能靠"旧名查不到"来判定重命名成功，要核对返回的 load_path。

### 附6. 场景 Actor 写能力（未保存关卡）

```python
world = ue.get_editor_world()                       # UGCmap，实测 12 个 Actor
a = world.actor_spawn(StaticMeshActor, FVector(1200,800,300), FRotator(0,0,45))
a.set_actor_label('MCP_Probe_Cube'); a.set_folder_path('MCPTest')
a.RootComponent.RelativeScale3D = FVector(2,2,2)
a.StaticMeshComponent.SetStaticMesh(ue.load_object(StaticMesh, '/Engine/BasicShapes/Cube'))
a.actor_destroy()
```

回读结果全部符合预期：

```json
{"label":"MCP_Probe_Cube","loc":{"x":1200,"y":800,"z":300},
 "rot":{"roll":0,"pitch":0,"yaw":44.999996185302734},"scale":{"x":2,"y":2,"z":2},
 "folder":"MCPTest","mesh_set":"Cube",
 "count_with_probe":13,"count_after_destroy":12,"probe_still_present":false}
```

- `FRotator(0,0,45)` 的 yaw 回读为 `44.999996`——旋转有浮点压缩误差，校验要用容差而非等值比较。
- `get_folder_path()` 可读回 Outliner 文件夹。
- 未调用保存关卡，但 spawn/destroy 之后 `ctx:` 的 `map_dirty` 由 `false` 变 `true`，说明 Actor 增删会脏化关卡，即使已还原。

### 附7. 只读查询面补测

| 查询 | 结果 |
| --- | --- |
| `schema:AUGCPlayerController` | 未找到。提示要用精确反射名/蓝图需 `_C` 结尾全路径 |
| `subclasses:UUserWidget` | 500 个（Native 208 / Blueprint 292），截断于 200 条 |
| `enum:EUGCGameState` | 未找到（该枚举名不存在） |
| `bt:nodes attack` | 7 个节点（Task 6 / Decorator 1），UGC 自定义节点带 `*UGC` 标记 |
| `ue.objed_query_assets('UI')` | 返回**聚合字符串**（7 个 UI 资产），不是 list，禁止直接 for 迭代 |
| `ue.editor_get_active_viewport_size()` | `(1190, 923)` |
| `ue.resolve_asset(name)` | load_object 失败后的标准恢复 API，返回真实 `load_path` |

不存在的 API（实测报错）：`ue.find_package` → `module 'unreal_engine' has no attribute 'find_package'`。

### 附8. 清理与残留

已删除：

| 资产 | 方式 | 结果 |
| --- | --- | --- |
| MCPTestUIProbeRenamed（UI 副本） | `objed_delete_asset(name,'UI')` | True，resolve 为空 |
| MCPTestConfigTable | `objed_delete_asset(name,'DataTable')` | True |
| UGCTemplateRowStruct_MCPTestConfigTable | `delete_asset(path)` | 返回 None，但 resolve 为空、磁盘文件消失 |
| MCPProbeActor | `delete_asset(path)` | 返回 None，但 resolve 为空、磁盘文件消失 |
| MCP_Probe_Cube（场景 Actor） | `actor_destroy()` | 已移除 |

磁盘复核（`Asset` 下 `*MCP*` 过滤）：无任何残留 `.uasset`；`Asset/Blueprint` 与 `Asset/Data/Table/Customized` 均恢复为测试前清单。

游离包文件的处置过程（值得记录的时序）：

`duplicate_asset` 误产生的 `Asset/Blueprint/Prefabs/UI.uasset`（529 字节，创建于 11:22:36），`ue.delete_asset('/…/Prefabs/UI')` 当场返回 `None` 且磁盘文件仍在；已先备份到 `%TEMP%/MCPTest_UI_package_backup_20260826.uasset`。走完后续 `objed_delete_asset` / `delete_asset` 清理链后，最终磁盘复核该文件已消失。即删除确实发生，但**时机不可控、返回值不可信**。

最终磁盘状态复核（`Asset` 递归 `*MCP*` 过滤 + 逐目录列举）：

- `Asset/Blueprint/Prefabs/UI/` 恢复为测试前 7 个正式 UI 资产；
- `Asset/Blueprint/` 无 `MCPProbeActor`；
- `Asset/Data/Table/Customized/` 恢复为测试前 14 个资产；
- `Asset/Blueprint/Prefabs/UI.uasset` 游离文件已不存在；
- `Script/Blueprint/` 下无 `MCP*` Lua 文件（探针蓝图未生成 Lua）。

未清理项（需人工处理）：

1. 空目录 `Asset/Data/Table/Customized/Test`（内含 0 个文件，空文件夹残留）。
2. `UGCmap` 的 `map_dirty=true`（spawn/destroy 造成），关卡未保存，Actor 已还原为 12 个；建议编辑器内选择「不保存」以彻底丢弃脏标记。

### 附9. 查证来源

- UGCAskQ MCP `ue_read`：`ctx:`、`qt:`、`py:index`、`py:workflow datatable/asset_browser/property/blueprint/scene/viewport`、`py:list objed/widget_edit/struct`、`py:guide objed/widget_edit`、`py:<method>`（objed_create_asset / objed_delete_asset / objed_duplicate_asset / objed_rename_asset / objed_query_assets / data_table_add_row / data_table_modify_row / data_table_remove_row / data_table_empty_row / data_table_as_dict / struct_add_variable / struct_get_variables / struct_remove_variable / duplicate_asset / delete_asset / rename_asset / resolve_asset / create_blueprint / compile_blueprint / blueprint_add_member_variable / bp_lua_get_path / widget_add / widget_inspect / widget_set_property / widget_slot / widget_remove）、`schema:CanvasPanelSlot`、`schema:FUGCStructVariableDescription`、`subclasses:UUserWidget`、`bt:nodes attack`
- 本地社区归档 `sq-skill`：`docs/community/manifest.json` 快照 `2026-05-31T05:38:58Z`，1229 帖。以 `unreal_engine`、`MCP`、`编辑器 Python` 为关键词 `rg` 检索**无相关结果**——社区归档不覆盖 UGCAskQ MCP 主题，本页结论全部来自编辑器实测与 MCP 内置文档。
- 未调用 `ugc-log-bug-analyzer`：本轮无崩溃、无 PIE 失败、无端侧差异问题，全部异常都在 MCP 返回中直接定位。

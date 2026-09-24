# 配置表与结构体的 MCP 编辑

> 来源：[2026-08-26 UGCAskQ MCP 编辑器修改能力实测](../来源记录/2026-08-26_UGCAskQ_MCP实测记录.md)、[2026-08-26 图鉴 UI 优化](../来源记录/2026-08-26_图鉴UI优化.md)
> 规范依据：项目 `AGENTS.md` 的「按功能分类创建文件夹与配置表规范」

---

## 一、一张自定义配置表 = 两个资产

`objed_create_asset('DataTable','自定义表格','空表格',名,子目录)` 会同时生成：

| 资产 | 类型 | 作用 |
| --- | --- | --- |
| `<名>` | `DataTable` | 存行数据 |
| `UGCTemplateRowStruct_<名>` | `UserDefinedStruct` | 定义列（行结构体） |

两者同目录、成对存在。删表时若只删 DataTable，行结构体会残留（实测：`objed_delete_asset` 删表后 `resolve_asset` 仍能查到行结构体，需再用 `delete_asset` 删路径）。

`自定义表格` 的唯一模版是 `空表格`（源 `/Game/UGCEditor/UGCConfigAsset/DataTableTemplate/UGCTemplateDataTable`，create_method=Duplicate），根目录固定 `/Asset/Data/Table/Customized`。

---

## 二、空表格的默认列必须替换

新建表的行结构体默认只有一个 bool 列 `MemberVar_0_<GUID后缀>`（FriendlyName `MemberVar_0`）。按项目规范要改成 4 列字符串结构。

已验证的 4 列取值（与 `AuctionGlobalConfigTable` 完全一致）：

| VarName | FriendlyName | Category | ToolTip |
| --- | --- | --- | --- |
| ValueType | 配置类型 | string | 配置值类型：int、float、bool 或 string。 |
| Value | 配置值 | string | 运行时由 AuctionConfig 读取的具体配置值。 |
| Description | 配置说明 | string | 说明配置用途、默认值和修改注意事项。 |
| ModificationNotes | 修改注意事项 | string | 保存配置修改边界、关联依赖和生效方式。 |

---

## 三、已验证的建表流程

```python
import unreal_engine as ue
from unreal_engine.classes import DataTable, UserDefinedStruct

# 1) 建表（必须先开编辑器）
ue.objed_open_editor('DataTable')
tbl_path = ue.objed_create_asset('DataTable', '自定义表格', '空表格', 'UIConfigTable', 'UI')

# 2) 加 4 列
st = ue.load_object(UserDefinedStruct, tbl_path.rsplit('/',1)[0] + '/UGCTemplateRowStruct_UIConfigTable')
desc = ue.find_struct('UGCStructVariableDescription')
for var_name, friendly, tip in COLS:
    d = desc()
    d.set_field("VarName", var_name)
    d.set_field("FriendlyName", friendly)
    d.set_field("Category", "string")
    d.set_field("ToolTip", tip)
    st.struct_add_variable(d)              # 返回 FGuid

# 3) 删默认 bool 列（入参必须是 FGuid）
for v in st.struct_get_variables():
    if str(v.get_field("VarName")).startswith("MemberVar_0"):
        st.struct_remove_variable(v.get_field("VarGuid"))
st.save_package()

# 4) 加行
dt = ue.load_object(DataTable, tbl_path)
row = dt.data_table_empty_row()
row.set_field("ValueType", "int")
row.set_field("Value", "6")
row.set_field("Description", "角色选择界面按钮槽位数量")
row.set_field("ModificationNotes", "边界：>=1。生效：重新 PIE。")
dt.data_table_add_row("UI.CharacterSlotCount", row)     # 返回 None 也算成功
dt.save_package()

# 5) 回读验证（必做）
dt2 = ue.load_object(DataTable, tbl_path)
print(dt2.RowStruct.properties())                        # ['ValueType','Value','Description','ModificationNotes']
d = dt2.data_table_as_dict()
print(d["UI.CharacterSlotCount"].get_field("Value"))     # '6'
```

行结构体加列后，DataTable 的 `RowStruct.properties()` 会同步更新，不需要额外操作。

---

## 四、行操作对照

| 操作 | API | 返回 |
| --- | --- | --- |
| 建空行 | `dt.data_table_empty_row()` | `UScriptStruct` |
| 加行 | `dt.data_table_add_row(行名, row)` | `None`（成功也是 None） |
| 改单字段 | `dt.data_table_modify_row(行名, 字段, 值)` | `True` |
| 删行 | `dt.data_table_remove_row(行名)` | `True` |
| 读全表 | `dt.data_table_as_dict()` | `{行名: UScriptStruct}` |
| 读单行 | `dt.data_table_find_row(行名)` | 不存在时**抛异常**；入参只接受 `str`，传其他类型直接失败 |
| 读全部行结构体 | `dt.data_table_get_all_rows()` | `[UScriptStruct]`（**是行数据实例列表，不是行名**） |
| 读全部行名 | ~~`dt.data_table_get_all_rows_name()`~~ | **该方法不存在**，勿调用 |

行名支持点号分层（`UI.InfoCard.Width`、`Test.MCPWriteProbe` 实测正常），值支持中文。

### 只读批量导出模板（已实测）

需要把整表导出给网页预览或离线分析时，用 `data_table_get_all_rows()` + `as_dict()`，属纯查询，无需 PRV plan：

```python
import unreal_engine as ue, json
from unreal_engine.classes import DataTable

t = ue.load_object(DataTable, "/IslandAuctionKing/Asset/Data/Table/Customized/CollectibleTable")
rows = t.data_table_get_all_rows()
IMG = 'Imger_3_0044C0DC499330E8E35A17939926C2AC'   # 对象引用列的内部字段名带 GUID 后缀
out = []
for r in rows:
    d = r.as_dict()               # r.fields() 取字段名清单
    tex = d.get(IMG)
    out.append({'name': d.get('Name'), 'tex': tex.get_path_name() if tex else ''})
__askq_result = json.dumps(out, ensure_ascii=False)
```

**注意**：对象引用列（如贴图 `Imger`）的内部字段名是 `<FriendlyName>_<序号>_<GUID>` 形式，不能按显示名取值，必须先 `r.fields()` 打印实际字段名。

---

## 五、补充实测：空串取值、结构体备份与建表前置（2026-09-14）

### 1. 空字符串在两条读取链路上表现不同

未定项/可留空的行，`Value` 写空串后：

| 读取链路 | 表现 |
| --- | --- |
| `dt.data_table_as_dict()[行名].Value`（MCP 回读） | 返回 `''` |
| UAssetGUI `tojson` 导出的 JSON | 该字段**整个不出现**，读出来是 `None`（零值不序列化） |

所以拿 JSON 做文件级核对时，**判定空串前必须先 `v is None → ''` 归一化**，否则会把正确的空占位误报成缺失。

### 2. 加列可以直接克隆已有结构体的变量描述

比重建描述体更稳：`set_field` 在 `UGCStructVariableDescription` 上的可用性随实例化入口变化，而 `clone()` 出来的实例字段一定齐全。

```python
src = ue.find_struct('UGCTemplateRowStruct_DressConfigTable')   # 任一 4 列结构体
tpl = {v.VarName: v for v in src.struct_get_variables()}
st  = ue.find_struct('UGCTemplateRowStruct_<新表名>')
for v in list(st.struct_get_variables()):
    if str(v.VarName).startswith('MemberVar'):
        st.struct_remove_variable(v.as_dict()['VarGuid'])      # 必须传 FGuid
for key in ['ValueType', 'Value', 'Description', 'ModificationNotes']:
    st.struct_add_variable(tpl[key].clone())                   # 返回 FGuid
st.save_package()
```

`v.as_dict()['VarGuid']` 给出 `{'A','B','C','D'}` 四个 int32，用 `ue.find_struct('Guid')` 实例化后逐字段赋值即可构造入参。

### 3. 保存要区分对象方法与模块函数

- `ue.save_package` **不存在**；`dt.save_package()` / `st.save_package()` 是对象方法，返回 `True`。
- 也可以用 `ue.objed_save_asset('表名', 'DataTable')`，返回 `True`。

### 4. 批量建表时逐个开编辑器

`objed_create_asset` 前若未 `objed_open_editor('DataTable')`，报 `Cannot get asset handler for DataTable/自定义表格`。同一会话内打开一次即可，后续表可连续创建。

### 5. 子目录用第 5 参数，不要拼路径

`ue.objed_create_asset('DataTable', '自定义表格', '空表格', 'DressControlTable', 'Dress')`
→ `/IslandAuctionKing/Asset/Data/Table/Customized/Dress/DressControlTable`，行结构体同目录自动命名。

---

## 六、补充实测：给已有行结构体加字段与改显示名（2026-09-14）

场景：`DressMaterialTable` 已上线并写满数据后，需要新增一列 `TargetWidget`（目标控件名），
且新增后要与另一张表 `DressControlTable` 的值逐条对齐。

### 1. 加字段的三步：克隆同类型变量 → 改名 → 追加

```python
st  = ue.find_struct('UGCTemplateRowStruct_DressMaterialTable')
src = [v for v in st.struct_get_variables() if v.VarName == 'Value'][0]   # 同类型模板
d = src.clone()
d.VarName      = 'TargetWidget'          # 程序列名（set_field 用的键）
d.FriendlyName = '目标控件名'             # 编辑器列显示名，本项目写中文
d.ToolTip      = '<列用途说明>'
st.struct_add_variable(d)                # 追加到末尾，返回 Guid
st.save_package()
```

`clone()` 出来的描述体上 `VarName` / `FriendlyName` / `DefaultValue` / `ToolTip` 均可直接赋值，
不需要重建描述体。加字段**不影响已有行**，旧行该列取默认值（空串）。

### 2. 克隆会连带旧显示名与旧提示，必须显式覆盖

`clone()` 复制的是**整份**描述体。只改 `VarName` 不改 `FriendlyName` / `ToolTip` 时，
新列在编辑器里会显示成模板那一列的显示名和提示（实测：新列显示名是 `TargetWidget`、
提示是模板 `Value` 的「运行时由 AuctionConfig 读取的具体配置值。」）。

本项目 `FriendlyName` 约定为中文：`配置类型` / `配置值` / `配置说明` / `修改注意事项`。
新增列没有专用 setter 时只能**删掉重加**：

```python
tgt = [v for v in st.struct_get_variables() if v.VarName == 'TargetWidget'][0]
guid = tgt.VarGuid                       # Guid 结构体，不能传下标或名称
st.struct_remove_variable(guid)
# 再 clone + 改名 + struct_add_variable
```

`struct_remove_variable` 只接受 `FGuid`（传整数或字符串报 `object is not a FGuid`）。

### 3. 改单行内容：没有 update，用「删行 + 重加」

批量写入时已存在的行会被 `SKIP_EXISTS` 跳过，想改这类行的文案，只能：

```python
dt.data_table_remove_row('Dress.Material.TablePath')   # 返回 True
dt.data_table_add_row('Dress.Material.TablePath', r)   # 用新内容重加
dt.save_package()
```

### 4. 验证要点

- `struct_get_variables()` 返回的 `VarName` 顺序 = 行的字段顺序，可用来核字段是否齐全。
- 展开行后做**跨表一致性**校验：新字段的值必须与来源表逐条相等，比对脚本要把
  「缺失 / 多余 / 字段不等」三类分开计数，全零才算过。
- 更严的验收：把本地生成的期望数据整体注入沙箱，与 `data_table_as_dict()` 做
  **逐行逐字段 diff**（本次 121 行 × 5 字段，`DIFF_COUNT=0`）。
- JSON 侧校验变量数看 `StructVariableDescription` 出现次数与 `VarName` 序列，
  **不要用 `ObjectMetaDataEntry` / `DisplayName` 的条数推断变量数**（同一文件里会
  混入被引用结构体的元数据，实测 5 个变量却出现 15 条 `ObjectMetaDataEntry`）。

### 5. 字段粒度决定了要不要拆行

「每条记录绑定一个控件」这类需求（同一素材要在不同控件上互不共通），必须**按控件展开行**，
行名带上归属（`Dress.Material.<界面键>.<区域键>.<材质键>`）；只在字段里写逗号清单是无法
保证隔离的。展开前先确认哪些区域已有确定的控件名，未定的区域不建空行。

---

## 七、生效方式

配置表属于资产改动，**必须重新调试 PIE**，PIE 运行中的表改动不生效。参见 [PIE 调试与热更新边界](PIE调试与热更新边界.md)。

---

## 七·补、改单行内容存在 `data_table_modify_row`（2026-09-17 实测，与 §六.3 并存）

§六.3 记录的是「自定义表（自建 struct 行）没有 update，只能删行 + 重加」。2026-09-17 在 pet_paradise 的**官方表**上实测到另一条可用路径：

```python
dt = ue.load_object(DataTable, "/<Project>/Asset/Data/Table/UGCBattleItem.UGCBattleItem")
r = dt.data_table_modify_row("8310029", "ItemName", "打工收益卡")   # 返回 True
dt.save_package()
dt2 = ue.load_object(DataTable, TBL)                                # 重新 load 再回读
```

**适用范围（两条结论不要互相覆盖）**：

| 场景 | 可行做法 | 证据 |
|---|---|---|
| 官方表（`UGCBattleItem` / `UGCObject` / `UGCShop` 等，行结构体随引擎） | `data_table_modify_row(行名, 字段名, 新值)` 返回 `True`，随后 `save_package()` | 2026-09-17 实测 ×4 组（pet_paradise 8310029 / UGCObject 1021 / 8310034 / 8310063），均 `modify→True` 且回读一致 |
| 自建表（自定义变量结构体，如 `Dress.Material.*`） | 仍按 §六.3：`data_table_remove_row` + `data_table_add_row` | 原记录（2026-09-14） |

**注意点**：

1. `data_table_modify_row` **不在 PRV 白名单**里，`ue_plan_submit` 会给出 `apis_to_call[0] ... not in the recognized whitelist` 警告；`apis_strict` 默认 `false`，计划仍为 `plan_valid: true`，可正常执行。
2. `save_package()` 后**必须重新 `load_object`** 再回读（否则读到的是同一内存对象，无法证明持久化）。
3. **`.uasset` 字节数变化与文案长度不成正比**（UAssetAPI 会整包重序列化）。例：`UGCBattleItem` 写 3 个字段 152171→152225；`UGCObject` 把 53 字符描述换成 48 字符却 14262→14195；`UGCBattleItem` 两条 101→57 字符 152225→152049。**不要用字节数增量判断改动大小**，落盘要用「在二进制里搜新文案命中 + 搜旧文案命中 0」（UTF-8 与 UTF-16LE 双编码各搜一次；实测中文串只以 UTF-16LE 落地）。

---

## 七·补二、物品/商品描述有 60 字符上限（2026-09-17 用户下达的硬约束）

**约束**：`UGCObject.ItemDesc`、`UGCBattleItem.ItemDetails`/`PickupDetails` 等展示给玩家的物品/商品描述，**必须 ≤ 60 个字符**。

**来源与证据状态**：用户下达的项目硬约束（2026-09-17 pet_paradise 整改过程中明确提出）；非引擎报错文本，故按"用户约束"记录，适用范围 = 本项目商品/物品文案。字符按 Unicode 码点计（中文 1 字符）。

**实测数据**：

| 位置 | 文案 | 长度 | 结果 |
|---|---|---|---|
| `UGCObject.1020` 打工月卡 | 所有打工区域基础收益永久 + 20%，打工经验永久 + 30%每日可免费领取 1 次全能营养剂 | 47 | 合规（既有） |
| `UGCObject.1021` 打工季卡（改前） | 打工收益卡 1 张 + 高级托管卡 1 张；所有打工区域基础收益永久 + 50%，打工经验永久 + 60% | 53 | 合规但漏每日奖励 |
| `UGCObject.1021` 打工季卡（改后） | 打工收益卡+高级托管卡各1；收益永久+50%、经验+60%；每日送完美打工卡1张+离线托管8小时 | 48 | 合规 |
| `UGCBattleItem.8310034` / `8310063`（改前，同商品重复行） | 至尊打工区基础收益额外 + 100%，完美打工加成提升至 3 倍,解锁至尊巨型宠物专属特效与动作… | 101 | 超限 → 已收紧到 57（对齐 `UGCObject.1022` 口径） |
| `UGCBattleItem.8310068` P90冲锋枪 | 空投武器，将使用新型5.7毫米弹药… | 74 | **未处理**（官方武器行，非本玩法商品，需确认） |

**工程做法**（防止再犯）：

- 把文案上移到集中配置并加长度守卫，而不是就地硬编码：

```lua
-- SeasonCardBenefitConfig.lua
ShopDetailText = "……",           -- 与配置表同口径，≤60
MaxDetailTextLength = 60,

function SeasonCardBenefitConfig.GetShopDetailText()
    local text = SeasonCardBenefitConfig.ShopDetailText
    if type(text) ~= "string" or text == "" then
        text = "…同口径兜底文案…"
    end
    if #text > (tonumber(SeasonCardBenefitConfig.MaxDetailTextLength) or 60) then
        ugcprint(string.format("【…+GetShopDetailText】错误: 商品描述超过 %d 字符上限, 实际=%d, text=%s",
            maxLen, #text, text))
    end
    return text
end
```

- **同商品跨表必须同口径**：`UGCBattleItem` 与 `UGCObject` 里同一个商品的描述要写成完全相同的字符串，否则改一边就会出现"表里写了、商城没有"（pet_paradise 项1 的真实成因）。
- 写入前后各做一次**全表长度体检**（遍历 `ItemName`/`ItemDetails`/`PickupDetails`/`ItemDesc`/`ProductName`，打印 `len > 60` 的行），比逐条抽查更能发现既有违规。

---

## 七·补三、表结构按业务自定义列，不必死板四列（2026-09-20 实测，用户明确要求）

**原则**：`ValueType / Value / Description / ModificationNotes` 四列是**键值型配置**的通用约定（行名 → 一个值），
不是强制格式。当需求是「**一行 = 一条多字段记录**」时，应当按业务语义自定义列，**不要**把多个值挤进
`Value` 再靠分隔符解析，也不要为凑四列而牺牲可读性。

### 1. 两类表该怎么选列

| 需求形态 | 列设计 | 例子 |
|---|---|---|
| 行名 → 一个值（开关/阈值/路径/文案） | 四列 `ValueType/Value/Description/ModificationNotes` | `DressConfigTable`、`UIConfigTable` |
| 一行 = 一条记录（含分类、层级、状态等多个字段） | **按业务自定义列**，每列一个语义 | 装扮 7 张 `DressTheme<Key>Table`（各 14 列） |

### 2. 实例：装扮「每个分类一张表」

装扮 UI 的分类与主题按钮全部由表格驱动。演进过程：

1. 初版**一张** `DressThemeFolderTable`（`按键 × 主题` 笛卡尔积 7 × 6 = 42 行），
   同一份 `Folder`/`Preview`/`ThemeName` 重复 6~7 次，改一个文件夹要改 6 行 → 太难读。
2. 中间态拆成三张（`DressCategoryTable` 4 行 + `DressSubCategoryTable` 4 行 + `DressThemeTable` 6 行）→
   主题与分类解耦，但解锁状态只能按主题统一配。
3. **终态：每个分类一张表**（7 张，各 14 列）。表内每行 = 该分类下的一个可选主题，
   **解锁状态按「分类 × 主题」独立配置**，主题文件夹为分类独有。

| 表名 | UiKey | 素材基目录 | 预览素材 |
|---|---|---|---|
| `DressThemeHubTable` | Hub | `ZhuJieMian` | `ZJMBackground` |
| `DressThemeAuctioninterfaceTable` | Auctioninterface | `AuctionUI/Auctioninterface` | `AuctionUI_Background` |
| `DressThemePriceTable` | Price | `AuctionUI/Price` | `PriceInput` |
| `DressThemeSkillTable` | Skill | `AuctionUI/Skill` | `SkillPanel` |
| `DressThemeInfoTable` | Info | `AuctionUI/Info` | `InfoPanel` |
| `DressThemeSettlementTable` | Settlement | `AuctionUI/Settlement` | `SettlementPanel` |
| `DressThemeCodexTable` | Codex | `TuJian` | `Codex_BackgroundBase` |

行名 `Dress.Theme.<UiKey>.<ThemeId>`；一级/二级归属与顺序用行内
`Category`/`CategorySortOrder` 与 `SubCategory`/`SubSortOrder` 表达，**不再另设分类表**。

**拆表原则**（判断是否该拆）：两个维度**各自独立变化**时不要做笛卡尔积大表；
若「某维度的值在另一维度下各不相同」（如每个分类的主题目录/解锁状态都不同），
就按其中一个维度**一张表**，另一维度做行。判断信号：同一份值在同一列里重复出现 → 该拆。

**通用装载器写法**（一张装载函数覆盖全部同构表）：把「列名清单 + 必填列」作为参数传入，
按列名单逐列取值，再按 `SortOrder` 排序，避免每张表复制一份装载代码：

```lua
local function LoadDressCustomTable(tablePath, logTag, columns, requiredColumns)
    -- pcall(UGCGameSystem.GetTableData, path) → 遍历行 → row[col] = ToText(rowData[col])
    -- 必填列缺失 → invalidCount++ 并打日志；最后 table.sort(rows, 按 SortOrder 升序)
end
for _, entry in ipairs(AuctionConfig.DressThemeTablePaths) do   -- 7 张表结构相同
    local ok, applied, invalid, rows = LoadDressCustomTable(entry.Path, entry.Key, COLUMNS, REQUIRED)
    rowsByKey[entry.Key] = rows
end
```

**列注释要写中文**：UGC 编辑器里 `FriendlyName` 就是策划看到的列头，
务必在 `struct_add_variable` 时一起写入中文（见 §4 坑 3）。

### 3. 自定义列表**不能**走通用装载器

`LoadOneDressTable` 这类通用装载器按「行名 → `Value` 单值 → 按点号写嵌套字段」工作。
自定义列没有 `Value` 列，会被判为「配置值解析失败」（`invalidCount++`）。
必须写**专用装载函数**：`pcall(UGCGameSystem.GetTableData, path)` 后遍历行，逐列取值存成行数组。

```lua
local function ToText(v)
    if v == nil or v == 0 then return "" end   -- 表格空单元格在 Lua 侧可能是 nil 或 0
    return tostring(v)
end
-- rows[#rows+1] = { Category = ToText(rowData.Category), Folder = ToText(rowData.Folder), ... }
```

**空单元格必须 `nil / 0` 双判空**（与 §五.1 同源）：只判 `nil` 会把 `0` 变成字符串 `"0"`。

### 4. 改列流程（含两个坑）

```python
# 1) 先清空所有行（改列后旧行的值会对不上新列）
d = dt.data_table_as_dict()
for n in list(d.keys()): dt.data_table_remove_row(n)
dt.save_package()

# 2) 删旧列：struct_remove_variable 必须传 FGuid
for name in ['ValueType','Value','Description','ModificationNotes']:
    for v in st.struct_get_variables():
        if str(v.get_field('VarName')) == name:
            st.struct_remove_variable(v.get_field('VarGuid'))

# 3) 加新列（find_struct('UGCStructVariableDescription') 逐列 set_field）
# 4) st.save_package() → 重新 load_object 回读列名
```

- **坑 1：遍历中删除会漏。** 一次循环删 4 列，实测只删掉 3 列，残留一列（`ModificationNotes`）留在首位；
  **必须回读 `struct_get_variables()` 确认，漏掉的补删一次**。
- **坑 2：加列后可立即写行**，不需要重建表；`data_table_add_row` 返回 `None` 也算成功，以回读为准。
- **坑 3：列注释（FriendlyName / ToolTip）事后改不动。** `struct_get_variables()` 返回的是**副本**，
  `v.set_field('FriendlyName', ...)` 与 `v.FriendlyName = ...` 当场读是新值，
  `save_package()` 后重新 `load_object` 回读仍是旧值（2026-09-20 实测，7 张表 × 14 列全部无效）。
  **唯一可靠做法：删列 → 重加**，在建列的 `UGCStructVariableDescription` 上写入中文：

  ```python
  st.struct_remove_variable(v.get_field('VarGuid'))      # 1) 删
  dsc = desc(); dsc.set_field('VarName', c)
  dsc.set_field('FriendlyName', '素材基目录')            # 2) 加，注释在这里写
  dsc.set_field('ToolTip', '素材基目录')
  dsc.set_field('Category', 'string')
  st.struct_add_variable(dsc); st.save_package()
  ```

  代价有两个，都要收尾：① **行数据会被清空** → 重加后必须重写行；
  ② **可能残留同名重复列**（本次 7 张表各多出一个 `SortOrder`，注释仍是英文）→
  按「VarName 命中且 FriendlyName 仍为英文」筛出来补删。收尾后务必回读列名 + 列注释 + 行值三项。

- **坑 4：分清「列名 VarName」与「列注释 FriendlyName / ToolTip」，中文只能加在注释上。**
  用户说「列注释用中文」= 改 `FriendlyName`（策划在编辑器里看到的列头），**不是**改 `VarName`。

  | 字段 | 作用 | 能否中文 |
  |---|---|---|
  | `VarName` | 真正的列名，Lua 侧 `rowData[列名]` 按它取值 | **不能**，必须英文 |
  | `FriendlyName` | 编辑器列头显示名 | 可以（推荐中文） |
  | `ToolTip` | 悬停提示 | 可以（推荐中文） |

  **把 VarName 改成中文会直接踩三个雷**：① Lua 按 `rowData[columnName]` 取值全部取空 → 必填列校验失败 →
  整表装载失败、功能静默退回兜底；② 行数据按列名序列化，列名一变旧值全部丢失；
  ③ UGC 命名规则要求变量标识英文字母开头。
  改完必查：`VarName` 中文数应为 0、`FriendlyName` 中文数应为列数，并能按英文列名读回行值。

  **编辑器里看到中文列头是正常的，不等于列名被改了**：DataTable 编辑器（表格行编辑视图）的**列头显示的是
  `FriendlyName`**，所以「列注释中文化」的直接表现就是编辑器里看到中文列头（2026-09-20 实测确认）。
  想看真正的标识名，去**行结构体资产** `UGCTemplateRowStruct_<表名>` 里看，那里列的是 `VarName`（英文）。
  一句话：**编辑器给人看的是 `FriendlyName`，代码取值用的是 `VarName`**，两者互不影响。

### 5. 删除废弃表

```python
r = ue.delete_asset('/<项目>/Asset/.../DressMaterialTable')   # 返回 True，磁盘文件同步消失
```

`objed_delete_asset` 会报 `not found in any object editor`（该资产没在编辑器里打开过），**用 `delete_asset` 即可**。
删表时**行结构体 `UGCTemplateRowStruct_<表名>` 要一并删**，否则留下孤儿结构。删前先核对全工程引用数为 0。

---

## 八、相关页面

- [配置表驱动开发](../配置与数据/配置表驱动开发.md)
- [UGCAskQ MCP 能力矩阵](UGCAskQ-MCP能力矩阵.md)
- [UGCAskQ MCP 实测陷阱清单](UGCAskQ-MCP实测陷阱清单.md)
- [图鉴 UI 高保真还原](../UI与交互/图鉴UI高保真还原.md)
- 来源：[2026-08-26 图鉴 UI 优化](../来源记录/2026-08-26_图鉴UI优化.md)
- 来源：[2026-09-14 装扮系统配置表创建实测](../来源记录/2026-09-14_装扮系统配置表创建实测.md)
- 来源：[2026-09-14 装扮材质表控件字段扩展实测](../来源记录/2026-09-14_装扮材质表控件字段扩展实测.md)

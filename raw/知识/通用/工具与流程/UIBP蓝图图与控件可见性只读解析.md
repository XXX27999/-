# UIBP 蓝图图与控件可见性只读解析

- 类型：通用方法
- 主题：从 `_JsonOutput` 的 UIBP JSON 中只读解析 UMG 蓝图图（EdGraph）与控件属性（Visibility 等），用于补齐 UGCAskQ MCP 读不到 WidgetBlueprint/控件树的缺口
- 适用范围：和平精英绿洲起源（OasisEraEditor）工程内的 UMG WidgetBlueprint（`.uasset`）以及 `ExtendResource` 下官方包的 UIBP
- 证据状态：项目实测（2026-09-17，pet_paradise 工程；UAssetAPI 导出的 JSON 结构可直接解析）
- 来源：`D:\知识库\和平精英绿洲起源\备份\pet_paradise\20260917_已知缺陷第二批整改\probe_umg_nodes.py`、`probe_umg_widgets.py`、`_umg_rankingmain_widgets.txt`
- 更新时间：2026-09-17
- 关联主题：[[UAsset转JSON工具]]、[[UGCAskQ-MCP能力矩阵]]、[[UGCAskQ-MCP实测陷阱清单]]、[[2026-09-17_已知缺陷第二批整改]]
- 排除范围：不涉及 JSON 写入；不把 JSON 当作资产修改接口（写入仍必须走 UGCAskQ MCP）
- 官方依据：项目规则《蓝图与 JSON》第 2/3 条（先同步再只读、严禁用 JSON 覆盖 `.uasset`）

## 1. 为什么需要这条路径

在 pet_paradise 排查"排行榜无匿名设置"时，`UGCAskQ` MCP 的 `ue_py` 沙箱只暴露 `unreal_engine`（`ue`）模块属性：`ue.WidgetBlueprint`、`ue.EditorLevelLibrary`、`ue.EditorAssetLibrary` **均不存在**，因此：

- 读不到 UMG 控件树
- 读不到选中实例的组件/材质

但 `_JsonOutput` 下由 UAssetAPI 生成的 JSON **完整保留了 UMG 蓝图图节点与控件属性**，可以只读解析出结论。这是本页要固化的方法。

## 2. JSON 里有什么（结构事实）

以 `_JsonOutput\Asset\UI\AreaPetChoice.json`（541 个 Exports）为例：

| 内容 | 载体 | 关键字段 |
|---|---|---|
| 蓝图事件节点 | `ObjectName = "UGCK2Node_Event_N"` 的 Export | `Data[]` 里 `Name="MemberName"` 的 `Value`（如 `PreConstruct`/`Construct`/`Tick`）；`Name="EnabledState"` 的 `Value`（`ENodeEnabledState::Disabled`/`Enabled`）；`NodeComment` |
| 控件属性 | 各控件 Export（如 `Button_Set`、`TextBlock_17`、`Image_Bg_Default`） | `Name="Visibility"` 的 `Value`（`ESlateVisibility::Collapsed`/`Visible`/`SelfHitTestInvisible`/`HitTestInvisible`）；`bIsVariable`；`Text` |
| 控件树 | `WidgetTree` Export | 仅作顶层入口索引 |

**关键坑（2026-09-17 实测）**：UAssetAPI 把属性名放在 `"Name"` 字段、属性值放在 `"Value"` 字段。所以**不能**用 `{"MemberName": "PreConstruct"}` 这种字典键去匹配，必须匹配 `{"Name": "MemberName", "Value": "PreConstruct"}` 这样的键值对结构。第一版脚本按字典键匹配，结果所有节点都打印为空，属假阳性排查。

## 3. 解析脚本（可复用）

两个只读脚本，放在知识库备份目录（工程内不留脚本，遵循《调试备份存放》与 PIE 文件名规则）：

- `probe_umg_nodes.py`：列出全部 `UGCK2Node*` 节点及其 `MemberName` / `EnabledState` / `NodeComment` / 引脚默认值
- `probe_umg_widgets.py`：列出全部控件的 `Visibility` / `bIsEnabled` / `RenderOpacity` / `bIsVariable` / `Text`

核心递归收集函数：

```python
WANT = ("Visibility", "bIsEnabled", "RenderOpacity", "bIsVariable", "SlotName", "Text", "MemberName", "EnabledState")

def walk_pairs(node, out):
    """收集 (属性名, 属性值) 对：UAssetAPI 把属性名放 Name、值放 Value"""
    if isinstance(node, dict):
        nm, val = node.get("Name"), node.get("Value")
        if isinstance(nm, str) and nm in WANT and isinstance(val, (str, int, float, bool)):
            out.append((nm, val))
        for v in node.values():
            walk_pairs(v, out)
    elif isinstance(node, list):
        for it in node:
            walk_pairs(it, out)
```

调用（UTF-8 无 BOM 落盘）：

```powershell
$py = "C:\Users\Administrator\.workbuddy\binaries\python\versions\3.13.12\python.exe"
& $py "<备份目录>\probe_umg_widgets.py" `
     "<工程>\_JsonOutput\...\UGC_RankingList_Main_UIBP.json" `
     "<备份目录>\_umg_rankingmain_widgets.txt"
```

## 4. 判读规则（实测归纳）

1. **`ENodeEnabledState::Disabled` = 该事件节点不参与编译**，标准注释为"此节点被禁用，将不会被调用"。若 `PreConstruct`/`Construct`/`Tick` 三个节点全部 Disabled，可判定**该 UIBP 图内零逻辑**，行为全部在 Lua 侧 → "UI 里有隐藏自动行为"的假设可以直接排除。
2. **`Visibility = Collapsed` 且全包内无 `SetVisibility` 写入** → 该控件永久不可见。判据要"两处一起看"：
   - JSON 里的默认值；
   - 对应 Lua（`Arts_UI/UIBP/*.lua`）全包里对控件名的引用是否包含 `SetVisibility` / `Visibility` 赋值。
   只看到默认 `Collapsed` 不能立刻下结论（很多按钮是运行时显隐的）；只有"默认 Collapsed + 无任何置可见代码"才是缺陷。
3. 同名控件可能出现**多个实例**（如 `Button_Set` 出现在 Export `[8]` 与 `[14]`），必须逐个看，不能只看第一个。
4. 对照同包内**已正确工作**的同类控件（如 `Button_Cancel` 在 Lua 里是显式 `SetVisibility` 的）可以快速区分"漏配"与"设计如此"。

## 5. 与 UGCAskQ MCP 的分工

| 任务 | 首选 | 兜底 |
|---|---|---|
| 改蓝图/UI 属性 | UGCAskQ MCP（Resolve → Plan → Execute） | 无（JSON 禁止写入） |
| 读 UMG 图逻辑与控件可见性 | 本页方法（先同步 `_JsonOutput`） | 编辑器内目视 |
| 读 DataTable | UGCAskQ MCP `ue_py` + `data_table_as_dict()` | 同步后的 JSON |

**约束不变**：JSON 只用于只读核查、字段补充与差异定位；严禁直接编辑 JSON、用 JSON 覆盖 `.uasset`，或据此声称已修改编辑器蓝图。

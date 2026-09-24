# 蓝图与 MCP 写入流程

> 来源：`raw/docs/ai/2026-07-13_RPC编码规范标准文档.md`（第 9 章）、`raw/docs/ai/2026-07-15_打工区3DUI挂载与显示距离修复.md`、`raw/docs/ai/2026-08-03_GM私有实体碰撞血条伤害隔离.md`、`raw/docs/ai/3D_UI_MOUNTING_GUIDE.md`、本次会话（2026-08-28、2026-09-14）用户指令、本次会话（2026-09-16）用户指令「同步工具与 `_JsonOutput` 迁出 UGC 工程，后续统一从知识库调用」
> 官方依据：`raw/docs/wiki/绿洲编辑器基础内容/20414_UGCAskQ MCP 使用说明.md`
> 主题：蓝图 / UI / UGCAskQ MCP / JSON 同步
> 适用范围：绿洲编辑器通用流程；`ConvertUAssetToJson.ps1` 的同步语义已封装为 [UAsset 转 JSON 工具](./UAsset转JSON工具.md)，其行为以原件 + 2026-09-16 实测为证据
> 证据状态：官方 MCP 规则 + 项目脚本核验 + 2026-09-16 工具实测
> 更新时间：2026-09-16
> 关联主题：UGCAskQ MCP 能力矩阵、PIE 调试与热更新边界、UAsset 转 JSON 工具、非运行辅助文件索引与调用
> 排除范围：直接编辑 `_JsonOutput` JSON 修改蓝图、未回读的写入结果

---

## 一、蓝图事件机制

蓝图没有事件图表，**所有事件默认启用，只通过对应函数名/调用触发**。因此 Lua 侧函数名与蓝图约定必须严格一致，改名等于断开事件。

---

## 二、读写职责划分

| 操作 | 方式 |
| --- | --- |
| 读取蓝图 / UI 属性 | 优先 UGCAskQ MCP；MCP 未查询到时，先同步再看只读的 `_JsonOutput` JSON 作补充 |
| 修改蓝图结构、组件、UI 属性、数据表 | 必须用 UGCAskQ MCP |
| `_JsonOutput` | 只用于只读核查、字段补充和差异定位；JSON 不一定是蓝图最新内容，禁止直接编辑或回写 `.uasset` |

---

### 2.1 JSON 只读补充与蓝图数据同步

当 UGCAskQ MCP 未查询到目标蓝图、控件或属性时，JSON 只能作为补充核查来源，不能作为蓝图写入接口。由于 `_JsonOutput` 可能滞后于编辑器中的 `.uasset`，读取前必须先同步。同步工具已迁出 UGC 工程，统一从知识库调用：

```powershell
# 图形界面：双击，或
Start-Process 'D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe'

# 命令行增量转换（--windowed exe 不回显 stdout，用 --report 落盘再读）
$EXE = 'D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe'
Start-Process -FilePath $EXE -ArgumentList @('--mode','convert','--report',"$env:TEMP\convert.json") -Wait -PassThru

# 持续监视资产变化（每 2 秒轮询）
Start-Process -FilePath $EXE -ArgumentList @('--mode','watch')
```

该工具有两种运行模式：

1. `1` / `--mode convert`：`Full Conversion (Incremental)`，转换所有发生变化的资产，并清理源已删除的孤儿 JSON。
2. `2` / `--mode watch`：`Auto Watch Mode`，持续监视资产变化并转换。

默认输出根为 `D:\知识库\和平精英绿洲起源\raw\<项目名>\_JsonOutput\`，**不再写回 UGC 工程**。若某工程仍保留自己的同步脚本，也可在项目根目录执行该脚本；两者语义一致，细节见 [UAsset 转 JSON 工具](./UAsset转JSON工具.md)。

同步脚本不存在、`UAssetGUI.exe` 缺失、转换失败或项目版本不匹配时，必须记录失败原因并停止使用旧 JSON 作确定性依据。JSON 只能用于字段补充和差异定位；蓝图结构、组件、UI 属性、事件入口和资源引用的实际修改必须回到 UGCAskQ MCP 的 `Resolve → Plan → Execute` 流程。

## 三、三段式写入流程

### 3.0 创建文件存放门槛

网页预览、Python 辅助脚本、Markdown/报告、截图及其他与地图运行无关的文件，默认只写入知识库 `备份/<ProjectName>/<YYYYMMDD>_<Theme>/` 或 `raw/知识/通用/`，不得进入 UGC 工程。蓝图、Lua 脚本和项目运行所需的导入资产属于项目运行文件，按本流程和对应项目目录处理。

仅生成非运行文件时，不执行项目导入或 MCP `Execute`。涉及蓝图、Lua 或运行资产部署时，继续执行下列 `Resolve → Plan → Execute` 流程，并完成写前备份、写后 MCP 回读和必要的 PIE 验证。

```
Resolve → Plan → Execute
```

1. **Resolve**：查 API 与工作流（`ue_read` 查 `py:workflow <domain>` / `py:<api>` / `schema:<Class>`），确认属性名、类型、枚举取值。
2. **Plan**：提交 PRV 计划（`intent`、`asset_path`、`mutations` 或 `scene_ops`、`apis_to_call`），拿到 `plan_id`。
3. **Execute**：带 `plan_id` 执行写入，服务端自动校验。

配套硬性要求：

- 写前**备份到知识库备份目录并通知用户**：D:\知识库\和平精英绿洲起源\备份\<ProjectName>\<YYYYMMDD>_<Theme>\。禁止写入 UGC 工程 Backup/；与地图运行无关的文件不得落入 UGC 工程。
- 资产路径用绝对形式 `/<ProjectName>/...`，不用 `/Game/`。
- 写后**立即回读验证**表结构、行名、类型、值或组件属性。
- 纯查询代码不需要计划；带 EditCondition 的 CDO 写入需要「开门 → 写值 → 保存 → 校验」两阶段。

### 3.1 改已有 Lua/文本工程文件：用精确串替换补丁脚本（要求幂等）

改 `Script/**.lua` 这类纯文本工程文件时，逐处手改容易漏且无法复核。改用 Python 补丁脚本，一次跑完并自证：

```python
PATCHES = [  # (键名, 幂等标记, old, new)
    ("A_helper", "只存在于新代码里的标识串", OLD, NEW),
]
for key, mark, old, new in PATCHES:
    if mark in text:            # 重跑安全：已打过就跳过
        print("SKIP", key); continue
    cnt = text.count(old)
    assert cnt == 1, "锚点 %s 命中 %d != 1，中止" % (key, cnt)   # 防止改错位置
    text = text.replace(old, new, 1)
# 写回后必须从磁盘重读复核 + 断言各标记出现次数
```

硬性要求：

1. **每项配一个只存在于新代码里的标识串作幂等标记**，否则重跑会重复插入。
   ⚠️ **2026-09-17 实测新坑**：标记串"只在新代码里"还不够，**还不能被同一批次的其他补丁包含**。
   反例：D 项标记 `"RPC_SetSeasonCardFeetOffset"`，而 B 项新增的
   `CallUnrealRPC(..., "RPC_SetSeasonCardFeetOffset", ...)` 也含该串；A→B→C→D 顺序执行时 B 先落盘，
   D 就被判成"已打过"而 `SKIP`，函数定义实际没写入（日志显示 `SKIP D (already patched)`，但磁盘上无该函数）。
   ⇒ 标记应尽量用**函数签名**这类唯一形态（`function Pet:RPC_SetSeasonCardFeetOffset(`），
   且必要时对"补跑某一项"单独写一个补丁脚本。
2. **锚点命中数必须断言为 1**，命中 0 或 >1 一律中止，不要靠 `replace` 的宽松匹配。
3. **写回后从磁盘重读复核**，统计各标记出现次数与期望值比对；只看"编辑成功"的返回不算验证。
4. 采用**追加式**改动（在函数末尾追加、在某行后插入）时风险最高——old 串被 new 串包含就会反复插入，
   实测曾把同一函数插成 3 份，只能靠备份恢复重做。
5. 收尾跑 `luaparser` AST 解析做语法验收，并检查**无 BOM**、以及文件级 `local` 的**声明顺序**
   （`local function` 必须在调用者之前定义，否则被解析成全局 nil，运行期才报 `attempt to call a nil value`）。
6. 补丁脚本一律放知识库 `备份/<ProjectName>/<YYYYMMDD>_<主题>/`，**禁止留在 UGC 工程内**；
   收尾扫描工程内不得有 `.py` / `__pycache__`。

---

## 四、MCP 覆盖的编辑器能力

官方说明列出的支持范围：场景与 Actor 管理、技能编辑器、物品编辑器、行为树、蓝图编辑器、UI 编辑器（UMG）、数据表、实体编辑器、资产查找与视窗控制。典型用法为批量内容生成、技能原型迭代、配置核查与批量修改、UI 布局辅助、行为树搭建。

---

## 四·补、实测校准（2026-08-26）

在 IslandAuctionKing 上逐项跑通后的校正点：

- **PRV 当前是 observe 等级**：无 plan 执行写入只返回 `warn_pass` 加告警，不拦截。规范要求提交 plan 靠自律，不能指望服务端兜底。
- **mutation 判定基于代码文本**：出现 `setattr` / `save_package` / `actor_spawn` 即判为写入，与实际写入目标无关。
- **plan_id 可复用**：TTL 默认 900 秒，同一 plan_id 跨多次 `ue_py` 有效（实测复用 10 次），`used_count` 递增。
- **事务可回滚**：传 `transaction_name` 后中途异常会整段回滚，返回 `No changes were made.`，实测无残留。
- **objed 系列有前置条件**：必须先 `objed_open_editor(<类型>)`，否则报 `Cannot get asset handler`。
- **UI/物编资产复制不能用 `duplicate_asset`**：会生成删不掉的游离包对象，必须用 `objed_duplicate_asset`。
- **回读是唯一判据**：`data_table_add_row` / `delete_asset` / `widget_*` 成功时都返回 `None`。

完整清单见 [UGCAskQ MCP 能力矩阵](UGCAskQ-MCP能力矩阵.md) 与 [UGCAskQ MCP 实测陷阱清单](UGCAskQ-MCP实测陷阱清单.md)。

---

## 五、Lua 与蓝图的联动检查

- 每次改 Lua 后确认 `_JsonOutput` 同名 JSON 是否需要同步。若本次只改运行时逻辑，没有新增蓝图暴露变量、组件引用或事件入口，则无需同步（跳楼机记录的实际判断）。若涉及蓝图数据核查，先运行 `ConvertUAssetToJson.ps1`，再只读查看同步后的 JSON。
- 打工区实战中，UMG 布局改动由 MCP 落盘，并要求旧标记物脚本禁用 SuperClass 以避免蓝图图二次挂载。
- 私有血条一类属性不能改蓝图 CDO 全局关闭，需按实例设置，见 [端侧权威与 HasAuthority](../程序与网络/端侧权威与HasAuthority.md)。

---

## 六、证据边界

蓝图 CDO 回读成功只证明写入落盘，不证明运行行为正确；`_JsonOutput` 在部分工程中可能不存在或不是蓝图最新内容。需要文件级对照时，先用 [UAsset 转 JSON 工具](./UAsset转JSON工具.md) 同步，再把 JSON 作为只读补充；不能直接编辑 JSON 或用 JSON 覆盖 `.uasset`。最终仍需依赖 MCP 回读与 PIE 日志验证运行行为。见 [PIE 调试与热更新边界](PIE调试与热更新边界.md)。

---

## 七、相关页面

- [配置表驱动开发](../配置与数据/配置表驱动开发.md)
- [资源导入与路径规范](../配置与数据/资源导入与路径规范.md)
- [3D UI 挂载方案](../程序与网络/3DUI挂载方案.md)
- [PIE 调试与热更新边界](PIE调试与热更新边界.md)
- [UGCAskQ MCP 能力矩阵](UGCAskQ-MCP能力矩阵.md)
- [UGCAskQ MCP 实测陷阱清单](UGCAskQ-MCP实测陷阱清单.md)
- [配置表与结构体的 MCP 编辑](配置表与结构体的MCP编辑.md)
- [绿洲编辑器提示词优化](绿洲编辑器提示词优化.md)
- [绿洲蓝图变量与玩家数据存储](../程序与网络/绿洲蓝图变量与玩家数据存储.md)
- 来源：[官方 API 与 Wiki 文档结构](../来源记录/官方API与Wiki文档结构.md)、[2026-08-26 raw 资料入库总结](../来源记录/2026-08-26_raw资料入库总结.md)、[2026-08-26 UGCAskQ MCP 实测记录](../来源记录/2026-08-26_UGCAskQ_MCP实测记录.md)、[2026-08-28 蓝图数据同步与 JSON 只读补充](../来源记录/2026-08-28_蓝图数据同步与JSON只读补充.md)

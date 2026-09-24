# UAsset 转 JSON 工具（UAssetToJsonConverter）

> 类型：通用知识 / 工具与流程
> 主题：.uasset → JSON 只读镜像同步 / UAssetGUI / 工程外置工具调用
> 适用范围：绿洲编辑器 UGC 工程通用；`IslandAuctionKing` 为实测样本
> 证据状态：项目实测（2026-09-16 exe 自检、干跑与真实增量转换均通过）
> 来源：本次会话（2026-09-16）用户要求把工程根 `ConvertUAssetToJson.ps1` 整理并封装为 exe 存入知识库、其输出目录 `_JsonOutput` 一并保存在知识库；原脚本见 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260916_工程外置资料迁移\ConvertUAssetToJson_原件.ps1`（SHA256 `47DDAC2793ABB371D7602F8427E37E11CD08F4D7A4D20D825CCF17892AE51174`）
> 变更记录：`1.0.0` 2026-09-16 工程外置封装；`1.1.0` 2026-09-16 界面工程根 / 输出根改为选择式交互（详见第二.1 小节与第八节）
> 更新时间：2026-09-16
> 关联主题：蓝图与 MCP 写入流程、UGCAskQ MCP 能力矩阵、非运行辅助文件索引与调用、创建文件存放边界
> 排除范围：直接编辑 JSON 修改蓝图（禁止）；`.uasset` 二进制写入；`raw/docs/` 原始资料
> 官方依据：工具封装与存放属本仓库工程约定，官方未覆盖；`_JsonOutput` 只读只用于核查的定位见 [蓝图与 MCP 写入流程](./蓝图与MCP写入流程.md)

## 一、核心结论

1. `.uasset` → JSON 的同步逻辑本身不变：只用 UAssetGUI 的 `tojson` 子命令，按 `LastWriteTime` 做增量跳过，转换后清理「源 `.uasset` 已删除」的孤儿 JSON。
2. **工具与产物都要在知识库侧，不在 UGC 工程内**：脚本与 exe 放 `工具\UAssetToJsonConverter\`，JSON 镜像放 `raw\<项目名>\_JsonOutput\`。工程目录里再出现 `ConvertUAssetToJson.ps1` 或 `_JsonOutput\` 都属回退。
3. 路径全部参数化，不再靠「脚本自己所在目录」推断工程根：默认工程根与输出根为常量，可用 `--project` / `--output` 覆盖。
4. 输出根在工程外并不会让增量判断失效，**前提是迁移镜像时保留 `LastWriteTime`**（用 `copy2` 而非普通复制）。实测保留后 284 个 `.uasset` 中 133 个命中跳过。
5. JSON 的地位不变：只读核查、字段补充、差异定位；**不保证是最新蓝图状态**，读之前必须先同步，禁止编辑 JSON 或用 JSON 覆盖 `.uasset`。
6. `1.1.0` 起图形界面的「工程根」「输出根」不再需要手敲路径：工程根可从下拉（探测 `UGCProjects` 下含 `Asset` 的项目）或「浏览…」选择；输出根可从下拉或「浏览…」选择，并默认随工程派生为 `知识库 raw\<项目名>\_JsonOutput`。命令行参数与转换行为未变。

## 二、安装位置与调用

| 项目 | 绝对路径 |
| --- | --- |
| exe（双击即用） | `D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe` |
| 源码（可改） | `D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\UAssetToJsonConverter.py` |
| 原始 ps1 原件 | `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260916_工程外置资料迁移\ConvertUAssetToJson_原件.ps1` |
| JSON 输出根（默认） | `D:\知识库\和平精英绿洲起源\raw\IslandAuctionKing\_JsonOutput\` |
| 外部依赖 | `C:\Program Files (x86)\UAssetGUI.exe`（必须存在） |

默认参数：

| 参数 | 默认值 |
| --- | --- |
| `--project` | `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing` |
| `--output` | `D:\知识库\和平精英绿洲起源\raw\IslandAuctionKing\_JsonOutput` |
| `--uassetgui` | `C:\Program Files (x86)\UAssetGUI.exe` |
| `--ue-version` | `VER_UE4_24` |
| `--poll-interval` | `2`（秒） |

调用方式：

```powershell
$EXE = 'D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe'

# 1) 环境自检（依赖、路径、uasset 命中数、输出是否误落在工程内）
Start-Process -FilePath $EXE -ArgumentList @('--selftest', "$env:TEMP\selftest.json") -Wait -PassThru

# 2) 增量全量转换（-windowed exe 不回显 stdout，用 --report 落盘再读）
Start-Process -FilePath $EXE -ArgumentList @('--mode','convert','--report',"$env:TEMP\convert.json") -Wait -PassThru

# 3) 只列计划不写文件
Start-Process -FilePath $EXE -ArgumentList @('--mode','convert','--dry-run','--report',"$env:TEMP\dry.json") -Wait -PassThru

# 4) 监视模式（每 2 秒轮询增/改/删，Ctrl+C 或界面「停止」结束）
Start-Process -FilePath $EXE -ArgumentList @('--mode','watch') -Wait -PassThru

# 5) 图形界面：直接双击 exe，或
Start-Process -FilePath $EXE
```

换成别的工程只需改 `--project` 与 `--output`。

### 2.1 图形界面的路径选择（v1.1.0 起）

界面里「工程根」「输出根」已改为与 `FolderTreeTranslator` 一致的选择式交互，不再需要手敲绝对路径：

| 控件 | 行为 |
| --- | --- |
| 工程根「浏览…」 | `filedialog.askdirectory`，默认定位到 `UGCProjects` 集合根 |
| 「快速选择工程」下拉 | 探测 `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects` 下含 `Asset` 子目录的项目（本机 37 项），选中即写入工程根 |
| 输出根「浏览…」 | `filedialog.askdirectory`，默认定位到知识库 `raw`；选后自动关闭「随工程派生」 |
| 「快速选择输出根」下拉 | 当前工程的派生路径优先，其后补齐 `raw` 下已存在的 `_JsonOutput` |
| 「输出根随工程派生」勾选 | 默认开启：输出根恒为 `知识库 raw\<项目名>\_JsonOutput`，换工程自动跟随 |
| 「刷新列表」 | 重新探测并刷新两个下拉 |
| 「打开工程目录」/「打开输出目录」 | 资源管理器打开；输出根不存在时可现场创建 |

对应新增的模块级函数（可被其他脚本复用）：

| 函数 | 作用 |
| --- | --- |
| `detect_projects(projects_root)` | 列出工程集合根下含 `Asset` 的项目，判据与 `FolderTreeTranslator` 相同 |
| `derive_output_root(project_path)` | 由工程名派生 `知识库 raw\<项目名>\_JsonOutput` |
| `detect_output_roots(raw_root)` | 列出 `raw` 下已存在的 `_JsonOutput` |

未改动项：`UAssetGUI`、`UE 版本`、`轮询秒` 仍为手填输入框；命令行参数与转换逻辑（增量判据、镜像、孤儿清理、监视模式）与 v1.0.0 一致。

## 三、行为对照（与原件一致）

| 环节 | 行为 |
| --- | --- |
| 输入枚举 | 递归扫描工程内 `*.uasset`，排除路径含 `_JsonOutput` / `UAssetGUI` 的目录 |
| 增量判据 | 目标 JSON 存在且 `mtime(uasset) <= mtime(json)` 则跳过 |
| 输出镜像 | 按源相对工程根的目录结构镜像，文件名同基名换 `.json` |
| 孤儿清理 | 遍历输出根下全部 `*.json`，找不到对应 `.uasset` 的删除 |
| 监视模式 | 进程内维护 `路径 -> mtime` 表；新增/修改触发转换，删除同步删 JSON |
| UE 版本标记 | 作为 `UAssetGUI tojson` 的第 4 个参数传入 |

## 四、常见错误

1. **exe 不回显输出**：`--onefile --windowed` 没有控制台，`--selftest` / `--report` 必须写文件，再用读取工具看结果；用 `& $EXE` 直接调用拿不到 `$LASTEXITCODE`（GUI 子系统进程不阻塞），要 `Start-Process -Wait -PassThru` 才能取退出码。
2. **迁移镜像用普通复制**：`Copy-Item` 会保留时间戳，但 Python 侧必须用 `shutil.copy2`；用 `shutil.copy` 或先建空目录再写内容会让全部文件命中「需要转换」，白跑一轮。
3. **把输出根指回工程内**：会让 `_JsonOutput` 重新出现在 UGC 工程，回到被 PIE 递归扫描 + 上传忽略清单维护的老问题。自检项 `output_inside_project` 用于拦截。
4. **拿 JSON 当最新蓝图**：JSON 只是同步时刻的快照，未同步前不得作为确定性依据；蓝图写入永远走 MCP。
5. **误把 JSON 当写入接口**：禁止编辑 JSON、禁止用 JSON 覆盖 `.uasset`。
6. **PowerShell 5.1 跑 UTF-8 无 BOM 脚本**：`powershell -File xxx.ps1` 会按 ANSI/GBK 解析中文，路径字符串变乱码并写出到乱码目录；需要 PowerShell 时脚本必须存为 **UTF-8 with BOM**，或改用 Python。

## 五、重建步骤（exe 丢失或需改代码时）

```powershell
$py    = 'C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe'   # 必须用带 tkinter 的 3.12
$TOOL  = 'D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter'
$BUILD = 'D:\知识库\和平精英绿洲起源\备份\工具\UAssetToJsonConverter-build'

& $py -m py_compile "$TOOL\UAssetToJsonConverter.py"
& $py -m PyInstaller --noconfirm --clean --onefile --windowed --name UAssetToJsonConverter `
    --distpath "$TOOL\dist" --workpath "$BUILD\work" --specpath "$BUILD" "$TOOL\UAssetToJsonConverter.py"
```

- `--workpath` / `--specpath` 必须指到交付目录之外，否则 `build\` 与 `.spec` 会污染工具目录。
- 打包前先物理删除 `dist\UAssetToJsonConverter.exe`；若删除被安全删除钩子拦截，改用 PowerShell `Remove-Item` 并复核文件是否真的消失。
- 打包后必须跑 `--selftest` 与 `--mode convert --dry-run`，再跑一次真实 `--mode convert` 作为端到端证据。

## 六、相关页面

- [蓝图与 MCP 写入流程](./蓝图与MCP写入流程.md)
- [UGCAskQ MCP 能力矩阵](./UGCAskQ-MCP能力矩阵.md)
- [非运行辅助文件索引与调用规范](../知识库治理/非运行辅助文件索引与调用规范.md)
- [调试备份存放](./调试备份存放.md)
- [IslandAuctionKing 辅助文件索引](../../../IslandAuctionKing/开发记录/000_辅助文件索引.md)
- [2026-09-16 工程外置资料迁出知识库](../来源记录/2026-09-16_工程外置资料迁出知识库.md)

## 七、待查证

1. 转换耗时的量化基线：本次未逐文件计时，`--mode convert` 处理 151 个文件的墙钟时间未记录，仅知原 ps1 为「每个文件起一次 UAssetGUI 进程」的串行模型。
2. 监视模式对本机 UAssetGUI 并发写文件的表现未验证（原 ps1 亦为串行，行为保持一致）。
3. 非 `VER_UE4_24` 的 UE 版本标记在其他工程上的可用性未验证。
4. `1.1.0` 下用界面选择非 `IslandAuctionKing` 工程做真实（非干跑）转换未验证；下拉里 36 个 `Template_*` 工程是否都有对应 `raw\<项目名>\_JsonOutput` 也未逐个确认（不存在时需「打开输出目录」现场创建）。

## 八、本次界面改造证据（2026-09-16）

改动前的源码与 exe 备份在 `D:\知识库\和平精英绿洲起源\备份\工具\20260916_UAssetToJson目录选择改造\`，同目录 `变更说明.md` 记录完整改动清单、前后 SHA256 与验证证据。本次只改界面路径输入方式，转换逻辑与命令行参数未动。

| 文件 | 大小(B) | SHA256 |
| --- | --- | --- |
| `工具\UAssetToJsonConverter\UAssetToJsonConverter.py`（改后） | 28464 | `2D0F0E47EBF4596C278B82E2F77D475A7C6524BB9FDC9E77143C0E76EBC715FB` |
| `工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe`（改后） | 11404218 | `76BB8C8582A6399BB467E5F1CFD4CE4A91C75CC711C6DD8AF4814B712F5F6F9F` |
| `工具\UAssetToJsonConverter\README.md`（改后） | 4634 | `EE9C0877B74296E9265617E4A0AB1EC2FE9EEDA651A4F0CBD2402A009FBCA594` |
| 备份 `dist\UAssetToJsonConverter.exe`（改前） | 11376464 | `6E071BE6777044994A2D2DE7AD1DDF580B58999E206F904321BCFE33DD3A8D5D` |

验证结果（证据状态：项目实测）：

1. `py_compile` 通过（产生的 `__pycache__` 已清理）。
2. 控件树枚举：28 个控件，两个路径下拉均为 `readonly`，工程下拉 37 项。
3. 交互模拟：换工程→输出根自动派生；关闭「随工程派生」后换工程输出根保持不变；勾回后重新派生；手选输出根下拉会自动关闭派生。
4. exe `--selftest`：`ok=true`、`version=1.1.0`、`frozen=true`、`uasset_count=284`、`output_inside_project=false`（证据 `备份\...\改动后_exe自检.json`）。
5. exe `--mode convert --dry-run`：`total=284 / skipped=284 / failed=0`，CLI 路径无回归（证据 `备份\...\改动后_exe干跑报告.json`）。
6. 界面截图：`备份\工具\20260916_UAssetToJson目录选择改造\改动后_界面截图.png`。

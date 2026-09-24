# UAssetToJsonConverter —— UAsset 转 JSON 同步工具

把绿洲编辑器 UGC 工程内的 `.uasset` 增量导出为只读 JSON 镜像，供 UGCAskQ MCP 未命中时做只读核查、字段补充与差异定位。

本工具由 `IslandAuctionKing` 工程根 `ConvertUAssetToJson.ps1` 整理并移植而来，**已迁出 UGC 工程**，统一从知识库调用；输出目录也不再写回工程内，避免编辑器递归扫描工程目录。

当前版本 `1.1.0`：`1.0.0` 为工程外置封装；`1.1.0` 把界面「工程根」「输出根」从手填改为下拉 + 浏览选择，输出根默认随工程派生为 `知识库 raw\<项目名>\_JsonOutput`（见下方「界面」小节）。转换逻辑与命令行参数未变。

## 目录内容

| 文件 | 说明 |
| --- | --- |
| `UAssetToJsonConverter.py` | 源码（命令行 + tkinter 界面） |
| `dist\UAssetToJsonConverter.exe` | 单文件 exe，双击即用 |
| `示例输出\` | 真实运行样本（自检 / 干跑 / 转换报告） |

原始 ps1 原件留档在 `D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260916_工程外置资料迁移\ConvertUAssetToJson_原件.ps1`。

## 默认参数

| 参数 | 默认值 |
| --- | --- |
| `--project` | `D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\UGCProjects\IslandAuctionKing` |
| `--output` | `D:\知识库\和平精英绿洲起源\raw\IslandAuctionKing\_JsonOutput` |
| `--uassetgui` | `C:\Program Files (x86)\UAssetGUI.exe` |
| `--ue-version` | `VER_UE4_24` |
| `--poll-interval` | `2` 秒 |

## 用法

```powershell
$EXE = 'D:\知识库\和平精英绿洲起源\工具\UAssetToJsonConverter\dist\UAssetToJsonConverter.exe'

# 图形界面
Start-Process $EXE

# 环境自检
Start-Process -FilePath $EXE -ArgumentList @('--selftest', "$env:TEMP\selftest.json") -Wait -PassThru

# 增量全量转换（--windowed exe 不回显 stdout，用 --report 落盘再读）
Start-Process -FilePath $EXE -ArgumentList @('--mode','convert','--report',"$env:TEMP\convert.json") -Wait -PassThru

# 只列计划
Start-Process -FilePath $EXE -ArgumentList @('--mode','convert','--dry-run','--report',"$env:TEMP\dry.json") -Wait -PassThru

# 监视模式（每 2 秒轮询增/改/删）
Start-Process -FilePath $EXE -ArgumentList @('--mode','watch')
```

## 界面（v1.1.0 起）

「工程根」「输出根」不再需要手敲，与 `FolderTreeTranslator` 一致：

| 控件 | 行为 |
| --- | --- |
| 工程根 `浏览…` | 打开目录选择框，默认定位到 `UGCProjects` 集合根 |
| 快速选择工程（下拉） | 自动列出 `UGCProjects` 下含 `Asset` 子目录的项目；选中即写入工程根 |
| 输出根 `浏览…` | 打开目录选择框，默认定位到知识库 `raw`；选后自动关闭「随工程派生」 |
| 快速选择输出根（下拉） | 列出当前工程的派生路径 + `raw` 下已存在的 `_JsonOutput` |
| 输出根随工程派生（勾选框，默认开启） | 开启时输出根恒为 `知识库 raw\<项目名>\_JsonOutput`，换工程自动跟随；标签文案随状态显示「（已开启）/（已关闭）」 |
| 打开工程目录 / 打开输出目录 | 资源管理器中打开；输出根不存在时可现场创建 |
| 刷新列表 | 重新探测工程集合根与 `raw`，刷新两个下拉 |

`UAssetGUI`、`UE 版本`、`轮询秒` 仍为手填输入框；命令行参数与转换逻辑未变。

## 行为

1. 递归扫描工程内 `*.uasset`，排除路径含 `_JsonOutput` / `UAssetGUI` 的目录。
2. 目标 JSON 存在且 `mtime(uasset) <= mtime(json)` 时跳过（增量）。
3. 输出按源相对工程根的目录结构镜像到 `--output`。
4. 转换后清理输出根下「源 `.uasset` 已删除」的孤儿 JSON。
5. 监视模式内存维护 `路径 -> mtime`，检测增/改/删并同步。

## 约束

- 依赖 `C:\Program Files (x86)\UAssetGUI.exe` 存在，否则自检 `ok=false`、退出码 3。
- 迁移或重建镜像目录时必须保留 `LastWriteTime`（`copy2` 一类），否则增量跳过全部失效。
- JSON 只读：不保证最新，禁止编辑、禁止覆盖 `.uasset`；蓝图/UI/DataTable 写入只能走 UGCAskQ MCP。
- 重建 exe 见 [UAsset 转 JSON 工具](D:\知识库\和平精英绿洲起源\raw\知识\通用\工具与流程\UAsset转JSON工具.md) 第五节。

## 登记

- 工具登记项：`AUX-20260916-005` / 产物 `AUX-20260916-006`，见 `D:\知识库\和平精英绿洲起源\raw\IslandAuctionKing\开发记录\000_辅助文件索引.md`
- 通用说明：`D:\知识库\和平精英绿洲起源\raw\知识\通用\工具与流程\UAsset转JSON工具.md`

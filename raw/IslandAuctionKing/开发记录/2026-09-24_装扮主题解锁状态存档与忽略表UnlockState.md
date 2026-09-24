- 类型：功能实现 / 修改记录
- 主题：装扮主题解锁状态改为玩家跨局存档数据，并停止依赖主题表 `UnlockState` 列
- 适用范围：IslandAuctionKing 玩家控制器、玩家存档服务、客户端私有状态分发与装扮界面（`Script/Blueprint/UGCPlayerController.lua`、`Script/Function/AuctionPlayerService.lua`、`Script/Blueprint/CF_FWDRPC.lua`、`Script/Function/AuctionDressUIService.lua`、`Script/Function/AuctionConfig.lua`）
- 项目索引：[IslandAuctionKing 项目资料索引](../000_项目索引.md)
- 证据状态：蓝图属性写入与回读为**项目实测**；Lua 静态校验、服务端/客户端日志与存档落盘为**项目实测**；非空解锁集合的跨局往返**尚未验证**
- 来源：工程内 5 个 Lua 文件与 `Asset/Blueprint/UGCPlayerController.uasset`（改后差异）；官方 `D:\oasis-skill-plus\docs\api\class\和平全局接口\角色系统\UGCPlayerStateSystem.md`；知识库 [存档与数据持久化](../../知识/通用/程序与网络/存档与数据持久化.md)、[绿洲蓝图变量与玩家数据存储](../../知识/通用/程序与网络/绿洲蓝图变量与玩家数据存储.md)
- 更新时间：2026-09-24
- 关联主题：[2026-09-20_装扮主题文件夹表与装扮UI改造](../配置表/2026-09-20_装扮主题文件夹表与装扮UI改造.md)、[2026-09-18_装扮主题索引与素材目录迁移](../配置表/2026-09-18_装扮主题索引与素材目录迁移.md)、[2026-09-16_选择与道具组数据持久化与滑动框定位](./2026-09-16_选择与道具组数据持久化与滑动框定位.md)
- 排除范围：不删除 `AuctionUITexturePaths`（仍由贴图替换链路使用）；不改主题表结构、不改 `UnlockState` 列本身；不新增解锁 RPC 或解锁按钮；不改装扮主题素材与画刷机制
- 官方依据：`UGCPlayerStateSystem.GetPlayerArchiveData` / `UGCPlayerStateSystem.SavePlayerArchiveData` 为跨局存档入口，返回 table 需按玩家维度读写；蓝图变量本身不跨局持久化；`203_网络同步系统介绍` 与 `FBPVariableDescription` 用于说明控制器变量的读写与属性标志位

---

## 一、需求与约束

玩家装扮主题的解锁状态需要成为玩家自己的跨局数据，不能再把主题表 `DressTheme*Table` 的 `UnlockState` 列当作解锁来源。玩家控制器上原先没有装扮解锁状态存储变量；本轮按当前装扮切换逻辑补一个控制器镜像变量，并把它接入服务端玩家存档、客户端私有状态分发和装扮 UI 刷新链路。

关键约束：

1. 主题表 `UnlockState` 列必须被忽略，哪怕表里写 `Unlocked` 也不得据此放行。
2. 默认主题始终视为已解锁，避免默认装扮在无存档时被锁死。
3. 非默认主题只认玩家控制器 `AuctionDressThemeUnlockState`，控制器数据来自服务端玩家存档。
4. 不改 `AuctionUITexturePaths`；该变量属于另一条贴图路径配置链路。

## 二、控制器变量

资产：`/IslandAuctionKing/Asset/Blueprint/UGCPlayerController`

新增变量：

| 变量名 | 类型 | PropertyFlags | 用途 |
| --- | --- | --- | --- |
| `AuctionDressThemeUnlockState` | `FString` | `65541`（Edit + BPVisible + DisableEditOnInstance） | 已解锁主题 ID 的逗号分隔镜像，供客户端装扮 UI 快速读取 |

蓝图写入使用 UGCAskQ MCP 的 `Resolve → Plan → Execute` 流程，plan id：`plan_16791119_52c51972`。写后已编译、保存并回读，控制器自定义属性共 8 个，其中包含新变量。

删除旧装扮数据存储变量的核查：

- 全资产扫描未发现除 `AuctionDressThemeUnlockState` 外的装扮解锁存储变量。
- 对 `git rev-list --all` 与历史 `git grep` 复核，`UGCPlayerController` 历史上没有其它 `Dress*` 存储变量可删。
- `AuctionUITexturePaths` 不属于装扮主题解锁数据，且当前仍被 `AuctionUITexturePathService` / `AuctionUITextureReplacementService` / `AuctionTestUIService` 使用，因此保留。

## 三、存档与同步链路

### 服务端玩家存档

文件：`Script/Function/AuctionPlayerService.lua`

- `CreateDefaultArchiveData` / `CreateBot` 增加 `DressThemeUnlockState = {}`，保证新玩家与人机都有稳定字段。
- `NormalizeArchiveData` 把该字段规范化为 `{[themeId] = true}` 映射，兼容旧存档缺失字段。
- `LoadOrReconnectPlayer` 把存档中的 `gameArchive.DressThemeUnlockState` 复制到运行时 `player.DressThemeUnlockState`，并新增日志 `restoredThemeCount=` 与 `archiveVersion=`。
- `SyncControllerOwnership` 把 `player.DressThemeUnlockState` 转成排序后的逗号串，写入 `playerController.AuctionDressThemeUnlockState`。
- `BuildPrivateState` 把该字段加入玩家私有状态，供客户端 RPC 分发。
- `SavePlayer` 把 `DeepCopy(player.DressThemeUnlockState or {})` 写回玩家总存档。

### 客户端私有状态

文件：`Script/Blueprint/CF_FWDRPC.lua`

- 客户端私有状态缓存新增 `DressThemeUnlockState`，缺失时沿用上一次缓存，避免状态包裁剪导致误清空。
- `ClientAuctionPrivateState` 收到状态后把 table 转成排序后的逗号串，写入 `playerController.AuctionDressThemeUnlockState`。
- 当该串与旧值不同时，懒加载 `Script.Function.AuctionDressUIService` 并调用 `RefreshUnlockState(playerController)`；装扮层未打开时该调用返回 `false reason=NoActiveWidget`，不视为错误。
- 日志已包含 `AuctionDressThemeUnlockState=`，并在状态变化时打印 `previous=` / `next=`。

### 装扮 UI 判定

文件：`Script/Function/AuctionDressUIService.lua`

- 新增 `ResolveDressPlayerController`：优先使用 `widget.DressPlayerController`，否则通过 `GameplayStatics.GetPlayerController` 解析并缓存。
- 新增 `GetUnlockStateFingerprint`、`BuildUnlockedThemeSet`、`IsThemeUnlocked`：默认主题始终加入已解锁集合，其余只解析控制器上的逗号分隔主题 ID。
- `LoadStyleThemes` 的 `Unlocked` 由原来的 `tostring(row.UnlockState or "") ~= "Locked"` 改为 `IsThemeUnlocked(widget, themeId)`，不再读取 `row.UnlockState`。
- 主题表不可用而回退到 `Dress.Theme.StyleIds` 时，同样逐项调用 `IsThemeUnlocked`，不再无条件视为全部解锁。
- 新增 `RefreshUnlockState(playerController)`：对齐当前主题后整体 `Refresh`，用于私有状态变化后刷新已打开的装扮层。
- `CreateAndShow` 缓存 `widget.DressPlayerController`，保证后续刷新读到正确玩家控制器。

文件：`Script/Blueprint/UGCPlayerController.lua` 只补 `---@field AuctionDressThemeUnlockState FString` 类型注释，未新增 RPC。

### 存档版本

文件：`Script/Function/AuctionConfig.lua`

`ArchiveVersion` 保持 `3`。原因是运行时 `AuctionGlobalConfigTableService` 会用表内 `ArchiveVersion=3` 覆盖脚本值，而且新增字段是可选项，`NormalizeArchiveData` 已兼容旧存档；升版本会与表格配置不一致且无实际收益。注释已写明该原因。

## 四、备份

写前备份目录：`D:\知识库\和平精英绿洲起源\备份\IslandAuctionKing\20260924_装扮主题解锁存档\`

已备份：`AuctionPlayerService.lua`、`AuctionDressUIService.lua`、`AuctionDressThemeService.lua`、`AuctionConfig.lua`、`CF_FWDRPC.lua`、`CF_KHDRPC.lua`、`UGCPlayerController.lua`、`UGCPlayerController.uasset`，另有 `_head_extract\` 子目录保存 HEAD 版本 uasset 供比对。

## 五、验证

### 静态与 MCP

- 编辑器内置 luacheck：`ReturnCode: 0`（14:42:30）。
- UGCAskQ MCP 回读：`AuctionDressThemeUnlockState` 已持久化在 `UGCPlayerController` 蓝图类，类型 `FString`。
- 工程内扫描 `$null`、`_tmp_*.py`、`__pycache__`、`*.pyc` 均为 0 命中。

### PIE 实测

DebugID：`_dkck7psp70h6ft`（14:42:43 DS）。

服务端日志：

```text
【AuctionPlayerService+LoadOrReconnectPlayer】关键数据 UID=10001 ... restoredThemeCount=0 archiveVersion=3
【AuctionPlayerService+SyncControllerOwnership】关键数据 ... dressThemeUnlockState=
```

客户端日志：

```text
【CF_FWDRPC+ClientAuctionPrivateState】关键数据 ... AuctionDressThemeUnlockState=
```

存档落盘证据：`D:\WeGameApps\rail_apps\OasisEraEditor(2001776)\ShadowTrackerExtra\Saved\ArchiveData\IslandAuctionKing\10001.json` 内含 `"DressThemeUnlockState": []`、`"Version": 3`；`SavePlayer` 日志 `API返回值=true`、`archiveSize=488`。

### 未验证项

- 非空解锁集合的存档往返尚未验证。PIE 控制台通过 `doluastring` 到 DS 后 `GetPlayerArchiveData` 返回 `archiveType=nil`，属于 PIE 跨局存档限制，官方文档已说明 PIE 可能无法保存/读取；当前已确认空集合字段可落盘，非空集合需在正式环境或可用存档环境中复核。
- 当前工程没有“解锁主题”业务入口，因此没有代码把非默认主题写入 `player.DressThemeUnlockState`；除默认主题外，其余主题默认判为未解锁。后续若新增解锁来源，应直接写服务端 `player.DressThemeUnlockState[themeId] = true`，再走 `SyncControllerOwnership` / `BuildPrivateState` / `SavePlayer` 链路。

## 六、环境干扰说明

本轮 PIE 曾两次报 `CheckUploadFileNameFailed Result 10001` 与 `$null may contain the following characters: $`，连锁 `lua file validation failed`。经查是并发 Codex 会话用 `bash` 执行 `2>$null` 造成的既有环境问题（13:37、14:26 两次），已记录在 [2026-09-24_null文件再次出现与并发命令根因](../日志证据/2026-09-24_null文件再次出现与并发命令根因.md)。工程目录与 `Saved\UGCLinuxDebug` 复扫 `$null` 为 0，与本轮 Lua/蓝图改动无关。

## 七、生效方式

涉及控制器蓝图变量、玩家存档字段与初始化链路，必须重新调试 PIE；仅改 Lua 函数体时可热更新。预估成功日志（标注为“预估”）：

```text
【AuctionPlayerService+LoadOrReconnectPlayer】关键数据 ... restoredThemeCount=<N> archiveVersion=3
【AuctionPlayerService+SyncControllerOwnership】关键数据 ... dressThemeUnlockState=<逗号分隔主题ID>
【CF_FWDRPC+ClientAuctionPrivateState】关键数据 ... AuctionDressThemeUnlockState=<逗号分隔主题ID>
【AuctionDressUIService+BuildUnlockedThemeSet】关键数据 rawState=<逗号分隔主题ID> defaultStyleId=DefaultGray
```

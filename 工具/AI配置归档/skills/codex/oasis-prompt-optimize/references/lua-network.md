# Lua 与网络提示词

仅在任务改 Lua、RPC、端侧权威、玩家数据或日志规范时读取本页。

## 必须写进提示词的约束

- 新功能放 `Script/Function` 独立脚本，其他位置只调用，不把业务堆进蓝图脚本或 Controller。
- 变量和函数加简短中文注释。关键逻辑用 `ugcprint`，不用 `print`。
- 每个函数都要有入口、关键数据、分支、错误、出口日志，统一以 `【脚本名+函数名】` 开头，记录入参、`self`、`HasAuthority`、关键变量和判断结果。
- 关键逻辑用 `pcall` 保护，错误日志含 error 和上下文。成功标记只能写在 `pcall` 成功分支内。
- 服务端必须 `self:HasAuthority()` 双分支且双端打日志。禁止 `if not X then return end` 静默退出；退则必印原因。
- 配置必须在函数内通过配置加载器读取，并给默认回退值。禁止模块加载时 `GetNumber/GetBoolean/GetString`。
- 玩法数值、时长、容量、概率、测试开关、UI 尺寸坐标、提示时长、资源路径进对应功能 DataTable，禁止硬编码。纯算法常量不必进表。

## RPC

默认按双入口分发写进提示词，但不要把 IslandAuctionKing 的注册格式写成所有项目的官方 API：

```lua
function UGCPlayerController:KHDRPC_Call(f, ...) CF_KHDRPC(f, self, ...) end
function UGCPlayerController:FWDRPC_Call(f, ...) CF_FWDRPC(f, self, ...) end
```

调用：

```lua
UnrealNetwork.CallUnrealRPC(pc, pc, "KHDRPC_Call", "ServerRPC_XXX", args)
UnrealNetwork.CallUnrealRPC(pc, pc, "FWDRPC_Call", "ClientXXX", args)
```

禁止项：

- 在 Controller 新增其他 RPC 属性，或直接 `pc:RPC`
- 在 KHDRPC 调客户端专用 API，在 FWDRPC 调服务端专用 API
- KHDRPC 期望 `HasAuthority()==true`，FWDRPC 期望 `false`；异常端必须报错
- 新函数名：客户端到服务端用 `ServerRPC_` + PascalCase；服务端到客户端用 `Client` + PascalCase

项目若已有不同的 `GetAvailableServerRPCs` 契约，提示词必须要求先读该项目 Controller 实际代码和知识库项目证据，不得用通用示例覆盖。

## 数据存放

提示词要先判定数据位置，不要把所有玩家相关数据都塞进 Controller：

- 仅自己需要：`UGCPlayerController` 蓝图变量
- 全员可见阶段/倒计时/比分：`UGCGameState`
- 角色实体属性：PlayerPawn
- 队友可见、敌人不该看：PlayerState
- 静态配置：DataTable
- UI Widget 只展示，不存权威数据

加载自己工程资源用 `UGCGameSystem.GetUGCResourcesFullPath`。MCP 资产路径用 `/<ProjectName>/Asset/...`，不要 `/Game/`。`_C` 只给 `LoadClass` / 运行时类路径，不给 MCP 资产路径。

需要客户端看到服务端权威值时，提示词必须要求走属性同步：Actor `Replicates` + `GetReplicatedProperties()` + 需要时 `OnRep_变量名()`，只在 DS 写权威值。

## API 端侧

不确定的 API 必须先 `$oasis-official-docs --scope api --mode verify-api`。提示词里不要写猜测性生效范围。经验分类只能标成经验，并以官方「生效范围」为准：

- 客户端：`UGCWidgetManagerSystem.*`、`AddToViewport`、`SpawnEmitterAttached`
- 服务端：`SpawnActor`、属性写入、存档、伤害判定
- 双端查询常见于 `UGCGameSystem.*`；写属性仍看官方页

## 日志与回复

改文件类提示词要要求最终回复包含：路径、核心修改、查证来源、验证、MCP 状态、生效方式、预估成功日志（标注为预估）。只答题则不输出 PIE/热更新/预估日志。

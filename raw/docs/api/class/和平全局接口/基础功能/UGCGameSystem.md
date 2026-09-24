# UGCGameSystem

游戏通用接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCGameSystemImplementation.PlayerAntiAFKData |  |  |
| UGCGameSystemImplementation.NationalArenaCachedData |  |  |
| UGCGameSystemImplementation.CampDataBuffer |  |  |
| UGCGameSystem._RateLimiters |  |  |
| UGCGameSystem.GameMode |  | GameMode变量<br>生效范围：服务器 |
| UGCGameSystem.GameState |  | GameState变量<br>生效范围：服务器&客户端 |
| UGCGameSystem.UGCSTExtraGMDelegatesMgr |  | 全局事件代理<br>生效范围：服务器 |
| UGCGameSystem.ApplyPlayerJoinStoppedDelegate |  | 停止补充玩家时触发<br>生效范围：服务器<br>@param ApplyPlayerJoinStoppedReason EApplyPlayerJoinStoppedReason @停止补充玩家的原因 |
| UGCGameSystem.ApplyPlayerJoinSucceededDelegate |  | 通过补充玩家接口（UGCGameSystem.ApplyPlayerJoin、UGCGameSystem.ApplyPlayerJoinLimitCount），使得每一名玩家加入成功时触发<br>生效范围：服务器<br>@param UID number @玩家 UID<br>@param RemainingPlayerCountToJoin number @剩余需要加入的玩家数量 |

## Functions

### GetAllPlayerController

获取所有的 PlayerController，客户端仅能拿到自己的PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotIgnorePureSpectator | `boolean` | 是否包含非玩家观战者（全局观战） |

**Return**

- Type: 
- Description: _None_

### GetAllPlayerPawn

获取所有的 PlayerPawn
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAllPlayerState

获取所有的 PlayerState，客户端仅能拿到所有队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotIgnorePureSpectator? | `boolean` | 是否包含非玩家观战者(全局观战)，客户端不生效 |

**Return**

- Type: 
- Description: _None_

### GetAllPlayerKey

获取所有的 PlayerKey，包括敌人的，该接口通过Pawn获取敌人的PlayerKey，如果敌人没有Pawn，则获取的UID不全
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotIgnorePureSpectator? | `boolean` | 是否包含非玩家观战者(全局观战)，客户端不生效 |

**Return**

- Type: 
- Description: _None_

### GetAllUID

获取所有的 UID，包括敌人的，该接口通过Pawn获取敌人的UID，如果敌人没有Pawn，则获取的UID不全
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotIgnorePureSpectator | `boolean` | 是否包含非玩家观战者(全局观战) |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyByPlayerController

通过PlayerController获取PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyByPlayerPawn

通过PlayerPawn获取PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `ASTExtraPlayerCharacter` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyByPlayerState

通过PlayerState获取PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyByUID

通过 UID 获取 PlayerKey，客户端也可以获取敌人的UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerControllerByPlayerKey

根据 PlayerKey 获取 PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家唯一 Key |

**Return**

- Type: 
- Description: _None_

### GetPlayerControllerByUID

通过UID获取PlayerController
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家UID |

**Return**

- Type: 
- Description: _None_

### GetPlayerControllerByPlayerState

通过PlayerState获取PlayerController，客户端只能通过PlayerState获取当前客户端的PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerControllerByPlayerPawn

通过PlayerPawn获取PlayerController，客户端只能通过PlayerPawn获取当前客户端的PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `ASTExtraPlayerCharacter` |  |

**Return**

- Type: 
- Description: _None_

### GetAIControllerByPlayerKey

根据 AIPlayerKey 获取 AIController
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AIPlayerKey | `number` | 假玩家唯一 Key |

**Return**

- Type: 
- Description: _None_

### GetPlayerPawnByPlayerKey

根据 PlayerKey 获取 PlayerPawn（不会获取到尸体）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家唯一 Key |

**Return**

- Type: 
- Description: _None_

### GetPlayerPawnByUID

通过UID获取PlayerPawn，客户端也可以获取敌人的Pawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家UID |

**Return**

- Type: 
- Description: _None_

### GetPlayerPawnByPlayerState

通过PlayerState获取PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `ASTExtraPlayerState` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerPawnByPlayerController

通过PlayerController获取PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerStateByPlayerKey

根据 PlayerKey 获取 PlayerState，客户端只能拿到队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家唯一 Key |

**Return**

- Type: 
- Description: _None_

### GetPlayerStateByPlayerPawn

通过 PlayerPawn 获取 PlayerState，客户端仅能拿到所有队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `ASTExtraPlayerCharacter` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerStateByUID

根据 UID 获取 PlayerState，客户端仅能拿到所有队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |

**Return**

- Type: 
- Description: _None_

### GetPlayerStateByPlayerController

根据 PlayerController 获取 PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) | 玩家 Controller |

**Return**

- Type: 
- Description: _None_

### GetUIDByPlayerController

根据 PlayerController 获取 UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) | 玩家 Controller |

**Return**

- Type: 
- Description: _None_

### GetUIDByPlayerState

根据 PlayerState 获取 UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `PlayerState` | 玩家 PlayerState |

**Return**

- Type: 
- Description: _None_

### GetUIDByPlayerPawn

根据 PlayerPawn 获取 UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `ASTExtraPlayerCharacter` | 玩家 PlayerPawn |

**Return**

- Type: 
- Description: _None_

### GetUIDByPlayerKey

根据 PlayerKey 获取 UID，通过Pawn获取敌人的UID，如果敌人Pawn死亡则获取的结果不全
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |

**Return**

- Type: 
- Description: _None_

### NewObject

创建 Object
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Outer | [UObject](../../Others/UObject.md) |  |
| Class | `UClass` |  |
| Name | `string` |  |

**Return**

- Type: 
- Description: _None_

### SpawnActor

【废弃】请使用 UGCActorComponentUtility.SpawnActor
创建 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| ActorClass | `UClass` | 需要使用 UE.LoadClass 加载对应 Class 再作为参数传入 |
| Location | `Vector` | 可使用 Vector.New(x,y,z) 创建,结构 {X=x,Y=y,Z=z} |
| Rotation | `Rotator` | 可使用 Rotator.New(Roll,Pitch,Yaw) 创建,结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |
| Scale3D | `Vector` | 可使用 Vector.New(x,y,z) 创建,结构 {X=x,Y=y,Z=z}，不传缩放默认为 0，建议传 {X=1,Y=1,Z=1} |
| Owner | `Actor` | Actor 的拥有者 |

**Return**

- Type: 
- Description: _None_

### GetRespawnComponent

【废弃】请使用 UGCPlayerPawnSystem
获取复活组件
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlayerRespawnInfo

【废弃】请使用 UGCPlayerPawnSystem
设置复活信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | PlayerKey |
| IsUseRespawnLocation | `boolean` | 是否使用复活点 是：复活点复活 否：出生点复活 |
| RespawnLocation | [FTransform](../../../cppstruct/F/FT/FTransform.md) | 复活点位置 |

**Return**

_None_

### RespawnPlayer

【废弃】复活单个角色
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | PlayerKey |

**Return**

_None_

### RespawnAllPlayers

【废弃】请使用 UGCPlayerPawnSystem
复活所有角色
生效范围：服务器

**Parameters**

_None_

**Return**

_None_

### GetPlayerNum

获取玩家数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsIgnoreAI | `boolean` | 是否忽略 AI |

**Return**

- Type: 
- Description: _None_

### GetControllerByPawn

获取角色 Controller，包括 AI
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | [APawn](../../Others/APawn.md) |  |

**Return**

- Type: 
- Description: _None_

### ApplyRadialDamageWhiteList

造成爆炸类伤害，指定列表内 Actor 接受伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BaseDamage | `number` | 伤害值（最大） |
| MinimumDamage | `number` | 最小伤害 |
| Origin | `Vector` | 伤害中心 |
| DamageInnerRadius | `number` | 伤害内圈范围（受到最大伤害) |
| DamageOuterRadius | `number` | 伤害外圈范围（伤害持续衰减） |
| DamageFalloff | `number` | 内圈至外圈伤害衰减指数 |
| DamageTypeTags | `FGameplayTag[]` | 造成伤害的自定义类型列表 |
| GivenActors | `Actor[]` | 指定受伤害的 Actor 列表 |
| DamageCauser | `Actor` | 造成伤害的人/物体 |
| InstigatedByController | `Controller` | 煽动者的玩家控制器 |
| DamagePreventionChannel | [ECollisionChannel](../../../cppenum/E/EC/ECollisionChannel.md) | 伤害可见性阻挡通道 |
| ItemID | `number` | 造成伤害的物品 ID |

**Return**

- Type: 
- Description: _None_

### ApplyRadialDamage

造成爆炸伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BaseDamage | `number` | 伤害值（最大） |
| MinimumDamage | `number` | 最小伤害 |
| Origin | `Vector` | 伤害中心 |
| DamageInnerRadius | `number` | 伤害内圈范围（受到最大伤害) |
| DamageOuterRadius | `number` | 伤害外圈范围（伤害持续衰减） |
| DamageFalloff | `number` | 内圈至外圈伤害衰减指数 |
| DamageTypeTags | `FGameplayTag[]` | 造成伤害的自定义类型列表 |
| IgnoreActors | `Actor[]` | 伤害忽略 Actor 列表 |
| DamageCauser | `Actor` | 造成伤害的人/物体 |
| InstigatedByController | `Controller` | 煽动者的玩家控制器 |
| DamagePreventionChannel | [ECollisionChannel](../../../cppenum/E/EC/ECollisionChannel.md) | 伤害可见性阻挡通道 |
| ItemID | `number` | 造成伤害的物品 ID |

**Return**

- Type: 
- Description: _None_

### ApplyPointDamage

造成点伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamagedActor | `Actor` | 伤害目标 |
| BaseDamage | `number` | 伤害值 |
| HitFromDirection | `Vector` | 伤害来源方向（如子弹射击方向） |
| HitInfo | [FHitResult](../../../cppstruct/F/FH/FHitResult.md) | 命中信息 |
| EventInstigator | `Controller` | 事件煽动者的玩家控制器 |
| DamageCauser | `Actor` | 造成伤害的人/物体 |
| DamageTypeTags | `FGameplayTag[]` | 造成伤害的自定义类型列表 |
| ItemID | `number` | 造成伤害的物品 ID |

**Return**

- Type: 
- Description: _None_

### ApplyAvatarPositionDamage

造成部位伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamagedActor | `Actor` | 伤害目标 |
| BaseDamage | `number` | 伤害值 |
| EventInstigator | `Controller` | 事件煽动者的玩家控制器 |
| DamageCauser | `Actor` | 造成伤害的人/物体 |
| AvatarDamagePosition | [EAvatarDamagePosition](../../../cppenum/E/EA/EAvatarDamagePosition.md) | 造成伤害的部位 |
| DamageTypeTags | `FGameplayTag[]` | 造成伤害的自定义类型列表 |

**Return**

- Type: 
- Description: _None_

### ApplyDamage

造成伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamagedActor | `Actor` | 伤害目标 |
| BaseDamage | `number` | 伤害值 |
| EventInstigator | `Controller` | 事件煽动者的玩家控制器 |
| DamageCauser | `Actor` | 造成伤害的人/物体 |
| DamageTypeTags | `FGameplayTag[]` | 造成伤害的自定义类型列表 |

**Return**

- Type: 
- Description: _None_

### SendPlayerSettlement

【废弃】发送玩家结算（代表玩家已经完成了游戏，后台进行完成率统计，每个玩家正常结束游戏都需要发送）
最新：现已废弃，调用无效果，可以无需再调用，会在玩家退出游戏和触发 UGC请求退出DS Action 时自动发送
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 Key |

**Return**

- Type: 
- Description: _None_

### DisconnectClient

断开客户端连接。DS关闭后，需要同步关闭客户端对服务器的长链接检测，否则玩家客户端会弹出无法连接到服务器的报错信息。
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### OpenPlayerJoin

开启补充玩家（需要先开启补充玩家，发送补充玩家申请才会有效）
例：成局人数最小为 10 人，最大 20 人，匹配设置中设置 10 人，然后开启补充玩家，申请 10 人的补充名额
生效范围：服务器

**Parameters**

_None_

**Return**

_None_

### StopPlayerJoin

停止补充玩家（清空补充玩家申请记录）
生效范围：服务器

**Parameters**

_None_

**Return**

_None_

### ApplyPlayerJoin

申请补充玩家（申请数量会累加,需先调用 UGCGameSystem.OpenPlayerJoin 开启补充玩家）
例：成局人数最小为10人，最大20人，匹配设置中设置10人，然后开启补充玩家，申请10人的补充名额
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Count | `number` | 需要补充的玩家数量 |
| TeamID | `number` | 队伍ID |

**Return**

_None_

### ApplyPlayerJoinLimitCount

申请补充玩家（申请数量会累加,需先调用 UGCGameSystem.OpenPlayerJoin 开启补充玩家）
例：成局人数最小为10人，最大20人，匹配设置中设置10人，然后开启补充玩家，申请10人的补充名额。但不会使得对局玩家的数量超过项目设置中 “小队玩家数量（TeamPlayers） * 队伍数量（NumberOfTeams）”设置的数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamPlayerCounts | `table<int, int>` | 需要补充的玩家数量，形式如同：TeamPlayerCounts = { [TeamID1] = PlayerCount1, [TeamID2] = PlayerCount2, ... } |

**Return**

_None_

### EnterSpectating

进入观战，默认观战任意队友
可以通过 UGCGameSystem.ChangeAllowOBPlayerKeys 自定义可观战玩家列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 进入观战的玩家 Controller |

**Return**

- Type: 
- Description: _None_

### LeaveSpectating

退出观战
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 退出观战的玩家 Controller |

**Return**

_None_

### ChangeAllowOBPlayerKeys

设置可被观战玩家列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 可被观战玩家列表的 Controller |
| PlayerKeyList | `int32[]` | 可观战玩家列表数组 |

**Return**

_None_

### MyObserversChangeTarget

让观战我的人切换别的观战目标，只有当观战对象的Pawn死亡时才生效
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 不再被观战的玩家 Controller |

**Return**

_None_

### IsEnableGM

是否开启 GM，自定义 GM 逻辑和界面可接入此开关，正式服中此开关为 false
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家 Controller |

**Return**

- Type: 
- Description: _None_

### IsServer

是否为服务端
逻辑依赖 UGCGameSystem.GameState，在 GameState 初始化前的逻辑不建议调用此函数判断
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsDebug

是否在 Debug（编辑器 Debug 调试）
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlatformInfo

获取平台类型
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAllAIController

获取所有的 AIController
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReturnToLobby

主动返回大厅（使用此接口返回大厅的玩家不会弹出重进战斗对话框）
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### ChangeOBPlayer

改变当前观战目标（仅限观战中使用）
例：被观战的玩家被淘汰后，需要使用此接口，切换至其他玩家进行观战
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 自己的 PlayerController |
| PlayerKey | `number` | 观战目标玩家 PlayerKey |

**Return**

_None_

### SendModeCustomEvent

向模式编辑器发送自定义事件
根据自定义事件参数顺序传入,如 SendModeCustomEvent(EventName,param1,param2)
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EventName | `string` | 事件名 |
| ... | `any` | 自定义事件参数 |

**Return**

_None_

### GetServerTimeSec

获取当前服务器时间
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTimer

设置定时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | [UObject](../../Others/UObject.md) | 对象 |
| CallbackFunction | `LuaFunction` | Lua 回调函数 |
| Time | `number` | 定时时长 |
| IsLooping | `boolean` | 是否循环 |

**Return**

- Type: 
- Description: _None_

### ClearTimer

移除定时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | [UObject](../../Others/UObject.md) | 上下文对象 |
| TimerHandle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | 定时器句柄 |

**Return**

_None_

### SendTLog

记录埋点日志
value 中多个字段建议使用_（下划线）分割
例: ItemName_NormalItem_Count_1
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `string` | 日志索引 |
| Value | `string` | 日志内容 |

**Return**

_None_

### SendGreyTLog

记录灰度埋点日志
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `number` | 灰度 ID |
| PlayerKey | `number` | 玩家 ID |

**Return**

_None_

### SendGameTlog

发送游戏日志
生效范围：服务器
注意：函数会先做本地参数校验和频率限制；命中拦截时会直接 return，不会真正发包。
Index 范围与 CustomData 结构规范，不符合条件会被拦截：
  · [800800, 801800]：自定义TLog，CustomData 无结构限制
  · [801801, 802800]：二级及以下货币TLog，CustomData 必须包含以下字段，否则会被拦截：
    AfterMoney(number/必填)、iMoney(number/必填)、Reason(number/必填)、SubReason(number/必填)、
    AddOrReduce(number/必填)、iMoneyType(number/必填)、CustomData(table/必填，空传{})
  · [802801, 804800]：物品流传说信息TLog，CustomData 必须包含以下字段，否则会被拦截：
    iGoodsType(number/必填)、iGoodsId(number/必填)、iGoodsName(string/必填)、iCount(number/必填)、
    AfterCount(number/必填)、Reason(number/必填)、SubReason(number/必填)、AddOrReduce(number/必填)、
    CustomData(table/必填，空传{})
拦截原因说明：
  1) Index 为 nil、非 number、或不在 [800800, 804800] 范围内
  2) UID 为 nil 或非 number
  3) CustomData 为 nil 或非 table
  4) 当 Index 属于 [801801, 802800] 或 [802801, 804800] 时，对应必填字段缺失或类型不符
  5) 触发频率限制（一分钟100次）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `number` | 日志索引，必填；具体范围与校验规则见上方说明 |
| UID | `number` | 玩家UID，必填；当前实现不支持传空，传 nil 或非 number 会在本地校验阶段被拦截，日志不会发出去；UID无效/错误仍可能导致上报失败 |
| CustomData | `table` | 自定义数据，必填 table；具体校验规则见上方说明 |

**Return**

_None_

### SendLiveStreamingTLog

发送直播日志
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LogType | `number` | 类型 1-赛事，2-人生 |
| Id | `number` | 事件ID(自定义) |
| Value | `table` | 事件内容(自定义) |

**Return**

_None_

### UploadOfficialModuleData

上传玩家维度的官方模块自定义数据
 moduleName = "national_arena"（全民赛场）:
   用于团竞类赛事结算数据上报。内核强制只允许 4 个字段，全部 number，不多不少。
   调用后仅缓存，不立即发送。等 ugc_result 发送时自动取用并合并到 UGCPlayerBattleResult，取后即清。
   data 结构：
     {
       player_kill_num = 5,      -- number, 击杀数，只有团竞类才有
       enemy_damage = 1280,      -- number, 对敌人伤害，团竞上报 / 造成伤害
       team_win = 1,             -- number, 队伍胜负：1=胜 2=负 3=平
       round_time = 632,         -- number, 对局时长（秒）
     }

 moduleName = "camp"（营地）:
   用于玩家档案、最近游玩、玩法详情等自定义数据展示。字段不强制限制，推荐以下结构。
   缓冲队列 + 防抖，同一 UID 10 秒内多次上传直接覆盖（不 deep merge），不发送。
   后台协议未定，实际发送逻辑暂留空。
   data 推荐结构：
     {
       profile = {               -- 数据档案
         history_play = "128",   -- 历史游玩次数
         max_power = "98000",    -- 最高战力
         realm = "化神",         -- 境界
       },
       recent = {                -- 最近游玩
         rank = "钻石",          -- 段位
         score = "2600",         -- 积分
         power = "87000",        -- 当前战力
       },
       detail = {                -- 玩法详情
         title = "宗门长老",     -- 称号
         career = "剑修",        -- 职业
       },
     }
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| playerUid | `string` | 玩家账号 UID，用于标识数据归属 |
| moduleName | `string` | 目标官方模块名，可选值：camp(营地)、national_arena(全民赛场) |
| data | `table` | 自定义数据表，结构根据 moduleName 不同而不同 |

**Return**

_None_

### SetTournamentInfo

设置赛事信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家Key |
| bEscaped | `boolean` | 是否逃跑 |
| PersonRank | `number` | 个人排名 |
| TeamRank | `number` | 队伍排名 |
| MatchResult | `ETournamentMatchResult` | 胜利失败信息 |

**Return**

_None_

### SetMoveInputEventEnable

是否关闭移动输入事件
IsOverride 开启后需要在 PlayerController 重载 UGCMoveEvent(Vector2D) 事件
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| IsEnable | `boolean` | 是否关闭 |
| IsOverride | `boolean` | 是否重载（原移动输入会被覆盖） |

**Return**

_None_

### SetLookInputEventEnable

开启/关闭旋转输入事件
IsOverride 开启后需要在 PlayerController 重载 UGCLookEvent(Vector2D) 事件
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `PlayerController` | 玩家控制器 |
| IsEnable | `boolean` | 是否开启 |
| IsOverride | `boolean` | 是否重载（原旋转输入会被覆盖） |

**Return**

_None_

### ClientPlayCameraShake

在PlayerController对应的客户端震屏
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) | 震屏玩家的 PlayerController |
| CameraShakeType | [EPESkillCameraShakeType](../../../cppenum/E/EP/EPESkillCameraShakeType.md) | 震屏类型(随机方向/X方向/Y方向) |
| ShakeScale | `number` | 震屏强度 |
| Duration | `number` | 震屏时间(单位:秒，<=0 表示一直持续) |

**Return**

_None_

### ClientStopCameraShake

在PlayerController对应的客户端停止某类型的震屏
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) | 震屏玩家的 PlayerController |
| CameraShakeType | [EPESkillCameraShakeType](../../../cppenum/E/EP/EPESkillCameraShakeType.md) | 震屏类型(随机方向/X方向/Y方向) |

**Return**

_None_

### GetTableData

根据表格路径获取表格内容
TablePath支持以下格式(...表示相对Asset目录的路径, 如Data/Table)：
.../TableName
UGCGameSystem.GetUGCResourcesFullPath('Asset/.../TableName.TableName')
/Game/.../TableName.TableName
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TablePath | `string` | 表格路径 |

**Return**

- Type: 
- Description: _None_

### GetTableCount

根据表格路径获取表格行数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TablePath | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |

**Return**

- Type: 
- Description: _None_

### GetTableDataByRowName

根据表格路径，以及key获取表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TablePath | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| RowName | `number` | key值 string型或者int型都可以 |

**Return**

- Type: 
- Description: _None_

### GetDataTableData

获取指定DataTable的表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DataTable | [UDataTable](../../Others/UDataTable.md) | 要读取的表格 |

**Return**

- Type: 
- Description: _None_

### GetDataTableDataByRowName

获取指定DataTable的指定行的表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DataTable | [UDataTable](../../Others/UDataTable.md) | 要读取的表格 |
| RowName | `string` | 行名 |

**Return**

- Type: 
- Description: _None_

### GetDataTableRowCount

获取指定DataTable的行数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DataTable | [UDataTable](../../Others/UDataTable.md) | 要读取的表格 |

**Return**

- Type: 
- Description: _None_

### AsyncGetTableData

异步根据表格路径获取表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TablePath | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| CallBack | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| CallBack_self | [UObject](../../Others/UObject.md) | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Return**

_None_

### AsyncGetTableCount

异步根据表格路径获取表格行数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TablePath | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| CallBack | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| CallBack_self | [UObject](../../Others/UObject.md) | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Return**

_None_

### AsyncGetTableDataByRowName

异步根据表格路径获取表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TablePath | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| RowName | `string` | 查询关键字 |
| CallBack | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| CallBack_self | [UObject](../../Others/UObject.md) | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Return**

_None_

### IsMyFriend

是否为好友
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |

**Return**

- Type: 
- Description: _None_

### AddFriend

添加好友
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |

**Return**

_None_

### OpenComplaintUI

打开举报界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 目标玩家 UID |

**Return**

_None_

### GetUGCResourcesFullPath

获取资源的完整加载路径
仅自己工程下资源需要使用此函数获取路径，和平精英目录资源不需要使用此函数拼接路径
例：自己工程资源
local ClassPath = "Asset/MyBlueprint.MyBlueprint_C"
UE.LoadClass(UGCGameSystem.GetUGCResourcesFullPath(ClassPath))
例：和平精英目录资源
local ClassPath = "/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C"
UE.LoadClass(ClassPath)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RelativePath | `string` | 工程资源路径 |

**Return**

- Type: 
- Description: _None_

### UGCRequire

用于替代原生require，如果需要将功能发布至资源商店，需要使用此函数 require lua 文件
例：require("Script.MyLua");
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RelativePath | `string` | Lua 文件路径 |

**Return**

- Type: 
- Description: _None_

### ShowUGCRankAndAchievementUI

显示绿洲段位，徽章结算界面
会自动显示段位变化以及新增徽章
详细内容参考：https://developer.gp.qq.com/wikieditor/#/catalog/375
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### GetSTExtraGMDelegatesMgr

获取 DS 全局事件代理
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalPlayerController

获取客户端当前的 PlayerController
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalPlayerPawn

获取客户端当前的 PlayerPawn
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalPlayerState

获取客户端当前的 PlayerState
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalPlayerKey

获取客户端当前的 PlayerKey
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGameMode

获取当前的 GameMode
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGameState

获取当前的 GameState
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsRoomMode

判断是否是房间模式
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CollectPlayerAntiAFKData

反挂机数据收集 在结算数据里上报 1.击杀数-Kill 2.伤害量-DamageAmount 3.移动距离-TravelDistance 4.达到存档数-ReachedArchives
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 上报玩家的UID |
| DataKey | `string` | 上报数据的字段名字 |
| DataValue | `string` | 上报数据 |

**Return**

_None_

### GetCurrentLevel

获取当前关卡
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 关卡上下文对象 |
| bRemovePrefixString | `boolean` | 是否移除前缀字符串 |

**Return**

- Type: 
- Description: _None_

### LoadStreamLevel

加载关卡
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LevelName | `string` | 关卡名字 |
| bMakeVisibleAfterLoad | `boolean` | 是否在加载完成后显示关卡 |
| bShouldBlockOnLoad | `boolean` | 是否延迟加载 |
| LatentInfo | `LatentInfo` | 延迟信息 |

**Return**

_None_

### UnloadStreamLevel

卸载关卡
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LevelName | `string` | 关卡名字 |
| LatentInfo | `LatentInfo` | 延迟信息 |

**Return**

_None_

### FlushLevelStreaming

强制刷新关卡流加载
生效范围：服务器

**Parameters**

_None_

**Return**

_None_

### MakeWeakObjectPtr

【废弃】创建弱对象指针
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | [UObject](../../Others/UObject.md) | 对象 |

**Return**

- Type: 
- Description: _None_

### GetObjectFromWeakObjectPtr

【废弃】从弱对象指针获取对象
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWeakObjectPtr | `WeakObjectPtr` | 弱对象指针 |

**Return**

- Type: 
- Description: _None_

### IsWeakObjectPtrValid

【废弃】判断弱对象指针是否有效
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWeakObjectPtr | `WeakObjectPtr` | 弱对象指针 |

**Return**

- Type: 
- Description: _None_

### SwitchMouseCursorShowState

切换鼠标显示
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### GetShowMouseCursor

获取鼠标显示状态
生效范围：客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMouseCursorShowState

设置鼠标显示
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bShow | `boolean` | 是否显示鼠标 |

**Return**

_None_

### DrawOutline

设置Actor描边
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | Actor |
| bIsDrawOutline | `boolean` | 是否描边 |
| OutlineThickness | `number` | 描边粗细 |
| OutlineColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 描边颜色 |

**Return**

_None_

### IsUGCPIE

是否为PIE环境
生效范围：服务器 & 客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SpawnEmitterAtLocation

在指定位置生成粒子效果，粒子系统播放完成后会自动销毁，不会进行网络复制
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| EmitterTemplate | [UParticleSystem](../../Others/UParticleSystem.md) | 要创建的粒子系统 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 旋转 |
| Scale | [FVector](../../../cppstruct/F/FV/FVector.md) | 缩放 |
| bAutoDestroy | `boolean` | 是否自动销毁 |

**Return**

- Type: 
- Description: _None_

### SpawnEmitterAttached

播放指定效果，该效果会附加到指定组件并跟随其移动。效果播放完成后系统将消失。此效果不进行网络复制
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterTemplate | [UParticleSystem](../../Others/UParticleSystem.md) | 要创建的粒子系统 |
| AttachComponent | [USceneComponent](../../Others/USceneComponent.md) | 要附加到的组件 |
| AttachPointName | `string` | 附加组件中用于生成发射器的可选命名点（若不指定则在附加组件原点生成） |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 根据 LocationType 的值，此参数可为相对于附加组件/点的偏移量；或为绝对世界位置（若 LocationType 为 KeepWorldPosition，则会将该位置转换为相对于附加组件/点的偏移） |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 根据 LocationType 的值，此参数可为相对于附加组件/点的旋转偏移量；或为绝对世界旋转（若 LocationType 为 KeepWorldPosition，则会将该旋转转换为相对于附加组件/点的偏移） |
| Scale | [FVector](../../../cppstruct/F/FV/FVector.md) | 根据 LocationType 的值，此参数可为相对于附加组件的缩放比例；或为绝对世界缩放（若 LocationType 为 KeepWorldPosition，则会将该缩放转换为相对于附加组件的比例） |
| LocationType | [EAttachLocation](../../../cppenum/E/EA/EAttachLocation.md) | 指定 Location 是相对偏移量还是绝对世界位置 |
| bAutoDestroy | `boolean` | 粒子系统播放完成后，此组件是自动销毁还是可重新激活 |

**Return**

- Type: 
- Description: _None_

### SpawnDecalAtLocation

在指定位置和旋转角度生成一个贴花，生成后无需管理。此效果不进行网络复制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| DecalMaterial | [UMaterialInterface](../../Others/UMaterialInterface.md) | 贴花的材质 |
| DecalSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 贴花的尺寸 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 贴花在世界空间中的放置位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 贴花在世界空间中的放置旋转 |
| LifeSpan | `number` | 贴花组件在时间结束后销毁（0表示永久存在） |

**Return**

- Type: 
- Description: _None_

### SpawnDecalAtAttached

在指定组件上生成一个附加并跟随的贴花。此效果不进行网络复制

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DecalMaterial | [UMaterialInterface](../../Others/UMaterialInterface.md) | 贴花的材质 |
| DecalSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 贴花的尺寸 |
| AttachComponent | [USceneComponent](../../Others/USceneComponent.md) | 要附加到的组件 |
| AttachPointName | `string` | 附加组件中用于生成发射器的可选命名点（若不指定则在附加组件原点生成） |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 根据 LocationType 的值，此参数可为相对于附加组件/点的偏移量；或为绝对世界位置（若 LocationType 指定为 KeepWorldPosition，则会将该位置转换为相对于附加组件/点的偏移） |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 根据 LocationType 的值，此参数可为相对于附加组件/点的旋转偏移量；或为绝对世界旋转（若 LocationType 指定为 KeepWorldPosition，则会将该旋转转换为相对于附加组件/点的偏移） |
| LocationType | [EAttachLocation](../../../cppenum/E/EA/EAttachLocation.md) | 指定 Location 是相对偏移量还是绝对世界位置 |
| LifeSpan | `number` | 贴花组件在时间结束后销毁（0 表示永久存在） |

**Return**

- Type: 
- Description: _None_

### GetTimeSeconds

获得当前游戏开始之后的时间，单位秒，受时间膨胀影响，但不受游戏暂停影响
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |

**Return**

- Type: 
- Description: _None_

### DateTimeToTimeStamp

将日期时间转换为时间戳
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DateTime | `FDateTime` | 日期时间 |

**Return**

- Type: 
- Description: _None_

### GetCurrentDateTime

获取当前日期时间
生效范围：服务器 & 客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDSRemainingTime

获取DS剩余时间，单位秒
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetDSCloseNotify

设置DS关闭通知时间，监听UGCGenericMessageSystem.UserDefinedMessages.UGC.UGCDSShutDownManager.DSCloseNotify，会在到达时间时发送通知，附带参数为DS剩余时间
假设已经到了设置的时间比DS长，例如DS剩余关闭时间是30s，设置的时间组是{50，40，20}，那么会在游戏开始时，50和40两个时间点合并仅发送一次通知，目前仅支持整数时间点
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotifyTimes | `int[]` | 通知时间组 |

**Return**

_None_

### GameOver

游戏结束，一键执行发送所有玩家结算，玩家退出和玩家销毁的动作，并关闭DS，这个接口会有一定延时，如果玩家还在游戏内执行，会将玩家强行踢出ds，返回大厅
生效范围：服务器

**Parameters**

_None_

**Return**

_None_

### IsObserver

判断玩家是否为观战玩家
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [APlayerController](../../Others/APlayerController.md) | 玩家控制器 |

**Return**

- Type: 
- Description: _None_

### MakeCustomDamageNumberParams

生成自定义伤害数字默认参数
生效范围：服务器 & 客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddUGCCustomDamageNumber

在目标对象位置显示自定义伤害数字
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| TargetActor | `Actor` | 伤害数字显示目标 |
| Params | [FUGCDamageNumberParams](../../../cppstruct/F/FU/FUGCDamageNumberParams.md) | 自定义伤害数字参数 |

**Return**

_None_

### AddUGCCustomDamageNumberByScreenOffset

在屏幕特定位置显示自定义伤害数字
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| ScreenOffset | `Vector2D` | 伤害数字显示位置相对于屏幕中心点的偏移 |
| Params | [FUGCDamageNumberParams](../../../cppstruct/F/FU/FUGCDamageNumberParams.md) | 自定义伤害数字参数 |

**Return**

_None_

### AddUGCCustomDamageNumberByNormalizedScreenPosition

在屏幕特定位置显示自定义伤害数字
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Pos | `Vector2D` | 伤害数字在屏幕上的相对显示位置 如{X=0.5, Y=0.5} 为屏幕中心 |
| Params | [FUGCDamageNumberParams](../../../cppstruct/F/FU/FUGCDamageNumberParams.md) | 自定义伤害数字参数 |

**Return**

_None_

### IsOuterlineDEV

【废弃】请使用 UGCGameSystem.GetDSEnvType
判断是否为外研线
生效范围：服务器 & 客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDSEnvType

获取当前DS所在的运行环境类型
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsGray

当前玩法是否处于灰度中
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

# UGCPlayerPawnSystem

角色系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### HasPawnState

是否在指定状态下
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### AllowPawnState

是否允许进入指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### SwitchPoseState

切换 Pose 状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PoseState | [ESTEPoseState](../../cppenum/E/ES/ESTEPoseState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### EnterPawnState

进入指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### LeavePawnState

离开指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### DisabledPawnState

禁用指定状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../cppenum/E/EP/EPawnState.md) | 角色状态 |
| IsDisabled | `boolean` | 是否禁用 |

**Return**

_None_

### GetIsFPP

获取是否第一人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` |  |

**Return**

- Type: 
- Description: _None_

### SetIsFPP

设置是否第一人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| IsFPP | `boolean` | 是否第一人称 |
| bForce | `boolean` | 强制设置人称 |

**Return**

- Type: 
- Description: _None_

### GetIsTPP

获取是否第三人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` |  |

**Return**

- Type: 
- Description: _None_

### SetIsTPP

设置是否第三人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| IsTPP | `boolean` | 是否第三人称 |
| bForce | `boolean` | 强制设置 TPP 模式 |

**Return**

- Type: 
- Description: _None_

### GetIsInvincible

获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetIsInvincible

设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| IsInvincible | `boolean` | 是否无敌 |

**Return**

_None_

### TryEnterParachuteState

尝试进入跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| CheckPawnState | `EPawnState[]` | 不允许进入跳伞的角色状态 |
| CanOpenParachuteHeight | `number` | 允许开伞高度 |
| ForceOpenParachuteHeight | `number` | 强制开伞高度 |
| CloseParachuteHeight | `number` | 关伞高度 |
| bParachuteAvatarNotShown | `boolean` | 是否不显示伞包 |

**Return**

_None_

### ExitParachuteState

退出跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

_None_

### HideBoneByBoneName

根据玩家角色的骨骼名称修改骨骼的显隐性
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BoneName | `string` | 骨骼名称 |
| bHide | `boolean` | true隐藏，false显示 |

**Return**

_None_

### SetAvatarVisibility

设置角色Avatar的显隐
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| bHide | `boolean` | true显示，false隐藏 |
| ExcludingAvatarSlot | `EAvatarSlotType[]` | 排除的AvatarSlot类型 |

**Return**

_None_

### ChangeAvatarMesh

切换玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| SkeletalMesh | `UClass\|string` | 全身骨骼体蓝图类或路径 |
| bIsUseBoneRetarget | `boolean` | 是否使用骨骼重定向,默认false,外部导入的骨骼体需要设置为true |

**Return**

_None_

### RecoverAvatarMesh

恢复玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

_None_

### SkipSpawnDeadTombBox

玩家死亡取消生成盒子
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| bIsSkip | `boolean` | 玩家是否取消生成死亡盒子 |

**Return**

_None_

### GetPartTypeSockets

获取角色骨骼里所有的PartTypeSocket
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Character | [ACharacter](./ACharacter.md) | 角色 |

**Return**

- Type: 
- Description: _None_

### SetDefaultPlayerRespawnPointSelectionMethod

设置玩家的默认复活方式
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Method | [EUGCPlayerRespawnPointSelectionMethod](../../cppenum/E/EU/EUGCPlayerRespawnPointSelectionMethod.md) | 复活方式 |
| RespawnMethodInfo | [FVector](../../cppstruct/F/FV/FVector.md) | 指定复活位置（仅选择复活方式为指定复活点生效） |

**Return**

_None_

### SetDefaultPlayerSpawnPointSelectionMethod

设置玩家默认的出生方式
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Method | [EUGCPlayerSpawnPointSelectionMethod](../../cppenum/E/EU/EUGCPlayerSpawnPointSelectionMethod.md) | 出生方式 |
| SpawnMethodInfo | `FVector\|uint8` | 出生点类型 |
| PlayerStartInfo | `boolean` | 是否随机出生点ID |

**Return**

_None_

### RespawnPlayer

复活单个角色
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | PlayerKey |
| RespawnDelayTime | `number` | 复活延时时间，默认为0 |
| IsDestoryAlivePawn | `boolean` | 是否销毁当前未死亡的角色 |
| DestroyDelayTime | `number` | 销毁未死亡角色的延时时间，默认为0.01，销毁时间不能设为零，否则角色不销毁 |

**Return**

_None_

### RespawnAllPlayers

复活所有角色
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RespawnDelayTime | `number` | 复活延时时间，默认为0 |
| IsDestroyAlivePawn | `boolean` | 是否销毁当前未死亡的角色 |
| DestroyDelayTime | `number` | 销毁未死亡角色的延时时间，默认为0 |

**Return**

_None_

### SetRescueInterruptable

设置救援队友是否能被打断
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bCanBeInterrupt | `boolean` | 是否能被打断 |
| CanBeInterruptWhenOverRadius | `number` | 施救者可以移动的范围半径(传入的bCanBeInterrupt为true时这个变量才生效) |

**Return**

_None_

### SetRescueOtherDuration

设置救援队友的时长
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| RescueOtherDuration | `number` | 救援队友的时长 |

**Return**

_None_

### SetRescuingSelfCDTime

设置自救的冷却时间
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| RescuingSelfCDTime | `number` | 救援队友的冷却时间 |

**Return**

_None_

### ConfirmRescueOther

确认救援队友
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| InTargetPawn | `PlayerPawn` | 救援对象 |

**Return**

_None_

### ConfirmRescueOtherImmediately

确认救援队友并将队友立即救起
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| InTargetPawn | `PlayerPawn` | 救援对象 |

**Return**

_None_

### SetIsDirectlyDie

设置玩家倒地后立即死亡
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bIsDirectlyDie | `boolean` | 是否倒地后立即死亡 |

**Return**

_None_

### ConfirmCarryOther

确认背负倒地队友
生效范围：服务器
前置条件：
   1. 被背负者处于倒地状态（IsHaveLastBreathStatus）
   2. 背负者未在背负他人（CarryWho == nil）
   3. 双方都允许背负/被背负（bEnableCarryOther / bEnableCarriedByOther）
   4. 不在脱离CD中
   5. 背负者与被背负者距离在检测范围内

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 背负者 |
| InTargetPawn | `PlayerPawn` | 被背负的倒地队友 |

**Return**

- Type: 
- Description: _None_

### ConfirmPutDownCarried

确认放下被背负的队友
生效范围：服务器
前置条件：
   1. 正在背负他人（CarryWho != nil）
   2. 当前状态为 Carring

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 背负者 |

**Return**

- Type: 
- Description: _None_

### InterruptCarry

中断背负（单方面中断）
生效范围：服务器
前置条件：
   bIsCarrier=true  时：正在背负他人（CarryWho != nil）
   bIsCarrier=false 时：正在被他人背负（BeCarriedByWho != nil）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bIsCarrier | `boolean` | 是否是背负方 |

**Return**

- Type: 
- Description: _None_

### BreakAwayFromCarrier

被背负者主动脱离
生效范围：服务器
前置条件：
   1. 正在被他人背负（BeCarriedByWho != nil）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 被背负的角色 |

**Return**

- Type: 
- Description: _None_

### SetCarryOtherEnabled

设置是否允许背负倒地队友
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bEnable | `boolean` | 是否允许 |

**Return**

_None_

### SetBeCarriedEnabled

设置是否允许被他人背负
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bEnable | `boolean` | 是否允许 |

**Return**

_None_

### SetCarryDetectRange

设置背负检测范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| Radius | `number` | 检测半径 |
| Angle | `number` | 扇形角度 |
| Offset | `number` | 检测中心前向偏移 |

**Return**

_None_

### SetBreakAwayCooldown

设置脱离冷却时间
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| Cooldown | `number` | 冷却时间（秒，0=无CD） |

**Return**

_None_

### GetCarryState

获取背负状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### GetCarryTarget

获取正在背负的目标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### GetCarriedByWho

获取谁在背我
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### IsBeingCarried

是否正在被背负
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### IsCarryingOther

是否正在背负他人
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### IsCarriedByAI

是否被AI背负
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### AddOnCarryStateChanged

监听背负状态变化事件
生效范围：服务器
 bIsCarrier=true=Character是背负方，false=Character是被背负方
 LastState/NewState 为 ECarringState 枚举: None(0)=无 Waitting(1)=等待 PuttingUp(2)=搬起中 Carring(3)=背负中 PuttingDown(4)=放下中
 背负开始: LastState~=Carring → NewState=Carring
 背负结束: LastState=Carring → NewState=None (放下/脱离/自杀/中断都是这个转换)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 要监听的玩家角色 |
| Callback | `function` | 回调函数 function(Character, bIsCarrier, LastState, NewState) |
| Context | `table` | 回调绑定的 self 对象（用于 Remove 时精确匹配，回调时作为 self 参数） |

**Return**

_None_

### RemoveOnCarryStateChanged

取消监听背负状态变化事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 要取消监听的玩家角色 |
| Callback | `function` | 注册时传入的回调函数 |
| Context | `table` | 注册时传入的 self 对象 |

**Return**

_None_

### ConfirmCarryDeadBox

确认搬起死亡盒子
生效范围：服务器
前置条件：
   1. 目标死亡盒子有效且未被搬运
   2. 当前未在搬运其他盒子（状态为 None）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 搬运者 |
| InTargetDeadBox | `PlayerTombBox` | 目标死亡盒子 |

**Return**

- Type: 
- Description: _None_

### ConfirmPutDownDeadBox

确认放下正在搬运的死亡盒子
生效范围：服务器
前置条件：
   1. 正在搬运死亡盒子（状态非 None）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 搬运者 |

**Return**

- Type: 
- Description: _None_

### InterruptCarryDeadBox

中断搬运死亡盒子
生效范围：服务器
前置条件：
   1. 正在搬运死亡盒子（状态非 None）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### SetCarryDeadBoxEnabled

设置搬运死亡盒子功能开关（全局）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色（作为 WorldContext） |
| bEnable | `boolean` | 是否允许 |

**Return**

_None_

### SetCarryDeadBoxDetectRange

设置搬运检测范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| Radius | `number` | 检测半径 |
| Angle | `number` | 扇形角度 |
| Offset | `number` | 检测中心前向偏移 |

**Return**

_None_

### SetCarryDeadBoxPutDownParams

设置放下检测参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| HalfExtent | [FVector](../../cppstruct/F/FV/FVector.md) | 检测盒半边长 |
| ForwardDist | `number` | 前向检测距离 |
| DownwardDist | `number` | 向下检测距离 |

**Return**

_None_

### GetCarryDeadBoxState

获取搬运死亡盒子状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### GetCarriedDeadBox

获取正在搬运的死亡盒子
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### IsCarryingDeadBox

是否正在搬运死亡盒子
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |

**Return**

- Type: 
- Description: _None_

### AddOnCarryDeadBoxStateChanged

监听搬运死亡盒子状态变化事件
生效范围：服务器
 Character=角色自身（仅有搬运方，无被搬运方概念）
 LastState/NewState 为 ECarringState 枚举: None(0)=无 Waitting(1)=等待 PuttingUp(2)=搬起中 Carring(3)=搬运中 PuttingDown(4)=放下中
 搬运开始: LastState~=Carring → NewState=Carring
 搬运结束: LastState=Carring → NewState=None (放下/中断)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 要监听的玩家角色（搬运者） |
| Callback | `function` | 回调函数 function(Character, LastState, NewState) |
| Context | `table` | 回调绑定的 self 对象（用于 Remove 时精确匹配，回调时作为 self 参数） |

**Return**

_None_

### RemoveOnCarryDeadBoxStateChanged

取消监听搬运死亡盒子状态变化事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 要取消监听的玩家角色 |
| Callback | `function` | 注册时传入的回调函数 |
| Context | `table` | 注册时传入的 self 对象 |

**Return**

_None_

### DrawOutline

设置玩家描边
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bIsDrawOutline | `boolean` | 是否描边 |
| OutlineThickness | `number` | 描边粗细 |
| OutlineColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | 描边颜色 |

**Return**

_None_

### AddOcclusionHighlight

添加透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetCharacter | [ACharacter](./ACharacter.md) | 被透视的角色或怪 |
| Causer | [AActor](./AActor.md) | 透视的发起方 |
| Type | [EPEBuffOcclusionHighlightType](../../cppenum/E/EP/EPEBuffOcclusionHighlightType.md) | 透视类型(仅Causer透视/Causer及其队友透视/所有人) |
| Color | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | 透视颜色 |

**Return**

- Type: 
- Description: _None_

### RemoveOcclusionHighlight

移除透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](./UObject.md) | 世界上下文对象 |
| OcclusionID | `number` | 透视ID，AddOcclusionHighlight函数的返回值, <=0为无效值 |

**Return**

_None_

### SetOutputBusVolume

修改角色发出的声音音量
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| Volume | `number` | 音量大小 |

**Return**

_None_

### SetEightWayUniformSpeedEnabled

设置八向移动相同速度
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| Enable | `boolean` | 是否启用 |

**Return**

_None_

### SetUpSubViewTargetServer

设置ViewTarget
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `PlayerPawn` | 角色 |
| bSetUp | `boolean` | 是否启用 |
| TargetActor | [AActor](./AActor.md) | 是否启用 |
| BlendTime | `number` | 缓动时间 |

**Return**

_None_

### PickUpWrapperActor

拾取地面物品
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| TargetWrapper | [AActor](./AActor.md) | 目标地面拾取物 |
| ItemData | `FPickUpItemData` | 拾取物品数据（可通过 WrapperActor:GetDataList() 获取） |
| PickupCount | `number` | 拾取数量 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

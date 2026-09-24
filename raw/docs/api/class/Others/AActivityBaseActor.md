# AActivityBaseActor

可实现可交互物基础功能的Actor

## Parents

- AUAERegionActor
- IOwnBlackboardInterface
- IPlayerLogicInterface
- IRelativeMoveMgrInterface
- IDamageableInterface
- IActivityStateInterface
- IGameplayTaskOwnerInterface
- INetContainerterface
- IClientConditionInerterface
- IObjectPoolInterface
- IInteractorInterface
- IUnifiedInteractionInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OnActivityActorChangeState | `FActivityChangeState` | 状态变化事件委托<br>	 @param LeaveState 离开的状态 名<br>	 @param EnterState 进入的状态名 |

## Functions

### GetCurrentStateName

生效范围：SC
	  获取当前状态名

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentStateTime

生效范围：SC
	  获取进入当前状态后所经过的时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### JumpToState

生效范围：S
	  跳转到指定状态

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StateName | `FName` | 要跳转的状态名 |
| EnterTime | `float` | 进入状态的时间 |
| bPause | `bool` | 是否暂停 |

**Return**

- Type: 
- Description: _None_

### Pause

生效范围：S
	  暂停当前状态的sequence的播放

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Resume

生效范围：S
	  恢复当前状态的sequence的播放

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheckCurrentStateIsEntry

生效范围：SC
	  检查当前状态是否为状态机的入口状态

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentSequnceIsEnd

生效范围：SC
	  检查当前sequence是否播放完毕

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnEnterState_BP |  | 进入某个状态触发 |
| OnPlayerAttachedToThisActor_BP |  | 当角色Attach到这个Actor时触发 |
| OnPlayerBeforeAttachedToThisActor_BP |  | 当角色Attach到这个Actor前触发 |
| OnPlayerDettachedToThisActor_BP |  | 当角色从Actor上Detach时触发 |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnPlayerAttachedDelegate |  | 角色Attach事件委托 |
| OnPlayerDettachedDelegate |  | 角色Detach事件委托 |

## Language

cpp

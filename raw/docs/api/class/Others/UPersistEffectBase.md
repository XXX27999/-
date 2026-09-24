# UPersistEffectBase

PersistEffectBase, PersistEffectSkill和PersistEffectBuff的基类

## Parents

- UBasicPersistEffect
- IGameplayTaskOwnerInterface
- ILimitationInterface
- IOwnershipChainInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bPersistOnUnapply | `bool` | Unapply 时是否缓存到 PlayerState 上的 PersistEffectCacheComponent，<br>	  下次同类型 Apply 会取回并触发 OnRecover |

## Functions

### HasAuthority

检查当前对象是否运行在服务器端
	  生效范围: 服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsAutonomous

检查当前对象是否运行在主控客户端
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bConsiderObReplay | `bool` | 是否包含观战和回放时的主控端 |

**Return**

- Type: 
- Description: _None_

### RefreshValidTime

刷新PersistEffect的生效时间
	  生效范围: 服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTickEnable

设置PersistEffect是否每帧执行Tick函数，在服务器调用只会开启服务器的Tick，在客户端调用只会开启客户端的Tick
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetApplyTime

设置PersistEffect的生效时间
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetApplyTime

获取PersistEffect的生效时间
	  生效范围: 服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTimeStamp

获取当前服务器时间戳
	  生效范围: 服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasTag

检查当前技能或Buff是否有某个类型的Tag
	  生效范围SC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 要检查的Tag |

**Return**

- Type: 
- Description: _None_

### GetRemainingTime

获取剩余时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPersistOnUnapply

运行时动态修改 bPersistOnUnapply。仅服务端生效，不 Replicated。
	  可在 OnApply  Tick  OnUnApply_BP 等任意服务端时机调用。

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInPersistOnUnapply | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ShouldPersistOnUnapply

读取当前 bPersistOnUnapply (含运行时修改值)。

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOwnerActor

获取PersistEffect所属的Actor
	  生效范围: 服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOwnerComponent

获取PersistEffect所属的组件
	  生效范围: 服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnApply_BP |  | 当PersistEffect挂载到角色身上时调用<br>	  生效范围: 服务器&客户端 |
| OnUnApply_BP |  | 当PersistEffect从角色身上移除时调用<br>	  生效范围: 服务器&客户端 |
| CanApply_BP |  | 当PersistEffect挂载到角色身上前检查是否可挂载时调用<br>	  生效范围: 服务器 |
| OnMerge_BP |  | 当PersistEffect合并时调用<br>	  生效范围: 服务器 |
| CanMerge_BP |  | 当PersistEffect合并前检查是否可合并时调用<br>	  生效范围: 服务器 |
| OnRecover_BP |  | 当PersistEffect从缓存中恢复使用<br>	  生效范围: 服务器 |
| Tick_BP |  | PersistEffect每帧调用，开启Tick需要SetTickEnable(true)<br>	  生效范围: 服务器&客户端 |
| OnInterrupted_BP |  | 当PersistEffect被打断时调用<br>	  生效范围: 服务器 |

## Delegate

_None_

## Language

cpp

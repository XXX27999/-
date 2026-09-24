# UPersistBaseComponent

技能Buff组件

## Parents

- [UGameplayTasksComponent](./UGameplayTasksComponent.md)
- IObjectPoolInterface

## Variables

_None_

## Functions

### RegisterPersistEffectWithSlot

生效范围：服务器
	  将PersistEffect注册到目标槽位中

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Slot | `FGameplayTag` | 槽位 |
| InPE | `UPersistEffectBase *` | 注册到槽位的PersistEffect |
| bShouldUnapply | `bool` | 是否将原来槽位上的PersistEffect进行Unapply |

**Return**

- Type: 
- Description: _None_

### UnRegisterPersistEffectWithSlot

生效范围：服务器
	  将目标槽位中的PersistEffect解除注册

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Slot | `FGameplayTag` | 槽位 |
| bShouldUnapply | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPersistEffectBySlot

生效范围：服务器&客户端
	  获取目标槽位中的PersistEffect

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Slot | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 槽位 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| DynamicStateEnterHandle |  | Event<br>	  生效范围：服务器&客户端<br>	  进入状态事件, 注意：服务端DynamicState是有计数的, 服务端多次EnterDynamicState都会触发这个代理 |
| DynamicStateLeaveHandle |  | Event<br>      生效范围：服务器&客户端<br>      离开状态事件, 注意：服务端DynamicState是有计数的, 服务端多次LeaveDynamicState都会触发这个代理, 只有当前计数为0时再Leave就不会触发 |
| DynamicStateInterruptedHandle |  | Event<br>	  生效范围：服务器&客户端<br>	  打断状态事件 |
| DynamicStateInterruptedWithSourceHandle |  | Event<br>	  生效范围：服务器<br>	  打断状态事件 |
| DynamicStateDisabledChangedHandle |  | Event<br>	  生效范围：服务器&客户端<br>	  禁用状态事件 |
| DynamicStateDisabledResetHandle |  | Event<br>	  生效范围：服务器&客户端<br>	  重置禁用状态事件 |

## Language

cpp

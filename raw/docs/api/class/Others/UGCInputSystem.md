# UGCInputSystem

输入系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### BindInputMapping

绑定指定InputTag事件的回调函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BindingOwner | [UObject](./UObject.md) | 绑定输入事件的对象 |
| InputTag | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |
| TriggerEvent | [ETriggerEvent](../../cppenum/E/ET/ETriggerEvent.md) | 输入事件类型 |
| CallbackFunction | `fun(InputValue:float, ElapsedTime:float, TriggeredTime:float, InputTag:FGameplayTag) @事件触发回调函数` | 事件触发回调函数 |

**Return**

- Type: 
- Description: _None_

### RemoveBindingToObject

解除与目标Object所有相关的输入事件绑定
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BindingOwner | [UObject](./UObject.md) | 绑定输入事件的对象 |

**Return**

_None_

### RemoveBinding

解除指定索引的输入事件绑定
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| InputBindingHandle | `int32` | 输入事件绑定的索引 |

**Return**

_None_

### InjectInputMapping

通过脚本手动触发某个InputTag
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| InputTag | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |
| Value | `float` | 输入事件的值 |

**Return**

_None_

### SetBindingConsumeInput

设置某个输入事件绑定是否消耗输入，消耗输入后，后续的其他输入事件绑定将不被触发
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| InputBindingHandle | `int32` | 输入事件绑定的索引 |
| bConsumeInput | `bool` | 是否消耗Input |

**Return**

_None_

### GetInputValue

获取指定InputTag对应Input的当前值
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 世界上下文对象 |
| InputTag | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

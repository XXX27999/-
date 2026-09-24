# ULuaMulticastDelegate

UE 多播委托基类，用于绑定多个回调函数

## Parents

_None_

## Variables

_None_

## Functions

### Add

添加回调，Func 作为 Key 去重，同 Func 不同 Obj 会覆盖

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callback | `function` | 回调函数，如果绑定了 Obj，则 Obj 作为回调第一个参数传入 |
| Obj | `any` | 可选的绑定对象，作为回调第一个参数传入 |

**Return**

- Type: 
- Description: _None_

### AddInstance

添加回调，Func && Obj 共同作为 Key 去重，同 Func 不同 Obj 会共存

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callback | `function` | 回调函数，Obj 作为回调第一个参数传入 |
| Obj | `any` | 绑定对象，作为回调第一个参数传入 |

**Return**

- Type: 
- Description: _None_

### Remove

移除指定回调

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callback | `function` | 要移除的回调函数 |
| Obj | `any` | 可选的绑定对象 |

**Return**

_None_

### RemoveAll

移除所有 Lua 绑定

**Parameters**

_None_

**Return**

_None_

### Clear

移除所有绑定（C++/BP/Lua）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDonotKeepThis | `boolean` | 是否不保留当前对象的回调 |

**Return**

_None_

### Broadcast

触发 Lua 广播

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ... | `any` | 委托参数 |

**Return**

_None_

### BroadcastAll

触发所有广播（C++/BP/Lua）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ... | `any` | 委托参数 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

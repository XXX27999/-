# ULuaSingleDelegate

UE 单播委托基类，用于绑定单个回调函数，后绑定会覆盖先绑定

## Parents

_None_

## Variables

_None_

## Functions

### Bind

绑定回调函数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callback | `function` | 回调函数，如果绑定了 Obj，则 Obj 作为回调第一个参数传入 |
| Obj? | `any` | 可选的绑定对象，作为回调第一个参数传入 |

**Return**

- Type: 
- Description: _None_

### UnBind

解绑回调函数

**Parameters**

_None_

**Return**

_None_

### Execute

执行委托，触发已绑定的回调

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

# UGCCommonDelegate

UGC通用委托

## Parents

_None_

## Variables

_None_

## Functions

### Add

添加回调

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callback | `function` | 回调函数 |
| CallbackOwner | `any` | 回调函数所有者，可不传 |

**Return**

_None_

### Remove

移除回调

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callback | `function` | 回调函数 |
| CallbackOwner | `any` | 回调函数所有者，可不传 |

**Return**

_None_

### RemoveAll

移除所有回调

**Parameters**

_None_

**Return**

_None_

### Broadcast

广播事件，会根据委托类型进行不同的处理
可以直接用函数调用的方式触发广播，例如`CommonDelegate(1, 2, 3)`

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ... | `any` | 事件参数 |

**Return**

_None_

### ToUEDelegate

转换为UE的单播委托，可以传递给需要UE单播委托的接口

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Outer | [UObject](./UObject.md) | Outer 对象（GC 相关） |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

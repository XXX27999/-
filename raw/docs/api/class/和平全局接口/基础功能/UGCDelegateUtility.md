# UGCDelegateUtility

UGC 委托工具库

Lua 委托工具
- 使用 New() 创建委托
- 使用 Add(callable, obj) 绑定可调用对象
- 使用 Remove(callable, obj) 解绑可调用对象
- 使用 Broadcast(...) 触发委托

## Parents

_None_

## Variables

_None_

## Functions

### CreateLuaDelegate

创建 Lua 委托（纯 Lua 实现）

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CopyLuaDelegate

复制 Lua 委托

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delegate | `UGCLuaDelegate` | 被复制的 Lua 委托 |

**Return**

- Type: 
- Description: _None_

### CreateUEDelegate

创建虚幻兼容单播委托

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Outer | [UObject](../../Others/UObject.md) | Outer 对象（GC 相关） |

**Return**

- Type: 
- Description: _None_

### DestroyUEDelegate

销毁虚幻兼容单播委托

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UEDelegate | [ULuaSingleDelegate](../../Others/ULuaSingleDelegate.md) | 虚幻兼容单播委托 |

**Return**

_None_

### CreateCommonDelegate

创建通用委托

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Type | [EUGCCommonDelegateType](../../../cppenum/E/EU/EUGCCommonDelegateType.md) | 委托类型，不传则默认为普通委托 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

# UGCTimerUtility

计时器工具类

## Parents

_None_

## Variables

_None_

## Functions

### CreateLuaTimer

创建 Lua 计时器
 1. TimeOffset > 0，则 TimeOffset 单位是秒。
 2. TimeOffset == 0，遇到 tick 就会执行。
 3. TimeOffset < 0，是负数如 -N 的话，会在间隔 N 帧后执行第一次。如果传入了 InitDelay，则此条略过，按下面 InitDelay 参数说明来执行：
  a) 如果 InitDelay ~= nil(即传入 InitDelay 参数)，则计时器会在 InitDelay 秒后执行第一次；后面根据 TimeOffset 的设置，循环调用。
  b) 如果 InitDelay == 0，则 InsertTimer 时，会立即执行第一次；后面根据 TimeOffset 的设置，循环调用。
  c) 如果 InitDelay == nil(即未传入 InitDelay 参数)，则会在 TimeOffset 后，执行第一次；后面根据 TimeOffset 的设置，循环调用。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeOffset | `number` | 间隔时间 |
| Callback | `function` | 回调函数 |
| bLoop | `boolean` | 是否循环 |
| TimerName | `string` | 计时器名称 |
| InitDelay | `number` | 第一次执行延迟时间 |
| bLog | `boolean` | 是否记录日志 |
| bCoroutine | `boolean` | 是否是协程 |

**Return**

- Type: 
- Description: _None_

### RemoveLuaTimer

移除 Lua 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimerInstance | `UGCLuaTimerInstance` | 计时器实例 |

**Return**

_None_

### RemoveLuaTimerByName

根据名称移除 Lua 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimerName | `string` | 计时器名称 |

**Return**

_None_

### IsLuaTimerExistByName

根据名称判断 Lua 计时器是否存在
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimerName | `string` | 计时器名称 |

**Return**

- Type: 
- Description: _None_

### CreateUETimer

设置 UE 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CallbackFunction | `LuaFunction` | Lua 回调函数 |
| Time | `number` | 定时时长 |
| IsLooping | `boolean` | 是否循环 |

**Return**

- Type: 
- Description: _None_

### RemoveUETimer

移除 UE 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimerHandle | [FTimerHandle](../../../cppstruct/F/FT/FTimerHandle.md) | 计时器句柄 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

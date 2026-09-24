# PromiseFuture

提供处理异步操作的类，支持链式调用和状态管理

说明：
- 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
- 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
- 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
- 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
- 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

## Parents

_None_

## Variables

_None_

## Functions

### Resume

手动恢复 PromiseFuture 的执行

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ... | `any` | 可选的参数，将传递给恢复的协程 |

**Return**

- Type: 
- Description: _None_

### IsPrerequisitesEstablished

检查所有先决条件是否已建立

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsAnyPrerequisiteCancellationRequested

检查任意先决条件是否已被取消

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsEstablished

检查当前 PromiseFuture 是否已建立

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### WaitForPrerequisites

等待所有前置条件变为已建立状态
如果前置条件未完成，则会自动 Yield
只能在 Set 回调函数中使用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddPrerequisites

添加前置条件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Prerequisite | [PromiseFuture](./PromiseFuture.md) | 前置条件 |

**Return**

- Type: 
- Description: _None_

### IsCancellationRequested

检查当前 PromiseFuture 是否已被取消

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetError

获取协程异常时保存的原始错误对象
主动 Cancel 时返回 nil；协程内业务异常时返回 error 值
可与 IsCancellationRequested 配合区分失败原因：
  IsCancellationRequested()==true 且 GetError()==nil  → 主动 Cancel
  IsCancellationRequested()==true 且 GetError()~=nil  → 协程内抛出的业务异常

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Cancel

取消当前 PromiseFuture 的执行

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CancelAll

取消当前 PromiseFuture 及其所有前置条件的执行

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Get

获取 Set 回调函数的返回值
只能在 Set、Then 回调函数中使用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Then

设置成功回调函数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callable | `function` | 回调函数 |
| ... | `any` | 可选的参数，将传递给回调函数 |

**Return**

- Type: 
- Description: _None_

### Else

设置失败回调函数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Callable | `function` | 回调函数 |
| ... | `any` | 可选的参数，将传递给回调函数 |

**Return**

- Type: 
- Description: _None_

### Set

设置执行逻辑

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Setter | `function` | 回调函数 |
| SetterValue | `any` |  |
| ... | `any` | 其他可选参数 |

**Return**

- Type: 
- Description: _None_

### Yield

暂停当前 PromiseFuture 的执行
只能在 Set 回调函数中使用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ... | `any` | 可选的参数，将传递给 yield(...) 方法 |

**Return**

- Type: 
- Description: _None_

### AutoResume

设置自动恢复功能

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WatchedObject | [UObject](../../Others/UObject.md) | 监控的对象，如果对象被销毁则停止自动恢复 |
| Interval | `number` | 自动恢复的间隔，单位为秒 |
| Timeout | `number` | 自动恢复的超时时间，单位为秒 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

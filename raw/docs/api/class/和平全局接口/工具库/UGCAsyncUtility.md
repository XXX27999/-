# UGCAsyncUtility

异步工具类

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCAsyncUtility.CoroutineManager |  |  |

## Functions

### CreatePromiseFuture

创建一个新的 PromiseFuture 实例
 - 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
 - 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
 - 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
 - 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
 - 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Prerequisite | `UGCPromiseFuture` | 可选的前置条件 PromiseFuture 实例 |
| ... | `any` | 其他可选的前置条件 |

**Return**

- Type: 
- Description: _None_

### NewSequenceList

新建一个保序列表，并返回ListHandle用于操作

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### InsertItemIntoSequenceList

往List里添加变量和函数。激活后时序逻辑为：轮询变量是否为空或者函数是否返回true，当变量不为空的时候，执行对应的函数，所以每次Insert一组变量和函数，就相当于添加一个时序逻辑。

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListHandle | `UGCAsyncSequenceHandle` | 保序列表的索引 |
| ParamIndex | `number` | 参数插入保序列表的位置，如果是0，则是插入到列表的尾部 |
| InConditionFunction | `any` | 可执行的Function或变量 |
| InConditionTable | `table` | 轮询变量或函数所在的Table |
| InFunction | `function@` | 当条件为true时执行的函数 |
| InFunctionTable | `table` | 当条件为true时执行函数的Table |
| ... | `any` | 可变参数，当条件为true时执行的函数参数 |

**Return**

_None_

### ActivateSequenceList

激活保序列表

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListHandle | `UGCAsyncSequenceHandle` | 保序列表的索引 |
| Interval | `number` | 自动恢复的间隔，单位为秒 |
| Timeout | `number` | 自动恢复的超时时间，单位为秒 |

**Return**

_None_

### AsyncLoadSomething

支持并行初始化的通用有序异步加载器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AsyncFun | `function` | 需要调用的异步函数（格式：func(LoadPath, CallBack, CallBack_Self)） |
| ParamTables | `UGCAsyncSequenceParamTable[]` | 参数表数组 |
| OnCompleteCallback | `function` | 最终回调(loadedObjects) |

**Return**

- Type: 
- Description: _None_

### AsyncRun

启动一个未驱动的 PromiseFuture（相当于 Python asyncio.run）
接收 AsyncDefine(...) 返回的 AsyncFunc 调用得到的未驱动 PF，挂上 AutoResume 启动驱动
如果 PF 已驱动或已 establish，**静默跳过**

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PF | `UGCPromiseFuture` | 通常是 AsyncDefine(Fn)(...) 返回的未驱动的 UGCPromiseFuture |
| Opts | `UGCAsyncOptions` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

**Return**

- Type: 
- Description: _None_

### AsyncDefine

定义一个 async 函数（相当于 Python 的 async def）
返回 AsyncFunc：调用 AsyncFunc(...) 返回**未驱动**的 PromiseFuture
未驱动 PF 不会自动推进，需要显式 AsyncRun(pf, opts) 启动，或在 Async 上下文内被 Await/AwaitAll/AwaitAny 等消费

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Fn | `function` | async 函数体，签名为 function(...) ... end |

**Return**

- Type: 
- Description: _None_

### AsyncSelf

获取当前 Async 任务的 PromiseFuture（仅在 Async 协程内有效）
用于高级场景：手动 AddPrerequisites / Cancel / Yield 等

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Await

在 Async 协程内等待任意 PromiseFuture 完成
任务取消时，抛字符串 error（值 = AsyncErrorType.Cancelled）
可用 AwaitSafe 简写或 pcall/xpcall 自行捕获

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PF | `UGCPromiseFuture` |  |

**Return**

- Type: 
- Description: _None_

### AwaitSafe

在 Async 协程内等待 PromiseFuture 完成的"安全版"——不抛错，返回 (Ok, ...Values 或 Err)
与 lua 原生 pcall 语义对齐：捕获 Await 路径上的**任何** error（取消、超时、业务自抛等）
成功时返回 (true, ...Values)
失败时返回 (false, Err)：
  * 取消：Err == AsyncErrorType.Cancelled（字符串）
  * 超时：Err == AsyncErrorType.Timeout（字符串，由 WaitFor 抛出）
  * 其它：Err 为原始 error 值（业务自抛的 string/table/任意值）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PF | `UGCPromiseFuture` |  |

**Return**

- Type: 
- Description: _None_

### AsyncSleep

在 Async 协程内暂停指定秒数
Seconds <= 0 时也会让出协程一次（"让出一帧"语义）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Seconds | `number` |  |

**Return**

_None_

### AwaitAll

等待一组 PromiseFuture 全部完成；任一被取消或发生业务异常即整体抛 error（table 形式，含 Err/Index/Values）
其中 Err 字段：主动 Cancel 时为 AsyncErrorType.Cancelled 字符串；业务异常时为原始 error 对象

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PFs | `UGCPromiseFuture[]` |  |

**Return**

- Type: 
- Description: _None_

### AwaitAllSettled

等待一组 PromiseFuture 全部"沉淀"（完成或取消都算）；**永不抛错**
与 AwaitAll 的区别：任一项失败不会中断/抛错，每项的成败状态独立返回
适合"局部容错、各项失败互不影响"场景（对齐 JS Promise.allSettled）
返回数组与传入任务顺序一一对应，每项形如：

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PFs | `UGCPromiseFuture[]` |  |

**Return**

_None_

### AwaitAny

等待一组 PromiseFuture，任一完成即返回；其余被 Cancel
若全部被取消/异常则抛字符串 error（值 = AsyncErrorType.Cancelled）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PFs | `UGCPromiseFuture[]` |  |

**Return**

- Type: 
- Description: _None_

### WaitFor

在 Async 协程内等待 PromiseFuture 完成，并施加单点超时（相当于 Python asyncio.wait_for）
在 Seconds 内任务未完成时，对任务 Cancel 并抛字符串 error（值 = AsyncErrorType.Timeout）
任务先被别人 Cancel 时抛 AsyncErrorType.Cancelled，不覆盖为 Timeout
精度受外层 AutoResume 的 Interval 限制：要求精确计时请保证 Opts.Interval = 0

与 AsyncRun 的 Timeout 区别：
  * AsyncRun({ Timeout = N })  ：整个任务的总超时
  * WaitFor(PF, N)             ：单个 await 点的局部超时

用法：
  local Icon = UGCAsyncUtility.WaitFor(LoadIcon(Path), 5)
  local Ok, Err = UGCAsyncUtility.WaitForSafe(LoadIcon(Path), 5)
  if not Ok and Err == AsyncErrorType.Timeout then ... end

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PF | `UGCPromiseFuture` |  |
| Seconds | `number` |  |

**Return**

- Type: 
- Description: _None_

### WaitForSafe

WaitFor 的"安全版"——不抛错，返回 (Ok, ...Values 或 Err)
成功时返回 (true, ...Values)
失败时返回 (false, Err)：Err 为字符串 AsyncErrorType.Cancelled / AsyncErrorType.Timeout，或业务自抛的原始 error 值

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PF | `UGCPromiseFuture` |  |
| Seconds | `number` |  |

**Return**

- Type: 
- Description: _None_

### AsyncFromEvent

把 Delegate 风格的事件订阅转换为**未驱动**的 PromiseFuture
事件触发一次后自动 Remove，PF 携带事件参数 establish
必须在 Async 上下文内 Await（或经 AsyncRun 启动）才会生效
超时需求请用 WaitFor 包装：UGCAsyncUtility.WaitFor(UGCAsyncUtility.AsyncFromEvent(D), 30)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EventDelegate | [Delegate](../基础功能/Delegate.md) |  |

**Return**

- Type: 
- Description: _None_

### AsyncFromCallback

把"传 callback"风格的函数封装为**未驱动**的 PromiseFuture
用法：AsyncFromCallback(SomeAPI, Arg1, Arg2)，SomeAPI 的最后一个参数应当是 callback
必须在 Async 上下文内 Await（或经 AsyncRun 启动）才会生效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Fn | `function` | 接受 callback 作为最后一个参数的函数 |
| ... | `any` | 透传给 Fn 的前置参数 |

**Return**

- Type: 
- Description: _None_

### AsyncCall

异步调用函数，直到 CheckFunction 返回 true 时停止调用，然后执行 Callback 函数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CallFunction | `function` | 调用函数 |
| Callback | `function` | 回调函数 |
| CheckFunction | `function` | 检查函数 |
| Opts | `UGCAsyncOptions` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

**Return**

- Type: 
- Description: _None_

### AsyncIfThen

异步调用函数，直到IfFunction返回true时执行ThenFunction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IfFunction | `function` | 条件函数，返回 true 时执行 ThenFunction |
| ThenFunction | `function` | 条件满足时执行的函数 |
| Opts | `UGCAsyncOptions` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

**Return**

- Type: 
- Description: _None_

### AsyncIfThenElse

异步调用函数，直到IfFunction返回true时执行ThenFunction，其他情况执行ElseFunction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IfFunction | `function` | 条件函数，返回 true 时执行 ThenFunction，超时/取消时执行 ElseFunction |
| ThenFunction | `function` | 条件满足时执行的函数 |
| ElseFunction | `function` | 超时或取消时执行的函数 |
| Opts | `UGCAsyncOptions` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

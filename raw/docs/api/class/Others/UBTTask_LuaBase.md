# UBTTask_LuaBase

Base class for lua based task nodes. Do NOT use it for creating native c++ classes!

   When task receives Abort event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Execute, but does not handle external events.
   Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

## Parents

- [UBTTaskNode](./UBTTaskNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AIOwner | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| bShowPropertyDetails | `uint32` | show detailed information about properties |

## Functions

### ReceiveExecuteAI

entry point, task will stay active until FinishExecute is called.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveAbortAI

if blueprint graph contains this event, task will stay active until FinishAbort is called

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveTickAI

tick function

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |
| DeltaSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### FinishExecute

finishes task execution with Success or Fail result

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bSuccess | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FinishAbort

aborts task execution

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFinishOnMessage

task execution will be finished (with result 'Success') after receiving specified message

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MessageName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetFinishOnMessageWithId

task execution will be finished (with result 'Success') after receiving specified message with indicated ID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MessageName | `FName` |  |
| RequestID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### IsTaskExecuting

check if task is currently being executed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsTaskAborting

check if task is currently being aborted

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

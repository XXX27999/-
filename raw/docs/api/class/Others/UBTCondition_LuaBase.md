# UBTCondition_LuaBase

Base class for lua based condition nodes. Do NOT use it for creating native c++ classes!

   Unlike task and attachments, condition have two execution chains:
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).

   Helper functions:
   - IsConditionExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsConditionObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AIOwner | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| ObservedKeyNames | `TArray < FName >` | blackboard key names that should be observed |
| bCheckConditionOnlyBlackBoardChanges | `uint32` | Applies only if Condition has any FBlackboardKeySelector property and if condition is<br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes<br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |
| bIsObservingBB | `uint32` | gets set to true if condition declared BB keys it can potentially observe |

## Functions

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

### ReceiveExecutionStartAI

called on execution of underlying node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveExecutionFinishAI

called when execution of underlying node is finished

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |
| NodeResult | `EBTNodeResult :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveObserverActivatedAI

called when observer is activated (flow controller)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveObserverDeactivatedAI

called when observer is deactivated (flow controller)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### PerformConditionCheckAI

called when testing if underlying node can be executed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### IsConditionExecutionActive

check if condition is part of currently active branch

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsConditionObserverActive

check if condition's observer is currently active

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

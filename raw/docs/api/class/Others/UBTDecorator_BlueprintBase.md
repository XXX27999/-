# UBTDecorator_BlueprintBase

Base class for blueprint based decorator nodes. Do NOT use it for creating native c++ classes!

   Unlike task and services, decorator have two execution chains:
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).

   Helper functions:
   - IsDecoratorExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsDecoratorObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AIOwner | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| ActorOwner | `AActor *` | Cached AIController owner of BehaviorTreeComponent. |
| ObservedKeyNames | `TArray < FName >` | blackboard key names that should be observed |
| bShowPropertyDetails | `uint32` | show detailed information about properties |
| bCheckConditionOnlyBlackBoardChanges | `uint32` | Applies only if Decorator has any FBlackboardKeySelector property and if decorator is<br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes<br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |
| bIsObservingBB | `uint32` | gets set to true if decorator declared BB keys it can potentially observe |

## Functions

### ReceiveTick

tick function

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |
| DeltaSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveExecutionStart

called on execution of underlying node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveExecutionFinish

called when execution of underlying node is finished

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |
| NodeResult | `EBTNodeResult :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveObserverActivated

called when observer is activated (flow controller)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveObserverDeactivated

called when observer is deactivated (flow controller)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### PerformConditionCheck

called when testing if underlying node can be executed, must call FinishConditionCheck

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveTickAI

Alternative AI version of ReceiveTick

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

Alternative AI version of ReceiveExecutionStart

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveExecutionFinishAI

Alternative AI version of ReceiveExecutionFinish

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

Alternative AI version of ReceiveObserverActivated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveObserverDeactivatedAI

Alternative AI version of ReceiveObserverDeactivated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### PerformConditionCheckAI

Alternative AI version of ReceiveConditionCheck

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### IsDecoratorExecutionActive

check if decorator is part of currently active branch

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsDecoratorObserverActive

check if decorator's observer is currently active

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

# UBTService_BlueprintBase

Base class for blueprint based service nodes. Do NOT use it for creating native c++ classes!

   When service receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsServiceActive() when in doubt.

## Parents

- [UBTService](./UBTService.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AIOwner | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| ActorOwner | `AActor *` | Cached actor owner of BehaviorTreeComponent. |
| bShowPropertyDetails | `uint32` | show detailed information about properties |
| bShowEventDetails | `uint32` | show detailed information about implemented events |

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

### ReceiveSearchStart

task search enters branch of tree

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActivation

service became active

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveDeactivation

service became inactive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveTickAI

Alternative AI version of ReceiveTick function.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |
| DeltaSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveSearchStartAI

Alternative AI version of ReceiveSearchStart function.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActivationAI

Alternative AI version of ReceiveActivation function.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveDeactivationAI

Alternative AI version of ReceiveDeactivation function.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerController | `AAIController *` |  |
| ControlledPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### IsServiceActive

check if service is currently being active

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

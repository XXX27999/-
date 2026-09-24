# UBrainComponent

## Parents

- [UActorComponent](./UActorComponent.md)
- IAIResourceInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BlackboardComp | `UBlackboardComponent *` | blackboard component |
| AIOwner | `AAIController *` |  |

## Functions

### RestartLogic

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopLogic

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reason | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### PauseLogic

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reason | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ResumeLogic

MUST be called by child implementations!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reason | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### IsRunning

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPaused

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

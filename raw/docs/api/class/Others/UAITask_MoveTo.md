# UAITask_MoveTo

## Parents

- [UAITask](./UAITask.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OnRequestFailed | `FGenericGameplayTaskDelegate` |  |
| MoveRequest | [FAIMoveRequest](../../cppstruct/F/FA/FAIMoveRequest.md) | parameters of move request |

## Functions

### AIMoveTo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AAIController *` |  |
| GoalLocation | `FVector` |  |
| GoalActor | `AActor *` |  |
| AcceptanceRadius | `float` |  |
| StopOnOverlap | `EAIOptionFlag :: Type` |  |
| AcceptPartialPath | `EAIOptionFlag :: Type` |  |
| bUsePathfinding | `bool` |  |
| bLockAILogic | `bool` |  |
| bUseContinuosGoalTracking | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnMoveFinished |  |  |

## Language

cpp

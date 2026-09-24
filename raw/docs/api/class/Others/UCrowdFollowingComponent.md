# UCrowdFollowingComponent

## Parents

- [UPathFollowingComponent](./UPathFollowingComponent.md)
- ICrowdAgentInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CrowdAgentMoveDirection | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| CharacterMovement | `UCharacterMovementComponent *` |  |
| AvoidanceGroup_DEPRECATED | [FNavAvoidanceMask](../../cppstruct/F/FN/FNavAvoidanceMask.md) | DEPRECATED: Group mask for this agent - use property from CharacterMovementComponent instead |
| GroupsToAvoid_DEPRECATED | [FNavAvoidanceMask](../../cppstruct/F/FN/FNavAvoidanceMask.md) | DEPRECATED: Will avoid other agents if they are in one of specified groups - use property from CharacterMovementComponent instead |
| GroupsToIgnore_DEPRECATED | [FNavAvoidanceMask](../../cppstruct/F/FN/FNavAvoidanceMask.md) | DEPRECATED: Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid - use property from CharacterMovementComponent instead |

## Functions

### SuspendCrowdSteering

master switch for crowd steering & avoidance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bSuspend | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

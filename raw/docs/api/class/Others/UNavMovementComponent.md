# UNavMovementComponent

NavMovementComponent defines base functionality for MovementComponents that move any 'agent' that may be involved in AI pathfinding.

## Parents

- [UMovementComponent](./UMovementComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NavAgentProps | [FNavAgentProperties](../../cppstruct/F/FN/FNavAgentProperties.md) | Properties that define how the component can move. |
| FixedPathBrakingDistance | `float` | Braking distance override used with acceleration driven path following (bUseAccelerationForPaths) |
| bUpdateNavAgentWithOwnersCollision | `uint32` | If set to true NavAgentProps' radius and height will be updated with Owner's collision capsule size |
| bUseAccelerationForPaths | `uint32` | If set, pathfollowing will control character movement via acceleration values. If false, it will set velocities directly. |
| bUseFixedBrakingDistanceForPaths | `uint32` | If set, FixedPathBrakingDistance will be used for path following deceleration |
| MovementState | [FMovementProperties](../../cppstruct/F/FM/FMovementProperties.md) | Expresses runtime state of character's movement. Put all temporal changes to movement properties here |

## Functions

### StopActiveMovement

Stops applying further movement (usually zeros acceleration).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopMovementKeepPathing

Stops movement immediately (reset velocity) but keeps following current path

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsCrouching

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsFalling

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsMovingOnGround

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsSwimming

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsFlying

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

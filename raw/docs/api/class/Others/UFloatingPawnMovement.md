# UFloatingPawnMovement

FloatingPawnMovement is a movement component that provides simple movement for any Pawn class.
  Limits on speed and acceleration are provided, while gravity is not implemented.

  Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
  During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

## Parents

- [UPawnMovementComponent](./UPawnMovementComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxSpeed | `float` | Maximum velocity magnitude allowed for the controlled Pawn. |
| Acceleration | `float` | Acceleration applied by input (rate of change of velocity) |
| Deceleration | `float` | Deceleration applied when there is no input (rate of change of velocity) |
| TurningBoost | `float` | Setting affecting extra force applied when changing direction, making turns have less drift and become more responsive.<br>	  Velocity magnitude is not allowed to increase, that only happens due to normal acceleration. It may decrease with large direction changes.<br>	  Larger values apply extra force to reach the target direction more quickly, while a zero value disables any extra turn force. |
| FloatingMoveSpeedScale | `float` | Engine Modify Start<br><br>	 Maximum velocity magnitude allowed for the controlled Pawn. |
| bPositionCorrected | `uint32` | Set to true when a position correction is applied. Used to avoid recalculating velocity when this occurs. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

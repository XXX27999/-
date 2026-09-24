# URotatingMovementComponent

Performs continuous rotation of a component at a specific rotation rate.
  Rotation can optionally be offset around a pivot point.
  Collision testing is not performed during movement.

## Parents

- [UMovementComponent](./UMovementComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RotationRate | [FRotator](../../cppstruct/F/FR/FRotator.md) | How fast to update rollpitchyaw of the component we update. |
| PivotTranslation | [FVector](../../cppstruct/F/FV/FVector.md) | Translation of pivot point around which we rotate, relative to current rotation.<br>	  For instance, with PivotTranslation set to (X=+100, Y=0, Z=0), rotation will occur<br>	  around the point +100 units along the local X axis from the center of the object,<br>	  rather than around the object's origin (the default). |
| bRotationInLocalSpace | `uint32` | Whether rotation is applied in local or world space. |
| bCirculatingRotation | `bool` |  |
| RotationAngle | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| OriginRotator | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| bCircleFlag | `bool` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

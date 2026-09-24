# AInteractiveFoliageActor

## Parents

- [AStaticMeshActor](./AStaticMeshActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CapsuleComponent | `UCapsuleComponent *` | Collision cylinder |
| TouchingActorEntryPosition | [FVector](../../cppstruct/F/FV/FVector.md) | Position of the last actor to enter the collision cylinder.<br>	  This currently does not handle multiple actors affecting the foliage simultaneously. |
| FoliageVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | Simulated physics state |
| FoliageForce | [FVector](../../cppstruct/F/FV/FVector.md) | @todo document |
| FoliagePosition | [FVector](../../cppstruct/F/FV/FVector.md) | @todo document |
| FoliageDamageImpulseScale | `float` | Scales forces applied from damage events. |
| FoliageTouchImpulseScale | `float` | Scales forces applied from touch events. |
| FoliageStiffness | `float` | Determines how strong the force that pushes toward the spring's center will be. |
| FoliageStiffnessQuadratic | `float` | Same as FoliageStiffness, but the strength of this force increases with the square of the distance to the spring's center.<br>	  This force is used to prevent the spring from extending past a certain point due to touch and damage forces. |
| FoliageDamping | `float` | Determines the amount of energy lost by the spring as it oscillates.<br>	  This force is similar to air friction. |
| MaxDamageImpulse | `float` | Clamps the magnitude of each damage force applied. |
| MaxTouchImpulse | `float` | Clamps the magnitude of each touch force applied. |
| MaxForce | `float` | Clamps the magnitude of combined forces applied each update. |
| Mass | `float` |  |

## Functions

### CapsuleTouched

Called when capsule is touched

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OverlappedComp | `UPrimitiveComponent *` |  |
| Other | `AActor *` |  |
| OtherComp | `UPrimitiveComponent *` |  |
| OtherBodyIndex | `int32` |  |
| bFromSweep | `bool` |  |
| OverlapInfo | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

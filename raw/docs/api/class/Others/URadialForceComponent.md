# URadialForceComponent

Used to emit a radial force or impulse that can affect physics objects and or destructible objects.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Radius | `float` | The radius to apply the force or impulse in |
| Falloff | `TEnumAsByte < enum ERadialImpulseFalloff >` | How the force or impulse should fall off as object are further away from the center |
| ImpulseStrength | `float` | How strong the impulse should be |
| bImpulseVelChange | `uint32` | If true, the impulse will ignore mass of objects and will always result in a fixed velocity change |
| bIgnoreOwningActor | `uint32` | If true, do not apply forceimpulse to any physics objects that are part of the Actor that owns this component. |
| ForceStrength | `float` | How strong the force should be |
| DestructibleDamage | `float` | If > 0.f, will cause damage to destructible meshes as well |
| ObjectTypesToAffect | `TArray < TEnumAsByte < enum EObjectTypeQuery > >` | The object types that are affected by this radial force |

## Functions

### FireImpulse

Fire a single impulse

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddObjectTypeToAffect

Add an object type for this radial force to affect

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectType | `TEnumAsByte < enum EObjectTypeQuery >` |  |

**Return**

- Type: 
- Description: _None_

### RemoveObjectTypeToAffect

Remove an object type that is affected by this radial force

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectType | `TEnumAsByte < enum EObjectTypeQuery >` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

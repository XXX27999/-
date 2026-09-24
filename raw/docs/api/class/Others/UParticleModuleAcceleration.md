# UParticleModuleAcceleration

## Parents

- [UParticleModuleAccelerationBase](./UParticleModuleAccelerationBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Acceleration | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The initial acceleration of the particle.<br>	 	Value is obtained using the EmitterTime at particle spawn.<br>	 	Each frame, the current and base velocity of the particle<br>	 	is then updated using the formula<br>	 		velocity += acceleration  DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |
| bApplyOwnerScale | `uint32` | If true, then apply the particle system components scale<br>	 	to the acceleration value. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

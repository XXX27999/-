# UParticleModuleAccelerationOverLifetime

## Parents

- [UParticleModuleAccelerationBase](./UParticleModuleAccelerationBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AccelOverLife | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The acceleration of the particle over its lifetime.<br>	 	Value is obtained using the RelativeTime of the partice.<br>	 	The current and base velocity values of the particle<br>	 	are then updated using the formula<br>	 		velocity += acceleration DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

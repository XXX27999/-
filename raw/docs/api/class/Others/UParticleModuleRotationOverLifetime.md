# UParticleModuleRotationOverLifetime

## Parents

- UParticleModuleRotationBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RotationOverLife | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The rotation of the particle (1.0 = 360 degrees).<br>	 	The value is retrieved using the RelativeTime of the particle. |
| Scale | `uint32` | If true,  the particle rotation is multiplied by the value retrieved from RotationOverLife.<br>	 	If false, the particle rotation is incremented by the value retrieved from RotationOverLife. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

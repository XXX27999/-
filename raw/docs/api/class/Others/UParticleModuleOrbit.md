# UParticleModuleOrbit

## Parents

- [UParticleModuleOrbitBase](./UParticleModuleOrbitBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ChainMode | `TEnumAsByte < enum EOrbitChainMode >` | Orbit modules will chain together in the order they appear in the module stack.<br>	 	The combination of a module with the one prior to it is defined by using one<br>	 	of the following enumerations:<br>	 		EOChainMode_Add		Add the values to the previous results<br>	 		EOChainMode_Scale	Multiply the values by the previous results<br>	 		EOChainMode_Link	'Break' the chain and apply the values from the	previous results |
| OffsetAmount | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The amount to offset the sprite from the particle position. |
| OffsetOptions | [FOrbitOptions](../../cppstruct/F/FO/FOrbitOptions.md) | The options associated with the OffsetAmount look-up. |
| RotationAmount | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The amount (in 'turns') to rotate the offset about the particle position.<br>	 		0.0 = no rotation<br>	 		0.5	= 180 degree rotation<br>	 		1.0 = 360 degree rotation |
| RotationOptions | [FOrbitOptions](../../cppstruct/F/FO/FOrbitOptions.md) | The options associated with the RotationAmount look-up. |
| RotationRateAmount | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The rate (in 'turns') at which to rotate the offset about the particle positon.<br>	 		0.0 = no rotation<br>	 		0.5	= 180 degree rotation<br>	 		1.0 = 360 degree rotation |
| RotationRateOptions | [FOrbitOptions](../../cppstruct/F/FO/FOrbitOptions.md) | The options associated with the RotationRateAmount look-up. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

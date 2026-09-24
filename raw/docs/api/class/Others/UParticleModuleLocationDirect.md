# UParticleModuleLocationDirect

## Parents

- UParticleModuleLocationBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Location | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The location of the particle at a give time. Retrieved using the particle RelativeTime.<br>	 	IMPORTANT: the particle location is set to this value, thereby over-writing any previous module impacts. |
| LocationOffset | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | An offset to apply to the position retrieved from the Location calculation.<br>	 	The offset is retrieved using the EmitterTime.<br>	 	The offset will remain constant over the life of the particle. |
| ScaleFactor | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | Scales the velocity of the object at a given point in the time-line. |
| Direction | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | Currently unused. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UParticleModuleTrailSource

## Parents

- UParticleModuleTrailBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceMethod | `TEnumAsByte < enum ETrail2SourceMethod >` | The source method for the trail. |
| SourceName | `FName` | The name of the source - either the emitter or Actor. |
| SourceStrength | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The strength of the tangent from the source point for each Trail. |
| bLockSourceStength | `uint32` | Whether to lock the source to the life of the particle. |
| SourceOffsetCount | `int32` | SourceOffsetCount<br>	 	The number of source offsets that can be expected to be found on the instance.<br>	 	These must be named<br>	 		TrailSourceOffset# |
| SourceOffsetDefaults | `TArray < FVector >` | Default offsets from the source(s).<br>	 	If there are < SourceOffsetCount slots, the grabbing of values will simply wrap. |
| SelectionMethod | `TEnumAsByte < enum EParticleSourceSelectionMethod >` | Particle selection method, when using the SourceMethod of Particle. |
| bInheritRotation | `uint32` | Interhit particle rotation - only valid for SourceMethod of PET2SRCM_Particle. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

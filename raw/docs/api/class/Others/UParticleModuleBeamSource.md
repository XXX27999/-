# UParticleModuleBeamSource

## Parents

- UParticleModuleBeamBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceMethod | `TEnumAsByte < enum Beam2SourceTargetMethod >` | The method flag. |
| SourceName | `FName` | The strength of the tangent from the source point for each beam. |
| bSourceAbsolute | `uint32` | Whether to treat the as an absolute position in world space. |
| Source | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | Default source-point to use. |
| bLockSource | `uint32` | Whether to lock the source to the life of the particle. |
| SourceTangentMethod | `TEnumAsByte < enum Beam2SourceTargetTangentMethod >` | The method to use for the source tangent. |
| SourceTangent | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The tangent for the source point for each beam. |
| bLockSourceTangent | `uint32` | Whether to lock the source to the life of the particle. |
| SourceStrength | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The strength of the tangent from the source point for each beam. |
| bLockSourceStength | `uint32` | Whether to lock the source to the life of the particle. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

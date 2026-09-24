# UParticleModuleCameraOffset

## Parents

- UParticleModuleCameraBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CameraOffset | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The camera-relative offset to apply to sprite location |
| bSpawnTimeOnly | `uint32` | If true, the offset will only be processed at spawn time |
| UpdateMethod | `TEnumAsByte < enum EParticleCameraOffsetUpdateMethod >` | How to update the offset for this module.<br>	  DirectSet - Set the value directly (overwrite any previous setting)<br>	  Additive  - Add the offset of this module to the existing offset<br>	  Scalar    - Scale the existing offset by the value of this module |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

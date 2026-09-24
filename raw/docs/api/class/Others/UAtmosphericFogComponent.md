# UAtmosphericFogComponent

Used to create fogging effects such as clouds.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SunMultiplier | `float` | Global scattering factor. |
| FogMultiplier | `float` | Scattering factor on object. |
| DensityMultiplier | `float` | Fog density control factor. |
| DensityOffset | `float` | Fog density offset to control opacity [-1.f ~ 1.f]. |
| DistanceScale | `float` | Distance scale. |
| AltitudeScale | `float` | Altitude scale (only Z scale). |
| DistanceOffset | `float` | Distance offset, in km (to handle large distance) |
| GroundOffset | `float` | Ground offset. |
| StartDistance | `float` | Start Distance. |
| SunDiscScale | `float` | Distance offset, in km (to handle large distance) |
| DefaultBrightness | `float` | Default light brightness. Used when there is no sunlight placed in the level. Unit is lumens |
| DefaultLightColor | [FColor](../../cppstruct/F/FC/FColor.md) | Default light color. Used when there is no sunlight placed in the level. |
| bDisableSunDisk | `uint32` | Disable Sun Disk rendering. |
| bDisableGroundScattering | `uint32` | Disable Color scattering from ground. |
| PrecomputeParams | [FAtmospherePrecomputeParameters](../../cppstruct/F/FA/FAtmospherePrecomputeParameters.md) |  |
| TransmittanceTexture_DEPRECATED | `UTexture2D *` |  |
| IrradianceTexture_DEPRECATED | `UTexture2D *` |  |

## Functions

### SetDefaultBrightness

Set brightness of the light

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewBrightness | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDefaultLightColor

Set color of the light

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetSunMultiplier

Set SunMultiplier

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewSunMultiplier | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFogMultiplier

Set FogMultiplier

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewFogMultiplier | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDensityMultiplier

Set DensityMultiplier

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDensityMultiplier | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDensityOffset

Set DensityOffset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDensityOffset | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDistanceScale

Set DistanceScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDistanceScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetAltitudeScale

Set AltitudeScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAltitudeScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetStartDistance

Set StartDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewStartDistance | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDistanceOffset

Set DistanceOffset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDistanceOffset | `float` |  |

**Return**

- Type: 
- Description: _None_

### DisableSunDisk

Set DisableSunDisk

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewSunDisk | `bool` |  |

**Return**

- Type: 
- Description: _None_

### DisableGroundScattering

Set DisableGroundScattering

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewGroundScattering | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPrecomputeParams

Set PrecomputeParams, only valid in Editor mode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DensityHeight | `float` |  |
| MaxScatteringOrder | `int32` |  |
| InscatterAltitudeSampleNum | `int32` |  |

**Return**

- Type: 
- Description: _None_

### StartPrecompute

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

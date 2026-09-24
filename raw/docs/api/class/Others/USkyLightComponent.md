# USkyLightComponent

## Parents

- [ULightComponentBase](./ULightComponentBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SourceType | `TEnumAsByte < enum ESkyLightSourceType >` | Indicates where to get the light contribution from. |
| Cubemap | `UTextureCube *` | Cubemap to use for sky lighting if SourceType is set to SLS_SpecifiedCubemap. |
| SourceCubemapAngle | `float` | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |
| CubemapResolution | `int32` | Maximum resolution for the very top processed cubemap mip. Must be a power of 2. |
| SkyDistanceThreshold | `float` | Distance from the sky light at which any geometry should be treated as part of the sky.<br>	  This is also used by reflection captures, so update reflection captures to see the impact. |
| bCaptureEmissiveOnly | `bool` | Only capture emissive materials. Skips all lighting making the capture cheaper. Recomended when using CaptureEveryFrame |
| bLowerHemisphereIsBlack | `bool` | Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.<br>	  Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,<br>	  However disabling it can be useful to approximate skylight bounce lighting (eg Movable light). |
| LowerHemisphereColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |
| OcclusionMaxDistance | `float` | Max distance that the occlusion of one point will affect another.<br>	  Higher values increase the cost of Distance Field AO exponentially. |
| Contrast | `float` | Contrast S-curve applied to the computed AO.  A value of 0 means no contrast increase, 1 is a significant contrast increase. |
| OcclusionExponent | `float` | Exponent applied to the computed AO.  Values lower than 1 brighten occlusion overall without losing contact shadows. |
| MinOcclusion | `float` | Controls the darkest that a fully occluded area can get.  This tends to destroy contact shadows, use Contrast or OcclusionExponent instead. |
| OcclusionTint | [FColor](../../cppstruct/F/FC/FColor.md) | Tint color on occluded areas, artistic control. |
| OcclusionCombineMode | `TEnumAsByte < enum EOcclusionCombineMode >` | Controls how occlusion from Distance Field Ambient Occlusion is combined with Screen Space Ambient Occlusion. |
| bForceHide | `uint8` | Whether to hide the primitive in game, if the primitive is Visible. |
| FakeSkyLightAOClampMin | `float` |  |
| BlendDestinationCubemap | `UTextureCube *` |  |

## Functions

### SetIntensity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewIntensity | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetIndirectLightingIntensity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewIntensity | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricScatteringIntensity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewIntensity | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetLightColor

Set color of the light

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetCubemap

Sets the cubemap used when SourceType is set to SpecifiedCubemap, and causes a skylight update on the next tick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewCubemap | `UTextureCube *` |  |

**Return**

- Type: 
- Description: _None_

### SetCubemapBlend

Creates sky lighting from a blend between two cubemaps, which is only valid when SourceType is set to SpecifiedCubemap.
	  This can be used to seamlessly transition sky lighting between different times of day.
	  The caller should continue to update the blend until BlendFraction is 0 or 1 to reduce rendering cost.
	  The caller is responsible for avoiding pops due to changing the source or destination.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceCubemap | `UTextureCube *` |  |
| DestinationCubemap | `UTextureCube *` |  |
| InBlendFraction | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOcclusionTint

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTint | `FColor &` |  |

**Return**

- Type: 
- Description: _None_

### SetOcclusionContrast

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOcclusionContrast | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOcclusionExponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOcclusionExponent | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetMinOcclusion

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMinOcclusion | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetForceHide

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInForceHide | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RecaptureSky

Recaptures the scene for the skylight.
	  This is useful for making sure the sky light is up to date after changing something in the world that it would capture.
	  Warning: this is very costly and will definitely cause a hitch.

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

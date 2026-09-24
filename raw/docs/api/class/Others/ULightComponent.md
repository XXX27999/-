# ULightComponent

## Parents

- [ULightComponentBase](./ULightComponentBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Temperature | `float` | Color temperature in Kelvin of the blackbody illuminant.<br>	 White (D65) is 6500K. |
| MaxDrawDistance | `float` |  |
| MaxDistanceFadeRange | `float` |  |
| bUseTemperature | `uint32` | false: use white (D65) as illuminant. |
| ShadowMapChannel_DEPRECATED | `int32` | Legacy shadowmap channel from the lighting build, now stored in FLightComponentMapBuildData. |
| MinRoughness | `float` | Min roughness effective for this light. Used for softening specular highlights. |
| SpecularScale | `float` | Multiplier on specular highlights. Use only with great care! Any value besides 1 is not physical!<br>	 Can be used to artistically remove highlights mimicking polarizing filters or photo touch up. |
| bLocalLightDisableDiffuse | `uint32` | Local light disable diffuse |
| ShadowResolutionScale | `float` | Scales the resolution of shadowmaps used to shadow this light.  By default shadowmap resolution is chosen based on screen size of the caster.<br>	  Note: shadowmap resolution is still clamped by 'r.Shadow.MaxResolution' |
| LightPriority | `int32` | Light priority for mobile light grid |
| ShadowBias | `float` | Controls how accurate self shadowing of whole scene shadows from this light are.<br>	  At 0, shadows will start at the their caster surface, but there will be many self shadowing artifacts.<br>	  larger values, shadows will start further from their caster, and there won't be self shadowing artifacts but object might appear to fly.<br>	  around 0.5 seems to be a good tradeoff. This also affects the soft transition of shadows |
| ShadowSharpen | `float` | Amount to sharpen shadow filtering |
| ContactShadowLength | `float` | Length of screen space ray trace for sharp contact shadows. Zero is disabled. |
| InverseSquaredFalloff_DEPRECATED | `uint32` |  |
| bCacheStaticShadows | `uint32` |  |
| CastTranslucentShadows | `uint32` | Whether the light is allowed to cast dynamic shadows from translucency. |
| bCastShadowsFromCinematicObjectsOnly | `uint32` | Whether the light should only cast shadows from components marked as bCastCinematicShadows.<br>	  This is useful for setting up cinematic Movable spotlights aimed at characters and avoiding the shadow depth rendering costs of the background.<br>	  Note: this only works with dynamic shadow maps, not with static shadowing or Ray Traced Distance Field shadows. |
| bAffectDynamicIndirectLighting | `uint32` | Whether the light should be injected into the Light Propagation Volume |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) | Channels that this light should affect.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| LightFunctionMaterial | `UMaterialInterface *` | The light function material to be applied to this light.<br>	  Note that only non-lightmapped lights (UseDirectLightMap=False) can have a light function. |
| LightFunctionScale | [FVector](../../cppstruct/F/FV/FVector.md) | Scales the light function projection.  X and Y scale in the directions perpendicular to the light's direction, Z scales along the light direction. |
| IESTexture | `UTextureLightProfile *` | IES texture (light profiles from real world measured data) |
| bUseIESBrightness | `uint32` | true: take light brightness from IES profile, false: use the light brightness - the maximum light in one direction is used to define no masking. Use with InverseSquareFalloff. Will be disabled if a valid IES profile texture is not supplied. |
| IESBrightnessScale | `float` | Global scale for IES brightness contribution. Only available when "Use IES Brightness" is selected, and a valid IES profile texture is set |
| LightFunctionFadeDistance | `float` | Distance at which the light function should be completely faded to DisabledBrightness.<br>	  This is useful for hiding aliasing from light functions applied in the distance. |
| DisabledBrightness | `float` | Brightness factor applied to the light when the light function is specified but disabled, for example in scene captures that use SceneCapView_LitNoShadows.<br>	  This should be set to the average brightness of the light function material's emissive input, which should be between 0 and 1. |
| bEnableLightShaftBloom | `uint32` | Whether to render light shaft bloom from this light.<br>	  For directional lights, the color around the light direction will be blurred radially and added back to the scene.<br>	  for point lights, the color on pixels closer than the light's SourceRadius will be blurred radially and added back to the scene. |
| BloomScale | `float` | Scales the additive color. |
| BloomThreshold | `float` | Scene color must be larger than this to create bloom in the light shafts. |
| BloomTint | [FColor](../../cppstruct/F/FC/FColor.md) | Multiplies against scene color to create the bloom color. |
| bUseRayTracedDistanceFieldShadows | `bool` | Whether to use ray traced distance field area shadows.  The project setting bGenerateMeshDistanceFields must be enabled for this to have effect.<br>	  Distance field shadows support area lights so they create soft shadows with sharp contacts.<br>	  They have less aliasing artifacts than standard shadowmaps, but inherit all the limitations of distance field representations (only uniform scale, no deformation).<br>	  These shadows have a low per-object cost (and don't depend on triangle count) so they are effective for distant shadows from a dynamic sun. |
| RayStartOffsetDepthScale | `float` | Controls how large of an offset ray traced shadows have from the receiving surface as the camera gets further away.<br>	  This can be useful to hide self-shadowing artifacts from low resolution distance fields on huge static meshes. |

## Functions

### SetIntensity

Set intensity of the light

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
| NewLightColor | `FLinearColor` |  |
| bSRGB | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTemperature

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTemperature | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetLightFunctionMaterial

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFunctionMaterial | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetLightFunctionScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFunctionScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetLightFunctionFadeDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFunctionFadeDistance | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetLightFunctionDisabledBrightness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetAffectDynamicIndirectLighting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAffectTranslucentLighting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetEnableLightShaftBloom

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBloomScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBloomThreshold

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBloomTint

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | [FColor](../../cppstruct/F/FC/FColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetIESTexture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `UTextureLightProfile *` |  |

**Return**

- Type: 
- Description: _None_

### SetShadowBias

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### ForceUpdateShadowState

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSpecularScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetLocalLightDisableDiffuse

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

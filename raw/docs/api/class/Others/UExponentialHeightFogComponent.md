# UExponentialHeightFogComponent

Used to create fogging effects such as clouds but with a density that is related to the height of the fog.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FogDensity | `float` | Global density factor. |
| CustomHightFogDensity | `TArray < FCustomHeightFog >` |  |
| bUseCustomFog | `bool` |  |
| CustomFogLow_Height | `float` |  |
| CustomFogLow_DensityCoefficient | `float` |  |
| CustomFogLow_Color | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |
| CustomFogHigh_Height | `float` |  |
| CustomFogHigh_DensityCoefficient | `float` |  |
| CustomFogHigh_Color | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |
| FogInscatteringColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |
| InscatteringColorCubemap | `UTextureCube *` | Cubemap that can be specified for fog color, which is useful to make distant, heavily fogged scene elements match the sky.<br>	  When the cubemap is specified, FogInscatteringColor is ignored and Directional inscattering is disabled. |
| InscatteringColorCubemapAngle | `float` | Angle to rotate the InscatteringColorCubemap around the Z axis. |
| InscatteringTextureTint | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Tint color used when InscatteringColorCubemap is specified, for quick edits without having to reimport InscatteringColorCubemap. |
| FullyDirectionalInscatteringColorDistance | `float` | Distance at which InscatteringColorCubemap should be used directly for the Inscattering Color. |
| NonDirectionalInscatteringColorDistance | `float` | Distance at which only the average color of InscatteringColorCubemap should be used as Inscattering Color. |
| DirectionalInscatteringExponent | `float` | Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.<br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| DirectionalInscatteringStartDistance | `float` | Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light.<br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| DirectionalInscatteringColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light.<br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| FogHeightFalloff | `float` | Height density factor, controls how the density increases as height decreases.<br>	  Smaller values make the visible transition larger. |
| FogMaxOpacity | `float` | Maximum opacity of the fog.<br>	  A value of 1 means the fog can become fully opaque at a distance and replace scene color completely,<br>	  A value of 0 means the fog color will not be factored in at all. |
| StartDistance | `float` | Distance from the camera that the fog will start, in world units. |
| FogCutoffDistance | `float` | Scene elements past this distance will not have fog applied.  This is useful for excluding skyboxes which already have fog baked in. |
| Priority | `int32` | Priority to be rendered with, useful if more than one exponential fogs are visible concurrently |
| bEnableVolumetricFog | `bool` | Whether to enable Volumetric fog.  Scalability settings control the resolution of the fog simulation.<br>	  Note that Volumetric fog currently does not support StartDistance, FogMaxOpacity and FogCutoffDistance.<br>	  Volumetric fog also can't match exponential height fog in general as exponential height fog has non-physical behavior. |
| VolumetricFogScatteringDistribution | `float` | Controls the scattering phase function - how much incoming light scatters in various directions.<br>	  A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.<br>	  In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0. |
| VolumetricFogAlbedo | [FColor](../../cppstruct/F/FC/FColor.md) | The height fog particle reflectiveness used by volumetric fog.<br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| VolumetricFogEmissive | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,<br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| VolumetricFogExtinctionScale | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |
| VolumetricFogDistance | `float` | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |
| VolumetricFogStaticLightingScatteringIntensity | `float` |  |
| bOverrideLightColorsWithFogInscatteringColors | `bool` | Whether to use FogInscatteringColor for the Sky Light volumetric scattering color and DirectionalInscatteringColor for the Directional Light scattering color.<br>	  Make sure your directional light has 'Atmosphere Sun Light' enabled!<br>	  Enabling this allows Volumetric fog to better match Height fog in the distance, but produces non-physical volumetric lighting that may not match surface lighting. |
| VolumetricFogStartDistance | `float` | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |
| VolumetricFogNoiseTexture | `UTexture2D *` |  |
| VolumetricFogNoiseTransform | [FTransform](../../cppstruct/F/FT/FTransform.md) |  |

## Functions

### SetFogDensity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetCustomFogHeight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetCustomFogDensityCoefficient

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |
| index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetCustomFogInscatteringColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `FLinearColor` |  |
| index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetFogInscatteringColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetInscatteringColorCubemap

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `UTextureCube *` |  |

**Return**

- Type: 
- Description: _None_

### SetInscatteringColorCubemapAngle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFullyDirectionalInscatteringColorDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetNonDirectionalInscatteringColorDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetInscatteringTextureTint

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetDirectionalInscatteringExponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDirectionalInscatteringStartDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetDirectionalInscatteringColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetFogHeightFalloff

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFogMaxOpacity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetStartDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFogCutoffDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFog

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogScatteringDistribution

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogExtinctionScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogAlbedo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | [FColor](../../cppstruct/F/FC/FColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogEmissive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogStartDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogNoiseTexture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `UTexture2D *` |  |

**Return**

- Type: 
- Description: _None_

### SetVolumetricFogNoiseTransform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transform | [FTransform](../../cppstruct/F/FT/FTransform.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

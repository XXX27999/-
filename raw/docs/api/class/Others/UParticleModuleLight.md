# UParticleModuleLight

## Parents

- UParticleModuleLightBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bUseInverseSquaredFalloff | `bool` | Whether to use physically based inverse squared falloff from the light.  If unchecked, the LightExponent distribution will be used instead. |
| bAffectsTranslucency | `bool` | Whether lights from this module should affect translucency.<br>	  Use with caution.  Modules enabling this should only make a few particle lights at most, and the smaller they are, the less they will cost. |
| bPreviewLightRadius | `bool` | Will draw wireframe spheres to preview the light radius if enabled.<br>	  Note: this is intended for previewing and the value will not be saved, it will always revert to disabled. |
| SpawnFraction | `float` | Fraction of particles in this emitter to create lights on. |
| ColorScaleOverLife | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | Scale that is applied to the particle's color to calculate the light's color, and can be setup as a curve over the particle's lifetime. |
| BrightnessOverLife | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | Brightness scale for the light, which can be setup as a curve over the particle's lifetime. |
| RadiusScale | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | Scales the particle's radius, to calculate the light's radius. |
| LightExponent | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | Provides the light's exponent when inverse squared falloff is disabled. |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) | Channels that this light should affect.<br>	 Only affect high quality lights<br>	 These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| VolumetricScatteringIntensity | `float` | Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor. |
| bHighQualityLights | `bool` | Converts the particle lights into high quality lights as if they came from a PointLightComponent.  High quality lights cost significantly more on both CPU and GPU. |
| bShadowCastingLights | `bool` | Whether to cast shadows from the particle lights.  Requires High Quality Lights to be enabled.<br>	  Warning: This can be incredibly expensive on the GPU - use with caution. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

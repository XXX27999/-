# FLightmassWorldInfoSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| StaticLightingLevelScale | `float` | Warning: Setting this to less than 1 will greatly increase build times!<br>	  Scale of the level relative to real world scale (1 Unreal Unit = 1 cm).<br>	  All scale-dependent Lightmass setting defaults have been tweaked to work well with real world scale,<br>	  Any levels with a different scale should use this scale to compensate.<br>	  For large levels it can drastically reduce build times to set this to 2 or 4. |
| NumIndirectLightingBounces | `int32` | Number of light bounces to simulate for point  spot  directional lights, starting from the light source.<br>	  0 is direct lighting only, 1 is one bounce, etc.<br>	  Bounce 1 takes the most time to calculate and contributes the most to visual quality, followed by bounce 2.<br>	  Successive bounces don't really affect build times, but have a much lower visual impact, unless the material diffuse colors are close to 1. |
| NumSkyLightingBounces | `int32` | Number of skylight and emissive bounces to simulate.<br>	  Lightmass uses a non-distributable radiosity method for skylight bounces whose cost is proportional to the number of bounces. |
| IndirectLightingQuality | `float` | Warning: Setting this higher than 1 will greatly increase build times!<br>	  Can be used to increase the GI solver sample counts in order to get higher quality for levels that need it.<br>	  It can be useful to reduce IndirectLightingSmoothness somewhat (~.75) when increasing quality to get defined indirect shadows.<br>	  Note that this can't affect compression artifacts, UV seams or other texture based artifacts. |
| IndirectLightingSmoothness | `float` | Smoothness factor to apply to indirect lighting.  This is useful in some lighting conditions when Lightmass cannot resolve accurate indirect lighting.<br>	  1 is default smoothness tweaked for a variety of lighting situations.<br>	  Higher values like 3 smooth out the indirect lighting more, but at the cost of indirect shadows losing detail. |
| EnvironmentColor | [FColor](../FC/FColor.md) | Represents a constant color light surrounding the upper hemisphere of the level, like a sky.<br>	  This light source currently does not get bounced as indirect lighting and causes reflection capture brightness to be incorrect.  Prefer using a Static Skylight instead. |
| EnvironmentIntensity | `float` | Scales EnvironmentColor to allow independent color and brightness controls. |
| EmissiveBoost | `float` | Scales the emissive contribution of all materials in the scene.  Currently disabled and should be removed with mesh area lights. |
| DiffuseBoost | `float` | Scales the diffuse contribution of all materials in the scene. |
| VolumeLightingMethod | `TEnumAsByte < enum EVolumeLightingMethod >` | Technique to use for providing precomputed lighting at all positions inside the Lightmass Importance Volume |
| VolumetricLightmapDetailCellSize | `float` | Size of an Volumetric Lightmap voxel at the highest density (used around geometry), in world space units.<br>	  This setting has a large impact on build times and memory, use with caution.<br>	  Halving the DetailCellSize can increase memory by up to a factor of 8x. |
| VolumetricLightmapMaximumBrickMemoryMb | `float` | Maximum amount of memory to spend on Volumetric Lightmap Brick data.  High density bricks will be discarded until this limit is met, with bricks furthest from geometry discarded first. |
| VolumeLightSamplePlacementScale | `float` | Scales the distances at which volume lighting samples are placed.  Volume lighting samples are computed by Lightmass and are used for GI on movable components.<br>	  Using larger scales results in less sample memory usage and reduces Indirect Lighting Cache update times, but less accurate transitions between lighting areas. |
| bUseVolumeLightmapStreaming | `uint32` |  |
| bUseAmbientOcclusion | `uint32` | If true, AmbientOcclusion will be enabled. |
| bGenerateAmbientOcclusionMaterialMask | `uint32` | Whether to generate textures storing the AO computed by Lightmass.<br>	  These can be accessed through the PrecomputedAOMask material node,<br>	  Which is useful for blending between material layers on environment assets.<br>	  Be sure to set DirectIlluminationOcclusionFraction and IndirectIlluminationOcclusionFraction to 0 if you only want the PrecomputedAOMask! |
| DirectIlluminationOcclusionFraction | `float` | How much of the AO to apply to direct lighting. |
| IndirectIlluminationOcclusionFraction | `float` | How much of the AO to apply to indirect lighting. |
| OcclusionExponent | `float` | Higher exponents increase contrast. |
| FullyOccludedSamplesFraction | `float` | Fraction of samples taken that must be occluded in order to reach full occlusion. |
| MaxOcclusionDistance | `float` | Maximum distance for an object to cause occlusion on another object. |
| bVisualizeMaterialDiffuse | `uint32` | If true, override normal direct and indirect lighting with just the exported diffuse term. |
| bVisualizeAmbientOcclusion | `uint32` | If true, override normal direct and indirect lighting with just the AO term. |
| bCompressLightmaps | `uint32` | Whether to compress lightmap textures.  Disabling lightmap texture compression will reduce artifacts but increase memory and disk size by 4x.<br>	  Use caution when disabling this. |
| bUseSimpleLightmap | `uint32` | Whether to use simple lightmap on the mobile platform. |
| LightmapResolutionScale | `float` |  |
| VolumeProbeGIBakingMethod | `TEnumAsByte < enum EBakingVolumeProbeGIMethod >` |  |
| bCompressLowQualityVolumeProbeGI | `uint32` |  |
| bUseSkyVisibility | `uint32` |  |
| bUseIndoorSkyVisibility | `uint32` |  |
| MaxSkyOcclusionDistance | `float` | Maximum distance for sky occlusion trace. 0 = no limit (default). Only affects VolumeProbeGI baking. |
| LandscapeLightmapResolutionScale | `float` |  |

# FIdeaBakingWorldInfoSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BakingLayout | [EIdeaBakingLayout](../../../cppenum/E/EI/EIdeaBakingLayout.md) | By luciuszhang: Baking layout mode |
| NumCoarseSamples | `int32` | Number of first pass light samples. |
| NumSamples | `int32` | Number of second pass light samples for two pass mode and samples for brute force mode. |
| NumLightingBounces | `int32` | Number of light bounces to simulate for point  spot  directional lights, starting from the light source.<br>	 0 is direct lighting only, 1 is one bounce, etc.<br>	 Bounce 1 takes the most time to calculate and contributes the most to visual quality, followed by bounce 2.<br>	 Successive bounces don't really affect build times, but have a much lower visual impact, unless the material diffuse colors are close to 1. |
| LightmapBoost | `float` | Scales the lightmap result of idea baking. |
| SunHardness | `float` | Control Sun direction falloff, bigger SunHardness, three direction will be more separated |
| BakingMode | [EIdeaBakingMode](../../../cppenum/E/EI/EIdeaBakingMode.md) | Baking path tracing mode, just for debug |
| bUseParallelBaking | `uint32` | If true, parallel baking will be enabled. |
| bUseConservativeRasterization | `uint32` | If true, Conservative Rasterization (emulated by multi-tap) will be enabled. |
| bUseLocalOcclusion | `uint32` | If true, local ambient occlusion (A0) will be enabled. |
| LocalOcclusionRadius | `float` | Local ambient occlusion(A0) tracing radius. |
| LocalOcclusionFallOff | `float` | Local ambient occlusion(A0) transition speed. |
| LocalOcclusionDistribution | `float` | Local ambient occlusion(A0) sampling distribution. |
| LocalOcclusionFadeRatio | `float` | Local ambient occlusion(A0) fade start ratio. |
| LocalOcclusionRes | `int32` | Local ambient occlusion(A0) resolution multiple. |
| LocalOcclusionMultiple | `int32` | Local ambient occlusion(A0) sampling multiple. |
| LocalOcclusionPower | `float` | Local ambient occlusion(A0) strength, larger value, darker AO. |
| LocalOcclusionDenoising | `int32` | Local ambient occlusion(A0) denoising filter count. |
| LocalOcclusionDilation | `int32` | Local ambient occlusion(A0) dilation filter count. |
| NumDenoisingIterators | `int32` | If true, denoise filter will be enabled. |
| NumDilationIterators | `int32` | If true, dilation filter will be enabled. |
| DirectLightDenoising | `int32` | Denoising filter iteration number for direct lighting. |
| RayTraceMaxDistance | `float` | By luciuszhang: Path tracing distance threshold in centimeters. |
| RayTraceBias | `float` | By luciuszhang: Path tracing ray bias in centimeters. |
| RetraceDistance | `float` | By luciuszhang: Retrace distance threshold in centimeters. |
| SmallestTexelRadius | `float` | By luciuszhang:<br>	 Smallest texel radius allowed, useful for clamping edge cases where some texels have a radius of 0.<br>	 This should be smaller than the smallest valid texel radius in the scene. |
| AreaLightSampleCount | `uint32` | Path tracing distance threshold in centimeters. |
| bWithPortalDirectLighting | `uint32` | If true, calculate portal light direct lighting. |
| bWithGrayDiffuse | `uint32` | If true, use gray diffuse material for sun indirect lighting. |

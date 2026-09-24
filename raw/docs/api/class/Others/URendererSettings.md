# URendererSettings

Rendering settings.

## Parents

- UDeveloperSettings

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bMobileHDR | `uint32` |  |
| bMobileDisableVertexFog | `uint32` |  |
| bMobileVTFLandscape | `uint32` |  |
| bMobileLandscapeVertexHole | `uint32` |  |
| bIdeaDecalOptimizedIO | `uint32` |  |
| MaxMobileCascades | `int32` |  |
| MobileMSAASampleCount | `TEnumAsByte < EMobileMSAASampleCount :: Type >` |  |
| CharacterDiffuseScale | `float` | ToolTip = "Character diffuse scale parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| CharacterDiffuseOffset | `float` | ToolTip = "Character diffuse offset parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| CharacterDiffusePower | `float` | ToolTip = "Character diffuse power parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| CharacterMinShadowFactor | `float` |  |
| StaticMeshDiffuseScale | `float` | ToolTip = "Character diffuse scale parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| StaticMeshDiffuseOffset | `float` | ToolTip = "Static Mesh diffuse offset parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| StaticMeshDiffusePower | `float` | ToolTip = "Static Mesh diffuse power parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| StaticMeshMinShadowFactor | `float` |  |
| bMobileAllowROCCook | `uint32` |  |
| bVirtualTextures | `uint32` | Virtual Texture |
| bMobileVirtualTextures | `uint32` |  |
| bDiscardUnusedQualityLevels | `uint32` |  |
| GlobalStaticMeshCullingScreenSize | `float` |  |
| bOcclusionCulling | `uint32` |  |
| MinScreenRadiusForLights | `float` |  |
| MinScreenRadiusForEarlyZPass | `float` |  |
| MinScreenRadiusForCSMdepth | `float` |  |
| bPrecomputedVisibilityWarning | `uint32` |  |
| bTextureStreaming | `uint32` |  |
| bUseDXT5NormalMaps | `uint32` |  |
| bClearCoatEnableSecondNormal | `uint32` |  |
| ReflectionCaptureResolution | `int32` |  |
| ReflectionEnvironmentLightmapMixBasedOnRoughness | `uint32` |  |
| bForwardShading | `uint32` |  |
| bVertexFoggingForOpaque | `uint32` |  |
| bAllowStaticLighting | `uint32` |  |
| bUseNormalMapsForStaticLighting | `uint32` |  |
| bGenerateMeshDistanceFields | `uint32` |  |
| bEightBitMeshDistanceFields | `uint32` |  |
| bGenerateLandscapeGIData | `uint32` |  |
| bCompressMeshDistanceFields | `uint32` |  |
| TessellationAdaptivePixelsPerTriangle | `float` |  |
| bSeparateTranslucency | `uint32` |  |
| TranslucentSortPolicy | `TEnumAsByte < ETranslucentSortPolicy :: Type >` |  |
| TranslucentSortAxis | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| CustomDepthStencil | `TEnumAsByte < ECustomDepthStencil :: Type >` |  |
| bCustomDepthTaaJitter | `uint32` |  |
| bEnableAlphaChannelInPostProcessing | `uint32` |  |
| bDefaultFeatureBloom | `uint32` |  |
| bDefaultFeatureAmbientOcclusion | `uint32` |  |
| bDefaultFeatureAmbientOcclusionStaticFraction | `uint32` |  |
| bDefaultFeatureAutoExposure | `uint32` |  |
| DefaultFeatureAutoExposure | `TEnumAsByte < EAutoExposureMethodUI :: Type >` |  |
| bDefaultFeatureMotionBlur | `uint32` |  |
| bDefaultFeatureLensFlare | `uint32` |  |
| DefaultFeatureAntiAliasing | `TEnumAsByte < EAntiAliasingMethod >` |  |
| bRenderUnbuiltPreviewShadowsInGame | `uint32` |  |
| bStencilForLODDither | `uint32` |  |
| EarlyZPass | `TEnumAsByte < EEarlyZPass :: Type >` |  |
| bEarlyZPassMovable | `uint32` |  |
| bEarlyZPassOnlyMaterialMasking | `uint32` |  |
| bDBuffer | `uint32` |  |
| ClearSceneMethod | `TEnumAsByte < EClearSceneOptions :: Type >` |  |
| bBasePassOutputsVelocity | `uint32` |  |
| bSelectiveBasePassOutputs | `uint32` |  |
| bDefaultParticleCutouts | `uint32` |  |
| bGlobalClipPlane | `uint32` |  |
| GBufferFormat | `TEnumAsByte < EGBufferFormat :: Type >` |  |
| bUseGPUMorphTargets | `uint32` |  |
| bNvidiaAftermathEnabled | `uint32` |  |
| bInstancedStereo | `uint32` |  |
| bMultiView | `uint32` |  |
| bMobileMultiView | `uint32` |  |
| bMobileMultiViewDirect | `uint32` |  |
| bMonoscopicFarField | `uint32` |  |
| bDebugCanvasInLayer | `uint32` |  |
| WireframeCullThreshold | `float` |  |
| bSupportStationarySkylight | `uint32` |  |
| bSupportLowQualityLightmaps | `uint32` |  |
| bSupportPointLightWholeSceneShadows | `uint32` |  |
| bSupportAtmosphericFog | `uint32` |  |
| bSupportSkinCacheShaders | `uint32` |  |
| bMobileEnableStaticAndCSMShadowReceivers | `uint32` |  |
| bMobileAllowDistanceFieldShadows | `uint32` |  |
| bMobileAllowMovableDirectionalLights | `uint32` |  |
| MobileNumDynamicPointLights | `uint32` |  |
| bMobileAllowMovableSpotlights | `uint32` |  |
| SkinCacheSceneMemoryLimitInMB | `float` |  |
| bGPUSkinLimit2BoneInfluences | `uint32` |  |
| bSupportDepthOnlyIndexBuffers | `uint32` |  |
| bSupportReversedIndexBuffers | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

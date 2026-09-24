# UPrimitiveComponent

PrimitiveComponents are SceneComponents that contain or generate some sort of geometry, generally to be rendered or used as collision data.
  There are several subclasses for the various types of geometry, but the most common by far are the ShapeComponents (Capsule, Sphere, Box), StaticMeshComponent, and SkeletalMeshComponent.
  ShapeComponents generate geometry that is used for collision detection but are not rendered, while StaticMeshComponents and SkeletalMeshComponents contain pre-built geometry that is rendered, but can also be used for collision detection.

## Parents

- [USceneComponent](./USceneComponent.md)
- INavRelevantInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ExpectedQualityLimit | [FExpectedQuality](../../cppstruct/F/FE/FExpectedQuality.md) | If limit > actual, primitive won't be rendered. |
| bFixedLODDistanceFactorSwitch | `uint8` | open this switch to use r.LOD.FixedDistanceFactor to control lod switch<br>	 for example r.LOD.FixedDistanceFactor=0.5 is half distance of origin to switch new lod |
| CullingScreenSize | `float` | If the screen percentage of the bounding box under this value, it will be culled.<br>	 Set "0" to avoid contribution culling |
| MinDrawDistance | `float` | The minimum distance at which the primitive should be rendered,<br>	  measured in world space units from the center of the primitive's bounding sphere to the camera position. |
| LDMaxDrawDistance | `float` | Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object. |
| CachedMaxDrawDistance | `float` | The distance to cull this primitive at.<br>	  A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance. |
| DepthPriorityGroup | `TEnumAsByte < enum ESceneDepthPriorityGroup >` | The scene depth priority group to draw the primitive in. |
| ViewOwnerDepthPriorityGroup | `TEnumAsByte < enum ESceneDepthPriorityGroup >` | The scene depth priority group to draw the primitive in, if it's being viewed by its owner. |
| LightmapType | [ELightmapType](../../cppenum/E/EL/ELightmapType.md) | Controls the type of lightmap used for this component. |
| VLMOptimizeType | [EVLMOptimizeType](../../cppenum/E/EV/EVLMOptimizeType.md) | To optimize performance, VLM can select optimization method. |
| bInstanceCulling | `uint8` |  |
| OverrideQueryMobilityType | [EOverrideQueryMobilityType](../../cppenum/E/EO/EOverrideQueryMobilityType.md) |  |
| bUseAsPVSOC | `uint8` |  |
| bUseDynamicPVS | `uint8` |  |
| FramePredictionCacheState | [EFPCacheState](../../cppenum/E/EF/EFPCacheState.md) |  |
| StaticSceneCacheState | [EFPCacheState](../../cppenum/E/EF/EFPCacheState.md) |  |
| bRenderToTerrainVirtualTexture | `uint8` | This primitive will be rendered to terrain VT if true |
| bForceInjectToHierarchicalSurfel | `uint8` | ------------------------------------Surfel GI Begin------------------------------------<br>	 If true, the primitive intersecting with the surfel volume will be injected into the volume whenever the camera moves. |
| bForceUseStaticMovability | `uint8` | If true, the movability of the primitive will be considered as static in Surfel GI pipeline. |
| bAffectSurfelGIWhenHidden | `uint8` | If true, always affect global illumination even if hidden in game |
| bBulletCanBreakThrough | `uint8` | 子弹碰撞穿透 |
| bAlwaysCreatePhysicsState | `uint8` | Indicates if we'd like to create physics state all the time (for collision and simulation).<br>	  If you set this to false, it still will create physics state if collision or simulation activated.<br>	  This can help performance if you'd like to avoid overhead of creating physics state when triggers |
| bGenerateOverlapEvents | `uint8` | If true, this component will generate overlap events when it is overlapping other components (eg Begin Overlap).<br>	  Both components (this and the other) must have this enabled for overlap events to occur.<br><br>	  @see UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap() |
| bUpdateOverlapEventsWhenMove | `uint8` |  |
| bForceUpdateOverlapEventsWhenMove | `uint8` |  |
| bUseSingleSweep | `uint8` | Use Sweep or single trace |
| bMultiBodyOverlap | `uint8` | If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will<br>	  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another componentbody. This flag has no<br>	  influence on single body components. |
| bCheckAsyncSceneOnMove | `uint8` | If true, this component will look for collisions on both physic scenes during movement.<br>	  Only required if the asynchronous physics scene is enabled and has geometry in it, and you wish to test for collisions with objects in that scene.<br>	  @see MoveComponent() |
| bTraceComplexOnMove | `uint8` | If true, component sweeps with this component should trace against complex collision during movement (for example, each triangle of a mesh).<br>	  If false, collision will be resolved against simple collision bounds instead.<br>	  @see MoveComponent() |
| bReturnMaterialOnMove | `uint8` | If true, component sweeps will return the material in their hit result.<br>	  @see MoveComponent(), FHitResult |
| bUseViewOwnerDepthPriorityGroup | `uint8` | True if the primitive should be rendered using ViewOwnerDepthPriorityGroup if viewed by its owner. |
| bAllowCullDistanceVolume | `uint8` | Whether to accept cull distance volumes to modify cached cull distance. |
| bHasMotionBlurVelocityMeshes | `uint8` | true if the primitive has motion blur velocity meshes |
| bVisibleInReflectionCaptures | `uint8` | If true, this component will be visible in reflection captures. |
| bRejectReflectionCapture | `uint8` | If true, this component won't be affected by any reflection capture. |
| bRenderInMainPass | `uint8` | If true, this component will be rendered in the main pass (z prepass, basepass, transparency) |
| bForceRenderInShadowPass | `uint8` | If true, this component will force be rendered in the shadow depth pass when bRenderInMainPass is false |
| HiddenInMainPassLocks | `TArray < FName >` | If Num() == 0, this component will be rendered in the main pass (z prepass, basepass, transparency) |
| bRenderInMono | `uint8` | If true, this component will be rendered in mono only if an HMD is connected and monoscopic far field rendering is activated. |
| bNeverFrustumCull | `uint8` | If true, this component will never be culled by frustum culling. It will always be considered visible regardless of camera orientation. |
| bReceivesDecals | `uint8` | Whether the primitive receives decals. |
| bOwnerNoSee | `uint8` | If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly. |
| bOnlyOwnerSee | `uint8` | If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly. |
| bTreatAsBackgroundForOcclusion | `uint8` | Treat this primitive as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes, large ground planes that are part of the vista, etc. |
| bDrawIdeaOutline | `uint8` | Whether to render the primitive's outline |
| bIdeaOutlineUseNormalInVertexColor | `uint8` | Whether to use normal vector stored in vertex color |
| bIdeaOutlineUseOutlineMesh | `uint8` |  |
| bIdeaOutlineNew | `uint8` | Should only be used in UGC and Home branch for now. This may significantly increase outline cost. Be sure you need this feature before you enable it.<br>	 Whether to use new outline pass. |
| bIdeaOutlineOcclusionHighlight | `uint8` | Whether to use occlusion highlight |
| bDisableWriteDepthForOcclusionHighlight | `uint8` | Whether to occlude other primitive's highlight. if this is already occlude highlight, it won't write depth and this flag make no use. |
| bIdeaOutlineNewUseBackFace | `uint8` | use backface for outline drawing in outline pass |
| bIdeaOverrideOutlineAndOcclusion | `uint8` | Override outline settings to enable both outline and occlusion |
| bDrawIdeaOutlineInHighlightPass | `uint8` | Move old draw outline to highlight pass, not work for outline for separate pass, maybe custom depth outline in the future |
| IdeaOutlineOcclusionColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Edit it when enable Use Both Outline And Occlusion, otherwise use IdeaOutlineColor |
| bOverrideIdeaOutlineColor | `uint8` | Whether to override the primitive's outline color |
| bOverrideIdeaOutlineThickness | `uint8` | Whether to override the primitive's outline color |
| IdeaOutlineThickness | `float` | the primitive's override outline color |
| IdeaOutlineColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | the primitive's override outline color |
| bDrawHighlight | `uint8` | Whether to draw highlight for this primitive |
| bHighlightCanBeOccluded | `uint8` | Whether the highlight mesh of this primitive can be occluded |
| bOverrideHighlightColor | `uint8` | Whether to use HighlightColor for highlight rendering, if false, use the default color in HighlightMaterial |
| HighlightColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | If bOverrideHighlightColor is true, use this color for highlight rendering |
| DrawDyeingMode | [EDrawDyeingMode](../../cppenum/E/ED/EDrawDyeingMode.md) | Draw dyeing mode of primitive |
| VisibleDyeingColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Primitive's visible color when dyeing |
| OccludedDyeingColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Primitive's occlued color when dyeing |
| bDrawDyeing | `uint8` | Whether to dyeing the primitive |
| bUseAsEarlyZ | `uint8` | Whether to render the primitive in the early z pass for mobile platform. |
| bRenderInTwoPass | `uint8` | Whether to render the primitive in the early z pass for mobile platform.<br>	 If the mesh is visibility grid's proxy<br>	 Whether to render the primitive in two pass - only work on masked hair model |
| bTwoPassTranslucent | `uint8` | Whether to render translucency in two pass. |
| bTranslucentDepthWrite | `uint8` | Whether to write depth for translucency. |
| bTranslucentDepthWriteInTwoPass | `uint8` | Write depth for translucency in two pass. Add a depth-only pass before rendering the translucent object. |
| bForceIBL | `uint8` | (TAPD:ID869829499) for SceneProxyIBL |
| bForceDisableIBL | `uint8` |  |
| bForceDynamic | `uint8` |  |
| ActiveScopeStatus | `int32` |  |
| ScopeLocalTranslation | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| ScopeLocalRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| ScopeRadius | `float` |  |
| bIsFppLayer | `uint8` |  |
| bIsTppLayer | `uint8` | When enabled, the component will NOT cast a shadow on components with bIsFppLayer enabled.<br>	  This requires bCastInsetShadow to be enabled. |
| bUseAsOccluder | `uint8` | Whether to render the primitive in the depth only pass.<br>	  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.<br>	  @todo - if any rendering features rely on a complete depth only pass, this variable needs to go away. |
| bOnlyAsOccluder | `uint8` |  |
| bSelectable | `uint8` | If this is True, this component can be selected in the editor. |
| bForceMipStreaming | `uint8` | If true, forces mips for textures used by this component to be resident when this component's level is loaded. |
| bHasPerInstanceHitProxies | `uint8` | If true a hit-proxy will be generated for each instance of instanced static meshes |
| bRecieveShadow | `uint8` | Controls whether the primitive component should recieve a shadow or not.(by jinglei) |
| CastShadow | `uint8` | Controls whether the primitive component should cast a shadow or not.<br><br>	  This flag is ignored (no shadows will be generated) if all materials on this component have an Unlit shading model. |
| bAffectDynamicIndirectLighting | `uint8` | Controls whether the primitive should inject light into the Light Propagation Volume.  This flag is only used if CastShadow is true. |
| bAffectDistanceFieldLighting | `uint8` | Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. |
| bCastDynamicShadow | `uint8` | Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. |
| bCastStaticShadow | `uint8` | Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true. |
| bCastVolumetricTranslucentShadow | `uint8` | Whether the object should cast a volumetric translucent shadow.<br>	  Volumetric translucent shadows are useful for primitives `with smoothly changing opacity like particles representing a volume,<br>	  But have artifacts when used on highly opaque surfaces. |
| bSelfShadowOnly | `uint8` | When enabled, the component will only cast a shadow on itself and not other components in the world.<br>	  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled. |
| bCastFarShadow | `uint8` | When enabled, the component will be rendering into the far shadow cascades (only for directional lights). |
| bCastInDoorShadow | `uint8` | When enabled, the component will be rendering shadow in door (only for directional lights). |
| bCastInsetShadow | `uint8` | Whether this component should create a per-object shadow that gives higher effective shadow resolution.<br>	  Useful for cinematic character shadowing. Assumed to be enabled if bSelfShadowOnly is enabled. |
| bCastTranslucentShadowAsMask | `uint8` |  |
| bCastPhotonShadow | `uint8` | #if WITH_PHOTON_SHADOW |
| bCastPhotonPerObjectShadow | `uint8` | #if WITH_PHOTON_PER_OBEJCT_SHADOW |
| bNearCascade | `uint8` |  |
| bCastCinematicShadow | `uint8` | Whether this component should cast shadows from lights that have bCastShadowsFromCinematicObjectsOnly enabled.<br>	  This is useful for characters in a cinematic with special cinematic lights, where the cost of shadowmap rendering of the environment is undesired. |
| bCastHiddenShadow | `uint8` | If true, the primitive will cast shadows even if bHidden is true.<br>	 	Controls whether the primitive should cast shadows when hidden.<br>	 	This flag is only used if CastShadow is true. |
| bCastShadowAsTwoSided | `uint8` | Whether this primitive should cast dynamic shadows as if it were a two sided material. |
| bLightAsIfStatic_DEPRECATED | `uint8` |  |
| bLightAttachmentsAsGroup | `uint8` | Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.<br>	  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.<br>	  This is useful for improving performance when multiple movable components are attached together. |
| bReceiveCombinedCSMAndStaticShadowsFromStationaryLights | `uint8` | Mobile only:<br>	  If enabled this component can receive combined static and CSM shadows from a stationary light. (Enabling will increase shading cost.)<br>	  If disabled this component will only receive static shadows from stationary lights. |
| bReceiveLandscapeShadows | `uint8` |  |
| bSingleSampleShadowFromStationaryLights | `uint8` | Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.<br>	  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.<br>	  This is currently only used on stationary directional lights. |
| bIgnoreRadialImpulse | `uint8` | Will ignore radial impulses applied to this component. |
| bIgnoreRadialForce | `uint8` | Will ignore radial forces applied to this component. |
| bApplyImpulseOnDamage | `uint8` | True for damage to this component to apply physics impulse, false to opt out of these impulses. |
| bReplicatePhysicsToAutonomousProxy | `uint8` | True if physics should be replicated to autonomous proxies. This should be true for<br>		server-authoritative simulations, and false for client authoritative simulations. |
| bCorrectPXTrans | `uint8` |  |
| bCorrectPXTransUsingRemovePhysTargetFunction | `uint8` |  |
| AlwaysLoadOnClient | `uint8` | If this is True, this component must always be loaded on clients, even if Hidden and CollisionEnabled is NoCollision. |
| AlwaysLoadOnServer | `uint8` | If this is True, this component must always be loaded on servers, even if Hidden and CollisionEnabled is NoCollision |
| bUseEditorCompositing | `uint8` | Composite the drawing of this component onto the scene after post processing (only applies to editor drawing) |
| bRenderCustomDepth | `uint8` | If true, this component will be rendered in the CustomDepth pass (usually used for outlines) |
| bUpdateTransformUseTeleportPhysics | `uint8` |  |
| bUseAsyncCompilePSO | `uint8` | #if WITH_ANDROID_ASYNC_COMPILE_PSO<br>	 whether this mesh is using async compile pso , only used for android |
| bIgnoreOtherCanBeOverlap | `uint8` |  |
| bMoveMultiPenetratingIgnoreFlag | `uint8` | 是否在移动的时候，有多个渗透，就忽略开启本标志的物体 |
| bHasCustomNavigableGeometry | `TEnumAsByte < EHasCustomNavigableGeometry :: Type >` | If true then DoCustomNavigableGeometryExport will be called to collect navigable geometry of this component. |
| CanCharacterStepUpOn | `TEnumAsByte < enum ECanBeCharacterBase >` | Determine whether a Character can step up onto this component.<br>	  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.<br>	  @see FWalkableSlopeOverride |
| JumpOffVelocityFactor | `float` | 不能站的时候，角色随机移动的最大速度的比率<br>	 如果>0，表示使用本值，移动组件上的值无效；否则使用移动组件上的值 |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) | Channels that this component should be in.  Lights with matching channels will affect the component.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| IndoorOutdoorMask | `TEnumAsByte < EIndoorOutdoorMask >` |  |
| CustomDepthStencilWriteMask | [ERendererStencilMask](../../cppenum/E/ER/ERendererStencilMask.md) | Mask used for stencil buffer writes. |
| CustomDepthStencilValue | `int32` | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |
| TranslucencySortPriority | `int32` | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br><br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.<br>	  It is especially problematic on dynamic gameplay effects. |
| TerrainRVTRenderSortPriority | `int32` | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |
| VisibilityId | `int32` | Used for precomputed visibility |
| PVSHandlerID | `int32` | Used for precomputed visibility |
| NumInstanceVisibilityVolumes | `int32` | Used for precomputed visibility |
| SkyLightIntensityScale | `float` | 天光强度缩放系数：按倍数缩放该 Primitive 接收到的天光强度。1.0 为默认原始强度，大于 1.0 增强天光，小于 1.0 减弱天光，0.0 表示不接收天光。 (ForceVolumeProbeGIWith AO不起效) |
| MinSkyVisibility | `float` | 最小天空可见度：限制该 Primitive 接收天光时的最小可见度下限（0~1）。用于防止角落遮蔽区域因烘焙 AO 过暗而完全看不到天光，数值越大底部越亮。 |
| FakeSkyLightAOIntensity | `float` | 伪天光 AO 强度：按单个 Primitive 控制 FakeSkyLightAO（伪天光环境光遮蔽）的作用强度。0 表示不施加伪 AO（完全明亮），1 表示完整效果（默认），中间值按比例混合，数值越小接收越多天光。 |
| bAffectSkyOcclusion | `uint8` | Whether this primitive affects sky occlusion during Lightmass baking. If false, rays will pass through this mesh for sky occlusionvisibility. |
| bForceSyncPSO | `uint32` | #if ALLOW_FORCE_SYNC_CREATE_PSO<br>	  Force this material to link PSO synchronously (on iOS).<br>	  It avoids popping when the material is not suitable for async linking but may introduce stutters.<br>	  remove for IG |
| OverrideCylinderMaxDrawHeight | `float` | Used if [r.CylinderMaxDrawHeight] is not zero, override [r.CylinderMaxDrawHeight] global setting |
| bCanSeparateParticleRendering | `bool` |  |
| bDisableDynamicInstancing | `bool` |  |
| BoundsScale | `float` | Scales the bounds of the object.<br>	  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.<br>	  Warning: Increasing the bounds of an object will reduce performance and shadow quality!<br>	  Currently only used by StaticMeshComponent and SkeletalMeshComponent. |
| OCBoundsScale | `float` |  |
| OCBoundsExtent | `int32` | ROC Extent the bounds a few pixels during depth test. |
| LastSubmitTime | `float` | Last time the component was submitted for rendering (called FScene::AddPrimitive). |
| LastRenderTime | `float` | The value of WorldSettings->TimeSeconds for the frame when this component was last rendered.  This is written<br>	  from the render thread, which is up to a frame behind the game thread, so you should allow this time to<br>	  be at least a frame behind the game thread's world time before you consider the actor non-visible. |
| LastRenderTimeOnScreen | `float` |  |
| TouchAsBlockActors | `TArray < AActor * >` |  |
| MoveIgnoreComponents | `TArray < UPrimitiveComponent * >` | Set of components to ignore during component sweeps in MoveComponent().<br>	 These components will be ignored when this component moves or updates overlaps.<br>	 The other components may also need to be told to do the same when they move.<br>	 Does not affect movement of this component when simulating physics.<br>	 @see IgnoreComponentWhenMoving() |
| BodyInstance | [FBodyInstance](../../cppstruct/F/FB/FBodyInstance.md) | Physics scene information for this component, holds a single rigid body with multiple shapes. |
| LODParentPrimitive | `UPrimitiveComponent *` | LOD parent primitive to draw instead of this one (multiple UPrim's will point to the same LODParent ) |
| PostPhysicsComponentTick | `FPrimitiveComponentPostPhysicsTickFunction` | Tick function for physics ticking |
| IndirectLightingCacheQuality | `TEnumAsByte < EIndirectLightingCacheQuality >` | Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time. |
| bGenerateSurfaceSample | `uint8` |  |
| bOccludeLightingRay | `uint8` |  |
| bEnableAutoLODGeneration | `uint8` | If true, and if World setting has bEnableHierarchicalLOD equal to true, then this component will be included when generating a Proxy mesh for the parent Actor |
| bUseMaxLODAsImposter | `uint8` | Use the Maximum LOD Mesh (imposter) instead of including Mesh data from this component in the Proxy Generation process |
| ExcludeForSpecificHLODLevels | `TArray < int32 >` | Which specific HLOD levels this component should be excluded from |
| bIsVisibilityGridProxy | `uint8` | Whether to render the primitive in the early z pass for mobile platform.<br>	 If the mesh is visibility grid's proxy |
| CanBeCharacterBase_DEPRECATED | `TEnumAsByte < enum ECanBeCharacterBase >` |  |
| LpvBiasMultiplier | `float` | Multiplier used to scale the Light Propagation Volume light injection bias, to reduce light bleeding.<br>	  Set to 0 for no bias, 1 for default or higher for increased biasing (e.g. for<br>	  thin geometry such as walls) |
| bCoastline | `uint8` | if true, primitive will be collected as coastline |

## Functions

### SetLightingChannels

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bChannel0Open | `bool` |  |
| bChannel1Open | `bool` |  |
| bChannel2Open | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IgnoreActorWhenMoving

Tells this component whether to ignore collision with all components of a specific Actor when this component is moved.
	  Components on the other Actor may also need to be told to do the same when they move.
	  Does not affect movement of this component when simulating physics.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| bShouldIgnore | `bool` |  |

**Return**

- Type: 
- Description: _None_

### CopyArrayOfMoveIgnoreActors

Returns the list of actors we currently ignore when moving.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearMoveIgnoreActors

Clear the list of actors we ignore when moving.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IgnoreComponentWhenMoving

Tells this component whether to ignore collision with another component when this component is moved.
	 The other components may also need to be told to do the same when they move.
	 Does not affect movement of this component when simulating physics.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UPrimitiveComponent *` |  |
| bShouldIgnore | `bool` |  |

**Return**

- Type: 
- Description: _None_

### CopyArrayOfMoveIgnoreComponents

Returns the list of actors we currently ignore when moving.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearMoveIgnoreComponents

Clear the list of components we ignore when moving.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOverlappingComponent

Check whether this component is overlapping another component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherComp | `UPrimitiveComponent *` | Component to test this component against. |

**Return**

- Type: 
- Description: _None_

### IsOverlappingActor

Check whether this component is overlapping any component of the given Actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Other | `AActor *` | Actor to test this component against. |

**Return**

- Type: 
- Description: _None_

### GetOverlappingActors

Returns a list of actors that this component is overlapping.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OverlappingActors | `TArray < AActor * > &` | [out] Returned list of overlapping actors |
| ClassFilter | `TSubclassOf < AActor >` | [optional] If set, only returns actors of this class or subclasses |

**Return**

- Type: 
- Description: _None_

### GetOverlappingComponents

Returns list of components this component is overlapping.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOverlappingComponents | `TArray < UPrimitiveComponent * > &` |  |

**Return**

- Type: 
- Description: _None_

### SetBoundsScale

Scale the bounds of this object, used for frustum culling. Useful for features like WorldPositionOffset.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewBoundsScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetBoundsScale

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaterial

Returns the material used by the element at the specified index

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` | - The element to access the material of. |

**Return**

- Type: 
- Description: _None_

### SetMaterial

Changes the material applied to an element of the mesh.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` | - The element to access the material of. |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetMaterialByName

Changes the material applied to an element of the mesh.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaterialSlotName | `FName` | - The slot name to access the material of. |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### CreateAndSetMaterialInstanceDynamic

Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |

**Return**

- Type: 
- Description: _None_

### CreateAndSetMaterialInstanceDynamicFromMaterial

Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |
| Parent | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### CreateDynamicMaterialInstance

Creates a Dynamic Material Instance for the specified element index, optionally from the supplied material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |
| SourceMaterial | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### GetMaterialFromCollisionFaceIndex

Try and retrieve the material applied to a particular collision face of mesh. Used with face index returned from collision trace.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FaceIndex | `int32` | Face index from hit result that was hit by a trace |
| SectionIndex | `int32 &` | Section of the mesh that the face belongs to |

**Return**

- Type: 
- Description: _None_

### GetWalkableSlopeOverride

Returns the slope override struct for this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWalkableSlopeOverride

Sets a new slope override for this component instance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewOverride | `FWalkableSlopeOverride &` |  |

**Return**

- Type: 
- Description: _None_

### SetSimulatePhysics

Sets whether or not a single body should use physics simulation, or should be 'fixed' (kinematic).
	 	Note that if this component is currently attached to something, beginning simulation will detach it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bSimulate | `bool` | New simulation state for single body |

**Return**

- Type: 
- Description: _None_

### SetLockedAxis

Sets the constraint mode of the component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LockedAxis | `EDOFMode :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetConstraintMode

Sets the constraint mode of the component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConstraintMode | `EDOFMode :: Type` | The type of constraint to use. |

**Return**

- Type: 
- Description: _None_

### AddImpulse

Add an impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` | Magnitude and direction of impulse to apply. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body. |
| bVelChange | `bool` | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |

**Return**

- Type: 
- Description: _None_

### AddAngularImpulse

Add an angular impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` |  |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |
| bVelChange | `bool` | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddAngularImpulseInRadians

Add an angular impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` |  |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |
| bVelChange | `bool` | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddAngularImpulseInDegrees

Add an angular impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` |  |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |
| bVelChange | `bool` | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddImpulseAtLocation

Add an impulse to a single rigid body at a specific location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` | Magnitude and direction of impulse to apply. |
| Location | `FVector` | Point in world space to apply impulse at. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### AddRadialImpulse

Add an impulse to all rigid bodies in this component, radiating out from the specified position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `FVector` | Point of origin for the radial impulse blast, in world space |
| Radius | `float` | Size of radial impulse. Beyond this distance from Origin, there will be no affect. |
| Strength | `float` | Maximum strength of impulse applied to body. |
| Falloff | `ERadialImpulseFalloff` | Allows you to control the strength of the impulse as a function of distance from Origin. |
| bVelChange | `bool` | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |

**Return**

- Type: 
- Description: _None_

### AddForce

Add a force to a single rigid body.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |

**Return**

- Type: 
- Description: _None_

### AddForce_AssumesLocked

Add a force to a single rigid body.
   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

 	Notice: AssumesLocked   yufeiili 未加锁版本

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |

**Return**

- Type: 
- Description: _None_

### AddForceAtLocation

Add a force to a single rigid body at a particular location in world space.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| Location | `FVector` | Location to apply force, in world space. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### AddForceAtLocation_AssumesLocked

Add a force to a single rigid body at a particular location in world space.
   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

 	Notice: AssumesLocked   yufeiili 未加锁版本

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| Location | `FVector` | Location to apply force, in world space. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### AddForceAtLocationLocal

Add a force to a single rigid body at a particular location. Both Force and Location should be in body space.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| Location | `FVector` | Location to apply force, in component space. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### AddRadialForce

Add a force to all bodies in this component, originating from the supplied world-space location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `FVector` | Origin of force in world space. |
| Radius | `float` | Radius within which to apply the force. |
| Strength | `float` | Strength of force to apply. |
| Falloff | `ERadialImpulseFalloff` | Allows you to control the strength of the force as a function of distance from Origin. |
| bAccelChange | `bool` | If true, Strength is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |

**Return**

- Type: 
- Description: _None_

### AddTorque

Add a torque to a single rigid body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Torque | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddTorqueInRadians

Add a torque to a single rigid body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Torque | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddTorqueInRadians_AssumesLocked

Add a torque to a single rigid body.
	 	assumesLocked yufeiii 未加锁版本

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Torque | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddTorqueInDegrees

Add a torque to a single rigid body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Torque | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### AddTorqueInDegrees_AssumesLocked

Add a torque to a single rigid body.
	 	Notice: AssumesLocked   yufeiili 未加锁版本

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Torque | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Return**

- Type: 
- Description: _None_

### SetPhysicsLinearVelocity

Set the linear velocity of a single body.
	 	This should be used cautiously - it may be better to use AddForce or AddImpulse.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewVel | `FVector` | New linear velocity to apply to physics. |
| bAddToCurrent | `bool` | If true, NewVel is added to the existing velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetPhysicsLinearVelocity

Get the linear velocity of a single body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetPhysicsLinearVelocity_AssumesLocked

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetPhysicsLinearVelocityAtPoint

Get the linear velocity of a point on a single body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector` | Point is specified in world space. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetAllPhysicsLinearVelocity

Set the linear velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewVel | `FVector` | New linear velocity to apply to physics. |
| bAddToCurrent | `bool` | If true, NewVel is added to the existing velocity of the body. |

**Return**

- Type: 
- Description: _None_

### SetPhysicsAngularVelocity

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngVel | `FVector` | New angular velocity to apply to body, in degrees per second. |
| bAddToCurrent | `bool` | If true, NewAngVel is added to the existing angular velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetPhysicsAngularVelocityInRadians

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngVel | `FVector` | New angular velocity to apply to body, in radians per second. |
| bAddToCurrent | `bool` | If true, NewAngVel is added to the existing angular velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetPhysicsAngularVelocityInDegrees

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngVel | `FVector` | New angular velocity to apply to body, in degrees per second. |
| bAddToCurrent | `bool` | If true, NewAngVel is added to the existing angular velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetPhysicsMaxAngularVelocity

Set the maximum angular velocity of a single body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMaxAngVel | `float` | New maximum angular velocity to apply to body, in degrees per second. |
| bAddToCurrent | `bool` | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetPhysicsMaxAngularVelocityInDegrees

Set the maximum angular velocity of a single body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMaxAngVel | `float` | New maximum angular velocity to apply to body, in degrees per second. |
| bAddToCurrent | `bool` | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetPhysicsMaxAngularVelocityInRadians

Set the maximum angular velocity of a single body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMaxAngVel | `float` | New maximum angular velocity to apply to body, in radians per second. |
| bAddToCurrent | `bool` | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetPhysicsAngularVelocity

Get the angular velocity of a single body, in degrees per second.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetPhysicsAngularVelocity_AssumesLocked

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetPhysicsAngularVelocityInDegrees

Get the angular velocity of a single body, in degrees per second.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetPhysicsAngularVelocityInDegrees_AssumesLocked

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetPhysicsAngularVelocityInRadians

Get the angular velocity of a single body, in radians per second.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetPhysicsAngularVelocityInRadians_AssumesLocked

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetCenterOfMass

Get the center of mass of a single body. In the case of a welded body this will return the center of mass of the entire welded body (including its parent and children)
	   Objects that are not simulated return (0,0,0) as they do not have COM

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to get center of mass of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetCenterOfMass

Set the center of mass of a single body. This will offset the physx-calculated center of mass.
		Note that in the case where multiple bodies are attached together, the center of mass will be set for the entire group.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CenterOfMassOffset | `FVector` | User specified offset for the center of mass of this object, from the calculated location. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### WakeRigidBody

'Wake' physics simulation for a single body.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to wake. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### PutRigidBodyToSleep

Force a single body back to sleep.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to put to sleep. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### SetNotifyRigidBodyCollision

Changes the value of bNotifyRigidBodyCollision

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewNotifyRigidBodyCollision | `bool` | - The value to assign to bNotifyRigidBodyCollision |

**Return**

- Type: 
- Description: _None_

### SetOwnerNoSee

Changes the value of bOwnerNoSee.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewOwnerNoSee | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetOnlyOwnerSee

Changes the value of bOnlyOwnerSee.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewOnlyOwnerSee | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDrawIdeaOutline

Changes the value of DrawOutline.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewDrawOutline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineUseNormalInVertexColor

Changes whether use the new outline method which uses normal vectors in vertex colors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewUseNormalInVertexColor | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineNew

Should only be used in  and Home branch for now. This may significantly increase outline cost. Be sure you need this feature before you enable it.
	 Changes whether use the new outline pass.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNew | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineUseOutlineMesh

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bUseOutlineMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineOcclusionHighlight

Changes whether use the occlusion highlight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOcclusionHighlight | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDisableWriteDepthForOcclusionHighlight

Changes whether to occlude other primitives' highlight. if this is already occlude highlight, it won't write depth and this flag make no use.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDisable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOverrideOutlineAndOcclusion

Override outline settings to enable both outline and occlusion

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOutlineAndOcclusion | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDrawIdeaOutlineInHighlightPass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bHighlight | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineNewUseBackFace

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bUseBackFace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OverrideIdeaOutlineColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOverride | `bool` |  |
| InOutlineColor | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### OverrideIdeaOutlineThickness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOverride | `bool` |  |
| InThickness | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineOcclusionColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOcclusionColor | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutline_UGC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDrawOutline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIdeaOutlineOcclusionHighlight_UGC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOcclusionHighlight | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetOutlineMesh

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StaticMesh | `UStaticMesh *` |  |

**Return**

- Type: 
- Description: _None_

### SetDrawHighlight

Turn onoff the highlight rendering for this primitive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewDrawHighlight | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetHighlightCanBeOccluded

Changes whether the highlight mesh of this primitive can be occluded

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInCanBeOccluded | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OverrideHighlightColor

Override the highlight color for this primitive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOverride | `bool` | - If true, override the highlight color using InHighlightColor. If false, use the default color in HighlightMaterial. |
| InHighlightColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | - New color used for highlight rendering |

**Return**

- Type: 
- Description: _None_

### SetDrawDyeing

Changes the value of DrawDyeing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewDrawOutline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDrawDyeingMode

Changes the value of DrawDyeingMode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDrawDyeingMode | [EDrawDyeingMode](../../cppenum/E/ED/EDrawDyeingMode.md) |  |

**Return**

- Type: 
- Description: _None_

### SetVisibleDyeingColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### SetOccludedDyeingColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### SetReveiceShadow

Changes the value of bReveiceShadow.(by jinglei)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewReveiceShadow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetCastShadow

Changes the value of CastShadow.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewCastShadow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetCastInsetShadow

Changes the value of CastInsetShadow.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInCastInsetShadow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetLightAttachmentsAsGroup

Changes the value of LightAttachmentsAsGroup.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInLightAttachmentsAsGroup | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetCastPhotonShadow

WITH_PHOTON_SHADOW
	 Set cast photon shadow.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewCastPhotonShadow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetSingleSampleShadowFromStationaryLights

Changes the value of bSingleSampleShadowFromStationaryLights.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewSingleSampleShadowFromStationaryLights | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTranslucentSortPriority

Changes the value of TranslucentSortPriority.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTranslucentSortPriority | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetReceivesDecals

Changes the value of bReceivesDecals.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewReceivesDecals | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetCollisionEnabled

Controls what kind of collision is enabled for this body

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewType | `ECollisionEnabled :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetCollisionProfileName

Set Collision Profile Name
	  This function is called by constructors when they set ProfileName
	  This will change current CollisionProfileName to be this, and overwrite Collision Setting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCollisionProfileName | `FName` | : New Profile Name |

**Return**

- Type: 
- Description: _None_

### GetCollisionProfileName

Get the collision profile name

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCollisionObjectType

Changes the collision channel that this object uses when it moves

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Channel | [ECollisionChannel](../../cppenum/E/EC/ECollisionChannel.md) |  |

**Return**

- Type: 
- Description: _None_

### K2_LineTraceComponent

Perform a line trace against a single component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TraceStart | `FVector` |  |
| TraceEnd | `FVector` |  |
| bTraceComplex | `bool` |  |
| bShowTrace | `bool` |  |
| HitLocation | `FVector &` |  |
| HitNormal | `FVector &` |  |
| BoneName | `FName &` |  |
| OutHit | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### SetRenderCustomDepth

Sets the bRenderCustomDepth property and marks the render state dirty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetCustomDepthStencilValue

Sets the CustomDepth stencil value (0 - 255) and marks the render state dirty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetCustomDepthStencilWriteMask

Sets the CustomDepth stencil write mask and marks the render state dirty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WriteMaskBit | [ERendererStencilMask](../../cppenum/E/ER/ERendererStencilMask.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRenderInMainPass

Sets bRenderInMainPass property and marks the render state dirty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bValue | `bool` |  |
| LockKey | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsRenderInMainPass

Sets bRenderInMainPass property and marks the render state dirty.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetRenderInMono

Sets bRenderInMono property and marks the render state dirty.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetNeverFrustumCull

Sets bNeverFrustumCull property and marks the render state dirty. When true, this component will never be culled by frustum culling.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsNeverFrustumCull

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForceIBL

set bForceIBL

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InForceIBL | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetForceDisableIBL

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InForceDisableIBL | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsForceDynamic

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForceDynamic

set bForceDynamic

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InForceDynamic | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsActiveScope

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActiveScope

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsActiveScope | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetScopeInfoLocal

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLocalTranslation | `FVector` |  |
| InLocalRotation | `FRotator` |  |
| InScopeRadius | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFppLayer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsFppLayer | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTppLayer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsTppLayer | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTwoPassTranslucent

Changes the value of Two Pass Translucent.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewTwoPassTranslucent | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTranslucentDepthWrite

Changes the value of Translucent Depth Write.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewTranslucentDepthWrite | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTranslucentDepthWriteInTwoPass

Changes the value of Translucent Depth Write In Two Pass.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewTranslucentDepthWriteInTwoPass | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetNumMaterials

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetClosestPointOnCollision

Returns the distance and closest point to the collision surface.
	 Component must have simple collision to be queried for closest point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FVector &` | World 3D vector |
| OutPointOnBody | `FVector &` | Point on the surface of collision closest to Point |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body. |

**Return**

- Type: 
- Description: _None_

### GetCollisionEnabled

Returns the form of collision for this component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_IsCollisionEnabled

Utility to see if there is any form of collision (query or physics) enabled on this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_IsQueryCollisionEnabled

Utility to see if there is any query collision enabled on this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_IsPhysicsCollisionEnabled

Utility to see if there is any physics collision enabled on this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCollisionResponseToChannel

Gets the response type given a specific channel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Channel | [ECollisionChannel](../../cppenum/E/EC/ECollisionChannel.md) |  |

**Return**

- Type: 
- Description: _None_

### GetCollisionObjectType

Gets the collision object type

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAllPhysicsAngularVelocity

Set the angular velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngVel | `FVector &` | New angular velocity to apply to physics, in degrees per second. |
| bAddToCurrent | `bool` | If true, NewAngVel is added to the existing angular velocity of all bodies. |

**Return**

- Type: 
- Description: _None_

### SetAllPhysicsAngularVelocityInDegrees

Set the angular velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngVel | `FVector &` | New angular velocity to apply to physics, in degrees per second. |
| bAddToCurrent | `bool` | If true, NewAngVel is added to the existing angular velocity of all bodies. |

**Return**

- Type: 
- Description: _None_

### SetAllPhysicsAngularVelocityInRadians

Set the angular velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAngVel | `FVector &` | New angular velocity to apply to physics, in radians per second. |
| bAddToCurrent | `bool` | If true, NewAngVel is added to the existing angular velocity of all bodies. |

**Return**

- Type: 
- Description: _None_

### WakeAllRigidBodies

Ensure simulation is running for all bodies in this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEnableGravity

Enablesdisables whether this component is affected by gravity. This applies only to components with bSimulatePhysics set to true.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bGravityEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsGravityEnabled

Returns whether this component is affected by gravity. Returns always false if the component is not simulated.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLinearDamping

Sets the linear damping of this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDamping | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetLinearDamping

Returns the linear damping of this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAngularDamping

Sets the angular damping of this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDamping | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetAngularDamping

Returns the angular damping of this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMassScale

Change the mass scale used to calculate the mass of a single physics body

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| InMassScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetMassScale

Returns the mass scale used to calculate the mass of a single physics body

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetAllMassScale

Change the mass scale used fo all bodies in this component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMassScale | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetMassOverrideInKg

Override the mass (in Kg) of a single physics body.
		Note that in the case where multiple bodies are attached together, the override mass will be set for the entire group.
		Set the Override Mass to false if you want to reset the body's mass to the auto-calculated physx mass.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| MassInKg | `float` |  |
| bOverrideMass | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetMass

Returns the mass of this component in kg.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetInertiaTensor

Returns the inertia tensor of this component in kg cm^2. The inertia tensor is in local component space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ScaleByMomentOfInertia

Scales the given vector by the world space moment of inertia. Useful for computing the torque needed to rotate an object.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InputVector | `FVector` |  |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsAnyRigidBodyAwake

Returns if any body in this component is currently awake and simulating.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCollisionResponseToChannel

Changes a member of the ResponseToChannels container for this PrimitiveComponent.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Channel | `ECollisionChannel` |  |
| NewResponse | [ECollisionResponse](../../cppenum/E/EC/ECollisionResponse.md) |  |

**Return**

- Type: 
- Description: _None_

### SetCollisionResponseToAllChannels

Changes all ResponseToChannels container for this PrimitiveComponent. to be NewResponse

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewResponse | [ECollisionResponse](../../cppenum/E/EC/ECollisionResponse.md) |  |

**Return**

- Type: 
- Description: _None_

### SetPhysMaterialOverride

Changes the current PhysMaterialOverride for this component.
	 	Note that if physics is already running on this component, this will _not_ alter its massinertia etc,
	 	it will only change its surface properties like friction.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPhysMaterial | `UPhysicalMaterial *` |  |

**Return**

- Type: 
- Description: _None_

### GetPhysMaterial

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Item | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetCullDistance

Changes the value of CullDistance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewCullDistance | `float` | - The value to assign to CullDistance. |
| EnableIncrease | `bool` | - Whether or not to increase the cull distance if it is greater than the current cull distance. |

**Return**

- Type: 
- Description: _None_

### CanCharacterStepUp

Return true if the given Pawn can step up onto this component.
	  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Pawn | `APawn *` | the Pawn that wants to step onto this component. |

**Return**

- Type: 
- Description: _None_

### IsComponentRenderQualityEnough

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsComponentDeviceQualityEnough

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsComponentMemoryEnough

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsComponentDeviceEnough

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnComponentHit |  | Event called when a component hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.<br>	 	For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event. |
| OnComponentBeginOverlap |  | Event called when something starts to overlaps this component, for example a player walking into a trigger.<br>	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events. |
| OnComponentEndOverlap |  | Event called when something stops overlapping this component |
| OnComponentWake |  | Event called when the underlying physics objects is woken up |
| OnComponentSleep |  | Event called when the underlying physics objects is put to sleep |
| OnComponentCollisionSettingsChangedEvent |  | Event called when collision settings change for this component. |
| OnBeginCursorOver |  | Event called when the mouse cursor is moved over this component and mouse over events are enabled in the player controller |
| OnEndCursorOver |  | Event called when the mouse cursor is moved off this component and mouse over events are enabled in the player controller |
| OnClicked |  | Event called when the left mouse button is clicked while the mouse is over this component and click events are enabled in the player controller |
| OnReleased |  | Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller |
| OnInputTouchBegin |  | Event called when a touch input is received over this component when touch events are enabled in the player controller |
| OnInputTouchEnd |  | Event called when a touch input is released over this component when touch events are enabled in the player controller |
| OnInputTouchEnter |  | Event called when a finger is moved over this component when touch over events are enabled in the player controller |
| OnInputTouchLeave |  | Event called when a finger is moved off this component when touch over events are enabled in the player controller |

## Language

cpp

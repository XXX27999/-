# ALandscapeProxy

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SplineComponent | `ULandscapeSplinesComponent *` |  |
| LandscapeGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) |  |
| BoundingGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) |  |
| bUseMaterialId | `bool` | Cached value of bUseMaterialId, should be equal to bUseMaterialId in ALandscape |
| MatIDFallbackMaterial | `UMaterialInterface *` |  |
| MatIDFallbackHoleMaterial | `UMaterialInterface *` |  |
| LandscapeSectionOffset | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) | Offset in quads from global components grid origin (in quads) |
| MaxLODLevel | `int32` | Max LOD level to use when rendering, -1 means the max available |
| MaxLODLevel_PC | `int32` | Combined material used to render the landscape |
| LODDistanceFactor_PC | `float` |  |
| LODStartDistance_PC | `float` |  |
| LODFalloff_PC | `TEnumAsByte < ELandscapeLODFalloff :: Type >` |  |
| LODDistanceFactor | `float` |  |
| LODFalloff | `TEnumAsByte < ELandscapeLODFalloff :: Type >` |  |
| bUseScreenSizeLOD | `bool` |  |
| LOD0DistributionSetting | `float` | The distribution setting used to change the LOD 0 generation, 1.75 is the normal distribution, numbers influence directly the LOD0 proportion on screen. |
| LODDistributionSetting | `float` | The distribution setting used to change the LOD generation, 2 is the normal distribution, small number mean you want your last LODs to take more screen space and big number mean you want your first LODs to take more screen space. |
| NearMaxLOD_Baked | `uint8` |  |
| NearFactor_Baked | `float` |  |
| FarFactor_Baked | `float` |  |
| LandscapeRoughness | `float` |  |
| NearExtent_Baked | `float` |  |
| EnableImproveLOD | `bool` |  |
| ImproveLODValues | `TArray < float >` | LOD Values |
| NearMaxLOD | `uint8` |  |
| NearFactor | `float` |  |
| NearExtent | `float` |  |
| FarFactor | `float` |  |
| StaticLightingLOD | `int32` | LOD level to use when running lightmass (increase to 1 or 2 for large landscapes to stop lightmass crashing) |
| DefaultPhysMaterial | `UPhysicalMaterial *` | Default physical material, used when no per-layer values physical materials |
| StreamingDistanceMultiplier | `float` | Allows artists to adjust the distance where textures using UV 0 are streamed inout.<br>	  1.0 is the default, whereas a higher value increases the streamed-in resolution.<br>	  Value can be < 0 (from legcay content, or code changes) |
| bCacheHeightData | `uint32` |  |
| LandscapeMaterial | `UMaterialInterface *` | Combined material used to render the landscape |
| LandscapeHoleMaterial | `UMaterialInterface *` | Material used to render landscape components with holes. If not set, LandscapeMaterial will be used (blend mode will be overridden to Masked if it is set to Opaque) |
| LandscapeMaterial_ForPC | `UMaterialInterface *` |  |
| LandscapeHoleMaterial_ForPC | `UMaterialInterface *` | Material used to render landscape components with holes. If not set, LandscapeMaterial will be used (blend mode will be overridden to Masked if it is set to Opaque) |
| bOverrideGrassTypes_ForPC | `uint8` |  |
| GrassTypes_ForPC | `TArray < ULandscapeGrassType * >` |  |
| OtherMaterials | `TMap < FName , UMaterialInterface * >` | Other materials allow LandscapeComponent to change its material in runtime |
| bOverrideGrassTypes | `uint8` |  |
| GrassTypes | `TArray < ULandscapeGrassType * >` |  |
| MinGrassWeightThreshold | `float` | Minimal weight threshold to generate landscape grass |
| NegativeZBoundsExtension | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the negative Z axis, positive value increases bound size<br>	   Note that this can also be overridden per-component when the component is selected with the component select tool |
| PositiveZBoundsExtension | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the positive Z axis, positive value increases bound size<br>	   Note that this can also be overridden per-component when the component is selected with the component select tool |
| GrassColor_WorldMaskNoiseTexture | `UTexture2D *` | Texture used to render grass color |
| GrassColor_UVScale_WorldMaskNoise | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| GrassColor_Center_WorldMaskNoise | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| LandscapeComponents | `TArray < ULandscapeComponent * >` | The array of LandscapeComponent that are used by the landscape |
| LandscapeAOTextureDataAsset | `ULandscapeAOTextureDataAsset *` |  |
| CollisionComponents | `TArray < ULandscapeHeightfieldCollisionComponent * >` | Array of LandscapeHeightfieldCollisionComponent |
| FoliageComponents | `TArray < UHierarchicalInstancedStaticMeshComponent * >` |  |
| StillUsed | `TSet < UHierarchicalInstancedStaticMeshComponent * >` |  |
| bHasLandscapeGrass | `bool` |  |
| StaticLightingResolution | `float` | The resolution to cache lighting at, in texelsquad in one axis<br>	   Total resolution would be changed by StaticLightingResolutionStaticLightingResolution<br>	 	Automatically calculate proper value for removing seams |
| bCastStaticShadow | `uint32` |  |
| bCastShadowAsTwoSided | `uint32` | Whether this primitive should cast dynamic shadows as if it were a two sided material. |
| bCastFarShadow | `uint32` | Whether this primitive should cast shadows in the far shadow cascades. |
| LightingChannels | [FLightingChannels](../../cppstruct/F/FL/FLightingChannels.md) | Channels that this Landscape should be in.  Lights with matching channels will affect the Landscape.<br>	 These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| bUseMaterialPositionOffsetInStaticLighting | `uint32` | Whether to use the landscape material's vertical world position offset when calculating static lighting.<br>		Does not work correctly with an XY offset map (mesh collision) |
| bRenderCustomDepth | `uint32` | If true, the Landscape will be rendered in the CustomDepth pass (usually used for outlines) |
| CustomDepthStencilValue | `int32` | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |
| LightmassSettings | [FLightmassPrimitiveSettings](../../cppstruct/F/FL/FLightmassPrimitiveSettings.md) | The Lightmass settings for this object. |
| CollisionMipLevel | `int32` |  |
| SimpleCollisionMipLevel | `int32` |  |
| CollisionThickness | `float` | Thickness of the collision surface, in unreal units |
| BodyInstance | [FBodyInstance](../../cppstruct/F/FB/FBodyInstance.md) | Collision profile settings for this landscape |
| bGenerateOverlapEvents | `uint32` | If true, Landscape will generate overlap events when other components are overlapping it (eg Begin Overlap).<br>	  Both the Landscape and the other component must have this flag enabled for overlap events to occur.<br><br>	  @see UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap() |
| bBakeMaterialPositionOffsetIntoCollision | `uint32` | Whether to bake the landscape material's vertical world position offset into the collision heightfield.<br>		Does not work with an XY offset map (mesh collision) |
| bUseHoleConsistent | `uint32` | Set to true before digging, making the physical data consistent with the rendered data, added by huiwenjiang |
| ComponentSizeQuads | `int32` | Data set at creation time |
| SubsectionSizeQuads | `int32` | Data set at creation time |
| NumSubsections | `int32` | Data set at creation time |
| bUsedForNavigation | `uint32` | Data set at creation time<br>	 Hints navigation system whether this landscape will ever be navigated on. true by default, but make sure to set it to false for faraway, background landscapes |
| bMobileMultiLayers | `uint32` |  |
| NavigationGeometryGatheringMode | [ENavDataGatheringMode](../../cppenum/E/EN/ENavDataGatheringMode.md) |  |
| bUseLandscapeForCullingInvisibleHLODVertices | `bool` | Flag whether or not this Landscape's surface can be used for culling hidden triangles |
| OverwrittenDeformWeightData | `ULandscapeDeformWeightDataAsset *` |  |
| DeformComponentMap | `TMap < FIntPoint , int32 >` |  |
| DeformWeightTileMap | `TArray < uint32 >` |  |
| DeformWeightData | `TArray < uint8 >` |  |
| ExportLOD | `int32` | LOD level to use when exporting the landscape to obj or FBX |
| TargetDisplayOrderList | `TArray < FName >` | Display Order of the targets |
| TargetDisplayOrder | [ELandscapeLayerDisplayMode](../../cppenum/E/EL/ELandscapeLayerDisplayMode.md) | Display Order mode for the targets |
| bUsePCMaterialToGenerateCollision | `bool` | Combined material used to render the landscape |
| bIsMovingToLevel | `uint32` |  |
| EditorCachedLayerInfos_DEPRECATED | `TArray < ULandscapeLayerInfoObject * >` |  |
| ReimportHeightmapFilePath | `FString` |  |
| EditorLayerSettings | `TArray < FLandscapeEditorLayerSettings >` |  |
| ExtraHeightmapNumber | `int32` |  |
| NoWeightBlendMaskNumber | `int32` |  |
| HeightmapNameSet | `TSet < FString >` |  |
| MaskNameSet | `TSet < FString >` |  |
| VisibleHeightmapNameSet | `TSet < FString >` |  |
| NoWeightBlendMaskNameSet | `TSet < FString >` |  |
| LockedHeightmapNameSet | `TSet < FString >` |  |
| ColorMaskList | `TArray < FLandscapeColorMask >` |  |
| VisibilityLayerNameSet | `TSet < FString >` | All Visibility Layer names |
| MaxPaintedLayersPerComponent | `int32` |  |
| LayerTextureParameterMapping | `TMap < FName , UTexture * >` |  |
| DeformWeightMsg | `FString` |  |

## Functions

### ChangebUseScreenSizeLOD

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbUseScreenSizeLOD | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ChangeLODDistanceFactor

Change the Level of Detail distance factor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLODDistanceFactor | `float` |  |

**Return**

- Type: 
- Description: _None_

### ChangeLOD0DistributionSettingConsoleVariable

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ChangeLODDistributionSettingConsoleVariable

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EditorApplySpline

Deform landscape using a given spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSplineComponent | `USplineComponent *` |  |
| StartWidth | `float` | - Width of the spline at the start node, in Spline Component local space |
| EndWidth | `float` | - Width of the spline at the end node, in Spline Component local space |
| StartSideFalloff | `float` | - Width of the falloff at either side of the spline at the start node, in Spline Component local space |
| EndSideFalloff | `float` | - Width of the falloff at either side of the spline at the end node, in Spline Component local space |
| StartRoll | `float` | - Roll applied to the spline at the start node, in degrees. 0 is flat |
| EndRoll | `float` | - Roll applied to the spline at the end node, in degrees. 0 is flat |
| NumSubdivisions | `int32` | - Number of triangles to place along the spline when applying it to the landscape. Higher numbers give better results, but setting it too high will be slow and may cause artifacts |
| bRaiseHeights | `bool` | - Allow the landscape to be raised up to the level of the spline. If both bRaiseHeights and bLowerHeights are false, no height modification of the landscape will be performed |
| bLowerHeights | `bool` | - Allow the landscape to be lowered down to the level of the spline. If both bRaiseHeights and bLowerHeights are false, no height modification of the landscape will be performed |
| PaintLayer | `ULandscapeLayerInfoObject *` | - LayerInfo to paint, or none to skip painting. The landscape must be configured with the same layer info in one of its layers or this will do nothing! |

**Return**

- Type: 
- Description: _None_

### BakeLandscape

UFUNCTION(BlueprintNativeEvent, BlueprintNativeEvent, CallInEditor, Category = "Improve LOD")

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DebugViewLandscapeCollision

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearCollisionDebugDraw

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FixPCOnlyWeightmapData

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FixPCOnlyWeightmap

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ChangeShowWeightmap

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

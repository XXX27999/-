# UStaticMeshComponent

StaticMeshComponent is used to create an instance of a UStaticMesh.
  A static mesh is a piece of geometry that consists of a static set of polygons.

  @see UStaticMesh

## Parents

- [UMeshComponent](./UMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ForcedLodModel | `int32` | If 0, auto-select LOD level. if >0, force to (ForcedLodModel-1). |
| PreviousLODLevel | `int32` | LOD that was desired for rendering this StaticMeshComponent last frame. |
| MinLOD | `int32` | Specifies the smallest LOD that will be used for this component.<br>	  This is ignored if ForcedLodModel is enabled. |
| MaxLOD | `int32` |  |
| StaticMesh | `UStaticMesh *` | The static mesh that this component uses to render |
| TightBoundsOrigin | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| TightBoundsBoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| TightBoundsSphereRadius | `float` |  |
| CanUseTightBound | `bool` |  |
| VisibilityCollisionColor | [FColor](../../cppstruct/F/FC/FColor.md) | Whether you want to turn on the collision display preview |
| bEnableSimpleMaterial | `bool` | If true, WireframeColorOverride will be used. If false, color is determined based on mobility and physics simulation settings |
| bOverrideWireframeColor | `uint8` | If true, WireframeColorOverride will be used. If false, color is determined based on mobility and physics simulation settings |
| bOverrideMinLOD | `uint8` | Whether to override the MinLOD setting of the static mesh asset with the MinLOD of this component. |
| bOverrideNavigationExport | `uint8` | If true, bForceNavigationObstacle flag will take priority over navigation data stored in StaticMesh |
| bForceNavigationObstacle | `uint8` | Allows overriding navigation export behavior per component: full collisions or dynamic obstacle |
| bDisallowMeshPaintPerInstance | `uint8` | If true, mesh painting is disallowed on this instance. Set if vertex colors are overridden in a construction script. |
| bHasHLODTag | `uint8` | Whether this component participates in HLOD (computed from ReorganizationTags) |
| bIgnoreInstanceForTextureStreaming | `uint8` | Ignore this instance of this static mesh when calculating streaming information.<br>	 	This can be useful when doing things like applying character textures to static geometry,<br>	 	to avoid them using distance-based streaming. |
| bOverrideLightMapRes | `uint8` | Whether to override the lightmap resolution defined in the static mesh. |
| bOverrideCullingScreenSize | `uint8` |  |
| bCastDistanceFieldIndirectShadow | `uint8` | Whether to use the mesh distance field representation (when present) for shadowing indirect lighting (from lightmaps or skylight) on Movable components.<br>	  This works like capsule shadows on skeletal meshes, except using the mesh distance field so no physics asset is required.<br>	  The StaticMesh must have 'Generate Mesh Distance Field' enabled, or the project must have 'Generate Mesh Distance Fields' enabled for this feature to work. |
| bOverrideDistanceFieldSelfShadowBias | `uint8` | Whether to override the DistanceFieldSelfShadowBias setting of the static mesh asset with the DistanceFieldSelfShadowBias of this component. |
| bUseSubDivisions | `uint8` | Whether to use subdivisions or just the triangle's vertices. |
| bUseDefaultCollision | `uint8` | Use the collision profile specified in the StaticMesh asset. |
| bForceNotHzbOccluder | `uint8` | not a hzb Occluder |
| bUseAsOccluderIgnoreMobility | `uint8` |  |
| bCanBeOccludeed | `uint8` |  |
| bCustomWaterBeOccludeed | `uint8` |  |
| bAllowCopyExpectedQualityFromMesh | `uint8` |  |
| OverriddenLightMapRes | `int32` | Light map resolution to use on this component, used if bOverrideLightMapRes is true and there is a valid StaticMesh. |
| StreamingDistanceMultiplier | `float` | Allows adjusting the desired streaming distance of streaming textures that uses UV 0.<br>	  1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.<br>	  A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).<br>	  Value can be < 0 (from legcay content, or code changes) |
| LODData | `TArray < FStaticMeshComponentLODInfo >` | Static mesh LOD data.  Contains static lighting data along with instanced mesh vertex colors. |
| StreamingTextureData | `TArray < FStreamingTextureBuildInfo >` | The list of texture, bounds and scales. As computed in the texture streaming build process. |
| IsDynamicInstancingParametersEnabled | `bool` | Is dynamic instancing parameters enabled |
| DynamicInstancingParameters | `TMap < FString , FVector4 >` | Dynamic instancing parameters |
| LightmassSettings | [FLightmassPrimitiveSettings](../../cppstruct/F/FL/FLightmassPrimitiveSettings.md) | The Lightmass settings for this object. |
| IdeaBakingSettings | [FIdeaBakingPrimitiveSettings](../../cppstruct/F/FI/FIdeaBakingPrimitiveSettings.md) | Add by luciuszhang: The IdeaBaking settings for this object. |
| AffectPointLightBPActors | `TArray < TWeakObjectPtr < AActor > >` |  |
| PointLightStaticMeshLODResources | `TArray < FStaticMeshPointLightVertexDataBuffer >` |  |
| bEnableISMbatching | `uint8` |  |
| bForceUseDynamicElement | `uint8` |  |
| LODSectionHiddenFlags | `TArray < uint8 >` | Hidden Flags for Rendering Section (8 bits = flags, Support 8 Sections), add by connerxiong 2022.6.16. |
| OutlineStaticMesh | `UStaticMesh *` | Outline Static Mesh |
| SubDivisionStepSize | `int32` | Subdivision step size for static vertex lighting. |
| WireframeColorOverride | [FColor](../../cppstruct/F/FC/FColor.md) | Wireframe color to use if bOverrideWireframeColor is true |
| SelectedEditorSection | `int32` | The section currently selected in the Editor. Used for highlighting |
| SelectedEditorMaterial | `int32` | The material currently selected in the Editor. Used for highlighting |
| SectionIndexPreview | `int32` | Index of the section to preview. If set to INDEX_NONE, all section will be rendered. Used for isolating in Static Mesh Tool |
| MaterialIndexPreview | `int32` | Index of the material to preview. If set to INDEX_NONE, all section will be rendered. Used for isolating in Static Mesh Tool |
| ReorganizationTags | [FReorganizationTagsContainer](../../cppstruct/F/FR/FReorganizationTagsContainer.md) | Reorganization tags for Level Partition system (inherits from StaticMesh by default) |
| bOverrideReorganizationTags | `bool` | Legacy serialized switch. New editorruntime logic uses per-group override flags on ReorganizationTags entries. |
| StaticMeshImportVersion | `int32` | The import version of the static mesh when it was assign this is update when:<br>	  - The user assign a new staticmesh to the component<br>	  - The component is serialize (IsSaving)<br>	  - Default value is BeforeImportStaticMeshVersionWasAdded<br><br>	  If when the component get load (PostLoad) the version of the attach staticmesh is newer<br>	  then this value, we will remap the material override because the order of the materials list<br>	  in the staticmesh can be changed. Hopefully there is a remap table save in the staticmesh. |
| bCustomOverrideVertexColorPerLOD | `uint8` | The component has some custom painting on LODs or not. |
| bDisplayVertexColors | `uint8` |  |
| DistanceFieldIndirectShadowMinVisibility | `float` | Controls how dark the dynamic indirect shadow can be. |
| DistanceFieldSelfShadowBias | `float` | Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices. |
| IrrelevantLights_DEPRECATED | `TArray < FGuid >` |  |
| StaticMeshDerivedDataKey | `FString` | Derived data key of the static mesh, used to determine if an update from the source static mesh is required. |
| MaterialStreamingRelativeBoxes | `TArray < uint32 >` | Material Bounds used for texture streaming. |

## Functions

### OnRep_StaticMesh

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldStaticMesh | `UStaticMesh *` |  |

**Return**

- Type: 
- Description: _None_

### SetStaticMesh

Change the StaticMesh used by this instance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMesh | `UStaticMesh *` |  |

**Return**

- Type: 
- Description: _None_

### SetDirty

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetVisibilityCollisionColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CollisionColor | [FColor](../../cppstruct/F/FC/FColor.md) |  |

**Return**

- Type: 
- Description: _None_

### GetVisibilityCollisionColor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetStaticMesh

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOutlineMesh

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStaticMesh | `UStaticMesh *` |  |

**Return**

- Type: 
- Description: _None_

### SetForcedLodModel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewForcedLodModel | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetDistanceFieldSelfShadowBias

Sets the component's DistanceFieldSelfShadowBias.  bOverrideDistanceFieldSelfShadowBias must be enabled for this to have an effect.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetLocalBounds

Get Local bounds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Min | `FVector &` |  |
| Max | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetDynamicInstancingParameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaterialIndex | `int` |  |
| Name | `FString &` |  |
| Value | `FVector4 &` |  |

**Return**

- Type: 
- Description: _None_

### EnableMeshClipPlane

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ClipPlane | `FPlane &` |  |
| PlaneIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### DisableMeshClipPlane

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlaneIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### EnableMeshClipArc

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ClipPlane | `FPlane &` |  |
| ClipSphere | `FVector4 &` |  |

**Return**

- Type: 
- Description: _None_

### DisableMeshClipArc

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableMeshClip4Planes

Num of ClipPlanes is 4
	  0: Top Plane
	  1: Down Plane
	  2: Left Plane
	  3: Right Plane

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ClipPlanes | `TArray < FPlane > &` |  |
| bBox | `bool` |  |

**Return**

- Type: 
- Description: _None_

### DisableMeshClip4Planes

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheckSwitchSimpleMaterial

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

# UMeshComponent

MeshComponent is an abstract base for any component that is an instance of a renderable collection of triangles.

  @see UStaticMeshComponent
  @see USkeletalMeshComponent

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OverrideMaterials | `TArray < UMaterialInterface * >` | Per-Component material overrides.  These must NOT be set directly or a race condition can occur between GC and the rendering thread. |
| OverlayMaterial | `UMaterialInterface *` | Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material |
| IndexedOverlayMaterials | `TArray < UMaterialInterface * >` | Overlay materials applied to each material slot. |
| IndexedOverrideOutlineMaterials | `TArray < UMaterialInterface * >` | Override overlay outline materials applied to each material slot. |
| bUseIndexedOverlayMaterials | `bool` | Whether to use IndexedOverlayMaterials (or OverlayMaterial). |
| bUseOverlayMaterials | `bool` | Whether to render overlay materials. (Indexed or not) |
| OverlayMaterialMaxDrawDistance | `float` | The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance. |
| bIsEnableRetrieveDefaultMat | `bool` |  |
| bDisableLODBiasExt | `uint8` |  |

## Functions

### GetMaterials

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaterialIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaterialSlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetMaterialSlotNames

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsMaterialSlotNameValid

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaterialSlotName | `FName` |  |

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

### GetOverlayMaterial

Get the overlay material used by this instance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOverlayMaterial

Change the overlay material used by this instance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewOverlayMaterial | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### GetUseIndexedOverlayMaterials

Get UseIndexedOverlayMaterials

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetUseIndexedOverlayMaterials

Set UseIndexedOverlayMaterials

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewUseIndexedOverlayMaterials | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetUseOverlayMaterials

Get UseOverlayMaterials

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetUseOverlayMaterials

Set UseOverlayMaterials

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewUseOverlayMaterials | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetIndexedOverlayMaterials

Get IndexedOverlayMaterials

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIndexedOverlayMaterial

Set IndexedOverlayMaterials

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` |  |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetOverlayMaterialMaxDrawDistance

Change the overlay material max draw distance used by this instance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaxDrawDistance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetIndexedOverrideOutlineMaterials

Get IndexedOverrideOutlineMaterials

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIndexedOverrideOutlineMaterials

Set IndexedOverrideOutlineMaterials

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ElementIndex | `int32` |  |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### PrestreamTextures

Tell the streaming system to start loading all textures with all mip-levels.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Seconds | `float` | Number of seconds to force all mip-levels to be resident |
| bPrioritizeCharacterTextures | `bool` | Whether character textures should be prioritized for a while by the streaming system |
| CinematicTextureGroups | `int32` | Bitfield indicating which texture groups that use extra high-resolution mips |

**Return**

- Type: 
- Description: _None_

### SetScalarParameterValueOnMaterials

Material parameter setting and caching
	 Set all occurrences of Scalar Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| ParameterValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorParameterValueOnMaterials

Set all occurrences of Vector Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| ParameterValue | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### UpdateLodBiasByDeviceLevel

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UpdateLodBiasManually

绕过 ShouldUpdateLODBiasExt 闸门、用于手动刷新

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetLODBias

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

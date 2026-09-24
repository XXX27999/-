# USkeletalMesh

SkeletalMesh is geometry bound to a hierarchical skeleton of bones which can be animated for the purpose of deforming the mesh.
  Skeletal Meshes are built up of two parts; a set of polygons composed to make up the surface of the mesh, and a hierarchical skeleton which can be used to animate the polygons.
  The 3D models, rigging, and animations are created in an external modeling and animation application (3DSMax, Maya, Softimage, etc).

## Parents

- [UObject](./UObject.md)
- IInterface_CollisionDataProvider
- IInterface_AssetUserData

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Skeleton | `USkeleton *` | Skeleton of this skeletal mesh |
| bAllowCPUAccess | `bool` |  |
| bForceAllowCPUAccess | `bool` | Ignore "FreeSkeletalMeshBuffers" console value. |
| EncodeBits_Position | `int32` |  |
| EncodeBits_TexCoord | `int32` |  |
| EncodeBits_Normal | `int32` |  |
| EncodeBits_Generic | `int32` |  |
| EncodeBits_VertexColor | `int32` |  |
| EncodeSpeed | `int32` |  |
| DecodeSpeed | `int32` |  |
| ImportedBounds | [FBoxSphereBounds](../../cppstruct/F/FB/FBoxSphereBounds.md) | Original imported mesh bounds |
| ExtendedBounds | [FBoxSphereBounds](../../cppstruct/F/FB/FBoxSphereBounds.md) | Bounds extended by user values below |
| PositiveBoundsExtension | [FVector](../../cppstruct/F/FV/FVector.md) | Bound extension values in addition to imported bound in the positive direction of XYZ,<br>	 	positive value increases bound size and negative value decreases bound size.<br>	 	The final bound would be from [Imported Bound - Negative Bound] to [Imported Bound + Positive Bound]. |
| NegativeBoundsExtension | [FVector](../../cppstruct/F/FV/FVector.md) | Bound extension values in addition to imported bound in the negative direction of XYZ,<br>	 	positive value increases bound size and negative value decreases bound size.<br>	 	The final bound would be from [Imported Bound - Negative Bound] to [Imported Bound + Positive Bound]. |
| bIsStreamable | `bool` | Streamable flag, determine whether to split the lod serialization, WITH_STREAMING_SM_LOD |
| bCompressData | `bool` |  |
| IndirectLightingCachePositionOffset | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| NotInlineLODCount | `uint8` |  |
| Materials | `TArray < FSkeletalMaterial >` | List of materials applied to this mesh. |
| ReplaceMaterialInterface | `UMaterialInterface *` | Replace for async compile pso. |
| SkelMirrorTable | `TArray < FBoneMirrorInfo >` | List of bones that should be mirrored. |
| SkelMirrorAxis | `TEnumAsByte < EAxis :: Type >` |  |
| SkelMirrorFlipAxis | `TEnumAsByte < EAxis :: Type >` |  |
| CullingScreenSize | `float` | Culling screen size |
| LODInfo | `TArray < FSkeletalMeshLODInfo >` | Struct containing information for each LOD level, such as materials to use, and when use the LOD. |
| bUseAnyLODFeature | `bool` |  |
| PerLODBiasTypeInfo | `TArray < FMeshPerLODBiasArray >` | When autonomous or simulated pawn needs special LOD bias |
| bUseLODBiasExt | `bool` |  |
| bAutoUpdateLODBiasExt | `bool` |  |
| PerLODBiasTypeInfoExt | `TArray < FMeshLODBiasCondition >` |  |
| bUseFullPrecisionUVs | `uint32` | If true, use 32 bit UVs. If false, use 16 bit UVs to save memory |
| bUsedWithDynamicInstancing | `uint32` | Whether or not this mesh can be used with dynamic instancing. |
| bHasBeenSimplified | `uint32` | true if this mesh has ever been simplified with Simplygon. |
| bHasVertexColors | `uint32` | Whether or not the mesh has vertex colors |
| bEnablePerPolyCollision | `uint32` | Uses skinned data for collision data. Per poly collision cannot be used for simulation, in most cases you are better off using the physics asset |
| bEnableSelfCollision | `uint32` | Need self-collision in an aggregate. In most cases you don't need if the aggregate isn't containing the ragdoll. submit by elvisxu |
| BodySetup | `UBodySetup *` |  |
| PhysicsAsset | `UPhysicsAsset *` | Physics and collision information used for this USkeletalMesh, set up in Physics Asset Editor.<br>	 	This is used for per-bone hit detection, accurate bounding box calculation and ragdoll physics for example. |
| ShadowPhysicsAsset | `UPhysicsAsset *` | Physics asset whose shapes will be used for shadowing when components have bCastCharacterCapsuleDirectShadow or bCastCharacterCapsuleIndirectShadow enabled.<br>	  Only spheres and sphyl shapes in the physics asset can be supported.  The more shapes used, the higher the cost of the capsule shadows will be. |
| NodeMappingData | `TArray < UNodeMappingContainer * >` | Mapping data that is saved |
| LodModelsHasSkinweight | `bool` | use for FStaticLODModel Serialize SkinweightProfilesData |
| MorphTargets | `TArray < UMorphTarget * >` |  |
| ClothingAssets_DEPRECATED | `TArray < FClothingAssetData_Legacy >` | Legacy clothing asset data, will be converted to new assets after loading |
| PostProcessAnimBlueprint | `TSubclassOf < UAnimInstance >` | Animation Blueprint class to run as a post process for this mesh.<br>	   This blueprint will be ran before physics, but after the main<br>	   anim instance for any skeletal mesh component using this mesh. |
| MeshClothingAssets | `TArray < UClothingAssetBase * >` | Clothing assets imported to this mesh. May or may not be in use currently on the mesh.<br>	  Ordering not guaranteed, use the provided getters to access elements in this array<br>	  whenever possible |
| AssetUserData | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| Sockets | `TArray < USkeletalMeshSocket * >` | Array of named socket locations, set up in editor and used as a shortcut instead of specifying<br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent. |
| TemplateRetargetSource | `FName` |  |
| RefBoneNames | `TArray < FName >` |  |
| SkinWeightProfiles | `TArray < FSkinWeightProfileInfo >` | Set of skin weight profiles associated with this mesh |
| ScreenSizeCullingRoughDistance | `float` | Rough Distance of Screen size Culling |
| bCloseDraco | `bool` |  |
| AssetImportData | `UAssetImportData *` | Importing data and options used for this mesh |
| SourceFilePath_DEPRECATED | `FString` | Path to the resource used to construct this skeletal mesh |
| SourceFileTimestamp_DEPRECATED | `FString` | DateTime-stamp of the file from the last import |
| ThumbnailInfo | `UThumbnailInfo *` | Information for thumbnail rendering |
| bHasCustomDefaultEditorCamera | `bool` | Should we use a custom camera transform when viewing this mesh in the tools |
| DefaultEditorCameraLocation | [FVector](../../cppstruct/F/FV/FVector.md) | Default camera location |
| DefaultEditorCameraRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | Default camera rotation |
| DefaultEditorCameraLookAt | [FVector](../../cppstruct/F/FV/FVector.md) | Default camera look at |
| DefaultEditorCameraOrthoZoom | `float` | Default camera ortho zoom |
| OptimizationSettings | `TArray < FSkeletalMeshOptimizationSettings >` | Optimization settings used to simplify LODs of this mesh. |
| PreviewAttachedAssetContainer | [FPreviewAssetAttachContainer](../../cppstruct/F/FP/FPreviewAssetAttachContainer.md) | Attached assets component for this mesh |
| bPreviewDraco | `bool` |  |
| bUseHighPrecision | `bool` |  |
| SelectedEditorSection | `int32` | The section currently selected in the Editor. Used for highlighting |
| SelectedEditorMaterial | `int32` | The Material currently selected. need to remember this index for reimporting cloth |
| SelectedClothingSection | `int32` | The section currently selected for clothing. need to remember this index for reimporting cloth |
| FloorOffset | `float` | Height offset for the floor mesh in the editor |
| RetargetBasePose | `TArray < FTransform >` | This is buffer that saves pose that is used by retargeting |

## Functions

### RefreshBulkNotExistsLODCount

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBounds

Get the extended bounds of this mesh (imported bounds plus bounds extension)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetImportedBounds

Get the original imported bounds of the skel mesh

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNodeMappingContainer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceAsset | `UBlueprint *` |  |

**Return**

- Type: 
- Description: _None_

### GetRefBonePose

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRefBoneInfo

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FindSocket

Find a socket object in this SkeletalMesh by name.
	 	Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### AddDynamicSocket

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocket | `USkeletalMeshSocket *` |  |

**Return**

- Type: 
- Description: _None_

### FindSocketAndIndex

Find a socket object in this SkeletalMesh by name.
		Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.
	   Also returns the index for the socket allowing for future fast access via GetSocketByIndex()

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` |  |
| OutIndex | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### NumSockets

Returns the number of sockets available. Both on this mesh and it's skeleton.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSocketByIndex

Returns a socket by index. Max index is NumSockets(). The meshes sockets are accessed first, then the skeletons.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### IsSectionUsingCloth

Checks whether the provided section is using APEX cloth. if bCheckCorrespondingSections is true
	  disabled sections will defer to correspond sections to see if they use cloth (non-cloth sections
	  are disabled and another section added when cloth is enabled, using this flag allows for a check
	  on the original section to succeed)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSectionIndex | `int32` | Index to check |
| bCheckCorrespondingSections | `bool` | Whether to check corresponding sections for disabled sections |

**Return**

- Type: 
- Description: _None_

### AddCopySocket

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocket | `USkeletalMeshSocket *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

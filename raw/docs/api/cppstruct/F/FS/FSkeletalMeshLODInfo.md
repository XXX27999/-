# FSkeletalMeshLODInfo

Struct containing information for a particular LOD level, such as materials and info for when to use it.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ScreenSize | `float` | ScreenSize to display this LOD.<br>	  The screen size is based around the projected diameter of the bounding<br>	  sphere of the model. i.e. 0.5 means half the screen's maximum dimension. |
| LODHysteresis | `float` | Used to avoid 'flickering' when on LOD boundary. Only taken into account when moving from complex->simple. |
| LODMaterialMap | `TArray < int32 >` | Mapping table from this LOD's materials to the USkeletalMesh materials array. |
| UVOffsets | `TArray < FVector4 >` |  |
| bEnableShadowCasting_DEPRECATED | `TArray < bool >` | Per-section control over whether to enable shadow casting. |
| TriangleSortSettings | `TArray < FTriangleSortSettings >` |  |
| bHasBeenSimplified | `uint32` | Whether to disable morph targets for this LOD. |
| ReductionSettings | [FSkeletalMeshOptimizationSettings](./FSkeletalMeshOptimizationSettings.md) | Reduction settings to apply when building render data. |
| RemeshingSettings_DEPRECATED | [FSimplygonRemeshingSettings](./FSimplygonRemeshingSettings.md) | Remeshing settings to apply when building render data. |
| OptimizationSettings | [FGroupedSkeletalOptimizationSettings](../FG/FGroupedSkeletalOptimizationSettings.md) |  |
| RemovedBones_DEPRECATED | `TArray < FName >` | This has been removed in editor. We could re-apply this in import time or by mesh reduction utilities |
| BonesToRemove | `TArray < FBoneReference >` | Bones which should be removed from the skeleton for the LOD level |
| BakePose | `UAnimSequence *` | Pose which should be used to reskin vertex influences for which the bones will be removed in this LOD level, uses ref-pose by default |
| SourceImportFilename | `FString` | The filename of the file tha was used to import this LOD if it was not auto generated. |
| bHasPerLODVertexColors | `uint32` |  |

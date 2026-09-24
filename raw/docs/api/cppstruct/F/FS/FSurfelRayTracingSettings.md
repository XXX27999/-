# FSurfelRayTracingSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bAllowSurfelRayTracing | `uint32` | Whether to allow surfel ray tracing for ray traced dynamic indirect lighting and ambient occlusion. |
| SurfelVoxelSize | [FVector](../FV/FVector.md) | The size in unreal unit of a voxel. |
| SurfelHierarchyDimension | [FIntVector](../FI/FIntVector.md) | The size of the dimension of Surfel Bricks. Each brick contain 4x4x4 voxels. |
| IrradianceVolumeCellSize | [FVector](../FV/FVector.md) | The cell world size of the dimension of Surfel Irradiance Volume. |
| IrradianceVolumeDimension | [FIntVector](../FI/FIntVector.md) | The size of the dimension of Surfel Irradiance Volume. |
| IrradianceVolumeMipLevels | `uint32` | The number of mip levels of Surfel Irradiance Volume. |
| IrradianceMipScale | [FVector4](../FV/FVector4.md) | The brick world size scale of each mip levels of Surfel Irradiance Volume. |
| IrradianceVolumeOffset | [FVector](../FV/FVector.md) | The position offset of Surfel Irradiance Volume. |
| IrradianceVolumeCellDim | `int32` | The number of positions where a probe can be in the Irradiance Volume Cell. Value 5 means 5x5x5 positions. |
| SurfelInjectSingleSize | `int32` | The size n of inject single mesh to Hierarchical Surfel of Surfel Bricks. Each brick contains 4x4x4 voxels. Default n=16 means 16x16x16 bricks. |
| SurfelInjectSingleDistance | `float` | The distance within which a primitive can be inject into the surfel. |
| SurfelPoolInitScale | `int32` | The init size of the sparse surfel pool. Default 1x is 16 MB. Turn larger the pool size to avoid losing GI when resizing the pool, but consume more video memory. |
| bSupportEmissive | `uint32` | Whether emissive object should affect GI |
| bSupportTOD | `uint32` | Whether GI should support time of day, turning this off will cause significant delay of GI convergence in scenes with TOD |

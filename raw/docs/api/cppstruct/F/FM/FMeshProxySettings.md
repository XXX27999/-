# FMeshProxySettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ScreenSize | `int32` | Screen size of the resulting proxy mesh in pixels |
| MaterialSettings | [FMaterialProxySettings](./FMaterialProxySettings.md) | Material simplification |
| TextureWidth_DEPRECATED | `int32` |  |
| TextureHeight_DEPRECATED | `int32` |  |
| bExportNormalMap_DEPRECATED | `bool` |  |
| bExportMetallicMap_DEPRECATED | `bool` |  |
| bExportRoughnessMap_DEPRECATED | `bool` |  |
| bExportSpecularMap_DEPRECATED | `bool` |  |
| bCalculateCorrectLODModel | `bool` | Determines whether or not the correct LOD models should be calculated given the source meshes and transition size |
| MergeDistance | `float` | Distance at which meshes should be merged together, this can close gaps like doors and windows in distant geometry |
| HardAngleThreshold | `float` | Angle at which a hard edge is introduced between faces |
| LightMapResolution | `int32` | Lightmap resolution |
| bComputeLightMapResolution | `bool` | If ticked will compute the lightmap resolution by summing the dimensions for each mesh included for merging |
| bRecalculateNormals | `bool` | Whether Simplygon should recalculate normals, otherwise the normals channel will be sampled from the original mesh |
| bBakeVertexData_DEPRECATED | `bool` |  |
| bUseLandscapeCulling | `bool` | Whether or not to use available landscape geometry to cull away invisible triangles |
| bAssignLODGroup | `bool` | Choose whether you want to apply LODs to the generated mesh or not. |
| LandscapeCullingPrecision | `TEnumAsByte < ELandscapeCullingPrecision :: Type >` | Level of detail of the landscape that should be used for the culling |
| LODGroupIndex | `int32` |  |
| bAggregateMeshes | `bool` |  |
| AggregatorMode | [EChartAggregationMode](../../../cppenum/E/EC/EChartAggregationMode.md) |  |
| bUseCustomHemisphere | `bool` |  |
| bUseTargetTriangleNumber | `bool` |  |
| TargetTriangleNumber | `int32` |  |
| LODSelectionType | [EMeshLODSelectionType](../../../cppenum/E/EM/EMeshLODSelectionType.md) |  |
| SpecificLOD | `int32` |  |
| bIncludeHISMMesh | `bool` |  |
| bHalfVoxelSize | `bool` |  |
| ExpectedQualityLimit | [FExpectedQuality](../FE/FExpectedQuality.md) | Render quality control for certain devicesplatforms, if limit > actual, primitive won't be rendered. |
| bOverrideVoxelSize | `uint8` | If true, Spatial Sampling Distance will not be automatically computed based on geometry and you must set it directly |
| VoxelSize | `float` | Override when converting multiple meshes for proxy LOD merging. Warning, large geometry with small sampling has very high memory costs |
| UnresolvedGeometryColor | [FColor](../FC/FColor.md) | Base color assigned to LOD geometry that can't be associated with the source geometry: e.g. doors and windows that have been closed by the Merge Distance |
| bOverrideTransferDistance | `bool` | Enable an override for material transfer distance |
| MaxRayCastDist | `float` | Override search distance used when discovering texture values for simplified geometry. Useful when non-zero Merge Distance setting generates new geometry in concave corners. |
| bUseHardAngleThreshold | `bool` | Enable the use of hard angle based vertex splitting |
| NormalCalculationMethod | `TEnumAsByte < EProxyNormalComputationMethod :: Type >` | Controls the method used to calculate the normal for the simplified geometry |
| bAllowAdjacency | `bool` | Whether to allow adjacency buffers for tessellation in the merged mesh |
| bAllowDistanceField | `bool` | Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance. |
| bReuseMeshLightmapUVs | `bool` | Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set. |
| bCreateCollision | `bool` | Whether to generate collision for the merged mesh |
| bAllowVertexColors | `bool` | Whether to allow vertex colors saved in the merged mesh |
| bGenerateLightmapUVs | `bool` | Whether to generate lightmap uvs for the merged mesh |

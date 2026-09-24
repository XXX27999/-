# FMeshReductionSettings

Settings used to reduce a mesh.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BaseLODModel | `int32` | Source Index. The index into source models from which to generate the LOD from |
| MetricToUse | [EOptimizationMetric](../../../cppenum/E/EO/EOptimizationMetric.md) | Optimize the mesh based on the following metric option |
| PercentTriangles | `float` | Percentage of triangles to keep. 1.0 = no reduction, 0.0 = no triangles. |
| ScreenSize | `float` |  |
| MaxDeviation | `float` | The maximum distance in object space by which the reduced mesh may deviate from the original mesh. |
| PixelError | `float` | The amount of error in pixels allowed for this LOD. |
| WeldingThreshold | `float` | Threshold in object space at which vertices are welded together. |
| SilhouetteImportance | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values minimize change to border edges. |
| TextureImportance | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values reduce texture stretching. |
| ShadingImportance | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values try to preserve normals better. |
| VertexColorImportance | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values minimize change to vertex color data. |
| bRecalculateNormals | `bool` |  |
| HardAngleThreshold | `float` | Angle at which a hard edge is introduced between faces. |
| bActive_DEPRECATED | `bool` |  |
| bGenerateUniqueLightmapUVs | `bool` |  |
| bKeepSymmetry | `bool` |  |
| bVisibilityAided | `bool` |  |
| bCullOccluded | `bool` |  |
| VisibilityAggressiveness | `TEnumAsByte < EMeshFeatureImportance :: Type >` | Higher values generates fewer samples |
| bUseVertexWeights | `bool` | Vertex colors are converted to weights. The weights are used<br>	- Red: Vertices will be less important |
| bSimplifyMaterials | `bool` | The following will create a material proxy |
| MaterialLODSettings_DEPRECATED | [FSimplygonMaterialLODSettings](../FS/FSimplygonMaterialLODSettings.md) |  |
| MaterialProxySettings | [FMaterialProxySettings](./FMaterialProxySettings.md) | Material Proxy for LODs |

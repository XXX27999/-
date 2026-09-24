# FMeshMergingSettings

Mesh merging settings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bGenerateLightMapUV | `bool` | Whether to generate lightmap UVs for a merged mesh |
| TargetLightMapResolution | `int32` | Target lightmap resolution |
| bComputedLightMapResolution | `bool` | Whether or not the lightmap resolution should be computed by summing the lightmap resolutions for the input Mesh Components |
| bImportVertexColors_DEPRECATED | `bool` | Whether we should import vertex colors into merged mesh |
| bPivotPointAtZero | `bool` | Whether merged mesh should have pivot at world origin, or at first merged component otherwise |
| bMergePhysicsData | `bool` | Whether to merge physics data (collision primitives) |
| bAssignLODGroup | `bool` |  |
| LODGroupIndex | `int32` |  |
| bMergeMaterials | `bool` | Whether to merge source materials into one flat material, ONLY available when merging a single LOD level, see LODSelectionType |
| MaterialSettings | [FMaterialProxySettings](./FMaterialProxySettings.md) | Material simplification |
| bBakeVertexDataToMesh | `bool` | Whether or not vertex data such as vertex colours should be baked into the resulting mesh |
| bUseVertexDataForBakingMaterial | `bool` | Whether or not vertex data such as vertex colours should be used when baking out materials |
| bUseTextureBinning | `bool` |  |
| bReuseMeshLightmapUVs | `bool` | Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set. |
| bMergeEquivalentMaterials | `bool` | Whether to attempt to merge materials that are deemed equivalent. This can cause artifacts in the merged mesh if world positionactor position etc. is used to determine output color. |
| OutputUVs | [EUVOutput](../../../cppenum/E/EU/EUVOutput.md) | Whether to output the specified UV channels into the merged mesh (only if the source meshes contain valid UVs for the specified channel) |
| GutterSize | `int32` | Whether to output the specified UV channels into the merged mesh (only if the source meshes contain valid UVs for the specified channel)<br>	 The gutter (in texels) to add to each sub-chart for our baked-out material for the top mip level |
| bCalculateCorrectLODModel_DEPRECATED | `bool` |  |
| LODSelectionType | [EMeshLODSelectionType](../../../cppenum/E/EM/EMeshLODSelectionType.md) |  |
| ExportSpecificLOD_DEPRECATED | `int32` |  |
| SpecificLOD | `int32` |  |
| bUseLandscapeCulling | `bool` | Whether or not to use available landscape geometry to cull away invisible triangles |
| bIncludeImposters | `bool` |  |
| bAllowDistanceField | `bool` | Whether to allow distance field to be computed for this mesh. Disable this to save memory if the merged mesh will only be rendered in the distance. |
| FilteredMinBoundsRadius | `float` |  |
| bDisableBorderSmear | `bool` |  |
| BorderSmearReplaceColor | [FLinearColor](../FL/FLinearColor.md) |  |
| CustomOutputSize | [FIntPoint](../FI/FIntPoint.md) |  |
| bExportNormalMap_DEPRECATED | `bool` | Whether to export normal maps for material merging |
| bExportMetallicMap_DEPRECATED | `bool` | Whether to export metallic maps for material merging |
| bExportRoughnessMap_DEPRECATED | `bool` | Whether to export roughness maps for material merging |
| bExportSpecularMap_DEPRECATED | `bool` | Whether to export specular maps for material merging |
| MergedMaterialAtlasResolution_DEPRECATED | `int32` | Merged material texture atlas resolution |

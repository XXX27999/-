# FLevelSimplificationDetails

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bCreatePackagePerAsset | `bool` | Whether to create separate packages for each generated asset. All in map package otherwise |
| DetailsPercentage | `float` | Percentage of details for static mesh proxy |
| StaticMeshMaterialSettings | [FMaterialProxySettings](../FM/FMaterialProxySettings.md) | Landscape material simplification |
| bOverrideLandscapeExportLOD | `bool` |  |
| LandscapeExportLOD | `int32` | Landscape LOD to use for static mesh generation, when not specified 'Max LODLevel' from landscape actor will be used |
| LandscapeMaterialSettings | [FMaterialProxySettings](../FM/FMaterialProxySettings.md) | Landscape material simplification |
| bBakeFoliageToLandscape | `bool` | Whether to bake foliage into landscape static mesh texture |
| bBakeGrassToLandscape | `bool` | Whether to bake grass into landscape static mesh texture |
| bGenerateMeshNormalMap_DEPRECATED | `bool` |  |
| bGenerateMeshMetallicMap_DEPRECATED | `bool` |  |
| bGenerateMeshRoughnessMap_DEPRECATED | `bool` |  |
| bGenerateMeshSpecularMap_DEPRECATED | `bool` |  |
| bGenerateLandscapeNormalMap_DEPRECATED | `bool` |  |
| bGenerateLandscapeMetallicMap_DEPRECATED | `bool` |  |
| bGenerateLandscapeRoughnessMap_DEPRECATED | `bool` |  |
| bGenerateLandscapeSpecularMap_DEPRECATED | `bool` |  |
| bUseLandscapeCulling | `bool` | Whether or not to use available landscape geometry to cull away invisible triangles |
| LandscapeCullingPrecision | `TEnumAsByte < ELandscapeCullingPrecision :: Type >` | Level of detail of the landscape that should be used for the culling |
| bUseScreenSize | `bool` |  |
| ScreenSize | `uint32` |  |
| bUseTargetTriangleNumber | `bool` |  |
| TargetTriangleNumber | `uint32` |  |
| LODSelectionType | [EMeshLODSelectionType](../../../cppenum/E/EM/EMeshLODSelectionType.md) |  |
| SpecificLOD | `int32` |  |
| UnresolvedGeometryColor | [FColor](../FC/FColor.md) | Base color assigned to LOD geometry that can't be associated with the source geometry: e.g. doors and windows that have been closed by the Merge Distance |
| bReuseMeshLightmapUVs | `bool` | Whether to attempt to re-use the source mesh's lightmap UVs when baking the material or always generate a new set. |
| bUseHardAngleThreshold | `bool` | Enable the use of hard angle based vertex splitting |
| HardAngleThreshold | `float` | Angle at which a hard edge is introduced between faces |
| NormalCalculationMethod | `TEnumAsByte < EProxyNormalComputationMethod :: Type >` | Controls the method used to calculate the normal for the simplified geometry |
| ExpectedQualityLimit | [FExpectedQuality](../FE/FExpectedQuality.md) | Render quality control for certain devicesplatforms, if limit > actual, primitive won't be rendered. |
| bLodGenerateSubLevel | `bool` |  |
| DefaultCullScreenSize | `float` |  |
| bIncludeHISMMesh | `bool` |  |
| bHalfVoxelSize | `bool` |  |

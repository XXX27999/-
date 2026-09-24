# FMeshBuildSettings

Settings applied when building a mesh.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bUseMikkTSpace | `bool` | If true, degenerate triangles will be removed. |
| bRecomputeNormals | `bool` | If true, normals in the raw mesh are ignored and recomputed. |
| bRecomputeTangents | `bool` | If true, tangents in the raw mesh are ignored and recomputed. |
| bRemoveDegenerates | `bool` | If true, degenerate triangles will be removed. |
| bBuildAdjacencyBuffer | `bool` | Required for PNT tessellation but can be slow. Recommend disabling for larger meshes. |
| bBuildReversedIndexBuffer | `bool` | Required to optimize mesh in mirrored transform. Double index buffer size. |
| bIgnoreTriangleOrderOptimization | `bool` |  |
| bUseHighPrecisionTangentBasis | `bool` | If true, Tangents will be stored at 16 bit vs 8 bit precision. |
| bUseFullPrecisionUVs | `bool` | If true, UVs will be stored at full floating point precision. |
| bGenerateLightmapUVs | `bool` |  |
| MinLightmapResolution | `int32` |  |
| SrcLightmapIndex | `int32` |  |
| DstLightmapIndex | `int32` |  |
| BuildScale_DEPRECATED | `float` |  |
| BuildScale3D | [FVector](../FV/FVector.md) | The local scale applied when building the mesh |
| DistanceFieldResolutionScale | `float` | Scale to apply to the mesh when allocating the distance field volume texture.<br>	  The default scale is 1, which is assuming that the mesh will be placed unscaled in the world. |
| bGenerateDistanceFieldAsIfTwoSided | `bool` | Whether to generate the distance field treating every triangle hit as a front face.<br>	  When enabled prevents the distance field from being discarded due to the mesh being open, but also lowers Distance Field AO quality. |
| DistanceFieldBias_DEPRECATED | `float` |  |
| DistanceFieldReplacementMesh | `UStaticMesh *` |  |

# FStaticMeshOptimizationSettings

Old optimization settings.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ReductionMethod | `TEnumAsByte < enum EOptimizationType >` | The method to use when optimizing the skeletal mesh LOD |
| NumOfTrianglesPercentage | `float` | If ReductionMethod equals SMOT_NumOfTriangles this value is the ratio of triangles [0-1] to remove from the mesh |
| MaxDeviationPercentage | `float` | If ReductionMethod equals SMOT_MaxDeviation this value is the maximum deviation from the base mesh as a percentage of the bounding sphere. |
| WeldingThreshold | `float` | The welding threshold distance. Vertices under this distance will be welded. |
| bRecalcNormals | `bool` | Whether Normal smoothing groups should be preserved. If false then NormalsThreshold is used |
| NormalsThreshold | `float` | If the angle between two triangles are above this value, the normals will not be<br>	smooth over the edge between those two triangles. Set in degrees. This is only used when PreserveNormals is set to false |
| SilhouetteImportance | `uint8` | How important the shape of the geometry is (EImportanceLevel). |
| TextureImportance | `uint8` | How important texture density is (EImportanceLevel). |
| ShadingImportance | `uint8` | How important shading quality is. |

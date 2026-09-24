# FHLODGroup

LODDrawDistanceScale 等参数。
   - bClusterBasedMode 不在 Group 内独立配置，全局服从 r.LevelReorgHLOD.ClusterBasedMode。

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` |  |
| GroupName | `FName` |  |
| StaticMeshes | `TArray < TSoftObjectPtr < UStaticMesh > >` | 参与该 Group 的 StaticMesh 集合（编辑用资产引用，运行期取 ToSoftObjectPath().ToString() 做精确字符串匹配） |
| ProxyBaseMaterial | `TSoftObjectPtr < UMaterialInterface >` | ProxyMesh 烘焙用 BaseMaterial |
| OverrideDrawDistance | `float` | DrawDistance value to use when the inline toggle is checked. Takes precedence over LODSetup.bUseOverrideDrawDistance and skips LODDrawDistanceScale. |
| bUseOverrideDrawDistance | `bool` |  |
| LODDrawDistanceScale | `float` |  |
| DesiredGridSize | `float` |  |
| DesiredGridOffset | `float` |  |
| MaxBoundForHLOD | `float` |  |
| MinSubActorsForHLOD | `int32` |  |
| ClusterBoundsMinRadius | `float` |  |
| ClusterTreeLevel | `int32` |  |
| ClusterMinInstances | `int32` |  |
| MinClustersPerLODActor | `int32` |  |
| MaxClustersPerLODActor | `int32` |  |
| LOD0ReduceFactor | `float` | LOD0 percentage-based reduction factor (OriginalTriangles  this value). Corresponds to global r.HLOD.ProxyMeshLOD0ReduceFactor |
| PerVolumeTriangles | `float` | Volume-based: triangles allowed per cubic-meter of Bounds. Corresponds to global r.HLOD.ProxyMeshPerVolumeTraingles |
| LODReduceFactor | `float` | LOD1~N successive reduction factor. Corresponds to global r.HLOD.ProxyMeshReduceFactor |
| LODMinTriangles | `int32` | Minimum triangle threshold (no further LOD generated below this). Corresponds to global r.HLOD.ProxyMeshLODMinTriangles |
| LODMaxCount | `int32` | Maximum LOD level count. Corresponds to global r.HLOD.ProxyMeshLODMax |
| ProxyMeshLOD1SwitchDistance | `float` | Distance (in cm) at which ProxyMesh switches from LOD0 to LOD1. Overrides legacy triangle-count-based ScreenSize calculation. |
| bOverrideProxyMeshLOD1SwitchDistance | `bool` |  |
| ProxyMeshCullingDistance | `float` | Distance (in cm) at which ProxyMesh is culled (not rendered). Overrides legacy CVar-based culling distance. |
| bOverrideProxyMeshCullingDistance | `bool` |  |
| bEmissiveMap | `bool` | Whether to bake Emissive channel into ProxyMesh material for this Group. |
| EmissiveTextureSize | [FIntPoint](../FI/FIntPoint.md) | Override Emissive texture size (only used when bEmissiveMap=true) |

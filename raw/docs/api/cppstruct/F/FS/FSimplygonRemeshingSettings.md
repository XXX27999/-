# FSimplygonRemeshingSettings

Settings used to ProxyLOD mesh(es).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bActive | `bool` |  |
| ScreenSize | `int32` | Screen size of the resulting proxy mesh in pixel size |
| bRecalculateNormals | `bool` | Should Simplygon recalculate normals for the proxy mesh? |
| HardAngleThreshold | `float` | Angle at which a hard edge is introduced between faces. |
| MergeDistance | `int32` |  |
| bUseClippingPlane | `bool` |  |
| ClippingLevel | `float` |  |
| AxisIndex | `int32` |  |
| bPlaneNegativeHalfspace | `bool` |  |
| bUseMassiveLOD | `bool` |  |
| bUseAggregateLOD | `bool` |  |
| MaterialLODSettings | [FSimplygonMaterialLODSettings](./FSimplygonMaterialLODSettings.md) |  |

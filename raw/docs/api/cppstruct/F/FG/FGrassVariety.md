# FGrassVariety

## Fields

| Name | Type | Description |
| --- | --- | --- |
| GrassMesh | `UStaticMesh *` |  |
| GrassDensity | `float` | Instances per 10 square meters. |
| bUseGrid | `bool` | If true, use a jittered grid sequence for placement, otherwise use a halton sequence. |
| PlacementJitter | `float` |  |
| StartCullDistance | `int32` | The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables. |
| EndCullDistance | `int32` | The distance where instances will have completely faded out when using a PerInstanceFadeAmount material node. 0 disables.<br>	  When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all. |
| MinLOD | `int32` | Specifies the smallest LOD that will be used for this component.<br>	  If -1 (default), the MinLOD of the static mesh asset will be used instead. |
| Scaling | [EGrassScaling](../../../cppenum/E/EG/EGrassScaling.md) | Specifies grass instance scaling type |
| ScaleX | [FFloatInterval](../FF/FFloatInterval.md) | Specifies the range of scale, from minimum to maximum, to apply to a grass instance's X Scale property |
| ScaleY | [FFloatInterval](../FF/FFloatInterval.md) | Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Y Scale property |
| ScaleZ | [FFloatInterval](../FF/FFloatInterval.md) | Specifies the range of scale, from minimum to maximum, to apply to a grass instance's Z Scale property |
| RandomRotation | `bool` | Whether the grass instances should be placed at random rotation (true) or all at the same rotation (false) |
| AlignToSurface | `bool` | Whether the grass instances should be tilted to the normal of the landscape (true), or always vertical (false) |
| bUseLandscapeLightmap | `bool` | Whether to use the landscape's lightmap when rendering the grass. |
| bUseVolumeProbeGI | `bool` |  |
| LightingChannels | [FLightingChannels](../FL/FLightingChannels.md) | Lighting channels that the grass will be assigned. Lights with matching channels will affect the grass.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| bReceivesDecals | `bool` | Whether the grass instances should receive decals. |

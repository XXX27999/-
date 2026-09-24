# FAnimNode_ApplyAdditive

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Base | `FPoseLink` |  |
| Additive | `FPoseLink` |  |
| Alpha | `float` |  |
| AlphaScaleBias | [FInputScaleBias](../FI/FInputScaleBias.md) |  |
| LODThreshold | `int32` | Max LOD that this node is allowed to run<br>	  For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	  when the component LOD becomes 3, it will stop updateevaluate<br>	  currently transition would be issue and that has to be re-visited |
| ActualAlpha | `float` |  |

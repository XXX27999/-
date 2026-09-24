# FAnimNode_RotationOffsetBlendSpace

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BasePose | `FPoseLink` |  |
| LODThreshold | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| bIsLODEnabled | `bool` |  |
| Alpha | `float` |  |
| AlphaScaleBias | [FInputScaleBias](../FI/FInputScaleBias.md) |  |
| ActualAlpha | `float` |  |

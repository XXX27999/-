# FAnimNode_AimOffsetLookAt

This node uses a source transform of a socket on the skeletal mesh to automatically calculate
  Yaw and Pitch directions for a referenced aim offset given a point in the world to look at.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BasePose | `FPoseLink` |  |
| LODThreshold | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| bIsLODEnabled | `bool` |  |
| LookAtLocation | [FVector](../FV/FVector.md) | Location, in world space to look at |
| SourceSocketName | `FName` | Socket to treat as the look at source |
| PivotSocketName | `FName` | Socket to treat as the look at pivot (optional). This will overwrite the translation of the source socket transform to better match the lookat direction |
| SocketAxis | [FVector](../FV/FVector.md) | Axis in the socket transform to consider the 'forward' or look at axis |
| Alpha | `float` | Amount of this node to blend into the output pose |
| SocketBoneReference | `FBoneReference` | Cached reference to the source socket's bone |
| SocketLocalTransform | [FTransform](../FT/FTransform.md) | Cached local transform of the source socket |
| PivotSocketBoneReference | `FBoneReference` | Cached reference to the pivot socket's bone |
| PivotSocketLocalTransform | [FTransform](../FT/FTransform.md) | Cached local transform of the pivot socket |

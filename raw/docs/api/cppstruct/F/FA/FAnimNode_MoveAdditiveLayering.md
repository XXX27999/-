# FAnimNode_MoveAdditiveLayering

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BasePose | `FPoseLink` |  |
| TargetPose | `FPoseLink` |  |
| RefPose | `FPoseLink` |  |
| bFixRootRotation | `bool` |  |
| ArmMeshSpaceAlphaL | `float` |  |
| ArmMeshSpaceAlphaR | `float` |  |
| ArmSwayAlphaL | `float` |  |
| ArmSwayAlphaR | `float` |  |
| HandAlphaL | `float` |  |
| HandAlphaR | `float` |  |
| UpperPoseOverrideLayerSetup | `TArray < FInputBlendPose >` | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |
| SpineLocalSpaceAdditiveLayerSetup | `TArray < FInputBlendPose >` |  |
| MeshSpaceAdditiveLayerSetup_Left | `TArray < FInputBlendPose >` |  |
| MeshSpaceAdditiveLayerSetup_Right | `TArray < FInputBlendPose >` |  |
| ArmLocalSpaceAdditiveLayerSetup | `TArray < FInputBlendPose >` |  |
| bEvaluateLayer0 | `bool` |  |
| bEvaluateLayer1 | `bool` |  |
| bEvaluateLayer2 | `bool` |  |
| bEvaluateLayer3 | `bool` |  |
| SkeletonGuid | [FGuid](../FG/FGuid.md) |  |
| VirtualBoneGuid | [FGuid](../FG/FGuid.md) |  |
| UpperPoseOverrideData | [FMoveAdditiveLayeringData](../FM/FMoveAdditiveLayeringData.md) |  |
| SpineLocalSpaceAdditiveData | [FMoveAdditiveLayeringData](../FM/FMoveAdditiveLayeringData.md) |  |
| MeshSpaceAdditiveData_Left | [FMoveAdditiveLayeringData](../FM/FMoveAdditiveLayeringData.md) |  |
| MeshSpaceAdditiveData_Right | [FMoveAdditiveLayeringData](../FM/FMoveAdditiveLayeringData.md) |  |
| ArmLocalSpaceAdditiveData | [FMoveAdditiveLayeringData](../FM/FMoveAdditiveLayeringData.md) |  |
| bOutputTargetPose | `bool` |  |
| bOutputRefPose | `bool` |  |
| bOutputLocalSpaceAdditivePose | `bool` |  |
| bOutputMeshSpaceAdditivePose | `bool` |  |

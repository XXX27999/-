# FAnimNode_LayeredBoneBlend

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BasePose | `FPoseLink` | The source pose |
| BlendPoses | `TArray < FPoseLink >` | Each layer's blended pose |
| LayerSetup | `TArray < FInputBlendPose >` | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |
| BlendWeights | `TArray < float >` | The weights of each layer |
| bMeshSpaceRotationBlend | `bool` | Whether to blend bone rotations in mesh space or in local space |
| bBlendRootMotionBasedOnRootBone | `bool` | Whether to incorporate the per-bone blend weight of the root bone when lending root motion |
| CurveBlendOption | `TEnumAsByte < enum ECurveBlendOption :: Type >` | How to blend the layers together |
| bHasRelevantPoses | `bool` |  |
| SkeletonGuid | [FGuid](../FG/FGuid.md) |  |
| VirtualBoneGuid | [FGuid](../FG/FGuid.md) |  |
| PerBoneBlendWeights | `TArray < FPerBoneBlendWeight >` |  |
| DesiredBoneBlendWeightsInitMesh | `TWeakObjectPtr < USkeletalMesh >` |  |

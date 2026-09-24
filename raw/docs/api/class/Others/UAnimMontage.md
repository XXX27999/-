# UAnimMontage

Any property you're adding to AnimMontage and parent class has to be considered for Child Asset

  Child Asset is considered to be only asset mapping feature using everything else in the class
  For example, you can just use all parent's setting  for the montage, but only remap assets
  This isn't magic bullet unfortunately and it is consistent effort of keeping the data synced with parent
  If you add new property, please make sure those property has to be copied for children.
  If it does, please add the copy in the function RefreshParentAssetData

## Parents

- UAnimCompositeBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BlendIn | `FAlphaBlend` | Blend in option. |
| BlendInTime_DEPRECATED | `float` |  |
| BlendOut | `FAlphaBlend` | Blend out option. This is only used when it blends out itself. If it's interrupted by other montages, it will use new montage's BlendIn option to blend out. |
| BlendOutTime_DEPRECATED | `float` |  |
| BlendOutTriggerTime | `float` | Time from Sequence End to trigger blend out.<br>	  <0 means using BlendOutTime, so BlendOut finishes as Montage ends.<br>	  >=0 means using 'SequenceEnd - BlendOutTriggerTime' to trigger blend out. |
| FilteredBones | [FInputBlendPose](../../cppstruct/F/FI/FInputBlendPose.md) |  |
| bAccumulateCurveSlotWeight | `bool` |  |
| bCheckSlotNodeRelevant | `bool` |  |
| SyncGroup | `FName` | If you're using marker based sync for this montage, make sure to add sync group name. For now we only support one group |
| SyncSlotIndex | `int32` | wip: until we have UI working |
| MarkerData | `FMarkerSyncData` |  |
| CompositeSections | `TArray < FCompositeSection >` |  |
| SlotAnimTracks | `TArray < struct FSlotAnimationTrack >` |  |
| BranchingPoints_DEPRECATED | `TArray < struct FBranchingPoint >` |  |
| bEnableRootMotionTranslation | `bool` | If this is on, it will allow extracting root motion translation. DEPRECATED in 4.5 root motion is controlled by anim sequences |
| bEnableRootMotionRotation | `bool` | If this is on, it will allow extracting root motion rotation. DEPRECATED in 4.5 root motion is controlled by anim sequences |
| bIsFarFromRoot | `bool` |  |
| RootMotionRootLock | `TEnumAsByte < ERootMotionRootLock :: Type >` | Root Bone will be locked to that position when extracting root motion. DEPRECATED in 4.5 root motion is controlled by anim sequences |
| bEnableMontageRandomSectionJump | `bool` |  |
| bRandomLoopJump | `bool` |  |
| RandomSectionNum | `int32` |  |
| RandomJumpTimes | `int32` |  |
| RetargetSource | `FName` |  |
| BranchingPointMarkers | `TArray < FBranchingPointMarker >` | Cached list of Branching Point markers |
| CurveForRootPosition | `UCurveVector *` | 当在对Montage 本身进行构造Root 位置曲线后才会被携带的三个曲线 |
| CurveForRootRotation | `UCurveVector *` |  |
| CurveForRootScale | `UCurveVector *` |  |
| BranchingPointStateNotifyIndices | `TArray < int32 >` | Keep track of which AnimNotify_State are marked as BranchingPoints, so we can update their state when the Montage is ticked |
| IgnoreNotifyType | `TArray < FString >` | Names of notifies should be ignore in Montage. |
| TimeStretchCurve | [FTimeStretchCurve](../../cppstruct/F/FT/FTimeStretchCurve.md) |  |
| TimeStretchCurveName | `FName` | Name of optional TimeStretchCurveName to look for in Montage. |
| PreviewBasePose | `UAnimSequence *` | Preview Base pose for additive BlendSpace |
| BoneRetargetBaseMesh | `USkeletalMesh *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

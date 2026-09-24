# UAnimSequence

## Parents

- [UAnimSequenceBase](./UAnimSequenceBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NumFrames | `int32` | Number of raw frames in this sequence (not used by engine - just for informational purposes). |
| TrackToSkeletonMapTable | `TArray < struct FTrackToSkeletonMap >` | In the future, maybe keeping RawAnimSequenceTrack + TrackMap as one would be good idea to avoid inconsistent array size<br>	  TrackToSkeletonMapTable(i) should contains  track mapping data for RawAnimationData(i). |
| OverrideChunkFreeTime | `float` |  |
| OverrideFollowingChunkSize | `float` |  |
| bIshugeAnim | `uint8` |  |
| bImmediateLoadChunk | `uint8` |  |
| bForceUseStreamable | `uint8` |  |
| bUseStreamable | `uint8` |  |
| StreamableAdvanceConfig | `bool` |  |
| StreamableFirstChunkSize | `float` |  |
| StreamableFollowingChunkSize | `float` |  |
| bIgnoreDirectoryLimit | `bool` |  |
| AdditiveAnimType | `TEnumAsByte < enum EAdditiveAnimationType >` | Additive animation type. |
| RefPoseType | `TEnumAsByte < enum EAdditiveBasePoseType >` | Additive refrerence pose type. Refer above enum type |
| RefPoseSeq | `UAnimSequence *` | Additive reference animation if it's relevant - i.e. AnimScaled or AnimFrame |
| RefFrameIndex | `int32` | Additve reference frame if RefPoseType == AnimFrame |
| EncodingPkgVersion | `int32` | The version of the global encoding package used at the time of import |
| RetargetSource | `FName` | Base pose to use when retargeting |
| Interpolation | [EAnimInterpolationType](../../cppenum/E/EA/EAnimInterpolationType.md) | This defines how values between keys are calculated |
| bEnableRootMotion | `bool` | If this is on, it will allow extracting of root motion |
| RootMotionRootLock | `TEnumAsByte < ERootMotionRootLock :: Type >` | Root Bone will be locked to that position when extracting root motion. |
| bForceRootLock | `bool` | Force Root Bone Lock even if Root Motion is not enabled |
| bRootMotionSettingsCopiedFromMontage | `bool` | Have we copied root motion settings from an owning montage |
| AuthoredSyncMarkers | `TArray < FAnimSyncMarker >` | Authored Sync markers |
| CurveForRootPosition | `UCurveVector *` | 当在对Sequence 本身进行构造Root 位置曲线后才会被携带的三个曲线和新的Sequence |
| CurveForRootRotation | `UCurveVector *` |  |
| CurveForRootScale | `UCurveVector *` |  |
| CreatedSequenceForRoot | `UAnimSequence *` |  |
| CurveForPositionRootSingleAxis | `TSoftObjectPtr < UCurveFloat >` |  |
| CurveForOnlySinglePosition | `TSoftObjectPtr < UCurveVector >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

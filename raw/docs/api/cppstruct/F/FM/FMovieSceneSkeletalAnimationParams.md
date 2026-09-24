# FMovieSceneSkeletalAnimationParams

For MovieSceneSkeletalAnimation MultipleDeviceGrade Feature End

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Animation | `UAnimSequenceBase *` | The animation this section plays |
| MultipleDeviceGradeAnimList | `TArray < FMovieSceneSkeletalAnimation_MultipleDeviceGrade >` |  |
| StartOffset | `float` | The offset into the beginning of the animation clip |
| EndOffset | `float` | The offset into the end of the animation clip |
| PlayRate | `float` | The playback rate of the animation clip |
| bReverse | `uint32` | Reverse the playback of the animation clip |
| SlotName | `FName` | The slot name to use for the animation |
| Weight | [FRichCurve](../FR/FRichCurve.md) | The weight curve for this animation section |
| BlendOutTime | `float` | BlendOutTimeWhenStop |
| bClearPose | `uint32` | clear the cached pose |
| bForceUseTPP | `uint32` | if use TPP when player is in Newfpp |
| bSetSequenceEvalReinitStartPosition | `uint32` | SetSequenceEvalReinit  to StartPosition |
| bApplySubAnim | `uint32` | Apply Anim To SubAnim |
| ApplyAvatarSlot | `TArray < int32 >` | Apply Anim To Avatar |
| DisableBoneResolve | `TArray < int32 >` | Apply Anim To SubAnim |
| bShouldUseWeight | `uint32` | If true, pass the Weight curve value through to SetMatineeAnimPositionInner to control animation blend |

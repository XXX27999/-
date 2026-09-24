# FAnimNode_BlendListBase

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BlendPose | `TArray < FPoseLink >` |  |
| BlendTime | `TArray < float >` |  |
| TransitionType | [EBlendListTransitionType](../../../cppenum/E/EB/EBlendListTransitionType.md) |  |
| BlendType | [EAlphaBlendOption](../../../cppenum/E/EA/EAlphaBlendOption.md) |  |
| CustomBlendCurve | `UCurveFloat *` |  |
| BlendProfile | `UBlendProfile *` |  |
| ResetFrameCountSubValue | `int32` |  |
| LastFrameCount | `uint64` |  |
| Blends | `TArray < struct FAlphaBlend >` |  |
| BlendWeights | `TArray < float >` |  |
| RemainingBlendTimes | `TArray < float >` |  |
| LastActiveChildIndex | `int32` |  |
| PerBoneSampleData | `TArray < FBlendSampleData >` |  |
| bResetChildOnActivation | `bool` | This reinitializes child pose when re-activated. For example, when active child changes |
| bResetChildOnBlendListChange | `bool` |  |

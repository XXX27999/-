# FAnimNode_SequencePlayer

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Sequence | `UAnimSequenceBase *` |  |
| bLoopAnimation | `bool` |  |
| bCheckNeedInitializeSupFirst | `bool` |  |
| PlayRate | `float` |  |
| StartPosition | `float` |  |
| ReversePlayRate | `bool` |  |
| bResetPlayTimeWhenReactivate | `bool` |  |
| bForceResetPlayTime | `bool` |  |
| CheckReactivateFrameCounterSubValue | `int32` |  |
| bShouldReinitPose | `bool` |  |
| ReInitPose | [FBonesTransfromsWithFPP](../FB/FBonesTransfromsWithFPP.md) |  |
| bResetToAdditivePose | `bool` |  |
| EnableSequenceBlend | `bool` |  |
| SequenceBlendOutTime | `float` |  |
| SequenceBlendBySyncGroup | `bool` |  |
| SequenceBlendResetNewTimeAccumulator | `bool` |  |
| SequenceBlendOutWeightScale | `float` |  |
| bClearBlendOutPoseWhenSequenceReactive | `bool` |  |
| SequenceBlendOutWhenRelevant | `bool` |  |
| SequenceBlendOutTime_Counter | `float` |  |
| SequenceBlendOutTime_Alpha | `float` |  |
| SequenceBlendOutWeight | `float` |  |
| LastSequence | `UAnimSequenceBase *` |  |
| BlendOutPlayers_Cache | `TArray < UAnimSequenceBase * >` |  |

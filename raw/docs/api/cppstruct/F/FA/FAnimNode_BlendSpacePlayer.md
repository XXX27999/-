# FAnimNode_BlendSpacePlayer

## Fields

| Name | Type | Description |
| --- | --- | --- |
| X | `float` |  |
| Y | `float` |  |
| Z | `float` |  |
| PlayRate | `float` |  |
| bLoop | `bool` |  |
| StartPosition | `float` |  |
| BlendSpace | `UBlendSpaceBase *` |  |
| bResetPlayTimeWhenBlendSpaceChanges | `bool` |  |
| bResetPlayTimeWhenBlendSpaceReactive | `bool` |  |
| bResetSampleCacheWhenBlendSpaceChanges | `bool` |  |
| BlendFilter | `FBlendFilter` |  |
| BlendSampleDataCache | `TArray < FBlendSampleData >` |  |
| PreviousBlendSpace | `UBlendSpaceBase *` |  |
| EnableBSBlend | `bool` |  |
| BSBlendOutTime | `float` |  |
| BSBlendOutBlendOption | [EAlphaBlendOption](../../../cppenum/E/EA/EAlphaBlendOption.md) |  |
| BSBlendMode | [EBSBlendMode](../../../cppenum/E/EB/EBSBlendMode.md) |  |
| BSBlendBySyncGroup | `bool` |  |
| BSBlendResetNewTimeAccumulator | `bool` |  |
| BSBlendOutWeightScale | `float` |  |
| bClearBlendOutPoseWhenBlendSpaceReactive | `bool` |  |
| BSBlendOutTime_Counter | `float` |  |
| BSBlendOutTime_Alpha | `float` |  |
| BSBlendOutWeight | `float` |  |
| LastBlendSpace | `UBlendSpaceBase *` |  |
| BlendOutPlayers_Cache | `TArray < UBlendSpaceBase * >` |  |

# FAnimNode_SubInstance

## Fields

| Name | Type | Description |
| --- | --- | --- |
| InPose | `FPoseLink` | Input pose for the node, intentionally not accessible because if there's no input<br>	   Node in the target class we don't want to show this as a pin |
| InPoses | `TArray < FPoseLink >` | Each layer's blended pose |
| SubInstanceSlotName | `FName` |  |
| InstanceClass | `TSubclassOf < UAnimInstance >` |  |
| bNeedCacheSubInstance | `bool` |  |
| MaxCacheSubInstanceCount | `int32` |  |
| bResetToAdditivePose | `bool` |  |
| InstanceToRun | `UAnimInstance *` | This is the actual instance allocated at runtime that will run |
| InstancePendingToRun | `UAnimInstance *` |  |
| bPendingCreateSubInstance | `bool` | Flag set during Restore_AnyThread when a sub-instance needs to be created on game thread |
| PendingSubInstanceClassPath | `FString` | The class path for the pending sub-instance to create |
| MultiInstancesToRunDatas | `TArray < FMultiSubInstanceData >` |  |
| BlendOutInstanceDatas | `TArray < FSubInstanceBlendData >` |  |
| InstanceProperties | `TArray < UProperty * >` | List of properties on the calling instance to push from |
| SubInstanceProperties | `TArray < UProperty * >` | List of properties on the sub instance to push to, built from name list when initialised |
| SourcePropertyNames | `TArray < FName >` | List of source properties to use, 1-1 with Dest names below, built by the compiler |
| DestPropertyNames | `TArray < FName >` | List of destination properties to use, 1-1 with Source names above, built by the compiler |
| PosInertialization | `FAnimNode_SubAnimInertialization` |  |
| bBlendSubAnim | `bool` |  |
| NewAnimBlendTime | `float` |  |
| bKeepUpdateOldSubInstanes | `bool` |  |
| bUpdateWhenNotRelevant | `bool` |  |
| NotRelevantUpdateConditions | `TArray < UAnimInstanceUpdateCondition * >` |  |
| UpdateConditions | `TArray < UAnimInstanceUpdateCondition * >` |  |
| bAlwaysUpdateInputNode | `bool` |  |
| bResetInertializationWhenReactive | `bool` |  |
| bUpdateAllInputNodeWhenNoInstanceRun | `bool` |  |
| bResetPendingBlendDurationWhenReactive | `bool` |  |

# FAnimNode_CopyPoseFromRemapping

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SourceMeshComponent | `TWeakObjectPtr < USkeletalMeshComponent >` | This is used by default if it's valid |
| bUseAttachedParent | `bool` | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |
| bIkGunValid | `bool` |  |
| bParentPoseOffset | `bool` |  |
| NewFPPPoseOffset | [FNewFPPPoseOffset](../FN/FNewFPPPoseOffset.md) |  |
| BoneNeedRelevant | `TMap < FName , FName >` |  |

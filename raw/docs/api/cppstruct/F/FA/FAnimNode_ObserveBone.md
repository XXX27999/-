# FAnimNode_ObserveBone

Debugging node that displays the current value of a bone in a specific space.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BoneToObserve | `FBoneReference` | Name of bone to observe. |
| DisplaySpace | `TEnumAsByte < EBoneControlSpace >` | Reference frame to display the bone transform in. |
| bRelativeToRefPose | `bool` | Show the difference from the reference pose? |
| Translation | [FVector](../FV/FVector.md) | Translation of the bone being observed. |
| Rotation | [FRotator](../FR/FRotator.md) | Rotation of the bone being observed. |
| Scale | [FVector](../FV/FVector.md) | Scale of the bone being observed. |

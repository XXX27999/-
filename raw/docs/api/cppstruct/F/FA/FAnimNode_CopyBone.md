# FAnimNode_CopyBone

Simple controller to copy a bone's transform to another one.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SourceBone | `FBoneReference` | Source Bone Name to get transform from |
| TargetBone | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| bCopyTranslation | `bool` | If Translation should be copied |
| bCopyRotation | `bool` | If Rotation should be copied |
| bCopyScale | `bool` | If Scale should be copied |
| ControlSpace | `TEnumAsByte < EBoneControlSpace >` | Space to convert transforms into prior to copying components |

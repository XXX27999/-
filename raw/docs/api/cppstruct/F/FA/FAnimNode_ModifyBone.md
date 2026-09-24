# FAnimNode_ModifyBone

Simple controller that replaces or adds to the translationrotation of a single bone.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BoneToModify | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| Translation | [FVector](../FV/FVector.md) | New translation of bone to apply. |
| Rotation | [FRotator](../FR/FRotator.md) | New rotation of bone to apply. |
| Scale | [FVector](../FV/FVector.md) | New Scale of bone to apply. This is only worldspace. |
| TranslationMode | `TEnumAsByte < EBoneModificationMode >` | Whether and how to modify the translation of this bone. |
| RotationMode | `TEnumAsByte < EBoneModificationMode >` | Whether and how to modify the translation of this bone. |
| ScaleMode | `TEnumAsByte < EBoneModificationMode >` | Whether and how to modify the translation of this bone. |
| TranslationSpace | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame to apply Translation in. |
| RotationSpace | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame to apply Rotation in. |
| ScaleSpace | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame to apply Scale in. |
| TranslationCoefficient | [FVector](../FV/FVector.md) |  |

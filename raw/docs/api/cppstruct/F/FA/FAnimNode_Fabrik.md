# FAnimNode_Fabrik

## Fields

| Name | Type | Description |
| --- | --- | --- |
| EffectorTransform | [FTransform](../FT/FTransform.md) | Coordinates for target location of tip bone - if EffectorLocationSpace is bone, this is the offset from Target Bone to use as target location |
| EffectorTransformSpace | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Effector Transform. |
| EffectorTransformBone_DEPRECATED | `FBoneReference` | If EffectorTransformSpace is a bone, this is the bone to use. |
| EffectorTarget | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) | If EffectorTransformSpace is a bone, this is the bone to use. |
| EffectorRotationSource | `TEnumAsByte < enum EBoneRotationSource >` |  |
| TipBone | `FBoneReference` | Name of tip bone |
| RootBone | `FBoneReference` | Name of the root bone |
| Precision | `float` | Tolerance for final tip location delta from EffectorLocation |
| MaxIterations | `int32` | Maximum number of iterations allowed, to control performance. |
| bEnableDebugDraw | `bool` | Toggle drawing of axes to debug joint rotation |

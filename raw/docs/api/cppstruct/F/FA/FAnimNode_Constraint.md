# FAnimNode_Constraint

Constraint node to parent or world transform for rotationtranslation

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BoneToModify | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| ConstraintSetup | `TArray < FConstraint >` | List of constraints |
| ConstraintWeights | `TArray < float >` | Weight data - post edit syncs up to ConstraintSetups |

# FConstraint

Constraint Set up

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TargetBone | `FBoneReference` | Target Bone this is constraint to |
| OffsetOption | [EConstraintOffsetOption](../../../cppenum/E/EC/EConstraintOffsetOption.md) | Maintain offset based on refpose or not.<br><br>	  None - no offset<br>	  Offset_RefPose - offset is created based on reference pose<br><br>	  In the future, we'd like to support custom offset, not just based on ref pose |
| TransformType | [ETransformConstraintType](../../../cppenum/E/ET/ETransformConstraintType.md) | What transform type is constraint to - Translation, Rotation, Scale OR Parent. Parent overrides all component |
| PerAxis | `FFilterOptionPerAxis` | Per axis filter options - applied in their local space not in world space |

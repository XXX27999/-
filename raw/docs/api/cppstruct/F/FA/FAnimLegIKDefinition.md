# FAnimLegIKDefinition

Per foot definitions

## Fields

| Name | Type | Description |
| --- | --- | --- |
| IKFootBone | `FBoneReference` |  |
| FKFootBone | `FBoneReference` |  |
| NumBonesInLimb | `int32` |  |
| FootBoneForwardAxis | `TEnumAsByte < EAxis :: Type >` | Forward Axis for Foot bone. |
| bEnableRotationLimit | `bool` | If enabled, we prevent the leg from bending backwards and enforce a min compression angle |
| MinRotationAngle | `float` | Only used if bEnableRotationLimit is enabled. Prevents the leg from folding onto itself,<br>	 and forces at least this angle between Parent and Child bone. |
| bEnableKneeTwistCorrection | `bool` | Enable Knee Twist correction, by comparing Foot FK with Foot IK orientation. |

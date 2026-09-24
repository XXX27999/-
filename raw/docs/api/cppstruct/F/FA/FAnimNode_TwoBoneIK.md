# FAnimNode_TwoBoneIK

Simple 2 Bone IK Controller.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| IKBone | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| bAllowStretching | `uint32` | Should stretching be allowed, to be prevent over extension |
| StartStretchRatio | `float` | Limits to use if stretching is allowed. This value determines when to start stretch. For example, 0.9 means once it reaches 90% of the whole length of the limb, it will start apply. |
| MaxStretchScale | `float` | Limits to use if stretching is allowed. This value determins what is the max stretch scale. For example, 1.5 means it will stretch until 150 % of the whole length of the limb. |
| StretchLimits_DEPRECATED | [FVector2D](../FV/FVector2D.md) | Limits to use if stretching is allowed - old property DEPRECATED |
| bTakeRotationFromEffectorSpace | `uint32` | Set end bone to use End Effector rotation |
| bMaintainEffectorRelRot | `uint32` | Keep local rotation of end bone |
| EffectorLocationSpace | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Effector Location. |
| EffectorSpaceBoneName_DEPRECATED | `FName` | If EffectorLocationSpace is a bone, this is the bone to use. |
| EffectorLocation | [FVector](../FV/FVector.md) | Effector Location. Target Location to reach. |
| EffectorTarget | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) |  |
| JointTargetLocationSpace | `TEnumAsByte < enum EBoneControlSpace >` | Reference frame of Joint Target Location. |
| JointTargetLocation | [FVector](../FV/FVector.md) | Joint Target Location. Location used to orient Joint bone. |
| JointTargetSpaceBoneName_DEPRECATED | `FName` | If JointTargetSpaceBoneName is a bone, this is the bone to use. |
| JointTarget | [FBoneSocketTarget](../FB/FBoneSocketTarget.md) |  |
| bAllowTwist | `bool` | Whether or not to apply twist on the chain of joints. This clears the twist value along the TwistAxis |
| TwistAxis | `FAxis` | Specify which axis it's aligned. Used when removing twist |
| bNoTwist_DEPRECATED | `bool` | Whether or not to apply twist on the chain of joints. This clears the twist value along the TwistAxis |

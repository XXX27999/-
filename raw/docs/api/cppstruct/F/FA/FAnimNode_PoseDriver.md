# FAnimNode_PoseDriver

RBF based orientation driver

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SourcePose | `FPoseLink` | Bones to use for driving parameters based on their transform |
| SourceBones | `TArray < FBoneReference >` | Bone to use for driving parameters based on its orientation |
| bOnlyDriveSelectedBones | `bool` | If we should filter bones to be driven using the DrivenBonesFilter array |
| OnlyDriveBones | `TArray < FBoneReference >` | If bFilterDrivenBones is specified, only these bones will be modified by this node |
| EvalSpaceBone | `FBoneReference` | Optional other bone space to use when reading SourceBone transform.<br>	 	If not specified, we just use local space of SourceBone (ie relative to parent bone) |
| RBFParams | [FRBFParams](../FR/FRBFParams.md) | Parameters used by RBF solver |
| DriveSource | [EPoseDriverSource](../../../cppenum/E/EP/EPoseDriverSource.md) | Which part of the transform is read |
| DriveOutput | [EPoseDriverOutput](../../../cppenum/E/EP/EPoseDriverOutput.md) | Whether we should drive poses or curves |
| PoseTargets | `TArray < FPoseDriverTarget >` | Targets used to compare with current pose and drive morphsposes |
| SourceBone_DEPRECATED | `FBoneReference` |  |
| TwistAxis_DEPRECATED | `TEnumAsByte < EBoneAxis >` |  |
| Type_DEPRECATED | [EPoseDriverType](../../../cppenum/E/EP/EPoseDriverType.md) |  |
| RadialScaling_DEPRECATED | `float` |  |

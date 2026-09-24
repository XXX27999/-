# FPoseDriverTarget

Information about each target in the PoseDriver

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BoneTransforms | `TArray < FPoseDriverTransform >` | Translation of this target |
| TargetRotation | [FRotator](../FR/FRotator.md) | Rotation of this target |
| TargetScale | `float` | Scale applied to this target's function - a larger value will activate this target sooner |
| bApplyCustomCurve | `bool` | If we should apply a custom curve mapping to how this target activates |
| CustomCurve | [FRichCurve](../FR/FRichCurve.md) | Custom curve mapping to apply if bApplyCustomCurve is true |
| DrivenName | `FName` | Name of item to drive - depends on DriveOutput setting.<br>	 	If DriveOutput is DrivePoses, this should be the name of a pose in the assigned PoseAsset<br>	 	If DriveOutput is DriveCurves, this is the name of the curve (morph target, material param etc) to drive |

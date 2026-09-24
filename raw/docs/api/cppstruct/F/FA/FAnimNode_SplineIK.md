# FAnimNode_SplineIK

## Fields

| Name | Type | Description |
| --- | --- | --- |
| StartBone | `FBoneReference` | Name of root bone from which the spline extends |
| EndBone | `FBoneReference` | Name of bone at the end of the spline chain. Bones after this will not be altered by the controller. |
| BoneAxis | [ESplineBoneAxis](../../../cppenum/E/ES/ESplineBoneAxis.md) | Axis of the controlled bone (ie the direction of the spline) to use as the direction for the curve. |
| bAutoCalculateSpline | `bool` | The number of points in the spline if we are specifying it directly |
| PointCount | `int32` | The number of points in the spline if we are not auto-calculating |
| ControlPoints | `TArray < FTransform >` | Transforms applied to spline points |
| Roll | `float` | Overall roll of the spline, applied on top of other rotations along the direction of the spline |
| TwistStart | `float` | The twist of the start bone. Twist is interpolated along the spline according to Twist Blend. |
| TwistEnd | `float` | The twist of the end bone. Twist is interpolated along the spline according to Twist Blend. |
| TwistBlend | `FAlphaBlend` | How to interpolate twist along the length of the spline |
| Stretch | `float` | The maximum stretch allowed when fitting bones to the spline. 0.0 means bones do not stretch their length,<br>	  1.0 means bones stretch to the length of the spline |
| Offset | `float` | The distance along the spline from the start from which bones are constrained |
| BoneSpline | [FSplineCurves](../FS/FSplineCurves.md) | Spline we maintain internally |
| OriginalSplineLength | `float` | Cached spline length from when the spline was originally applied to the skeleton |
| CachedBoneReferences | `TArray < FSplineIKCachedBoneData >` | Cached data for bones in the IK chain, from start to end |
| CachedBoneLengths | `TArray < float >` | Cached bone lengths. Same size as CachedBoneReferences |
| CachedOffsetRotations | `TArray < FQuat >` | Cached bone offset rotations. Same size as CachedBoneReferences |

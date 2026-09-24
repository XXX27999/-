# FAnimPhysConstraintSetup

Constraint setup struct, holds data required to build a physics constraint

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LinearXLimitType | [AnimPhysLinearConstraintType](../../../cppenum/A/AN/AnimPhysLinearConstraintType.md) | Whether to limit the linear X axis |
| LinearYLimitType | [AnimPhysLinearConstraintType](../../../cppenum/A/AN/AnimPhysLinearConstraintType.md) | Whether to limit the linear Y axis |
| LinearZLimitType | [AnimPhysLinearConstraintType](../../../cppenum/A/AN/AnimPhysLinearConstraintType.md) | Whether to limit the linear Z axis |
| LinearAxesMin | [FVector](../FV/FVector.md) | Minimum linear movement per-axis (Set zero here and in the max limit to lock) |
| LinearAxesMax | [FVector](../FV/FVector.md) | Maximum linear movement per-axis (Set zero here and in the min limit to lock) |
| AngularConstraintType | [AnimPhysAngularConstraintType](../../../cppenum/A/AN/AnimPhysAngularConstraintType.md) | Method to use when constraining angular motion |
| TwistAxis | [AnimPhysTwistAxis](../../../cppenum/A/AN/AnimPhysTwistAxis.md) | Axis to consider for twist when constraining angular motion (forward axis) |
| ConeAngle | `float` | Angle to use when constraining using a cone |
| AngularXAngle_DEPRECATED | `float` | X-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| AngularYAngle_DEPRECATED | `float` | Y-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| AngularZAngle_DEPRECATED | `float` | Z-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| AngularLimitsMin | [FVector](../FV/FVector.md) |  |
| AngularLimitsMax | [FVector](../FV/FVector.md) |  |
| AngularTargetAxis | [AnimPhysTwistAxis](../../../cppenum/A/AN/AnimPhysTwistAxis.md) | Axis on body1 to match to the angular target direction. |
| AngularTarget | [FVector](../FV/FVector.md) | Target direction to face for body1 (in body0 local space) |
| bLinearFullyLocked | `bool` | The values below are calculated on initialisation and used when building the limits<br>	 If all axes are locked we can use 3 linear limits instead of the 6 needed for limited axes |

# FAnimPhysConstraintSetup_UE5

Constraint setup struct, holds data required to build a physics constraint

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LinearXLimitType | [AnimPhysLinearConstraintType_UE5](../../../cppenum/A/AN/AnimPhysLinearConstraintType_UE5.md) | Whether to limit the linear X axis |
| LinearYLimitType | [AnimPhysLinearConstraintType_UE5](../../../cppenum/A/AN/AnimPhysLinearConstraintType_UE5.md) | Whether to limit the linear Y axis |
| LinearZLimitType | [AnimPhysLinearConstraintType_UE5](../../../cppenum/A/AN/AnimPhysLinearConstraintType_UE5.md) | Whether to limit the linear Z axis |
| LinearAxesMin | [FVector](../FV/FVector.md) | Minimum linear movement per-axis (Set zero here and in the max limit to lock) |
| LinearAxesMax | [FVector](../FV/FVector.md) | Maximum linear movement per-axis (Set zero here and in the min limit to lock) |
| AngularConstraintType | [AnimPhysAngularConstraintType_UE5](../../../cppenum/A/AN/AnimPhysAngularConstraintType_UE5.md) | Method to use when constraining angular motion |
| TwistAxis | [AnimPhysTwistAxis](../../../cppenum/A/AN/AnimPhysTwistAxis.md) | Axis to consider for twist when constraining angular motion (forward axis) |
| AngularTargetAxis | [AnimPhysTwistAxis](../../../cppenum/A/AN/AnimPhysTwistAxis.md) | The axis in the simulation pose to align to the Angular Target.<br>	  This is typically the axis pointing along the bone.<br>	  Note: This is affected by the Angular Spring Constant. |
| ConeAngle | `float` | Angle to use when constraining using a cone |
| AngularLimitsMin | [FVector](../FV/FVector.md) |  |
| AngularLimitsMax | [FVector](../FV/FVector.md) |  |
| AngularTarget | [FVector](../FV/FVector.md) | The axis to align the angular spring constraint to in the animation pose.<br>	  This typically points down the bone - so values of (1.0, 0.0, 0.0) are common,<br>	  but you can pick other values to align the spring to a different direction.<br>	  Note: This is affected by the Angular Spring Constant. |
| AngularXAngle_DEPRECATED | `float` | X-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| AngularYAngle_DEPRECATED | `float` | Y-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| AngularZAngle_DEPRECATED | `float` | Z-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |

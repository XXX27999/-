# UPhysicsConstraintTemplate

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DefaultInstance | [FConstraintInstance](../../cppstruct/F/FC/FConstraintInstance.md) |  |
| ProfileHandles | `TArray < FPhysicsConstraintProfileHandle >` | Handles to the constraint profiles applicable to this constraint |
| DefaultProfile | [FConstraintProfileProperties](../../cppstruct/F/FC/FConstraintProfileProperties.md) | When no profile is selected, use these settings. Only needed in editor as we serialize it into DefaultInstance on save |
| JointName_DEPRECATED | `FName` |  |
| ConstraintBone1_DEPRECATED | `FName` |  |
| ConstraintBone2_DEPRECATED | `FName` |  |
| Pos1_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| PriAxis1_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| SecAxis1_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| Pos2_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| PriAxis2_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| SecAxis2_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| bEnableProjection_DEPRECATED | `uint32` |  |
| ProjectionLinearTolerance_DEPRECATED | `float` |  |
| ProjectionAngularTolerance_DEPRECATED | `float` |  |
| LinearXMotion_DEPRECATED | `TEnumAsByte < enum ELinearConstraintMotion >` |  |
| LinearYMotion_DEPRECATED | `TEnumAsByte < enum ELinearConstraintMotion >` |  |
| LinearZMotion_DEPRECATED | `TEnumAsByte < enum ELinearConstraintMotion >` |  |
| LinearLimitSize_DEPRECATED | `float` |  |
| bLinearLimitSoft_DEPRECATED | `uint32` |  |
| LinearLimitStiffness_DEPRECATED | `float` |  |
| LinearLimitDamping_DEPRECATED | `float` |  |
| bLinearBreakable_DEPRECATED | `uint32` |  |
| LinearBreakThreshold_DEPRECATED | `float` |  |
| AngularSwing1Motion_DEPRECATED | `TEnumAsByte < enum EAngularConstraintMotion >` |  |
| AngularSwing2Motion_DEPRECATED | `TEnumAsByte < enum EAngularConstraintMotion >` |  |
| AngularTwistMotion_DEPRECATED | `TEnumAsByte < enum EAngularConstraintMotion >` |  |
| bSwingLimitSoft_DEPRECATED | `uint32` |  |
| bTwistLimitSoft_DEPRECATED | `uint32` |  |
| Swing1LimitAngle_DEPRECATED | `float` |  |
| Swing2LimitAngle_DEPRECATED | `float` |  |
| TwistLimitAngle_DEPRECATED | `float` |  |
| SwingLimitStiffness_DEPRECATED | `float` |  |
| SwingLimitDamping_DEPRECATED | `float` |  |
| TwistLimitStiffness_DEPRECATED | `float` |  |
| TwistLimitDamping_DEPRECATED | `float` |  |
| bAngularBreakable_DEPRECATED | `uint32` |  |
| AngularBreakThreshold_DEPRECATED | `float` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

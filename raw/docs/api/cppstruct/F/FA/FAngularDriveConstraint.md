# FAngularDriveConstraint

Angular Drive

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TwistDrive | [FConstraintDrive](../FC/FConstraintDrive.md) | Controls the twist (roll) constraint drive between current orientationvelocity and target orientationvelocity. This is available as long as the twist limit is set to free or limited. |
| SwingDrive | [FConstraintDrive](../FC/FConstraintDrive.md) | Controls the cone constraint drive between current orientationvelocity and target orientationvelocity. This is available as long as there is at least one swing limit set to free or limited. |
| SlerpDrive | [FConstraintDrive](../FC/FConstraintDrive.md) | Controls the SLERP (spherical lerp) drive between current orientationvelocity and target orientationvelocity. NOTE: This is only available when all three angular limits are either free or limited. Locking any angular limit will turn off the drive implicitly. |
| OrientationTarget | [FRotator](../FR/FRotator.md) | Target orientation relative to the the body reference frame. |
| AngularVelocityTarget | [FVector](../FV/FVector.md) | Target angular velocity relative to the body reference frame. |
| AngularDriveMode | `TEnumAsByte < enum EAngularDriveMode :: Type >` | Whether motors use SLERP (spherical lerp) or decompose into a Swing motor (cone constraints) and Twist motor (roll constraints). NOTE: SLERP will NOT work if any of the angular constraints are locked. |

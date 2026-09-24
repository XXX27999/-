# FConstraintProfileProperties

Container for properties of a physics constraint that can be easily swapped at runtime. This is useful for switching different setups when going from ragdoll to standup for example

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ProjectionLinearTolerance | `float` | Linear tolerance value in world units. If the distance error exceeds this tolerence limit, the body will be projected. |
| ProjectionAngularTolerance | `float` | Angular tolerance value in world units. If the distance error exceeds this tolerence limit, the body will be projected. |
| LinearBreakThreshold | `float` | Force needed to break the distance constraint. |
| AngularBreakThreshold | `float` | Torque needed to break the joint. |
| LinearLimit | [FLinearConstraint](../FL/FLinearConstraint.md) |  |
| ConeLimit | [FConeConstraint](./FConeConstraint.md) |  |
| TwistLimit | [FTwistConstraint](../FT/FTwistConstraint.md) |  |
| LinearDrive | [FLinearDriveConstraint](../FL/FLinearDriveConstraint.md) |  |
| AngularDrive | [FAngularDriveConstraint](../FA/FAngularDriveConstraint.md) |  |
| bDisableCollision | `uint8` |  |
| bParentDominates | `uint8` |  |
| bEnableProjection | `uint8` | If distance error between bodies exceeds 0.1 units, or rotation error exceeds 10 degrees, body will be projected to fix this.<br>	 For example a chain spinning too fast will have its elements appear detached due to velocity, this will project all bodies so they still appear attached to each other. |
| bAngularBreakable | `uint8` | Whether it is possible to break the joint with angular force. |
| bLinearBreakable | `uint8` | Whether it is possible to break the joint with linear force. |

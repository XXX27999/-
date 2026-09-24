# UPhysicsConstraintComponent

This is effectively a joint that allows you to connect 2 rigid bodies together. You can create different types of joints using the various parameters of this component.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ConstraintActor1 | `AActor *` | Pointer to first Actor to constrain. |
| ComponentName1 | [FConstrainComponentPropName](../../cppstruct/F/FC/FConstrainComponentPropName.md) | Name of first component property to constrain. If Actor1 is NULL, will look within Owner.<br>	 	If this is NULL, will use RootComponent of Actor1 |
| ConstraintActor2 | `AActor *` | Pointer to second Actor to constrain. |
| ComponentName2 | [FConstrainComponentPropName](../../cppstruct/F/FC/FConstrainComponentPropName.md) | Name of second component property to constrain. If Actor2 is NULL, will look within Owner.<br>	 	If this is NULL, will use RootComponent of Actor2 |
| ConstraintSetup_DEPRECATED | `UPhysicsConstraintTemplate *` |  |
| OnConstraintBroken | `FConstraintBrokenSignature` | Notification when constraint is broken. |
| ConstraintInstance | [FConstraintInstance](../../cppstruct/F/FC/FConstraintInstance.md) | All constraint settings |

## Functions

### SetConstrainedComponents

Directly specify component to connect. Will update frames based on current position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component1 | `UPrimitiveComponent *` |  |
| BoneName1 | `FName` |  |
| Component2 | `UPrimitiveComponent *` |  |
| BoneName2 | `FName` |  |

**Return**

- Type: 
- Description: _None_

### BreakConstraint

Break this constraint

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLinearPositionDrive

EnablesDisables linear position drive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableDriveX | `bool` | Indicates whether the drive for the X-Axis should be enabled |
| bEnableDriveY | `bool` | Indicates whether the drive for the Y-Axis should be enabled |
| bEnableDriveZ | `bool` | Indicates whether the drive for the Z-Axis should be enabled |

**Return**

- Type: 
- Description: _None_

### SetLinearVelocityDrive

EnablesDisables linear position drive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableDriveX | `bool` | Indicates whether the drive for the X-Axis should be enabled |
| bEnableDriveY | `bool` | Indicates whether the drive for the Y-Axis should be enabled |
| bEnableDriveZ | `bool` | Indicates whether the drive for the Z-Axis should be enabled |

**Return**

- Type: 
- Description: _None_

### SetAngularOrientationDrive

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableSwingDrive | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| bEnableTwistDrive | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Return**

- Type: 
- Description: _None_

### SetOrientationDriveTwistAndSwing

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableTwistDrive | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| bEnableSwingDrive | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Return**

- Type: 
- Description: _None_

### SetOrientationDriveSLERP

EnablesDisables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableSLERP | `bool` | Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |

**Return**

- Type: 
- Description: _None_

### SetAngularVelocityDrive

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableSwingDrive | `bool` |  |
| bEnableTwistDrive | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAngularVelocityDriveTwistAndSwing

EnablesDisables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableTwistDrive | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| bEnableSwingDrive | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Return**

- Type: 
- Description: _None_

### SetAngularVelocityDriveSLERP

EnablesDisables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableSLERP | `bool` | Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |

**Return**

- Type: 
- Description: _None_

### SetAngularDriveMode

Switches the angular drive mode between SLERP and Twist And Swing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DriveMode | `EAngularDriveMode :: Type` | The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock |

**Return**

- Type: 
- Description: _None_

### SetLinearPositionTarget

Sets the target position for the linear drive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPosTarget | `FVector &` | Target position |

**Return**

- Type: 
- Description: _None_

### SetLinearVelocityTarget

Sets the target velocity for the linear drive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVelTarget | `FVector &` | Target velocity |

**Return**

- Type: 
- Description: _None_

### SetLinearDriveParams

Sets the drive params for the linear drive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PositionStrength | `float` | Positional strength for the drive (stiffness) |
| VelocityStrength | `float` | Velocity strength of the drive (damping) |
| InForceLimit | `float` | Max force applied by the drive |

**Return**

- Type: 
- Description: _None_

### SetAngularOrientationTarget

Sets the target orientation for the angular drive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPosTarget | `FRotator &` | Target orientation |

**Return**

- Type: 
- Description: _None_

### SetAngularVelocityTarget

Sets the target velocity for the angular drive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVelTarget | `FVector &` | Target velocity |

**Return**

- Type: 
- Description: _None_

### SetAngularDriveParams

Sets the drive params for the angular drive.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PositionStrength | `float` | Positional strength for the drive (stiffness) |
| VelocityStrength | `float` | Velocity strength of the drive (damping) |
| InForceLimit | `float` | Max force applied by the drive |

**Return**

- Type: 
- Description: _None_

### SetLinearXLimit

Sets the LinearX Motion Type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConstraintType | `ELinearConstraintMotion` | New Constraint Type |
| LimitSize | `float` | Size of limit |

**Return**

- Type: 
- Description: _None_

### SetLinearYLimit

Sets the LinearY Motion Type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConstraintType | `ELinearConstraintMotion` | New Constraint Type |
| LimitSize | `float` | Size of limit |

**Return**

- Type: 
- Description: _None_

### SetLinearZLimit

Sets the LinearZ Motion Type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConstraintType | `ELinearConstraintMotion` | New Constraint Type |
| LimitSize | `float` | Size of limit |

**Return**

- Type: 
- Description: _None_

### SetAngularSwing1Limit

Sets the Angular Swing1 Motion Type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MotionType | `EAngularConstraintMotion` |  |
| Swing1LimitAngle | `float` | Size of limit in degrees |

**Return**

- Type: 
- Description: _None_

### SetAngularSwing2Limit

Sets the Angular Swing2 Motion Type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MotionType | `EAngularConstraintMotion` |  |
| Swing2LimitAngle | `float` | Size of limit in degrees |

**Return**

- Type: 
- Description: _None_

### SetAngularTwistLimit

Sets the Angular Twist Motion Type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConstraintType | `EAngularConstraintMotion` | New Constraint Type |
| TwistLimitAngle | `float` | Size of limit in degrees |

**Return**

- Type: 
- Description: _None_

### SetLinearBreakable

Sets the Linear Breakable properties

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bLinearBreakable | `bool` | Whether it is possible to break the joint with linear force |
| LinearBreakThreshold | `float` | Force needed to break the joint |

**Return**

- Type: 
- Description: _None_

### SetAngularBreakable

Sets the Angular Breakable properties

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bAngularBreakable | `bool` | Whether it is possible to break the joint with angular force |
| AngularBreakThreshold | `float` | Torque needed to break the joint |

**Return**

- Type: 
- Description: _None_

### GetCurrentTwist

Gets the current Angular Twist of the constraint

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentSwing1

Gets the current Swing1 of the constraint

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentSwing2

Gets the current Swing2 of the constraint

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetConstraintReferenceFrame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Frame | `EConstraintFrame :: Type` |  |
| RefFrame | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### SetConstraintReferencePosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Frame | `EConstraintFrame :: Type` |  |
| RefPosition | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetConstraintReferenceOrientation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Frame | `EConstraintFrame :: Type` |  |
| PriAxis | `FVector &` |  |
| SecAxis | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetDisableCollision

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDisableCollision | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetConstraintForce

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutLinearForce | `FVector &` |  |
| OutAngularForce | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### IsBroken

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

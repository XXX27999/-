# UMovementComponent

MovementComponent is an abstract component class that defines functionality for moving a PrimitiveComponent (our UpdatedComponent) each tick.
  Base functionality includes:
     - Restricting movement to a plane or axis.
     - Utility functions for special handling of collision results (SlideAlongSurface(), ComputeSlideVector(), TwoWallAdjust()).
     - Utility functions for moving when there may be initial penetration (SafeMoveUpdatedComponent(), ResolvePenetration()).
     - Automatically registering the component tick and finding a component to move on the owning Actor.
  Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
  During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UpdatedComponent | `USceneComponent *` | The component we move and update.<br>	  If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.<br>	  @see bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive |
| UpdatedPrimitive | `UPrimitiveComponent *` | UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent. |
| Velocity | [FVector](../../cppstruct/F/FV/FVector.md) | Current velocity of updated component. |
| PlaneConstraintNormal | [FVector](../../cppstruct/F/FV/FVector.md) | The normal or axis of the plane that constrains movement, if bConstrainToPlane is enabled.<br>	  If for example you wanted to constrain movement to the X-Z plane (so that Y cannot change), the normal would be set to X=0 Y=1 Z=0.<br>	  This is recalculated whenever PlaneConstraintAxisSetting changes. It is normalized once the component is registered with the game world.<br>	  @see bConstrainToPlane, SetPlaneConstraintNormal(), SetPlaneConstraintFromVectors() |
| PlaneConstraintOrigin | [FVector](../../cppstruct/F/FV/FVector.md) | The origin of the plane that constrains movement, if plane constraint is enabled.<br>	  This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().<br>	  @see bConstrainToPlane, SetPlaneConstraintOrigin(). |
| bUpdateOnlyIfRendered | `uint8` | If true, skips TickComponent() if UpdatedComponent was not recently rendered. |
| bAutoUpdateTickRegistration | `uint8` | If true, whenever the updated component is changed, this component will enable or disable its tick dependent on whether it has something to update.<br>	  This will NOT enable tick at startup if bAutoActivate is false, because presumably you have a good reason for not wanting it to start ticking initially. |
| bTickBeforeOwner | `uint8` | If true, after registration we will add a tick dependency to tick before our owner (if we can both tick).<br>	  This is important when our tick causes an update in the owner's position, so that when the owner ticks it uses the most recent position without lag.<br>	  Disabling this can improve performance if both objects tick but the order of ticks doesn't matter. |
| bAutoRegisterUpdatedComponent | `uint8` | If true, registers the owner's Root component as the UpdatedComponent if there is not one currently assigned. |
| bConstrainToPlane | `uint8` | If true, movement will be constrained to a plane.<br>	  @see PlaneConstraintNormal, PlaneConstraintOrigin, PlaneConstraintAxisSetting |
| bSnapToPlaneAtStart | `uint8` | If true and plane constraints are enabled, then the updated component will be snapped to the plane when first attached. |
| bAutoRegisterPhysicsVolumeUpdates | `uint8` | If true, then applies the value of bComponentShouldUpdatePhysicsVolume to the UpdatedComponent. If false, will not change bShouldUpdatePhysicsVolume on the UpdatedComponent at all.<br>	  @see bComponentShouldUpdatePhysicsVolume |
| bComponentShouldUpdatePhysicsVolume | `uint8` | If true, enables bShouldUpdatePhysicsVolume on the UpdatedComponent during initialization from SetUpdatedComponent(), otherwise disables such updates.<br>	  Only enabled if bAutoRegisterPhysicsVolumeUpdates is true.<br>	  WARNING: UpdatePhysicsVolume is potentially expensive if overlap events are also disabled because it requires a separate query against all physics volumes in the world. |
| PlaneConstraintAxisSetting | [EPlaneConstraintAxisSetting](../../cppenum/E/EP/EPlaneConstraintAxisSetting.md) | Setting that controls behavior when movement is restricted to a 2D plane defined by a specific axisnormal,<br>	  so that movement along the locked axis is not be possible.<br>	  @see SetPlaneConstraintAxisSetting |

## Functions

### GetGravityZ

Returns gravity that affects this component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaxSpeed

Returns maximum speed of component in current movement mode.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetMaxSpeedModifier

Returns a scalar applied to the maximum velocity that the component can currently move.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetModifiedMaxSpeed

Returns the result of GetMaxSpeed()  GetMaxSpeedModifier().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsExceedingMaxSpeed

Returns true if the current velocity is exceeding the given max speed (usually the result of GetMaxSpeed()), within a small error tolerance.
	  Note that under normal circumstances updates cause by acceleration will not cause this to be true, however external forces or changes in the max speed limit
	  can cause the max speed to be violated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaxSpeed | `float` |  |

**Return**

- Type: 
- Description: _None_

### StopMovementImmediately

Stops movement immediately (zeroes velocity, usually zeros acceleration for components with acceleration).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPhysicsVolume

Returns the PhysicsVolume this MovementComponent is using, or the world's default physics volume if none.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PhysicsVolumeChanged

Delegate when PhysicsVolume of UpdatedComponent has been changed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewVolume | `APhysicsVolume *` |  |

**Return**

- Type: 
- Description: _None_

### SetUpdatedComponent

Assign the component we move and update.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewUpdatedComponent | `USceneComponent *` |  |

**Return**

- Type: 
- Description: _None_

### K2_MoveUpdatedComponent

Moves our UpdatedComponent by the given Delta, and sets rotation to NewRotation.
	  Respects the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delta | `FVector` |  |
| NewRotation | `FRotator` |  |
| OutHit | `FHitResult &` |  |
| bSweep | `bool` |  |
| bTeleport | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPlaneConstraintAxisSetting

Set the plane constraint axis setting.
	  Changing this setting will modify the current value of PlaneConstraintNormal.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAxisSetting | [EPlaneConstraintAxisSetting](../../cppenum/E/EP/EPlaneConstraintAxisSetting.md) | New plane constraint axis setting. |

**Return**

- Type: 
- Description: _None_

### GetPlaneConstraintAxisSetting

Get the plane constraint axis setting.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlaneConstraintNormal

Sets the normal of the plane that constrains movement, enforced if the plane constraint is enabled.
	  Changing the normal automatically sets PlaneConstraintAxisSetting to "Custom".

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlaneNormal | [FVector](../../cppstruct/F/FV/FVector.md) | The normal of the plane. If non-zero in length, it will be normalized. |

**Return**

- Type: 
- Description: _None_

### SetPlaneConstraintFromVectors

Uses the Forward and Up vectors to compute the plane that constrains movement, enforced if the plane constraint is enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Forward | `FVector` |  |
| Up | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetPlaneConstraintOrigin

Sets the origin of the plane that constrains movement, enforced if the plane constraint is enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlaneOrigin | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetPlaneConstraintEnabled

Sets whether or not the plane constraint is enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPlaneConstraintNormal

Returns the normal of the plane that constrains movement, enforced if the plane constraint is enabled.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaneConstraintOrigin

Get the plane constraint origin. This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConstrainDirectionToPlane

Constrain a direction vector to the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Direction | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### ConstrainLocationToPlane

Constrain a position vector to the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### ConstrainNormalToPlane

Constrain a normal vector (of unit length) to the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Normal | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SnapUpdatedComponentToPlane

Snap the updated component to the plane constraint, if enabled.

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

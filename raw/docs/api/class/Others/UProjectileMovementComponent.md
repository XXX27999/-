# UProjectileMovementComponent

ProjectileMovementComponent updates the position of another component during its tick.

  Behavior such as bouncing after impacts and homing toward a target are supported.

  Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
  If the updated component is simulating physics, only the initial launch parameters (when initial velocity is non-zero)
  will affect the projectile, and the physics sim will take over from there.

  @see UMovementComponent

## Parents

- [UMovementComponent](./UMovementComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InitialSpeed | `float` | Initial speed of projectile. If greater than zero, this will override the initial Velocity value and instead treat Velocity as a direction. |
| MaxSpeed | `float` | Limit on speed of projectile (0 means no limit). |
| bRotationFollowsVelocity | `uint8` | If true, this projectile will have its rotation updated each frame to match the direction of its velocity. |
| bRotationRemainsVertical | `uint8` | If true, this projectile will have its rotation updated each frame to maintain the rotations Yaw only. (bRotationFollowsVelocity is required to be true) |
| bShouldBounce | `uint8` | If true, simple bounces will be simulated. Set this to false to stop simulating on contact. |
| bInitialVelocityInLocalSpace | `uint8` | If true, the initial Velocity is interpreted as being in local space upon startup.<br>	  @see SetVelocityInLocalSpace() |
| bForceSubStepping | `uint8` | If true, forces sub-stepping to break up movement into discrete smaller steps to improve accuracy of the trajectory.<br>	  Objects that move in a straight line typically do not need to set this, as movement always uses continuous collision detection (sweeps) so collision is not missed.<br>	  Sub-stepping is automatically enabled when under the effects of gravity or when homing towards a target.<br>	  @see MaxSimulationTimeStep, MaxSimulationIterations |
| bSimulationEnabled | `uint8` | If true, does normal simulation ticking and update. If false, simulation is halted, but component will still tick (allowing interpolation to run). |
| bSweepCollision | `uint8` | If true, movement uses swept collision checks.<br>	  If false, collision effectively teleports to the destination. Note that when this is disabled, movement will never generate blocking collision hits (though overlaps will be updated). |
| bIsHomingProjectile | `uint8` | If true, we will accelerate toward our homing target. HomingTargetComponent must be set after the projectile is spawned.<br>	  @see HomingTargetComponent, HomingAccelerationMagnitude |
| bBounceAngleAffectsFriction | `uint8` | Controls the effects of friction on velocity parallel to the impact surface when bouncing.<br>	  If true, friction will be modified based on the angle of impact, making friction higher for perpendicular impacts and lower for glancing impacts.<br>	  If false, a bounce will retain a proportion of tangential velocity equal to (1.0 - Friction), acting as a "horizontal restitution". |
| bIsSliding | `uint8` | If true, projectile is sliding  rolling along a surface. |
| bInterpMovement | `uint8` | If true and there is an interpolated component set, location (and optionally rotation) interpolation is enabled which allows the interpolated object to smooth uneven updates<br>	  of the UpdatedComponent's location (usually to smooth network updates). This requires using SetInterpolatedComponent() to indicate the visual component that lags behind the collision,<br>	  and using MoveInterpolationTarget() when the new target locationrotation is received (usually on a net update).<br>	  @see SetInterpolatedComponent(), MoveInterpolationTarget() |
| bInterpRotation | `uint8` | If true and there is an interpolated component set, rotation interpolation is enabled which allows the interpolated object to smooth uneven updates<br>	  of the UpdatedComponent's rotation (usually to smooth network updates).<br>	  Rotation interpolation is only applied if bInterpMovement is also enabled.<br>	  @see SetInterpolatedComponent(), MoveInterpolationTarget() |
| PreviousHitTime | `float` | Saved HitResult Time (0 to 1) from previous simulation step. Equal to 1.0 when there was no impact. |
| PreviousHitNormal | [FVector](../../cppstruct/F/FV/FVector.md) | Saved HitResult Normal from previous simulation step that resulted in an impact. If PreviousHitTime is 1.0, then the hit was not in the last step. |
| ProjectileGravityScale | `float` | Custom gravity scale for this projectile. Set to 0 for no gravity. |
| Buoyancy | `float` | Buoyancy of UpdatedComponent in fluid. 0.0=sinks as fast as in air, 1.0=neutral buoyancy |
| Bounciness | `float` | Percentage of velocity maintained after the bounce in the direction of the normal of impact (coefficient of restitution).<br>	  1.0 = no velocity lost, 0.0 = no bounce. Ignored if bShouldBounce is false. |
| Friction | `float` | Coefficient of friction, affecting the resistance to sliding along a surface.<br>	  Normal range is [0,1] : 0.0 = no friction, 1.0+ = very high friction.<br>	  Also affects the percentage of velocity maintained after the bounce in the direction tangent to the normal of impact.<br>	  Ignored if bShouldBounce is false.<br>	  @see bBounceAngleAffectsFriction |
| BounceVelocityStopSimulatingThreshold | `float` | If velocity is below this threshold after a bounce, stops simulating and triggers the OnProjectileStop event.<br>	  Ignored if bShouldBounce is false, in which case the projectile stops simulating on the first impact.<br>	  @see StopSimulating(), OnProjectileStop |
| MinFrictionFraction | `float` | When bounce angle affects friction, apply at least this fraction of normal friction.<br>	  Helps consistently slow objects sliding or rolling along surfaces or in valleys when the usual friction amount would take a very long time to settle. |
| HomingAccelerationMagnitude | `float` | The magnitude of our acceleration towards the homing target. Overall velocity magnitude will still be limited by MaxSpeed. |
| HomingTargetComponent | `TWeakObjectPtr < USceneComponent >` | The current target we are homing towards. Can only be set at runtime (when projectile is spawned or updating).<br>	  @see bIsHomingProjectile |
| MaxSimulationTimeStep | `float` | Max time delta for each discrete simulation step.<br>	  Lowering this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br><br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationIterations, bForceSubStepping |
| MaxSimulationIterations | `int32` | Max number of iterations used for each discrete simulation step.<br>	  Increasing this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br><br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationTimeStep, bForceSubStepping |
| BounceAdditionalIterations | `int32` | On the first few bounces (up to this amount), allow extra iterations over MaxSimulationIterations if necessary. |
| InterpLocationTime | `float` | "Time" over which most of the location interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.<br>	  Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.<br>	  A value of zero is effectively instantaneous interpolation. |
| InterpRotationTime | `float` | "Time" over which most of the rotation interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.<br>	  Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.<br>	  A value of zero is effectively instantaneous interpolation. |
| InterpLocationMaxLagDistance | `float` | Max distance behind UpdatedComponent which the interpolated component is allowed to lag. |
| InterpLocationSnapToTargetDistance | `float` | Max distance behind UpdatedComponent beyond which the interpolated component is snapped to the target location instead.<br>	  For instance if the target teleports this far beyond the interpolated component, the interpolation is snapped to match the target. |

## Functions

### IsVelocityUnderSimulationThreshold

Returns true if velocity magnitude is less than BounceVelocityStopSimulatingThreshold.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetVelocityInLocalSpace

Sets the velocity to the new value, rotated into Actor space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewVelocity | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### StopSimulating

Clears the reference to UpdatedComponent, fires stop event (OnProjectileStop), and stops ticking (if bAutoUpdateTickRegistration is true).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### SetInterpolatedComponent

Assigns the component that will be used for network interpolationsmoothing. It is expected that this is a component attached somewhere below the UpdatedComponent.
	  When network updates use MoveInterpolationTarget() to move the UpdatedComponent, the interpolated component's relative offset will be maintained and smoothed over
	  the course of future component ticks. The current relative location and rotation of the component is saved as the target offset for future interpolation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `USceneComponent *` |  |

**Return**

- Type: 
- Description: _None_

### MoveInterpolationTarget

Moves the UpdatedComponent, which is also the interpolation target for the interpolated component. If there is not interpolated component, this simply moves UpdatedComponent.
	  Use this typically from PostNetReceiveLocationAndRotation() or similar from an Actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector &` |  |
| NewRotation | `FRotator &` |  |

**Return**

- Type: 
- Description: _None_

### ResetInterpolation

Resets interpolation so that interpolated component snaps back to the initial locationrotation without any additional offsets.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsInterpolationComplete

Returns whether interpolation is complete because the target has been reached. True when interpolation is disabled.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LimitVelocity

Don't allow velocity magnitude to exceed MaxSpeed, if MaxSpeed is non-zero.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewVelocity | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnProjectileBounce |  | Called when projectile impacts something and bounces are enabled. |
| OnProjectileStop |  | Called when projectile has come to a stop (velocity is below simulation threshold, bounces are disabled, or it is forcibly stopped). |

## Language

cpp

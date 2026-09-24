# UCharacterMovementComponent

CharacterMovementComponent handles movement logic for the associated Character owner.
  It supports various movement modes including: walking, falling, swimming, flying, custom.

  Movement is affected primarily by current Velocity and Acceleration. Acceleration is updated each frame
  based on the input vector accumulated thus far (see UPawnMovementComponent::GetPendingInputVector()).

  Networking is fully implemented, with server-client correction and prediction included.

  @see ACharacter, UPawnMovementComponent

## Parents

- [UPawnMovementComponent](./UPawnMovementComponent.md)
- IRVOAvoidanceInterface
- INetworkPredictionInterface
- IObjectPoolInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CharacterOwner | `ACharacter *` | Character movement component belongs to |
| bApplyGravityWhileJumping | `uint32` | Apply gravity while the character is actively jumping (e.g. holding the jump key).<br>	 	Helps remove frame-rate dependent jump height, but may alter base jump height. |
| GravityScale | `float` | Custom gravity scale. Gravity is multiplied by this amount for the character. |
| MaxStepHeight | `float` | Maximum height character can step up |
| JumpZVelocity | `float` | Initial velocity (instantaneous vertical acceleration) when jumping. |
| JumpOffJumpZFactor | `float` | Fraction of JumpZVelocity to use when automatically "jumping off" of a base actor that's not allowed to be a base for a character. (For example, if you're not allowed to stand on other players.) |
| WalkableFloorAngle | `float` | Max angle in degrees of a walkable surface. Any greater than this and it is too steep to be walkable. |
| WalkableFloorZ | `float` | Minimum Z value for floor normal. If less, not a walkable surface. Computed from WalkableFloorAngle. |
| MovementMode | `TEnumAsByte < enum EMovementMode >` | Actor's current movement mode (walking, falling, etc).<br>	     - walking:  Walking on a surface, under the effects of friction, and able to "step up" barriers. Vertical velocity is zero.<br>	     - falling:  Falling under the effects of gravity, after jumping or walking off the edge of a surface.<br>	     - flying:   Flying, ignoring the effects of gravity.<br>	     - swimming: Swimming through a fluid volume, under the effects of gravity and buoyancy.<br>	     - custom:   User-defined custom movement mode, including many possible sub-modes.<br>	  This is automatically replicated through the Character owner and for client-server movement functions.<br>	  @see SetMovementMode(), CustomMovementMode |
| CustomMovementMode | `uint8` | Current custom sub-mode if MovementMode is set to Custom.<br>	  This is automatically replicated through the Character owner and for client-server movement functions.<br>	  @see SetMovementMode() |
| OldBaseLocation | [FVector](../../cppstruct/F/FV/FVector.md) | Saved location of object we are standing on, for UpdateBasedMovement() to determine if base moved in the last frame, and therefore pawn needs an update. |
| OldBaseQuat | [FQuat](../../cppstruct/F/FQ/FQuat.md) | Saved location of object we are standing on, for UpdateBasedMovement() to determine if base moved in the last frame, and therefore pawn needs an update. |
| OldReplaySampleLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| OldReplaySampleTime | `float` |  |
| GroundFriction | `float` | Setting that affects movement control. Higher values allow faster changes in direction.<br>	  If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero), where it is multiplied by BrakingFrictionFactor.<br>	  When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.<br>	  This can be used to simulate slippery surfaces such as ice or oil by changing the value (possibly based on the material pawn is standing on).<br>	  @see BrakingDecelerationWalking, BrakingFriction, bUseSeparateBrakingFriction, BrakingFrictionFactor |
| MaxWalkSpeed | `float` | The maximum ground speed when walking. Also determines maximum lateral speed when falling. |
| MaxWalkSpeedCrouched | `float` | The maximum ground speed when walking and crouched. |
| MaxSwimSpeed | `float` | The maximum swimming speed. |
| MaxFlySpeed | `float` | The maximum flying speed. |
| MaxCustomMovementSpeed | `float` | The maximum speed when using Custom movement mode. |
| MaxAcceleration | `float` | Max Acceleration (rate of change of velocity) |
| MinAnalogWalkSpeed | `float` | The ground speed that we should accelerate up to when walking at minimum analog stick tilt |
| BrakingFrictionFactor | `float` | Factor used to multiply actual value of friction used when braking.<br>	  This applies to any friction value that is currently used, which may depend on bUseSeparateBrakingFriction.<br>	  @note This is 2 by default for historical reasons, a value of 1 gives the true drag equation.<br>	  @see bUseSeparateBrakingFriction, GroundFriction, BrakingFriction |
| BrakingFriction | `float` | Friction (drag) coefficient applied when braking (whenever Acceleration = 0, or if character is exceeding max speed); actual value used is this multiplied by BrakingFrictionFactor.<br>	  When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.<br>	  Braking is composed of friction (velocity-dependent drag) and constant deceleration.<br>	  This is the current value, used in all movement modes; if this is not desired, override it or bUseSeparateBrakingFriction when movement mode changes.<br>	  @note Only used if bUseSeparateBrakingFriction setting is true, otherwise current friction such as GroundFriction is used.<br>	  @see bUseSeparateBrakingFriction, BrakingFrictionFactor, GroundFriction, BrakingDecelerationWalking |
| bUseSeparateBrakingFriction | `uint32` | If true, BrakingFriction will be used to slow the character to a stop (when there is no Acceleration).<br>	  If false, braking uses the same friction passed to CalcVelocity() (ie GroundFriction when walking), multiplied by BrakingFrictionFactor.<br>	  This setting applies to all movement modes; if only desired in certain modes, consider toggling it when movement modes change.<br>	  @see BrakingFriction |
| BrakingDecelerationWalking | `float` | Deceleration when walking and not applying acceleration. This is a constant opposing force that directly lowers velocity by a constant value.<br>	  @see GroundFriction, MaxAcceleration |
| BrakingDecelerationFalling | `float` | Lateral deceleration when falling and not applying acceleration.<br>	  @see MaxAcceleration |
| BrakingDecelerationSwimming | `float` | Deceleration when swimming and not applying acceleration.<br>	  @see MaxAcceleration |
| BrakingDecelerationFlying | `float` | Deceleration when flying and not applying acceleration.<br>	  @see MaxAcceleration |
| AirControl | `float` | When falling, amount of lateral movement control available to the character.<br>	  0 = no control, 1 = full control at max speed of MaxWalkSpeed. |
| AirControlBoostMultiplier | `float` | When falling, multiplier applied to AirControl when lateral velocity is less than AirControlBoostVelocityThreshold.<br>	  Setting this to zero will disable air control boosting. Final result is clamped at 1. |
| AirControlBoostVelocityThreshold | `float` | When falling, if lateral velocity magnitude is less than this value, AirControl is multiplied by AirControlBoostMultiplier.<br>	  Setting this to zero will disable air control boosting. |
| FallingLateralFriction | `float` | Friction to apply to lateral air movement when falling.<br>	  If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero).<br>	  @see BrakingFriction, bUseSeparateBrakingFriction |
| CrouchedHalfHeight | `float` | Collision half-height when crouching (component scale is applied separately) |
| Buoyancy | `float` | Water buoyancy. A ratio (1.0 = neutral buoyancy, 0.0 = no buoyancy) |
| PerchRadiusThreshold | `float` | Don't allow the character to perch on the edge of a surface if the contact is this close to the edge of the capsule.<br>	  Note that characters will not fall off if they are within MaxStepHeight of a walkable surface below. |
| PerchAdditionalHeight | `float` | When perching on a ledge, add this additional distance to MaxStepHeight when determining how high above a walkable floor we can perch.<br>	  Note that we still enforce MaxStepHeight to start the step up; this just allows the character to hang off the edge or step slightly higher off the floor.<br>	  (@see PerchRadiusThreshold) |
| RotationRate | [FRotator](../../cppstruct/F/FR/FRotator.md) | Change in rotation per second, used when UseControllerDesiredRotation or OrientRotationToMovement are true. Set a negative value for infinite rotation rate and instant turns. |
| bUseControllerDesiredRotation | `uint32` | If true, smoothly rotate the Character toward the Controller's desired rotation (typically Controller->ControlRotation), using RotationRate as the rate of rotation change. Overridden by OrientRotationToMovement.<br>	  Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character. |
| bOrientRotationToMovement | `uint32` | If true, rotate the Character toward the direction of acceleration, using RotationRate as the rate of rotation change. Overrides UseControllerDesiredRotation.<br>	  Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character. |
| bSweepWhileNavWalking | `uint32` | Whether or not the character should sweep for collision geometry while walking.<br>	  @see USceneComponent::MoveComponent. |
| bMovementInProgress | `uint32` | True during movement update.<br>	  Used internally so that attempts to change CharacterOwner and UpdatedComponent are deferred until after an update.<br>	  @see IsMovementInProgress() |
| bEnableScopedMovementUpdates | `uint32` | If true, high-level movement updates will be wrapped in a movement scope that accumulates updates and defers a bulk of the work until the end.<br>	  When enabled, touch and hit events will not be triggered until the end of multiple moves within an update, which can improve performance.<br><br>	  @see FScopedMovementUpdate |
| bForceMaxAccel | `uint32` | Ignores size of acceleration component, and forces max acceleration to drive character at full velocity. |
| bRunPhysicsWithNoController | `uint32` | If true, movement will be performed even if there is no Controller for the Character owner.<br>	  Normally without a Controller, movement will be aborted and velocity and acceleration are zeroed if the character is walking.<br>	  Characters that are spawned without a Controller but with this flag enabled will initialize the movement mode to DefaultLandMovementMode or DefaultWaterMovementMode appropriately.<br>	  @see DefaultLandMovementMode, DefaultWaterMovementMode |
| bForceNextFloorCheck | `uint32` | Force the Character in MOVE_Walking to do a check for a valid floor even if he hasn't moved. Cleared after next floor check.<br>	  Normally if bAlwaysCheckFloor is false we try to avoid the floor check unless some conditions are met, but this can be used to force the next check to always run. |
| bShrinkProxyCapsule | `uint32` | If true, the capsule needs to be shrunk on this simulated proxy, to avoid replication rounding putting us in geometry.<br>	   Whenever this is set to true, this will cause the capsule to be shrunk again on the next update, and then set to false. |
| bCanWalkOffLedges | `uint32` | If true, Character can walk off a ledge. |
| bCanWalkOffLedgesWhenCrouching | `uint32` | If true, Character can walk off a ledge when crouching. |
| bNetworkSmoothingComplete | `uint32` | Signals that smoothed positionrotation has reached target, and no more smoothing is necessary until a future update.<br>	  This is used as an optimization to skip calls to SmoothClientPosition() when true. SmoothCorrection() sets it false when a new network update is received.<br>	  SmoothClientPosition_Interpolate() sets this to true when the interpolation reaches the target, before one last call to SmoothClientPosition_UpdateVisuals().<br>	  If this is not desired, override SmoothClientPosition() to always set this to false to avoid this feature. |
| bNetworkSkipProxyPredictionOnNetUpdate | `uint32` | Whether we skip prediction on frames where a proxy receives a network update. This can avoid expensive prediction on those frames,<br>	 with the side-effect of predicting with a frame of additional latency. |
| bForceNoSimulatePrediction | `uint32` | Whether we skip prediction on simulate movement, only interpolate from server replicated movement |
| bDeferUpdateMoveComponent | `uint32` | true to update CharacterOwner and UpdatedComponent after movement ends |
| DeferredUpdatedMoveComponent | `USceneComponent *` | What to update CharacterOwner and UpdatedComponent after movement ends |
| MaxOutOfWaterStepHeight | `float` | Maximum step height for getting out of water |
| OutofWaterZ | `float` | Z velocity applied when pawn tries to get out of water |
| Mass | `float` | Mass of pawn (for when momentum is imparted to it). |
| bEnablePhysicsInteraction | `bool` | If enabled, the player will interact with physics objects when walking into them. |
| bTouchForceScaledToMass | `bool` | If enabled, the TouchForceFactor is applied per kg mass of the affected object. |
| bPushForceScaledToMass | `bool` | If enabled, the PushForceFactor is applied per kg mass of the affected object. |
| bPushForceUsingZOffset | `bool` | If enabled, the PushForce location is moved using PushForcePointZOffsetFactor. Otherwise simply use the impact point. |
| bScalePushForceToVelocity | `bool` | If enabled, the applied push force will try to get the physics object to the same velocity than the player, not faster. This will only<br>		scale the force down, it will never apply more force than defined by PushForceFactor. |
| StandingDownwardForceScale | `float` | Force applied to objects we stand on (due to Mass and Gravity) is scaled by this amount. |
| InitialPushForceFactor | `float` | Initial impulse force to apply when the player bounces into a blocking physics object. |
| PushForceFactor | `float` | Force to apply when the player collides with a blocking physics object. |
| PushForcePointZOffsetFactor | `float` | Z-Offset for the position the force is applied to. 0.0f is the center of the physics object, 1.0f is the top and -1.0f is the bottom of the object. |
| TouchForceFactor | `float` | Force to apply to physics objects that are touched by the player. |
| MinTouchForce | `float` | Minimum Force applied to touched physics objects. If < 0.0f, there is no minimum. |
| MaxTouchForce | `float` | Maximum force applied to touched physics objects. If < 0.0f, there is no maximum. |
| RepulsionForce | `float` | Force per kg applied constantly to all overlapping components. |
| bForceBraking_DEPRECATED | `uint32` |  |
| CrouchedSpeedMultiplier_DEPRECATED | `float` | Multiplier to max ground speed to use when crouched |
| UpperImpactNormalScale_DEPRECATED | `float` |  |
| Acceleration | [FVector](../../cppstruct/F/FV/FVector.md) | Current acceleration vector (with magnitude).<br>	  This is calculated each update based on the input vector and the constraints of MaxAcceleration and the current movement mode. |
| LastUpdateLocation | [FVector](../../cppstruct/F/FV/FVector.md) | Location after last PerformMovement or SimulateMovement update. Used internally to detect changes in position from outside character movement to try to validate the current floor. |
| LastUpdateRotation | [FQuat](../../cppstruct/F/FQ/FQuat.md) | Rotation after last PerformMovement or SimulateMovement update. |
| LastUpdateVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | Velocity after last PerformMovement or SimulateMovement update. Used internally to detect changes in velocity from external sources. |
| ServerLastTransformUpdateTimeStamp | `float` | Timestamp when location or rotation last changed during an update. Only valid on the server. |
| PendingImpulseToApply | [FVector](../../cppstruct/F/FV/FVector.md) | Accumulated impulse to be added next tick. |
| PendingForceToApply | [FVector](../../cppstruct/F/FV/FVector.md) | Accumulated force to be added next tick. |
| AnalogInputModifier | `float` | Modifier to applied to values such as acceleration and max speed due to analog input. |
| LastStuckWarningTime | `float` | Used for throttling "stuck in geometry" logging. |
| LastPrintApplyImpactPhysicsForcesLog | `float` |  |
| MaxSimulationTimeStep | `float` | Max time delta for each discrete simulation step.<br>	  Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).<br>	  Lowering this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br><br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationIterations |
| MaxSimulationIterations | `int32` | Max number of iterations used for each discrete simulation step.<br>	  Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).<br>	  Increasing this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br><br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationTimeStep |
| MaxDepenetrationWithGeometry | `float` | Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.<br>	 This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.<br>	 @see MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy |
| MaxDepenetrationWithGeometryAsProxy | `float` | Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.<br>	 This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.<br>	 @see MaxDepenetrationWithGeometry, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy |
| MaxDepenetrationWithPawn | `float` | Max distance we are allowed to depenetrate when moving out of other Pawns.<br>	 @see MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawnAsProxy |
| MaxDepenetrationWithPawnAsProxy | `float` | Max distance we allow simulated proxies to depenetrate when moving out of other Pawns.<br>	  Typically we don't want a large value, because we receive a server authoritative position that we should not then ignore by pushing them out of the local player.<br>	  @see MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn |
| NetworkSimulatedSmoothLocationTime | `float` | How long to take to smoothly interpolate from the old pawn position on the client to the corrected one sent by the server. Not used by Linear smoothing. |
| NetworkSimulatedSmoothRotationTime | `float` | How long to take to smoothly interpolate from the old pawn rotation on the client to the corrected one sent by the server. Not used by Linear smoothing. |
| ListenServerNetworkSimulatedSmoothLocationTime | `float` | Similar setting as NetworkSimulatedSmoothLocationTime but only used on Listen servers. |
| ListenServerNetworkSimulatedSmoothRotationTime | `float` | Similar setting as NetworkSimulatedSmoothRotationTime but only used on Listen servers. |
| NetProxyShrinkRadius | `float` | Shrink simulated proxy capsule radius by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.<br>	  @see AdjustProxyCapsuleSize() |
| NetProxyShrinkHalfHeight | `float` | Shrink simulated proxy capsule half height by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.<br>	  @see AdjustProxyCapsuleSize() |
| NetworkMaxSmoothUpdateDistance | `float` | Maximum distance character is allowed to lag behind server location when interpolating between updates. |
| NetworkNoSmoothUpdateDistance | `float` | Maximum distance beyond which character is teleported to the new server location without any smoothing. |
| bReplaySmoothUseInterp | `bool` |  |
| NetworkSmoothingMode | [ENetworkSmoothingMode](../../cppenum/E/EN/ENetworkSmoothingMode.md) | Smoothing mode for simulated proxies in network game. |
| LedgeCheckThreshold | `float` | Used in determining if pawn is going off ledge.  If the ledge is "shorter" than this value then the pawn will be able to walk off it. |
| JumpOutOfWaterPitch | `float` | When exiting water, jump if control pitch angle is this high or above. |
| CurrentFloor | [FFindFloorResult](../../cppstruct/F/FF/FFindFloorResult.md) | Information about the floor the Character is standing on (updated only during walking movement). |
| DefaultLandMovementMode | `TEnumAsByte < enum EMovementMode >` | Default movement mode when not in water. Used at player startup or when teleported.<br>	  @see DefaultWaterMovementMode<br>	  @see bRunPhysicsWithNoController |
| DefaultWaterMovementMode | `TEnumAsByte < enum EMovementMode >` | Default movement mode when in water. Used at player startup or when teleported.<br>	  @see DefaultLandMovementMode<br>	  @see bRunPhysicsWithNoController |
| GroundMovementMode | `TEnumAsByte < enum EMovementMode >` | Ground movement mode to switch to after falling and resuming ground movement.<br>	  Only allowed values are: MOVE_Walking, MOVE_NavWalking.<br>	  @see SetGroundMovementMode(), GetGroundMovementMode() |
| bMaintainHorizontalGroundVelocity | `uint32` | If true, walking movement always maintains horizontal velocity when moving up ramps, which causes movement up ramps to be faster parallel to the ramp surface.<br>	  If false, then walking movement maintains velocity magnitude parallel to the ramp surface. |
| bImpartBaseVelocityX | `uint32` | If true, impart the base actor's X velocity when falling off it (which includes jumping) |
| bImpartBaseVelocityY | `uint32` | If true, impart the base actor's Y velocity when falling off it (which includes jumping) |
| bImpartBaseVelocityZ | `uint32` | If true, impart the base actor's Z velocity when falling off it (which includes jumping) |
| bImpartBaseAngularVelocity | `uint32` | If true, impart the base component's tangential components of angular velocity when jumping or falling off it.<br>	  Only those components of the velocity allowed by the separate component settings (bImpartBaseVelocityX etc) will be applied.<br>	  @see bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ |
| bJustTeleported | `uint32` | Used by movement code to determine if a change in position is based on normal movement or a teleport. If not a teleport, velocity can be recomputed based on the change in position. |
| bNetworkUpdateReceived | `uint32` | True when a network replication update is received for simulated proxies. |
| bNetworkMovementModeChanged | `uint32` | True when the networked movement mode has been replicated. |
| bIgnoreClientMovementErrorChecksAndCorrection | `uint32` | True when we should ignore server location difference checks for client error on this movement component<br>	  This can be useful when character is moving at extreme speeds for a duration and you need it to look<br>	  smooth on clients. Make sure to disable when done, as this would break this character's server-client<br>	  movement correction. |
| bNotifyApex | `uint32` | If true, event NotifyJumpApex() to CharacterOwner's controller when at apex of jump. Is cleared when event is triggered.<br>	  By default this is off, and if you want the event to fire you typically set it to true when movement mode changes to "Falling" from another mode (see OnMovementModeChanged). |
| bCheatFlying | `uint32` | Instantly stop when in flying mode and no acceleration is being applied. |
| bWantsToCrouch | `uint32` | If true, try to crouch (or keep crouching) on next update. If false, try to stop crouching on next update. |
| bCrouchMaintainsBaseLocation | `uint32` | If true, crouching should keep the base of the capsule in place by lowering the center of the shrunken capsule. If false, the base of the capsule moves up and the center stays in place.<br>	  The same behavior applies when the character uncrouches: if true, the base is kept in the same location and the center moves up. If false, the capsule grows and only moves up if the base impacts something.<br>	  By default this variable is set when the movement mode changes: set to true when walking and false otherwise. Feel free to override the behavior when the movement mode changes. |
| bIgnoreBaseRotation | `uint32` | Whether the character ignores changes in rotation of the base it is standing on.<br>	  If true, the character maintains current world rotation.<br>	  If false, the character rotates with the moving base. |
| bFastAttachedMove | `uint32` | Set this to true if riding on a moving base that you know is clear from non-moving world obstructions.<br>	  Optimization to avoid sweeps during based movement, use with care. |
| bAlwaysCheckFloor | `uint32` | Whether we always force floor checks for stationary Characters while walking.<br>	  Normally floor checks are avoided if possible when not moving, but this can be used to force them if there are use-cases where they are being skipped erroneously<br>	  (such as objects moving up into the character from below). |
| bUseFlatBaseForFloorChecks | `uint32` | Performs floor checks as if the character is using a shape with a flat base.<br>	  This avoids the situation where characters slowly lower off the side of a ledge (as their capsule 'balances' on the edge). |
| bPerformingJumpOff | `uint32` | Used to prevent reentry of JumpOff() |
| bWantsToLeaveNavWalking | `uint32` | Used to safely leave NavWalking movement mode |
| bUseRVOAvoidance | `uint32` | If set, component will use RVO avoidance. This only runs on the server. |
| bRequestedMoveUseAcceleration | `uint32` | Should use acceleration for path following?<br>	  If true, acceleration is applied when path following to reach the target velocity.<br>	  If false, path following velocity is set directly, disregarding acceleration. |
| bIsNavWalkingOnServer | `uint32` | Set on clients when server's movement mode is NavWalking |
| bHasRequestedVelocity | `uint32` | Was velocity requested by path following? |
| bRequestedMoveWithMaxSpeed | `uint32` | Was acceleration requested to be always max speed? |
| bWasAvoidanceUpdated | `uint32` | Was avoidance updated in this frame? |
| bUseRVOPostProcess | `uint32` | if set, PostProcessAvoidanceVelocity will be called |
| bDeferUpdateBasedMovement | `uint32` | Flag set in pre-physics update to indicate that based movement should be updated post-physics |
| bProjectNavMeshWalking | `uint32` | Whether to raycast to underlying geometry to better conform navmesh-walking characters |
| bProjectNavMeshOnBothWorldChannels | `uint32` | Use both WorldStatic and WorldDynamic channels for NavWalking geometry conforming |
| AvoidanceLockVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | forced avoidance velocity, used when AvoidanceLockTimer is > 0 |
| AvoidanceLockTimer | `float` | remaining time of avoidance velocity lock |
| AvoidanceConsiderationRadius | `float` |  |
| RequestedVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | Velocity requested by path following.<br>	  @see RequestDirectMove() |
| AvoidanceUID | `int32` | No default value, for now it's assumed to be valid if GetAvoidanceManager() returns non-NULL. |
| AvoidanceGroup | [FNavAvoidanceMask](../../cppstruct/F/FN/FNavAvoidanceMask.md) | Moving actor's group mask |
| GroupsToAvoid | [FNavAvoidanceMask](../../cppstruct/F/FN/FNavAvoidanceMask.md) | Will avoid other agents if they are in one of specified groups |
| GroupsToIgnore | [FNavAvoidanceMask](../../cppstruct/F/FN/FNavAvoidanceMask.md) | Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid |
| AvoidanceWeight | `float` | De facto default value 0.5 (due to that being the default in the avoidance registration function), indicates RVO behavior. |
| PendingLaunchVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | Temporarily holds launch velocity when pawn is to be launched so it happens at end of movement. |
| CachedProjectedNavMeshHitResult | [FHitResult](../../cppstruct/F/FH/FHitResult.md) | Last valid projected hit result from raycast to geometry from navmesh |
| NavMeshProjectionInterval | `float` | How often we should raycast to project from navmesh to underlying geometry |
| NavMeshProjectionTimer | `float` |  |
| NavMeshProjectionInterpSpeed | `float` | Speed at which to interpolate agent navmesh offset between traces. 0: Instant (no interp) > 0: Interp speed") |
| NavMeshProjectionHeightScaleUp | `float` | Scale of the total capsule height to use for projection from navmesh to underlying geometry in the upward direction.<br>	  In other words, start the trace at [CapsuleHeight  NavMeshProjectionHeightScaleUp] above nav mesh. |
| NavMeshProjectionHeightScaleDown | `float` | Scale of the total capsule height to use for projection from navmesh to underlying geometry in the downward direction.<br>	  In other words, trace down to [CapsuleHeight  NavMeshProjectionHeightScaleDown] below nav mesh. |
| NavWalkingFloorDistTolerance | `float` | Ignore small differences in ground height between server and client data during NavWalking mode |
| PostPhysicsTickFunction | `FCharacterMovementComponentPostPhysicsTickFunction` | Post-physics tick function for this character |
| MinTimeBetweenTimeStampResets | `float` | Minimum time between client TimeStamp resets.<br>	 So we trigger a TimeStamp reset at regular intervals to maintain a high level of accuracy. |
| CurrentRootMotion | [FRootMotionSourceGroup](../../cppstruct/F/FR/FRootMotionSourceGroup.md) | Root Motion Group containing active root motion sources being applied to movement |
| RootMotionParams | [FRootMotionMovementParams](../../cppstruct/F/FR/FRootMotionMovementParams.md) | Animation root motion (special case for now)<br><br>	 Root Motion movement params. Holds result of anim montage root motion during PerformMovement(), and is overridden<br>	   during autonomous move playback to force historical root motion for MoveAutonomous() calls |
| AnimRootMotionVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | Velocity extracted from RootMotionParams when there is anim root motion active. Invalid to use when HasAnimRootMotion() returns false. |
| bWasSimulatingRootMotion | `bool` | True when SimulatedProxies are simulating RootMotion |
| bAllowPhysicsRotationDuringAnimRootMotion | `uint32` |  |

## Functions

### GetToString

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAvoidanceGroup

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupFlags | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetAvoidanceGroupMask

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupMask | `FNavAvoidanceMask &` |  |

**Return**

- Type: 
- Description: _None_

### SetGroupsToAvoid

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupFlags | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetGroupsToAvoidMask

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupMask | `FNavAvoidanceMask &` |  |

**Return**

- Type: 
- Description: _None_

### SetGroupsToIgnore

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupFlags | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetGroupsToIgnoreMask

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupMask | `FNavAvoidanceMask &` |  |

**Return**

- Type: 
- Description: _None_

### SetAvoidanceEnabled

Change avoidance state and registers in RVO manager if needed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetCharacterOwner

Get the Character that owns UpdatedComponent.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMovementMode

Change movement mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMovementMode | `EMovementMode` | The new movement mode |
| NewCustomMode | `uint8` | The new custom sub-mode, only applicable if NewMovementMode is Custom. |

**Return**

- Type: 
- Description: _None_

### SetGroundMovementMode

Set movement mode to use when returning to walking movement (either MOVE_Walking or MOVE_NavWalking).
	  If movement mode is currently one of Walking or NavWalking, this will also change the current movement mode (via SetMovementMode())
	  if the new mode is not the current ground mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewGroundMovementMode | [EMovementMode](../../cppenum/E/EM/EMovementMode.md) | New ground movement mode. Must be either MOVE_Walking or MOVE_NavWalking, other values are ignored. |

**Return**

- Type: 
- Description: _None_

### GetGroundMovementMode

Get current GroundMovementMode value.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PackNetworkMovementMode

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UnpackNetworkMovementMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ReceivedMode | `uint8` |  |
| OutMode | `TEnumAsByte < EMovementMode > &` |  |
| OutCustomMode | `uint8 &` |  |
| OutGroundMode | `TEnumAsByte < EMovementMode > &` |  |

**Return**

- Type: 
- Description: _None_

### ApplyNetworkMovementMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ReceivedMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### CheckBaseIsMoveable

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MovementBase | `USceneComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsWalking

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DisableMovement

Make movement impossible (sets movement mode to MOVE_None).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasValidData

Return true if we have a valid CharacterOwner and UpdatedComponent.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMovementBase

Return PrimitiveComponent we are based on (standing and walking on).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MaybeUpdateBasedMovement

Update or defer updating of position based on Base movement

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### MaybeSaveBaseLocation

Call SaveBaseLocation() if not deferring updates (bDeferUpdateBasedMovement is false).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetImpartedMovementBaseVelocity

If we have a movement base, get the velocity that should be imparted by that base, usually when jumping off of it.
	  Only applies the components of the velocity enabled by bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CalcVelocity

Updates Velocity and Acceleration based on the current state, applying the effects of friction and acceleration or deceleration. Does not apply gravity.
	  This is used internally during movement updates. Normally you don't need to call this from outside code, but you might want to use it for custom movement modes.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTime | `float` | time elapsed since last frame. |
| Friction | `float` | coefficient of friction when not accelerating, or in the direction opposite acceleration. |
| bFluid | `bool` | true if moving through a fluid, causing Friction to always be applied regardless of acceleration. |
| BrakingDeceleration | `float` | deceleration applied when not accelerating, or when exceeding max velocity. |

**Return**

- Type: 
- Description: _None_

### GetMaxJumpHeight

Compute the max jump height based on the JumpZVelocity velocity and gravity.
	 	This does not take into account the CharacterOwner's MaxJumpHoldTime.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaxJumpHeightWithJumpTime

Compute the max jump height based on the JumpZVelocity velocity and gravity.
	 	This does take into account the CharacterOwner's MaxJumpHoldTime.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMinAnalogSpeed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetModifiedMaxAcceleration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaxAcceleration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaxBrakingDeceleration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentAcceleration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAnalogInputModifier

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanStepUp

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### SetBase

Update the base of the character, which is the PrimitiveComponent we are standing on.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewBase | `UPrimitiveComponent *` |  |
| BoneName | `FName` |  |
| bNotifyActor | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBaseFromFloor

Update the base of the character, using the given floor result if it is walkable, or null if not. Calls SetBase().

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FloorResult | `FFindFloorResult &` |  |

**Return**

- Type: 
- Description: _None_

### ClearAccumulatedForces

Clears forces accumulated through AddImpulse() and AddForce(), and also pending launch velocity.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasAccumulatedForcesOrLaunch

Add by zoranouyang
	 Is there AddImpulse() or AddForce() or Launch()?

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddImpulse

Add impulse to character. Impulses are accumulated each tick and applied together
	  so multiple calls to this function will accumulate.
	  An impulse is an instantaneous force, usually applied once. If you want to continually apply
	  forces each frame, use AddForce().
	  Note that changing the momentum of characters like this can change the movement mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` | Impulse to apply. |
| bVelocityChange | `bool` | Whether or not the impulse is relative to mass. |

**Return**

- Type: 
- Description: _None_

### AddForce

Add force to character. Forces are accumulated each tick and applied together
	  so multiple calls to this function will accumulate.
	  Forces are scaled depending on timestep, so they can be applied each frame. If you want an
	  instantaneous force, use AddImpulse.
	  Adding a force always takes the actor's mass into account.
	  Note that changing the momentum of characters like this can change the movement mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | [FVector](../../cppstruct/F/FV/FVector.md) | Force to apply. |

**Return**

- Type: 
- Description: _None_

### GetPerchRadiusThreshold

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetValidPerchRadius

Returns the radius within which we can stand on the edge of a surface without falling (if this is a walkable surface).
	  Simply computed as the capsule radius minus the result of GetPerchRadiusThreshold().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsWalkable

Return true if the hit result should be considered a walkable surface for the character.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetWalkableFloorAngle

Get the max angle in degrees of a walkable surface for the character.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWalkableFloorAngle

Set the max angle in degrees of a walkable surface for the character. Also computes WalkableFloorZ.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWalkableFloorAngle | `float` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetWalkableFloorZ

Get the Z component of the normal of the steepest walkable surface for the character. Any lower than this and it is not walkable.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWalkableFloorZ

Set the Z component of the normal of the steepest walkable surface for the character. Also computes WalkableFloorAngle.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWalkableFloorZ | `float` |  |

**Return**

- Type: 
- Description: _None_

### K2_FindFloor

Sweeps a vertical trace to find the floor for the capsule at the given location. Will attempt to perch if ShouldComputePerchResult() returns true for the downward sweep result.
	 No floor will be found if collision is disabled on the capsule!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CapsuleLocation | `FVector` | Location where the capsule sweep should originate |
| FloorResult | `FFindFloorResult &` | Result of the floor check |

**Return**

- Type: 
- Description: _None_

### K2_ComputeFloorDist

Compute distance to the floor from bottom sphere of capsule and store the result in FloorResult.
	 This distance is the swept distance of the capsule to the first point impacted by the lower hemisphere, or distance from the bottom of the capsule in the case of a line trace.
	 This function does not care if collision is disabled on the capsule (unlike FindFloor).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CapsuleLocation | `FVector` | Location where the capsule sweep should originate |
| LineDistance | `float` | If non-zero, max distance to test for a simple line check from the capsule base. Used only if the sweep test fails to find a walkable floor, and only returns a valid result if the impact normal is a walkable normal. |
| SweepDistance | `float` | If non-zero, max distance to use when sweeping a capsule downwards for the test. MUST be greater than or equal to the line distance. |
| SweepRadius | `float` | The radius to use for sweep tests. Should be <= capsule radius. |
| FloorResult | `FFindFloorResult &` | Result of the floor check |

**Return**

- Type: 
- Description: _None_

### CapsuleTouched

Called when the collision capsule touches another primitive component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OverlappedComp | `UPrimitiveComponent *` |  |
| Other | `AActor *` |  |
| OtherComp | `UPrimitiveComponent *` |  |
| OtherBodyIndex | `int32` |  |
| bFromSweep | `bool` |  |
| SweepResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### ResetPredictionData_Client

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetPredictionData_Server

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSmoothNetUpdateRotationTimeTemporaty

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSmoothNetUpdateRotationTimeTemporaty

Add by zoranouyang
	 临时的SmoothNetUpdateRotationTime，用于部分情况下需要一段时间内修改一下模拟端Rotation插值速度
	 主要还是以NetworkSimulatedSmoothRotationTime配置为主
	 注意：本值要记得还原到-1，表示不生效

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSmoothNetUpdateRotationTime | `float` | 模拟端的Rotation插值时间，默认值-1表示使用NetworkSimulatedSmoothRotationTime配置的值 |

**Return**

- Type: 
- Description: _None_

### ServerMove

Replicated function sent by client to server - contains client movement and view info.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |
| InAccel | `FVector_NetQuantize10` |  |
| ClientLoc | `FVector_NetQuantize100` |  |
| CompressedMoveFlags | `uint8` |  |
| ClientRoll | `uint8` |  |
| View | `uint32` |  |
| ClientMovementBase | `UPrimitiveComponent *` |  |
| ClientBaseBoneName | `FName` |  |
| ClientMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ServerMoveDual

Replicated function sent by client to server - contains client movement and view info for two moves.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp0 | `float` |  |
| InAccel0 | `FVector_NetQuantize10` |  |
| PendingFlags | `uint8` |  |
| View0 | `uint32` |  |
| TimeStamp | `float` |  |
| InAccel | `FVector_NetQuantize10` |  |
| ClientLoc | `FVector_NetQuantize100` |  |
| NewFlags | `uint8` |  |
| ClientRoll | `uint8` |  |
| View | `uint32` |  |
| ClientMovementBase | `UPrimitiveComponent *` |  |
| ClientBaseBoneName | `FName` |  |
| ClientMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ServerMoveDualHybridRootMotion

Replicated function sent by client to server - contains client movement and view info for two moves. First move is non root motion, second is root motion.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp0 | `float` |  |
| InAccel0 | `FVector_NetQuantize10` |  |
| PendingFlags | `uint8` |  |
| View0 | `uint32` |  |
| TimeStamp | `float` |  |
| InAccel | `FVector_NetQuantize10` |  |
| ClientLoc | `FVector_NetQuantize100` |  |
| NewFlags | `uint8` |  |
| ClientRoll | `uint8` |  |
| View | `uint32` |  |
| ClientMovementBase | `UPrimitiveComponent *` |  |
| ClientBaseBoneName | `FName` |  |
| ClientMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ServerMoveOld

Resending an (important) old move. Process it if not already processed.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldTimeStamp | `float` |  |
| OldAccel | `FVector_NetQuantize10` |  |
| OldMoveFlags | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ClientAckGoodMove

If no client adjustment is needed after processing received ServerMove(), ack the good move so client can remove it from SavedMoves

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |

**Return**

- Type: 
- Description: _None_

### OnGoodMoveAck

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClientAdjustPosition

Replicate position correction to client, associated with a timestamped servermove.  Client will replay subsequent moves after applying adjustment.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |
| NewLoc | `FVector` |  |
| NewVel | `FVector` |  |
| NewBase | `UPrimitiveComponent *` |  |
| NewBaseBoneName | `FName` |  |
| bHasBase | `bool` |  |
| bBaseRelativePosition | `bool` |  |
| ServerMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ClientVeryShortAdjustPosition

Bandwidth saving version, when velocity is zeroed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |
| NewLoc | `FVector` |  |
| NewBase | `UPrimitiveComponent *` |  |
| NewBaseBoneName | `FName` |  |
| bHasBase | `bool` |  |
| bBaseRelativePosition | `bool` |  |
| ServerMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ClientAdjustRootMotionPosition

Replicate position correction to client when using root motion for movement. (animation root motion specific)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |
| ServerMontageTrackPosition | `float` |  |
| ServerLoc | `FVector` |  |
| ServerRotation | `FVector_NetQuantizeNormal` |  |
| ServerVelZ | `float` |  |
| ServerBase | `UPrimitiveComponent *` |  |
| ServerBoneName | `FName` |  |
| bHasBase | `bool` |  |
| bBaseRelativePosition | `bool` |  |
| ServerMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ClientAdjustRootMotionSourcePosition

Replicate root motion source correction to client when using root motion for movement.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeStamp | `float` |  |
| ServerRootMotion | `FRootMotionSourceGroup` |  |
| bHasAnimRootMotion | `bool` |  |
| ServerMontageTrackPosition | `float` |  |
| ServerLoc | `FVector` |  |
| ServerRotation | `FVector_NetQuantizeNormal` |  |
| ServerVelZ | `float` |  |
| ServerBase | `UPrimitiveComponent *` |  |
| ServerBoneName | `FName` |  |
| bHasBase | `bool` |  |
| bBaseRelativePosition | `bool` |  |
| ServerMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

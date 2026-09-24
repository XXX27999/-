# FBodyInstance

Container for a physics representation of an object

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SleepFamily | [ESleepFamily](../../../cppenum/E/ES/ESleepFamily.md) | The set of values used in considering when put this body to sleep. |
| DOFMode | `TEnumAsByte < EDOFMode :: Type >` | Locks physical movement along specified axis. |
| CollisionEnabled | `TEnumAsByte < ECollisionEnabled :: Type >` | Type of collision enabled.<br><br>	 	No Collision      : Will not create any representation in the physics engine. Cannot be used for spatial queries (raycasts, sweeps, overlaps) or simulation (rigid body, constraints). Best performance possible (especially for moving objects)<br>	 	Query Only        : Only used for spatial queries (raycasts, sweeps, and overlaps). Cannot be used for simulation (rigid body, constraints). Useful for character movement and things that do not need physical simulation. Performance gains by keeping data out of simulation tree.<br>	 	Physics Only      : Only used only for physics simulation (rigid body, constraints). Cannot be used for spatial queries (raycasts, sweeps, overlaps). Useful for jiggly bits on characters that do not need per bone detection. Performance gains by keeping data out of query tree<br>	 	Collision Enabled : Can be used for both spatial queries (raycasts, sweeps, overlaps) and simulation (rigid body, constraints). |
| CollisionProfileName | `FName` | Collision Profile Name |
| CollisionResponses | [FCollisionResponse](../FC/FCollisionResponse.md) | Custom Channels for Responses |
| bUseCCD | `uint8` | If true Continuous Collision Detection (CCD) will be used for this component |
| bNotifyRigidBodyCollision | `uint8` | Should 'Hit' events fire when this object collides during physics simulation. |
| bUseShapeCollisionOverride | `uint8` | PhysicsAsset中有bCollisionPerShape功能，载具中经常用到。<br>	  在使用这个功能时，如果运行时调用了UpdatePhysicsShapeFilterData，shape的flag会被改写为组件中的配置，即bCollisionPerShape功能无效了。<br>	  这里增加一个开关，如果为true，在UpdatePhysicsShapeFilterData时也会去应用PA的bCollisionPerShape功能。	-lyonarzhang |
| bSimulatePhysics | `uint8` | If true, this body will use simulation. If false, will be 'fixed' (ie kinematic) and move where it is told.<br>	  For a Skeletal Mesh Component, simulating requires a physics asset setup and assigned on the SkeletalMesh asset.<br>	  For a Static Mesh Component, simulating requires simple collision to be setup on the StaticMesh asset. |
| bOverrideMass | `uint8` | If true, mass will not be automatically computed and you must set it directly |
| bEnableGravity | `uint8` | If object should have the force of gravity applied |
| bAutoWeld | `uint8` | If true and is attached to a parent, the two bodies will be joined into a single rigid body. Physical settings like collision profile and body settings are determined by the root |
| bStartAwake | `uint8` | If object should start awake, or if it should initially be sleeping |
| bGenerateWakeEvents | `uint8` | Should 'wakesleep' events fire when this object is woken up or put to sleep by the physics simulation. |
| bUpdateMassWhenScaleChanges | `uint8` | If true, it will update mass when scale changes |
| bLockTranslation | `uint8` | When a Locked Axis Mode is selected, will lock translation on the specified axis |
| bLockRotation | `uint8` | When a Locked Axis Mode is selected, will lock rotation to the specified axis |
| bLockXTranslation | `uint8` | Lock translation along the X-axis |
| bLockYTranslation | `uint8` | Lock translation along the Y-axis |
| bLockZTranslation | `uint8` | Lock translation along the Z-axis |
| bLockXRotation | `uint8` | Lock rotation about the X-axis |
| bLockYRotation | `uint8` | Lock rotation about the Y-axis |
| bLockZRotation | `uint8` | Lock rotation about the Z-axis |
| bOverrideMaxAngularVelocity | `uint8` | Override the default max angular velocity |
| bUseAsyncScene | `uint8` | If true, this body will be put into the asynchronous physics scene. If false, it will be put into the synchronous physics scene.<br>	 If the body is static, it will be placed into both scenes regardless of the value of bUseAsyncScene. |
| bOverrideMaxDepenetrationVelocity | `uint8` | Whether this body instance has its own custom MaxDepenetrationVelocity |
| bOverrideWalkableSlopeOnInstance | `uint8` | Whether this instance of the object has its own custom walkable slope override setting. |
| MaxDepenetrationVelocity | `float` | The maximum velocity used to depenetrate this object |
| MassInKgOverride | `float` | Mass of the body in KG. By default we compute this based on physical material and mass scale.<br>	@see bOverrideMass to set this directly |
| LinearDamping | `float` | 'Drag' force added to reduce linear movement |
| AngularDamping | `float` | 'Drag' force added to reduce angular movement |
| CustomDOFPlaneNormal | [FVector](../FV/FVector.md) | Locks physical movement along a custom plane for a given normal. |
| COMNudge | [FVector](../FV/FVector.md) | User specified offset for the center of mass of this object, from the calculated location |
| bUseOverrideCOM | `bool` | 为true时，锁定重心位置为OverrideCOM(Component space)，只对载具有效 |
| OverrideCOM | [FVector](../FV/FVector.md) |  |
| MassScale | `float` | Per-instance scaling of mass |
| InertiaTensorScale | [FVector](../FV/FVector.md) | Per-instance scaling of inertia (bigger number means  it'll be harder to rotate) |
| bUsedPhysSimpleStaticMesh | `uint8` |  |
| ObjectType | `TEnumAsByte < enum ECollisionChannel >` | Enum indicating what type of object this should be considered as when it moves |
| WalkableSlopeOverride | [FWalkableSlopeOverride](../FW/FWalkableSlopeOverride.md) | Custom walkable slope override setting for this instance.<br>	 @see GetWalkableSlopeOverride(), SetWalkableSlopeOverride() |
| PhysMaterialOverride | `UPhysicalMaterial *` | Allows you to override the PhysicalMaterial to use for simple collision on this body. |
| MaxAngularVelocity | `float` | The maximum angular velocity for this instance |
| CustomSleepThresholdMultiplier | `float` | If the SleepFamily is set to custom, multiply the natural sleep threshold by this amount. A higher number will cause the body to sleep sooner. |
| StabilizationThresholdMultiplier | `float` | Stabilization factor for this body if Physics stabilization is enabled. A higher number will cause more aggressive stabilization at the risk of loss of momentum at low speeds. A value of 0 will disable stabilization for this body. |
| PhysicsBlendWeight | `float` | Influence of rigid body physics (blending) on the mesh's pose (0.0 == use only animation, 1.0 == use only physics)<br>	 Provide appropriate interface for doing this instead of allowing BlueprintReadWrite |
| PositionSolverIterationCount | `int32` | This physics body's solver iteration count for position. Increasing this will be more CPU intensive, but better stabilized. |
| VelocitySolverIterationCount | `int32` | This physics body's solver iteration count for velocity. Increasing this will be more CPU intensive, but better stabilized. |
| ResponseToChannels_DEPRECATED | [FCollisionResponseContainer](../FC/FCollisionResponseContainer.md) | Types of objects that this physics objects will collide with. |

# UPhysicsSettings

Default physics settings.

## Parents

- UDeveloperSettings

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ServerPvdThresholdMs | `float` | Default ServerPvdThresholdMs. |
| ClientPvdThresholdMs | `float` | Default ClientPvdThresholdMs. |
| ServerPvdRecordTimeSeconds | `int32` | Default ServerPvdRecordTimeSeconds. |
| ClientPvdRecordTimeSeconds | `int32` | Default ClientPvdRecordTimeSeconds. |
| DefaultGravityZ | `float` | Default gravity. |
| DefaultTerminalVelocity | `float` | Default terminal velocity for Physics Volumes. |
| DefaultFluidFriction | `float` | Default fluid friction for Physics Volumes. |
| SimulateScratchMemorySize | `int32` | Amount of memory to reserve for PhysX simulate(), this is per pxscene and will be rounded up to the next 16K boundary |
| RagdollAggregateThreshold | `int32` | Threshold for ragdoll bodies above which they will be added to an aggregate before being added to the scene |
| TriangleMeshTriangleMinAreaThreshold | `float` | Triangles from triangle meshes (BSP) with an area less than or equal to this value will be removed from physics collision data. Set to less than 0 to disable. |
| bEnableAsyncScene | `bool` | Enables the use of an async scene |
| bEnableShapeSharing | `bool` | Enables shape sharing between sync and async scene for static rigid actors |
| bEnablePCM | `bool` | Enables persistent contact manifolds. This will generate fewer contact points, but with more accuracy. Reduces stability of stacking, but can help energy conservation. |
| bEnableStabilization | `bool` | Enables stabilization of contacts for slow moving bodies. This will help improve the stability of stacking. |
| bWarnMissingLocks | `bool` | Whether to warn when physics locks are used incorrectly. Turning this off is not recommended and should only be used by very advanced users. |
| bEnable2DPhysics | `bool` | Can 2D physics be used (Box2D)? |
| PhysicErrorCorrection | [FRigidBodyErrorCorrectionNew](../../cppstruct/F/FR/FRigidBodyErrorCorrectionNew.md) | Error correction data for replicating simulated physics (rigid bodies) |
| LockedAxis_DEPRECATED | `TEnumAsByte < ESettingsLockedAxis :: Type >` |  |
| DefaultDegreesOfFreedom | `TEnumAsByte < ESettingsDOF :: Type >` | Useful for constraining all objects in the world, for example if you are making a 2D game using 3D environments. |
| BounceThresholdVelocity | `float` | Minimum relative velocity required for an object to bounce. A typical value for simulation stability is about 0.2  gravity |
| FrictionCombineMode | `TEnumAsByte < EFrictionCombineMode :: Type >` | Friction combine mode, controls how friction is computed for multiple materials. |
| RestitutionCombineMode | `TEnumAsByte < EFrictionCombineMode :: Type >` | Restitution combine mode, controls how restitution is computed for multiple materials. |
| MaxAngularVelocity | `float` | Max angular velocity that a simulated object can achieve. |
| MaxDepenetrationVelocity | `float` | Max velocity which may be used to depenetrate simulated physics objects. 0 means no maximum. |
| ContactOffsetMultiplier | `float` | Contact offset multiplier. When creating a physics shape we look at its bounding volume and multiply its minimum value by this multiplier. A bigger number will generate contact points earlier which results in higher stability at the cost of performance. |
| MinContactOffset | `float` | Min Contact offset. |
| MaxContactOffset | `float` | Max Contact offset. |
| bSimulateSkeletalMeshOnDedicatedServer | `bool` | If true, simulate physics for this component on a dedicated server.<br>	  This should be set if simulating physics and replicating with a dedicated server. |
| DefaultShapeComplexity | `TEnumAsByte < ECollisionTraceFlag >` | Determines the default physics shape complexity. |
| bDefaultHasComplexCollision_DEPRECATED | `bool` | If true, static meshes will use per poly collision as complex collision by default. If false the default behavior is the same as UseSimpleAsComplex. |
| bSuppressFaceRemapTable | `bool` | If true, the internal physx face to UE face mapping will not be generated. This is a memory optimization available if you do not rely on face indices returned by scene queries. |
| bSupportUVFromHitResults | `bool` | If true, store extra information to allow FindCollisionUV to derive UV info from a line trace hit result, using the FindCollisionUV utility |
| bDisableActiveActors | `bool` | If true, physx will not update unreal with any bodies that have moved during the simulation. This should only be used if you have no physx simulation or you are manually updating the unreal data via polling physx. |
| bDisableCCD | `bool` | If true CCD will be ignored. This is an optimization when CCD is never used which removes the need for physx to check it internally. |
| bEnableEnhancedDeterminism | `bool` | If set to true, the scene will use enhanced determinism at the cost of a bit more resources. See eENABLE_ENHANCED_DETERMINISM to learn about the specifics |
| MaxPhysicsDeltaTime | `float` | Max Physics Delta Time to be clamped. |
| bSubstepping | `bool` | Whether to substep the physics simulation. This feature is still experimental. Certain functionality might not work correctly |
| bSubsteppingAsync | `bool` | Whether to substep the async physics simulation. This feature is still experimental. Certain functionality might not work correctly |
| MaxSubstepDeltaTime | `float` | Max delta time (in seconds) for an individual simulation substep. |
| MaxSubsteps | `int32` | Max number of substeps for physics simulation. |
| ServerMaxSubstepDeltaTime | `float` | pixelchen 服务器单独设置MaxSubstepDeltaTime |
| ServerMaxSubsteps | `int32` | pixelchen 服务器单独设置MaxSubsteps |
| SyncSceneSmoothingFactor | `float` | Physics delta time smoothing factor for sync scene. |
| AsyncSceneSmoothingFactor | `float` | Physics delta time smoothing factor for async scene. |
| InitialAverageFrameRate | `float` | Physics delta time initial average. |
| PhysXTreeRebuildRate | `int` | The number of frames it takes to rebuild the PhysX scene query AABB tree. The bigger the number, the smaller fetchResults takes per frame, but the more the tree deteriorates until a new tree is built |
| PhysicalSurfaces | `TArray < FPhysicalSurfaceName >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

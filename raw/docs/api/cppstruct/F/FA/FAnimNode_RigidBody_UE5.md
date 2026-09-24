# FAnimNode_RigidBody_UE5

Controller that simulates physics based on the physics asset of the skeletal mesh component

## Fields

| Name | Type | Description |
| --- | --- | --- |
| OverridePhysicsAsset | `UPhysicsAsset *` | Physics asset to use. If empty use the skeletal mesh's default physics asset |
| OverrideWorldGravity | [FVector](../FV/FVector.md) | Override gravity |
| ExternalForce | [FVector](../FV/FVector.md) | Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example |
| ComponentLinearAccScale | [FVector](../FV/FVector.md) | When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation. |
| ComponentLinearVelScale | [FVector](../FV/FVector.md) | When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity. |
| ComponentAppliedLinearAccClamp | [FVector](../FV/FVector.md) | When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large. |
| SimSpaceSettings | [FSimSpaceSettings](../FS/FSimSpaceSettings.md) | Settings for the system which passes motion of the simulation's space<br>	  into the simulation. This allows the simulation to pass a<br>	  fraction of the world space motion onto the bodies which allows Bone-Space<br>	  and Component-Space simulations to react to world-space movement in a<br>	  controllable way.<br>	  This system is a superset of the functionality provided by ComponentLinearAccScale,<br>	  ComponentLinearVelScale, and ComponentAppliedLinearAccClamp. In general<br>	  you should not have both systems enabled.<br><br>	UPROPERTY(EditAnywhere not support for without WITH_CHAOS, Category = Settings, meta = (PinHiddenByDefault)) |
| CachedBoundsScale | `float` | Scale of cached bounds (vs. actual bounds).<br>	  Increasing this may improve performance, but overlaps may not work as well.<br>	  (A value of 1.0 effectively disables cached bounds).<br><br>	UPROPERTY(EditAnywhere, Category = Settings, meta = (ClampMin="1.0", ClampMax="2.0")) |
| BaseBoneRef | `FBoneReference` | Matters if SimulationSpace is BaseBone |
| OverlapChannel | `TEnumAsByte < ECollisionChannel >` | The channel we use to find static geometry to collide with<br>	UPROPERTY(EditAnywhere, Category = Settings, meta = (editcondition = "bEnableWorldGeometry")) |
| SimulationSpace | [ESimulationSpace_UE5](../../../cppenum/E/ES/ESimulationSpace_UE5.md) | What space to simulate the bodies in. This affects how velocities are generated |
| bForceDisableCollisionBetweenConstraintBodies | `bool` | Whether to allow collisions between two bodies joined by a constraint |
| bEnableWorldGeometry | `uint8` |  |
| bOverrideWorldGravity | `uint8` | UPROPERTY(EditAnywhere, Category = Settings, meta = (InlineEditConditionToggle)) |
| bTransferBoneVelocities | `uint8` | UPROPERTY(EditAnywhere, Category = Settings, meta=(PinHiddenByDefault)) |
| bFreezeIncomingPoseOnStart | `uint8` | UPROPERTY(EditAnywhere, Category = Settings Not Support Feature for Depends on Chaos) |
| bClampLinearTranslationLimitToRefPose | `uint8` |  |
| WorldSpaceMinimumScale | `float` |  |
| EvaluationResetTime | `float` |  |
| bComponentSpaceSimulation_DEPRECATED | `bool` |  |

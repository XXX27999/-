# FAnimNode_AnimDynamics_UE5

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LinearDampingOverride | `float` | Overridden linear damping value. The default is 0.7. Values below 0.7 won't have an effect. |
| AngularDampingOverride | `float` | Overridden angular damping value. The default is 0.7. Values below 0.7 won't have an effect. |
| RelativeSpaceBone | `FBoneReference` | When in BoneRelative sim space, the simulation will use this bone as the origin |
| BoundBone | `FBoneReference` | The bone to attach the physics body to, if bChain is true this is the top of the chain |
| ChainEnd | `FBoneReference` | If bChain is true this is the bottom of the chain, otherwise ignored |
| PhysicsBodyDefinitions | `TArray < FAnimPhysBodyDefinition_UE5 >` |  |
| GravityScale | `float` | Scale for gravity, higher values increase forces due to gravity |
| GravityOverride | [FVector](../FV/FVector.md) | Gravity Override Value |
| LinearSpringConstant | `float` | Spring constant to use when calculating linear springs, higher values mean a stronger spring.<br>	  You need to enable the Linear Spring checkbox for this to have an effect. |
| AngularSpringConstant | `float` | Spring constant to use when calculating angular springs, higher values mean a stronger spring.<br>	  You need to enable the Angular Spring checkbox for this to have an effect.<br>	  Note: Make sure to also set the Angular Target Axis and Angular Target in the Constraint Setup for this to have an effect. |
| WindScale | `float` | Scale to apply to calculated wind velocities in the solver |
| ComponentLinearAccScale | [FVector](../FV/FVector.md) | When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation. |
| ComponentLinearVelScale | [FVector](../FV/FVector.md) | When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity. |
| ComponentAppliedLinearAccClamp | [FVector](../FV/FVector.md) | When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large. |
| AngularBiasOverride | `float` | Overridden angular bias value<br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	  in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	  the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| NumSolverIterationsPreUpdate | `int32` | Number of update passes on the linear and angular limits before we solve the position of the bodies recommended to be four times the value of NumSolverIterationsPostUpdate |
| NumSolverIterationsPostUpdate | `int32` | Number of update passes on the linear and angular limits after we solve the position of the bodies, recommended to be around a quarter of NumSolverIterationsPreUpdate |
| SphericalLimits | `TArray < FAnimPhysSphericalLimit_UE5 >` | List of available spherical limits for this node |
| ExternalForce | [FVector](../FV/FVector.md) | An external force to apply to all bodies in the simulation when ticked, specified in world space |
| PlanarLimits | `TArray < FAnimPhysPlanarLimit_UE5 >` | List of available planar limits for this node |
| SimulationSpace | [AnimPhysSimSpaceType_UE5](../../../cppenum/A/AN/AnimPhysSimSpaceType_UE5.md) | The space used to run the simulation |
| bUseSphericalLimits | `uint8` | Whether to evaluate spherical limits |
| bUsePlanarLimit | `uint8` | Whether to evaluate planar limits |
| bDoUpdate | `uint8` | If true we will perform physics update, otherwise skip - allows visualization of the initial state of the bodies |
| bDoEval | `uint8` | If true we will perform bone transform evaluation, otherwise skip - allows visualization of the initial anim state compared to the physics sim |
| bOverrideLinearDamping | `uint8` | If true, the override value will be used for linear damping |
| bOverrideAngularBias | `uint8` | If true, the override value will be used for the angular bias for bodies in this node.<br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	   in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	   the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| bOverrideAngularDamping | `uint8` | If true, the override value will be used for angular damping |
| bEnableWind | `uint8` | Whether or not wind is enabled for the bodies in this simulation |
| bUseGravityOverride | `uint8` | Use gravity override value vs gravity scale |
| bGravityOverrideInSimSpace | `uint8` | If true the gravity override value is defined in simulation space, by default it is in world space |
| bLinearSpring | `uint8` | If true the body will attempt to spring back to its initial position |
| bAngularSpring | `uint8` | If true the body will attempt to align itself with the specified angular target |
| bChain | `uint8` | Set to true to use the solver to simulate a connected chain |
| BoxExtents_DEPRECATED | [FVector](../FV/FVector.md) |  |
| LocalJointOffset_DEPRECATED | [FVector](../FV/FVector.md) |  |
| ConstraintSetup_DEPRECATED | [FAnimPhysConstraintSetup_UE5](./FAnimPhysConstraintSetup_UE5.md) |  |
| CollisionType_DEPRECATED | [AnimPhysCollisionType](../../../cppenum/A/AN/AnimPhysCollisionType.md) |  |
| SphereCollisionRadius_DEPRECATED | `float` |  |

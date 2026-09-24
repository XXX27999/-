# FAnimNode_AnimDynamics

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bUseLazyChange | `bool` |  |
| LazyChangeInterval | `float` |  |
| LazyChangeCurve | `UCurveFloat *` |  |
| bLazySimulate_Location | `bool` |  |
| bLazySimulate_Location_OnlyRoot | `bool` |  |
| LazySimulateAlpha_Location | `float` |  |
| bLazySimulate_Rotation | `bool` |  |
| bLazySimulate_Rotation_OnlyRoot | `bool` |  |
| LazySimulateAlpha_Rotation | `float` |  |
| SimulationSpace | [AnimPhysSimSpaceType](../../../cppenum/A/AN/AnimPhysSimSpaceType.md) | The space used to run the simulation |
| RelativeSpaceBone | `FBoneReference` | When in BoneRelative sim space, the simulation will use this bone as the origin |
| bChain | `bool` | Set to true to use the solver to simulate a connected chain |
| BoundBone | `FBoneReference` | The bone to attach the physics body to, if bChain is true this is the top of the chain |
| ChainEnd | `FBoneReference` | If bChain is true this is the bottom of the chain, otherwise ignored |
| BoxExtents | [FVector](../FV/FVector.md) | Extents of the box to use for simulation |
| LocalJointOffset | [FVector](../FV/FVector.md) | Vector relative to the body being simulated to attach the constraint to |
| OldLocalJointOffset | [FVector](../FV/FVector.md) |  |
| GravityScale | `float` | Scale for gravity, higher values increase forces due to gravity |
| bLinearSpring | `bool` | If true the body will attempt to spring back to its initial position |
| bAngularSpring | `bool` | If true the body will attempt to align itself with the specified angular target |
| LinearSpringConstant | `float` | Spring constant to use when calculating linear springs, higher values mean a stronger spring. |
| AngularSpringConstant | `float` | Spring constant to use when calculating angular springs, higher values mean a stronger spring |
| bEnableWind | `bool` | Whether or not wind is enabled for the bodies in this simulation |
| bWindWasEnabled | `bool` |  |
| WindScale | `float` | Scale to apply to calculated wind velocities in the solver |
| bOverrideLinearDamping | `bool` | If true, the override value will be used for linear damping |
| LinearDampingOverride | `float` | Overridden linear damping value |
| bOverrideAngularDamping | `bool` | If true, the override value will be used for angular damping |
| AngularDampingOverride | `float` | Overridden angular damping value |
| bOverrideAngularBias | `bool` | If true, the override value will be used for the angular bias for bodies in this node.<br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	   in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	   the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| AngularBiasOverride | `float` | Overridden angular bias value<br>	   Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability<br>	   in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with<br>	   the mesh, if that's the case override this and push it towards 1.0f until it settles correctly |
| bDoUpdate | `bool` | If true we will perform physics update, otherwise skip - allows visualisation of the initial state of the bodies |
| bDoEval | `bool` | If true we will perform bone transform evaluation, otherwise skip - allows visualisation of the initial anim state compared to the physics sim |
| NumSolverIterationsPreUpdate | `int32` | Number of update passes on the linear and angular limits before we solve the position of the bodies recommended to be four times the value of NumSolverIterationsPostUpdate |
| NumSolverIterationsPostUpdate | `int32` | Number of update passes on the linear and angular limits after we solve the position of the bodies, recommended to be around a quarter of NumSolverIterationsPreUpdate |
| ConstraintSetup | [FAnimPhysConstraintSetup](./FAnimPhysConstraintSetup.md) | Data describing the constraints we will apply to the body |
| bUseDynamicAngularLimits | `bool` | if set, will use Dynamic_AngularLimits as ConstraintSetup.AngularLimits when UpdateLimits |
| Dynamic_AngularLimitsMin | [FVector](../FV/FVector.md) | if bUseDynamicAngularLimits set, will use Dynamic_AngularLimitsMin as ConstraintSetup.AngularLimitsMin when UpdateLimits |
| Dynamic_AngularLimitsMax | [FVector](../FV/FVector.md) | if bUseDynamicAngularLimits set, will use Dynamic_AngularLimitsMax as ConstraintSetup.AngularLimitsMax when UpdateLimits |
| bUsePlanarLimit | `bool` | Whether to evaluate planar limits |
| PlanarLimits | `TArray < FAnimPhysPlanarLimit >` | List of available planar limits for this node |
| bUseSphericalLimits | `bool` | Whether to evaluate spherical limits |
| SphericalLimits | `TArray < FAnimPhysSphericalLimit >` | List of available spherical limits for this node |
| CollisionType | [AnimPhysCollisionType](../../../cppenum/A/AN/AnimPhysCollisionType.md) | Resolution method for planar limits |
| SphereCollisionRadius | `float` | Radius to use if CollisionType is set to CustomSphere |
| NonEvaluateFrameNum | `int32` | Non Evaluate frame from start |
| ExternalForce | [FVector](../FV/FVector.md) | An external force to apply to all bodies in the simulation when ticked, specified in world space |
| BoneShiftTolerenceChecker | [FAnimNodeBoneShiftTolerenceChecker](./FAnimNodeBoneShiftTolerenceChecker.md) | Bone Shift Tolerence Check Start |

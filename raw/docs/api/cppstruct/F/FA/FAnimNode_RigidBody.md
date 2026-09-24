# FAnimNode_RigidBody

Controller that simulates physics based on the physics asset of the skeletal mesh component

## Fields

| Name | Type | Description |
| --- | --- | --- |
| OverridePhysicsAsset | `UPhysicsAsset *` | Physics asset to use. If empty use the skeletal mesh's default physics asset |
| LastUsePhysicsAsset | `TWeakObjectPtr < UPhysicsAsset >` |  |
| OverrideWorldGravity | [FVector](../FV/FVector.md) | Override gravity |
| ExternalForce | [FVector](../FV/FVector.md) | Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example |
| OverlapChannel | `TEnumAsByte < ECollisionChannel >` | The channel we use to find static geometry to collide with |
| bEnableWorldGeometry | `bool` |  |
| SimulationSpace | [ESimulationSpace](../../../cppenum/E/ES/ESimulationSpace.md) | What space to simulate the bodies in. This affects how velocities are generated |
| bOverrideWorldGravity | `bool` |  |
| CachedBoundsScale | `float` | Scale of cached bounds (vs. actual bounds).<br>	  Increasing this may improve performance, but overlaps may not work as well.<br>	  (A value of 1.0 effectively disables cached bounds). |
| bUseCompPhysicsAssetWhenNotSet | `bool` |  |
| bUseIntersectDetect | `bool` |  |
| bUseMultipleRigidBodyNodeInitDelay | `bool` |  |
| bComponentSpaceSimulation_DEPRECATED | `bool` |  |
| BoneShiftTolerenceChecker | [FAnimNodeBoneShiftTolerenceChecker](./FAnimNodeBoneShiftTolerenceChecker.md) | Bone Shift Tolerence Check Start |

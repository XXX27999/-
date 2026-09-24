# FClothConfig

Holds initial, asset level config for clothing actors.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| WindMethod | [EClothingWindMethod](../../../cppenum/E/EC/EClothingWindMethod.md) |  |
| VerticalConstraintConfig | [FClothConstraintSetup](./FClothConstraintSetup.md) |  |
| HorizontalConstraintConfig | [FClothConstraintSetup](./FClothConstraintSetup.md) |  |
| BendConstraintConfig | [FClothConstraintSetup](./FClothConstraintSetup.md) |  |
| ShearConstraintConfig | [FClothConstraintSetup](./FClothConstraintSetup.md) |  |
| SelfCollisionRadius | `float` |  |
| SelfCollisionStiffness | `float` |  |
| SelfCollisionCullScale | `float` | Scale to use for the radius of the culling checks for self collisions.<br>	  Any other self collision body within the radius of this check will be culled.<br>	  This helps performance with higher resolution meshes by reducing the number<br>	  of colliding bodies within the cloth. Reducing this will have a negative<br>	  effect on performance! |
| Damping | [FVector](../FV/FVector.md) |  |
| Friction | `float` |  |
| WindDragCoefficient | `float` |  |
| WindLiftCoefficient | `float` |  |
| LinearDrag | [FVector](../FV/FVector.md) |  |
| AngularDrag | [FVector](../FV/FVector.md) |  |
| LinearInertiaScale | [FVector](../FV/FVector.md) |  |
| AngularInertiaScale | [FVector](../FV/FVector.md) |  |
| CentrifugalInertiaScale | [FVector](../FV/FVector.md) |  |
| SolverFrequency | `float` |  |
| StiffnessFrequency | `float` |  |
| GravityScale | `float` |  |
| TetherStiffness | `float` |  |
| TetherLimit | `float` |  |
| CollisionThickness | `float` |  |

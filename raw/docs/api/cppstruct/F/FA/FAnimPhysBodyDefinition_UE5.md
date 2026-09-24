# FAnimPhysBodyDefinition_UE5

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BoundBone | `FBoneReference` |  |
| BoxExtents | [FVector](../FV/FVector.md) | Extents of the box to use for simulation |
| LocalJointOffset | [FVector](../FV/FVector.md) | Vector relative to the body being simulated to attach the constraint to |
| ConstraintSetup | [FAnimPhysConstraintSetup_UE5](./FAnimPhysConstraintSetup_UE5.md) | Data describing the constraints we will apply to the body |
| CollisionType | [AnimPhysCollisionType](../../../cppenum/A/AN/AnimPhysCollisionType.md) | Resolution method for planar limits |
| SphereCollisionRadius | `float` | Radius to use if CollisionType is set to CustomSphere |

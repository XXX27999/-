# FAnimPhysSphericalLimit_UE5

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DrivingBone | `FBoneReference` | Bone to attach the sphere to |
| SphereLocalOffset | [FVector](../FV/FVector.md) | Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space |
| LimitRadius | `float` | Radius of the sphere |
| LimitType | [ESphericalLimitType_UE5](../../../cppenum/E/ES/ESphericalLimitType_UE5.md) | Whether to lock bodies inside or outside of the sphere |

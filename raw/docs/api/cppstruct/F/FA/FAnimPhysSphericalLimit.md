# FAnimPhysSphericalLimit

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DrivingBone | `FBoneReference` | Bone to attach the sphere to |
| SphereLocalOffset | [FVector](../FV/FVector.md) | Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space |
| LimitRadius | `float` | Radius of the sphere |
| LimitType | [ESphericalLimitType](../../../cppenum/E/ES/ESphericalLimitType.md) | Whether to lock bodies inside or outside of the sphere |
| IsEnabled | `bool` |  |

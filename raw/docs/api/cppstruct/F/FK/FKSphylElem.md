# FKSphylElem

Capsule shape used for collision. Z axis is capsule axis.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TM_DEPRECATED | [FMatrix](../FM/FMatrix.md) |  |
| Orientation_DEPRECATED | [FQuat](../FQ/FQuat.md) |  |
| Center | [FVector](../FV/FVector.md) | Position of the capsule's origin |
| Rotation | [FRotator](../FR/FRotator.md) | Rotation of the capsule |
| Radius | `float` | Radius of the capsule |
| Length | `float` | This is of line-segment ie. add Radius to both ends to find total length. |

# FAnimPhysPlanarLimit_UE5

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DrivingBone | `FBoneReference` | When using a driving bone, the plane transform will be relative to the bone transform |
| PlaneTransform | [FTransform](../FT/FTransform.md) | Transform of the plane, this is either in component-space if no DrivinBone is specified<br>	   or in bone-space if a driving bone is present. |

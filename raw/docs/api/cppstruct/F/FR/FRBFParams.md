# FRBFParams

Parameters used by RBF solver

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TargetDimensions | `int32` | How many dimensions input data has |
| Radius | `float` | Default radius for each target, scaled by per-Target ScaleFactor |
| Function | [ERBFFunctionType](../../../cppenum/E/ER/ERBFFunctionType.md) |  |
| DistanceMethod | [ERBFDistanceMethod](../../../cppenum/E/ER/ERBFDistanceMethod.md) |  |
| TwistAxis | `TEnumAsByte < EBoneAxis >` | Axis to use when DistanceMethod is SwingAngle |
| WeightThreshold | `float` | Weight below which we shouldn't bother returning a contribution from a target |

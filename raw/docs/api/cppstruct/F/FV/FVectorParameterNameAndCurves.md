# FVectorParameterNameAndCurves

Structure representing an animated vector parameter and it's associated animation curve.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` | The name of the vector parameter which is being animated. |
| Index | `int32` |  |
| XCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the x component of the vector parameter. |
| YCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the y component of the vector parameter. |
| ZCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the z component of the vector parameter. |

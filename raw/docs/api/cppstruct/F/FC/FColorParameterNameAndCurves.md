# FColorParameterNameAndCurves

Structure representing an animated vector parameter and it's associated animation curve.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` | The name of the vector parameter which is being animated. |
| Index | `int32` |  |
| RedCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the red component of the color parameter. |
| GreenCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the green component of the color parameter. |
| BlueCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the blue component of the color parameter. |
| AlphaCurve | [FRichCurve](../FR/FRichCurve.md) | The curve which contains the animation data for the alpha component of the color parameter. |

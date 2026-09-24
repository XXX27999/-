# FRichCurveKey

One key in a rich, editable float curve

## Fields

| Name | Type | Description |
| --- | --- | --- |
| InterpMode | `TEnumAsByte < ERichCurveInterpMode >` | Interpolation mode between this key and the next |
| TangentMode | `TEnumAsByte < ERichCurveTangentMode >` | Mode for tangents at this key |
| TangentWeightMode | `TEnumAsByte < ERichCurveTangentWeightMode >` | If either tangent at this key is 'weighted' |
| Time | `float` | Time at this key |
| Value | `float` | Value at this key |
| ArriveTangent | `float` | If RCIM_Cubic, the arriving tangent at this key |
| ArriveTangentWeight | `float` | If RCTWM_WeightedArrive or RCTWM_WeightedBoth, the weight of the left tangent |
| LeaveTangent | `float` | If RCIM_Cubic, the leaving tangent at this key |
| LeaveTangentWeight | `float` | If RCTWM_WeightedLeave or RCTWM_WeightedBoth, the weight of the right tangent |

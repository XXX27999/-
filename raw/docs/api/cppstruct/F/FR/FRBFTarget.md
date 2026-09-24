# FRBFTarget

Data about a particular target in the RBF, including scaling factor

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ScaleFactor | `float` | How large to scale |
| bApplyCustomCurve | `bool` | Whether we want to apply an additional custom curve when activating this target |
| CustomCurve | [FRichCurve](./FRichCurve.md) | Custom curve to apply to activation of this target, if bApplyCustomCurve is true |

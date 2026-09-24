# FLayerBlendInput

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LayerName | `FName` |  |
| BlendType | `TEnumAsByte < ELandscapeLayerBlendType >` |  |
| LayerInput | [FExpressionInput](../FE/FExpressionInput.md) |  |
| HeightInput | [FExpressionInput](../FE/FExpressionInput.md) |  |
| PreviewWeight | `float` |  |
| ConstLayerInput | [FVector](../FV/FVector.md) | only used if LayerInput is not hooked up |
| ConstHeightInput | `float` | only used if HeightInput is not hooked up |

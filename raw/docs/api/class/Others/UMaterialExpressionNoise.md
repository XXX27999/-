# UMaterialExpressionNoise

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Position | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | 2 to 3 dimensional vector |
| FilterWidth | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | scalar, to clamp the Levels at pixel level, can be computed like this: max(length(ddx(Position)), length(ddy(Position)) |
| Scale | `float` | can also be done with a multiply on the Position |
| Quality | `int32` | Lower numbers are faster and lower quality, higher numbers are slower and higher quality |
| NoiseFunction | `TEnumAsByte < enum ENoiseFunction >` | Noise function, affects performance and look |
| bTurbulence | `uint32` | How multiple frequencies are getting combined |
| Levels | `int32` | 1 = fast but little detail, .. larger numbers cost more performance |
| OutputMin | `float` |  |
| OutputMax | `float` |  |
| LevelScale | `float` | usually 2 but higher values allow efficient use of few levels |
| bTiling | `uint32` | Whether to use tiling noise pattern, useful for baking to seam-free repeating textures |
| RepeatSize | `uint32` | How many units in each tile (if Tiling is on) |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UMaterialExpressionVectorNoise

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Position | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | 2 to 3 dimensional vector |
| NoiseFunction | `TEnumAsByte < enum EVectorNoiseFunction >` | Noise function, affects performance and look |
| Quality | `int32` | For noise functions where applicable, lower numbers are faster and lower quality, higher numbers are slower and higher quality |
| bTiling | `uint32` | Whether tile the noise pattern, useful for baking to seam-free repeating textures |
| TileSize | `uint32` | How many units in each tile (if Tiling is on)<br>	   For Perlin noise functions, Tile Size must be a multiple of three |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UMaterialExpressionSceneDepthWithoutWater

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InputMode | `TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type >` | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |
| Input | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or<br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |
| ConstInput | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | only used if Input is not hooked up |
| FallbackDepth | `float` | Depth to fall back to in case the needed texture isn't available on a particular platform or configuration |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

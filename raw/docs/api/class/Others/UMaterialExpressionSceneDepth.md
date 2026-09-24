# UMaterialExpressionSceneDepth

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InputMode | `TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type >` | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |
| Input | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or<br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |
| Coordinates_DEPRECATED | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| ConstInput | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | only used if Input is not hooked up |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

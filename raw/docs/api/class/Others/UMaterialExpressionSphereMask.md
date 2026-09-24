# UMaterialExpressionSphereMask

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| A | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | 1 to 4 dimensional vector, should be the same type as B |
| B | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | 1 to 4 dimensional vector, should be the same type as A |
| Radius | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | in the units that A and B are measured, if not hooked up the internal constant is used |
| Hardness | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | 0..1 for the range of 0\% to 100\%, if not hooked up the internal constant is used |
| AttenuationRadius | `float` | in the unit that A and B are measured |
| HardnessPercent | `float` | in percent 0%=soft .. 100%=hard |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

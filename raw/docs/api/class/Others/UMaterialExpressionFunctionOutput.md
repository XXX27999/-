# UMaterialExpressionFunctionOutput

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OutputName | `FString` | The output's name, which will be drawn on the connector in function call expressions that use this function. |
| Description | `FString` | The output's description, which will be used as a tooltip on the connector in function call expressions that use this function. |
| SortPriority | `int32` | Controls where the output is displayed relative to the other outputs. |
| A | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Stores the expression in the material function connected to this output. |
| bLastPreviewed | `uint32` | Whether this output was previewed the last time this function was edited. |
| Id | [FGuid](../../cppstruct/F/FG/FGuid.md) | Id of this input, used to maintain references through name changes. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

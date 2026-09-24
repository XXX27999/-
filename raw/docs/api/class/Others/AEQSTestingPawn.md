# AEQSTestingPawn

this class is abstract even though it's perfectly functional on its own.
 	The reason is to stop it from showing as valid player pawn type when configuring
 	project's game mode.

## Parents

- [ACharacter](./ACharacter.md)
- IEQSQueryResultSourceInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| QueryTemplate | `UEnvQuery *` |  |
| QueryParams | `TArray < FEnvNamedValue >` | optional parameters for query |
| QueryConfig | `TArray < FAIDynamicParam >` |  |
| TimeLimitPerStep | `float` |  |
| StepToDebugDraw | `int32` |  |
| HighlightMode | [EEnvQueryHightlightMode](../../cppenum/E/EE/EEnvQueryHightlightMode.md) |  |
| bDrawLabels | `uint32` |  |
| bDrawFailedItems | `uint32` |  |
| bReRunQueryOnlyOnFinishedMove | `uint32` |  |
| bShouldBeVisibleInGame | `uint32` |  |
| bTickDuringGame | `uint32` |  |
| QueryingMode | `TEnumAsByte < EEnvQueryRunMode :: Type >` |  |
| EdRenderComp | `UEQSRenderingComponent *` | Editor Preview |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

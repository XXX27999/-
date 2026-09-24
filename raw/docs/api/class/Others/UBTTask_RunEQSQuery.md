# UBTTask_RunEQSQuery

Run Environment Query System Query task node.
  Runs the specified environment query when executed.

## Parents

- [UBTTask_BlackboardBase](./UBTTask_BlackboardBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| QueryTemplate | `UEnvQuery *` | query to run |
| QueryParams | `TArray < FEnvNamedValue >` | optional parameters for query |
| QueryConfig | `TArray < FAIDynamicParam >` |  |
| RunMode | `TEnumAsByte < EEnvQueryRunMode :: Type >` | determines which item will be stored (All = only first matching) |
| EQSQueryBlackboardKey | `FBlackboardKeySelector` | blackboard key storing an EQS query template |
| bUseBBKey | `bool` |  |
| EQSRequest | `FEQSParametrizedQueryExecutionRequest` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

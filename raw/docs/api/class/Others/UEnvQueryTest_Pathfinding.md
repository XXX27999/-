# UEnvQueryTest_Pathfinding

## Parents

- [UEnvQueryTest](./UEnvQueryTest.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TestMode | `TEnumAsByte < EEnvTestPathfinding :: Type >` | testing mode |
| Context | `TSubclassOf < UEnvQueryContext >` | context: other end of pathfinding test |
| PathFromContext | [FAIDataProviderBoolValue](../../cppstruct/F/FA/FAIDataProviderBoolValue.md) | pathfinding direction |
| SkipUnreachable | [FAIDataProviderBoolValue](../../cppstruct/F/FA/FAIDataProviderBoolValue.md) | if set, items with failed path will be invalidated (PathCost, PathLength) |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` | navigation filter to use in pathfinding |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

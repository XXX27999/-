# UEnvQueryGenerator_ActorsOfClass

## Parents

- [UEnvQueryGenerator](./UEnvQueryGenerator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SearchedActorClass | `TSubclassOf < AActor >` |  |
| GenerateOnlyActorsInRadius | [FAIDataProviderBoolValue](../../cppstruct/F/FA/FAIDataProviderBoolValue.md) | If true, this will only returns actors of the specified class within the SearchRadius of the SearchCenter context.  If false, it will return ALL actors of the specified class in the world. |
| SearchRadius | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Max distance of path between point and context.  NOTE: Zero and negative values will never return any results if<br>	   UseRadius is true.  "Within" requires Distance < Radius.  Actors ON the circle (Distance == Radius) are excluded. |
| SearchCenter | `TSubclassOf < UEnvQueryContext >` | context |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

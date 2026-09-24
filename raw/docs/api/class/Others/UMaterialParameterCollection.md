# UMaterialParameterCollection

Asset class that contains a list of parameter names and their default values.
  Any number of materials can reference these parameters and get new values when the parameter values are changed.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StateId | [FGuid](../../cppstruct/F/FG/FGuid.md) | Used by materials using this collection to know when to recompile. |
| ScalarParameters | `TArray < FCollectionScalarParameter >` |  |
| VectorParameters | `TArray < FCollectionVectorParameter >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UEnvQueryGenerator_Composite

Composite generator allows using multiple generators in single query option
  All child generators must produce exactly the same item type!

## Parents

- [UEnvQueryGenerator](./UEnvQueryGenerator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Generators | `TArray < UEnvQueryGenerator * >` |  |
| bAllowDifferentItemTypes | `uint32` | allow generators with different item types, use at own risk!<br><br>	   WARNING:<br>	   generator will use ForcedItemType for raw data, you MUST ensure proper memory layout<br>	   child generators will be writing to memory block through their own item types:<br>	   - data must fit info block allocated by ForcedItemType<br>	   - tests will read item locationproperties through ForcedItemType |
| bHasMatchingItemType | `uint32` |  |
| ForcedItemType | `TSubclassOf < UEnvQueryItemType >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UEnvQueryGenerator_BlueprintBase

## Parents

- [UEnvQueryGenerator](./UEnvQueryGenerator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| GeneratorsActionDescription | `FText` | A short description of what test does, like "Generate pawn named Joe" |
| Context | `TSubclassOf < UEnvQueryContext >` | context |
| GeneratedItemType | `TSubclassOf < UEnvQueryItemType >` | @todo this should show up only in the generator's BP, but<br>	 	due to the way EQS editor is generating widgets it's there as well<br>	 	It's a bug and we'll fix it |

## Functions

### DoItemGeneration

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ContextLocations | `TArray < FVector > &` |  |

**Return**

- Type: 
- Description: _None_

### AddGeneratedVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GeneratedVector | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### AddGeneratedActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GeneratedActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetQuerier

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

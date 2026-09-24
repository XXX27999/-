# UMovieSceneBindingOverrides

A one-to-many definition of movie scene object binding IDs to overridden objects that should be bound to that binding.

## Parents

- [UObject](./UObject.md)
- IMovieSceneBindingOverridesInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BindingData | `TArray < FMovieSceneBindingOverrideData >` | The actual binding data |

## Functions

### GetBindingData

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MakeBindingID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBindingID | `FGuid &` |  |
| InSequenceID | `FMovieSceneSequenceID` |  |
| InSpace | [EMovieSceneObjectBindingSpace](../../cppenum/E/EM/EMovieSceneObjectBindingSpace.md) |  |

**Return**

- Type: 
- Description: _None_

### GetGuidStr

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BindingID | `FMovieSceneObjectBindingID &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

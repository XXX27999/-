# UAIPerceptionStimuliSourceComponent

Gives owning actor a way to auto-register as perception system's sense stimuli source

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bAutoRegisterAsSource | `uint32` |  |
| RegisterAsSourceForSenses | `TArray < TSubclassOf < UAISense > >` |  |

## Functions

### RegisterWithPerceptionSystem

Registers owning actor as source of stimuli for senses specified in RegisterAsSourceForSenses.
	 	Note that you don't have to do it if bAutoRegisterAsSource == true

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RegisterForSense

Registers owning actor as source for specified sense class

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenseClass | `TSubclassOf < UAISense >` |  |

**Return**

- Type: 
- Description: _None_

### UnregisterFromPerceptionSystem

Unregister owning actor from being a source of sense stimuli

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UnregisterFromSense

Unregisters owning actor from sources list of a specified sense class

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenseClass | `TSubclassOf < UAISense >` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

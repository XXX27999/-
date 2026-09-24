# UAIPerceptionSystem

By design checks perception between hostile teams

## Parents

- [UObject](./UObject.md)
- FTickableGameObject

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Senses | `TArray < UAISense * >` |  |
| PerceptionAgingRate | `float` |  |

## Functions

### ReportEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PerceptionEvent | `UAISenseEvent *` |  |

**Return**

- Type: 
- Description: _None_

### ReportPerceptionEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PerceptionEvent | `UAISenseEvent *` |  |

**Return**

- Type: 
- Description: _None_

### RegisterPerceptionStimuliSource

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Sense | `TSubclassOf < UAISense >` |  |
| Target | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetSenseClassForStimulus

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Stimulus | `FAIStimulus &` |  |

**Return**

- Type: 
- Description: _None_

### OnPerceptionStimuliSourceEndPlay

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| EndPlayReason | `EEndPlayReason :: Type` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UAISense_Blueprint

## Parents

- [UAISense](./UAISense.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ListenerDataType | `TSubclassOf < UUserDefinedStruct >` |  |
| ListenerContainer | `TArray < UAIPerceptionComponent * >` |  |
| UnprocessedEvents | `TArray < UAISenseEvent * >` |  |

## Functions

### OnUpdate

returns requested amount of time to pass until next frame.
	 	Return 0 to get update every frame (WARNING: hits performance)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EventsToProcess | `TArray < UAISenseEvent * > &` |  |

**Return**

- Type: 
- Description: _None_

### OnListenerRegistered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActorListener | `AActor *` |  |
| PerceptionComponent | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Return**

- Type: 
- Description: _None_

### OnListenerUpdated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActorListener | `AActor *` |  |
| PerceptionComponent | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Return**

- Type: 
- Description: _None_

### OnListenerUnregistered

called when a listener unregistered from this sense. Most often this is called due to actor's death

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActorListener | `AActor *` |  |
| PerceptionComponent | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Return**

- Type: 
- Description: _None_

### GetAllListenerActors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListenerActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetAllListenerComponents

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ListenerComponents | `TArray < UAIPerceptionComponent * > &` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnNewPawn

called when sense's instance gets notified about new pawn that has just been spawned

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

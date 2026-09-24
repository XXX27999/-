# UAIPerceptionComponent

AIPerceptionComponent is used to register as stimuli listener in AIPerceptionSystem
 	and gathers registered stimuli. UpdatePerception is called when component gets new stimuli (batched)

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SensesConfig | `TArray < UAISenseConfig * >` |  |
| DominantSense | `TSubclassOf < UAISense >` | Indicated sense that takes precedence over other senses when determining sensed actor's location.<br>	 	Should be set to one of the senses configured in SensesConfig, or None. |
| AIOwner | `AAIController *` |  |

## Functions

### OnOwnerEndPlay

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| EndPlayReason | `EEndPlayReason :: Type` |  |

**Return**

- Type: 
- Description: _None_

### RequestStimuliListenerUpdate

Notifies AIPerceptionSystem to update properties for this "stimuli listener"

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPerceivedHostileActors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentlyPerceivedActors

If SenseToUse is none all actors currently perceived in any way will get fetched

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenseToUse | `TSubclassOf < UAISense >` |  |
| OutActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetKnownPerceivedActors

If SenseToUse is none all actors ever perceived in any way (and not forgotten yet) will get fetched

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenseToUse | `TSubclassOf < UAISense >` |  |
| OutActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetPerceivedActors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenseToUse | `TSubclassOf < UAISense >` |  |
| OutActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetActorsPerception

Retrieves whatever has been sensed about given actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |
| Info | `FActorPerceptionBlueprintInfo &` |  |

**Return**

- Type: 
- Description: _None_

### SetSenseEnabled

Note that this works only if given sense has been already configured for
	 	this component instance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenseClass | `TSubclassOf < UAISense >` |  |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnPerceptionUpdated |  |  |
| OnTargetPerceptionUpdated |  |  |

## Language

cpp

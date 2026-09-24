# UGameplayTasksComponent

The core ActorComponent for interfacing with the GameplayAbilities System

## Parents

- [UActorComponent](./UActorComponent.md)
- IGameplayTaskOwnerInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SimulatedTasks | `TArray < UGameplayTask * >` | Tasks that run on simulated proxies |
| AutonomousTasks | `TArray < UGameplayTask * >` |  |
| TaskPriorityQueue | `TArray < UGameplayTask * >` |  |
| TickingTasks | `TArray < UGameplayTask * >` | Array of currently active UGameplayTask that require ticking |
| KnownTasks | `TArray < UGameplayTask * >` | All known tasks (processed by this component) referenced for GC |

## Functions

### OnRep_SimulatedTasks

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_AutonomousTasks

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_RunGameplayTask

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskOwner | `TScriptInterface < IGameplayTaskOwnerInterface >` |  |
| Task | `UGameplayTask *` |  |
| Priority | `uint8` |  |
| AdditionalRequiredResources | `TArray < TSubclassOf < UGameplayTaskResource > >` |  |
| AdditionalClaimedResources | `TArray < TSubclassOf < UGameplayTaskResource > >` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnClaimedResourcesChange |  |  |

## Language

cpp

# UChildActorComponent

A component that spawns an Actor when registered, and destroys it when unregistered.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ChildActorClass | `TSubclassOf < AActor >` | The class of Actor to spawn |
| ChildActor | `AActor *` | The actor that we spawned and own |
| bAllowTemplateModification | `bool` |  |
| ChildActorTemplate | `AActor *` | Property to point to the template child actor for details panel purposes |
| IsDestoryChildActor | `bool` |  |
| bKeepChildActorComponet | `bool` |  |
| bEnableReplication | `bool` |  |
| bDumpChildActorLocation | `bool` |  |
| bRedirectComps | `uint8` |  |
| bPCOnlyComps | `uint8` |  |

## Functions

### SetChildActorClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClass | `TSubclassOf < AActor >` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_ChildActor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CreateChildActor

Create the child actor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DestroyChildActor

Kill any currently present child actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNeedInstanceData | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnChildActorRep |  |  |

## Language

cpp

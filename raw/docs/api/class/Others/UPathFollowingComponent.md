# UPathFollowingComponent

## Parents

- [UActorComponent](./UActorComponent.md)
- IAIResourceInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MovementComp | `UNavMovementComponent *` | associated movement component |
| MyNavData | `ANavigationData *` | navigation data for agent described in movement component |

## Functions

### OnActorBump

called when moving agent collides with another actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SelfActor | `AActor *` |  |
| OtherActor | `AActor *` |  |
| NormalImpulse | `FVector` |  |
| Hit | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### GetPathActionType

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPathDestination

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnNavDataRegistered

called when NavigationSystem registers new navigation data type while this component
	 	instance has empty MyNavData. This is usually the case for AI agents hand-placed
	 	on levels.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NavData | `ANavigationData *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

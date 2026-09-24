# UAIBlueprintHelperLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### CreateMoveToProxyObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Pawn | `APawn *` |  |
| Destination | `FVector` |  |
| TargetActor | `AActor *` |  |
| AcceptanceRadius | `float` |  |
| bStopOnOverlap | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SendAIMessage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `APawn *` |  |
| Message | `FName` |  |
| MessageSource | `UObject *` |  |
| bSuccess | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SpawnAIFromClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PawnClass | `TSubclassOf < APawn >` |  |
| BehaviorTree | `UBehaviorTree *` |  |
| Location | `FVector` |  |
| Rotation | `FRotator` |  |
| bNoCollisionFail | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetAIController

The way it works exactly is if the actor passed in is a pawn, then the function retrieves
	 	pawn's controller cast to AIController. Otherwise the function returns actor cast to AIController.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ControlledActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboard

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### LockAIResourcesWithAnimation

locks indicated AI resources of animated pawn

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AnimInstance | `UAnimInstance *` |  |
| bLockMovement | `bool` |  |
| LockAILogic | `bool` |  |

**Return**

- Type: 
- Description: _None_

### UnlockAIResourcesWithAnimation

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AnimInstance | `UAnimInstance *` |  |
| bUnlockMovement | `bool` |  |
| UnlockAILogic | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsValidAILocation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### IsValidAIDirection

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DirectionVector | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### IsValidAIRotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentPath

Returns a copy of navigation path given controller is currently using.
	 	The result being a copy means you won't be able to influence agent's pathfollowing
	 	by manipulating received path

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AController *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

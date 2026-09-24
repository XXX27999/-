# AAIController

AIController is the base class of controllers for AI-controlled Pawns.

  Controllers are non-physical actors that can be attached to a pawn to control its actions.
  AIControllers manage the artificial intelligence for the pawns they control.
  In networked games, they only exist on the server.

## Parents

- [AController](./AController.md)
- IAIPerceptionListenerInterface
- IGameplayTaskOwnerInterface
- IGenericTeamAgentInterface
- IVisualLoggerDebugSnapshotInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bStopAILogicOnUnposses | `uint32` | By default AI's logic gets stopped when controlled Pawn is unpossesed. Setting this flag to false<br>	 	will make AI logic persist past loosing controll over a pawn |
| bSkipExtraLOSChecks | `uint32` | Skip extra line of sight traces to extremities of target being checked. |
| bAllowStrafe | `uint32` | Is strafing allowed during movement? |
| bWantsPlayerState | `uint32` | Specifies if this AI wants its own PlayerState. |
| bSetControlRotationFromPawnOrientation | `uint32` | Copy Pawn rotation to ControlRotation, if there is no focus point. |
| PathFollowingComponent | `UPathFollowingComponent *` | Component used for moving along a path. |
| BrainComponent | `UBrainComponent *` | Component responsible for behaviors. |
| PerceptionComponent | `UAIPerceptionComponent *` |  |
| ActionsComp | `UPawnActionsComponent *` |  |
| Blackboard | `UBlackboardComponent *` | blackboard |
| CachedGameplayTasksComponent | `UGameplayTasksComponent *` |  |
| DefaultNavigationFilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

## Functions

### OnPossess

Event called when PossessedPawn is possessed by this controller.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PossessedPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### OnUnpossess

Gets triggered after given pawn has been unpossesed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UnpossessedPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### MoveToActor

Makes AI go toward specified Goal actor (destination will be continuously updated), aborts any active path following

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Goal | `AActor *` |  |
| AcceptanceRadius | `float` | - finish move if pawn gets close enough |
| bStopOnOverlap | `bool` | - add pawn's radius to AcceptanceRadius |
| bUsePathfinding | `bool` | - use navigation data to calculate path (otherwise it will go in straight line) |
| bCanStrafe | `bool` | - set focus related flag: bAllowStrafe |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |
| bAllowPartialPath | `bool` | - use incomplete path when goal can't be reached |

**Return**

- Type: 
- Description: _None_

### MoveToLocation

Makes AI go toward specified Dest location, aborts any active path following

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Dest | `FVector &` |  |
| AcceptanceRadius | `float` | - finish move if pawn gets close enough |
| bStopOnOverlap | `bool` | - add pawn's radius to AcceptanceRadius |
| bUsePathfinding | `bool` | - use navigation data to calculate path (otherwise it will go in straight line) |
| bProjectDestinationToNavigation | `bool` | - project location on navigation data before using it |
| bCanStrafe | `bool` | - set focus related flag: bAllowStrafe |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |
| bAllowPartialPath | `bool` | - use incomplete path when goal can't be reached |
| bUseNavLink | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetMoveStatus

Returns status of path following

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasPartialPath

Returns true if the current PathFollowingComponent's path is partial (does not reach desired destination).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetImmediateMoveDestination

Returns position of current path segment's end.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMoveBlockDetection

Updates state of movement block detection.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RunBehaviorTree

Starts executing behavior tree.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BTAsset | `UBehaviorTree *` |  |

**Return**

- Type: 
- Description: _None_

### UseBlackboard

Makes AI use the specified Blackboard asset & creates a Blackboard Component if one does not already exist.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BlackboardAsset | `UBlackboardData *` | The Blackboard asset to use. |
| BlackboardComponent | `UBlackboardComponent * &` | The Blackboard component that was used or created to work with the passed-in Blackboard Asset. |

**Return**

- Type: 
- Description: _None_

### ClaimTaskResource

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ResourceClass | `TSubclassOf < UGameplayTaskResource >` |  |

**Return**

- Type: 
- Description: _None_

### UnclaimTaskResource

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ResourceClass | `TSubclassOf < UGameplayTaskResource >` |  |

**Return**

- Type: 
- Description: _None_

### OnUsingBlackBoard

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BlackboardComp | `UBlackboardComponent *` |  |
| BlackboardAsset | `UBlackboardData *` |  |

**Return**

- Type: 
- Description: _None_

### GetFocalPoint

Retrieve the final position that controller should be looking at.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetFocalPointOnActor

Retrieve the focal point this controller should focus to on given actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetFocalPoint

Set the position that controller should be looking at.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FP | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### K2_SetFocus

Set Focus for actor, will set FocalPoint as a result.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewFocus | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetFocusActor

Get the focused actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_ClearFocus

Clears Focus, will also clear FocalPoint as a result

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnGameplayTaskResourcesClaimed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewlyClaimed | `FGameplayResourceSet` |  |
| FreshlyReleased | `FGameplayResourceSet` |  |

**Return**

- Type: 
- Description: _None_

### GetPathFollowingComponent

Returns PathFollowingComponent subobject

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAIPerceptionComponent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| ReceiveMoveCompleted |  | Blueprint notification that we've completed the current movement request |

## Language

cpp

# UPawnAction

Things to remember:
 	 Actions are created paused

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ChildAction | `UPawnAction *` | Current child node executing on top of this Action |
| ParentAction | `UPawnAction *` |  |
| OwnerComponent | `UPawnActionsComponent *` | Extra reference to the component this action is being governed by |
| Instigator | `UObject *` | indicates an object that caused this action. Used for mass removal of actions<br>	 	by specific object |
| BrainComp | `UBrainComponent *` | @Note: THIS IS HERE _ONLY_ BECAUSE OF THE WAY AI MESSAGING IS CURRENTLY IMPLEMENTED. WILL GO AWAY! |
| bAllowNewSameClassInstance | `uint32` | if this is FALSE and we're trying to push a new instance of a given class,<br>	 	but the top of the stack is already an instance of that class ignore the attempted push |
| bReplaceActiveSameClassInstance | `uint32` | if this is TRUE, when we try to push a new instance of an action who has the<br>	 	same class as the action on the top of the stack, pop the one on the stack, and push the new one<br>	 	NOTE: This trumps bAllowNewClassInstance (e.g. if this is true and bAllowNewClassInstance<br>	 	is false the active instance will still be replaced) |
| bShouldPauseMovement | `uint32` | this is a temporary solution to allow having movement action running in background while there's<br>	 	another action on top doing its thing<br>	 	@note should go away once AI resource locking comes on-line |
| bAlwaysNotifyOnFinished | `uint32` | if set, action will call OnFinished notify even when ending as FailedToStart |

## Functions

### GetActionPriority

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CreateActionInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ActionClass | `TSubclassOf < UPawnAction >` |  |

**Return**

- Type: 
- Description: _None_

### Finish

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WithResult | `TEnumAsByte < EPawnActionResult :: Type >` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

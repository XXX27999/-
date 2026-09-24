# AController

Controllers are non-physical actors that can possess a Pawn to control
  its actions.  PlayerControllers are used by human players to control pawns, while
  AIControllers implement the artificial intelligence for the pawns they control.
  Controllers take control of a pawn using their Possess() method, and relinquish
  control of the pawn by calling UnPossess().

  Controllers receive notifications for many of the events occurring for the Pawn they
  are controlling.  This gives the controller the opportunity to implement the behavior
  in response to this event, intercepting the event and superseding the Pawn's default
  behavior.

  ControlRotation (accessed via GetControlRotation()), determines the viewingaiming
  direction of the controlled Pawn and is affected by input such as from a mouse or gamepad.

## Parents

- [AActor](./AActor.md)
- INavAgentInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Pawn | `APawn *` | Pawn currently being controlled by this controller.  Use Pawn.Possess() to take control of a pawn |
| Character | `ACharacter *` | Character currently being controlled by this controller.  Value is same as Pawn if the controlled pawn is a character, otherwise NULL |
| PlayerState | `APlayerState *` | PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs). |
| IgnoreMoveInputChnage | `FString` | ShadowVar.  Use for debug |
| IgnoreLookInputChnage | `FString` | ShadowVar.  Use for debug |
| TransformComponent | `USceneComponent *` | Component to give controllers a transform and enable attachment if desired. |
| ControlRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | The control rotation of the Controller. See GetControlRotation. |
| bAttachToPawn | `uint32` | If true, the controller location will match the possessed Pawn's location. If false, it will not be updated. Rotation will match ControlRotation in either case.<br>	  Since a Controller's location is normally inaccessible, this is intended mainly for purposes of being able to attach<br>	  an Actor that follows the possessed Pawn location, but that still has the full aim rotation (since a Pawn might<br>	  update only some components of the rotation). |
| bIsPlayerController | `uint32` | Whether this controller is a PlayerController. |
| IgnoreMoveInput | `uint8` | Ignores movement input. Stacked state storage, Use accessor function IgnoreMoveInput() |
| IgnoreLookInput | `uint8` | Ignores look input. Stacked state storage, use accessor function IgnoreLookInput(). |
| StateName | `FName` |  |

## Functions

### GetControlRotation

Get the control rotation. This is the full aim rotation, which may be different than a camera orientation (for example in a third person view),
	   and may differ from the rotation of the controlled Pawn (which may choose not to visually pitch or roll, for example).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetControlRotation

Set the control rotation. The RootComponent's rotation will also be updated to match it if RootComponent->bAbsoluteRotation is true.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRotation | `FRotator &` |  |

**Return**

- Type: 
- Description: _None_

### SetInitialLocationAndRotation

Set the initial location and rotation of the controller, as well as the control rotation. Typically used when the controller is first created.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector &` |  |
| NewRotation | `FRotator &` |  |

**Return**

- Type: 
- Description: _None_

### SetStartSpot

Set the StartSpot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ClearStartSpot

Clear the StartSpot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetStartSpot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LineOfSightTo

Checks line to center and top of other actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Other | `AActor *` | is the actor whose visibility is being checked. |
| ViewPoint | `FVector` | is eye position visibility is being checked from. If vect(0,0,0) passed in, uses current viewtarget's eye position. |
| bAlternateChecks | `bool` | used only in AIController implementation |

**Return**

- Type: 
- Description: _None_

### OnRep_Pawn

Replication Notification Callbacks

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_PlayerState

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CastToPlayerController

DEPRECATED! Use the standard "Cast To" node instead. Casts this Controller to a Player Controller, if possible.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientSetLocation

Replicated function to set the pawn location and rotation, allowing server to force (ex. teleports).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` |  |
| NewRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### ClientSetRotation

Replicated function to set the pawn rotation, allowing the server to force.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRotation | `FRotator` |  |
| bResetCamera | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetPawn

Return the Pawn that is currently 'controlled' by this PlayerController

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetViewTarget

Get the actor the controller is looking at

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDesiredRotation

Get the desired pawn target rotation

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlayerController

Returns whether this Controller is a PlayerController.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsLocalPlayerController

Returns whether this Controller is a locally controlled PlayerController.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsLocalController

Returns whether this Controller is a local controller.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Possess

Handles attaching this controller to the specified pawn.
	  Only runs on the network authority (where HasAuthority() returns true).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPawn | `APawn *` | The Pawn to be possessed. |

**Return**

- Type: 
- Description: _None_

### UnPossess

Called to unpossess our pawn for any reason that is not the pawn being destroyed (destruction handled by PawnDestroyed()).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopMovement

Aborts the move the controller is currently performing

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIgnoreMoveInput

Locks or unlocks movement input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreMoveInput.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewMoveInput | `bool` | If true, move input is ignored. If false, input is not ignored. |

**Return**

- Type: 
- Description: _None_

### ResetIgnoreMoveInput

Stops ignoring move input by resetting the ignore move input state.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsMoveInputIgnored

Returns true if movement input is ignored.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIgnoreLookInput

Locks or unlocks look input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreLookInput.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewLookInput | `bool` | If true, look input is ignored. If false, input is not ignored. |

**Return**

- Type: 
- Description: _None_

### ResetIgnoreLookInput

Stops ignoring look input by resetting the ignore look input state.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsLookInputIgnored

Returns true if look input is ignored.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetIgnoreInputFlags

Reset move and look input ignore flags.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveInstigatedAnyDamage

Event when this controller instigates ANY damage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Damage | `float` |  |
| DamageType | `UDamageType *` |  |
| DamagedActor | `AActor *` |  |
| DamageCauser | `AActor *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnInstigatedAnyDamage |  | Called when the controller has instigated damage in any way |

## Language

cpp

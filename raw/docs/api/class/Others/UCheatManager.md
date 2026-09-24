# UCheatManager

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DebugCameraControllerRef | `ADebugCameraController *` | Debug camera - used to have independent camera without stopping gameplay |
| DebugCameraControllerClass | `TSubclassOf < ADebugCameraController >` | Debug camera - used to have independent camera without stopping gameplay |

## Functions

### FreezeFrame

Pause the game for Delay seconds.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delay | `float` |  |

**Return**

- Type: 
- Description: _None_

### Teleport

Teleport to surface player is looking at.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ChangeSize

Scale the player's size to be F  default size.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| F | `float` |  |

**Return**

- Type: 
- Description: _None_

### Fly

Pawn can fly.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Walk

Return to walking movement mode from Fly or Ghost cheat.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Ghost

Pawn no longer collides with the world, and can fly

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### God

Invulnerability cheat.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Slomo

Modify time dilation to change apparent speed of passage of time. e.g. "Slomo 0.1" makes everything move very slowly, while "Slomo 10" makes everything move very fast.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTimeDilation | `float` |  |

**Return**

- Type: 
- Description: _None_

### DamageTarget

Damage the actor you're looking at (sourced from the player).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamageAmount | `float` |  |

**Return**

- Type: 
- Description: _None_

### DestroyTarget

Destroy the actor you're looking at.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DestroyAll

Destroy all actors of class aClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| aClass | `TSubclassOf < AActor >` |  |

**Return**

- Type: 
- Description: _None_

### DestroyAllPawnsExceptTarget

Destroy all pawns except for the (pawn) target.  If no (pawn) target is found we don't destroy anything.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DestroyPawns

Destroys (by calling destroy directly) all non-player pawns of class aClass in the level

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| aClass | `TSubclassOf < APawn >` |  |

**Return**

- Type: 
- Description: _None_

### Summon

Load Classname and spawn an actor of that class

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ClassName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### PlayersOnly

Freeze everything in the level except for players.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ViewSelf

Make controlled pawn the viewtarget again.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ViewPlayer

View from the point of view of player with PlayerName S.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| S | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ViewActor

View from the point of view of AActor with Name ActorName.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActorName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ViewClass

View from the point of view of an AActor of class DesiredClass.  Each subsequent ViewClass cycles through the list of actors of that class.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DesiredClass | `TSubclassOf < AActor >` |  |

**Return**

- Type: 
- Description: _None_

### StreamLevelIn

Stream in the given level.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### OnlyLoadLevel

Load the given level.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### StreamLevelOut

Stream out the given level.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ToggleDebugCamera

Toggle between debug cameraplayer camera without locking gameplay and with locking local player controller input.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ToggleAILogging

toggles AI logging

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerToggleAILogging

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweep

Toggle capsule trace debugging. Will trace a capsule from current view point and show where it hits the world

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweepSize

Change Trace capsule size

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HalfHeight | `float` |  |
| Radius | `float` |  |

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweepChannel

Change Trace Channel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Channel | [ECollisionChannel](../../cppenum/E/EC/ECollisionChannel.md) |  |

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweepComplex

Change Trace Complex setting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bTraceComplex | `bool` |  |

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweepCapture

Capture current trace and add to persistent list

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweepPawn

Capture current local PC's pawn's location and add to persistent list

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DebugCapsuleSweepClear

Clear persistent list for trace capture

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TestCollisionDistance

Test all volumes in the world to the player controller's view location

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RebuildNavigation

Builds the navigation mesh (or rebuilds it).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetNavDrawDistance

Sets navigation drawing distance. Relevant only in non-editor modes.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DrawDistance | `float` |  |

**Return**

- Type: 
- Description: _None_

### DumpOnlineSessionState

Dump online session information

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DumpPartyState

Dump known party information

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DumpChatState

Dump known chat information

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DumpVoiceMutingState

Dump current state of voice chat

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BugItGo

This will move the player and set their rotation to the passed in values.
	  We have this version of the BugIt family as it is easier to type in just raw numbers in the console.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `float` |  |
| Y | `float` |  |
| Z | `float` |  |
| Pitch | `float` |  |
| Yaw | `float` |  |
| Roll | `float` |  |

**Return**

- Type: 
- Description: _None_

### BugIt

This function is used to print out the BugIt location.  It prints out copy and paste versions for both IMing someone to type in
	 and also a gameinfo ?options version so that you can append it to your launching url and be taken to the correct place.
	 Additionally, it will take a screen shot so reporting bugs is a one command action!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScreenShotDescription | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### BugItStringCreator

This will create a BugItGo string for us.  Nice for calling form c++ where you just want the string and no Screenshots

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ViewLocation | `FVector` |  |
| ViewRotation | `FRotator` |  |
| GoString | `FString &` |  |
| LocString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### FlushLog

This will force a flush of the output log to file

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LogLoc

Logs the current location in bugit format without taking screenshot and further routing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWorldOrigin

Translate world origin to this player position

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMouseSensitivityToDefault

Exec function to return the mouse sensitivity to its default value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### InvertMouse

Backwards compatibility exec function for people used to it instead of using InvertAxisKey

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheatScript

Executes commands listed in CheatScript.ScriptName ini section of DefaultGame.ini

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScriptName | `FString` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveInitCheatManager

BP implementable event for when CheatManager is created to allow any needed initialization.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveEndPlay

This is the End Play event for the CheatManager

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableDebugCamera

Switch controller to debug camera without locking gameplay and with locking local player controller input

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DisableDebugCamera

Switch controller from debug camera back to normal controller

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

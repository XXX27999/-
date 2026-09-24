# UGameInstance

GameInstance: high-level manager object for an instance of the running game.
  Spawned at game creation and not destroyed until game instance is shut down.
  Running as a standalone game, there will be one of these.
  Running in PIE (play-in-editor) will generate one of these per PIE instance.

## Parents

- [UObject](./UObject.md)
- FExec

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EncryptedLocalPlayers | `TArray < int64 >` |  |
| LocalPlayers | `TArray < ULocalPlayer * >` |  |
| OnlineSession | `UOnlineSession *` | Class to manage online services |
| bUseEncryptLocalPlayerPtr | `bool` |  |
| DSHUD | `UObject *` |  |
| CachedConsoleVariableBunch_Groups | `TArray < TArray < uint8 > >` |  |
| CachedConsoleVariableBunch_BigWorld | `TArray < uint8 >` |  |
| CachedConsoleVariableBunch_Permanent | `TArray < uint8 >` |  |
| SpecialPakResStates | `TMap < ESpecialPakID , EPakResState >` |  |

## Functions

### ReceiveInit

Opportunity for blueprints to handle the game instance being initialized.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveShutdown

Opportunity for blueprints to handle the game instance being shutdown.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HandleNetworkError

Opportunity for blueprints to handle network errors.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FailureType | `ENetworkFailure :: Type` |  |
| bIsServer | `bool` |  |

**Return**

- Type: 
- Description: _None_

### HandleTravelError

Opportunity for blueprints to handle travel errors.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FailureType | `ETravelFailure :: Type` |  |

**Return**

- Type: 
- Description: _None_

### DebugCreatePlayer

Local player access

	  Debug console command to create a player.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ControllerId | `int32` | - The controller ID the player should accept input from. |

**Return**

- Type: 
- Description: _None_

### DebugRemovePlayer

Debug console command to remove the player with a given controller ID.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ControllerId | `int32` | - The controller ID to search for. |

**Return**

- Type: 
- Description: _None_

### ResetDynaConfigAndDynaCVar

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetDynaConfig

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SendConsoleVariableBunch

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CVarType | `ECVarType` |  |
| Connection | `UNetConnection *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveConsoleVariableBunch_BigWorld

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InConsoleVariablesBunch | `TArray < uint8 >` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveConsoleVariableBunch_Permanent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InConsoleVariablesBunch | `TArray < uint8 >` |  |

**Return**

- Type: 
- Description: _None_

### EnableConsoleVariableBunch

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CVarType | `ECVarType` |  |
| bMapIsBigWorld | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClearConsoleVariableBunch

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CVarType | [ECVarType](../../cppenum/E/EC/ECVarType.md) |  |

**Return**

- Type: 
- Description: _None_

### ResetConsoleVariable

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CVarType | [ECVarType](../../cppenum/E/EC/ECVarType.md) |  |

**Return**

- Type: 
- Description: _None_

### SetPakResState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPakID | `ESpecialPakID` |  |
| InPakState | [EPakResState](../../cppenum/E/EP/EPakResState.md) |  |

**Return**

- Type: 
- Description: _None_

### GetPakResState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPakID | [ESpecialPakID](../../cppenum/E/ES/ESpecialPakID.md) |  |

**Return**

- Type: 
- Description: _None_

### IsPlatformSplitPakRes

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPakID | [ESpecialPakID](../../cppenum/E/ES/ESpecialPakID.md) |  |

**Return**

- Type: 
- Description: _None_

### InitPakResState

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
| OnPakResStateChanged |  |  |

## Language

cpp

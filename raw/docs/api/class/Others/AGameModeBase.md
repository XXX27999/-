# AGameModeBase

The GameModeBase defines the game being played. It governs the game rules, scoring, what actors
  are allowed to exist in this game type, and who may enter the game.

  It is only instanced on the server and will never exist on the client.

  A GameModeBase actor is instantiated when the level is initialized for gameplay in
  C++ UGameEngine::LoadMap().

  The class of this GameMode actor is determined by (in order) either the URL ?game=xxx,
  the GameMode Override value set in the World Settings, or the DefaultGameMode entry set
  in the game's Project Settings.

## Parents

- [AInfo](./AInfo.md)
- IVirtualParallelWorld

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OptionsString | `FString` | Save options string and parse it when needed |
| GameSessionClass | `TSubclassOf < AGameSession >` | Class of GameSession, which handles login approval and online game interface |
| GameStateClass | `TSubclassOf < AGameStateBase >` | Class of GameState associated with this GameMode. |
| PlayerControllerClass | `TSubclassOf < APlayerController >` | The class of PlayerController to spawn for players logging in. |
| PlayerStateClass | `TSubclassOf < APlayerState >` | A PlayerState of this class will be associated with every player to replicate relevant player information to all clients. |
| HUDClass | `TSubclassOf < AHUD >` | HUD class this game uses. |
| DefaultPawnClass | `TSubclassOf < APawn >` | The default pawn class used by players. |
| SpectatorClass | `TSubclassOf < ASpectatorPawn >` | The pawn class used by the PlayerController for players when spectating. |
| ReplaySpectatorPlayerControllerClass | `TSubclassOf < APlayerController >` | The PlayerController class used when spectating a network replay. |
| GameSession | `AGameSession *` | Game Session handles login approval, arbitration, online game interface |
| GameState | `AGameStateBase *` | GameState is used to replicate game state relevant properties to all clients. |
| DefaultPlayerName | `FText` | The default player name assigned to players that join with no name specified. |
| bUseSeamlessTravel | `uint32` | Whether the game perform map travels using SeamlessTravel() which loads in the background and doesn't disconnect clients |
| bUnlimitedRegionZ | `uint32` |  |
| bStartPlayersAsSpectators | `uint32` | Whether players should immediately spawn when logging in, or stay as spectators until they manually spawn |
| bPauseable | `uint32` | Whether the game is pauseable. |

## Functions

### GetDefaultPawnClassForController

Returns default pawn class for given controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InController | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### GetNumPlayers

Returns number of active human players, excluding spectators

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNumSpectators

Returns number of human players currently spectating

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StartPlay

Transitions to calls BeginPlay on actors.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasMatchStarted

Returns true if the match start callbacks have been called

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ShouldReset

Overridable function to determine whether an Actor should have Reset called when the game has Reset called on it.
	  Default implementation returns true

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActorToReset | `AActor *` | The actor to make a determination for |

**Return**

- Type: 
- Description: _None_

### ResetLevel

Overridable function called when resetting level. This is used to reset the game state while staying in the same map
	  Default implementation calls Reset() on all actors except GameMode and Controllers

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReturnToMainMenuHost

Return to main menu, and disconnect any players

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_PostLogin

Notification that a player has successfully logged in, and has been given a player controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnLogout

Implementable event when a Controller with a PlayerState leaves the game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ExitingController | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### HandleStartingNewPlayer

Signals that a player is ready to enter the game, which may start it up

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### MustSpectate

Returns true if NewPlayerController may only join the server as a spectator.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayerController | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### CanSpectate

Return whether Viewer is allowed to spectate from the point of view of ViewTarget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Viewer | `APlayerController *` |  |
| ViewTarget | `APlayerState *` |  |

**Return**

- Type: 
- Description: _None_

### ChangeName

Sets the name for a controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AController *` | The controller of the player to change the name of |
| NewName | `FString &` | The name to set the player to |
| bNameChange | `bool` | Whether the name is changing or if this is the first time it has been set |

**Return**

- Type: 
- Description: _None_

### K2_OnChangeName

Overridable event for GameMode blueprint to respond to a change name call

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Other | `AController *` |  |
| NewName | `FString &` | The name to set the player to |
| bNameChange | `bool` | Whether the name is changing or if this is the first time it has been set |

**Return**

- Type: 
- Description: _None_

### ChoosePlayerStart

Return the 'best' player start for this player to spawn from
	  Default implementation looks for a random unoccupied spot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `AController *` | is the controller for whom we are choosing a playerstart |

**Return**

- Type: 
- Description: _None_

### FindPlayerStart

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `AController *` | The AController for whom we are choosing a Player Start |
| IncomingName | `FString &` | Specifies the tag of a Player Start to use |

**Return**

- Type: 
- Description: _None_

### K2_FindPlayerStart

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `AController *` | The AController for whom we are choosing a Player Start |
| IncomingName | `FString &` | Specifies the tag of a Player Start to use |

**Return**

- Type: 
- Description: _None_

### PlayerCanRestart

Returns true if it's valid to call RestartPlayer. By default will call Player->CanRestartPlayer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### RestartPlayer

Tries to spawn the player's pawn, at the location returned by FindPlayerStart

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### RestartPlayerAtPlayerStart

Tries to spawn the player's pawn at the specified actor's location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `AController *` |  |
| StartSpot | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### RestartPlayerAtTransform

Tries to spawn the player's pawn at a specific location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `AController *` |  |
| SpawnTransform | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### SpawnDefaultPawnFor

Called during RestartPlayer to actually spawn the player's pawn, when using a start spot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `AController *` | - Controller for whom this pawn is spawned |
| StartSpot | `AActor *` | - Actor at which to spawn pawn |

**Return**

- Type: 
- Description: _None_

### SpawnDefaultPawnAtTransform

Called during RestartPlayer to actually spawn the player's pawn, when using a transform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `AController *` | - Controller for whom this pawn is spawned |
| SpawnTransform | `FTransform &` |  |

**Return**

- Type: 
- Description: _None_

### InitStartSpot

Called from RestartPlayerAtPlayerStart, can be used to initialize the start spawn actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartSpot | `AActor *` |  |
| NewPlayer | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnRestartPlayer

Implementable event called at the end of RestartPlayer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### InitializeHUDForPlayer

Initialize the AHUD object for a player. Games can override this to do something different

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlayer | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnSwapPlayerControllers

Called when a PlayerController is swapped to a new one during seamless travel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldPC | `APlayerController *` |  |
| NewPC | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

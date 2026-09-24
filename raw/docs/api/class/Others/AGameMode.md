# AGameMode

GameMode is a subclass of GameModeBase that behaves like a multiplayer match-based game.
  It has default behavior for picking spawn points and match state.
  If you want a simpler base, inherit from GameModeBase instead.

## Parents

- [AGameModeBase](./AGameModeBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MatchState | `FName` | What match state we are currently in |
| bDelayedStart | `uint32` | Whether the game should immediately start when the first player logs in. Affects the default behavior of ReadyToStartMatch |
| NumSpectators | `int32` | Current number of spectators. |
| NumPlayers | `int32` | Current number of human players. |
| NumBots | `int32` | number of non-human players (AI controlled but participating as a player). |
| MinRespawnDelay | `float` | Minimum time before player can respawn after dying. |
| NumTravellingPlayers | `int32` | Number of players that are still traveling from a previous map |
| EngineMessageClass | `TSubclassOf < ULocalMessage >` | Contains strings describing localized game agnostic messages. |
| InactivePlayerArray | `TArray < APlayerState * >` | PlayerStates of players who have disconnected from the server (saved in case they reconnect) |
| bEnabelPawnPool | `bool` | Weather to enable Gamemode Pawn Pool |
| InactivePlayerStateLifeSpan | `float` | Time a playerstate will stick around in an inactive state after a player logout |
| bHandleDedicatedServerReplays | `bool` | If true, dedicated servers will record replays when HandleMatchHasStartedHandleMatchHasStopped is called |

## Functions

### GetMatchState

Returns the current match state, this is an accessor to protect the state machine flow

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsMatchInProgress

Returns true if the match state is InProgress or other gameplay state

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasMatchEnded

Returns true if the match state is WaitingPostMatch or later

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StartMatch

Transition from WaitingToStart to InProgress. You can call this manually, will also get called if ReadyToStartMatch returns true

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EndMatch

Transition from InProgress to WaitingPostMatch. You can call this manually, will also get called if ReadyToEndMatch returns true

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RestartGame

Restart the game, by default travel to the current map

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AbortMatch

Report that a match has failed due to unrecoverable error

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_OnSetMatchState

Implementable event to respond to match state changes

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewState | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ReadyToStartMatch

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReadyToEndMatch

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Say

Exec command to broadcast a string to all players

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Msg | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### SetBandwidthLimit

Alters the synthetic bandwidth limit for a running game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AsyncIOBandwidthLimit | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# AGameStateBase

GameStateBase is a class that manages the game's global state, and is spawned by GameModeBase.
  It exists on both the client and the server and is fully replicated.

## Parents

- [AInfo](./AInfo.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| GameModeClass | `TSubclassOf < AGameModeBase >` | Class of the server's game mode, assigned by GameModeBase. |
| AuthorityGameMode | `AGameModeBase *` | Instance of the current game mode, exists only on the server. For non-authority clients, this will be NULL. |
| SpectatorClass | `TSubclassOf < ASpectatorPawn >` | Class used by spectators, assigned by GameModeBase. |
| PlayerArray | `TArray < APlayerState * >` | Array of all PlayerStates, maintained on both server and clients (PlayerStates are always relevant) |
| bReplicatedHasBegunPlay | `bool` | Replicated when GameModeBase->StartPlay has been called so the client will also start play |
| ReplicatedWorldTimeSeconds | `float` | Server TimeSeconds. Useful for syncing up animation and gameplay. |
| ServerWorldTimeSecondsDelta | `float` | The difference from the local world's TimeSeconds and the server world's TimeSeconds. |
| ServerWorldTimeSecondsUpdateFrequency | `float` | Frequency that the server updates the replicated TimeSeconds from the world. Set to zero to disable periodic updates. |
| bRecordControllerReplay | `bool` | If use rec ctrl in replay |
| PauseInfo | `bool` |  |

## Functions

### GetServerWorldTimeSeconds

Returns the simulated TimeSeconds on the server, will be synchronized on client and server

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetServerWorldTimeSecondsForReplay

Returns the simulated TimeSeconds on the server while playing replay, with fastforward skipped time considered

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasBegunPlay

Returns true if the world has started play (called BeginPlay on actors)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasMatchStarted

Returns true if the world has started match (called MatchStarted callbacks)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlayerStartTime

Returns the time that should be used as when a player started

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerRespawnDelay

Returns how much time needs to be spent before a player can respawn

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_GameModeClass

GameModeBase class notification callback.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_SpectatorClass

Callback when we receive the spectator class

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedHasBegunPlay

By default calls BeginPlay and StartMatch

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedWorldTimeSeconds

Allows clients to calculate ServerWorldTimeSecondsDelta

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldValue | `float &` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_RecordControllerReplay

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_PauseInfo

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
| OnPauseState |  |  |

## Language

cpp

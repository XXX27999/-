# AGameState

GameState is a subclass of GameStateBase that behaves like a multiplayer match-based game.
  It is tied to functionality in GameMode.

## Parents

- [AGameStateBase](./AGameStateBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MatchState | `FName` | What match state we are currently in |
| PreviousMatchState | `FName` | Previous map state, used to handle if multiple transitions happen per frame |
| ElapsedTime | `int32` | Elapsed game time since match has started. |

## Functions

### OnRep_MatchState

Match state has changed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ElapsedTime

Gives clients the chance to do something when time gets updates

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGeneralCampNameByCampID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CampID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetGeneralCampRelation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CampAID | `int32` |  |
| CampBID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetGameModeGeneralDataAsset

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

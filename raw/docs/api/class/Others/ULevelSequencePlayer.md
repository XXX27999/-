# ULevelSequencePlayer

ULevelSequencePlayer is used to actually "play" an level sequence asset at runtime.

  This class keeps track of playback state and provides functions for manipulating
  an level sequence while its playing.

## Parents

- [UMovieSceneSequencePlayer](./UMovieSceneSequencePlayer.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AdditionalEventReceivers | `TArray < UObject * >` | Array of additional event receivers |

## Functions

### CreateLevelSequencePlayer

Create a new level sequence player.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | Context object from which to retrieve a UWorld. |
| LevelSequence | `ULevelSequence *` | The level sequence to play. |
| Settings | `FMovieSceneSequencePlaybackSettings` | The desired playback settings |
| OutActor | `ALevelSequenceActor * &` | The level sequence actor created to play this sequence. |

**Return**

- Type: 
- Description: _None_

### GetEventReceivers

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
| OnCameraCut |  | Event triggered when there is a camera cut |

## Language

cpp

# UMovieSceneSequencePlayer

Abstract class that provides consistent player behaviour for various animation players

## Parents

- [UObject](./UObject.md)
- IMovieScenePlayer

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Status | `TEnumAsByte < EMovieScenePlayerStatus :: Type >` | Movie player status. |
| bReversePlayback | `uint32` | Whether we're currently playing in reverse. |
| bPendingFirstUpdate | `uint32` | True where we're waiting for the first update of the sequence after calling StartPlayingNextTick. |
| Sequence | `UMovieSceneSequence *` | The sequence to play back |
| TimeCursorPosition | `float` | The current time cursor position within the sequence (in seconds) |
| StartTime | `float` | Time time at which to start playing the sequence (defaults to the lower bound of the sequence's play range) |
| EndTime | `float` | Time time at which to end playing the sequence (defaults to the upper bound of the sequence's play range) |
| CurrentNumLoops | `int32` | The number of times we have looped in the current playback |
| PlaybackSettings | [FMovieSceneSequencePlaybackSettings](../../cppstruct/F/FM/FMovieSceneSequencePlaybackSettings.md) | Specific playback settings for the animation. |
| RootTemplateInstance | [FMovieSceneRootEvaluationTemplateInstance](../../cppstruct/F/FM/FMovieSceneRootEvaluationTemplateInstance.md) | The root template instance we're evaluating |

## Functions

### Play

Start playback forwards from the current time cursor position, using the current play rate.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PlayReverse

Reverse playback.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ChangePlaybackDirection

Changes the direction of playback (go in reverse if it was going forward, or vice versa)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SeekPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### PlayLooping

Start playback from the current time cursor position, looping the specified number of times.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NumLoops | `int32` | - The number of loops to play. -1 indicates infinite looping. |

**Return**

- Type: 
- Description: _None_

### StartPlayingNextTick

Start playback from the current time cursor position, using the current play rate. Does not update the animation until next tick.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Pause

Pause playback.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Scrub

Scrub playback.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Stop

Stop playback.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GoToEndAndStop

Go to end and stop.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaybackPosition

Get the current playback position

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlaybackPosition

Set the current playback position

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlaybackPosition | `float` | - The new playback position to set. |

**Return**

- Type: 
- Description: _None_

### SetPlaybackPostionWithloop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetTargetTimePostionWithloop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### JumpToPosition

Jump to new playback position

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlaybackPosition | `float` | - The new playback position to set. |

**Return**

- Type: 
- Description: _None_

### JumpToPositionEx

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPlaybackPosition | `float` |  |

**Return**

- Type: 
- Description: _None_

### IsPlaying

Check whether the sequence is actively playing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPaused

Check whether the sequence is paused.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLength

Get the playback length of the sequence

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlayRate

Get the playback rate of this player.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsEvaluating

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlayRate

Set the playback rate of this player. Negative values will play the animation in reverse.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayRate | `float` | - The new rate of playback for the animation. |

**Return**

- Type: 
- Description: _None_

### SetPlayLoopCount

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NumLoops | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetPlaybackRange

Sets the range in time to be played back by this player, overriding the default range stored in the asset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewStartTime | `float` | The new starting time for playback |
| NewEndTime | `float` | The new ending time for playback. Must be larger than the start time. |

**Return**

- Type: 
- Description: _None_

### GetPlaybackStart

Get the offset within the level sequence to start playing

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaybackStartSeconds

Get the offset seconds within the level sequence to start playing

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaybackEnd

Get the offset within the level sequence to finish playing

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlaybackEndSeconds

Get the offset seconds within the level sequence to finish playing

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBoundObjects

Retrieve all objects currently bound to the specified binding identifier

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectBinding | [FMovieSceneObjectBindingID](../../cppstruct/F/FM/FMovieSceneObjectBindingID.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnPlay |  | Event triggered when the level sequence player is played |
| OnPlayReverse |  | Event triggered when the level sequence player is played in reverse |
| OnStop |  | Event triggered when the level sequence player is stopped |
| OnPause |  | Event triggered when the level sequence player is paused |
| OnFinished |  | Event triggered when the level sequence player finishes naturally (without explicitly calling stop) |
| OnObjectSpawnedEvent |  |  |

## Language

cpp

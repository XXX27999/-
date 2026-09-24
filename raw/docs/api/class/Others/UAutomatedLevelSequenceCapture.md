# UAutomatedLevelSequenceCapture

## Parents

- [UMovieSceneCapture](./UMovieSceneCapture.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| LevelSequenceAsset | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | A level sequence asset to playback at runtime - used where the level sequence does not already exist in the world. |
| bUseCustomStartFrame | `bool` | When enabled, the StartFrame setting will override the default starting frame number |
| StartFrame | `int32` | Frame number to start capturing.  The frame number range depends on whether the bUseRelativeFrameNumbers option is enabled. |
| bUseCustomEndFrame | `bool` | When enabled, the EndFrame setting will override the default ending frame number |
| EndFrame | `int32` | Frame number to end capturing.  The frame number range depends on whether the bUseRelativeFrameNumbers option is enabled. |
| WarmUpFrameCount | `int32` | The number of extra frames to play before the sequence's start frame, to "warm up" the animation.  This is useful if your<br>	    animation contains particles or other runtime effects that are spawned into the scene earlier than your capture start frame |
| DelayBeforeWarmUp | `float` | The number of seconds to wait (in real-time) before we start playing back the warm up frames.  Useful for allowing post processing effects to settle down before capturing the animation. |
| BurnInOptions | `ULevelSequenceBurnInOptions *` |  |
| bWriteEditDecisionList | `bool` | Whether to write edit decision lists (EDLs) if the sequence contains shots |
| LevelSequenceActor | `TWeakObjectPtr < ALevelSequenceActor >` | The pre-existing level sequence actor to use for capture that specifies playback settings |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

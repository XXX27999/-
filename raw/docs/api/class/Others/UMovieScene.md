# UMovieScene

Implements a movie scene asset.

## Parents

- [UMovieSceneSignedObject](./UMovieSceneSignedObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Spawnables | `TArray < FMovieSceneSpawnable >` | Data-only blueprints for all of the objects that we we're able to spawn.<br>	  These describe objects and actors that we may instantiate at runtime,<br>	  or create proxy objects for previewing in the editor. |
| Possessables | `TArray < FMovieScenePossessable >` | Typed slots for already-spawned objects that we are able to control with this MovieScene |
| ObjectBindings | `TArray < FMovieSceneBinding >` | Tracks bound to possessed or spawned objects |
| MasterTracks | `TArray < UMovieSceneTrack * >` | Master tracks which are not bound to spawned or possessed objects |
| CameraCutTrack | `UMovieSceneTrack *` | The camera cut track is a specialized track for switching between cameras on a cinematic |
| SelectionRange | [FFloatRange](../../cppstruct/F/FF/FFloatRange.md) | User-defined selection range. |
| PlaybackRange | [FFloatRange](../../cppstruct/F/FF/FFloatRange.md) | User-defined playback range for this movie scene. Must be a finite range. Relative to this movie-scene's 0-time origin. |
| bForceFixedFrameIntervalPlayback | `bool` |  |
| FixedFrameInterval | `float` |  |
| InTime_DEPRECATED | `float` |  |
| OutTime_DEPRECATED | `float` |  |
| StartTime_DEPRECATED | `float` |  |
| EndTime_DEPRECATED | `float` |  |
| bGlobalUseQuaternionInterpolation | `bool` | 全局四元数插值开关：开启后该 LevelSequence 中所有 Transform Section 的旋转都走四元数 Slerp（默认关闭） |
| EmptySections | `TArray < UMovieSceneSection * >` |  |
| bPlaybackRangeLocked | `bool` | User-defined playback range is locked. |
| ObjectsToDisplayNames | `TMap < FString , FText >` | Maps object GUIDs to user defined display names. |
| ObjectsToLabels | `TMap < FString , FMovieSceneTrackLabels >` | Maps object GUIDs to user defined labels. |
| EditorData | [FMovieSceneEditorData](../../cppstruct/F/FM/FMovieSceneEditorData.md) | Editor only data that needs to be saved between sessions for editing but has no runtime purpose |
| RootFolders | `TArray < UMovieSceneFolder * >` | The root folders for this movie scene. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

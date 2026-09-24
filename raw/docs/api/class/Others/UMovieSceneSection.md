# UMovieSceneSection

Base class for movie scene sections

## Parents

- [UMovieSceneSignedObject](./UMovieSceneSignedObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EvalOptions | [FMovieSceneSectionEvalOptions](../../cppstruct/F/FM/FMovieSceneSectionEvalOptions.md) |  |
| Easing | [FMovieSceneEasingSettings](../../cppstruct/F/FM/FMovieSceneEasingSettings.md) |  |
| StartTime | `float` | The start time of the section |
| EndTime | `float` | The end time of the section |
| RowIndex | `int32` | The row index that this section sits on |
| OverlapPriority | `int32` | This section's priority over overlapping sections |
| bIsActive | `uint32` | Toggle whether this section is activeinactive |
| bIsLocked | `uint32` | Toggle whether this section is lockedunlocked |
| bIsInfinite | `uint32` | Toggle to set this section to be infinite |
| PreRollTime | `float` | The amount of time to prepare this section for evaluation before it actually starts. |
| PostRollTime | `float` | The amount of time to continue 'postrolling' this section for after evaluation has ended. |
| BlendType | [FOptionalMovieSceneBlendType](../../cppstruct/F/FO/FOptionalMovieSceneBlendType.md) |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

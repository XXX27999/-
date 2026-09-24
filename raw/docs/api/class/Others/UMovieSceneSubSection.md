# UMovieSceneSubSection

Implements a section in sub-sequence tracks.

## Parents

- [UMovieSceneSection](./UMovieSceneSection.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Parameters | [FMovieSceneSectionParameters](../../cppstruct/F/FM/FMovieSceneSectionParameters.md) |  |
| StartOffset_DEPRECATED | `float` |  |
| TimeScale_DEPRECATED | `float` |  |
| PrerollTime_DEPRECATED | `float` |  |
| SubSequence | `UMovieSceneSequence *` | Movie scene being played by this section.<br><br>	  @todo Sequencer: Should this be lazy loaded? |
| ActorToRecord | `TLazyObjectPtr < AActor >` | Target actor to record |
| TargetSequenceName | `FString` | Target name of sequence to try to record to (will record automatically to another if this already exists) |
| TargetPathToRecordTo | [FDirectoryPath](../../cppstruct/F/FD/FDirectoryPath.md) | Target path of sequence to record to |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

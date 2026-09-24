# UMovieSceneNewEventTrack

Implements a movie scene track that triggers discrete events during playback.

## Parents

- UMovieSceneNameableTrack

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bFireEventsWhenForwards | `uint32` | If events should be fired when passed playing the sequence forwards. |
| bFireEventsWhenBackwards | `uint32` | If events should be fired when passed playing the sequence backwards. |
| EventPosition | [EFireEventsAtPosition](../../cppenum/E/EF/EFireEventsAtPosition.md) | Defines where in the evaluation to trigger events |
| Sections | `TArray < UMovieSceneSection * >` | The track's sections. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

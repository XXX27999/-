# UInterpTrackEvent

## Parents

- [UInterpTrack](./UInterpTrack.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EventTrack | `TArray < struct FEventTrackKey >` | Array of events to fire off. |
| bFireEventsWhenForwards | `uint32` | If events should be fired when passed playing the sequence forwards. |
| bFireEventsWhenBackwards | `uint32` | If events should be fired when passed playing the sequence backwards. |
| bFireEventsWhenJumpingForwards | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |
| bUseCustomEventName | `uint32` | If checked each key's event name is the exact name of the custom event function in level script that will be called |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

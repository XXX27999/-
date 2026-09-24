# UInterpTrackAnimControl

## Parents

- [UInterpTrackFloatBase](./UInterpTrackFloatBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FName` | Name of slot to use when playing animation. Passed to Actor.<br>	 	When multiple tracks use the same slot name, they are each given a different ChannelIndex when SetAnimPosition is called. |
| AnimSeqs | `TArray < struct FAnimControlTrackKey >` | Track of different animations to play and when to start playing them. |
| bSkipAnimNotifiers | `uint32` | Skip all anim notifiers |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

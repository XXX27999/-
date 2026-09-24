# UInterpTrackSound

## Parents

- [UInterpTrackVectorBase](./UInterpTrackVectorBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Sounds | `TArray < struct FSoundTrackKey >` | Array of sounds to play at specific times. |
| bPlayOnReverse | `uint32` | if set, sound plays only when playing the matinee in reverse instead of when the matinee plays forward |
| bContinueSoundOnMatineeEnd | `uint32` | If true, sounds on this track will not be forced to finish when the matinee sequence finishes. |
| bSuppressSubtitles | `uint32` | If true, don't show subtitles for sounds played by this track. |
| bTreatAsDialogue | `uint32` | If true and track is controlling a pawn, makes the pawn "speak" the given audio. |
| bAttach | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

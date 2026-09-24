# UAnimSequenceBase

## Parents

- [UAnimationAsset](./UAnimationAsset.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Notifies | `TArray < FAnimNotifyEvent >` | Animation notifies, sorted by time (earliest notification first). |
| SequenceLength | `float` | Length (in seconds) of this AnimSequence if played back with a speed of 1.0. |
| RateScale | `float` | Number for tweaking playback rate of this animation globally. |
| bEnableExcludeNotifiesWhenPlayAsMontage | `bool` |  |
| RawCurveData | `FRawCurveTracks` | Raw uncompressed float curve data |

## Functions

### GetPlayLength

Returns the total play length of the montage, if played back with a speed of 1.0.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

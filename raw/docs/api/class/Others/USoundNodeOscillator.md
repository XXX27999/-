# USoundNodeOscillator

Defines how a sound oscillates

## Parents

- [USoundNode](./USoundNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bModulateVolume | `uint32` | Whether to oscillate volume. |
| bModulatePitch | `uint32` | Whether to oscillate pitch. |
| AmplitudeMin | `float` | An amplitude of 0.25 would oscillate between 0.75 and 1.25. |
| AmplitudeMax | `float` | An amplitude of 0.25 would oscillate between 0.75 and 1.25. |
| FrequencyMin | `float` | A frequency of 20 would oscillate at 10Hz. |
| FrequencyMax | `float` | A frequency of 20 would oscillate at 10Hz. |
| OffsetMin | `float` | Offset into the sine wave. Value modded by 2  PI. |
| OffsetMax | `float` | Offset into the sine wave. Value modded by 2  PI. |
| CenterMin | `float` | A center of 0.5 would oscillate around 0.5. |
| CenterMax | `float` | A center of 0.5 would oscillate around 0.5. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

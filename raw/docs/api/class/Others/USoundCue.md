# USoundCue

The behavior of audio playback is defined within Sound Cues.

## Parents

- [USoundBase](./USoundBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bOverrideAttenuation | `uint32` | Indicates whether attenuation should use the Attenuation Overrides or the Attenuation Settings asset |
| FirstNode | `USoundNode *` |  |
| VolumeMultiplier | `float` | Volume multiplier for the Sound Cue |
| PitchMultiplier | `float` | Pitch multiplier for the Sound Cue |
| AttenuationOverrides | [FSoundAttenuationSettings](../../cppstruct/F/FS/FSoundAttenuationSettings.md) | Attenuation settings to use if Override Attenuation is set to true |
| SubtitlePriority | `float` |  |
| AllNodes | `TArray < USoundNode * >` |  |
| SoundCueGraph | `UEdGraph *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

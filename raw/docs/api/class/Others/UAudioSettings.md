# UAudioSettings

Audio settings.

## Parents

- UDeveloperSettings

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DefaultSoundClassName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The SoundClass assigned to newly created sounds |
| DefaultSoundConcurrencyName | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The SoundConcurrency assigned to newly created sounds |
| DefaultBaseSoundMix | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | The SoundMix to use as base when no other system has specified a Base SoundMix |
| VoiPSoundClass | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | Sound class to be used for the VOIP audio component |
| DefaultReverbSendLevel | `float` | The amount of audio to send to reverb submixes if no reverb send is setup for the source through attenuation settings. Only used in audio mixer. |
| LowPassFilterResonance | `float` |  |
| MaximumConcurrentStreams | `int32` | How many streaming sounds can be played at the same time (if more are played they will be sorted by priority) |
| QualityLevels | `TArray < FAudioQualitySettings >` |  |
| bAllowVirtualizedSounds | `uint32` | Allows sounds to play at 0 volume. |
| bDisableMasterEQ | `uint32` | Disables master EQ effect in the audio DSP graph. |
| bDisableMasterReverb | `uint32` | Disables master reverb effect in the audio DSP graph. |
| bAllowCenterChannel3DPanning | `uint32` | Enables the surround sound spatialization calculations to include the center channel. |
| DialogueFilenameFormat | `FString` |  |
| AkEventCppNotifyClass | `TSoftClassPtr < UAnimNotify >` | UAnimNotify_AkEventCpp is the subclass of UAnimNotify. |
| TimedAkEventNotifyStateClass | `TSoftClassPtr < UAnimNotifyState >` | UAnimNotifyState_TimedAkEvent is the subclass of UAnimNotifyState. |
| AkAudioEventSearchDepth | `uint8` | Search depth when trying to link commerce animation montage with its AkAudioEvent. |
| bUsePreCachedMontageMap | `bool` | Whether to use pre-cached map for AkAudio-Montages searching. |
| bDynamicPreCachedMontageMap | `bool` | Whether to dynamically update pre-cached map for AkAudio-Montages searching. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

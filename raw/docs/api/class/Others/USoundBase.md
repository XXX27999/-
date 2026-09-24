# USoundBase

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SoundClassObject | `USoundClass *` | Sound class this sound belongs to |
| bDebug | `uint32` | When "stat sounds -debug" has been specified, draw this sound's attenuation shape when the sound is audible. For debugging purpose only. |
| bOverrideConcurrency | `uint32` | Whether or not to override the sound concurrency object with local concurrency settings. |
| bOutputToBusOnly | `uint32` | Whether or not to only send this audio's output to a bus. If true, will not be this sound won't be audible except through bus sends. |
| bIgnoreFocus_DEPRECATED | `uint32` |  |
| SoundConcurrencySettings | `USoundConcurrency *` | If Override Concurrency is false, the sound concurrency settings to use for this sound. |
| ConcurrencyOverrides | [FSoundConcurrencySettings](../../cppstruct/F/FS/FSoundConcurrencySettings.md) | If Override Concurrency is true, concurrency settings to use. |
| MaxConcurrentResolutionRule_DEPRECATED | `TEnumAsByte < enum EMaxConcurrentResolutionRule :: Type >` |  |
| MaxConcurrentPlayCount_DEPRECATED | `int32` | Maximum number of times this sound can be played concurrently. |
| Duration | `float` | Duration of sound in seconds. |
| AttenuationSettings | `USoundAttenuation *` | Attenuation settings package for the sound |
| Priority | `float` | Sound priority (higher value is higher priority) used for concurrency resolution. This priority value is weighted against the final volume of the sound. |
| SoundSubmixObject | `USoundSubmix *` | Sound submix this sound belongs to.<br>	   Audio will play here and traverse through the submix graph.<br>	   A null entry will make the sound obey the default master effects graph. |
| SoundSubmixSends | `TArray < FSoundSubmixSendInfo >` | An array of submix sends. Audio from this sound will send a portion of its audio to these effects. |
| SourceEffectChain | `USoundEffectSourcePresetChain *` | The source effect chain to use for this sound. |
| BusSends | `TArray < FSoundSourceBusSendInfo >` | This sound will send it's audio output to this list of buses if there are bus instances playing. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

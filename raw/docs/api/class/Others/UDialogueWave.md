# UDialogueWave

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bMature | `uint32` | true if this dialogue is considered to contain matureadult content. |
| bOverride_SubtitleOverride | `uint32` |  |
| SpokenText | `FString` | A localized version of the text that is actually spoken phonetically in the audio. |
| SubtitleOverride | `FString` | A localized version of the subtitle text that should be displayed for this audio. By default this will be the same as the Spoken Text. |
| ContextMappings | `TArray < FDialogueContextMapping >` | Mappings between dialogue contexts and associated soundwaves. |
| LocalizationGUID | [FGuid](../../cppstruct/F/FG/FGuid.md) |  |
| VoiceActorDirection | `FString` | Provides general notes to the voice actor intended to direct their performance, as well as contextual information to the translator. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

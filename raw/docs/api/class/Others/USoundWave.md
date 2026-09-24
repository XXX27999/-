# USoundWave

## Parents

- [USoundBase](./USoundBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CompressionQuality | `int32` | Platform agnostic compression quality. 1..100 with 1 being best compression and 100 being best quality. |
| bLooping | `uint32` | If set, when played directly (not through a sound cue) the wave will be played looping. |
| bStreaming | `uint32` | Whether this sound can be streamed to avoid increased memory usage |
| StreamingPriority | `int32` | Priority of this sound when streaming (lower priority streams may not always play) |
| bMature | `uint32` | If set to true if this sound is considered to contain matureadult content. |
| bManualWordWrap | `uint32` | If set to true will disable automatic generation of line breaks - use if the subtitles have been split manually. |
| bSingleLine | `uint32` | If set to true the subtitles display as a sequence of single lines as opposed to multiline. |
| bVirtualizeWhenSilent | `uint32` | Allows sound to play at 0 volume, otherwise will stop the sound when the sound is silent. |
| SoundGroup | `TEnumAsByte < ESoundGroup >` |  |
| SpokenText | `FString` | A localized version of the text that is actually spoken phonetically in the audio. |
| SubtitlePriority | `float` | The priority of the subtitle. |
| Volume | `float` | Playback volume of sound 0 to 1 - Default is 1.0. |
| Pitch | `float` | Playback pitch for sound. |
| NumChannels | `int32` | Number of channels of multichannel data; 1 or 2 for regular mono and stereo files |
| SampleRate | `int32` | Cached sample rate for displaying in the tools |
| RawPCMDataSize | `int32` | Size of RawPCMData, or what RawPCMData would be if the sound was fully decompressed |
| Subtitles | `TArray < struct FSubtitleCue >` | Subtitle cues.  If empty, use SpokenText as the subtitle.  Will often be empty,<br>	  as the contents of the subtitle is commonly identical to what is spoken. |
| LocalizedSubtitles | `TArray < struct FLocalizedSubtitle >` | The array of the subtitles for each language. Generated at cook time. |
| Curves | `UCurveTable *` | Curves associated with this sound wave |
| InternalCurves | `UCurveTable *` | Hold a reference to our internal curve so we can switch back to it if we want to |
| ChannelOffsets | `TArray < int32 >` | Offsets into the bulk data for the source wav data |
| ChannelSizes | `TArray < int32 >` | Sizes of the bulk data for the source wav data |
| Comment | `FString` | Provides contextual information for the sound to the translator. |
| SourceFilePath_DEPRECATED | `FString` |  |
| SourceFileTimestamp_DEPRECATED | `FString` |  |
| AssetImportData | `UAssetImportData *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

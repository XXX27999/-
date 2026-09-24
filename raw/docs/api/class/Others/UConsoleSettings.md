# UConsoleSettings

Implements the settings for the UConsole class.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxScrollbackSize | `int32` | Visible Console stuff |
| ManualAutoCompleteList | `TArray < struct FAutoCompleteCommand >` | Manual list of auto-complete commands and info specified in BaseInput.ini |
| AutoCompleteMapPaths | `TArray < FString >` | List of relative paths (e.g. ContentMaps) to search for map names for auto-complete usage. Specified in BaseInput.ini. |
| BackgroundOpacityPercentage | `float` | Amount of transparency of the console background. |
| bOrderTopToBottom | `bool` | Whether we legacy bottom-to-top ordering or regular top-to-bottom ordering |
| InputColor | [FColor](../../cppstruct/F/FC/FColor.md) | The color used for text input. |
| HistoryColor | [FColor](../../cppstruct/F/FC/FColor.md) | The color used for the previously typed commands history. |
| AutoCompleteCommandColor | [FColor](../../cppstruct/F/FC/FColor.md) | The autocomplete color used for executable commands. |
| AutoCompleteCVarColor | [FColor](../../cppstruct/F/FC/FColor.md) | The autocomplete color used for mutable CVars. |
| AutoCompleteFadedColor | [FColor](../../cppstruct/F/FC/FColor.md) | The autocomplete color used for command descriptions and read-only CVars. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

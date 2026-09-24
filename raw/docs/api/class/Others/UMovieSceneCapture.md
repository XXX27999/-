# UMovieSceneCapture

Class responsible for capturing scene data

## Parents

- [UObject](./UObject.md)
- IMovieSceneCaptureInterface
- ICaptureProtocolHost

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CaptureType | [FCaptureProtocolID](../../cppstruct/F/FC/FCaptureProtocolID.md) | The type of capture protocol to use |
| ProtocolSettings | `UMovieSceneCaptureProtocolSettings *` | Settings specific to the capture protocol |
| Settings | [FMovieSceneCaptureSettings](../../cppstruct/F/FM/FMovieSceneCaptureSettings.md) | Settings that define how to capture |
| bUseSeparateProcess | `bool` | Whether to capture the movie in a separate process or not |
| bCloseEditorWhenCaptureStarts | `bool` | When enabled, the editor will shutdown when the capture starts |
| AdditionalCommandLineArguments | `FString` | Additional command line arguments to pass to the external process when capturing |
| InheritedCommandLineArguments | `FString` | Command line arguments inherited from this process |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UMovieSceneFolder

Reprents a folder used for organizing objects in tracks in a movie scene.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FolderName | `FName` | The name of this folder. |
| ChildFolders | `TArray < UMovieSceneFolder * >` | The folders contained by this folder. |
| ChildMasterTracks | `TArray < UMovieSceneTrack * >` | The master tracks contained by this folder. |
| ChildObjectBindingStrings | `TArray < FString >` | The guid strings used to serialize the guids for the object bindings contained by this folder. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

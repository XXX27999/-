# UInterpTrackDirector

## Parents

- [UInterpTrack](./UInterpTrack.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CutTrack | `TArray < struct FDirectorTrackCut >` | Array of cuts between cameras. |
| bSimulateCameraCutsOnClients | `uint32` | True to allow clients to simulate their own camera cuts.  Can help with latency-induced timing issues. |
| PreviewCamera | `ACameraActor *` | The camera actor which the track is currently focused on. Only valid if this track or it's group is selected |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

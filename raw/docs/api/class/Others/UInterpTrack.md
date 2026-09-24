# UInterpTrack

## Parents

- [UObject](./UObject.md)
- FCurveEdInterface
- FInterpEdInputInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SubTracks | `TArray < UInterpTrack * >` | A list of subtracks that belong to this track |
| TrackInstClass | `TSubclassOf < UInterpTrackInst >` |  |
| ActiveCondition | `TEnumAsByte < enum ETrackActiveCondition >` | Sets the condition that must be met for this track to be enabled |
| TrackTitle | `FString` | Title of track type. |
| bOnePerGroup | `uint32` | Whether there may only be one of this track in an UInterpGroup. |
| bDirGroupOnly | `uint32` | If this track can only exist inside the Director group. |
| bDisableTrack | `uint32` | Whether or not this track should actually update the target actor. |
| bIsSelected | `uint32` | Whether or not this track is selected in the editor. |
| bIsAnimControlTrack | `uint32` | If true, the  AActor  this track is working on will have BeginAnimControlFinishAnimControl called on it. |
| bSubTrackOnly | `uint32` | If this track can only exist as a sub track. |
| bVisible | `uint32` | Whether or not this track is visible in the editor. |
| bIsRecording | `uint32` | Whether or not this track is recording in the editor. |
| SubTrackGroups | `TArray < struct FSubTrackGroup >` | A list of subtrack groups (for editor UI organization only) |
| SupportedSubTracks | `TArray < struct FSupportedSubTrackInfo >` | A list of supported tracks that can be a subtrack of this track. |
| TrackIcon | `UTexture2D *` |  |
| bIsCollapsed | `uint32` | If this track is collapsed. (Only applies  to tracks with subtracks). |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

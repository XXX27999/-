# FSubTrackGroup

A small structure holding data for grouping subtracks. (For UI drawing purposes)

## Fields

| Name | Type | Description |
| --- | --- | --- |
| GroupName | `FString` | Name of the subtrack  group |
| TrackIndices | `TArray < int32 >` | Indices to tracks in the parent track subtrack array. |
| bIsCollapsed | `uint32` | If this group is collapsed |
| bIsSelected | `uint32` | If this group is selected |

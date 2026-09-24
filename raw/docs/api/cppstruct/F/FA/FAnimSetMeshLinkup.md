# FAnimSetMeshLinkup

This is a mapping table between each bone in a particular skeletal mesh and the tracks of this animation set.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BoneToTrackTable | `TArray < int32 >` | Mapping table. Size must be same as size of SkelMesh reference skeleton.<br>	  No index should be more than the number of tracks in this AnimSet.<br>	  -1 indicates no track for this bone - will use reference pose instead. |

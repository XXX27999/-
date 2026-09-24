# FSkeletonToMeshLinkup

This is a mapping table between bone in a particular skeletal mesh and bone of this skeleton set.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SkeletonToMeshTable | `TArray < int32 >` | Mapping table. Size must be same as size of bone tree (not Mesh Ref Pose).<br>	  No index should be more than the number of bones in this skeleton<br>	  -1 indicates no match for this bone - will be ignored. |
| MeshToSkeletonTable | `TArray < int32 >` | Mapping table. Size must be same as size of ref pose (not bone tree).<br>	  No index should be more than the number of bones in this skeletalmesh<br>	  -1 indicates no match for this bone - will be ignored. |

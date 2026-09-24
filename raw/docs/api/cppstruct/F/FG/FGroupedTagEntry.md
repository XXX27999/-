# FGroupedTagEntry

Grouped Tag Entry - Stores tags for a single category group

## Fields

| Name | Type | Description |
| --- | --- | --- |
| GroupName | `FName` | Group name (e.g. "StreamingType", "LODLevel") |
| Tags | `TArray < FName >` | Tags in this group |
| bOverrideStaticMeshTags | `bool` | Component-local flag: this group overrides the same StaticMesh tag group, even when Tags is empty. |

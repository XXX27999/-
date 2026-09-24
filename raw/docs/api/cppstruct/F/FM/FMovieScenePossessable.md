# FMovieScenePossessable

MovieScenePossessable is a "typed slot" used to allow the MovieScene to control an already-existing object

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Guid | [FGuid](../FG/FGuid.md) | Unique identifier of the possessable object. |
| Name | `FString` | Name label for this slot |
| PossessedObjectClass | `UClass *` | Type of the object we'll be possessing |
| ParentGuid | [FGuid](../FG/FGuid.md) | GUID relating to this possessable's parent, if applicable. |

# FMovieSceneSpawnable

MovieSceneSpawnable describes an object that can be spawned for this MovieScene

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Guid | [FGuid](../FG/FGuid.md) | Unique identifier of the spawnable object. |
| Name | `FString` | Name label |
| ObjectTemplate | `UObject *` |  |
| ChildPossessables | `TArray < FGuid >` | Set of GUIDs to possessable object bindings that are bound to an object inside this spawnable |
| Ownership | [ESpawnOwnership](../../../cppenum/E/ES/ESpawnOwnership.md) | Property indicating where ownership responsibility for this object lies |
| GeneratedClass_DEPRECATED | `UClass *` | Deprecated generated class |

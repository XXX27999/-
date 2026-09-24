# FMovieSceneObjectBindingID

Persistent identifier to a specific object binding within a sequence hierarchy.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SequenceID | `int32` | Sequence ID stored as an int32 so that it can be used in the blueprint VM |
| Space | [EMovieSceneObjectBindingSpace](../../../cppenum/E/EM/EMovieSceneObjectBindingSpace.md) | The binding's resolution space |
| Guid | [FGuid](../FG/FGuid.md) | Identifier for the object binding within the sequence |

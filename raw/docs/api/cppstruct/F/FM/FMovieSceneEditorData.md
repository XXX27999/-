# FMovieSceneEditorData

Editor only data that needs to be saved between sessions for editing but has no runtime purpose

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ExpansionStates | `TMap < FString , FMovieSceneExpansionState >` | Map of node path -> expansion state. |
| WorkingRange | [FFloatRange](../FF/FFloatRange.md) | User-defined working range in which the entire sequence should reside. |
| ViewRange | [FFloatRange](../FF/FFloatRange.md) | The last view-range that the user was observing |

# FMovieSceneTrackCompilationParams

Movie scene compilation parameters. Serialized items contribute to a compiled template's cached hash

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bForEditorPreview | `bool` | Whether we're generating for an editor preview, or for efficient runtime evaluation |
| bDuringBlueprintCompile | `bool` | Whether we're generating during a blueprint compile. As such, UObject types may not have been fully loaded. |

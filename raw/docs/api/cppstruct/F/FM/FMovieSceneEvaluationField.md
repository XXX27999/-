# FMovieSceneEvaluationField

Memory layout optimized primarily for speed of searching the applicable ranges

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Ranges | `TArray < FFloatRange >` | Ranges stored separately for fast (cache efficient) lookup. Each index has a corresponding entry in FMovieSceneEvaluationField::Groups. |
| Groups | `TArray < FMovieSceneEvaluationGroup >` | Groups that store segment pointers for each of the above ranges. Each index has a corresponding entry in FMovieSceneEvaluationField::Ranges. |
| MetaData | `TArray < FMovieSceneEvaluationMetaData >` | Meta data that maps to entries in the 'Ranges' array. |

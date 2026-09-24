# FMovieSceneEvaluationTemplate

Template that is used for efficient runtime evaluation of a movie scene sequence. Potentially serialized into the asset.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Tracks | `TMap < uint32 , FMovieSceneEvaluationTrack >` | Map of evaluation tracks from identifier to track |
| EvaluationField | [FMovieSceneEvaluationField](./FMovieSceneEvaluationField.md) | Evaluation field for efficient runtime evaluation |
| Hierarchy | [FMovieSceneSequenceHierarchy](./FMovieSceneSequenceHierarchy.md) | Map of all sequences found in this template (recursively) |
| TemplateLedger | [FMovieSceneTemplateGenerationLedger](./FMovieSceneTemplateGenerationLedger.md) |  |
| bHasLegacyTrackInstances | `uint32` | When set, this template contains legacy track instances that require the initialization of a legacy sequence instance |
| bKeepStaleTracks | `uint32` | Primarily used in editor to keep stale tracks around during template regeneration to ensure we can call OnEndEvaluation on them. |

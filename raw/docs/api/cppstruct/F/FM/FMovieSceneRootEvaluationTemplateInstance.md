# FMovieSceneRootEvaluationTemplateInstance

Root evaluation template instance used to play back any sequence

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DirectorInstances | `TMap < FMovieSceneSequenceID , UObject * >` | Map of director instances by sequence ID. Kept alive by this map assuming this struct is reference collected |

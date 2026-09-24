# FSectionEvaluationData

Evaluation data that specifies information about what to evaluate for a given template

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ImplIndex | `int32` | The implementation index we should evaluate (index into FMovieSceneEvaluationTrack::ChildTemplates) |
| ForcedTime | `float` | A forced time to evaluate this section at |
| Flags | [ESectionEvaluationFlags](../../../cppenum/E/ES/ESectionEvaluationFlags.md) | Additional flags for evaluating this section |

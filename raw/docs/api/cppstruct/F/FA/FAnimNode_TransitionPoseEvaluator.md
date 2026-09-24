# FAnimNode_TransitionPoseEvaluator

Animation data node for state machine transitions.
  Can be set to supply either the animation data from the transition source (From State) or the transition destination (To State).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DataSource | `TEnumAsByte < EEvaluatorDataSource :: Type >` |  |
| EvaluatorMode | `TEnumAsByte < EEvaluatorMode :: Mode >` |  |
| FramesToCachePose | `int32` |  |
| CacheFramesRemaining | `int32` |  |

# FMovieSceneEvaluationGroup

Holds segment pointers for all segments that are active for a given range of the sequence

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LUTIndices | `TArray < FMovieSceneEvaluationGroupLUTIndex >` | Array of indices that define all the flush groups in the range. |
| SegmentPtrLUT | `TArray < FMovieSceneEvaluationFieldSegmentPtr >` | A grouping of evaluation pointers that occur in this range of the sequence |

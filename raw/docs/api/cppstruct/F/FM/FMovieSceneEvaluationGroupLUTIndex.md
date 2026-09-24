# FMovieSceneEvaluationGroupLUTIndex

Lookup table index for a group of evaluation templates

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LUTOffset | `int32` | The offset within FMovieSceneEvaluationGroup::SegmentPtrLUT that this index starts |
| NumInitPtrs | `int32` | The number of initialization pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset. |
| NumEvalPtrs | `int32` | The number of evaluation pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset + NumInitPtrs. |

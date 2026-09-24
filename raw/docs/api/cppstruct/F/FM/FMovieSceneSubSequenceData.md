# FMovieSceneSubSequenceData

Sub sequence data that is stored within an evaluation template as a backreference to the originating sequence, and section

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Sequence | `UMovieSceneSequence *` | The sequence that the sub section references |
| SequenceKeyObject | `UObject *` | The key object that the sub section uses. Usually either the sequence or the section. |
| RootToSequenceTransform | [FMovieSceneSequenceTransform](./FMovieSceneSequenceTransform.md) | Transform that transforms a given time from the sequences outer space, to its authored space. |
| SourceSequenceSignature | [FGuid](../FG/FGuid.md) | Cached signature of the evaluation template |
| DeterministicSequenceID | [FMovieSceneSequenceID](./FMovieSceneSequenceID.md) | This sequence's deterministic sequence ID. Used in editor to reduce the risk of collisions on recompilation |
| PreRollRange | [FFloatRange](../FF/FFloatRange.md) | The sequence preroll range considering the start offset |
| PostRollRange | [FFloatRange](../FF/FFloatRange.md) | The sequence postroll range considering the start offset |
| HierarchicalBias | `int32` | The accumulated hierarchical bias of this sequence. Higher bias will take precedence |

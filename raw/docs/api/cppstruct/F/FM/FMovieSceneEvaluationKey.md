# FMovieSceneEvaluationKey

Keyable struct that represents a particular entity within an evaluation template (either a sectiontemplate or a track)

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SequenceID | [FMovieSceneSequenceID](./FMovieSceneSequenceID.md) | ID of the sequence that the entity is contained within |
| TrackIdentifier | [FMovieSceneTrackIdentifier](./FMovieSceneTrackIdentifier.md) | ID of the track this key relates to |
| SectionIdentifier | `uint32` | ID of the section this key relates to (or -1 where this key relates to a track) |

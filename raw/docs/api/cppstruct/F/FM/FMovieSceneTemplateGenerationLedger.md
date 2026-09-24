# FMovieSceneTemplateGenerationLedger

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LastTrackIdentifier | [FMovieSceneTrackIdentifier](./FMovieSceneTrackIdentifier.md) |  |
| TrackReferenceCounts | `TMap < FMovieSceneTrackIdentifier , int32 >` | Map of track identifiers to number of references within th template (generally 1, maybe >1 for shared tracks) |
| TrackSignatureToTrackIdentifier | `TMap < FGuid , FMovieSceneTrackIdentifiers >` | Map of track signature to array of track identifiers that it created |

# FMovieSceneTrackEvalOptions

Generic evaluation options for any track

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bCanEvaluateNearestSection | `uint32` | true when the value of bEvalNearestSection is to be considered for the track |
| bEvalNearestSection | `uint32` | When evaluating empty space on a track, will evaluate the last position of the previous section (if possible), or the first position of the next section, in that order of preference. |
| bEvaluateInPreroll | `uint32` | Evaluate this track as part of its parent sub-section's pre-roll, if applicable |
| bEvaluateInPostroll | `uint32` | Evaluate this track as part of its parent sub-section's post-roll, if applicable |
| bEvaluateNearestSection_DEPRECATED | `uint32` |  |

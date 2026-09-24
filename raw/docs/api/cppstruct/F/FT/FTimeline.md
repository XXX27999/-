# FTimeline

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LengthMode | `TEnumAsByte < ETimelineLengthMode >` | Specified how the timeline determines its own length (e.g. specified length, last keyframe) |
| Length | `float` | How long the timeline is, will stop or loop at the end |
| bLooping | `uint32` | Whether timeline should loop when it reaches the end, or stop |
| bReversePlayback | `uint32` | If playback should move the current position backwards instead of forwards |
| bPlaying | `uint32` | Are we currently playing (moving Position) |
| PlayRate | `float` | How fast we should play through the timeline |
| Position | `float` | Current position in the timeline |
| Events | `TArray < struct FTimelineEventEntry >` | Array of events that are fired at various times during the timeline |
| InterpVectors | `TArray < struct FTimelineVectorTrack >` | Array of vector interpolations performed during the timeline |
| InterpFloats | `TArray < struct FTimelineFloatTrack >` | Array of float interpolations performed during the timeline |
| InterpLinearColors | `TArray < struct FTimelineLinearColorTrack >` | Array of linear color interpolations performed during the timeline |
| PropertySetObject | `TWeakObjectPtr < UObject >` | Optional. If set, Timeline will also set floatvector properties on this object using the PropertyName set in the tracks. |
| DirectionPropertyName | `FName` | Optional. If set, Timeline will also set ETimelineDirection property on PropertySetObject using the name. |
| DirectionProperty | `UProperty *` | Cached property pointer for setting timeline direction |

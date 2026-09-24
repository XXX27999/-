# FTimelineVectorTrack

Struct that contains one entry for each vector interpolation performed by the timeline

## Fields

| Name | Type | Description |
| --- | --- | --- |
| VectorCurve | `UCurveVector *` | Vector curve to be evaluated |
| TrackName | `FName` | Name of track, usually set in Timeline Editor. Used by SetInterpVectorCurve function. |
| VectorPropertyName | `FName` | Name of property that we should update from this curve |
| VectorProperty | `UStructProperty *` | Cached vector struct property pointer |

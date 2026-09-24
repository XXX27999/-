# FTimelineFloatTrack

Struct that contains one entry for each vector interpolation performed by the timeline

## Fields

| Name | Type | Description |
| --- | --- | --- |
| FloatCurve | `UCurveFloat *` | Float curve to be evaluated |
| TrackName | `FName` | Name of track, usually set in Timeline Editor. Used by SetInterpFloatCurve function. |
| FloatPropertyName | `FName` | Name of property that we should update from this curve |
| FloatProperty | `UFloatProperty *` | Cached float property pointer |

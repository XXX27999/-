# FTimelineLinearColorTrack

Struct that contains one entry for each linear color interpolation performed by the timeline

## Fields

| Name | Type | Description |
| --- | --- | --- |
| LinearColorCurve | `UCurveLinearColor *` | Float curve to be evaluated |
| TrackName | `FName` | Name of track, usually set in Timeline Editor. Used by SetInterpLinearColorCurve function. |
| LinearColorPropertyName | `FName` | Name of property that we should update from this curve |
| LinearColorProperty | `UStructProperty *` | Cached linear color struct property pointer |

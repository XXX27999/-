# FBaseAttenuationSettings

Base class for attenuation settings.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DistanceAlgorithm | [EAttenuationDistanceModel](../../../cppenum/E/EA/EAttenuationDistanceModel.md) | The type of attenuation as a function of distance to use. |
| CustomAttenuationCurve | [FRuntimeFloatCurve](../FR/FRuntimeFloatCurve.md) | The custom volume attenuation curve to use. |
| AttenuationShape | `TEnumAsByte < enum EAttenuationShape :: Type >` | The shape of the non-custom attenuation method. |
| dBAttenuationAtMax | `float` | The attenuation volume at maximum distance in decibels, used for natural attenuation method. |
| AttenuationShapeExtents | [FVector](../FV/FVector.md) | The dimensions to use for the attenuation shape. Interpretation of the values differ per shape. |
| ConeOffset | `float` | The distance back from the sound's origin to begin the cone when using the cone attenuation shape. |
| FalloffDistance | `float` | The distance over which volume attenuation occurs. |

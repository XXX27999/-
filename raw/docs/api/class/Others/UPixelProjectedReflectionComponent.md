# UPixelProjectedReflectionComponent

UPixelProjectedReflectionComponent

## Parents

- [USceneCaptureComponent](./USceneCaptureComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PreviewBox | `UBoxComponent *` |  |
| NormalDistortionStrength | `float` | Controls the strength of normals when distorting the planar reflection. |
| SkyDistanceFadeoutStart | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| SkyDistanceFadeoutEnd | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| DistanceFromPlaneFadeStart_DEPRECATED | `float` |  |
| DistanceFromPlaneFadeEnd_DEPRECATED | `float` |  |
| DistanceFromPlaneFadeoutStart | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| DistanceFromPlaneFadeoutEnd | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| AngleFromPlaneFadeStart | `float` | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |
| AngleFromPlaneFadeEnd | `float` | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |
| HeightAdjustmentVolumes | `TArray < APixelProjectedReflectionHeightAdjustmentVolume * >` |  |
| VisibilityVolumes | `TArray < APixelProjectedReflectionVisibilityVolume * >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

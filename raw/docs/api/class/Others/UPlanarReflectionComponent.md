# UPlanarReflectionComponent

UPlanarReflectionComponent

## Parents

- [USceneCaptureComponent](./USceneCaptureComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PreviewBox | `UBoxComponent *` |  |
| NormalDistortionStrength | `float` | Controls the strength of normals when distorting the planar reflection. |
| PrefilterRoughnessY | `float` | The vertical roughness value to prefilter the planar reflection texture with, useful for hiding low resolution.  Larger values have larger GPU cost. |
| PrefilterRoughnessDistanceY | `float` | The vertical distance at which the prefilter roughness value will be achieved. |
| ScreenPercentage | `int32` | Downsample percent, can be used to reduce GPU time rendering the planar reflection. |
| ExtraFOV | `float` | Additional FOV used when rendering to the reflection texture.<br>	  This is useful when normal distortion is causing reads outside the reflection texture.<br>	  Larger values increase rendering thread and GPU cost, as more objects and triangles have to be rendered into the planar reflection. |
| DistanceFromPlaneFadeStart_DEPRECATED | `float` |  |
| DistanceFromPlaneFadeEnd_DEPRECATED | `float` |  |
| DistanceFromPlaneFadeoutStart | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| DistanceFromPlaneFadeoutEnd | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| AngleFromPlaneFadeStart | `float` | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |
| AngleFromPlaneFadeEnd | `float` | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |
| bRenderSceneTwoSided | `bool` | Whether to render the scene as two-sided, which can be useful to hide artifacts where normal distortion would read 'under' an object that has been clipped by the reflection plane.<br>	  With this setting enabled, the backfaces of a mesh would be displayed in the clipped region instead of the background which is potentially a bright sky.<br>	  Be sure to add the water plane to HiddenActors if enabling this, as the water plane will now block the reflection. |
| bBlurHorizontal | `bool` | Whether to blur along horizontal direction |
| PrefilterRoughnessX | `float` | The horizontal roughness value to prefilter the planar reflection texture with, useful for hiding low resolution.  Larger values have larger GPU cost. |
| PrefilterRoughnessDistanceX | `float` | The horizontal distance at which the prefilter roughness value will be achieved. |
| PrefilterRoughnessLowerBound | `float` | The Roughness Threshold For Prefilter |
| ScreenSizeCullScale | `float` | The ScreenSize Cull Scale |
| FrustumOptim | `bool` | Frustum Cull Range Optimization |
| NoReflectionShadow | `bool` | Do Not Render Shadow for PlanarRefelction |
| FrameBufferCache | `bool` | Enable FrameBuffer Cache Or Not |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

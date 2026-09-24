# USceneCaptureComponent2D

Used to capture a 'snapshot' of the scene from a single plane and feed it to a render target.

## Parents

- [USceneCaptureComponent](./USceneCaptureComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ProjectionType | `TEnumAsByte < ECameraProjectionMode :: Type >` |  |
| FOVAngle | `float` | Camera field of view (in degrees). |
| OrthoWidth | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| TextureTarget | `UTextureRenderTarget2D *` | Output render target of the scene capture that can be read in materals. |
| CaptureSource | `TEnumAsByte < enum ESceneCaptureSource >` |  |
| CompositeMode | `TEnumAsByte < enum ESceneCaptureCompositeMode >` | When enabled, the scene capture will composite into the render target instead of overwriting its contents. |
| PostProcessSettings | [FPostProcessSettings](../../cppstruct/F/FP/FPostProcessSettings.md) |  |
| PostProcessBlendWeight | `float` | Range (0.0, 1.0) where 0 indicates no effect, 1 indicates full effect. |
| bUseCustomProjectionMatrix | `bool` | Whether a custom projection matrix will be used during rendering. Use with caution. Does not currently affect culling |
| CustomProjectionMatrix | [FMatrix](../../cppstruct/F/FM/FMatrix.md) | The custom projection matrix to use |
| bEnableClipPlane | `bool` | Enables a clip plane while rendering the scene capture which is useful for portals.<br>	  The global clip plane must be enabled in the renderer project settings for this to work. |
| ClipPlaneBase | [FVector](../../cppstruct/F/FV/FVector.md) | Base position for the clip plane, can be any position on the plane. |
| ClipPlaneNormal | [FVector](../../cppstruct/F/FV/FVector.md) | Normal for the plane. |
| bCameraCutThisFrame | `uint32` | True if we did a camera cut this frame. Automatically reset to false at every capture.<br>	  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).<br>	  Similar to UPlayerCameraManager::bGameCameraCutThisFrame. |

## Functions

### AddOrUpdateBlendable

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendableObject | `TScriptInterface < IBlendableInterface >` |  |
| InWeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### CaptureScene

Render the scene to the texture target immediately.
	  This should not be used if bCaptureEveryFrame is enabled, or the scene capture will render redundantly.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

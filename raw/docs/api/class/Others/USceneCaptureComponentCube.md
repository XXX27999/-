# USceneCaptureComponentCube

Used to capture a 'snapshot' of the scene from a 6 planes and feed it to a render target.

## Parents

- [USceneCaptureComponent](./USceneCaptureComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TextureTarget | `UTextureRenderTargetCube *` | Temporary render target that can be used by the editor. |

## Functions

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

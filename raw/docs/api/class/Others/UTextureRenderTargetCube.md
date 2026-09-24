# UTextureRenderTargetCube

TextureRenderTargetCube

  Cube render target texture resource. This can be used as a target
  for rendering as well as rendered as a regular cube texture resource.

## Parents

- [UTextureRenderTarget](./UTextureRenderTarget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SizeX | `int32` | The width of the texture. |
| ClearColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | the color the texture is cleared to |
| OverrideFormat | `TEnumAsByte < enum EPixelFormat >` | The format of the texture data.<br>	 Normally the format is derived from bHDR, this allows code to set the format explicitly. |
| bHDR | `uint32` | Whether to support storing HDR values, which requires more memory. |
| bForceLinearGamma | `uint32` | True to force linear gamma space for this render target |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UStereoLayerComponent

A geometry layer within the stereo rendered viewport.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bLiveTexture | `uint32` | True if the stereo layer texture needs to update itself every frame(scene capture, video, etc.) |
| bSupportsDepth | `uint32` | True if the stereo layer needs to support depth intersections with the scene geometry, if available on the platform |
| bNoAlphaChannel | `uint32` | True if the texture should not use its own alpha channel (1.0 will be substituted) |
| Texture | `UTexture *` | Texture displayed on the stereo layer (is stereocopic textures are supported on the platfrom and more than one texture is provided, this will be the right eye) |
| LeftTexture | `UTexture *` | Texture displayed on the stereo layer for left eye, if stereoscopic textures are supported on the platform |
| bQuadPreserveTextureRatio | `uint32` | True if the quad should internally set it's Y value based on the set texture's dimensions |
| QuadSize | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Size of the rendered stereo layer quad |
| UVRect | [FBox2D](../../cppstruct/F/FB/FBox2D.md) | UV coordinates mapped to the quad face |
| CylinderRadius | `float` | Radial size of the rendered stereo layer cylinder |
| CylinderOverlayArc | `float` | Arc angle for the stereo layer cylinder |
| CylinderHeight | `int` | Height of the stereo layer cylinder |
| StereoLayerType | `TEnumAsByte < enum EStereoLayerType >` | Specifies how and where the quad is rendered to the screen |
| StereoLayerShape | `TEnumAsByte < enum EStereoLayerShape >` | Specifies which type of layer it is.  Note that some shapes will be supported only on certain platforms! |
| Priority | `int32` | Render priority among all stereo layers, higher priority render on top of lower priority |

## Functions

### SetTexture

Change the texture displayed on the stereo layer quad

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTexture | `UTexture *` |  |

**Return**

- Type: 
- Description: _None_

### GetTexture

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetQuadSize

Change the quad size. This is the unscaled height and width, before component scale is applied.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InQuadSize | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetQuadSize

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetUVRect

Change the UV coordinates mapped to the quad face

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InUVRect | [FBox2D](../../cppstruct/F/FB/FBox2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetUVRect

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPriority

Change the layer's render priority, higher priorities render on top of lower priorities

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPriority | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetPriority

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MarkTextureForUpdate

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

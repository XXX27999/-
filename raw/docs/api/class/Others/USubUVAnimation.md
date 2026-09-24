# USubUVAnimation

SubUV animation asset, which caches bounding geometry for regions in the SubUVTexture with non-zero opacity.
  Particle emitters with a SubUV module which use this asset leverage the optimal bounding geometry to reduce overdraw.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SubUVTexture | `UTexture2D *` | Texture to generate bounding geometry from. |
| SubImages_Horizontal | `int32` | The number of sub-images horizontally in the texture |
| SubImages_Vertical | `int32` | The number of sub-images vertically in the texture |
| BoundingMode | `TEnumAsByte < enum ESubUVBoundingVertexCount >` | More bounding vertices results in reduced overdraw, but adds more triangle overhead.<br>	  The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,<br>	  and when the particles using the texture will be few and large. |
| OpacitySourceMode | `TEnumAsByte < enum EOpacitySourceMode >` |  |
| AlphaThreshold | `float` | Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.<br>	  Raising this threshold slightly can reduce overdraw in particles using this animation asset. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

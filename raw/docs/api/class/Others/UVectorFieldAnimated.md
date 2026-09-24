# UVectorFieldAnimated

## Parents

- [UVectorField](./UVectorField.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` | The texture from which to create the vector field. |
| ConstructionOp | `TEnumAsByte < enum EVectorFieldConstructionOp >` | The operation used to construct the vector field. |
| VolumeSizeX | `int32` | The size of the volume. Valid sizes: 16, 32, 64. |
| VolumeSizeY | `int32` | The size of the volume. Valid sizes: 16, 32, 64. |
| VolumeSizeZ | `int32` | The size of the volume. Valid sizes: 16, 32, 64. |
| SubImagesX | `int32` | The number of horizontal subimages in the texture atlas. |
| SubImagesY | `int32` | The number of vertical subimages in the texture atlas. |
| FrameCount | `int32` | The number of frames in the atlas. |
| FramesPerSecond | `float` | The rate at which to interpolate between frames. |
| bLoop | `uint32` | Whether or not the simulation should loop. |
| NoiseField | `UVectorFieldStatic *` | A static vector field used to add noise. |
| NoiseScale | `float` | Scale to apply to vectors in the noise field. |
| NoiseMax | `float` | The maximum magnitude of noise vectors to apply. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# FTextureLODGroup

LOD settings for a single texture group.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Group | `TEnumAsByte < TextureGroup >` | Minimum LOD mip count below which the code won't bias. |
| LODBias | `int32` | Group LOD bias. |
| NumStreamedMips | `int32` | Number of mip-levels that can be streamed. -1 means all mips can stream. |
| MipGenSettings | `TEnumAsByte < TextureMipGenSettings >` | Defines how the the mip-map generation works, e.g. sharpening |
| MinLODSize | `int32` |  |
| MaxLODSize | `int32` |  |
| MinMagFilter | `FName` |  |
| MipFilter | `FName` |  |

# UMaterialExpressionTextureCoordinate

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CoordinateIndex | `int32` | Texture coordinate index |
| UTiling | `float` | Controls how much the texture tiles horizontally, by scaling the U component of the vertex UVs by the specified amount. |
| VTiling | `float` | Controls how much the texture tiles vertically, by scaling the V component of the vertex UVs by the specified amount. |
| UnMirrorU | `uint32` | Would like to unmirror U or V<br>	   - if the texture is mirrored and if you would like to undo mirroring for this texture sample, use this to unmirror |
| UnMirrorV | `uint32` |  |
| bForceFloatHP | `uint32` | When enabled, forces this TexCoord node to output float precision UV, preventing half-precision artifacts on mobile. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

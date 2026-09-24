# UMaterialExpressionSceneTexture

## Parents

- [UMaterialExpression](./UMaterialExpression.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Coordinates | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | UV in 0..1 range |
| SceneTextureId | `TEnumAsByte < ESceneTextureId >` | Which scene texture (screen aligned texture) we want to make a lookup into |
| bClampUVs | `bool` | Clamps texture coordinates to the range 0 to 1. Incurs a performance cost. |
| bFiltered | `bool` | Whether to use point sampled texture lookup (default) or using [bi-linear] filtered (can be slower, avoid faceted lock with distortions), some SceneTextures cannot be filtered |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

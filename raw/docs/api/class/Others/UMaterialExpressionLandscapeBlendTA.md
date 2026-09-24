# UMaterialExpressionLandscapeBlendTA

## Parents

- [UMaterialExpressionTerrainBlendBase](./UMaterialExpressionTerrainBlendBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UV | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| DiffuseTexture | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| NormalTexture | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| HeightTexture | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| RoughnessTexture | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| Layers | `TArray < FTerrainLayerTA >` |  |
| ConstCoordinate | `uint32` | only used if Coordinates is not hooked up |
| ExpressionGUID | [FGuid](../../cppstruct/F/FG/FGuid.md) | GUID that should be unique within the material, this is used for parameter renaming. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

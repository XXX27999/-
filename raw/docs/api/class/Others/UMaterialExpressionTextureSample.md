# UMaterialExpressionTextureSample

## Parents

- [UMaterialExpressionTextureBase](./UMaterialExpressionTextureBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Coordinates | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) |  |
| TextureObject | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Texture object input which overrides Texture if specified.<br>	  This only shows up in material functions and is used to implement texture parameters without actually putting the texture parameter in the function. |
| MipValue | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Meaning depends on MipValueMode, a single unit is one mip level |
| CoordinatesDX | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Enabled only if MipValueMode == TMVM_Derivative |
| CoordinatesDY | [FExpressionInput](../../cppstruct/F/FE/FExpressionInput.md) | Enabled only if MipValueMode == TMVM_Derivative |
| MipValueMode | `TEnumAsByte < enum ETextureMipValueMode >` | Defines how the MipValue property is applied to the texture lookup |
| SamplerSource | `TEnumAsByte < enum ESamplerSourceMode >` | Controls where the sampler for this texture lookup will come from.<br>	  Choose 'from texture asset' to make use of the UTexture addressing settings,<br>	  Otherwise use one of the global samplers, which will not consume a sampler slot.<br>	  This allows materials to use more than 16 unique textures on SM5 platforms. |
| ConstCoordinate | `uint32` | only used if Coordinates is not hooked up |
| ConstMipValue | `int32` | only used if MipValue is not hooked up |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

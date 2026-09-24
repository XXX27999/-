# UClipmapGenerateConfig

## Parents

- [UDataAsset](./UDataAsset.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TargetTexture | `UTexture2D *` |  |
| TargetClipmapTexture | `UClipmapTexture *` |  |
| ClipmapWetnessConfig | [FClipmapWetness](../../cppstruct/F/FC/FClipmapWetness.md) |  |
| FoliageHealthAndAbsorptionConfig | [FClipmapFoliageHealthAndAbsorption](../../cppstruct/F/FC/FClipmapFoliageHealthAndAbsorption.md) |  |
| LandscapeTintConfig | [FClipmapLandscapeTint](../../cppstruct/F/FC/FClipmapLandscapeTint.md) |  |
| BurshTintNum | `int32` |  |
| WeightBitsNum | `int32` |  |
| WeightMax | `int32` |  |

## Functions

### GenerateGChannel

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GenerateBAChannel

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GenerateCustomMips

统一的Mip后处理入口：先让引擎生成标准Mip，再后处理R通道(Max降采样)，可选BA通道(众数)

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

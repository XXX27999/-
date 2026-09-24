# UClipmapTexture

Runtime virtual texture UObject

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bSkipOneMip | `bool` |  |
| DisFirstMip | `float` |  |
| bUsePointSample | `bool` |  |
| bUseBorder | `bool` |  |
| TileSize | `int32` |  |
| FirstMipImageSize | `int32` |  |
| NumTile | `int32` |  |
| bUseCompressType | `bool` |  |
| NormalSetting | [FClipmapSetting](../../cppstruct/F/FC/FClipmapSetting.md) |  |
| CompressSetting | `TMap < FString , FClipmapSetting >` |  |
| bsRGB | `bool` |  |
| FileDDCPath | `FString` |  |
| ClipmapInfos | [FClipmapInfos](../../cppstruct/F/FC/FClipmapInfos.md) |  |
| CompressInfos | `TMap < FString , FClipmapInfos >` |  |
| DebugName | `FString` |  |
| HashNum | `uint32` |  |
| Owner | `UClipmapTextureComponent *` |  |
| OriginTexture | `UTexture2D *` |  |
| TargetTexture | `TSoftObjectPtr < UTexture2D >` |  |

## Functions

### CreateClipmapTargetTexture

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

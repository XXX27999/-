# UTexture2D

## Parents

- [UTexture](./UTexture.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StreamingIndex | `int32` | FStreamingTexture index used by the texture streaming system. |
| LevelIndex | `int32` | Level scope index of this texture. It is used to reduce the amount of lookup to map a texture to its level index.<br>	  Useful when building texture streaming data, as well as when filling the texture streamer with precomputed data.<br>      It relates to FStreamingTextureBuildInfo::TextureLevelIndex and also the index in ULevel::StreamingTextureGuids.<br>	  Default value of -1, indicates that the texture has an unknown index (not yet processed). At level load time,<br>	  -2 is also used to indicate that the texture has been processed but no entry were found in the level table.<br>	  After any of these processes, the LevelIndex is reset to INDEX_NONE. Making it ready for the next level task. |
| FirstResourceMemMip | `int32` | keep track of first mip level used for ResourceMem creation |
| bSuperSamplingMipBiasResponsive | `uint32` |  |
| PerTextureMipBias | `int32` |  |
| bUseForTerrainRVT | `uint32` |  |
| ImportedSize | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) | The imported size of the texture. Only valid on cooked builds when texture source is not<br>	  available. Access ONLY via the GetImportedSize() accessor! |
| ForceMipLevelsToBeResidentTimestamp | `double` | WorldSettings timestamp that tells the streamer to force all miplevels to be resident up until that time. |
| bTemporarilyDisableStreaming | `bool` | True if streaming is temporarily disabled so we can update subregions of this texture's resource<br>	without streaming clobbering it. Automatically cleared before saving. |
| bIsStreamable | `bool` | Whether the texture is currently streamable or not. |
| bHasStreamingUpdatePending | `uint32` | Whether some mips might be streamed soon. If false, the texture is not planned resolution will be stable. |
| bForceMiplevelsToBeResident | `uint32` | Override whether to fully stream even if texture hasn't been rendered. |
| bIgnoreStreamingMipBias | `uint32` | Ignores the streaming mip bias used to accommodate memory constraints. |
| bGlobalForceMipLevelsToBeResident | `uint32` | Global and serialized version of ForceMiplevelsToBeResident. |
| bIsTransient | `uint32` |  |
| AddressX | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the X axis. |
| AddressY | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the Y axis. |
| NotInlineMipCountOverride | `uint8` |  |
| bTryDownloadWhenSplit | `bool` |  |
| bHasBeenPaintedInEditor | `uint32` | Whether the texture has been painted in the editor. |

## Functions

### Blueprint_GetSizeX

Gets the X size of the texture, in pixels

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Blueprint_GetSizeY

Gets the Y size of the texture, in pixels

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RefreshBulkNotExistsMipCount

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

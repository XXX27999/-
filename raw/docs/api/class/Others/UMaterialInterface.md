# UMaterialInterface

## Parents

- [UObject](./UObject.md)
- IBlendableInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SubsurfaceProfile | `USubsurfaceProfile *` | SubsurfaceProfile, for Screen Space Subsurface Scattering |
| LightmassSettings | [FLightmassMaterialInterfaceSettings](../../cppstruct/F/FL/FLightmassMaterialInterfaceSettings.md) | The Lightmass settings for this object. |
| TextureStreamingData | `TArray < FMaterialTextureInfo >` | Data used by the texture streaming to know how each texture is sampled by the material. Sorted by names for quick access. |

## Functions

### GetBaseMaterial

Walks up parent chain and finds the base Material that this is an instance of. Just calls the virtual GetMaterial()

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPhysicalMaterial

Return a pointer to the physical material used by this material instance.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForceMipLevelsToBeResident

Force the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by this material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OverrideForceMiplevelsToBeResident | `bool` | - Whether to use (true) or ignore (false) the bForceMiplevelsToBeResidentValue parameter. |
| bForceMiplevelsToBeResidentValue | `bool` | - true forces all mips to stream in. false lets other factors decide what to do with the mips. |
| ForceDuration | `float` | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. Negative value turns it off. |
| CinematicTextureGroups | `int32` | - Bitfield indicating texture groups that should use extra high-resolution mips |

**Return**

- Type: 
- Description: _None_

### SetStreamingTextureMipOffset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMipOffset | `int32` |  |
| SizeLimited | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# ALandscape

## Parents

- [ALandscapeProxy](./ALandscapeProxy.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaterialIdUserSettings | [FMaterialIdUserSettings](../../cppstruct/F/FM/FMaterialIdUserSettings.md) |  |
| UseFarLandNormalDistance | `float` |  |
| BlendFarLandNormalDistance | `float` |  |
| FarLandVertexColorThreshold | `float` |  |
| FarLandVertexColorBlendThreshold | `float` |  |
| bUseLandscapeDeform | `bool` |  |
| bCanUseMaterialIdShading | `bool` |  |
| CurrentBiomesIndex | `int32` | Current selected biomes info |
| bTextureArrayDirty | `bool` |  |
| PaintingCustomWeightLayerIndex | `int32` |  |
| MatIdLayerVisibility | `TArray < bool >` |  |
| FarLandDiffuseTexture | `UTexture2D *` |  |
| FarLandNormalTexture | `UTexture2D *` |  |
| FarLandInfoDebug | `TMap < ULandscapeComponent * , FFarLandInfo >` |  |
| ExportSplatmapTexture | `UTexture2D *` |  |
| Platform | [EMyLandscapePlatfromConfiguration](../../cppenum/E/EM/EMyLandscapePlatfromConfiguration.md) |  |
| PCConfig | [FMyLandscapeConfigurationParams](../../cppstruct/F/FM/FMyLandscapeConfigurationParams.md) |  |
| MobileConfig | [FMyLandscapeConfigurationParams](../../cppstruct/F/FM/FMyLandscapeConfigurationParams.md) |  |

## Functions

### EnumerateLandscapePaintMatIDLayers

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Landscape | `ALandscapeProxy *` |  |

**Return**

- Type: 
- Description: _None_

### IsMaterialIDLandscape

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Landscape | `ALandscapeProxy *` |  |

**Return**

- Type: 
- Description: _None_

### SetLandscapeCorner

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SplitFarLandTextureForComponent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetFarLandTextureInfo

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GenerateSplatmapMip

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ExportWeightAsSplatmapMipEditor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BuildLandscapeStaticMesh

UFUNCTION(CallInEditor, Category = "Build Static Mesh", meta = (CallInEditor = "true"))

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

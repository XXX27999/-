# UTexture

## Parents

- [UObject](./UObject.md)
- IInterface_AssetUserData

## Variables

| Name | Type | Description |
| --- | --- | --- |
| LightingGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) | Unique ID for this material, used for caching during distributed lighting |
| LODBias | `int32` | --------------------------------------------------------------------------<br>	--------------------------------------------------------------------------<br>	 A bias to the index of the top mip level to use. |
| ExpectedQualityLimit | [FExpectedQuality](../../cppstruct/F/FE/FExpectedQuality.md) |  |
| NumCinematicMipLevels | `int32` | Number of mip-levels to use for cinematic quality. |
| SRGB | `uint32` | This should be unchecked if using alpha channels individually as masks. |
| bNotUsedInUltimateHighQuality | `uint32` |  |
| bNotUsedInHighQuality | `uint32` |  |
| bNotUsedInMediumQuality | `uint32` |  |
| bNotUsedInLowQuality | `uint32` |  |
| NeverStream | `uint32` |  |
| bNoTiling | `uint32` | If true, the RHI texture will be created using TexCreate_NoTiling |
| bUseCinematicMipLevels | `uint32` | Whether to use the extra cinematic quality mip-levels, when we're forcing mip-levels to be resident. |
| AssetUserData | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| CachedCombinedLODBias | `int32` | Cached combined group and texture LOD bias to use. |
| bAsyncResourceReleaseHasBeenStarted | `uint32` | Whether the async resource release process has already been kicked off or not |
| CompressionSettings | `TEnumAsByte < enum TextureCompressionSettings >` | Compression settings to use when building the texture. |
| Filter | `TEnumAsByte < enum TextureFilter >` | The texture filtering mode to use when sampling this texture. |
| LODGroup | `TEnumAsByte < enum TextureGroup >` | Texture group this texture belongs to |
| CrunchSetting | `TEnumAsByte < enum ETextureCrunchSetting >` |  |
| bOverrideCrunchCompressionAmount | `uint32` |  |
| CrunchCompressionAmount | `float` |  |
| bOverrideBasisCompressionAmount | `uint32` |  |
| BasisSetting | `TEnumAsByte < enum ETextureBasisSetting >` |  |
| BasisCompressionAmount | `float` |  |
| Source | [FTextureSource](../../cppstruct/F/FT/FTextureSource.md) | --------------------------------------------------------------------------<br>	-------------------------------------------------------------------------- |
| SourceFilePath_DEPRECATED | `FString` |  |
| AssetImportData | `UAssetImportData *` |  |
| AdjustBrightness | `float` | Static texture brightness adjustment (scales HSV value.)  (Non-destructive; Requires texture source art to be available.) |
| AdjustBrightnessCurve | `float` | Static texture curve adjustment (raises HSV value to the specified power.)  (Non-destructive; Requires texture source art to be available.) |
| AdjustVibrance | `float` | Static texture "vibrance" adjustment (0 - 1) (HSV saturation algorithm adjustment.)  (Non-destructive; Requires texture source art to be available.) |
| AdjustSaturation | `float` | Static texture saturation adjustment (scales HSV saturation.)  (Non-destructive; Requires texture source art to be available.) |
| AdjustRGBCurve | `float` | Static texture RGB curve adjustment (raises linear-space RGB color to the specified power.)  (Non-destructive; Requires texture source art to be available.) |
| AdjustHue | `float` | Static texture hue adjustment (0 - 360) (offsets HSV hue by value in degrees.)  (Non-destructive; Requires texture source art to be available.) |
| AdjustMinAlpha | `float` | Remaps the alpha to the specified minmax range, defines the new value of 0 (Non-destructive; Requires texture source art to be available.) |
| AdjustMaxAlpha | `float` | Remaps the alpha to the specified minmax range, defines the new value of 1 (Non-destructive; Requires texture source art to be available.) |
| CompressionNoAlpha | `uint32` | If enabled, the texture's alpha channel will be discarded during compression |
| CompressionNone | `uint32` |  |
| DeferCompression | `uint32` | If enabled, defer compression of the texture until save. |
| MaxTextureSize | `int32` | The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform, except HDR longlat cubemaps, which default to a resolution of 512. |
| MaxTextureSizeHD | `int32` |  |
| MaxTextureSizeWinOB | `int32` |  |
| MaxTextureSizePC | `int32` |  |
| CompressionQuality | `TEnumAsByte < enum ETextureCompressionQuality >` | The compression quality for generated textures. |
| bDitherMipMapAlpha | `uint32` | When true, the alpha channel of mip-maps and the base image are dithered for smooth LOD transitions. |
| AlphaCoverageThresholds | [FVector4](../../cppstruct/F/FV/FVector4.md) | Alpha values per channel to compare to when preserving alpha coverage. |
| bPreserveBorder | `uint32` | When true the texture's border will be preserved during mipmap generation. |
| bFlipGreenChannel | `uint32` | When true the texture's green channel will be inverted. This is useful for some normal maps. |
| bForcePVRTC4 | `uint32` | For DXT1 textures, setting this will cause the texture to be twice the size, but better looking, on iPhone |
| bUseASTCForCookTargetPlatform | `uint32` | Whether to use astc for cook target platform . |
| PowerOfTwoMode | `TEnumAsByte < enum ETexturePowerOfTwoSetting :: Type >` | How to pad the texture to a power of 2 size (if necessary) |
| PaddingColor | [FColor](../../cppstruct/F/FC/FColor.md) | The color used to pad the texture out if it is resized due to PowerOfTwoMode |
| bChromaKeyTexture | `bool` | Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black |
| ChromaKeyThreshold | `float` | The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match) |
| ChromaKeyColor | [FColor](../../cppstruct/F/FC/FColor.md) | The color that will be replaced with transparent black if chroma keying is enabled |
| MipGenSettings | `TEnumAsByte < enum TextureMipGenSettings >` | Per asset specific setting to define the mip-map generation properties like sharpening and kernel size. |
| bUseNewFilter_UE4 | `bool` | New Tex Mip Filter  Tex MaxSize Filter from UE5 |
| FloodFillByNearestThreshold | `float` | For masked texture which using alpha channel as the clip value, flood fill background zone RGB values with nearest valid pixels.<br>	  Mask texture should setup this to actual clip value to avoid polluting color in high mip level.<br>	  All pixels has lower alpha value than this threshold will be filled by nearest valid pixel(which has higher value than threshold). Value of 0.0 means no flood fill process at all. |
| CompositeTexture | `UTexture *` | Can be defined to modify the roughness based on the normal map variation (mostly from mip maps).<br>	  MaxAlpha comes in handy to define a base roughness if no source alpha was there.<br>	  Make sure the normal map has at least as many mips as this texture. |
| CompositeTextureMode | `TEnumAsByte < enum ECompositeTextureMode >` | defines how the CompositeTexture is applied, e.g. CTM_RoughnessFromNormalAlpha |
| CompositePower | `float` | default 1, high values result in a stronger effect e.g 1, 2, 4, 8<br>	  this is no slider because the texture update would not be fast enough |
| bIsCookingHDTexture | `bool` |  |
| bIsCookingPCTexture | `bool` |  |
| bUseLegacyGamma | `uint32` | A flag for using the simplified legacy gamma space e.g pow(color,12.2) for converting from FColor to FLinearColor, if we're doing sRGB. |
| bKeepSourceDataWhenCookingUGCEditor | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

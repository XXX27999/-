# FMaterialProxySettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| TextureSizingType | `TEnumAsByte < ETextureSizingType >` |  |
| GutterSpace | `float` |  |
| SamplingQuality | [EMaterialProxySmaplingQuality](../../../cppenum/E/EM/EMaterialProxySmaplingQuality.md) | Texture Sampling Quality for our parameterizer |
| UVStrech | [EUVStrech](../../../cppenum/E/EU/EUVStrech.md) | The max amount of uv stretch allowed |
| bSplitProxyMaterialBasedOnType | `bool` | Enabling this settings would split split non-opaques and opaque types |
| bUseTangentSpace | `bool` |  |
| bNormalMap | `bool` |  |
| bMetallicMap | `bool` |  |
| MetallicConstant | `float` |  |
| bRoughnessMap | `bool` |  |
| RoughnessConstant | `float` |  |
| bSpecularMap | `bool` |  |
| SpecularConstant | `float` |  |
| bEmissiveMap | `bool` |  |
| bOpacityMap | `bool` |  |
| OpacityConstant | `float` |  |
| AOConstant_DEPRECATED | `float` |  |
| bOpacityMaskMap | `bool` |  |
| OpacityMaskConstant | `float` |  |
| bAmbientOcclusionMap | `bool` |  |
| AmbientOcclusionConstant | `float` |  |
| DiffuseTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| NormalTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| MetallicTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| RoughnessTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| SpecularTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| EmissiveTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| OpacityTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| OpacityMaskTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| AmbientOcclusionTextureSize | [FIntPoint](../FI/FIntPoint.md) |  |
| MaterialMergeType | `TEnumAsByte < EMaterialMergeType >` |  |
| BlendMode | `TEnumAsByte < EBlendMode >` |  |

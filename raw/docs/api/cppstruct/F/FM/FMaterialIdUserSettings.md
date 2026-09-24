# FMaterialIdUserSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| BiomesInfoObjectList | `TArray < ULandscapeBiomesInfoObject * >` | List of BiomesInfoObject used by this Landscape Actor |
| CustomWeightAllocations | `TArray < FLandscapeCustomWeightAllocation >` |  |
| bEditMatIDProperty | `bool` |  |
| bUseOneShaderMap | `bool` |  |
| HoleIndex | `uint8` |  |
| NoiseTexture | `UTexture2D *` | Noise Texture applied when sample splatmap |
| LandscapeCorner | [FVector2D](../FV/FVector2D.md) |  |
| NoiseMultiplier | `float` | Larger the value is, larger the UVOffset will applied when sample splatmap |
| NoiseTiling | [FVector2D](../FV/FVector2D.md) |  |
| NoiseLerpPercentFromEdge | `float` | Starting percentage of lerp from Edge to center of the component, to avoid shifted UV go over the component. |
| DiffuseArrayInfo | [FTextureArrayInfo](../FT/FTextureArrayInfo.md) | Diffuse texture array used as base color to render the landscape |
| NormalArrayInfo | [FTextureArrayInfo](../FT/FTextureArrayInfo.md) | Normalmap texture array used as base color to render the landscape |
| LayerInfoToAllocInfoMap | `TMap < ULandscapeLayerInfoObject * , FMaterialIdLayerAllocInfo >` | Valid LayerInfoObject to MaterialIdAllocInfo map. |
| MaterialIdLayerCount | `int32` | MaterialId Layer Count, fixed with 2, align SJZ |
| CustomWeightPaintingColor | [FLinearColor](../FL/FLinearColor.md) |  |
| DummyLayerInfoRemap | `TMap < FName , ULandscapeLayerInfoObject * >` |  |
| CustomWeightConfig | `UCustomWeightConfig *` |  |
| FallbackLayerConfig | `UMatIDFallbackConfig *` |  |

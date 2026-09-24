# FClipmapLandscapeTint

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TintConfig | [FClipmapGenOneOriChannel](./FClipmapGenOneOriChannel.md) |  |
| IntensityConfig | [FClipmapGenOneOriChannel](./FClipmapGenOneOriChannel.md) |  |
| DepthCurve | `UCurveLinearColor *` |  |
| bHasBrushTint | `bool` |  |
| TintLayerName | `FName` |  |
| BrushPresetColors | `TArray < FLinearColor >` | 笔刷预设色列表，美术在此配置可选的染色颜色，地形笔刷UI会提供下拉框选择 |
| MaxWaterNum | `int32` |  |
| TintMaterialInstance | `UMaterialInstanceConstant *` | 染色完成后自动设置LutNum的材质实例（可选，配置后每次生成染色会自动写入LutNum参数） |
| TintLutNumParamName | `FName` | 材质实例上的LutNum标量参数名 |
| WaterTintLutNumParamName | `FName` |  |
| LandscapeTintLUT | `UTexture2D *` |  |
| CustomNodeCode | `FString` |  |

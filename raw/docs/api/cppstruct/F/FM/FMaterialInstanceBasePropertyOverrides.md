# FMaterialInstanceBasePropertyOverrides

Properties from the base material that can be overridden in material instances.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bOverride_OpacityMaskClipValue | `bool` | Enables override of the opacity mask clip value. |
| bOverride_BlendMode | `bool` | Enables override of the blend mode. |
| bOverride_ShadingModel | `bool` | Enables override of the shading model. |
| bOverride_DitheredLODTransition | `bool` | Enables override of the dithered LOD transition property. |
| bOverride_ForceOpaqueLevelPointIndirectLighting | `bool` |  |
| bOverride_CastDynamicShadowAsMasked | `bool` | Enables override of whether to shadow using masked opacity on translucent materials. |
| bOverride_TwoSided | `bool` | Enables override of the two sided property. |
| bOverride_UsedWithTranslucentGI | `bool` | [SurfelGI - brainfkli ADD]<br>	  Indicates that the material and its instances can be affected by GI in translucent blend mode. |
| bOverride_ShadingRate | `bool` | Enables override of the shading rate. |
| OpacityMaskClipValue | `float` | If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue. |
| BlendMode | `TEnumAsByte < EBlendMode >` | The blend mode |
| ShadingModel | `TEnumAsByte < EMaterialShadingModel >` | The shading model |
| TwoSided | `uint32` | Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces. |
| DitheredLODTransition | `uint32` | Whether the material should support a dithered LOD transition when used with the foliage system. |
| ForceOpaqueLevelPointIndirectLighting | `uint32` |  |
| bCastDynamicShadowAsMasked | `uint32` | Whether the material should cast shadows as masked even though it has a translucent blend mode. |
| bUsedWithTranslucentGI | `uint32` | [SurfelGI - brainfkli ADD]<br>	  Indicates that the material and its instances can be affected by GI in translucent blend mode. |
| ShadingRate | `TEnumAsByte < EMaterialShadingRate >` | The shading rate |

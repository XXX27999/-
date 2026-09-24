# FLightmassMaterialInterfaceSettings

UMaterial interface settings for Lightmass

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bCastShadowAsMasked | `uint32` | If true, forces translucency to cast static shadows as if the material were masked. |
| EmissiveBoost | `float` | Scales the emissive contribution of this material to static lighting. |
| DiffuseBoost | `float` | Scales the diffuse contribution of this material to static lighting. |
| ExportResolutionScale | `float` | Scales the resolution that this material's attributes were exported at.<br>	  This is useful for increasing material resolution when details are needed. |
| bOverrideCastShadowAsMasked | `uint32` | Boolean override flags - only used in MaterialInstance cases.<br>	 If true, override the bCastShadowAsMasked setting of the parent material. |
| bOverrideEmissiveBoost | `uint32` | If true, override the emissive boost setting of the parent material. |
| bOverrideDiffuseBoost | `uint32` | If true, override the diffuse boost setting of the parent material. |
| bOverrideExportResolutionScale | `uint32` | If true, override the export resolution scale setting of the parent material. |

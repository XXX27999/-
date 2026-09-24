# FFontOutlineSettings

Settings for applying an outline to a font

## Fields

| Name | Type | Description |
| --- | --- | --- |
| OutlineSize | `int32` | Size of the outline in slate units (at 1.0 font scale this unit is a pixel) |
| OutlineMaterial | `UObject *` | Optional material to apply to the outline |
| OutlineColor | [FLinearColor](../FL/FLinearColor.md) | The color of the outline for any character in this font |
| bSeparateFillAlpha | `bool` | If checked, the outline will be completely translucent where the filled area will be.  This allows for a separate fill alpha value<br>	  The trade off when enabling this is slightly worse quality for completely opaque fills where the inner outline border meets the fill area |

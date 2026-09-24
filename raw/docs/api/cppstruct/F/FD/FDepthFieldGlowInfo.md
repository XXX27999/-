# FDepthFieldGlowInfo

info for glow when using depth field rendering

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bEnableGlow | `uint32` | whether to turn on the outline glow (depth field fonts only) |
| GlowColor | [FLinearColor](../FL/FLinearColor.md) | base color to use for the glow |
| GlowOuterRadius | [FVector2D](../FV/FVector2D.md) | if bEnableGlow, outline glow outer radius (0 to 1, 0.5 is edge of character silhouette)<br>	  glow influence will be 0 at GlowOuterRadius.X and 1 at GlowOuterRadius.Y |
| GlowInnerRadius | [FVector2D](../FV/FVector2D.md) | if bEnableGlow, outline glow inner radius (0 to 1, 0.5 is edge of character silhouette)<br>	  glow influence will be 1 at GlowInnerRadius.X and 0 at GlowInnerRadius.Y |

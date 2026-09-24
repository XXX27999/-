# FIdeaBakingPrimitiveSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| IdeaMaterialDiffuse | `float` | When baking, use this diffuse calculate reflection fro sun related lighting, not use really material's diffuse texture |
| LightmapBoost | `float` | Scales the lightmap result of idea baking. |
| DiscardPixelFrontfaceFactor | `float` | When ray intersected surface frontface counter lower DiscardPixelFrontfaceFactor  NumRays, the pixel will be discard. Larger value will help decrease black edge artifact.<br>	 But if scene has two side surface(like flags), will cause another artifact, pixels behind back side of flags maybe discarded wrong. |
| SunIntensity | `float` | By luciuszhang:<br>	 Control the sun intensity from the sky, unit is cdm^2, default value is 1.0. |
| LocalLightsAffectMaxDistance | `float` | By luciuszhang:<br>	 Control the sun indirect intensity from the sky, unit is cdm^2, default value is 1.0. |

# FLightmassLightSettings

Per-light settings for Lightmass

## Fields

| Name | Type | Description |
| --- | --- | --- |
| IndirectLightingSaturation | `float` | 0 will be completely desaturated, 1 will be unchanged |
| ShadowExponent | `float` | Controls the falloff of shadow penumbras |
| bUseAreaShadowsForStationaryLight | `bool` | Whether to use area shadows for stationary light precomputed shadowmaps.<br>	  Area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp. |

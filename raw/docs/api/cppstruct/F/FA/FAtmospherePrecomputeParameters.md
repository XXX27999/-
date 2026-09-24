# FAtmospherePrecomputeParameters

Structure storing Data for pre-computation

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DensityHeight | `float` | Rayleigh scattering density height scale, ranges from [0...1] |
| DecayHeight_DEPRECATED | `float` |  |
| MaxScatteringOrder | `int32` | Maximum scattering order |
| TransmittanceTexWidth | `int32` | Transmittance Texture Width |
| TransmittanceTexHeight | `int32` | Transmittance Texture Height |
| IrradianceTexWidth | `int32` | Irradiance Texture Width |
| IrradianceTexHeight | `int32` | Irradiance Texture Height |
| InscatterAltitudeSampleNum | `int32` | Number of different altitudes at which to sample inscatter color (size of 3D texture Z dimension) |
| InscatterMuNum | `int32` | Inscatter Texture Height |
| InscatterMuSNum | `int32` | Inscatter Texture Width |
| InscatterNuNum | `int32` | Inscatter Texture Width |

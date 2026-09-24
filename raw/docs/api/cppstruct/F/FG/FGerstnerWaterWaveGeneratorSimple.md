# FGerstnerWaterWaveGeneratorSimple

## Fields

| Name | Type | Description |
| --- | --- | --- |
| NumWaves | `int32` |  |
| Seed | `int32` |  |
| Randomness | `float` |  |
| MinWavelength | `float` |  |
| MaxWavelength | `float` |  |
| WavelengthFalloff | `float` |  |
| MinAmplitude | `float` |  |
| MaxAmplitude | `float` |  |
| AmplitudeFalloff | `float` |  |
| DirectionAngularSpreadDeg | `float` | UPROPERTY(EditAnywhere, BlueprintReadWrite, meta = (DisplayName = "Dominant Wind Angle", Category = "Directions", UIMin = -180, ClampMin = -180, UIMax = 180, ClampMax = 180, Units = deg))<br>		float GerstnerAngleDeg = 0.0f; |
| SmallWaveSteepness | `float` |  |
| LargeWaveSteepness | `float` |  |
| SteepnessFalloff | `float` |  |
| WaveSpeed | `float` |  |
| Gerstnersamplesize | `float` |  |
| GerstnerParallelness | `float` |  |
| GerstnerWaves | `TArray < FGerstnerWave >` |  |

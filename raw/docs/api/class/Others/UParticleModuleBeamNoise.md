# UParticleModuleBeamNoise

## Parents

- UParticleModuleBeamBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bLowFreq_Enabled | `uint32` | Is low frequency noise enabled. |
| Frequency | `int32` | The frequency of noise points. |
| Frequency_LowRange | `int32` | If not 0, then the frequency will select a random value in the range<br>	 		[Frequency_LowRange..Frequency] |
| NoiseRange | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The noise point ranges. |
| NoiseRangeScale | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | A scale factor that will be applied to the noise range. |
| bNRScaleEmitterTime | `uint32` | If true,  the NoiseRangeScale will be grabbed based on the emitter time.<br>	 	If false, the NoiseRangeScale will be grabbed based on the particle time. |
| NoiseSpeed | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The speed with which to move each noise point. |
| bSmooth | `uint32` | Whether the noise movement should be smooth or 'jerky'. |
| NoiseLockRadius | `float` | Default target-point information to use if the beam method is endpoint. |
| bNoiseLock | `uint32` | INTERNAL - Whether the noise points should be locked. |
| bOscillate | `uint32` | Whether the noise points should be oscillate. |
| NoiseLockTime | `float` | How long the  noise points should be locked - 0.0 indicates forever. |
| NoiseTension | `float` | The tension to apply to the tessellated noise line. |
| bUseNoiseTangents | `uint32` | If true, calculate tangents at each noise point. |
| NoiseTangentStrength | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The strength of noise tangents, if enabled. |
| NoiseTessellation | `int32` | The amount of tessellation between noise points. |
| bTargetNoise | `uint32` | Whether to apply noise to the target point (or end of line in distance mode...)<br>	 	If true, the beam could potentially 'leave' the target... |
| FrequencyDistance | `float` | The distance at which to deposit noise points.<br>	 	If 0.0, then use the static frequency value.<br>	 	If not, distribute noise points at the given distance, up to the static Frequency value.<br>	 	At that point, evenly distribute them along the beam. |
| bApplyNoiseScale | `uint32` | If true, apply the noise scale to the beam. |
| NoiseScale | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The scale factor to apply to noise range.<br>	 	The lookup value is determined by dividing the number of noise points present by the<br>	 	maximum number of noise points (Frequency). |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

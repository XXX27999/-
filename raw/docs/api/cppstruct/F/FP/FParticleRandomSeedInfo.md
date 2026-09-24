# FParticleRandomSeedInfo

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` | The name to expose to the placed instances for setting this seed |
| bGetSeedFromInstance | `uint32` | If true, the module will attempt to get the seed from the owner<br>	 	instance. If that fails, it will fall back to getting it from<br>	 	the RandomSeeds array. |
| bInstanceSeedIsIndex | `uint32` | If true, the seed value retrieved from the instance will be an<br>	 	index into the array of seeds. |
| bResetSeedOnEmitterLooping | `uint32` | If true, then reset the seed upon the emitter looping.<br>	 	For looping environmental effects this should likely be set to false to avoid<br>	 	a repeating pattern. |
| bRandomlySelectSeedArray | `uint32` | If true, then randomly select a seed entry from the RandomSeeds array |
| RandomSeeds | `TArray < int32 >` | The random seed values to utilize for the module.<br>	 	More than 1 means the instance will randomly select one. |

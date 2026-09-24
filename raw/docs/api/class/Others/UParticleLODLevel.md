# UParticleLODLevel

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Level | `int32` | The index value of the LOD level |
| bEnabled | `uint32` | True if the LOD level is enabled, meaning it should be updated and rendered. |
| RequiredModule | `UParticleModuleRequired *` | The required module for this LOD level |
| Modules | `TArray < UParticleModule * >` | An array of particle modules that contain the adjusted data for the LOD level |
| TypeDataModule | `UParticleModuleTypeDataBase *` |  |
| SpawnModule | `UParticleModuleSpawn *` | The SpawnRateBurst module - required by all emitters. |
| EventGenerator | `UParticleModuleEventGenerator *` | The optional EventGenerator module. |
| SpawningModules | `TArray < UParticleModuleSpawnBase * >` | SpawningModules - These are called to determine how many particles to spawn. |
| SpawnModules | `TArray < UParticleModule * >` | SpawnModules - These are called when particles are spawned. |
| UpdateModules | `TArray < UParticleModule * >` | UpdateModules - These are called when particles are updated. |
| OrbitModules | `TArray < UParticleModuleOrbit * >` | OrbitModules<br>	 	These are used to do offsets of the sprite from the particle location. |
| EventReceiverModules | `TArray < UParticleModuleEventReceiverBase * >` | Event receiver modules only! |
| ConvertedModules | `uint32` |  |
| PeakActiveParticles | `int32` |  |
| ActualPeakParticles | `int32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

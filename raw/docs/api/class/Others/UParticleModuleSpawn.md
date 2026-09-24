# UParticleModuleSpawn

## Parents

- [UParticleModuleSpawnBase](./UParticleModuleSpawnBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Rate | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The rate at which to spawn particles. |
| RateScale | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The scalar to apply to the rate. |
| ParticleBurstMethod | `TEnumAsByte < EParticleBurstMethod >` | The method to utilize when burst-emitting particles. |
| BurstList | `TArray < FParticleBurst >` | The array of burst entries. |
| BurstScale | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | Scale all burst entries by this amount. |
| bApplyGlobalSpawnRateScale | `uint32` | If true, the SpawnRate will be scaled by the global CVar r.EmitterSpawnRateScale |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

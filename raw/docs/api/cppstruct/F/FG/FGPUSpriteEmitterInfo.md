# FGPUSpriteEmitterInfo

The data needed by the runtime to simulate sprites.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| RequiredModule | `UParticleModuleRequired *` | The required module. Needed for now, but should be divorced from the runtime. |
| SpawnModule | `UParticleModuleSpawn *` | The spawn module. Needed for now, but should be divorced from the runtime. |
| SpawnPerUnitModule | `UParticleModuleSpawnPerUnit *` | The spawn-per-unit module. |
| SpawnModules | `TArray < UParticleModule * >` | List of spawn modules that must be evaluated at runtime. |
| LocalVectorField | [FGPUSpriteLocalVectorFieldInfo](./FGPUSpriteLocalVectorFieldInfo.md) | Local vector field info. |
| VectorFieldScale | [FFloatDistribution](../FF/FFloatDistribution.md) | Per-particle vector field scale. |
| DragCoefficient | [FFloatDistribution](../FF/FFloatDistribution.md) | Per-particle drag coefficient. |
| PointAttractorStrength | [FFloatDistribution](../FF/FFloatDistribution.md) | Point attractor strength over time. |
| Resilience | [FFloatDistribution](../FF/FFloatDistribution.md) | Damping factor applied to particle collisions. |
| ConstantAcceleration | [FVector](../FV/FVector.md) | Constant acceleration to apply to particles. |
| PointAttractorPosition | [FVector](../FV/FVector.md) | Point attractor position. |
| PointAttractorRadiusSq | `float` | Point attractor radius, squared. |
| OrbitOffsetBase | [FVector](../FV/FVector.md) | Amount by which to offset particles when they are spawned. |
| OrbitOffsetRange | [FVector](../FV/FVector.md) |  |
| InvMaxSize | [FVector2D](../FV/FVector2D.md) | One over the maximum size of a sprite particle. |
| InvRotationRateScale | `float` | The inverse scale to apply to rotation rate. |
| MaxLifetime | `float` | The maximum lifetime of particles in this emitter. |
| MaxParticleCount | `int32` | The maximum number of particles expected for this emitter. |
| ScreenAlignment | `TEnumAsByte < EParticleScreenAlignment >` | The method for aligning the particle based on the camera. |
| LockAxisFlag | `TEnumAsByte < EParticleAxisLock >` | The method for locking the particles to a particular axis. |
| bEnableCollision | `uint32` | If true, collisions are enabled for this emitter. |
| CollisionMode | `TEnumAsByte < EParticleCollisionMode :: Type >` |  |
| bRemoveHMDRoll | `uint32` | If true, removes the HMD view roll (e.g. in VR) |
| MinFacingCameraBlendDistance | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_Square |
| MaxFacingCameraBlendDistance | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_FacingCameraPosition |
| DynamicColor | [FRawDistributionVector](../FR/FRawDistributionVector.md) | Dynamic color scale from the ColorOverLife module. |
| DynamicAlpha | [FRawDistributionFloat](../FR/FRawDistributionFloat.md) | Dynamic alpha scale from the ColorOverLife module. |
| DynamicColorScale | [FRawDistributionVector](../FR/FRawDistributionVector.md) | Dynamic color scale from the ColorScaleOverLife module. |
| DynamicAlphaScale | [FRawDistributionFloat](../FR/FRawDistributionFloat.md) | Dynamic alpha scale from the ColorScaleOverLife module. |
| DynamicColorHDR | [FRawDistributionVector](../FR/FRawDistributionVector.md) | Dynamic color scale from the ColorOverLife module. |
| DynamicAlphaHDR | [FRawDistributionFloat](../FR/FRawDistributionFloat.md) | Dynamic alpha scale from the ColorOverLife module. |
| DynamicColorScaleHDR | [FRawDistributionVector](../FR/FRawDistributionVector.md) | Dynamic color scale from the ColorScaleOverLife module. |
| DynamicAlphaScaleHDR | [FRawDistributionFloat](../FR/FRawDistributionFloat.md) | Dynamic alpha scale from the ColorScaleOverLife module. |

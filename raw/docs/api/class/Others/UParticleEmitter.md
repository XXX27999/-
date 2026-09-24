# UParticleEmitter

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EmitterName | `FName` | The name of the emitter. |
| SubUVDataOffset | `int32` |  |
| EmitterRenderMode | `TEnumAsByte < enum EEmitterRenderMode >` | How to render the emitter particles. Can be one of the following:<br>	 		ERM_Normal	- As the intended spritemesh<br>	 		ERM_Point	- As a 2x2 pixel block with no scaling and the color set in EmitterEditorColor<br>	 		ERM_Cross	- As a cross of lines, scaled to the size of the particle in EmitterEditorColor<br>	 		ERM_None	- Do not render |
| LODLevels | `TArray < UParticleLODLevel * >` |  |
| ConvertedModules | `uint32` |  |
| PeakActiveParticles | `int32` |  |
| InitialAllocationCount | `int32` | Initial allocation count - overrides calculated peak count if > 0 |
| MediumDetailSpawnRateScale_DEPRECATED | `float` | Scales the spawn rate of this emitter when the engine is running in medium or low detail mode.<br>	  This can be used to optimize particle draw cost in splitscreen.<br>	  A value of 0 effectively disables this emitter outside of high detail mode,<br>	  And this does not affect spawn per unit, unless the value is 0. |
| QualityLevelSpawnRateScale | `float` |  |
| GPUToCPUEmitterSpawnRateScale | `float` |  |
| DetailMode | `TEnumAsByte < EDetailMode >` | If detail mode is >= system detail mode, primitive won't be rendered. |
| bIsSoloing | `uint32` | If true, then show only this emitter in the editor |
| bCookedOut | `uint32` | If true, then this emitter was 'cooked out' by the cooker.<br>	 	This means it was completely disabled, but to preserve any<br>	 	indexing schemes, it is left in place. |
| bDisabledLODsKeepEmitterAlive | `uint32` | When true, if the current LOD is disabled the emitter will be kept alive. Otherwise, the emitter will be considered complete if the current LOD is disabled. |
| bDisableWhenInsignficant | `uint32` | When true, emitters deemed insignificant will have their tick and render disabled Instantly. When false they will simple stop spawning new particles. |
| SignificanceLevel | [EParticleSignificanceLevel](../../cppenum/E/EP/EParticleSignificanceLevel.md) | The significance level required of this emitter's owner for this emitter to be active. |
| bSupportParticleDynamicInstance | `uint32` | When true, if r.ParticleDynamicinstance = 1 and the particle emitter type support dynamic instance,the same particle emitter will use 1 draw call command to render |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

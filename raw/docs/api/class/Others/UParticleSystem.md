# UParticleSystem

A ParticleSystem is a complete particle effect that contains any number of ParticleEmitters. By allowing multiple emitters
  in a system, the designer can create elaborate particle effects that are held in a single system. Once created using
  Cascade, a ParticleSystem can then be inserted into a level or created in script.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SystemUpdateMode | `TEnumAsByte < enum EParticleSystemUpdateMode >` |  |
| UpdateTime_FPS | `float` | UpdateTime_FPS	- the frame per second to update at in FixedTime mode |
| UpdateTime_Delta | `float` | UpdateTime_Delta	- internal |
| WarmupTime | `float` | WarmupTime - the time to warm-up the particle system when first rendered<br>	  Warning: WarmupTime is implemented by simulating the particle system for the time requested upon activation.<br>	  This is extremely prone to cause hitches, especially with large particle counts - use with caution. |
| WarmupTickRate | `float` | WarmupTickRate - the time step for each tick during warm up.<br>		Set to 0 to use the default tick time. |
| bEnableSeparateRendering | `bool` |  |
| Emitters | `TArray < UParticleEmitter * >` | Emitters	- internal - the array of emitters in the system |
| PreviewComponent | `UParticleSystemComponent *` | The component used to preview the particle system in Cascade |
| CurveEdSetup | `UInterpCurveEdSetup *` | Used for curve editor to remember curve-editing setup. |
| bOrientZAxisTowardCamera | `uint32` | If true, the system's Z axis will be oriented toward the camera |
| LODDistanceCheckTime | `float` | How often (in seconds) the system should perform the LOD distance check. |
| bUseDeviceConstBias | `bool` |  |
| bUseUltraDeviceBias | `bool` |  |
| bUseDeviceQualityBias | `bool` |  |
| bUsePCDeviceConstBias | `bool` |  |
| bUseCustomCullDistance | `bool` |  |
| bUseAbsoluteDistance | `bool` | default false ,use for cull distance not affected by r.ViewDistanceScale |
| CustomCullDistance | `float` | default 0 ,use for mobile particle distance cull |
| CustomPCCullDistance | `float` | default -1 then use same distance as mobile do |
| CullDistanceCheckTime | `float` |  |
| LODMethod | `TEnumAsByte < enum ParticleSystemLODMethod >` | The method of LOD level determination to utilize for this particle system<br>	 	  PARTICLESYSTEMLODMETHOD_Automatic - Automatically set the LOD level, checking every LODDistanceCheckTime seconds.<br>	     PARTICLESYSTEMLODMETHOD_DirectSet - LOD level is directly set by the game code.<br>	     PARTICLESYSTEMLODMETHOD_ActivateAutomatic - LOD level is determined at Activation time, then left alone unless directly set by game code. |
| LODDistances | `TArray < float >` | The array of distances for each LOD level in the system.<br>	 	Used when LODMethod is set to PARTICLESYSTEMLODMETHOD_Automatic.<br><br>	 	Example: System with 3 LOD levels<br>	 		LODDistances(0) = 0.0<br>	 		LODDistances(1) = 2500.0<br>	 		LODDistances(2) = 5000.0<br><br>	 		In this case, when the system is [   0.0 ..   2499.9] from the camera, LOD level 0 will be used.<br>	 										 [2500.0 ..   4999.9] from the camera, LOD level 1 will be used.<br>	 										 [5000.0 .. INFINITY] from the camera, LOD level 2 will be used. |
| bRegenerateLODDuplicate | `uint32` | Internal value that tracks the regenerate LOD levels preference.<br>	 	If true, when autoregenerating LOD levels in code, the low level will<br>	 	be a duplicate of the high. |
| LODSettings | `TArray < struct FParticleSystemLOD >` |  |
| bUseFixedRelativeBoundingBox | `uint32` | Whether to use the fixed relative bounding box or calculate it every frame. |
| FixedRelativeBoundingBox | [FBox](../../cppstruct/F/FB/FBox.md) | Fixed relative bounding box for particle system. |
| SecondsBeforeInactive | `float` | Number of seconds of emitter not being rendered that need to pass before it<br>	  no longer gets ticked becomes inactive. |
| bShouldResetPeakCounts | `uint32` | EDITOR ONLY: Indicates that Cascade would like to have the PeakActiveParticles count reset |
| bHasPhysics | `uint32` | Set during load time to indicate that physics is used... |
| bUseRealtimeThumbnail | `uint32` | Inidicates the old 'real-time' thumbnail rendering should be used |
| ThumbnailImageOutOfDate | `uint32` | Internal: Indicates the PSys thumbnail image is out of date |
| Delay | `float` | How long this Particle system should delay when ActivateSystem is called on it. |
| DelayLow | `float` | The low end of the emitter delay if using a range. |
| bUseDelayRange | `uint32` | If true, select the emitter delay from the range<br>	 		[DelayLow..Delay] |
| bAllowGcCluster | `uint8` |  |
| bAllowRenderDataUpdateLag | `uint8` |  |
| bAllowManagedTicking | `uint8` |  |
| bEnableSigTickBudget | `uint8` | sinyagao : Whether instances of this particle system opt in to SignificanceManager tick-budget and LOD control. |
| bAutoDeactivate | `bool` |  |
| MinTimeBetweenTicks | `uint32` |  |
| InsignificantReaction | [EParticleSystemInsignificanceReaction](../../cppenum/E/EP/EParticleSystemInsignificanceReaction.md) | The reaction this system takes when all emitters are insignificant. |
| InsignificanceDelay | `float` | Time delay between all emitters becoming insignificant and the systems insignificant reaction. |
| MaxSignificanceLevel | [EParticleSignificanceLevel](../../cppenum/E/EP/EParticleSignificanceLevel.md) | The maximum level of significance for emitters in this system. Any emitters with a higher significance will be capped at this significance level. |
| bAllowTickOptimization | `uint8` |  |
| bAllowSlowTickWhenInVisiable | `uint8` |  |
| bAllowSlowTickWhenFarAway | `uint8` |  |
| MacroUVPosition | [FVector](../../cppstruct/F/FV/FVector.md) | Local space position that UVs generated with the ParticleMacroUV material node will be centered on. |
| MacroUVRadius | `float` | World space radius that UVs generated with the ParticleMacroUV material node will tile based on. |
| OcclusionBoundsMethod | `TEnumAsByte < enum EParticleSystemOcclusionBoundsMethod >` | Which occlusion bounds method to use for this particle system.<br>	 	EPSOBM_None - Don't determine occlusion for this system.<br>	 	EPSOBM_ParticleBounds - Use the bounds of the component when determining occlusion. |
| CustomOcclusionBounds | [FBox](../../cppstruct/F/FB/FBox.md) | The occlusion bounds to use if OcclusionBoundsMethod is set to EPSOBM_CustomBounds |
| SoloTracking | `TArray < struct FLODSoloTrack >` |  |
| NamedMaterialSlots | `TArray < FNamedEmitterMaterial >` | Array of named material slots for use by emitters of this system.<br>		Emitters can use these instead of their own materials by providing the name to the NamedMaterialOverrides property of their required module.<br>		These materials can be overridden using CreateNamedDynamicMaterialInstance() on a ParticleSystemComponent. |
| bInitParticlesOnCanNotEverRender | `uint8` |  |
| AvailableDeviceLevel | `int32` |  |

## Functions

### ContainsEmitterType

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TypeData | `UClass *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

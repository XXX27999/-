# UParticleModule

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bSpawnModule | `uint32` | If true, the module performs operations on particles during Spawning |
| bUpdateModule | `uint32` | If true, the module performs operations on particles during Updating |
| bFinalUpdateModule | `uint32` | If true, the module performs operations on particles during final update |
| bUpdateForGPUEmitter | `uint32` | If true, the module performs operations on particles during update andor final update for GPU emitters |
| bCurvesAsColor | `uint32` | If true, the module displays FVector curves as colors |
| b3DDrawMode | `uint32` | If true, the module should render its 3D visualization helper |
| bSupported3DDrawMode | `uint32` | If true, the module supports rendering a 3D visualization helper |
| bEnabled | `uint32` | If true, the module is enabled |
| bEditable | `uint32` | If true, the module has had editing enabled on it |
| LODDuplicate | `uint32` | If true, this flag indicates that auto-generation for LOD will result in<br>		an exact duplicate of the module, regardless of the percentage.<br>		If false, it will result in a module with different settings. |
| bSupportsRandomSeed | `uint32` | If true, the module supports RandomSeed setting |
| bRequiresLoopingNotification | `uint32` | If true, the module should be told when looping |
| LODValidity | `uint8` | The LOD levels this module is present in.<br>	 	Bit-flags are used to indicate validity for a given LOD level.<br>	 	For example, if<br>	 		((1 << Level) & LODValidity) != 0<br>	 	then the module is used in that LOD. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

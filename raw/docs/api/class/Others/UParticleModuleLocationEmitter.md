# UParticleModuleLocationEmitter

## Parents

- UParticleModuleLocationBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| EmitterName | `FName` | The name of the emitter to use that the source location for particle. |
| SelectionMethod | `TEnumAsByte < enum ELocationEmitterSelectionMethod >` | The method to use when selecting a spawn target particle from the emitter.<br>	 	Can be one of the following:<br>	 		ELESM_Random		Randomly select a particle from the source emitter.<br>	 		ELESM_Sequential	Step through each particle from the source emitter in order. |
| InheritSourceVelocity | `uint32` | If true, the spawned particle should inherit the velocity of the source particle. |
| InheritSourceVelocityScale | `float` | Amount to scale the source velocity by when inheriting it. |
| bInheritSourceRotation | `uint32` | If true, the spawned particle should inherit the rotation of the source particle. |
| InheritSourceRotationScale | `float` | Amount to scale the source rotation by when inheriting it. |
| bApplySourceOrbitOffset | `uint32` | If true, the spawned particle should uses the location with the orbit offset of the source particle. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

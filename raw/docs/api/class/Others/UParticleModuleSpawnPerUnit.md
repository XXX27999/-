# UParticleModuleSpawnPerUnit

## Parents

- [UParticleModuleSpawnBase](./UParticleModuleSpawnBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UnitScalar | `float` | The scalar to apply to the distance traveled.<br>	 	The value from SpawnPerUnit is divided by this value to give the actual<br>	 	number of particles per unit. |
| SpawnPerUnit | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The amount to spawn per meter distribution.<br>	 	The value is retrieved using the EmitterTime. |
| bIgnoreSpawnRateWhenMoving | `uint32` | If true, process the default spawn rate when not moving...<br>	 	When not moving, skip the default spawn rate.<br>	 	If false, return the bProcessSpawnRate setting. |
| MovementTolerance | `float` | The tolerance for moving vs. not moving w.r.t. the bIgnoreSpawnRateWhenMoving flag.<br>	 	Ie, if (DistanceMoved < (UnitScalar x MovementTolerance)) then consider it not moving. |
| MaxFrameDistance | `float` | The maximum valid movement for a single frame.<br>	 	If 0.0, then the check is not performed.<br>	 	Currently, if the distance moved between frames is greater than this<br>	 	then NO particles will be spawned.<br>	 	This is primiarily intended to cover cases where the PSystem is<br>	 	attached to teleporting objects. |
| bIgnoreMovementAlongX | `uint32` | If true, ignore the X-component of the movement |
| bIgnoreMovementAlongY | `uint32` | If true, ignore the Y-component of the movement |
| bIgnoreMovementAlongZ | `uint32` | If true, ignore the Z-component of the movement |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

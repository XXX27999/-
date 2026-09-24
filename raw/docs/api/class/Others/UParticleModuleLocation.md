# UParticleModuleLocation

## Parents

- UParticleModuleLocationBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StartLocation | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The location the particle should be emitted.<br>	 	Relative in local space to the emitter by default.<br>	 	Relative in world space as a WorldOffset module or when the emitter's UseLocalSpace is off.<br>	 	Retrieved using the EmitterTime at the spawn of the particle. |
| DistributeOverNPoints | `float` | When set to a non-zero value this will force the particles to only spawn on evenly distributed<br>	   positions between the two points specified. |
| DistributeThreshold | `float` | When DistributeOverNPoints is set to a non-zero value, this specifies the ratio of particles spawned<br>	   that should use the distribution.  (For example setting this to 1 will cause all the particles to<br>	   be distributed evenly whereas .75 would cause 14 of the particles to be randomly placed). |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

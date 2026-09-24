# UParticleModuleCollision

## Parents

- UParticleModuleCollisionBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DampingFactor | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | How much to `slow' the velocity of the particle after a collision.<br>	 	Value is obtained using the EmitterTime at particle spawn. |
| DampingFactorRotation | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | How much to `slow' the rotation of the particle after a collision.<br>	 	Value is obtained using the EmitterTime at particle spawn. |
| MaxCollisions | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The maximum number of collisions a particle can have.<br>	   Value is obtained using the EmitterTime at particle spawn. |
| CollisionCompletionOption | `TEnumAsByte < enum EParticleCollisionComplete >` | What to do once a particles MaxCollisions is reached.<br>	 	One of the following:<br>	 	EPCC_Kill<br>	 		Kill the particle when MaxCollisions is reached<br>	 	EPCC_Freeze<br>	 		Freeze in place, NO MORE UPDATES<br>	 	EPCC_HaltCollisions,<br>	 		Stop collision checks, keep updating everything<br>	 	EPCC_FreezeTranslation,<br>	 		Stop translations, keep updating everything else<br>	 	EPCC_FreezeRotation,<br>	 		Stop rotations, keep updating everything else<br>	 	EPCC_FreezeMovement<br>	 		Stop all movement, keep updating |
| CollisionTypes | `TArray < TEnumAsByte < enum EObjectTypeQuery > >` | Which ObjectTypes to collide with |
| bApplyPhysics | `uint32` | If true, physic will be applied between a particle and the<br>	 	object it collides with.<br>	 	This is one-way - particle --> object. The particle does<br>	 	not have physics applied to it - it just generates an<br>	 	impulse applied to the object it collides with.<br>	  NOTE: having this on prevents the code from running off the game thread. |
| bIgnoreTriggerVolumes | `uint32` | Any trigger volumes that are hit will be ignored. NOTE: This can be turned off if the TrigerVolume physics object type is not in the CollisionTypes array.<br>	 Turning this off is strongly recommended as having it on prevents the code from running off the game thread. |
| ClassesToIgnore | `TArray < UClass * >` |  |
| ActorTagsToIgnore | `TArray < FName >` |  |
| ComponentClassesToIgnore | `TArray < UClass * >` |  |
| ComponentTagsToIgnore | `TArray < FName >` |  |
| bTraceByChannel | `bool` |  |
| TraceChannel | `TEnumAsByte < ECollisionChannel >` |  |
| ParticleMass | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The mass of the particle - for use when bApplyPhysics is true.<br>	 	Value is obtained using the EmitterTime at particle spawn. |
| DirScalar | `float` | The directional scalar value - used to scale the bounds to<br>	 	'assist' in avoiding inter-penetration or large gaps. |
| bPawnsDoNotDecrementCount | `uint32` | If true, then collisions with Pawns will still react, but<br>	 	the UsedMaxCollisions count will not be decremented.<br>	 	(ie., They don't 'count' as collisions)<br>	  NOTE: Having this on prevents the code from running in parallel. |
| bOnlyVerticalNormalsDecrementCount | `uint32` | If true, then collisions that do not have a vertical hit<br>	 	normal will still react, but UsedMaxCollisions count will<br>	 	not be decremented. (ie., They don't 'count' as collisions)<br>	 	Useful for having particles come to rest on floors. |
| VerticalFudgeFactor | `float` | The fudge factor to use to determine vertical.<br>	 	True vertical will have a Hit.Normal.Z == 1.0<br>	 	This will allow for Z components in the range of<br>	 	[1.0-VerticalFudgeFactor..1.0]<br>	 	to count as vertical collisions. |
| DelayAmount | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | How long to delay before checking a particle for collisions.<br>	 	Value is retrieved using the EmitterTime.<br>	 	During update, the particle flag IgnoreCollisions will be<br>	 	set until the particle RelativeTime has surpassed the<br>	 	DelayAmount. |
| bDropDetail | `uint32` | If true, when the World->bDropDetail flag is set, the module will be ignored. |
| bCollideOnlyIfVisible | `uint32` | If true, Particle collision only if particle system is currently being rendered. |
| bIgnoreSourceActor | `uint32` | If true, then the source actor is ignored in collision checks.<br>	 	Defaults to true. |
| bClearCacheIgnoreActorsAndCompsOnSpawn | `uint32` |  |
| ClearCacheIgnoreActorsAndCompsInterval | `float` |  |
| MaxCollisionDistance | `float` | Max distance at which particle collision will occur. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

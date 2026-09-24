# UParticleModuleTypeDataRibbon

## Parents

- UParticleModuleTypeDataBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxTessellationBetweenParticles | `int32` | The maximum amount to tessellate between two particles of the trail.<br>	 	Depending on the distance between the particles and the tangent change, the<br>	 	system will select a number of tessellation points<br>	 		[0..MaxTessellationBetweenParticles] |
| SheetsPerTrail | `int32` | The number of sheets to render for the trail. |
| MaxTrailCount | `int32` | The number of live trails |
| MaxParticleInTrailCount | `int32` | Max particles per trail |
| bDeadTrailsOnDeactivate | `uint32` | If true, when the system is deactivated, mark trails as dead.<br>	 	This means they will still render, but will not have more particles<br>	 	added to them, even if the system re-activates... |
| bDeadTrailsOnSourceLoss | `uint32` | If true, when the source of a trail is 'lost' (ie, the source particle<br>	 	dies), mark the current trail as dead. |
| bClipSourceSegement | `uint32` | If true, do not join the trail to the source position |
| bEnablePreviousTangentRecalculation | `uint32` | If true, recalculate the previous tangent when a new particle is spawned |
| bTangentRecalculationEveryFrame | `uint32` | If true, recalculate tangents every frame to allow velocityacceleration to be applied |
| bSpawnInitialParticle | `uint32` | If true, ribbon will spawn a particle when it first starts moving |
| RenderAxis | `TEnumAsByte < enum ETrailsRenderAxisOption >` | The 'render' axis for the trail (what axis the trail is stretched out on)<br>	 		Trails_CameraUp - Traditional camera-facing trail.<br>	 		Trails_SourceUp - Use the up axis of the source for each spawned particle.<br>	 		Trails_WorldUp  - Use the world up axis. |
| TangentSpawningScalar | `float` | The tangent scalar for spawning.<br>	 	Angles between tangent A and B are mapped to [0.0f .. 1.0f]<br>	 	This is then multiplied by TangentTessellationScalar to give the number of particles to spawn |
| bRenderGeometry | `uint32` | If true, render the trail geometry (this should typically be on) |
| bRenderSpawnPoints | `uint32` | If true, render stars at each spawned particle point along the trail |
| bRenderTangents | `uint32` | If true, render a line showing the tangent at each spawned particle point along the trail |
| bRenderTessellation | `uint32` | If true, render the tessellated path between spawned particles |
| TilingDistance | `float` | The (estimated) covered distance to tile the 2nd UV set at.<br>	 	If 0.0, a second UV set will not be passed in. |
| DistanceTessellationStepSize | `float` | The distance step size for tessellation.<br>	 	# Tessellation Points = TruncToInt((Distance Between Spawned Particles)  DistanceTessellationStepSize)) |
| bEnableTangentDiffInterpScale | `uint32` | If this flag is enabled, the system will scale the number of interpolated vertices<br>	 	based on the difference in the tangents of neighboring particles.<br>	 	Each pair of neighboring particles will compute the following CheckTangent value:<br>	 		CheckTangent = ((ParticleA Tangent DOT ParticleB Tangent) - 1.0f)  0.5f<br>	 	If CheckTangent is LESS THAN 0.5, then the DistanceTessellationStepSize will be<br>	 	scaled based on the result. This will map so that from parallel to orthogonal<br>	 	(0..90 degrees) will scale from [0..1]. Anything greater than 90 degrees will clamp<br>	 	at a scale of 1. |
| TangentTessellationScalar | `float` | The tangent scalar for tessellation.<br>	 	Angles between tangent A and B are mapped to [0.0f .. 1.0f]<br>	 	This is then multiplied by TangentTessellationScalar to give the number of points to tessellate |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

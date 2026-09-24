# UParticleModuleRequired

## Parents

- [UParticleModule](./UParticleModule.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` | The material to utilize for the emitter at this LOD level. |
| EmitterOrigin | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| EmitterRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| EmitterOrbitOrigin | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| EmitterRotateAxis | [EEmitterRotationMode](../../cppenum/E/EE/EEmitterRotationMode.md) |  |
| EmitterOrbitRadius | `float` |  |
| EmitterOrbitSpeed | `float` |  |
| EmitterInitialDegree | `float` |  |
| EmitterInitialRotation | `float` |  |
| EmitterSelfRotateAxis | [EEmitterSelfRotationMode](../../cppenum/E/EE/EEmitterSelfRotationMode.md) |  |
| EmitterSelfRotationSpeed | `float` |  |
| ScreenAlignment | `TEnumAsByte < EParticleScreenAlignment >` | The screen alignment to utilize for the emitter at this LOD level.<br>	 	One of the following:<br>	 	PSA_FacingCameraPosition - Faces the camera position, but is not dependent on the camera rotation.<br>	 								This method produces more stable particles under camera rotation.<br>	 	PSA_Square			- Uniform scale (via SizeX) facing the camera<br>	 	PSA_Rectangle		- Non-uniform scale (via SizeX and SizeY) facing the camera<br>	 	PSA_Velocity		- Orient the particle towards both the camera and the direction<br>	 						  the particle is moving. Non-uniform scaling is allowed.<br>	 	PSA_TypeSpecific	- Use the alignment method indicated in the type data module.<br>	 	PSA_FacingCameraDistanceBlend - Blends between PSA_FacingCameraPosition and PSA_Square over specified distance. |
| MinFacingCameraBlendDistance | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_Square |
| MaxFacingCameraBlendDistance | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_FacingCameraPosition |
| bUseLocalSpace | `uint32` | If true, update the emitter in local space |
| bKillOnDeactivate | `uint32` | If true, kill the emitter when the particle system is deactivated |
| bKillOnCompleted | `uint32` | If true, kill the emitter when it completes |
| SortMode | `TEnumAsByte < enum EParticleSortMode >` | The sorting mode to use for this emitter.<br>	 	PSORTMODE_None				- No sorting required.<br>	 	PSORTMODE_ViewProjDepth		- Sort by view projected depth of the particle.<br>	 	PSORTMODE_DistanceToView	- Sort by distance of particle to view in world space.<br>	 	PSORTMODE_Age_OldestFirst	- Sort by age, oldest drawn first.<br>	 	PSORTMODE_Age_NewestFirst	- Sort by age, newest drawn first. |
| bConsiderOrbitOffsetWhenSort | `uint32` |  |
| bUseLegacyEmitterTime | `uint32` | If true, the EmitterTime for the emitter will be calculated by<br>	 	modulating the SecondsSinceCreation by the EmitterDuration. As<br>	 	this can lead to issues w looping and variable duration, a new<br>	 	approach has been implemented.<br>	 	If false, this new approach is utilized, and the EmitterTime is<br>	 	simply incremented by DeltaTime each tick. When the emitter<br>	 	loops, it adjusts the EmitterTime by the current EmitterDuration<br>	 	resulting in proper loopingdelay behavior. |
| bRemoveHMDRoll | `uint32` | If true, removes the HMD view roll (e.g. in VR) |
| EmitterDuration | `float` | How long, in seconds, the emitter will run before looping. |
| EmitterDurationLow | `float` | The low end of the emitter duration if using a range. |
| bEmitterDurationUseRange | `uint32` | If true, select the emitter duration from the range<br>	 		[EmitterDurationLow..EmitterDuration] |
| bDurationRecalcEachLoop | `uint32` | If true, recalculate the emitter duration on each loop. |
| EmitterLoops | `int32` | The number of times to loop the emitter.<br>	 	0 indicates loop continuously |
| SpawnRate | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The rate at which to spawn particles |
| ParticleBurstMethod | `TEnumAsByte < EParticleBurstMethod >` | The method to utilize when burst-emitting particles |
| BurstList | `TArray < struct FParticleBurst >` | The array of burst entries. |
| EmitterDelay | `float` | Indicates the time (in seconds) that this emitter should be delayed in the particle system. |
| EmitterDelayLow | `float` | The low end of the emitter delay if using a range. |
| bEmitterDelayUseRange | `uint32` | If true, select the emitter delay from the range<br>	 		[EmitterDelayLow..EmitterDelay] |
| bDelayFirstLoopOnly | `uint32` | If true, the emitter will be delayed only on the first loop. |
| InterpolationMethod | `TEnumAsByte < EParticleSubUVInterpMethod >` | The interpolation method to used for the SubUV image selection.<br>	 	One of the following:<br>	 	PSUVIM_None			- Do not apply SubUV modules to this emitter.<br>	 	PSUVIM_Linear		- Smoothly transition between sub-images in the given order,<br>	 						  with no blending between the current and the next<br>	 	PSUVIM_Linear_Blend	- Smoothly transition between sub-images in the given order,<br>	 						  blending between the current and the next<br>	 	PSUVIM_Random		- Pick the next image at random, with no blending between<br>	 						  the current and the next<br>	 	PSUVIM_Random_Blend	- Pick the next image at random, blending between the current<br>	 						  and the next |
| SubImages_Horizontal | `int32` | The number of sub-images horizontally in the texture |
| SubImages_Vertical | `int32` | The number of sub-images vertically in the texture |
| bScaleUV | `uint32` | Whether to scale the UV or not - ie, the model wasn't setup with sub uvs |
| RandomImageTime | `float` | The amount of time (particle-relative, 0.0 to 1.0) to 'lock' on a random sub image<br>	 	    0.0 = change every frame<br>	       1.0 = select a random image at spawn and hold for the life of the particle |
| RandomImageChanges | `int32` | The number of times to change a random image over the life of the particle. |
| bOverrideSystemMacroUV | `uint32` | Override the system MacroUV settings |
| MacroUVPosition | [FVector](../../cppstruct/F/FV/FVector.md) | Local space position that UVs generated with the ParticleMacroUV material node will be centered on. |
| MacroUVRadius | `float` | World space radius that UVs generated with the ParticleMacroUV material node will tile based on. |
| bUseMaxDrawCount | `uint32` | If true, use the MaxDrawCount to limit the number of particles rendered.<br>	 	NOTE: This does not limit the number spawnedupdated, only what is drawn. |
| MaxDrawCount | `int32` | The maximum number of particles to DRAW for this emitter.<br>	 	If set to 0, it will use whatever number are present. |
| UVFlippingMode | [EParticleUVFlipMode](../../cppenum/E/EP/EParticleUVFlipMode.md) | Controls UV Flipping for this emitter. |
| CutoutTexture | `UTexture2D *` | Texture to generate bounding geometry from. |
| BoundingMode | `TEnumAsByte < enum ESubUVBoundingVertexCount >` | More bounding vertices results in reduced overdraw, but adds more triangle overhead.<br>	 The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,<br>	 and when the particles using the texture will be few and large. |
| OpacitySourceMode | `TEnumAsByte < enum EOpacitySourceMode >` |  |
| AlphaThreshold | `float` | Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.<br>	 Raising this threshold slightly can reduce overdraw in particles using this animation asset. |
| bCutoutUseSingleFrame | `bool` | Generate Cutout geometry from the complete CutoutTexture instead of its SubUV grid. |
| CutoutSubImagesX | `int32` |  |
| CutoutSubImagesY | `int32` | The number of sub-images vertically in the texture |
| bEnableCutOut | `bool` |  |
| EmitterNormalsMode | `TEnumAsByte < enum EEmitterNormalsMode >` | Normal generation mode for this emitter LOD. |
| NormalsSphereCenter | [FVector](../../cppstruct/F/FV/FVector.md) | When EmitterNormalsMode is ENM_Spherical, particle normals are created to face away from NormalsSphereCenter.<br>	  NormalsSphereCenter is in local space. |
| NormalsCylinderDirection | [FVector](../../cppstruct/F/FV/FVector.md) | When EmitterNormalsMode is ENM_Cylindrical,<br>	  particle normals are created to face away from the cylinder going through NormalsSphereCenter in the direction NormalsCylinderDirection.<br>	  NormalsCylinderDirection is in local space. |
| bOrbitModuleAffectsVelocityAlignment | `uint32` | Ensures that movement generated from the orbit module is applied to velocity-aligned particles |
| NamedMaterialOverrides | `TArray < FName >` | Named material overrides for this emitter.<br>		Overrides this emitter's material(s) with those in the correspondingly named slot(s) of the owning system. |
| UBOBoundingGeometry | `TArray < FVector2D >` |  |
| bUseComputeRaster | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

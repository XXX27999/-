# UParticleModuleTypeDataBeam2

## Parents

- UParticleModuleTypeDataBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BeamMethod | `TEnumAsByte < enum EBeam2Method >` | The method with which to form the beam(s). Must be one of the following:<br>	 		PEB2M_Distance	- Use the distance property to emit a beam along the X-axis of the emitter.<br>	 		PEB2M_Target	- Emit a beam from the source to the supplied target.<br>	 		PEB2M_Branch	- Currently unimplemented. |
| TextureTile | `int32` | The number of times to tile the texture along each beam.<br>	   Overridden by TextureTilingDistance if it is > 0.0.<br>	 	1st UV set only. 2nd UV set does not Tile. |
| TextureTileDistance | `float` | The distance per texture tile.<br>	 	1st UV set only. 2nd UV set does not Tile. |
| Sheets | `int32` | The number of sheets to render |
| MaxBeamCount | `int32` | The number of live beams |
| Speed | `float` | The speed at which the beam should move from source to target when firing up.<br>	 	'0' indicates instantaneous |
| InterpolationPoints | `int32` | Indicates whether the beam should be interpolated.<br>	      <= 0 --> no<br>	      >  0 --> yes (and is equal to the number of interpolation steps that should be taken. |
| bAlwaysOn | `uint32` | If true, there will ALWAYS be a beam... |
| UpVectorStepSize | `int32` | The approach to use for determining the Up vector(s) for the beam.<br><br>	 	0 indicates that the Up FVector should be calculated at EVERY point in the beam.<br>	 	1 indicates a single Up FVector should be determined at the start of the beam and used at every point.<br>	 	N indicates an Up FVector should be calculated every N points of the beam and interpolated between them.<br>	 	    [NOTE: This mode is currently unsupported.] |
| BranchParentName | `FName` | The name of the emitter to branch from (if mode is PEB2M_Branch)<br>	  MUST BE IN THE SAME PARTICLE SYSTEM! |
| Distance | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | The distance along the X-axis to stretch the beam<br>	 	Distance is only used if BeamMethod is PEB2M_Distance |
| TaperMethod | `TEnumAsByte < enum EBeamTaperMethod >` | Tapering mode - one of the following:<br>	 	PEBTM_None		- No tapering is applied<br>	 	PEBTM_Full		- Taper the beam relative to source-->target, regardless of current beam length<br>	 	PEBTM_Partial	- Taper the beam relative to source-->location, 0=source,1=endpoint |
| TaperFactor | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | Tapering factor, 0 = source of beam, 1 = target |
| TaperScale | [FRawDistributionFloat](../../cppstruct/F/FR/FRawDistributionFloat.md) | Tapering scaling<br>	 	This is intended to be either a constant, uniform or a ParticleParam.<br>	 	If a curve is used, 01 mapping of sourcetarget... which could be integrated into<br>	 	the taper factor itself, and therefore makes no sense. |
| RenderGeometry | `uint32` |  |
| RenderDirectLine | `uint32` |  |
| RenderLines | `uint32` |  |
| RenderTessellation | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UParticleModuleTypeDataMesh

## Parents

- UParticleModuleTypeDataBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Mesh | `UStaticMesh *` | The static mesh to render at the particle positions |
| CastShadows | `uint32` | If true, has the meshes cast shadows |
| DoCollisions | `uint32` | UNUSED (the collision module dictates doing collisions) |
| MeshAlignment | `TEnumAsByte < enum EMeshScreenAlignment >` | The alignment to use on the meshes emitted.<br>	 	The RequiredModule->ScreenAlignment MUST be set to PSA_TypeSpecific to use.<br>	 	One of the following:<br>	 	PSMA_MeshFaceCameraWithRoll<br>	 		Face the camera allowing for rotation around the mesh-to-camera FVector<br>	 		(amount provided by the standard particle sprite rotation).<br>	 	PSMA_MeshFaceCameraWithSpin<br>	 		Face the camera allowing for the mesh to rotate about the tangential axis.<br>	 	PSMA_MeshFaceCameraWithLockedAxis<br>	 		Face the camera while maintaining the up FVector as the locked direction. |
| bOverrideMaterial | `uint32` | If true, use the emitter material when rendering rather than the one applied<br>	 	to the static mesh model. |
| bOverrideDefaultMotionBlurSettings | `uint32` |  |
| bEnableMotionBlur | `uint32` |  |
| Pitch_DEPRECATED | `float` | deprecated properties for initial orientation |
| Roll_DEPRECATED | `float` |  |
| Yaw_DEPRECATED | `float` |  |
| RollPitchYawRange | [FRawDistributionVector](../../cppstruct/F/FR/FRawDistributionVector.md) | The 'pre' rotation pitch (in degrees) to apply to the static mesh used. |
| AxisLockOption | `TEnumAsByte < EParticleAxisLock >` | The axis to lock the mesh on. This overrides TypeSpecific mesh alignment as well as the LockAxis module.<br>	 		EPAL_NONE		 -	No locking to an axis.<br>	 		EPAL_X			 -	Lock the mesh X-axis facing towards +X.<br>	 		EPAL_Y			 -	Lock the mesh X-axis facing towards +Y.<br>	 		EPAL_Z			 -	Lock the mesh X-axis facing towards +Z.<br>	 		EPAL_NEGATIVE_X	 -	Lock the mesh X-axis facing towards -X.<br>	 		EPAL_NEGATIVE_Y	 -	Lock the mesh X-axis facing towards -Y.<br>	 		EPAL_NEGATIVE_Z	 -	Lock the mesh X-axis facing towards -Z.<br>	 		EPAL_ROTATE_X	 -	Ignored for mesh emitters. Treated as EPAL_NONE.<br>	 		EPAL_ROTATE_Y	 -	Ignored for mesh emitters. Treated as EPAL_NONE.<br>	 		EPAL_ROTATE_Z	 -	Ignored for mesh emitters. Treated as EPAL_NONE. |
| bCameraFacing | `uint32` | If true, then point the X-axis of the mesh towards the camera.<br>	 	When set, AxisLockOption as well as all other locked axisscreen alignment settings are ignored. |
| CameraFacingUpAxisOption_DEPRECATED | `TEnumAsByte < enum EMeshCameraFacingUpAxis >` | The axis of the mesh to point up when camera facing the X-axis.<br>	 		CameraFacing_NoneUP			No attempt to face an axis up or down.<br>	 		CameraFacing_ZUp			Z-axis of the mesh should attempt to point up.<br>	 		CameraFacing_NegativeZUp	Z-axis of the mesh should attempt to point down.<br>	 		CameraFacing_YUp			Y-axis of the mesh should attempt to point up.<br>	 		CameraFacing_NegativeYUp	Y-axis of the mesh should attempt to point down. |
| CameraFacingOption | `TEnumAsByte < enum EMeshCameraFacingOptions >` | The camera facing option to use:<br>	 	All camera facing options without locked axis assume X-axis will be facing the camera.<br>	 		XAxisFacing_NoUp				- X-axis camera facing, no attempt to face an axis up or down.<br>	 		XAxisFacing_ZUp					- X-axis camera facing, Z-axis of the mesh should attempt to point up.<br>	 		XAxisFacing_NegativeZUp			- X-axis camera facing, Z-axis of the mesh should attempt to point down.<br>	 		XAxisFacing_YUp					- X-axis camera facing, Y-axis of the mesh should attempt to point up.<br>	 		XAxisFacing_NegativeYUp			- X-axis camera facing, Y-axis of the mesh should attempt to point down.<br>	 	All axis-locked camera facing options assume the AxisLockOption is set. EPAL_NONE will be treated as EPAL_X.<br>	 		LockedAxis_ZAxisFacing			- X-axis locked on AxisLockOption axis, rotate Z-axis of the mesh to face towards camera.<br>	 		LockedAxis_NegativeZAxisFacing	- X-axis locked on AxisLockOption axis, rotate Z-axis of the mesh to face away from camera.<br>	 		LockedAxis_YAxisFacing			- X-axis locked on AxisLockOption axis, rotate Y-axis of the mesh to face towards camera.<br>	 		LockedAxis_NegativeYAxisFacing	- X-axis locked on AxisLockOption axis, rotate Y-axis of the mesh to face away from camera.<br>	 	All velocity-aligned options do NOT require the ScreenAlignment be set to PSA_Velocity.<br>	 	Doing so will result in additional work being performed... (it will orient the mesh twice).<br>	 		VelocityAligned_ZAxisFacing         - X-axis aligned to the velocity, rotate the Z-axis of the mesh to face towards camera.<br>	 		VelocityAligned_NegativeZAxisFacing - X-axis aligned to the velocity, rotate the Z-axis of the mesh to face away from camera.<br>	 		VelocityAligned_YAxisFacing         - X-axis aligned to the velocity, rotate the Y-axis of the mesh to face towards camera.<br>	 		VelocityAligned_NegativeYAxisFacing - X-axis aligned to the velocity, rotate the Y-axis of the mesh to face away from camera. |
| bApplyParticleRotationAsSpin | `uint32` | If true, apply 'sprite' particle rotation about the orientation axis (direction mesh is pointing).<br>	 	If false, apply 'sprite' particle rotation about the camera facing axis. |
| bFaceCameraDirectionRatherThanPosition | `uint32` | If true, all camera facing options will point the mesh against the camera's view direction rather than pointing at the cameras location.<br>		If false, the camera facing will point to the cameras position as normal. |
| bCollisionsConsiderPartilceSize | `uint32` | If true, all collisions for mesh particle on this emitter will take the particle size into account.<br>		If false, particle size will be ignored in collision checks. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

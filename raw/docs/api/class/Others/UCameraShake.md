# UCameraShake

A CameraShake is an asset that defines how to shake the camera in
  a particular way. CameraShakes can be authored as either oscillating shakes,
  animated shakes, or both.

  An oscillating shake will sinusoidally vibrate various camera parameters over time. Each location
  and rotation axis can be oscillated independently with different parameters to create complex and
  random-feeling shakes. These are easier to author and tweak, but can still feel mechanical and are
  limited to vibration-style shakes, such as earthquakes.

  Animated shakes play keyframed camera animations.  These can take more effort to author, but enable
  more natural-feeling results and things like directional shakes.  For instance, you can have an explosion
  to the camera's right push it primarily to the left.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bSingleInstance | `uint32` | If true to only allow a single instance of this shake class to play at any given time.<br>	   Subsequent attempts to play this shake will simply restart the timer. |
| OscillationDuration | `float` | Duration in seconds of current screen shake. Less than 0 means indefinite, 0 means no oscillation. |
| OscillationBlendInTime | `float` | Duration of the blend-in, where the oscillation scales from 0 to 1. |
| OscillationBlendOutTime | `float` | Duration of the blend-out, where the oscillation scales from 1 to 0. |
| RotOscillation | [FROscillator](../../cppstruct/F/FR/FROscillator.md) | Rotational oscillation |
| LocOscillation | [FVOscillator](../../cppstruct/F/FV/FVOscillator.md) | Positional oscillation |
| FOVOscillation | [FFOscillator](../../cppstruct/F/FF/FFOscillator.md) | FOV oscillation |
| AnimPlayRate | `float` | Parameters for defining CameraAnim-driven camera shakes<br><br>	 Scalar defining how fast to play the anim. |
| AnimScale | `float` | Scalar defining how "intense" to play the anim. |
| AnimBlendInTime | `float` | Linear blend-in time. |
| AnimBlendOutTime | `float` | Linear blend-out time. |
| RandomAnimSegmentDuration | `float` | When bRandomAnimSegment is true, this defines how long the anim should play. |
| Anim | `UCameraAnim *` | Source camera animation to play. Can be null. |
| Anims | `TArray < UCameraAnim * >` | Source camera animations to play. Can be empty. |
| bRandomAnimSegment | `uint32` | If true, play a random snippet of the animation of length Duration.  Implies bLoop and bRandomStartTime = true for the CameraAnim.<br>	 If false, play the full anim once, non-looped. Useful for getting variety out of a single looped CameraAnim asset. |
| RandomFinalIntenseScaleRange | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| RandomFinalIntenseScaleRange_X | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| RandomFinalIntenseScaleRange_Y | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| RandomFinalIntenseScaleRange_Z | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| RandomFinalIntenseScaleRange_Yaw | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| RandomFinalIntenseScaleRange_Pitch | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| RandomFinalIntenseScaleRange_Roll | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| CameraOwner | `APlayerCameraManager *` |  |
| ShakeScale | `float` | Overall intensity scale for this shake instance. |
| OscillatorTimeRemaining | `float` | Time remaining for oscillation shakes. Less than 0.f means shake infinitely. |
| AttenuationFloatCurve | `UCurveFloat *` | Source camera curve to add. Can be null. |

## Functions

### BlueprintUpdateCameraShake

Called every tick to let the shake modify the point of view

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTime | `float` |  |
| Alpha | `float` |  |
| POV | `FMinimalViewInfo &` |  |
| ModifiedPOV | `FMinimalViewInfo &` |  |

**Return**

- Type: 
- Description: _None_

### ReceivePlayShake

Called when the shake starts playing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Scale | `float` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveIsFinished

Called to allow a shake to decide when it's finished playing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveStopShake

Called when the shake is explicitly stopped.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bImmediately | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

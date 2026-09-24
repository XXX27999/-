# USpringArmComponent

This component tries to maintain its children at a fixed distance from the parent,
  but will retract the children if there is a collision, and spring back when there is no collision.

  Example: Use as a 'camera boom' to keep the follow camera for a player from colliding into the world.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TargetArmLength | `float` | Natural length of the spring arm when there are no collisions |
| SocketOffset | [FVector](../../cppstruct/F/FV/FVector.md) | offset at end of spring arm; use this instead of the relative offset of the attached component to ensure the line trace works as desired |
| TargetOffset | [FVector](../../cppstruct/F/FV/FVector.md) | Offset at start of spring, applied in world space. Use this if you want a world-space offset from the parent component instead of the usual relative-space offset. |
| ProbeSize | `float` | How big should the query probe sphere be (in unreal units) |
| ProbeChannel | `TEnumAsByte < ECollisionChannel >` | Collision channel of the query probe (defaults to ECC_Camera) |
| bDoCollisionTest | `uint32` | If true, do a collision test using ProbeChannel and ProbeSize to prevent camera clipping into level. |
| bUsePawnControlRotation | `uint32` | If this component is placed on a pawn, should it use the viewcontrol rotation of the pawn where possible?<br>	  When disabled, the component will revert to using the stored RelativeRotation of the component.<br>	  Note that this component itself does not rotate, but instead maintains its relative rotation to its parent as normal,<br>	  and just repositions and rotates its children as desired by the inherited rotation settings. Use GetTargetRotation()<br>	  if you want the rotation target based on all the settings (UsePawnControlRotation, InheritPitch, etc).<br><br>	  @see GetTargetRotation(), APawn::GetViewRotation() |
| bInheritPitch | `uint32` | Should we inherit pitch from parent component. Does nothing if using Absolute Rotation. |
| bInheritYaw | `uint32` | Should we inherit yaw from parent component. Does nothing if using Absolute Rotation. |
| bInheritRoll | `uint32` | Should we inherit roll from parent component. Does nothing if using Absolute Rotation. |
| bEnableCameraLag | `uint32` | If true, camera lags behind target position to smooth its movement.<br>	  @see CameraLagSpeed |
| bEnableCameraRotationLag | `uint32` | If true, camera lags behind target rotation to smooth its movement.<br>	  @see CameraRotationLagSpeed |
| bUseCameraLagSubstepping | `uint32` | If bUseCameraLagSubstepping is true, sub-step camera damping so that it handles fluctuating frame rates well (though this comes at a cost).<br>	  @see CameraLagMaxTimeStep |
| bDrawDebugLagMarkers | `uint32` | If true and camera location lag is enabled, draws markers at the camera target (in green) and the lagged position (in yellow).<br>	  A line is drawn between the two locations, in green normally but in red if the distance to the lag target has been clamped (by CameraLagMaxDistance). |
| CameraLagSpeed | `float` | If bEnableCameraLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag). |
| CameraRotationLagSpeed | `float` | If bEnableCameraRotationLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag). |
| CameraLagMaxTimeStep | `float` | Max time step used when sub-stepping camera lag. |
| CameraLagMaxDistance | `float` | Max distance the camera target may lag behind the current location. If set to zero, no max distance is enforced. |
| IgnoredActors | `TArray < AActor * >` |  |
| CacheHit | [FHitResult](../../cppstruct/F/FH/FHitResult.md) |  |

## Functions

### GetTargetRotation

Get the target rotation we inherit, used as the base target for the boom rotation.
	  This is derived from attachment to our parent and considering the UsePawnControlRotation and absolute rotation flags.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActive

Sets whether the component is active or not

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewActive | `bool` | - The new active state of the component |
| bReset | `bool` |  |

**Return**

- Type: 
- Description: _None_

### UpdateDesiredArmLocationCustom

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDoTrace | `bool` |  |
| bDoLocationLag | `bool` |  |
| bDoRotationLag | `bool` |  |
| DeltaTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetExtraIgnoreActors

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetExtraIgnoreCompoents

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

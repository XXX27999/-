# ACameraActor

A CameraActor is a camera viewpoint that can be placed in a level.

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AutoActivateForPlayer | `TEnumAsByte < EAutoReceiveInput :: Type >` | Specifies which player controller, if any, should automatically use this Camera when the controller is active. |
| CameraComponent | `UCameraComponent *` | The camera component for this camera |
| SceneComponent | `USceneComponent *` |  |
| bConstrainAspectRatio_DEPRECATED | `uint32` |  |
| AspectRatio_DEPRECATED | `float` |  |
| FOVAngle_DEPRECATED | `float` |  |
| PostProcessBlendWeight_DEPRECATED | `float` |  |
| PostProcessSettings_DEPRECATED | [FPostProcessSettings](../../cppstruct/F/FP/FPostProcessSettings.md) |  |

## Functions

### GetAutoActivatePlayerIndex

Returns index of the player for whom we auto-activate, or INDEX_NONE (-1) if disabled.

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

# UCameraModifier_CameraShake

A UCameraModifier_CameraShake is a camera modifier that can apply a UCameraShake to
  the owning camera.

## Parents

- [UCameraModifier](./UCameraModifier.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ActiveShakes | `TArray < UCameraShake * >` | List of active CameraShake instances |
| SplitScreenShakeScale | `float` | Scaling factor applied to all camera shakes in when in splitscreen mode. Normally used to reduce shaking, since shakes feel more intense in a smaller viewport. |
| CacheShakeInsMap | `TMap < TSubclassOf < UCameraShake > , FCacheCameraShakeData >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

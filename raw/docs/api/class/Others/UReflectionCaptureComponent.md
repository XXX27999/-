# UReflectionCaptureComponent

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CaptureOffsetComponent | `UBillboardComponent *` |  |
| ReflectionSourceType | [EReflectionSourceType](../../cppenum/E/ER/EReflectionSourceType.md) | Indicates where to get the reflection source from. |
| IndoorOutdoorMask | `TEnumAsByte < EIndoorOutdoorMask >` |  |
| Cubemap | `UTextureCube *` | Cubemap to use for reflection if ReflectionSourceType is set to RS_SpecifiedCubemap. |
| SourceCubemapAngle | `float` | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |
| Brightness | `float` | A brightness control to scale the captured scene's reflection intensity. |
| CaptureOffset | [FVector](../../cppstruct/F/FV/FVector.md) | World space offset to apply before capturing. |
| EnabledPlatform | [EReflectionPlatform](../../cppenum/E/ER/EReflectionPlatform.md) |  |
| StateId | [FGuid](../../cppstruct/F/FG/FGuid.md) |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

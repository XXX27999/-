# UCurveLinearColorAtlas

Manages gradient LUT textures for registered actors and assigns them to the corresponding materials on the actor

## Parents

- [UTexture2D](./UTexture2D.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TextureSize | `uint32` |  |
| bSquareResolution | `uint32` | Set texture height equal to texture width. |
| TextureHeight | `uint32` |  |
| GradientCurves | `TArray < UCurveLinearColor * >` |  |
| bIsDirty | `uint32` |  |
| bDisableAllAdjustments | `uint32` | Disable all color adjustments to preserve negative values in curves. Color adjustments clamp to 0 when enabled. |
| bHasCachedColorAdjustments | `uint32` |  |
| CachedColorAdjustments | [FCurveAtlasColorAdjustments](../../cppstruct/F/FC/FCurveAtlasColorAdjustments.md) |  |

## Functions

### GetCurvePosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCurve | `UCurveLinearColor *` |  |
| Position | `float &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

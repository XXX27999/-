# UArrowComponent

A simple arrow rendered using lines. Useful for indicating which way an object is facing.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ArrowColor | [FColor](../../cppstruct/F/FC/FColor.md) |  |
| ArrowSize | `float` |  |
| bIsScreenSizeScaled | `bool` | Set to limit the screen size of this arrow |
| ScreenSize | `float` | The size on screen to limit this arrow to (in screen space) |
| bTreatAsASprite | `uint32` | If true, don't show the arrow when EngineShowFlags.BillboardSprites is disabled. |

## Functions

### SetArrowColor

Updates the arrow's colour, and tells it to refresh

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

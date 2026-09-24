# UBoxComponent

A box generally used for simple collision. Bounds are rendered as lines in the editor.

## Parents

- [UShapeComponent](./UShapeComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BoxExtent | [FVector](../../cppstruct/F/FV/FVector.md) | The extents (radii dimensions) of the box |
| LineThickness | `float` | Used to control the line thickness when rendering |

## Functions

### SetBoxExtent

Change the box extent size. This is the unscaled size, before component scale is applied.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoxExtent | `FVector` |  |
| bUpdateOverlaps | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetScaledBoxExtent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetUnscaledBoxExtent

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

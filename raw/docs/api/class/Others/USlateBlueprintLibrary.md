# USlateBlueprintLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### IsUnderLocation

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry &` |  |
| AbsoluteCoordinate | `FVector2D &` |  |

**Return**

- Type: 
- Description: _None_

### AbsoluteToLocal

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry &` |  |
| AbsoluteCoordinate | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### LocalToAbsolute

Translates local coordinates into absolute coordinates

	  Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry &` |  |
| LocalCoordinate | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetLocalSize

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry &` |  |

**Return**

- Type: 
- Description: _None_

### GetAbsoluteSize

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry &` |  |

**Return**

- Type: 
- Description: _None_

### GetAbsolutePosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Geometry | `FGeometry &` |  |

**Return**

- Type: 
- Description: _None_

### EqualEqual_SlateBrush

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FSlateBrush &` |  |
| B | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### LocalToViewport

Translates local coordinate of the geometry provided into local viewport coordinates.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Geometry | `FGeometry &` |  |
| LocalCoordinate | `FVector2D` |  |
| PixelPosition | `FVector2D &` | The position in the game's viewport, usable for line traces and |
| ViewportPosition | `FVector2D &` | The position in the space of other widgets in the viewport. Like if you wanted |

**Return**

- Type: 
- Description: _None_

### AbsoluteToViewport

Translates absolute coordinate in desktop space of the geometry provided into local viewport coordinates.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| AbsoluteDesktopCoordinate | `FVector2D` |  |
| PixelPosition | `FVector2D &` | The position in the game's viewport, usable for line traces and |
| ViewportPosition | `FVector2D &` | The position in the space of other widgets in the viewport. Like if you wanted |

**Return**

- Type: 
- Description: _None_

### ScreenToWidgetLocal

Translates a screen position in pixels into the local space of a widget with the given geometry.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Geometry | `FGeometry &` |  |
| ScreenPosition | `FVector2D` |  |
| LocalCoordinate | `FVector2D &` |  |

**Return**

- Type: 
- Description: _None_

### ScreenToWidgetAbsolute

Translates a screen position in pixels into absolute application coordinates.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ScreenPosition | `FVector2D` |  |
| AbsoluteCoordinate | `FVector2D &` |  |

**Return**

- Type: 
- Description: _None_

### ScreenToViewport

Translates a screen position in pixels into the local space of the viewport widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ScreenPosition | `FVector2D` |  |
| ViewportPosition | `FVector2D &` |  |

**Return**

- Type: 
- Description: _None_

### GetSlateConstant_GlobalScrollAmount

Provide GetGlobalScrollAmount() to Lua.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReleaseAllMouseCapture

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReleaseMouseCaptureWithIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ReleaseAllMousePassThroughCapture

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReleaseMousePassThroughCaptureWithIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetMouseCaptor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointerIndex | `int32` |  |
| Widget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### SetMousePassThroughCaptor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointerIndex | `int32` |  |
| Widget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UWidgetLayoutLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### ProjectWorldLocationToWidgetPosition

Gets the projected world to screen position for a player, then converts it into a widget
	  position, which takes into account any quality scaling.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` | The player controller to project the position in the world to their screen. |
| WorldLocation | `FVector` | The world location to project from. |
| ScreenPosition | `FVector2D &` | The position in the viewport with quality scale removed and DPI scale remove. |

**Return**

- Type: 
- Description: _None_

### GetViewportScale

Gets the current DPI Scale being applied to the viewport and all the Widgets.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetViewportSize

Gets the size of the game viewport.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetViewportWidgetGeometry

Gets the geometry of the widget holding all widgets added to the "Viewport".  You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerScreenWidgetGeometry

Gets the geometry of the widget holding all widgets added to the "Player Screen". You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### GetMousePositionOnPlatform

Gets the platform's mouse cursor position.  This is the 'absolute' desktop location of the mouse.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMousePositionOnViewport

Gets the platform's mouse cursor position in the local space of the viewport widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetMousePositionScaledByDPI

Gets the mouse position of the player controller, scaled by the DPI.  If you're trying to go from raw mouse screenspace coordinates
	  to fullscreen widget space, you'll need to transform the mouse into DPI Scaled space.  This function performs that scaling.

	  MousePositionScaledByDPI = MousePosition  (1  ViewportScale).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` |  |
| LocationX | `float &` |  |
| LocationY | `float &` |  |

**Return**

- Type: 
- Description: _None_

### SlotAsBorderSlot

Gets the slot object on the child widget as a Border Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a border panel. |

**Return**

- Type: 
- Description: _None_

### SlotAsCanvasSlot

Gets the slot object on the child widget as a Canvas Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a canvas panel. |

**Return**

- Type: 
- Description: _None_

### SlotAsGridSlot

Gets the slot object on the child widget as a Grid Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a grid panel. |

**Return**

- Type: 
- Description: _None_

### SlotAsHorizontalBoxSlot

Gets the slot object on the child widget as a Horizontal Box Slot, allowing you to manipulate its information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a Horizontal Box. |

**Return**

- Type: 
- Description: _None_

### SlotAsOverlaySlot

Gets the slot object on the child widget as a Overlay Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a overlay panel. |

**Return**

- Type: 
- Description: _None_

### SlotAsUniformGridSlot

Gets the slot object on the child widget as a Uniform Grid Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a uniform grid panel. |

**Return**

- Type: 
- Description: _None_

### SlotAsVerticalBoxSlot

Gets the slot object on the child widget as a Vertical Box Slot, allowing you to manipulate its information.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` | The child widget of a Vertical Box. |

**Return**

- Type: 
- Description: _None_

### RemoveAllWidgets

Removes all widgets from the viewport.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SetNewUsedLayerPolicy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` |  |
| NewLayerPolicy | `int32` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

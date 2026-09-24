# UWidgetBlueprintLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### Create

Creates a widget

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| WidgetType | `TSubclassOf < UUserWidget >` |  |
| OwningPlayer | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### CreateDragDropOperation

Creates a new drag and drop operation that can be returned from a drag begin to inform the UI what i
	  being dragged and dropped and what it looks like.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OperationClass | `TSubclassOf < UDragDropOperation >` |  |

**Return**

- Type: 
- Description: _None_

### SetInputMode_UIOnly

Setup an input mode that allows only the UI to respond to user input.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `APlayerController *` |  |
| InWidgetToFocus | `UWidget *` |  |
| bLockMouseToViewport | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetInputMode_UIOnlyEx

Setup an input mode that allows only the UI to respond to user input.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `APlayerController *` |  |
| InWidgetToFocus | `UWidget *` |  |
| InMouseLockMode | [EMouseLockMode](../../cppenum/E/EM/EMouseLockMode.md) |  |

**Return**

- Type: 
- Description: _None_

### SetInputMode_GameAndUI

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `APlayerController *` |  |
| InWidgetToFocus | `UWidget *` |  |
| bLockMouseToViewport | `bool` |  |
| bHideCursorDuringCapture | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetInputMode_GameAndUIEx

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `APlayerController *` |  |
| InWidgetToFocus | `UWidget *` |  |
| InMouseLockMode | `EMouseLockMode` |  |
| bHideCursorDuringCapture | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetInputMode_GameOnly

Setup an input mode that allows only player input  player controller to respond to user input.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### SetFocusToGameViewport

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DrawBox

Draws a box

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FPaintContext &` |  |
| Position | `FVector2D` |  |
| Size | `FVector2D` |  |
| Brush | `USlateBrushAsset *` |  |
| Tint | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### DrawLine

Draws a line.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FPaintContext &` |  |
| PositionA | `FVector2D` | Starting position of the line in local space. |
| PositionB | `FVector2D` | Ending position of the line in local space. |
| Tint | `FLinearColor` | Color to render the line. |
| bAntiAlias | `bool` |  |

**Return**

- Type: 
- Description: _None_

### DrawLines

Draws several line segments.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FPaintContext &` |  |
| Points | `TArray < FVector2D > &` | Line pairs, each line needs to be 2 separate points in the array. |
| Tint | `FLinearColor` | Color to render the line. |
| bAntiAlias | `bool` |  |

**Return**

- Type: 
- Description: _None_

### DrawText

Draws text.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FPaintContext &` |  |
| InString | `FString &` | The string to draw. |
| Position | `FVector2D` | The starting position where the text is drawn in local space. |
| Tint | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color to render the line. |

**Return**

- Type: 
- Description: _None_

### DrawTextFormatted

Draws text.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Context | `FPaintContext &` |  |
| Text | `FText &` | The string to draw. |
| Position | `FVector2D` | The starting position where the text is drawn in local space. |
| Font | `UFont *` |  |
| FontSize | `int32` |  |
| FontTypeFace | `FName` |  |
| Tint | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color to render the line. |

**Return**

- Type: 
- Description: _None_

### Handled

The event reply to use when you choose to handle an event.  This will prevent the event
	  from continuing to bubble up  down the widget hierarchy.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Unhandled

The event reply to use when you choose not to handle an event.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CaptureMouse

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| CapturingWidget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### ReleaseMouseCapture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |

**Return**

- Type: 
- Description: _None_

### LockMouse

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| CapturingWidget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### UnlockMouse

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |

**Return**

- Type: 
- Description: _None_

### SetUserFocus

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| FocusWidget | `UWidget *` |  |
| bInAllUsers | `bool` |  |

**Return**

- Type: 
- Description: _None_

### CaptureJoystick

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| CapturingWidget | `UWidget *` |  |
| bInAllJoysticks | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClearUserFocus

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| bInAllUsers | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ReleaseJoystickCapture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| bInAllJoysticks | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetMousePosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| NewMousePosition | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### DetectDrag

Ask Slate to detect if a user starts dragging in this widget later.  Slate internally tracks the movement
	  and if it surpasses the drag threshold, Slate will send an OnDragDetected event to the widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |
| WidgetDetectingDrag | `UWidget *` | Detect dragging in this widget |
| DragKey | `FKey` | This button should be pressed to detect the drag |

**Return**

- Type: 
- Description: _None_

### DetectDragIfPressed

Given the pointer event, emit the DetectDrag reply if the provided key was pressed.
	  If the DragKey is a touch key, that will also automatically work.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointerEvent | `FPointerEvent &` | The pointer device event coming in. |
| WidgetDetectingDrag | `UWidget *` | Detect dragging in this widget. |
| DragKey | `FKey` | This button should be pressed to detect the drag, won't emit the DetectDrag FEventReply unless this is pressed. |

**Return**

- Type: 
- Description: _None_

### EndDragDrop

An event should return FReply::Handled().EndDragDrop() to request that the current dragdrop operation be terminated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reply | `FEventReply &` |  |

**Return**

- Type: 
- Description: _None_

### IsDragDropping

Returns true if a dragdrop event is occurring that a widget can handle.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDragDroppingContent

Returns the drag and drop operation that is currently occurring if any, otherwise nothing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CancelDragDrop

Cancels any current drag drop operation.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MakeBrushFromAsset

Creates a Slate Brush from a Slate Brush Asset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BrushAsset | `USlateBrushAsset *` |  |

**Return**

- Type: 
- Description: _None_

### MakeBrushFromTexture

Creates a Slate Brush from a Texture2D

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` |  |
| Width | `int32` | When less than or equal to zero, the Width of the brush will default to the Width of the Texture |
| Height | `int32` | When less than or equal to zero, the Height of the brush will default to the Height of the Texture |

**Return**

- Type: 
- Description: _None_

### MakeBrushFromMaterial

Creates a Slate Brush from a Material.  Materials don't have an implicit size, so providing a widget and height
	  is required to hint slate with how large the image wants to be by default.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` |  |
| Width | `int32` |  |
| Height | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetBrushResource

Gets the resource object on a brush.  This could be a UTexture2D or a UMaterialInterface.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### GetBrushResourceConst

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### GetBrushResourceAsTexture2D

Gets the brush resource as a texture 2D.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### GetBrushResourceAsMaterial

Gets the brush resource as a material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushResourceToTexture

Sets the resource on a brush to be a UTexture2D.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |
| Texture | `UTexture2D *` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushResourceToMaterial

Sets the resource on a brush to be a Material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### NoResourceBrush

Creates a Slate Brush that wont draw anything, the "Null Brush".

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDynamicMaterial

Gets the material that allows changes to parameters at runtime.  The brush must already have a material assigned to it,
	  if it does it will automatically be converted to a MID.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Brush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### DismissAllMenus

Closes any popup menu

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAllWidgetsOfClass

Find all widgets of a certain class.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| FoundWidgets | `TArray < UUserWidget * > &` | The widgets that were found matching the filter. |
| WidgetClass | `TSubclassOf < UUserWidget >` | The widget class to filter by. |
| TopLevelOnly | `bool` | Only the widgets that are direct children of the viewport will be returned. |

**Return**

- Type: 
- Description: _None_

### GetAllWidgetsWithInterface

Find all widgets in the world with the specified interface.
	 This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Interface | `TSubclassOf < UInterface >` | The interface to find. Must be specified or result array will be empty. |
| FoundWidgets | `TArray < UUserWidget * > &` | Output array of widgets that implement the specified interface. |
| TopLevelOnly | `bool` | Only the widgets that are direct children of the viewport will be returned. |

**Return**

- Type: 
- Description: _None_

### GetInputEventFromKeyEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Event | `FKeyEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetKeyEventFromAnalogInputEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Event | `FAnalogInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetInputEventFromCharacterEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Event | `FCharacterEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetInputEventFromPointerEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Event | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetInputEventFromNavigationEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Event | `FNavigationEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetSafeZonePadding

Gets the amount of padding that needs to be added when accounting for the safe zone on TVs.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| SafePadding | `FVector2D &` |  |
| SafePaddingScale | `FVector2D &` |  |
| SpillOverPadding | `FVector2D &` |  |

**Return**

- Type: 
- Description: _None_

### SetHardwareCursor

Loads or sets a hardware cursor from the content directory in the game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| CursorShape | `EMouseCursor :: Type` |  |
| CursorName | `FName` |  |
| HotSpot | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### ApplyUserWidgetSkin

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UserWidget | `UUserWidget *` |  |
| SkinPathPtr | `TSoftClassPtr < UUserWidgetSkin >` |  |
| bAsyncLoad | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RevertUserWidgetSkin

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UserWidget | `UUserWidget *` |  |
| SkinPathPtr | `TSoftClassPtr < UUserWidgetSkin >` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

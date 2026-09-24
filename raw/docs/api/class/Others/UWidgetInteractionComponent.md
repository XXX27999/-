# UWidgetInteractionComponent

This is a component to allow interaction with the Widget Component.  This class allows you to
  simulate a sort of laser pointer device, when it hovers over widgets it will send the basic signals
  to show as if the mouse were moving on top of it.  You'll then tell the component to simulate key presses,
  like Left Mouse, down and up, to simulate a mouse click.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| VirtualUserIndex | `int32` | Represents the Virtual User Index.  Each virtual user should be represented by a different<br>	  index number, this will maintain separate capture and focus states for them.  Each<br>	  controller or finger-tip should get a unique PointerIndex. |
| PointerIndex | `float` | Each user virtual controller or virtual finger tips being simulated should use a different pointer index. |
| TraceChannel | `TEnumAsByte < ECollisionChannel >` | The trace channel to use when tracing for widget components in the world. |
| InteractionDistance | `float` | The distance in game units the component should be able to interact with a widget component. |
| InteractionSource | [EWidgetInteractionSource](../../cppenum/E/EW/EWidgetInteractionSource.md) | Should we project from the world location of the component?  If you set this to false, you'll<br>	  need to call SetCustomHitResult(), and provide the result of a custom hit test form whatever<br>	  location you wish. |
| bEnableHitTesting | `bool` | Should the interaction component perform hit testing (Automatic or Custom) and attempt to<br>	  simulate hover - if you were going to emulate a keyboard you would want to turn this option off<br>	  if the virtual keyboard was separate from the virtual pointer device and used a second interaction<br>	  component. |
| bSimulateTouchEvents | `bool` | When true, pointer events will be sent as touch events instead of mouse events.<br>	  This enables drag-scrolling on ScrollBoxListView widgets in 3D UI,<br>	  since those widgets only respond to touch-based drag gestures. |
| bShowDebug | `bool` | Shows some debugging lines and a hit sphere to help you debug interactions. |
| DebugColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Determines the color of the debug lines. |
| CustomHitResult | [FHitResult](../../cppstruct/F/FH/FHitResult.md) | Stores the custom hit result set by the player. |
| LocalHitLocation | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The 2D location on the widget component that was hit. |
| LastLocalHitLocation | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The last 2D location on the widget component that was hit. |
| HoveredWidgetComponent | `UWidgetComponent *` | The widget component we're currently hovering over. |
| LastHitResult | [FHitResult](../../cppstruct/F/FH/FHitResult.md) | The last hit result we used. |
| bIsHoveredWidgetInteractable | `bool` | Are we hovering over any interactive widgets. |
| bIsHoveredWidgetFocusable | `bool` | Are we hovering over any focusable widget? |
| bIsHoveredWidgetHitTestVisible | `bool` | Are we hovered over a widget that is hit test visible? |

## Functions

### PressPointerKey

Presses a key as if the mousepointer were the source of it.  Normally you would just use
	  LeftRight mouse button for the Key.  However - advanced uses could also be imagined where you
	  send other keys to signal widgets to take special actions if they're under the cursor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### ReleasePointerKey

Releases a key as if the mousepointer were the source of it.  Normally you would just use
	  LeftRight mouse button for the Key.  However - advanced uses could also be imagined where you
	  send other keys to signal widgets to take special actions if they're under the cursor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### PressKey

Press a key as if it had come from the keyboard.  Avoid using this for 'a-z|A-Z', things like
	  the Editable Textbox in Slate expect OnKeyChar to be called to signal a specific character being
	  send to the widget.  So for those cases you should use SendKeyChar.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |
| bRepeat | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ReleaseKey

Releases a key as if it had been released by the keyboard.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### PressAndReleaseKey

Does both the press and release of a simulated keyboard key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### SendKeyChar

Transmits a list of characters to a widget by simulating a OnKeyChar event for each key listed in
	  the string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Characters | `FString` |  |
| bRepeat | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ScrollWheel

Sends a scroll wheel event to the widget under the last hit result.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScrollDelta | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetHoveredWidgetComponent

Get the currently hovered widget component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOverInteractableWidget

Returns true if a widget under the hit result is interactive.  e.g. Slate widgets
	  that return true for IsInteractable().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOverFocusableWidget

Returns true if a widget under the hit result is focusable.  e.g. Slate widgets that
	  return true for SupportsKeyboardFocus().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOverHitTestVisibleWidget

Returns true if a widget under the hit result is has a visibility that makes it hit test
	  visible.  e.g. Slate widgets that return true for GetVisibility().IsHitTestVisible().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLastHitResult

Gets the last hit result generated by the component.  Returns the custom hit result if that was set.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Get2DHitLocation

Gets the last hit location on the widget in 2D, local pixel units of the render target.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCustomHitResult

Set custom hit result.  This is only taken into account if InteractionSource is set to EWidgetInteractionSource::Custom.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnHoveredWidgetChanged |  | Called when the hovered Widget Component changes.  The interaction component functions at the Slate<br>	  level - so it's unable to report anything about what UWidget is under the hit result. |

## Language

cpp

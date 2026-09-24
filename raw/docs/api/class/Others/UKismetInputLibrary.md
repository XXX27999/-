# UKismetInputLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### CalibrateTilt

Calibrate the tilt for the input device

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EqualEqual_KeyKey

Test if the input key are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FKey` | - The key to compare against |
| B | `FKey` | - The key to compare |

**Return**

- Type: 
- Description: _None_

### EqualEqual_InputChordInputChord

Test if the input chords are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FInputChord` | - The chord to compare against |
| B | [FInputChord](../../cppstruct/F/FI/FInputChord.md) | - The chord to compare |

**Return**

- Type: 
- Description: _None_

### Key_IsModifierKey

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### Key_IsGamepadKey

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### Key_IsMouseButton

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### Key_IsKeyboardKey

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### Key_IsFloatAxis

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### Key_IsVectorAxis

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### Key_GetDisplayName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsRepeat

Returns whether or not this character is an auto-repeated keystroke

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsShiftDown

Returns true if either shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsLeftShiftDown

Returns true if left shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsRightShiftDown

Returns true if right shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsControlDown

Returns true if either control key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsLeftControlDown

Returns true if left control key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsRightControlDown

Returns true if left control key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsAltDown

Returns true if either alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsLeftAltDown

Returns true if left alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsRightAltDown

Returns true if right alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsCommandDown

Returns true if either command key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsLeftCommandDown

Returns true if left command key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### InputEvent_IsRightCommandDown

Returns true if right command key was down when this event occurred

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetKeyByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetKey

Returns the key for this event.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FKeyEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetUserIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FKeyEvent &` |  |

**Return**

- Type: 
- Description: _None_

### GetAnalogValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FAnalogInputEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetScreenSpacePosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetLastScreenSpacePosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetCursorDelta

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_IsMouseButtonDown

Mouse buttons that are currently pressed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |
| MouseButton | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetEffectingButton

Mouse button that caused this event to be raised (possibly EB_None)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetWheelDelta

How much did the mouse wheel turn since the last mouse event

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetUserIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetPointerIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetTouchpadIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_IsTouchEvent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_TouchForce

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetGestureType

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### PointerEvent_GetGestureDelta

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Input | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UInputComponent

Implement an Actor component for input bindings.

  An Input Component is a transient component that enables an Actor to bind various forms of input events to delegate functions.
  Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
  Each binding can consume the input event preventing other components on the input stack from processing the input.

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

_None_

## Functions

### IsControllerKeyDown

Returns true if the given keybutton is pressed on the input of the controller (if present)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### WasControllerKeyJustPressed

Returns true if the given keybutton was up last frame and down this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### WasControllerKeyJustReleased

Returns true if the given keybutton was down last frame and up this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetControllerAnalogKeyState

Returns the analog value for the given keybutton.  If analog isn't supported, returns 1 for down and 0 for up.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetControllerVectorKeyState

Returns the vector value for the given keybutton.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetTouchState

Returns the location of a touch, and if it's held down

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `int32` |  |
| LocationX | `float &` |  |
| LocationY | `float &` |  |
| bIsCurrentlyPressed | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### GetControllerKeyTimeDown

Returns how long the given keybutton has been down.  Returns 0 if it's up or it just went down this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetControllerMouseDelta

Retrieves how far the mouse moved this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaX | `float &` |  |
| DeltaY | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetControllerAnalogStickState

Retrieves the X and Y displacement of the given analog stick.  For WhickStick, 0 = left, 1 = right.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WhichStick | `EControllerAnalogStick :: Type` |  |
| StickX | `float &` |  |
| StickY | `float &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

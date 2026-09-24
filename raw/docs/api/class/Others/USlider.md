# USlider

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.

   No Children

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` | The volume value to display. |
| ValueDelegate | `FGetFloat` | A bindable delegate to allow logic to drive the value of the widget |
| WidgetStyle | [FSliderStyle](../../cppstruct/F/FS/FSliderStyle.md) | The progress bar style |
| Orientation | `TEnumAsByte < EOrientation >` | The slider's orientation. |
| SliderBarColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color to draw the slider bar in. |
| SliderHandleColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color to draw the slider handle in. |
| IndentHandle | `bool` | Whether the slidable area should be indented to fit the handle. |
| Locked | `bool` | Whether the handle is interactive or fixed. |
| StepSize | `float` | The amount to adjust the value by, when using a controller or keyboard |
| IsFocusable | `bool` | Should the slider be focusable? |
| SupportClickChange | `bool` |  |

## Functions

### GetValue

Gets the current value of the slider.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetValue

Sets the current value of the slider.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetIndentHandle

Sets if the slidable area should be indented to fit the handle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetLocked

Sets the handle to be interactive or fixed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetStepSize

Sets the amount to adjust the value by, when using a controller or keyboard

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetSliderBarColor

Sets the color of the slider bar

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetSliderHandleColor

Sets the color of the handle bar

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InValue | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnMouseCaptureBegin |  | Invoked when the mouse is pressed and a capture begins. |
| OnMouseCaptureEnd |  | Invoked when the mouse is released and a capture ends. |
| OnControllerCaptureBegin |  | Invoked when the controller capture begins. |
| OnControllerCaptureEnd |  | Invoked when the controller capture ends. |
| OnValueChanged |  | Called when the value is changed by slider or typing. |

## Language

cpp

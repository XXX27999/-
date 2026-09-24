# USpinBox

A numerical entry box that allows for direct entry of the number or allows the user to click and slide the number.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` | Value stored in this spin box |
| ValueDelegate | `FGetFloat` | A bindable delegate to allow logic to drive the value of the widget |
| WidgetStyle | [FSpinBoxStyle](../../cppstruct/F/FS/FSpinBoxStyle.md) | The Style |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` |  |
| Delta | `float` | The amount by which to change the spin box value as the slider moves. |
| SliderExponent | `float` | The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta). |
| Font | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | Font color and opacity (overrides style) |
| Justification | `TEnumAsByte < ETextJustify :: Type >` | The justification the value text should appear as. |
| MinDesiredWidth | `float` | The minimum width of the spin box |
| ClearKeyboardFocusOnCommit | `bool` | Whether to remove the keyboard focus from the spin box when the value is committed |
| SelectAllTextOnCommit | `bool` | Whether to select the text in the spin box when the value is committed |
| ForegroundColor | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) |  |
| bOverride_MinValue | `uint32` | Whether the optional MinValue attribute of the widget is set |
| bOverride_MaxValue | `uint32` | Whether the optional MaxValue attribute of the widget is set |
| bOverride_MinSliderValue | `uint32` | Whether the optional MinSliderValue attribute of the widget is set |
| bOverride_MaxSliderValue | `uint32` | Whether the optional MaxSliderValue attribute of the widget is set |
| MinValue | `float` | The minimum allowable value that can be manually entered into the spin box |
| MaxValue | `float` | The maximum allowable value that can be manually entered into the spin box |
| MinSliderValue | `float` | The minimum allowable value that can be specified using the slider |
| MaxSliderValue | `float` | The maximum allowable value that can be specified using the slider |

## Functions

### GetValue

Get the current value of the spin box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetValue

Set the value of the spin box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetMinValue

Get the current minimum value that can be manually set in the spin box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMinValue

Set the minimum value that can be manually set in the spin box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMinValue

Clear the minimum value that can be manually set in the spin box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaxValue

Get the current maximum value that can be manually set in the spin box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMaxValue

Set the maximum value that can be manually set in the spin box.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMaxValue

Clear the maximum value that can be manually set in the spin box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMinSliderValue

Get the current minimum value that can be specified using the slider.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMinSliderValue

Set the minimum value that can be specified using the slider.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMinSliderValue

Clear the minimum value that can be specified using the slider.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMaxSliderValue

Get the current maximum value that can be specified using the slider.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMaxSliderValue

Set the maximum value that can be specified using the slider.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMaxSliderValue

Clear the maximum value that can be specified using the slider.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForegroundColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InForegroundColor | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnValueChanged |  | Called when the value is changed interactively by the user |
| OnValueCommitted |  | Called when the value is committed. Occurs when the user presses Enter or the text box loses focus. |
| OnBeginSliderMovement |  | Called right before the slider begins to move |
| OnEndSliderMovement |  | Called right after the slider handle is released by the user |

## Language

cpp

# UCheckBox

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and
  'indeterminable.  You can use the checkbox for a classic checkbox, or as a toggle button,
  or as radio buttons.

   Single Child
   Toggle

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CheckedState | [ECheckBoxState](../../cppenum/E/EC/ECheckBoxState.md) | Whether the check box is currently in a checked state |
| CheckedStateDelegate | `FGetCheckBoxState` | A bindable delegate for the IsChecked. |
| WidgetStyle | [FCheckBoxStyle](../../cppstruct/F/FC/FCheckBoxStyle.md) | The checkbox bar style |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` | Style of the check box |
| UncheckedImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is unchecked |
| UncheckedHoveredImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is unchecked and hovered |
| UncheckedPressedImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is unchecked and pressed |
| CheckedImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is checked |
| CheckedHoveredImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is checked and hovered |
| CheckedPressedImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is checked and pressed |
| UndeterminedImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is in an ambiguous state and hovered |
| UndeterminedHoveredImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is checked and hovered |
| UndeterminedPressedImage_DEPRECATED | `USlateBrushAsset *` | Image to use when the checkbox is in an ambiguous state and pressed |
| HorizontalAlignment | `TEnumAsByte < EHorizontalAlignment >` | How the content of the toggle button should align within the given space |
| Padding_DEPRECATED | [FMargin](../../cppstruct/F/FM/FMargin.md) | Spacing between the check box image and its content |
| BorderBackgroundColor_DEPRECATED | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) | The color of the background border |
| IsFocusable | `bool` | Sometimes a button should only be mouse-clickable and never keyboard focusable. |
| ClickMethod | `TEnumAsByte < EButtonClickMethod :: Type >` | The type of mouse action required by the user to trigger the buttons 'Click' |
| TouchMethod | `TEnumAsByte < EButtonTouchMethod :: Type >` | The type of touch action required by the user to trigger the buttons 'Click' |

## Functions

### IsPressed

Returns true if this button is currently pressed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsChecked

Returns true if the checkbox is currently checked

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCheckedState

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsChecked

Sets the checked state.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsChecked | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetCheckedState

Sets the checked state.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCheckedState | [ECheckBoxState](../../cppenum/E/EC/ECheckBoxState.md) |  |

**Return**

- Type: 
- Description: _None_

### SetClickMethod

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InClickMethod | `EButtonClickMethod :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetTouchMethod

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTouchMethod | `EButtonTouchMethod :: Type` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnCheckStateChanged |  | Called when the checked state has changed |

## Language

cpp

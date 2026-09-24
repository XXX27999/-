# UComboBoxKey

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.
  Use OnGenerateConentWidgetEvent to return a custom built widget.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Options | `TArray < TSharedPtr < FName > >` | . |
| SelectedOption | `TSharedPtr < FName >` |  |
| WidgetStyle | [FComboBoxStyle](../../cppstruct/F/FC/FComboBoxStyle.md) | The combobox style. |
| ItemStyle | [FTableRowStyle](../../cppstruct/F/FT/FTableRowStyle.md) | The item row style. |
| ScrollBarStyle | [FScrollBarStyle](../../cppstruct/F/FS/FScrollBarStyle.md) | The scroll bar style. |
| ForegroundColor | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) | The foreground color to pass through the hierarchy. |
| ContentPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |
| MaxListHeight | `float` | The max height of the combobox list that opens |
| bHasDownArrow | `bool` | When false, the down arrow is not generated and it is up to the API consumer<br>	  to make their own visual hint that this is a drop down. |
| bEnableGamepadNavigationMode | `bool` | When false, directional keys will change the selection. When true, ComboBox<br>	  must be activated and will only capture arrow input while activated. |
| bIsFocusable | `bool` | When true, allows the combo box to receive keyboard focus |

## Functions

### AddOption

Add an element to the option list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FName` |  |

**Return**

- Type: 
- Description: _None_

### RemoveOption

Remove an element to the option list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ClearOptions

Remove all the elements of the option list.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearSelection

Clear the current selection.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSelectedOption

Set the current selected option.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetSelectedOption

Get the current selected option

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOpen

Is the combobox menu opened.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetContentPadding

Set the padding for content.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |

**Return**

- Type: 
- Description: _None_

### GetContentPadding

Get the padding for content.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsEnableGamepadNavigationMode

Is the combobox navigated by gamepad.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEnableGamepadNavigationMode

Set whether the combobox is navigated by gamepad.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InEnableGamepadNavigationMode | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsHasDownArrow

Is the combobox arrow showing.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetHasDownArrow

Set whether the combobox arrow is showing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InHasDownArrow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetMaxListHeight

Get the maximum height of the combobox list.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMaxListHeight

Set the maximum height of the combobox list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaxHeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetWidgetStyle

Get the style of the combobox.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWidgetStyle

Set the style of the combobox.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWidgetStyle | `FComboBoxStyle &` |  |

**Return**

- Type: 
- Description: _None_

### GetItemStyle

Get the style of the items.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetItemStyle

Set the style of the items.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InItemStyle | `FTableRowStyle &` |  |

**Return**

- Type: 
- Description: _None_

### GetScrollBarStyle

Get the style of the scrollbar.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsFocusable

Is the combobox focusable.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetForegroundColor

Get the foreground color of the button.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnGenerateContentWidget |  | Called when the widget is needed for the content. |
| OnGenerateItemWidget |  | Called when the widget is needed for the item. |
| OnSelectionChanged |  | Called when a new item is selected in the combobox. |
| OnOpening |  | Called when the combobox is opening |

## Language

cpp

# UComboBoxString

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| DefaultOptions | `TArray < FString >` | The default list of items to be displayed on the combobox. |
| SelectedOption | `FString` | The item in the combobox to select by default |
| WidgetStyle | [FComboBoxStyle](../../cppstruct/F/FC/FComboBoxStyle.md) | The style. |
| ItemStyle | [FTableRowStyle](../../cppstruct/F/FT/FTableRowStyle.md) | The item row style. |
| ScrollBarStyle | [FScrollBarStyle](../../cppstruct/F/FS/FScrollBarStyle.md) | The scroll bar style. |
| ContentPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |
| MaxListHeight | `float` | The max height of the combobox list that opens |
| HasDownArrow | `bool` | When false, the down arrow is not generated and it is up to the API consumer<br>	  to make their own visual hint that this is a drop down. |
| EnableGamepadNavigationMode | `bool` | When false, directional keys will change the selection. When true, ComboBox<br>	 must be activated and will only capture arrow input while activated. |
| Font | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | The default font to use in the combobox, only applies if you're not implementing OnGenerateWidgetEvent<br>	  to factory each new entry. |
| ForegroundColor | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) | The foreground color to pass through the hierarchy. |
| bIsFocusable | `bool` |  |
| bForceNotify | `bool` |  |
| OnGenerateWidgetEvent | `FGenerateWidgetForString` | Called when the widget is needed for the item. |
| OnGenerateSelectWidgetEvent | `FGenerateWidgetForString` |  |

## Functions

### AddOption

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### RemoveOption

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### FindOptionIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetOptionAtIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ClearOptions

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearSelection

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RefreshOptions

Refreshes the list of options.  If you added new ones, and want to update the list even if it's
	  currently being displayed use this.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSelectedOption

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Option | `FString` |  |

**Return**

- Type: 
- Description: _None_

### GetSelectedOption

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOptionCount

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
| OnSelectionChanged |  | Called when a new item is selected in the combobox. |
| OnOpening |  | Called when the combobox is opening |
| OnClosing |  | Called when the combobox is closing |

## Language

cpp

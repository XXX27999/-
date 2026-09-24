# UInputKeySelector

A widget for selecting a single key or a single key with a modifier.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| WidgetStyle | [FButtonStyle](../../cppstruct/F/FB/FButtonStyle.md) | The button style used at runtime |
| TextStyle | [FTextBlockStyle](../../cppstruct/F/FT/FTextBlockStyle.md) | The button style used at runtime |
| SelectedKey | [FInputChord](../../cppstruct/F/FI/FInputChord.md) | The currently selected key chord. |
| Font_DEPRECATED | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) |  |
| Margin | [FMargin](../../cppstruct/F/FM/FMargin.md) | The amount of blank space around the text used to display the currently selected key. |
| ColorAndOpacity_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |
| KeySelectionText | `FText` | Sets the text which is displayed while selecting keys. |
| NoKeySpecifiedText | `FText` | Sets the text to display when no key text is available or not selecting a key. |
| bAllowModifierKeys | `bool` | When true modifier keys such as control and alt are allowed in the<br>	 input chord representing the selected key, if false modifier keys are ignored. |
| bAllowGamepadKeys | `bool` | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |
| EscapeKeys | `TArray < FKey >` | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |

## Functions

### SetSelectedKey

Sets the currently selected key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSelectedKey | `FInputChord &` |  |

**Return**

- Type: 
- Description: _None_

### SetKeySelectionText

Sets the text which is displayed while selecting keys.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InKeySelectionText | `FText` |  |

**Return**

- Type: 
- Description: _None_

### SetNoKeySpecifiedText

Sets the text to display when no key text is available or not selecting a key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNoKeySpecifiedText | `FText` |  |

**Return**

- Type: 
- Description: _None_

### SetAllowModifierKeys

Sets whether or not modifier keys are allowed in the selected key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInAllowModifierKeys | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllowGamepadKeys

Sets whether or not gamepad keys are allowed in the selected key.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInAllowGamepadKeys | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetIsSelectingKey

Returns true if the widget is currently selecting a key, otherwise returns false.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTextBlockVisibility

Sets the visibility of the text block.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVisibility | [ESlateVisibility](../../cppenum/E/ES/ESlateVisibility.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnKeySelected |  | Called whenever a new key is selected by the user. |
| OnIsSelectingKeyChanged |  | Called whenever the key selection mode starts or stops. |

## Language

cpp

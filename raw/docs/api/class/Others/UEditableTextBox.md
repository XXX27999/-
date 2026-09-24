# UEditableTextBox

Allows the user to type in custom text.  Only permits a single line of text to be entered.

   No Children
   Text Entry

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` | The text content for this editable text box widget |
| TextDelegate | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| WidgetStyle | [FEditableTextBoxStyle](../../cppstruct/F/FE/FEditableTextBoxStyle.md) | The style |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` | Style used for the text box |
| HintText | `FText` | Hint text that appears when there is no text in the text box |
| HintTextDelegate | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| Font_DEPRECATED | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | Font color and opacity (overrides Style) |
| ForegroundColor_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Text color and opacity (overrides Style) |
| BackgroundColor_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color of the backgroundborder around the editable text (overrides Style) |
| ReadOnlyForegroundColor_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Text color and opacity when read-only (overrides Style) |
| IsReadOnly | `bool` | Sets whether this text box can actually be modified interactively by the user |
| IsPassword | `bool` | Sets whether this text box is for storing a password |
| MinimumDesiredWidth | `float` | Minimum width that a text block should be |
| Padding_DEPRECATED | [FMargin](../../cppstruct/F/FM/FMargin.md) | Padding between the boxborder and the text widget inside (overrides Style) |
| IsCaretMovedWhenGainFocus | `bool` | Workaround as we lose focus when the auto completion closes. |
| SelectAllTextWhenFocused | `bool` | Whether to select all text when the user clicks to give focus on the widget |
| RevertTextOnEscape | `bool` | Whether to allow the user to back out of changes when they press the escape key |
| ClearKeyboardFocusOnCommit | `bool` | Whether to clear keyboard focus when pressing enter to commit changes |
| SelectAllTextOnCommit | `bool` | Whether to select all text when pressing enter to commit changes |
| AllowContextMenu | `bool` | Whether the context menu can be opened |
| KeyboardType | `TEnumAsByte < EVirtualKeyboardType :: Type >` | If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use? |
| ShapedTextOptions | [FShapedTextOptions](../../cppstruct/F/FS/FShapedTextOptions.md) | Controls how the text within this widget should be shaped. |

## Functions

### GetText

Provide a alternative mechanism for error reporting.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText` |  |

**Return**

- Type: 
- Description: _None_

### SetHintText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText` |  |

**Return**

- Type: 
- Description: _None_

### SetError

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InError | `FText` |  |

**Return**

- Type: 
- Description: _None_

### SetIsReadOnly

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bReadOnly | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClearError

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasError

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
| OnTextChanged |  | Called whenever the text is changed interactively by the user |
| OnTextCommitted |  | Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus. |

## Language

cpp

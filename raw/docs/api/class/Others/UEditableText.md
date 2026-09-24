# UEditableText

Editable text box widget

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` | The text content for this editable text box widget |
| TextDelegate | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| HintText | `FText` | Hint text that appears when there is no text in the text box |
| HintTextDelegate | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| WidgetStyle | [FEditableTextStyle](../../cppstruct/F/FE/FEditableTextStyle.md) | The style |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` | Text style |
| BackgroundImageSelected_DEPRECATED | `USlateBrushAsset *` | Background image for the selected text (overrides Style) |
| BackgroundImageComposing_DEPRECATED | `USlateBrushAsset *` | Background image for the composing text (overrides Style) |
| CaretImage_DEPRECATED | `USlateBrushAsset *` | Image brush used for the caret (overrides Style) |
| Font_DEPRECATED | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | Font color and opacity (overrides Style) |
| ColorAndOpacity_DEPRECATED | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) | Text color and opacity (overrides Style) |
| IsReadOnly | `bool` | Sets whether this text box can actually be modified interactively by the user |
| IsPassword | `bool` | Sets whether this text box is for storing a password |
| MinimumDesiredWidth | `float` | Minimum width that a text block should be |
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

Gets the widget text

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetText

Directly sets the widget text.
	  Warning: This will wipe any binding created for the Text property!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InText | `FText` | The text to assign to the widget |

**Return**

- Type: 
- Description: _None_

### SetIsPassword

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbIsPassword | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetHintText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InHintText | `FText` |  |

**Return**

- Type: 
- Description: _None_

### SetIsReadOnly

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbIsReadyOnly | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetFont

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Font | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### SetColorAndOpacity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Color | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) |  |

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
| OnTextBeginEditTransation |  | Called to begin an undoable editable text transaction |
| OnTextEndEditTransaction |  | Called to end an undoable editable text transaction |
| OnTextFocusReceived |  |  |

## Language

cpp

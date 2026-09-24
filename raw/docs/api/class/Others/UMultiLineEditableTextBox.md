# UMultiLineEditableTextBox

Allows a user to enter multiple lines of text

## Parents

- [UTextLayoutWidget](./UTextLayoutWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` | The text content for this editable text box widget |
| HintText | `FText` | Hint text that appears when there is no text in the text box |
| HintTextDelegate | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| WidgetStyle | [FEditableTextBoxStyle](../../cppstruct/F/FE/FEditableTextBoxStyle.md) | The style |
| TextStyle | [FTextBlockStyle](../../cppstruct/F/FT/FTextBlockStyle.md) | The text style |
| bIsReadOnly | `bool` | Sets whether this text block can be modified interactively by the user |
| AllowContextMenu | `bool` | Whether the context menu can be opened |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` |  |
| Font_DEPRECATED | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | Font color and opacity (overrides Style) |
| ForegroundColor_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Text color and opacity (overrides Style) |
| BackgroundColor_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color of the backgroundborder around the editable text (overrides Style) |
| ReadOnlyForegroundColor_DEPRECATED | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Text color and opacity when read-only (overrides Style) |

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

### SetIsEnableMultiLineTextInsertNewLine

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

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

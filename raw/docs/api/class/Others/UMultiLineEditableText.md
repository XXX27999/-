# UMultiLineEditableText

Editable text box widget

## Parents

- [UTextLayoutWidget](./UTextLayoutWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` | The text content for this editable text box widget |
| HintText | `FText` | Hint text that appears when there is no text in the text box |
| HintTextDelegate | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| WidgetStyle | [FTextBlockStyle](../../cppstruct/F/FT/FTextBlockStyle.md) | The style |
| bIsReadOnly | `bool` | Sets whether this text block can be modified interactively by the user |
| Font_DEPRECATED | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | Font color and opacity (overrides Style) |
| AllowContextMenu | `bool` | Whether the context menu can be opened |
| UseModiferKeyForNewLine | `bool` |  |

## Functions

### GetText

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
| InHintText | `FText` |  |

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

### SetWidgetStyle

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWidgetStyle | `FTextBlockStyle &` |  |

**Return**

- Type: 
- Description: _None_

### SetModiferKeyForNewLine

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bReadOnly | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetWrapTextAt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWrapTextAt | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFont

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFontInfo | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) |  |

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
| OnTextFocusReceived |  | Called when editable text received focus |

## Language

cpp

# UTextBlock

A simple static text widget.

   No Children
   Text

## Parents

- [UTextLayoutWidget](./UTextLayoutWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` | The text to display |
| TextDelegate | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| ColorAndOpacity | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) | The color of the text |
| ColorAndOpacityDelegate | `FGetSlateColor` | A bindable delegate for the ColorAndOpacity. |
| Font | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | The font to render the text with |
| ShadowOffset | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The direction the shadow is cast |
| ShadowColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The color of the shadow |
| ShadowColorAndOpacityDelegate | `FGetLinearColor` | A bindable delegate for the ShadowColorAndOpacity. |
| MinDesiredWidth | `float` | The minimum desired size for the text |
| AutoEllipsisText | `bool` |  |
| MutiEllipsisText | `bool` |  |
| MutiEllipsisLine | `int32` |  |
| bWrapWithInvalidationPanel | `bool` | If true, it will automatically wrap this text widget with an invalidation panel |

## Functions

### SetColorAndOpacity

Sets the color and opacity of the text in this text block

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColorAndOpacity | [FSlateColor](../../cppstruct/F/FS/FSlateColor.md) | The new text color and opacity |

**Return**

- Type: 
- Description: _None_

### SetColorRGBStr

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HexString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### SetOpacity

Sets the opacity of the text in this text block

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOpacity | `float` | The new text opacity |

**Return**

- Type: 
- Description: _None_

### SetShadowColorAndOpacity

Sets the color and opacity of the text drop shadow
	  Note: if opacity is zero no shadow will be drawn

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InShadowColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The new drop shadow color and opacity |

**Return**

- Type: 
- Description: _None_

### SetShadowOffset

Sets the offset that the text drop shadow should be drawn at

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InShadowOffset | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The new offset |

**Return**

- Type: 
- Description: _None_

### SetFont

Dynamically set the font info for this text block

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFontInfo | [FSlateFontInfo](../../cppstruct/F/FS/FSlateFontInfo.md) | THe new font info |

**Return**

- Type: 
- Description: _None_

### SetJustification

Set the text justification for this text block

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InJustification | `ETextJustify :: Type` | new justification |

**Return**

- Type: 
- Description: _None_

### SetVerticalJustification

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InJustification | `ETextVerticalJustify :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetNeedVerticalJustificationWhenOverflow

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetMinDesiredWidth

Set the minimum desired width for this text block

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMinDesiredWidth | `float` | new minimum desired width |

**Return**

- Type: 
- Description: _None_

### SetAutoEllipsisText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAutoEllipsisText | `bool` |  |

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

### SetMutiEllipsisText

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMutiEllipsisText | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetText

Gets the widget text

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalText

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


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnTextBlockTextChangeDelegate |  |  |

## Language

cpp

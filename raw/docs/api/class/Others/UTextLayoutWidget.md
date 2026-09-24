# UTextLayoutWidget

Base class for all widgets that use a text layout.
  Contains the common options that should be exposed for the underlying Slate widget.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ShapedTextOptions | [FShapedTextOptions](../../cppstruct/F/FS/FShapedTextOptions.md) | Controls how the text within this widget should be shaped. |
| Justification | `TEnumAsByte < ETextJustify :: Type >` | How the text should be aligned with the margin. |
| VerticalJustification | `TEnumAsByte < ETextVerticalJustify :: Type >` |  |
| bNeedVerticalJustificationWhenOverflow | `bool` | Should the text still be justified vertically when it overflow its block. |
| AutoWrapText | `bool` | True if we're wrapping text automatically based on the computed horizontal space for this widget. |
| WrapTextAt | `float` | Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs. |
| WrappingPolicy | [ETextWrappingPolicy](../../cppenum/E/ET/ETextWrappingPolicy.md) | The wrapping policy to use. |
| Margin | [FMargin](../../cppstruct/F/FM/FMargin.md) | The amount of blank space left around the edges of text area. |
| LineHeightPercentage | `float` | The amount to scale each lines height by. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

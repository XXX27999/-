# FCheckBoxStyle

Represents the appearance of an SCheckBox

## Fields

| Name | Type | Description |
| --- | --- | --- |
| CheckBoxType | `TEnumAsByte < ESlateCheckBoxType :: Type >` | The visual type of the checkbox |
| UncheckedImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when the CheckBox is unchecked (normal) |
| UncheckedHoveredImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when the CheckBox is unchecked and hovered |
| UncheckedPressedImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when the CheckBox is unchecked and hovered |
| CheckedImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when the CheckBox is checked |
| CheckedHoveredImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when checked and hovered |
| CheckedPressedImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when checked and pressed |
| UndeterminedImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when the CheckBox is undetermined |
| UndeterminedHoveredImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when CheckBox is undetermined and hovered |
| UndeterminedPressedImage | [FSlateBrush](../FS/FSlateBrush.md) | CheckBox appearance when CheckBox is undetermined and pressed |
| Padding | [FMargin](../FM/FMargin.md) | Padding |
| ForegroundColor | [FSlateColor](../FS/FSlateColor.md) | The foreground color |
| BorderBackgroundColor | [FSlateColor](../FS/FSlateColor.md) | BorderBackgroundColor refers to the actual color and opacity of the supplied border image on toggle buttons |
| CheckedSlateSound | [FSlateSound](../FS/FSlateSound.md) | The sound the check box should play when checked |
| UncheckedSlateSound | [FSlateSound](../FS/FSlateSound.md) | The sound the check box should play when unchecked |
| HoveredSlateSound | [FSlateSound](../FS/FSlateSound.md) | The sound the check box should play when initially hovered over |
| CheckedSound_DEPRECATED | `FName` |  |
| UncheckedSound_DEPRECATED | `FName` |  |
| HoveredSound_DEPRECATED | `FName` |  |

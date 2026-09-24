# FButtonStyle

Represents the appearance of an SButton

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Normal | [FSlateBrush](../FS/FSlateBrush.md) | Button appearance when the button is not hovered or pressed |
| Hovered | [FSlateBrush](../FS/FSlateBrush.md) | Button appearance when hovered |
| Pressed | [FSlateBrush](../FS/FSlateBrush.md) | Button appearance when pressed |
| Disabled | [FSlateBrush](../FS/FSlateBrush.md) | Button appearance when disabled, by default this is set to an invalid resource when that is the case default disabled drawing is used. |
| NormalPadding | [FMargin](../FM/FMargin.md) | Padding that accounts for the border in the button's background image.<br>	  When this is applied, the content of the button should appear flush<br>	  with the button's border. Use this padding when the button is not pressed. |
| PressedPadding | [FMargin](../FM/FMargin.md) | Same as NormalPadding but used when the button is pressed. Allows for moving the content to match<br>	  any "movement" in the button's border image. |
| PressedSlateSound | [FSlateSound](../FS/FSlateSound.md) | The sound the button should play when pressed |
| HoveredSlateSound | [FSlateSound](../FS/FSlateSound.md) | The sound the button should play when initially hovered over |
| PressedSound_DEPRECATED | `FName` |  |
| HoveredSound_DEPRECATED | `FName` |  |

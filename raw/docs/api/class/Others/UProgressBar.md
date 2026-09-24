# UProgressBar

The progress bar widget is a simple bar that fills up that can be restyled to fit any number of uses.

   No Children

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| WidgetStyle | [FProgressBarStyle](../../cppstruct/F/FP/FProgressBarStyle.md) | The progress bar style |
| Style_DEPRECATED | `USlateWidgetStyleAsset *` | Style used for the progress bar |
| BackgroundImage_DEPRECATED | `USlateBrushAsset *` | The brush to use as the background of the progress bar |
| FillImage_DEPRECATED | `USlateBrushAsset *` | The brush to use as the fill image |
| MarqueeImage_DEPRECATED | `USlateBrushAsset *` | The brush to use as the marquee image |
| Percent | `float` | Used to determine the fill position of the progress bar ranging 0..1 |
| BarFillType | `TEnumAsByte < EProgressBarFillType :: Type >` | Defines if this progress bar fills Left to right or right to left |
| bIsMarquee | `bool` |  |
| BorderPadding | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| PercentDelegate | `FGetFloat` | A bindable delegate to allow logic to drive the text of the widget |
| FillColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Fill Color and Opacity |
| FillColorAndOpacityDelegate | `FGetLinearColor` |  |

## Functions

### SetPercent

Sets the current value of the ProgressBar.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPercent | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetOppositePercent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPercent | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetFillColorAndOpacity

Sets the fill color of the progress bar.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetIsMarquee

Sets the progress bar to show as a marquee.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbIsMarquee | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPercent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOppositePercent

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
| OnPercentChangeDelegate |  |  |

## Language

cpp

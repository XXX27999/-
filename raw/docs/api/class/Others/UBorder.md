# UBorder

A border is a container widget that can contain one child widget, providing an opportunity
  to surround it with a background image and adjustable padding.

   Single Child
   Image

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| HorizontalAlignment | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the content horizontally. |
| VerticalAlignment | `TEnumAsByte < EVerticalAlignment >` | The alignment of the content vertically. |
| bShowEffectWhenDisabled | `uint8` | Whether or not to show the disabled effect when this border is disabled |
| ContentColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color and opacity multiplier of content in the border |
| ContentColorAndOpacityDelegate | `FGetLinearColor` | A bindable delegate for the ContentColorAndOpacity. |
| ResetBlendColor | `bool` |  |
| Padding | [FMargin](../../cppstruct/F/FM/FMargin.md) | The padding area between the slot and the content it contains. |
| Background | [FSlateBrush](../../cppstruct/F/FS/FSlateBrush.md) | Brush to drag as the background |
| BackgroundDelegate | `FGetSlateBrush` | A bindable delegate for the Brush. |
| BrushColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color and opacity of the actual border image |
| BrushColorDelegate | `FGetLinearColor` | A bindable delegate for the BrushColor. |
| DesiredSizeScale | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Scales the computed desired size of this border and its contents. Useful<br>	  for making things that slide open without having to hard-code their size.<br>	  Note: if the parent widget is set up to ignore this widget's desired size,<br>	  then changing this value will have no effect. |
| OnMouseButtonDownEvent | `FOnPointerEvent` |  |
| OnMouseButtonUpEvent | `FOnPointerEvent` |  |
| OnMouseMoveEvent | `FOnPointerEvent` |  |
| OnMouseDoubleClickEvent | `FOnPointerEvent` |  |

## Functions

### SetContentColorAndOpacity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InContentColorAndOpacity | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetResetBlendColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bResetBlendColor | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPadding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |

**Return**

- Type: 
- Description: _None_

### SetHorizontalAlignment

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InHorizontalAlignment | [EHorizontalAlignment](../../cppenum/E/EH/EHorizontalAlignment.md) |  |

**Return**

- Type: 
- Description: _None_

### SetVerticalAlignment

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InVerticalAlignment | [EVerticalAlignment](../../cppenum/E/EV/EVerticalAlignment.md) |  |

**Return**

- Type: 
- Description: _None_

### SetBrushColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBrushColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetBrush

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBrush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromAsset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Asset | `USlateBrushAsset *` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromTexture

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` |  |

**Return**

- Type: 
- Description: _None_

### SetBrushFromMaterial

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### GetDynamicMaterial

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetDesiredSizeScale

Sets the DesireSizeScale of this border.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InScale | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | The X and Y multipliers for the desired size |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

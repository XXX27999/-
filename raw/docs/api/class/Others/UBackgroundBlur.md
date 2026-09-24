# UBackgroundBlur

A background blur is a container widget that can contain one child widget, providing an opportunity
  to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.

   Single Child
   Blur Effect

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Padding | [FMargin](../../cppstruct/F/FM/FMargin.md) | The padding area between the slot and the content it contains. |
| HorizontalAlignment | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the content horizontally. |
| VerticalAlignment | `TEnumAsByte < EVerticalAlignment >` | The alignment of the content vertically. |
| bApplyAlphaToBlur | `bool` | True to modulate the strength of the blur based on the widget alpha. |
| BlurStrength | `float` | How blurry the background is.  Larger numbers mean more blurry but will result in larger runtime cost on the gpu. |
| bOverrideAutoRadiusCalculation | `bool` | Whether or not the radius should be computed automatically or if it should use the radius |
| BlurType | `TEnumAsByte < EBlurType >` | Blur type |
| BlurDirection | `float` | Blur direction for directional blur |
| BlurCenter | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Blur center for radial and rotate blur |
| BlurRadius | `int32` | This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur<br>	  A larger value is more costly but allows for stronger blurs. |
| BlurMask | `UTexture *` | A blur mask texture |
| LowQualityFallbackBrush | [FSlateBrush](../../cppstruct/F/FS/FSlateBrush.md) | An image to draw instead of applying a blur when low quality override mode is enabled.<br>	  You can enable low quality mode for background blurs by setting the cvar Slate.ForceBackgroundBlurLowQualityOverride to 1.<br>	  This is usually done in the project's scalability settings |
| BlurMaskBrush | [FSlateBrush](../../cppstruct/F/FS/FSlateBrush.md) |  |

## Functions

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

### SetApplyAlphaToBlur

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInApplyAlphaToBlur | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBlurRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlurRadius | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetBlurStrength

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStrength | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBlurDirection

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDirection | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBlurCenter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCenter | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### SetBlurMask

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTexture | `UTexture *` |  |

**Return**

- Type: 
- Description: _None_

### SetLowQualityFallbackBrush

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBrush | `FSlateBrush &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

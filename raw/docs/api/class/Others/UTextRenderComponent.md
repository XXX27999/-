# UTextRenderComponent

Renders text in the world with given font. Contains usual font related attributes such as Scale, Alignment, Color etc.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Text | `FText` | Text content, can be multi line using <br> as line separator |
| TextMaterial | `UMaterialInterface *` | Text material |
| Font | `UFont *` | Text font |
| HorizontalAlignment | `TEnumAsByte < enum EHorizTextAligment >` | Horizontal text alignment |
| VerticalAlignment | `TEnumAsByte < enum EVerticalTextAligment >` | Vertical text alignment |
| TextRenderColor | [FColor](../../cppstruct/F/FC/FColor.md) | Color of the text, can be accessed as vertex color |
| XScale | `float` | Horizontal scale, default is 1.0 |
| YScale | `float` | Vertical scale, default is 1.0 |
| WorldSize | `float` | Vertical size of the fonts largest character in world units. Transform, XScale and YScale will affect final size. |
| InvDefaultSize | `float` | The inverse of the Font's character height. |
| HorizSpacingAdjust | `float` | Horizontal adjustment per character, default is 0.0 |
| VertSpacingAdjust | `float` | Vertical adjustment per character, default is 0.0 |
| bAlwaysRenderAsText | `uint32` | Allows text to draw unmodified when using debug visualization modes. |

## Functions

### SetText

Change the text value and signal the primitives to be rebuilt
	  The FString variant is deprecated in favor of the FText variant

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetText

Change the text value and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### SetTextMaterial

Change the text material and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetFont

Change the font and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `UFont *` |  |

**Return**

- Type: 
- Description: _None_

### SetHorizontalAlignment

Change the horizontal alignment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [EHorizTextAligment](../../cppenum/E/EH/EHorizTextAligment.md) |  |

**Return**

- Type: 
- Description: _None_

### SetVerticalAlignment

Change the vertical alignment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [EVerticalTextAligment](../../cppenum/E/EV/EVerticalTextAligment.md) |  |

**Return**

- Type: 
- Description: _None_

### SetTextRenderColor

Change the text render color and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | [FColor](../../cppstruct/F/FC/FColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetXScale

Change the text X scale and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetYScale

Change the text Y scale and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetHorizSpacingAdjust

Change the text horizontal spacing adjustment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVertSpacingAdjust

Change the text vertical spacing adjustment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetWorldSize

Change the world size of the text and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetTextLocalSize

Get local size of text

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTextWorldSize

Get world space size of text

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

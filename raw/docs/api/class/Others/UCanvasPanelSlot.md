# UCanvasPanelSlot

## Parents

- [UPanelSlot](./UPanelSlot.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| LayoutData | [FAnchorData](../../cppstruct/F/FA/FAnchorData.md) | The anchoring information for the slot |
| bAutoSize | `bool` | When AutoSize is true we use the widget's desired size |
| ZOrder | `int32` | The order priority this widget is rendered in.  Higher values are rendered last (and so they will appear to be on top). |
| bAntiAdaptation | `bool` |  |

## Functions

### SetLayout

Sets the layout data of the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLayoutData | `FAnchorData &` |  |

**Return**

- Type: 
- Description: _None_

### GetLayout

Gets the layout data of the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPosition

Sets the position of the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPosition | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetPosition

Gets the position of the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSize

Sets the size of the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSize | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetSize

Gets the size of the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOffsets

Sets the offset data of the slot, which could be position and size, or margins depending on the anchor points

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InOffset | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |

**Return**

- Type: 
- Description: _None_

### GetOffsets

Gets the offset data of the slot, which could be position and size, or margins depending on the anchor points

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAnchors

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnchors | [FAnchors](../../cppstruct/F/FA/FAnchors.md) |  |

**Return**

- Type: 
- Description: _None_

### GetAnchors

Gets the anchors on the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAlignment

Sets the alignment on the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAlignment | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### GetAlignment

Gets the alignment on the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAutoSize

Sets if the slot to be auto-sized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbAutoSize | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetAutoSize

Gets if the slot to be auto-sized

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetZOrder

Sets the z-order on the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InZOrder | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetZOrder

Gets the z-order on the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAntiAdaptation

Sets the bAntiAdaptation on the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbAntiAdaptation | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetAntiAdaptation

Gets the bAntiAdaptation on the slot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMinimum

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMinimumAnchors | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### SetMaximum

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaximumAnchors | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### OnAntiAdaptationOffsetsChange

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

# UGridSlot

A slot for UGridPanel, these slots all share the same size as the largest slot
  in the grid.

## Parents

- [UPanelSlot](./UPanelSlot.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Padding | [FMargin](../../cppstruct/F/FM/FMargin.md) | The padding area between the slot and the content it contains. |
| HorizontalAlignment | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| VerticalAlignment | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |
| Row | `int32` | The row index of the cell this slot is in |
| RowSpan | `int32` |  |
| Column | `int32` | The column index of the cell this slot is in |
| ColumnSpan | `int32` |  |
| Layer | `int32` | Positive values offset this cell to be hit-tested and drawn on top of others. Default is 0; i.e. no offset. |
| Nudge | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Offset this slot's content by some amount; positive values offset to lower right |

## Functions

### SetPadding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |

**Return**

- Type: 
- Description: _None_

### SetRow

Sets the row index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRow | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetRowSpan

How many rows this this slot spans over

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRowSpan | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetColumn

Sets the column index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColumn | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetColumnSpan

How many columns this slot spans over

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InColumnSpan | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetLayer

Sets positive values offset this cell to be hit-tested and drawn on top of others.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLayer | `int32` |  |

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


## Event

_None_

## Delegate

_None_

## Language

cpp

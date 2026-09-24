# UUniformGridSlot

A slot for UUniformGridPanel, these slots all share the same size as the largest slot
  in the grid.

## Parents

- [UPanelSlot](./UPanelSlot.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| HorizontalAlignment | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| VerticalAlignment | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |
| Row | `int32` | The row index of the cell this slot is in |
| Column | `int32` | The column index of the cell this slot is in |

## Functions

### SetRow

Sets the row index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRow | `int32` |  |

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

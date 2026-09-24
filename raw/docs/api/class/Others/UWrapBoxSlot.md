# UWrapBoxSlot

The Slot for the UWrapBox, contains the widget that is flowed vertically

## Parents

- [UPanelSlot](./UPanelSlot.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Padding | [FMargin](../../cppstruct/F/FM/FMargin.md) | The padding area between the slot and the content it contains. |
| bFillEmptySpace | `bool` | Should this slot fill the remaining space on the line? |
| bForceNewLine | `bool` | Force this slot display to a new line |
| FillSpanWhenLessThan | `float` | If the total available space in the wrap panel drops below this threshold, this slot will attempt to fill an entire line.<br>	  NOTE: A value of 0, denotes no filling will occur. |
| HorizontalAlignment | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| VerticalAlignment | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

## Functions

### SetPadding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPadding | [FMargin](../../cppstruct/F/FM/FMargin.md) |  |

**Return**

- Type: 
- Description: _None_

### SetFillEmptySpace

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InbFillEmptySpace | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetFillSpanWhenLessThan

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFillSpanWhenLessThan | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetForceNewLine

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInForceNewLine | `bool` |  |

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

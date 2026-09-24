# UStackBox

A stack box widget is a layout panel allowing child widgets to be automatically laid out
  vertically or horizontally.

   Many Children
   Flows Vertical or Horizontal

## Parents

- [UPanelWidget](./UPanelWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Orientation | `TEnumAsByte < EOrientation >` | The orientation of the stack box. |

## Functions

### GetOrientation

Get the orientation of the stack box.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOrientation

Set the orientation of the stack box. The existing elements will be rearranged.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InType | [EOrientation](../../cppenum/E/EO/EOrientation.md) |  |

**Return**

- Type: 
- Description: _None_

### AddChildToStackBox

Adds a new child widget to the container.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### ReplaceStackBoxChildAt

Replace the widget at the given index it with a different widget.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

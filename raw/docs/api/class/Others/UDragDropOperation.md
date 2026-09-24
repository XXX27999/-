# UDragDropOperation

This class is the base drag drop operation for UMG, extend it to add additional data and add new functionality.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Tag | `FString` | A simple string tag you can optionally use to provide extra metadata about the operation. |
| Payload | `UObject *` | The payload of the drag operation.  This can be any UObject that you want to pass along as dragged data.  If you<br>	  were building an inventory screen this would be the UObject representing the item being moved to another slot. |
| DefaultDragVisual | `UWidget *` | The Drag Visual is the widget to display when dragging the item.  Normally people create a new widget to represent the<br>	  temporary drag. |
| Pivot | [EDragPivot](../../cppenum/E/ED/EDragPivot.md) | Controls where the drag widget visual will appear when dragged relative to the pointer performing<br>	  the drag operation. |
| Offset | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | A percentage offset (-1..+1) from the Pivot location, the percentage is of the desired size of the dragged visual. |
| StartOffset | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| bRemoveMoveAnimDelay | `bool` |  |

## Functions

### Drop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointerEvent | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### DragCancelled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointerEvent | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_

### Dragged

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointerEvent | `FPointerEvent &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnDrop |  |  |
| OnDragCancelled |  |  |
| OnDragged |  |  |

## Language

cpp

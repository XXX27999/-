# UPanelWidget

The base class for all UMG panel widgets.  Panel widgets layout a collection of child widgets.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Slots | `TArray < UPanelSlot * >` | The slots in the widget holding the child widgets of this panel. |
| CachedContents_ForGC | `TArray < UWidget * >` |  |

## Functions

### GetChildrenCount

Gets number of child widgets in the container.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetChildAt

Gets the widget at an index.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` | The index of the widget. |

**Return**

- Type: 
- Description: _None_

### GetChildIndex

Gets the index of a specific child widget

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### HasChild

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveChildAt

Removes a child by it's index.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### AddChild

Adds a new child widget to the container.  Returns the base slot type,
	  requires casting to turn it into the type specific to the container.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### InsertChildAtIndex

Insert a widget at a specific index, available in game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### ShiftChildToIndex

Moves the child widget from its current index to the new index provided, available in game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |
| Child | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveChild

Removes a specific widget from the container.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### HasAnyChildren

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearChildren

Remove all child widgets from the panel widget.

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

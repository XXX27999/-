# UWidgetSwitcher

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

## Parents

- [UPanelWidget](./UPanelWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ActiveWidgetIndex | `int32` | The slot index to display |
| bHideInactiveWidgets | `bool` |  |
| ActiveWidgetIndexDelegate | `FGetInt32` |  |

## Functions

### GetNumWidgets

Gets the number of widgets that this switcher manages.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActiveWidgetIndex

Gets the slot index of the currently active widget

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocalActiveWidgetIndex

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActiveWidgetIndex

Activates the widget at the specified index.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetActiveWidget

Activates the widget and makes it the active index.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Widget | `UWidget *` |  |

**Return**

- Type: 
- Description: _None_

### GetWidgetAtIndex

Get a widget at the provided index

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetActiveWidget

Get the reference of the currently active widget

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnActiveIndexChanged |  |  |
| OnActiveIndexChangeDelegate |  |  |

## Language

cpp

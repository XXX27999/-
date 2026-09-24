# UMenuAnchor

The Menu Anchor allows you to specify an location that a popup menu should be anchored to,
  and should be summoned from.
   Single Child
   Popup

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MenuClass | `TSubclassOf < UUserWidget >` | The widget class to spawn when the menu is required.  Creates the widget freshly each time.<br>	  If you want to customize the creation of the popup, you should bind a function to OnGetMenuContentEvent<br>	  instead. |
| OnGetMenuContentEvent | `FGetWidget` | Called when the menu content is requested to allow a more customized handling over what to display |
| Placement | `TEnumAsByte < EMenuPlacement >` | The placement location of the summoned widget. |
| ShouldDeferPaintingAfterWindowContent | `bool` |  |
| UseApplicationMenuStack | `bool` | Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself. |

## Functions

### ToggleOpen

Toggles the menus open state.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bFocusOnOpen | `bool` | Should we focus the popup as soon as it opens? |

**Return**

- Type: 
- Description: _None_

### Open

Opens the menu if it is not already open

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bFocusMenu | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Close

Closes the menu if it is currently open.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOpen

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ShouldOpenDueToClick

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMenuPosition

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasOpenSubMenus

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
| OnMenuOpenChanged |  | Called when the opened state of the menu changes |

## Language

cpp

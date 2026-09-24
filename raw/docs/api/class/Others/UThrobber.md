# UThrobber

A Throbber widget that shows several zooming circles in a row.

## Parents

- [UWidget](./UWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NumberOfPieces | `int32` | How many pieces there are |
| bAnimateHorizontally | `bool` | Should the pieces animate horizontally? |
| bAnimateVertically | `bool` | Should the pieces animate vertically? |
| bAnimateOpacity | `bool` | Should the pieces animate their opacity? |
| PieceImage_DEPRECATED | `USlateBrushAsset *` | Image to use for each segment of the throbber |
| Image | [FSlateBrush](../../cppstruct/F/FS/FSlateBrush.md) |  |

## Functions

### SetNumberOfPieces

Sets how many pieces there are

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InNumberOfPieces | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetAnimateHorizontally

Sets whether the pieces animate horizontally.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInAnimateHorizontally | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAnimateVertically

Sets whether the pieces animate vertically.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInAnimateVertically | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAnimateOpacity

Sets whether the pieces animate their opacity.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInAnimateOpacity | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

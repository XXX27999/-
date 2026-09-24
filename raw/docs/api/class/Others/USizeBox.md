# USizeBox

A widget that allows you to specify the size it reports to have and desire.  Not all widgets report a desired size
  that you actually desire.  Wrapping them in a SizeBox lets you have the Size Box force them to be a particular size.

   Single Child
   Fixed Size

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bOverride_WidthOverride | `uint32` |  |
| bOverride_HeightOverride | `uint32` |  |
| bOverride_MinDesiredWidth | `uint32` |  |
| bOverride_MinDesiredHeight | `uint32` |  |
| bOverride_MaxDesiredWidth | `uint32` |  |
| bOverride_MaxDesiredHeight | `uint32` |  |
| bOverride_MaxAspectRatio | `uint32` |  |
| WidthOverride | `float` | When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width. |
| HeightOverride | `float` | When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height. |
| MinDesiredWidth | `float` | When specified, will report the MinDesiredWidth if larger than the content's desired width. |
| MinDesiredHeight | `float` | When specified, will report the MinDesiredHeight if larger than the content's desired height. |
| MaxDesiredWidth | `float` | When specified, will report the MaxDesiredWidth if smaller than the content's desired width. |
| MaxDesiredHeight | `float` | When specified, will report the MaxDesiredHeight if smaller than the content's desired height. |
| MaxAspectRatio | `float` |  |

## Functions

### SetWidthOverride

When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InWidthOverride | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearWidthOverride

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetHeightOverride

When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InHeightOverride | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearHeightOverride

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMinDesiredWidth

When specified, will report the MinDesiredWidth if larger than the content's desired width.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMinDesiredWidth | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMinDesiredWidth

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMinDesiredHeight

When specified, will report the MinDesiredHeight if larger than the content's desired height.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMinDesiredHeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMinDesiredHeight

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMaxDesiredWidth

When specified, will report the MaxDesiredWidth if smaller than the content's desired width.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaxDesiredWidth | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMaxDesiredWidth

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMaxDesiredHeight

When specified, will report the MaxDesiredHeight if smaller than the content's desired height.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaxDesiredHeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMaxDesiredHeight

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMaxAspectRatio

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaxAspectRatio | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMaxAspectRatio

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

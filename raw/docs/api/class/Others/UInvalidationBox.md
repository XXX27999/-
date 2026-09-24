# UInvalidationBox

Invalidate
   Single Child
   Caching  Performance

## Parents

- [UContentWidget](./UContentWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bCanCache | `bool` | Should the invalidation panel cache the widgets?  Making this false makes it so the invalidation<br>	  panel stops acting like an invalidation panel, just becomes a simple container widget. |
| CacheRelativeTransforms | `bool` | Caches the locations for child draw elements relative to the invalidation box,<br>	  this adds extra overhead to drawing them every frame.  However, in cases where<br>	  the position of the invalidation boxes changes every frame this can be a big savings. |

## Functions

### InvalidateCache

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCanCache

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCanCache

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CanCache | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UKismetGuidLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### EqualEqual_GuidGuid

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGuid &` |  |
| B | `FGuid &` |  |

**Return**

- Type: 
- Description: _None_

### NotEqual_GuidGuid

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `FGuid &` |  |
| B | `FGuid &` |  |

**Return**

- Type: 
- Description: _None_

### IsValid_Guid

Checks whether the given GUID is valid

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InGuid | `FGuid &` |  |

**Return**

- Type: 
- Description: _None_

### Invalidate_Guid

Invalidates the given GUID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InGuid | `FGuid &` |  |

**Return**

- Type: 
- Description: _None_

### NewGuid

Returns a new unique GUID

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Conv_GuidToString

Converts a GUID value to a string, in the form 'A-B-C-D'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InGuid | `FGuid &` |  |

**Return**

- Type: 
- Description: _None_

### Parse_StringToGuid

Converts a String of format EGuidFormats to a Guid. Returns Guid OutGuid, Returns bool Success

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GuidString | `FString &` |  |
| OutGuid | `FGuid &` |  |
| Success | `bool &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UBlueprintMapLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### Map_Add

Adds a key and value to the map. If something already uses the provided key it will be overwritten with the new value.
	  After calling Key is guaranteed to be associated with Value until a subsequent mutation of the Map.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to add the key and value to |
| Key | `int32 &` | The key that will be used to look the value up |
| Value | `int32 &` | The value to be retrieved later |

**Return**

- Type: 
- Description: _None_

### Map_Remove

Removes a key and its associated value from the map.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to remove the key and its associated value from |
| Key | `int32 &` | The key that will be used to look the value up |

**Return**

- Type: 
- Description: _None_

### Map_Find

Finds the value associated with the provided Key

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to perform the lookup on |
| Key | `int32 &` | The key that will be used to look the value up |
| Value | `int32 &` | The value associated with the key, default constructed if key was not found |

**Return**

- Type: 
- Description: _None_

### Map_Contains

Checks whether key is in a provided Map

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to perform the lookup on |
| Key | `int32 &` | The key that will be used to lookup |

**Return**

- Type: 
- Description: _None_

### Map_Keys

Outputs an array of all keys present in the map

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to get the list of keys from |
| Keys | `TArray < int32 > &` | All keys present in the map |

**Return**

- Type: 
- Description: _None_

### Map_Values

Outputs an array of all values present in the map

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to get the list of values from |
| Values | `TArray < int32 > &` | All values present in the map |

**Return**

- Type: 
- Description: _None_

### Map_Length

Determines the number of entries in a provided Map

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map in question |

**Return**

- Type: 
- Description: _None_

### Map_Clear

Clears a map of all entries, resetting it to empty

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMap | `TMap < int32 , int32 > &` | The map to clear |

**Return**

- Type: 
- Description: _None_

### SetMapPropertyByName

Not exposed to users. Supports setting a map property on an object by name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `TMap < int32 , int32 > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

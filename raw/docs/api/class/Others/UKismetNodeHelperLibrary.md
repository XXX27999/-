# UKismetNodeHelperLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### BitIsMarked

Returns whether the bit at index "Index" is set or not in the data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32` | - The integer containing the bits that are being tested against |
| Index | `int32` | - The bit index into the Data that we are inquiring |

**Return**

- Type: 
- Description: _None_

### MarkBit

Sets the bit at index "Index" in the data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32 &` | - The integer containing the bits that are being set |
| Index | `int32` | - The bit index into the Data that we are setting |

**Return**

- Type: 
- Description: _None_

### ClearBit

Clears the bit at index "Index" in the data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32 &` | - The integer containing the bits that are being cleared |
| Index | `int32` | - The bit index into the Data that we are clearing |

**Return**

- Type: 
- Description: _None_

### ClearAllBits

Clears all of the bit in the data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32 &` | - The integer containing the bits that are being cleared |

**Return**

- Type: 
- Description: _None_

### HasUnmarkedBit

Returns whether there exists an unmarked bit in the data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32` | - The data being tested against |
| NumBits | `int32` | - The logical number of bits we want to track |

**Return**

- Type: 
- Description: _None_

### HasMarkedBit

Returns whether there exists a marked bit in the data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32` | - The data being tested against |
| NumBits | `int32` | - The logical number of bits we want to track |

**Return**

- Type: 
- Description: _None_

### GetUnmarkedBit

Gets an already unmarked bit and returns the bit index selected

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32` | - The integer containing the bits that are being set |
| StartIdx | `int32` | - The index to start with when determining the selection' |
| NumBits | `int32` | - The logical number of bits we want to track |
| bRandom | `bool` | - Whether to select a random index or not |

**Return**

- Type: 
- Description: _None_

### GetRandomUnmarkedBit

Gets a random not already marked bit and returns the bit index selected

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32` | - The integer containing the bits that are being set |
| StartIdx | `int32` |  |
| NumBits | `int32` | - The logical number of bits we want to track |

**Return**

- Type: 
- Description: _None_

### GetFirstUnmarkedBit

Gets the first index not already marked starting from a specific index and returns the bit index selected

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `int32` | - The integer containing the bits that are being set |
| StartIdx | `int32` | - The index to start looking for an available index from |
| NumBits | `int32` | - The logical number of bits we want to track |

**Return**

- Type: 
- Description: _None_

### GetEnumeratorName

Gets enumerator name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Enum | `UEnum *` | - Enumeration |
| EnumeratorValue | `uint8` | - Value of searched enumeration |

**Return**

- Type: 
- Description: _None_

### GetEnumeratorUserFriendlyName

Gets enumerator name as FString. Use DeisplayName when possible.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Enum | `UEnum *` | - Enumeration |
| EnumeratorValue | `uint8` | - Value of searched enumeration |

**Return**

- Type: 
- Description: _None_

### GetValidValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Enum | `UEnum *` | - Enumeration |
| EnumeratorValue | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### GetEnumeratorValueFromIndex

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Enum | `UEnum *` | - Enumeration |
| EnumeratorIndex | `uint8` | - Input index |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UBlueprintSetLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### Set_Add

Adds item to set. Output value indicates whether the item was successfully added, meaning an
	  output of False indicates the item was already in the Set.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to add item to |
| NewItem | `int32 &` | The item to add to the set |

**Return**

- Type: 
- Description: _None_

### Set_AddItems

Adds all elements from an Array to a Set

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to search for the item |
| NewItems | `TArray < int32 > &` | The items to add to the set |

**Return**

- Type: 
- Description: _None_

### Set_Remove

Remove item from set. Output value indicates if something was actually removed. False
	  indicates no equivalent item was found.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to remove from |
| Item | `int32 &` | The item to remove from the set |

**Return**

- Type: 
- Description: _None_

### Set_RemoveItems

Removes all elements in an Array from a set.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to remove from |
| Items | `TArray < int32 > &` | The items to remove from the set |

**Return**

- Type: 
- Description: _None_

### Set_ToArray

Outputs an Array containing copies of the entries of a Set.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSet < int32 > &` | Set |
| Result | `TArray < int32 > &` | Array |

**Return**

- Type: 
- Description: _None_

### Set_Clear

Clear a set, removes all content.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to clear |

**Return**

- Type: 
- Description: _None_

### Set_Length

Get the number of items in a set.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to get the length of |

**Return**

- Type: 
- Description: _None_

### Set_Contains

Returns true if the set contains the given item.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetSet | `TSet < int32 > &` | The set to search for the item |
| ItemToFind | `int32 &` | The item to look for |

**Return**

- Type: 
- Description: _None_

### Set_Intersection

Assigns Result to the intersection of Set A and Set B. That is, Result will contain
	  all elements that are in both Set A and Set B. To intersect with the empty set use
	  Clear.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSet < int32 > &` | One set to intersect |
| B | `TSet < int32 > &` | Another set to intersect |
| Result | `TSet < int32 > &` | Set to store results in |

**Return**

- Type: 
- Description: _None_

### Set_Union

Assigns Result to the union of two sets, A and B. That is, Result will contain
	  all elements that are in Set A and in addition all elements in Set B. Note that
	  a Set is a collection of unique elements, so duplicates will be eliminated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSet < int32 > &` | One set to union |
| B | `TSet < int32 > &` | Another set to union |
| Result | `TSet < int32 > &` | Set to store results in |

**Return**

- Type: 
- Description: _None_

### Set_Difference

Assigns Result to the relative difference of two sets, A and B. That is, Result will
	  contain  all elements that are in Set A but are not found in Set B. Note that the
	  difference between two sets  is not commutative. The Set whose elements you wish to
	  preserve should be the first (top) parameter. Also called the relative complement.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `TSet < int32 > &` | Starting set |
| B | `TSet < int32 > &` | Set of elements to remove from set A |
| Result | `TSet < int32 > &` | Set containing all elements in A that are not found in B |

**Return**

- Type: 
- Description: _None_

### SetSetPropertyByName

Not exposed to users. Supports setting a set property on an object by name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |
| PropertyName | `FName` |  |
| Value | `TSet < int32 > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

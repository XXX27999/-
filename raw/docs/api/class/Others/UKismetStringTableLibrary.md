# UKismetStringTableLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### IsRegisteredTableId

Returns true if the given table ID corresponds to a registered string table.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsRegisteredTableEntry

Returns true if the given table ID corresponds to a registered string table, and that table has.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |
| Key | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetTableNamespace

Returns the namespace of the given string table.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetTableEntrySourceString

Returns the source string of the given string table entry (or an empty string).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |
| Key | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetTableEntryMetaData

Returns the specified meta-data of the given string table entry (or an empty string).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |
| Key | `FString &` |  |
| MetaDataId | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetRegisteredStringTables

Returns an array of all registered string table IDs

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetKeysFromStringTable

Returns an array of all keys within the given string table

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetMetaDataIdsFromStringTableEntry

Returns an array of all meta-data IDs within the given string table entry

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TableId | `FName` |  |
| Key | `FString &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

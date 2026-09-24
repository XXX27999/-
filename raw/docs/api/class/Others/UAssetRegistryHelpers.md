# UAssetRegistryHelpers

## Parents

- [UObject](./UObject.md)

## Variables

_None_

## Functions

### GetAssetRegistry

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CreateAssetData

Creates asset data from a UObject.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAsset | `UObject *` | The asset to create asset data for |
| bAllowBlueprintClass | `bool` | By default trying to create asset data for a blueprint class will create one for the UBlueprint instead |

**Return**

- Type: 
- Description: _None_

### IsValid

Checks to see if this AssetData refers to an asset or is NULL

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### IsUAsset

Returns true if this asset was found in a UAsset file

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### IsRedirector

Returns true if the this asset is a redirector.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### GetFullName

Returns the full name for the asset in the form: Class ObjectPath

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### ToSoftObjectPath

Convert to a SoftObjectPath for loading

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### GetClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### GetAsset

Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### IsAssetLoaded

Returns true if the asset is loaded

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### GetExportTextName

Returns the name for the asset in the form: Class'ObjectPath'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |

**Return**

- Type: 
- Description: _None_

### GetTagValue < FName >

Gets the value associated with the given tag as a string

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAssetData | `FAssetData &` |  |
| InTagName | `FName &` |  |
| OutTagValue | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### SetFilterTagsAndValues

Populates the FARFilters tags and values map with the passed in tags and values

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFilter | `FARFilter &` |  |
| InTagsAndValues | `TArray < FTagAndValue > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

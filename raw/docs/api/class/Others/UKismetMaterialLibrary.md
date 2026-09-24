# UKismetMaterialLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### SetScalarParameterValue

Sets a scalar parameter value on the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Collection | `UMaterialParameterCollection *` |  |
| ParameterName | `FName` |  |
| ParameterValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorParameterValue

Sets a vector parameter value on the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Collection | `UMaterialParameterCollection *` |  |
| ParameterName | `FName` |  |
| ParameterValue | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### GetScalarParameterValue

Gets a scalar parameter value from the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Collection | `UMaterialParameterCollection *` |  |
| ParameterName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetVectorParameterValue

Gets a vector parameter value from the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Collection | `UMaterialParameterCollection *` |  |
| ParameterName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### CreateDynamicMaterialInstance

Creates a Dynamic Material Instance which you can modify during gameplay.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Parent | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UMaterialInstanceDynamic

## Parents

- [UMaterialInstance](./UMaterialInstance.md)

## Variables

_None_

## Functions

### SetScalarParameterValue

Set a MID scalar (float) parameter value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetScalarParameterValue

Get the current scalar (float) parameter value from an MID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetTextureParameterValue

Set an MID texture parameter value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Value | `UTexture *` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetTextureParameterValue

Get the current MID texture parameter value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorParameterValue

Set an MID vector parameter value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Value | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### K2_GetVectorParameterValue

Get the current MID vector parameter value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### K2_InterpolateMaterialInstanceParams

Interpolates the scalar and vector parameters of this material instance based on two other material instances, and an alpha blending factor
	  The output is the object itself (this).
	  Supports the case SourceA==this || SourceB==this
	  Both material have to be from the same base material

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SourceA | `UMaterialInstance *` | value that is used for Alpha=0, silently ignores the case if 0 |
| SourceB | `UMaterialInstance *` | value that is used for Alpha=1, silently ignores the case if 0 |
| Alpha | `float` | usually in the range 0..1, values outside the range extrapolate |

**Return**

- Type: 
- Description: _None_

### K2_CopyMaterialInstanceParameters

Copies over parameters given a material interface (copy each instance following the hierarchy)
	  Very slow implementation, avoid using at runtime. Hopefully we can replace ity later with something like CopyInterpParameters()
	  The output is the object itself (this).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Source | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### CopyInterpParameters

Copies over parameters given a material instance (only copy from the instance, not following the hierarchy)
	  much faster than K2_CopyMaterialInstanceParameters(),
	  The output is the object itself (this).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Source | `UMaterialInstance *` | ignores the call if 0 |

**Return**

- Type: 
- Description: _None_

### CopyParameterOverrides

Copy parameter values from another material instance. This will copy only
	  parameters explicitly overridden in that material instance!!

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaterialInstance | `UMaterialInstance *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

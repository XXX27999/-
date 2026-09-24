# ALight

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| LightComponent | `ULightComponent *` | @todo document |
| bEnabled | `uint32` | replicated copy of LightComponent's bEnabled property |

## Functions

### OnRep_bEnabled

Replication Notification Callbacks

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEnabled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bSetEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsEnabled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ToggleEnabled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBrightness

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewBrightness | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetBrightness

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLightColor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### GetLightColor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetLightFunctionMaterial

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFunctionMaterial | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetLightFunctionScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFunctionScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetLightFunctionFadeDistance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLightFunctionFadeDistance | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetCastShadows

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAffectTranslucentLighting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

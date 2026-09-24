# UBlackboardComponent

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BrainComp | `UBrainComponent *` | cached behavior tree component |
| BlackboardAsset | `UBlackboardData *` | data asset defining entries |
| KeyInstances | `TArray < UBlackboardKeyType * >` | instanced keys with custom data allocations |

## Functions

### GetValueAsObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsEnum

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsInt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsFloat

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsBool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsString

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetValueAsRotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| ObjectValue | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| ClassValue | `UClass *` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsEnum

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| EnumValue | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsInt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| IntValue | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsFloat

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| FloatValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsBool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| BoolValue | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsString

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| StringValue | `FString` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| NameValue | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| VectorValue | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetValueAsRotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| VectorValue | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### IsVectorValueSet

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetLocationFromEntry

return false if call failed (most probably no such entry in BB)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| ResultLocation | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### GetRotationFromEntry

return false if call failed (most probably no such entry in BB)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |
| ResultRotation | `FRotator &` |  |

**Return**

- Type: 
- Description: _None_

### ClearValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KeyName | `FName &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

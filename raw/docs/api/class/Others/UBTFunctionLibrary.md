# UBTFunctionLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### GetOwnersBlackboard

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |

**Return**

- Type: 
- Description: _None_

### GetOwnerComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsEnum

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsInt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsFloat

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsBool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsString

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBlackboardValueAsRotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `UClass *` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsEnum

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsInt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsFloat

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsBool

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsString

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `FString` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsVector

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### ClearBlackboardValueAsVector

(DEPRECATED) Use ClearBlackboardValue instead

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### SetBlackboardValueAsRotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |
| Value | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### ClearBlackboardValue

Resets indicated value to "not set" value, based on values type

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| Key | `FBlackboardKeySelector &` |  |

**Return**

- Type: 
- Description: _None_

### StartUsingExternalEvent

Initialize variables marked as "instance memory" and set owning actor for blackboard operations

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |
| OwningActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### StopUsingExternalEvent

Save variables marked as "instance memory" and clear owning actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeOwner | `UBTNode *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

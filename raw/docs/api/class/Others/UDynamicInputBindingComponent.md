# UDynamicInputBindingComponent

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ActionBindingClusters | `TArray < FActionBindingCluster >` |  |
| AxisBindingClusters | `TArray < FAxisBindingCluster >` |  |

## Functions

### BindAction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActionName | `FName &` |  |
| ActorInputEvent | `EActorInputEvent` |  |
| FunctionName | `FName &` |  |
| bConsumeInput | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BindAxis

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AxisName | `FName &` |  |
| FunctionName | `FName &` |  |
| bConsumeInput | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RemoveActionBinding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActionName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### RemoveAxisBinding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AxisName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### BindActionCluster

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### BindAxisCluster

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RemoveActionClusterBinding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RemoveAxisClusterBinding

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

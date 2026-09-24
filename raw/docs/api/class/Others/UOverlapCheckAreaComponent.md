# UOverlapCheckAreaComponent

区域重叠检测组件，能够检测到某个范围内开启重叠检测的Actor

## Parents

- [UActorComponent](./UActorComponent.md)
- IRegionObjectInterface
- IComponentHibernationNotifyInterface

## Variables

_None_

## Functions

### CheckOverlapActor

生效范围：S
	  触发一次区域重叠检测

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### StartCheck

生效范围：S
	  开始检测

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIgnoreActorList | `TArray < AActor * >` |  |
| bStopIfStarted | `bool` |  |

**Return**

- Type: 
- Description: _None_

### StopCheck

生效范围：S
	  停止检测

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddIgnoreActors

生效范围：S
	  添加要忽略的Actor列表

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Ignores | `TArray < AActor * >` | 要添加的Actor列表 |

**Return**

- Type: 
- Description: _None_

### RemoveIgnoreActor

生效范围：S
	  移除忽略的Actor列表

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Ignore | `AActor *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

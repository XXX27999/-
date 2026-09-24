# UCustomActorMoveComponent

一个给ActivityBaseActor移动功能的组件，用于移动所挂载的ActivityBaseActor

## Parents

- [UActorComponent](./UActorComponent.md)

## Variables

_None_

## Functions

### StartMove

生效范围：S
	  开始移动

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopMove

生效范围：S
	  结束移动

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMoveSpeed

生效范围：S
	  设置移动速度

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSpeed | `float` | 速度 |

**Return**

- Type: 
- Description: _None_

### SetGlideTime

生效范围：S
	  设置固定的滑行时间, 而不是使用起始点到终点位置除以速度得到这个数值

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GlideTime | `float` | 滑行时间 |

**Return**

- Type: 
- Description: _None_

### SetPosition

生效范围：S
	  设置移动的起始点和终点

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InStart | `FVector` | 起点 |
| InEnd | [FVector](../../cppstruct/F/FV/FVector.md) | 终点 |

**Return**

- Type: 
- Description: _None_

### IsMoving

生效范围：SC
	  获取Actor是否在移动
	  return 是否在移动

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| ActorMoveEvent |  | 移动状态改变事件委托 |

## Language

cpp

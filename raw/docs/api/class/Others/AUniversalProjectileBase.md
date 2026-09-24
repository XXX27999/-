# AUniversalProjectileBase

通用抛体

## Parents

- [AUniversalProjectileCore](./AUniversalProjectileCore.md)

## Variables

_None_

## Functions

### ReceiveCustomFilter

自定义的过滤器接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceivePlayExplosionEffectToAllTarget

自定义爆炸范围内筛选过后所有碰撞结果接口
	 生效范围：S

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FoundTargets | `TArray < FHitResult > &` |  |

**Return**

- Type: 
- Description: _None_

### ReceivePlayExplosionEffect

自定义爆炸范围内筛选过后碰撞接口
	 生效范围：S

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ExplosionTarget | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveBeginExplodeTimer

爆炸开始计时的额外接口（如果有延时爆炸）
	 生效范围：S

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveEndExplodeTimer

爆炸停止计时的额外接口（如果有延时爆炸）
	 生效范围：S

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# AEliteProjectile

投掷物

## Parents

- [AActor](./AActor.md)
- IRegionObjectInterface

## Variables

_None_

## Functions

### AddOnProjectileDestroyedHandler

生效范围SC
	  添加销毁事件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDelegate | `FSimpleProjectileDelegate` |  |

**Return**

- Type: 
- Description: _None_

### RemoveOnProjectileDestroyedHandler

生效范围SC
	  移除销毁事件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InDelegate | `FSimpleProjectileDelegate` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveProjectileExplodedEvent

生效范围SC
	  爆炸事件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impact | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveProjectileHit

生效范围SC
	  击中事件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveProjectileBouncedEvent

生效范围SC
	  弹射事件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ImpactResult | `FHitResult &` |  |
| ImpactVelocity | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveProjectileStoppedEvent

生效范围SC
	  停止事件

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

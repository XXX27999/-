# UGCProjectileSystem

抛体系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### SpawnProjectile

生成抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProjectileSpawnInfo | `ProjectileSpawnInfo` | 抛体生成参数 |

**Return**

- Type: 
- Description: _None_

### GetDestroyAfterHit

获取抛体命中之后是否销毁
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | `APVEProjectileBase` | 抛体 |

**Return**

- Type: 
- Description: _None_

### SetDestroyAfterHit

设置抛体命中之后是否销毁
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | `APVEProjectileBase` | 抛体 |
| bNewDestroyAfterHit | `boolean` | 是否销毁 |

**Return**

_None_

### GetPMComp

获取抛体运动组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | `APVEProjectileBase` | 抛体 |

**Return**

- Type: 
- Description: _None_

### SetMoveAfterImpactWithNoLost

设置抛体命中之后是否继续移动
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | `APVEProjectileBase` | 抛体 |
| bNeedUpdateImmide | `boolean` | 是否更新组件速度 |

**Return**

_None_

### GetLastUpdateCompBeforeStop

停止前最后更新的组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | `APVEProjectileBase` | 抛体 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

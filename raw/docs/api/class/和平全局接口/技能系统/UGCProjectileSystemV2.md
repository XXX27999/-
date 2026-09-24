# UGCProjectileSystemV2

技能抛体系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### CreateProjectile

发射技能抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProjectileClass | `UClass` | 抛体类型 |
| Owner | [AActor](../../Others/AActor.md) | 新生成抛体的所属对象 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 生成坐标 |
| Direction | [FVector](../../../cppstruct/F/FV/FVector.md) | 初始方向 |
| Speed | `number` | 初始速度 |
| GravityScale | `number` | 初始重力系数 |
| DamageValue | `number` | 抛体的伤害值 |
| DamageType | `FRestrictedDamageTypeData` | 抛体的伤害类型 |

**Return**

- Type: 
- Description: _None_

### CreateProjectileSimple

发射技能抛体（不传递伤害）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProjectileClass | `UClass` | 抛体类型 |
| Owner | [AActor](../../Others/AActor.md) | 新生成抛体的所属对象 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 生成坐标 |
| Direction | [FVector](../../../cppstruct/F/FV/FVector.md) | 初始方向 |
| Speed | `number` | 初始速度 |
| GravityScale | `number` | 初始重力系数 |
| Target | `number` | 抛体的伤害值 |

**Return**

- Type: 
- Description: _None_

### SetDirection

设置抛体速度方向
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |
| NewDirection | [FVector](../../../cppstruct/F/FV/FVector.md) | 新方向 |

**Return**

_None_

### SetSpeed

设置抛体速度大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |
| NewSpeed | `number` | 新速度 |

**Return**

_None_

### SetGravityScale

设置抛体重力系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |
| NewGravityScale | `number` | 新重力系数 |

**Return**

_None_

### SetDamage

设置抛体伤害，会覆盖所有的伤害值，伤害方式会调整为常量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |
| NewDamage | `number` | 伤害值 |

**Return**

_None_

### SetTarget

设置抛体目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |
| NewTarget | [APawn](../../Others/APawn.md) | 新的目标单位 |

**Return**

_None_

### GetProjectileMovementComponent

获取抛体移动组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |

**Return**

- Type: 
- Description: _None_

### GetDirection

获取抛体速度方向
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |

**Return**

- Type: 
- Description: _None_

### GetSpeed

获取抛体速度大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |

**Return**

- Type: 
- Description: _None_

### GetGravityScale

获取抛体重力系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |

**Return**

- Type: 
- Description: _None_

### GetTarget

获取抛体目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Projectile | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 抛体实例 |

**Return**

- Type: 
- Description: _None_

### GetProjectileListByGroupKey

获取抛体组中的抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [APESkillProjectileBase](../../Others/APESkillProjectileBase.md) | 发射抛体的角色 |
| GroupKey | `string` | 抛体组Key |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

# AUGCMobCharacter

怪物角色类

## Parents

- [ACharacter](./ACharacter.md)
- IObjectPoolInterface
- IDamageableInterface
- IAttrModifyInterface
- IGameAttributeCarrierInterface
- IRegionObjectInterface
- IBulletEffectInterface
- IBulletHitInterface
- IUGCCharacterAnimPlayInterfaceBase
- ICommonAIInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Health | `float` | 当前生命值 |
| HealthAddScale | `float` | 加血速率 |
| HealthMax | `float` | 最大生命值 |
| bInvincible | `int` | 是否无敌 |
| SkillCDRecoverRate | `FGameAttributeProperty` | 技能急速，值越大技能冷却越快结束 |
| IsShowDamageNum | `bool` | 是否显示伤害数字 |
| HealthBarWidget | `UUGCCharacterPositionWidget *` | 血条的蓝图类 |
| bIsShowHealthBar | `bool` | 是否显示血条 |
| ShowName | `FName` | 血条上显示的名字 |
| PlayBeHitedAnimTimeInterval | `float` | 受击动画播放最小间隔，小于受击动画长度时无效 |
| bNeedDestroyOnDeath | `bool` | 是否启用尸体消失后延迟销毁 |
| DisappearOnDeathLifeSpan | `float` | 尸体消失后延迟多久销毁 |
| DelayRemoveDeadBody | `float` | 死亡后尸体存在时间 |
| BornTime | `float` | 出生状态持续时间 |
| StunDuration | `float` | 硬直状态持续时间 |
| UGCGeneralMoveSpeedScale | `float` | 移动速度倍率 |
| AttackMeActorRemainTime | `float` | 活动范围，处于活动范围外时索敌无效，仇恨随时间消失<br><br>	 UGC<br>	  处于活动范围外时仇恨持续时间 |
| SpawnLoc | [FVector](../../cppstruct/F/FV/FVector.md) | 出生地点 |
| bOutOfActivityRange | `bool` | 是否在活动范围外 |

## Functions

### IsAlive

是否存活

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsInvincible

是否无敌

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ForceDie

生效范围 服务器
	  强制杀死怪物

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentSpeed

生效范围 服务器&客户端
	  获取当前速度值

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVelocity

生效范围 服务器&客户端
	  获取当前速度向量

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| PreTakeDamageEvent |  | 生效范围 服务器<br>	  小怪即将受到伤害前事件 |
| PostTakeDamageEvent |  | 生效范围 服务器<br>	  受到伤害后事件 |
| PreOverrideDamageValue |  | 生效范围 服务器<br>	  伤害值覆盖事件,在全局伤害公式前 |
| PostOverrideDamageValue |  | 生效范围 服务器<br>	  伤害值覆盖事件,在全局伤害公式后 |
| MobPawnDeadEvent |  | 生效范围 服务器&客户端<br>	  怪物死亡事件 |
| StateChangeEvent |  | 生效范围 服务器&客户端<br>	  状态变化事件 |

## Delegate

_None_

## Language

cpp

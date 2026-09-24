# UPersistEffectSkill

技能实体

## Parents

- [UPersistEffectWithState](./UPersistEffectWithState.md)
- ISkillObjectInterface
- IPESkillTaskTrackConditionFilterInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PESkillSlot | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 技能槽位Tag, 槽位为空时无法自动创建UI |
| ApplyTagGroup | `FGameplayTagGroups` | Tag的配置组，包含该技能与各个Tag的互斥关系 |
| CustomActivateConditions | `FPESkillConditionContainer` | 技能激活自定义条件 |
| ConsumeTime | [EPESkillConsumeTimeType](../../cppenum/E/EP/EPESkillConsumeTimeType.md) | CD能量和消耗扣除时机 |
| SkillCD | [FPESkillCDWapper](../../cppstruct/F/FP/FPESkillCDWapper.md) | 技能CD |
| CostConsume | [FPESkillConsume](../../cppstruct/F/FP/FPESkillConsume.md) | 技能消耗 |
| UIInfo | [FPESkillUIInfo](../../cppstruct/F/FP/FPESkillUIInfo.md) | 技能外显信息 |
| SkillGroup | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | 技能组，同组互斥，不能同时激活同组的技能，如果填空的话则没有任何互斥关系 |
| bDefaultEnable | `bool` | 默认是否可用，如果配置了false，则需要调用enable才能激活技能 |

## Functions

### EnableSkill

生效范围：S
	  使技能可用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DisableSkill

生效范围：S
	  使技能不可用

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsSkillEnable

生效范围：SC

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DeActivateSkill

生效范围：SC
	  取消技能释放

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Reason | [EPESkillDeActivateReason](../../cppenum/E/EP/EPESkillDeActivateReason.md) |  |

**Return**

- Type: 
- Description: _None_

### CanActivateSkill

生效范围：SC

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ActivateSkill

生效范围：SC
	  释放技能

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsActivating

生效范围：SC

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheckCDReady

生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheckCostReady

生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConsumeCD

生效范围：服务器
	  消耗CD

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConsumeCost

生效范围：服务器
	  消耗道具

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRemainingCDTime

生效范围：服务器&客户端
	  获取CD剩余时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCDRecoveryTime

生效范围：服务器&客户端
	  获取CD恢复时间

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCDRecoveryTime

生效范围：服务器
	  设置CD恢复时间

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CDRecoveryTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetCDRecoverRate

生效范围：服务器&客户端
	  获取CD恢复速率

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCDRecoverRate

生效范围：服务器
	  设置CD恢复速率

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rate | `float` | CD恢复速率 |

**Return**

- Type: 
- Description: _None_

### ChargeCDEnergy

生效范围：服务器
	  恢复CD比例，1代表完全恢复一层CD，大于1代表恢复多层，不超过层数上限

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ChargeRate | `float` | 恢复的层数 |

**Return**

- Type: 
- Description: _None_

### ChargeCDTime

生效范围：服务器
	  恢复CD固定时间，不超过层数上限

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ChargeTime | `float` | 恢复的时间，单位秒 |

**Return**

- Type: 
- Description: _None_

### RefreshCD

生效范围：服务器
	  刷新技能CD

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCDMaxLayer

生效范围：服务器
	  设置CD最大层数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMaxLayer | `int` |  |

**Return**

- Type: 
- Description: _None_

### OverwriteSkillUIInfo

生效范围：服务器&客户端
	  更改UI信息，但双端不同步

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SkillName | `FName` | 技能名字 |
| SkillDetail | `FString` | 技能描述 |
| SkillIconPath | `FString` | 技能图标路径 |

**Return**

- Type: 
- Description: _None_

### GetSkillName

生效范围：服务器&客户端
	  获取技能名字

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSkillDetail

生效范围：服务器&客户端
	  获取技能描述

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSkillIconPath

生效范围：服务器&客户端
	  获取技能图标路径

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetShowTipsEnable

生效范围：服务器
	  设置是否开启技能激活检查失败显示Tips

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` | 是否开启提示 |

**Return**

- Type: 
- Description: _None_

### SetPlayActivateFailedSoundEnable

生效范围：服务器
	  设置是否开启技能激活检查失败播放提示音

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` | 是否开启提示 |

**Return**

- Type: 
- Description: _None_

### GetSelectTargetActor

获取技能目标角色

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SelectType | [EPESkillSelectTarget](../../cppenum/E/EP/EPESkillSelectTarget.md) | 选择类型 |

**Return**

- Type: 
- Description: _None_

### SetSelectTargetActor

设置技能目标角色

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actors | `TArray < AActor * > &` | Actor数组 |

**Return**

- Type: 
- Description: _None_

### SetSelectTargetOneActor

设置技能目标角色

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| pActor | `AActor *` | Actor指针 |

**Return**

- Type: 
- Description: _None_

### SetSelectDirection

设置技能方向

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Direction | `FVector &` | 方向 |

**Return**

- Type: 
- Description: _None_

### GetSelectDirection

获取技能方向

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSelectTransform

获取技能目标位置

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSelectTransform

设置技能目标位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transform | `FTransform &` | 技能目标位置 |

**Return**

- Type: 
- Description: _None_

### SetSelectTransforms

设置技能多目标位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Transforms | `TArray < FTransform > &` |  |

**Return**

- Type: 
- Description: _None_

### GetSelectTransforms

获取技能多目标位置

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearSelectTransforms

清除技能目标位置

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnEnableSkill_BP |  | 生效范围：服务器<br>	  技能可用通知 |
| OnDisableSkill_BP |  | 生效范围：服务器<br>	  技能不可用通知 |
| OnActivateSkill_BP |  | 生效范围：服务器<br>	  技能被触发 |
| OnDeActivateSkill_BP |  | 生效范围：服务器<br>	  技能结束 |
| CanActivateSkill_BP |  | 生效范围：服务器&客户端<br>	  技能是否可用 |
| OnCDStateChange_BP |  | 生效范围：服务器&客户端<br>	  技能CD状态改变 |
| OnRegisterToSlot_BP |  | 技能被挂载到 Slot 或从 Slot 上摘下时触发 |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnUIInfoChange |  | Event<br>	  生效范围：客户端<br>	  技能的UI信息改变事件 |
| CDStateChangeHandle |  | Event<br>	  生效范围：服务器&客户端<br>	  客户端同步技能CD状态变化 |

## Language

cpp

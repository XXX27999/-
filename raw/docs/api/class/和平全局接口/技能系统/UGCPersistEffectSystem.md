# UGCPersistEffectSystem

新技能和Buff系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### AddSkillByClass

给指定拥有新技能组件的目标 Actor 添加技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标Actor |
| SkillClass | `UClass\|string` | 技能蓝图类或蓝图路径 |
| OverrideApplyTime | `number` | 技能生效时长(可选，默认为技能类中配置的时长) |
| Slot | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的技能槽位 |

**Return**

- Type: 
- Description: _None_

### RemoveSkillInstance

给指定拥有新技能组件的目标 Actor 移除技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| SkillInstance | [UPersistEffectSkill](../../Others/UPersistEffectSkill.md) | 技能对象 |

**Return**

- Type: 
- Description: _None_

### GetSkillsByClass

从指定拥有新技能组件的目标 Actor 获取指定类型的技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标Actor |
| SkillClass | `UClass\|string` | 技能蓝图类或蓝图路径,为空时获取所有技能 |

**Return**

- Type: 
- Description: _None_

### GetSkillsByTag

从指定拥有新技能组件的目标 Actor 获取拥有指定 Tag 的技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标Actor |
| Tag | `UGCGameplayTag\|string\|FGameplayTag` | 需要获取的技能所包含的 Tag,为空时获取所有技能 |

**Return**

- Type: 
- Description: _None_

### AddBuffByClass

给指定拥有新技能组件的目标 Actor 添加 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| BuffClass | `UClass\|string` | Buff 蓝图类或蓝图路径 |
| Causer | [AActor](../../Others/AActor.md) | Buff释放者（可选，默认为空） |
| OverrideDuration | `number` | 技能生效时长（可选，默认为-1代表Buff类中配置的时长） |
| StackNum | `number` | Buff的堆叠层数（可选，默认为 1 层） |

**Return**

- Type: 
- Description: _None_

### RemoveBuffByClass

给指定拥有新技能组件的目标 Actor 移除 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| BuffClass | `UClass\|string` | Buff 蓝图类或蓝图路径 |
| RemoveNum | `number` | Buff减少堆叠数量（可选，默认-1移除全部层） |
| Causer | [AActor](../../Others/AActor.md) | 筛选特定的释放者（可选，默认不筛选） |

**Return**

- Type: 
- Description: _None_

### RemoveBuffByTag

给指定拥有新技能组件的目标 Actor 移除包含某个 Tag 的 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| Tag | `UGCGameplayTag\|string\|FGameplayTag` | 需要移除的 Buff 所包含的 Tag |
| RemoveNum | `number` | Buff 减少堆叠数量（可选，默认移除全部层） |
| Causer | [AActor](../../Others/AActor.md) | 筛选特定的释放者(可选，默认不筛选) |

**Return**

- Type: 
- Description: _None_

### GetBuffsByClass

从指定拥有新技能组件的目标 Actor 获取指定类型的Buff
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标Actor |
| BuffClass | `UClass\|string` | Buff蓝图类或蓝图路径,为空时获取所有Buff |

**Return**

- Type: 
- Description: _None_

### GetBuffsByTag

从指定拥有新技能组件的目标 Actor 获取拥有指定Tag的Buff
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标Actor |
| Tag | `UGCGameplayTag\|string\|FGameplayTag` | 需要获取的 Buff 所包含的 Tag,为空时获取所有Buff |

**Return**

- Type: 
- Description: _None_

### HasDynamicState

检查指定拥有新技能组件的目标 Actor 是否包含某个 Tag 标识的状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要检查的 Tag 标识的状态 |

**Return**

- Type: 
- Description: _None_

### AllowDynamicState

检查指定拥有新技能组件的目标 Actor 是否允许进入某个 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要检查的 Tag 标识的状态 |

**Return**

- Type: 
- Description: _None_

### EnterDynamicState

尝试让拥有新技能组件的目标 Actor 获取指定 Tag 标识的状态，多次获取同一个 Tag 会叠加计数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要添加的 Tag 标识的状态 |

**Return**

- Type: 
- Description: _None_

### LeaveDynamicState

尝试从拥有新技能组件的目标 Actor 移除指定 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要移除的 Tag 标识的状态 |

**Return**

- Type: 
- Description: _None_

### InterruptDynamicState

将拥有新技能组件的目标 Actor 的 Tag 标识的状态移除并触发打断事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要打断的 Tag 标识的状态 |

**Return**

- Type: 
- Description: _None_

### SetDynamicStateDisabled

设置由 Tag 标识的状态的是否禁用，Actor 中 Tag 的禁用计数大于 0 时禁用生效
 - bNewDisabled == True：将拥有新技能组件的目标 Actor 的一组 Tag 标识的状态进行打断，并为这一组 Tag 的禁用计数 +1
 - bNewDisabled == false：将拥有新技能组件的目标 Actor 的一组 Tag 标识的状态禁用计数 -1
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要增加或减少禁用的 Tag 标识的状态 |
| bNewDisabled | `boolean` | 是否禁用 |
| bInterrupt | `boolean` | 是否打断，默认为 true |

**Return**

_None_

### ResetDynamicStateDisabled

重置被禁用的由 Tag 标识的状态，重置后目标 Actor 将允许进入这个 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |
| DynamicStateTag | `UGCGameplayTag\|string\|FGameplayTag` | 需要增加或减少禁用的 Tag 标识的状态 |

**Return**

_None_

### GetPersistBaseComponentByContent

从拥有新技能组件的目标 Actor 上获取 PersistBaseComponent 组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetActor | [AActor](../../Others/AActor.md) | 拥有新技能组件的目标 Actor |

**Return**

- Type: 
- Description: _None_

### AddOcclusionHighlight

添加透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetCharacter | [ACharacter](../../Others/ACharacter.md) | 被透视的角色或怪 |
| Causer | [AActor](../../Others/AActor.md) | 透视的发起方 |
| Type | [EPEBuffOcclusionHighlightType](../../../cppenum/E/EP/EPEBuffOcclusionHighlightType.md) | 透视类型(仅Causer透视/Causer及其队友透视/所有人) |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 透视颜色 |

**Return**

- Type: 
- Description: _None_

### RemoveOcclusionHighlight

移除透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| OcclusionID | `number` | 透视ID，AddOcclusionHighlight函数的返回值, <=0为无效值 |

**Return**

_None_

### AddFresnelEffect

添加菲涅尔效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetCharacter | [ACharacter](../../Others/ACharacter.md) | 被透视的角色或怪 |
| Color | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 颜色 |
| Duration | `number` | 时长 |

**Return**

_None_

### PickTargets

选取参数指定范围内的目标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OwnerActor | [AActor](../../Others/AActor.md) | 发起选目标的角色 |
| StartTransform | [FTransform](../../../cppstruct/F/FT/FTransform.md) | Picker开始位置 |
| TargetPickerParams | `FTargetPickerParams` | Picker参数 |
| IgnoreActors | `AActor[]` | 忽略的Actors |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

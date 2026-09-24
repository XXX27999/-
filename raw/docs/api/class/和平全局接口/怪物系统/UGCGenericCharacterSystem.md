# UGCGenericCharacterSystem

怪物系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### KillGenericCharacter

强制杀死怪物
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

_None_

### IsAlive

小怪是否存活
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### IsGenericCharacter

目标是否为小怪
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | [AActor](../../Others/AActor.md) | 目标 |

**Return**

- Type: 
- Description: _None_

### GetHealth

获取小怪血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### GetHealthMax

获取小怪血量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### SetHealth

设置小怪血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| Health | `number` | 血量 |

**Return**

_None_

### SetHealthMax

设置小怪血量上限
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| HealthMax | `number` | 血量上限 |

**Return**

_None_

### EnableMovement

启动移动能力
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

_None_

### DisableMovement

关闭移动能力
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

_None_

### SetAvoidanceGroup

设置避障组
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| AvoidanceGroup | [EGenericAvoidanceGroup](../../../cppenum/E/EG/EGenericAvoidanceGroup.md) | 避障组 |

**Return**

_None_

### MoveTo

移动到目标位置(注意不要和行为树移动冲突)
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| InDestination | [FVector](../../../cppstruct/F/FV/FVector.md) | 目的地 |
| InStopRadius | `number` | 停止距离 |

**Return**

_None_

### StopMove

停止移动(注意不要和行为树移动冲突)
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

_None_

### GetCurrentVelocity

获取当前怪物动量
生效范围：服务器/客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### SetMaxSpeed

设置最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| InSpeed | `number` | 速度 |
| Reason | `number` | 原因 |

**Return**

_None_

### GetMaxSpeed

获取最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### GetDefaultMaxSpeed

获取默认最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### GetTargetEnemy

获取当前仇恨目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### RunBehavior

运行指定行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| BehaviorTreePath | `string` | 行为树路径 |

**Return**

_None_

### StopBehavior

停止当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| Reason | `string` | 原因 |

**Return**

_None_

### OverrideBehaviorTreeSetting

覆盖行为树设置并重新启动行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| InBehaviorTreeSetting | `FBehaviorTreeReflectSetting` | 新的行为树设置 |

**Return**

_None_

### GetBehaviorTreeSetting

获取当前行为树设置
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |

**Return**

- Type: 
- Description: _None_

### PauseBehavior

暂停当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| Reason | `string` | 原因 |

**Return**

_None_

### ResumeBehavior

继续当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| Reason | `string` | 原因 |

**Return**

_None_

### PlayAnimMontage

播放蒙太奇动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| AnimMontage | [UAnimMontage](../../Others/UAnimMontage.md) | 蒙太奇动画 |
| InPlayRate | `number` | 播放速率 |

**Return**

_None_

### PlayAnimMontageByTag

通过Tag播放蒙太奇动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| AnimGameplayTag | [FGameplayTag](../../../cppstruct/F/FG/FGameplayTag.md) | 蒙太奇动画Tag |
| InPlayRate | `number` | 播放速率 |

**Return**

_None_

### AddOverrideAnimAsset

覆盖指定Tag的动画资源
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| Data | `FGenericCharacterAnimOverrideData` | 覆写数据 |
| BlendTime | `number` | 混合时间 |

**Return**

_None_

### RemoveOverrideAnimAsset

移除覆盖指定Tag的动画资源
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| Data | `FGenericCharacterAnimOverrideData` | 覆写数据 |
| BlendTime | `number` | 混合时间 |

**Return**

_None_

### IsEnableLogicPart

是否启用LogicPart
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GenericCharacter | [AUGCGenericCharacter](../../Others/AUGCGenericCharacter.md) | 怪物 |
| InLogicPartTag | [FGameplayTag](../../../cppstruct/F/FG/FGameplayTag.md) | LogicPart Tag |

**Return**

- Type: 
- Description: _None_

### SpawnGenericCharacter

在目标位置刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| GenericCharacterClass | `UClass` | 怪物的类 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪的位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |

**Return**

- Type: 
- Description: _None_

### SpawnGenericCharacterByGroup

在目标位置根据怪物组表中的ID刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| GroupID | `number` | 怪物组表中的ID |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪的位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |

**Return**

- Type: 
- Description: _None_

### RangeSpawnGenericCharacters

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| GenericCharacterClass | `UClass` | 怪物的类 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪范围的中心位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |
| Range | `number` | 刷怪圆形范围的半径 |
| HeightRange | `number` | 怪物刷出位置与中心位置的最大高度差 |
| Count | `number` | 刷出怪物的数量 |

**Return**

- Type: 
- Description: _None_

### RangeSpawnGenericCharactersByGroup

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪，怪物类型由怪物组表ID指定
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| GroupID | `number` | 怪物组表中的ID |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪范围的中心位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |
| Range | `number` | 刷怪圆形范围的半径 |
| HeightRange | `number` | 怪物刷出位置与中心位置的最大高度差 |
| Count | `number` | 刷出怪物的数量 |

**Return**

- Type: 
- Description: _None_

### RangeSpawnGenericCharactersOnTime

在指定位置的圆形范围中每隔一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| GenericCharacterClass | `UClass` | 怪物类 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪范围的中心位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |
| Range | `number` | 刷怪圆形范围的半径 |
| HeightRange | `number` | 怪物刷出位置与中心位置的最大高度差 |
| MinSpawnCountPerLoop | `number` | 每次刷怪的最小数量 |
| MaxSpawnCountPerLoop | `number` | 每次刷怪的最大数量 |
| LoopTimes | `number` | 总的刷怪轮数 |
| IntervalMinTime | `number` | 刷怪轮次间的最小时间间隔 |
| IntervalMaxTime | `number` | 刷怪轮次间的最大时间间隔 |
| FirstDelayTime | `number` | 从接口调用到首次刷怪的延迟时间 |
| Callback | `function` | 回调函数 |
| CallbackSelf | `table` | 回调函数的调用主体，静态函数时留空 |

**Return**

_None_

### RangeSpawnGenericCharactersByGroupOnTime

在指定位置的圆形范围中每个一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| GroupID | `number` | 怪物组表中的ID |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪范围的中心位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |
| Range | `number` | 刷怪圆形范围的半径 |
| HeightRange | `number` | 怪物刷出位置与中心位置的最大高度差 |
| MinSpawnCountPerLoop | `number` | 每次刷怪的最小数量 |
| MaxSpawnCountPerLoop | `number` | 每次刷怪的最大数量 |
| LoopTimes | `number` | 总的刷怪轮数 |
| IntervalMinTime | `number` | 刷怪轮次间的最小时间间隔 |
| IntervalMaxTime | `number` | 刷怪轮次间的最大时间间隔 |
| FirstDelayTime | `number` | 从接口调用到首次刷怪的延迟时间 |
| Callback | `function` | 回调函数 |
| CallbackSelf | `table` | 回调函数的调用主体，静态函数时留空 |

**Return**

_None_

### GetPartTypeSockets

获取角色骨骼里所有的PartTypeSocket
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Character | [ACharacter](../../Others/ACharacter.md) | 角色 |

**Return**

- Type: 
- Description: _None_

### GetBlackboard

获取Actor的BlackboardComponent
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](../../Others/AActor.md) | Actor |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

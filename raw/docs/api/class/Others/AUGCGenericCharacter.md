# AUGCGenericCharacter

怪物角色类

## Parents

- AGenericCharacter

## Variables

| Name | Type | Description |
| --- | --- | --- |
| HealthBarWidgetClass | `TSoftClassPtr < UUGCGenericCharacterPositionWidget >` | 血条控件蓝图路径 |
| bHealthBarShowWhenOcclusionHide | `bool` | 被遮挡后血条是否仍显示 |
| HealthBarMaxShowDistance | `float` | 血条实时显示最大距离，单位厘米 |
| HealthBarLocOffset | [FVector](../../cppstruct/F/FV/FVector.md) | 血条位置偏移 |
| bHealthBarLocScaleWithRoot | `bool` | 血条偏移是否随缩放变化 |
| bHealthBarUseSocket | `bool` | 血条是否附着到特定部位 |
| HealthBarSocketName | `FName` | 血条附着的部位名 |
| bHealthBarShowWhenTakeDamage | `bool` | 怪物受伤时显示血条 |
| bHealthBarShowWhenLockPlayer | `bool` | 当怪物将玩家作为当前目标时显示血条 |
| bHealthBarShowWhenBeAimAt | `bool` | 当玩家瞄准怪物时显示血条 |
| HealthBarConditionShowDistance | `float` | 能触发瞄准显示的最大距离 |
| HealthBarShowDuration | `float` | 血条显示条件触发后显示时间 |
| HealthBarCampFilter | `int32` | 阵营过滤 |
| HealthBarDamageFilter | [EShowHPBarDamageType](../../cppenum/E/ES/EShowHPBarDamageType.md) | 伤害来源过滤 |
| bEnableDistanceBasedNetworkOptimization | `bool` | 网络同步距离分档优化开关<br>	  只在客户端生效，控制是否根据与玩家的距离动态调整网络同步参数 |
| NetworkOptimizationLevels | `TArray < FUGCNetworkOptimizationLevelConfig >` | 距离分档配置数组<br>	  按 DistanceThreshold 从小到大排序配置，遍历找到第一个满足距离 <= 阈值的档位<br>	  如果距离超过所有阈值，则使用数组最后一个配置 |
| DistanceCheckInterval | `float` | 检测玩家距离的间隔时间 |
| CurrentDistanceLevel | `int32` | 当前档位索引 (-1表示未初始化) |

## Functions

### GetBlackBoardComponent

获取黑板组件
	  生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForceHatredTarget

设置当前强制仇恨目标
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTarget | `AActor *` | 仇恨目标 |

**Return**

- Type: 
- Description: _None_

### RemoveForceHatredTarget

清除强制仇恨目标
	  生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddTargetHatredValue

增加目标仇恨值
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Target | `AActor *` | 目标 |
| HatredValue | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnEnterTagState_BP |  | 状态进入事件<br>	  生效范围：服务器&客户端 |
| OnLeaveTagState_BP |  | 状态退出事件<br>	  生效范围：服务器&客户端 |
| OnInterruptTagState_BP |  | 状态打断事件<br>	  生效范围：服务器&客户端 |
| OnBehaviorNotify_BP |  | 行为树消息<br>	  生效范围：服务器 |
| OnArriveWaypoint_BP |  | 行为树消息<br>      生效范围：服务器 |

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnCreateHealthWidget |  | 血条创建成功事件 |

## Language

cpp

# UGCTweenSystem

Tween 动画系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### MakeConfig

创建一个 Tween 配置表

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Delay | `number` | 初始延迟（秒），默认 0 |
| RepeatCount | `number` | 重复次数（-1 无限，0 不重复），默认 1 |
| bYoyo | `boolean` | 是否往返，默认 false |
| RepeatDelay | `number` | 重复间隔（秒），默认 0 |

**Return**

- Type: 
- Description: _None_

### GetTweenSubsystem

获取 TweenSubsystem 实例
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TweenActorLocation

移动 Actor 到目标位置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 目标 Actor |
| TargetLocation | [FVector](../../cppstruct/F/FV/FVector.md) | 目标位置 |
| Duration | `number` | 动画时长（秒） |
| Easing | [EEasingType](../../cppenum/E/EE/EEasingType.md) | 缓动类型（EEasingType 枚举） |
| Config | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Return**

- Type: 
- Description: _None_

### TweenActorRotation

旋转 Actor 到目标朝向
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | [AActor](./AActor.md) | 目标 Actor |
| TargetRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | 目标旋转 |
| Duration | `number` | 动画时长（秒） |
| Easing | [EEasingType](../../cppenum/E/EE/EEasingType.md) | 缓动类型（EEasingType 枚举） |
| bShortestPath | `boolean` | 是否走最短路径旋转 |
| Config | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Return**

- Type: 
- Description: _None_

### TweenFloatValue

对 float 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | `number` | 起始值 |
| End | `number` | 目标值 |
| Duration | `number` | 动画时长（秒） |
| Easing | [EEasingType](../../cppenum/E/EE/EEasingType.md) | 缓动类型（EEasingType 枚举） |
| Callback | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 float 值 |
| Config | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Return**

- Type: 
- Description: _None_

### TweenVectorValue

对 FVector 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FVector](../../cppstruct/F/FV/FVector.md) | 起始向量 |
| End | [FVector](../../cppstruct/F/FV/FVector.md) | 目标向量 |
| Duration | `number` | 动画时长（秒） |
| Easing | [EEasingType](../../cppenum/E/EE/EEasingType.md) | 缓动类型（EEasingType 枚举） |
| Callback | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FVector 值 |
| Config | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Return**

- Type: 
- Description: _None_

### TweenRotatorValue

对 FRotator 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FRotator](../../cppstruct/F/FR/FRotator.md) | 起始旋转 |
| End | [FRotator](../../cppstruct/F/FR/FRotator.md) | 目标旋转 |
| Duration | `number` | 动画时长（秒） |
| Easing | [EEasingType](../../cppenum/E/EE/EEasingType.md) | 缓动类型（EEasingType 枚举） |
| Callback | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FRotator 值 |
| Config | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Return**

- Type: 
- Description: _None_

### TweenColorValue

对 FLinearColor 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Start | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | 起始颜色 |
| End | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | 目标颜色 |
| Duration | `number` | 动画时长（秒） |
| Easing | [EEasingType](../../cppenum/E/EE/EEasingType.md) | 缓动类型（EEasingType 枚举） |
| Callback | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FLinearColor 值 |
| Config | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Return**

- Type: 
- Description: _None_

### ConfigureTween

配置已创建的 Tween 的高级属性（延迟/循环/Yoyo）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 动画句柄 |
| Delay | `number` | 初始延迟（秒） |
| RepeatCount | `number` | 重复次数（-1 为无限循环，0 为不重复） |
| bYoyo | `boolean` | 是否往返播放（A->B->A） |
| RepeatDelay | `number` | 每次重复前的等待时间（秒），默认 0 |

**Return**

_None_

### ChainTween

链式连接两个 Tween：Parent 完成后自动播放 Child
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 父动画句柄 |
| NextHandle | `FTweenHandle` | 子动画句柄（将在父动画完成后自动触发） |

**Return**

_None_

### PauseTween

暂停 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 动画句柄 |

**Return**

_None_

### ResumeTween

恢复已暂停的 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 动画句柄 |

**Return**

_None_

### KillTween

停止并销毁 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 动画句柄 |

**Return**

_None_

### IsTweenValid

判断 Tween 句柄是否有效（动画是否仍在运行）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 动画句柄 |

**Return**

- Type: 
- Description: _None_

### BindCompletedDelegate

绑定 Tween 完成回调
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Handle | `FTweenHandle` | 动画句柄 |
| Callback | `function` | 完成回调，签名 function(Obj, Handle)，Obj 为 WorldContext，Handle 为动画句柄 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

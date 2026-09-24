# UGCMobPawnSystem

怪物系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### SpawnMob

在目标位置刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| MobClass | `UClass` | 怪物的类 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪的位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |

**Return**

- Type: 
- Description: _None_

### SpawnMobByMobGroup

在目标位置根据怪物组表中的ID刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| MobGroupID | `number` | 怪物组表中的ID |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪的位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |

**Return**

- Type: 
- Description: _None_

### RangeSpawnMobs

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| MobClass | `UClass` | 怪物的类 |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪范围的中心位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |
| Range | `number` | 刷怪圆形范围的半径 |
| HeightRange | `number` | 怪物刷出位置与中心位置的最大高度差 |
| Count | `number` | 刷出怪物的数量 |

**Return**

- Type: 
- Description: _None_

### RangeSpawnMobsByMobGroup

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪，怪物类型由怪物组表ID指定
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| MobGroupID | `number` | 怪物组表中的ID |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | 刷怪范围的中心位置 |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 刷出怪物的朝向 |
| Range | `number` | 刷怪圆形范围的半径 |
| HeightRange | `number` | 怪物刷出位置与中心位置的最大高度差 |
| Count | `number` | 刷出怪物的数量 |

**Return**

- Type: 
- Description: _None_

### RangeSpawnMobsOnTime

在指定位置的圆形范围中每隔一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| MobClass | `UClass` | 怪物类 |
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

### RangeSpawnMobsByMobGroupOnTime

在指定位置的圆形范围中每个一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| MobGroupID | `number` | 怪物组表中的ID |
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


## Event

_None_

## Delegate

_None_

## Language

lua

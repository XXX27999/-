# UGCSceneQueryUtility

环境查询工具库

## Parents

_None_

## Variables

_None_

## Functions

### QueryByLineSingle

使用射线执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryByLineMulti

使用射线执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryBySphereSingle

使用球体执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| Radius | `number` | 球体半径（默认值：100） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryBySphereMulti

使用球体执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| Radius | `number` | 球体半径（默认值：100） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryByBoxSingle

使用盒子执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 各轴到盒子中心的距离（默认值：X = 25, Y = 25, Z = 25） |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 盒子朝向（默认值：Pitch = 0, Yaw = 0, Roll = 0） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryByBoxMulti

使用盒子执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | 各轴到盒子中心的距离（默认值：X = 25, Y = 25, Z = 25） |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 盒子朝向（默认值：Pitch = 0, Yaw = 0, Roll = 0） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryByCapsuleSingle

使用胶囊执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 胶囊起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 胶囊终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| Radius | `number` | 胶囊半径（默认值：100） |
| HalfHeight | `number` | 胶囊高度（默认值：50） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryByCapsuleMulti

使用胶囊执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 胶囊起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 胶囊终点 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| Radius | `number` | 胶囊半径（默认值：100） |
| HalfHeight | `number` | 胶囊高度（默认值：50） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| IgnoreSelf | `boolean` | 是否忽略自身（默认值：true） |

**Return**

- Type: 
- Description: _None_

### QueryOverlapActorsBySphere

使用球体检测重叠的Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Position | [FVector](../../../cppstruct/F/FV/FVector.md) | 球体中心位置 |
| QueryType | `ESceneQueryType` | 环境查询类型 |
| Radius | `number` | 球体半径（默认值：100） |
| ActorsToIgnore | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| ActorClassFilter | `UClass` | Actor类型过滤器（默认值：nil） |
| OutActors | `AActor[]` | 输出的Actor数组（如果为nil则创建新数组） |

**Return**

- Type: 
- Description: _None_

### QueryByBoxMultiForObjects

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| HalfSize | [FVector](../../../cppstruct/F/FV/FVector.md) | Box边的半长尺寸 |
| Orientation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | Box的朝向 |
| ObjectTypes | `EObjectTypeQuery[]` | 要检测的对象类型数组 |
| bTraceComplex | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `AActor[]` | 需要忽略的Actor列表 |
| DrawDebugType | [EDrawDebugTrace](../../../cppenum/E/ED/EDrawDebugTrace.md) | 绘制调试类型 |
| OutHits | `FHitResult[]` | 存储所有碰撞结果 |
| bIgnoreSelf | `boolean` | 是否忽略自身 |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 未命中时的调试线颜色 |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 命中时的调试线颜色 |
| DrawTime | `number` | 绘制时间 |

**Return**

- Type: 
- Description: _None_

### QueryOverlapActorsBySphereWithFinder

在指定位置和半径的球体范围内检测所有重叠的Actor对象

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Finder | [AActor](../../Others/AActor.md) | 检测发起者，不被检测 |
| Origin | [FVector](../../../cppstruct/F/FV/FVector.md) | 球体中心位置 |
| Radius | `number` | 球体半径 |
| Channel | [ECollisionChannel](../../../cppenum/E/EC/ECollisionChannel.md) | 碰撞通道，默认为ECollisionChannel.ECC_WorldDynamic |

**Return**

- Type: 
- Description: _None_

### QueryBlocksByChannel

检测从起点到终点之间所有阻挡物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| OutHits | `FHitResult[]` | 存储所有碰撞结果 |
| IgnoreActors | `AActor[]` | 需要忽略的Actor列表 |
| TraceChannels | `ECollisionChannel[]` | 需要检测的碰撞通道数组 |

**Return**

- Type: 
- Description: _None_

### QueryBySphereMultiForObjects

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | 世界上下文 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| Radius | `number` | 扫描球体的半径 |
| ObjectTypes | `EObjectTypeQuery[]` | 对象类型列表 |
| bTraceComplex | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `AActor[]` | 要忽略的Actor列表 |
| DrawDebugType | [EDrawDebugTrace](../../../cppenum/E/ED/EDrawDebugTrace.md) | 调试模式 |
| OutHits | `FHitResult[]` | 碰撞结果列表，按从起点到终点的检测顺序排序。如果存在阻挡性碰撞，它将是列表中的最后一个碰撞结果 |
| bIgnoreSelf | `boolean` | 是否忽略自身 |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 未命中时的调试线颜色 |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 命中时的调试线颜色 |
| DrawTime | `number` | 调试线的持续时间 |

**Return**

- Type: 
- Description: _None_

### QueryByLineMultiForObjects

返回所有跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | world上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| ObjectTypes | `EObjectTypeQuery[]` | 对象类型列表 |
| bTraceComplex | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| ActorsToIgnore | `AActor[]` | 需要忽略的Actor列表 |
| DrawDebugType | [EDrawDebugTrace](../../../cppenum/E/ED/EDrawDebugTrace.md) | 调试模式 |
| OutHits | `FHitResult[]` | 输出的HitResult列表 |
| bIgnoreSelf | `boolean` | 是否忽略自身 |
| TraceColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 未命中时的调试线颜色 |
| TraceHitColor | [FLinearColor](../../../cppstruct/F/FL/FLinearColor.md) | 命中时的调试线颜色 |
| DrawTime | `number` | 调试线的持续时间 |

**Return**

- Type: 
- Description: _None_

### QueryByLineWithChannel

返回指定通道的射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutHit | [FHitResult](../../../cppstruct/F/FH/FHitResult.md) | 输出的HitResult |
| ContextObject | [UObject](../../Others/UObject.md) | world上下文对象 |
| Start | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测起点 |
| End | [FVector](../../../cppstruct/F/FV/FVector.md) | 射线检测终点 |
| IgnoreActors | `AActor[]` | 需要忽略的Actor列表 |
| TraceChannel | [ECollisionChannel](../../../cppenum/E/EC/ECollisionChannel.md) | 碰撞通道 |

**Return**

- Type: 
- Description: _None_

### FindPositionToHoldCapsule

获取一个目标位置附近能容纳胶囊体的坐标，以目标位置为中心，八方向向外迭代寻找位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | [UObject](../../Others/UObject.md) | World上下文 |
| SourceLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | 目标位置 |
| CapsuleRotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | 胶囊体的旋转 |
| CapsuleRadius | `float` | 胶囊体半径 |
| CapsuleHalfHeight | `float` | 胶囊体半高 |
| IgnoreActors | `AActor[]` | 需要忽略的Actor列表 |
| DetectObjectTypes | `EObjectTypeQuery[]` | 检测的对象类型列表 |
| Iterations | `int` | 检测迭代次数 |
| bNearestLocation | `bool` | 是否返回最近的位置 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

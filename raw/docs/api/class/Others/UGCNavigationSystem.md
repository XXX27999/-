# UGCNavigationSystem

寻路导航系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### BuildNavmesh

同步生成全地图寻路图, 会阻塞服务器运行
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |
| AgentName | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |

**Return**

_None_

### AsyncBuildNavmesh

异步生成全地图寻路图
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |
| AgentName | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |

**Return**

_None_

### AddDynamicNavAffect

添加寻路图动态影响区域，标记后可只针对该区域增量更新寻路
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |
| AgentName | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |
| InBounds | [FBox](../../cppstruct/F/FB/FBox.md) | 区域大小 |

**Return**

- Type: 
- Description: _None_

### AsyncIncrementalBuild

区域异步增量生成寻路图，和AddDynamicNavAffect配合使用
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |
| AgentName | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |

**Return**

- Type: 
- Description: _None_

### ProjectPointToNavigation

投影点到寻路图上的位置
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |
| Point | [FVector](../../cppstruct/F/FV/FVector.md) | 要投影的点 |
| QueryExtent | [FVector](../../cppstruct/F/FV/FVector.md) | 投影查询范围 |

**Return**

- Type: 
- Description: _None_

### GetRandomReachablePointInRadius

范围获取随机可寻路到达点位
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |
| Origin | [FVector](../../cppstruct/F/FV/FVector.md) | 查找原点 |
| Radius | `float` | 查询范围 |

**Return**

- Type: 
- Description: _None_

### IsNavigationBeingBuilt

寻路图是否构建
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |

**Return**

- Type: 
- Description: _None_

### GetNavigationGenerationFinishedDelegate

获取寻路图生成结束Delegate
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContext | [UObject](./UObject.md) | 当前世界上下文 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

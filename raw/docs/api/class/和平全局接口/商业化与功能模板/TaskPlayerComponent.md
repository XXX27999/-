# TaskPlayerComponent

UGC任务系统玩家组件

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TaskPlayerComponent.OnTaskLineAwardInfoChangeDelegate |  | 生效范围：客户端<br>任务线奖励状态变更回调<br>@param TaskLineName string @任务线名称<br>@param Index number @奖励索引 |
| TaskPlayerComponent.OnTaskInfoChangeDelegate |  | 生效范围：客户端<br>任务数据变更回调<br>@param Index UGCTaskIndex @榜单周期 |
| TaskPlayerComponent.OnTaskLineProgressChangeDelegate |  | 生效范围：客户端&服务端<br>任务线进度变更回调<br>@param TaskLineName string @任务线名称 |

## Functions

### ResetPercentTaskLine

重置活跃任务线
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

_None_

### ClaimLevelTaskAward

领取成长任务奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| LevelIndex | `number` |  |
| TaskIndex | `number` |  |

**Return**

_None_

### ClaimPercentTaskAward

领取活跃任务奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| TaskIndex | `number` |  |

**Return**

_None_

### GetTaskLineProgress

获取任务线进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

- Type: 
- Description: _None_

### GetLevelTaskInfoList

获取成长任务线的任务信息列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

- Type: 
- Description: _None_

### GetPercentTaskInfoList

获取活跃任务线的任务信息列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

- Type: 
- Description: _None_

### GetPercentTaskLineAwardStateList

获取活跃任务线的奖励状态列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

- Type: 
- Description: _None_

### GetTaskLineAwardState

获取任务线奖励状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| Index | `number` |  |

**Return**

- Type: 
- Description: _None_

### ClaimAllAward

领取任务线的全部奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

_None_

### ClaimTaskLineAward

领取任务线奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| Index | `number` |  |

**Return**

_None_

### SetTaskLineProgress

设置任务线进度
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| Progress | `number` |  |

**Return**

_None_

### GetPercentTaskProgress

获取活跃任务进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| Index | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetPercentTaskState

获取活跃任务状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| Index | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetLevelTaskProgress

获取成长任务进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| LevelIndex | `number` |  |
| TaskIndex | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetLevelTaskState

获取成长任务状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| LevelIndex | `number` |  |
| TaskIndex | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetTaskManager

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTaskLineTime

设置任务线和任务线下所有任务的开始/结束时间
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| BeginTime | `number` |  |
| EndTime | `number` |  |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

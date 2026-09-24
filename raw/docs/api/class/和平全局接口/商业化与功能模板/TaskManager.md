# TaskManager

UGC任务系统全局管理器

## Parents

_None_

## Variables

_None_

## Functions

### GetTaskLineConfig

获取任务线配置
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |

**Return**

- Type: 
- Description: _None_

### GetTaskConfig

获取任务配置
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskID | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetTaskType

获取任务类型
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskID | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetTaskDesc

获取任务目标进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskID | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetTaskTarget

获取任务目标进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskID | `number` |  |

**Return**

- Type: 
- Description: _None_

### UpdateTaskProgress

通用更新任务进度
生效范围：服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskIndex | `FUGCTaskIndex` |  |
| PlayerController | `Controller` |  |
| Progress | `number` |  |
| IsIncremental | `boolean` |  |

**Return**

_None_

### GetPercentTaskPercent

获取活跃任务完成后获得的活跃度数量
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TaskLineName | `string` |  |
| TaskID | `number` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

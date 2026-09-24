# BP_UGCVehicleRefresherTool

载具刷新器工具，用于管理载具的自动刷新和生成

## Parents

_None_

## Variables

_None_

## Functions

### AddVehicleEventListener

添加载具生成事件监听器，外部代码调用此方法注册载具生成事件监听
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| callback | `function` | 回调函数，参数为(Vehicle) |
| context | `any` | 上下文对象（可选） |

**Return**

_None_

### AddVehicleDriveAwayEventListener

添加载具开走事件监听器，外部代码调用此方法注册载具开走事件监听
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| callback | `function` | 回调函数，参数为(Vehicle) |
| context | `any` | 上下文对象（可选） |

**Return**

_None_

### RemoveVehicleEventListener

移除载具生成事件监听器
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| callback | `function` | 回调函数 |
| context | `any` | 上下文对象 |

**Return**

_None_

### RemoveVehicleDriveAwayEventListener

移除载具开走事件监听器
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| callback | `function` | 回调函数 |
| context | `any` | 上下文对象 |

**Return**

_None_

### GenerateVehicle

根据权重配置随机生成载具
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GenerateCustomizeVehicle

生成指定的载具蓝图
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VehiclePath | `string` | 载具蓝图路径，如"/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C" |

**Return**

- Type: 
- Description: _None_

### DestroyCurrentVehicle

销毁当前刷新点管理的载具
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetVehicleRespawnPoint

重置载具刷新点，如果载具还在原地，先销毁再重新刷新
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVehicleRespawnPointConfig

获取配置的载具列表信息
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVehicleStatusConfig

获取当前车辆的实时状态信息
生效范围：服务器&客户端

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

# UGCVehicleCommonSystem

载具系统通用功能接口库

## Parents

_None_

## Variables

_None_

## Functions

### SetVehicleHPMax

设置载具最大血量
本接口不会自动改变载具血量，游戏逻辑中改变载具血量时（比如收到伤害、载具维修等）会考虑载具最大血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| MaxHP | `number` | 最大血量 |

**Return**

_None_

### SetVehicleHP

设置载具血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| HP | `number` | 血量 |

**Return**

_None_

### SetVehicleFuelPercent

设置载具油量（按照百分比设置）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| FuelPercent | `number` | 油量百分比 |

**Return**

_None_

### GetVehicleHPMax

获得载具最大血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetVehicleHP

获得载具当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetVehicleFuelMax

获得载具最大油量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetVehicleFuelConsumeFactor

获得当前油耗系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetVehicleFuel

获得当前油量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### IsDontConsumeFuel

获得当前是否不耗油
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### IsDontDamage

获得当前是否不受到伤害
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetWheelHP

获得轮胎血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| WheelIndex | `number` | 轮胎 ID（从 1 开始） |

**Return**

- Type: 
- Description: _None_

### SetWheelHP

设置轮胎血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| WheelIndex | `number` | 轮胎 ID（从 1 开始） |
| HP | `number` | 载具轮子血量 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

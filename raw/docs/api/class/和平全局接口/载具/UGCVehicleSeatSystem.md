# UGCVehicleSeatSystem

载具系统座位系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### ChangePassengerSeat

在目标座位上没有乘客时更换乘客座位
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Passenger | [ASTExtraBaseCharacter](../../和平类事件/主角类（PlayerPawn）/ASTExtraBaseCharacter.md) | 乘客 |
| SeatIndex | `number` | 座位 ID |

**Return**

_None_

### ForceChangePassengerSeat

在目标座位上有乘客时更换乘客座位
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Passenger | [ASTExtraBaseCharacter](../../和平类事件/主角类（PlayerPawn）/ASTExtraBaseCharacter.md) | 乘客 |
| SeatIndex | `number` | 座位 ID |

**Return**

_None_

### GetSeatNum

获得载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetAvailableSeatNum

获得空闲的载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetPassenger

获得对应座位的乘客
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `number` | 座位 ID |

**Return**

- Type: 
- Description: _None_

### IsSeatIndexAvailable

获得对应座位是否空着
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `number` | 座位 ID |

**Return**

- Type: 
- Description: _None_

### GetCharacterSeatIndex

获得指定乘客的座位 ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Passenger | [ASTExtraBaseCharacter](../../和平类事件/主角类（PlayerPawn）/ASTExtraBaseCharacter.md) | 乘客 |
| GetBySocket | `boolean` | BySocket |

**Return**

- Type: 
- Description: _None_

### GetDriver

获得司机
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetPassengers

获得所有乘客
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetAvailableSeatIndexes

获得所有空闲座位的 Index
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### CanLeanOut

座位上是否可以探头
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `number` | 座位 ID |

**Return**

- Type: 
- Description: _None_

### RemoveVehicleWeapon

移除指定座位上对应 ID 的车载武器
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `number` | 座位 ID |
| WeaponIndex | `number` | 车载武器 ID |

**Return**

_None_

### AddVehicleWeaponFromSupportKit

将座位武器库中的武器装备到座位武器孔上
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `number` | 座位 ID |
| WeaponIndex | `number` | 车载武器 ID |
| WeaponIndexSupport | `number` | 武器库武器 ID |

**Return**

_None_

### SetPassengerVehicleWeapon

设置当前座位上的车载武器是否能使用
需要这个座位原来也配置了载具武器，且乘客正在该座位上
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `number` | 座位 ID |
| bControlVehicleWeapon | `boolean` | 是否能控制车载武器 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

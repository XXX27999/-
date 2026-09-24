# UGCVehicleSystemV2

载具系统接口库V2

## Parents

_None_

## Variables

_None_

## Functions

### SpawnVehicle

使用蓝图路径生成载具
不要在 Spawn 之后立马修改载具位置，等载具落地停稳后再修改，不然位置修改会失败（如果有类似需求，建议直接创建在对应点）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| VehiclePath | `string` | 载具蓝图路径，格式示例："/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C" |
| Location | `Vector` | 生成位置 |
| Rotation | `Rotator` | 旋转。可缺省，默认无旋转 |
| SnapFloor | `bool` | 是否贴地。可缺省，默认 true |
| IsForce | `bool` | 是否无视碰撞强行生成。 可缺省，默认 false |

**Return**

- Type: 
- Description: _None_

### DestroyVehicle

摧毁载具
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

_None_

### Respawn

重生载具
重生将创建新载具，旧的载具将被销毁不再可用
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### EnterVehicle

玩家角色进入载具
生效范围：服务器&客户端(客户端仅能操作自己的玩家角色)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `PlayerPawn \| PlayerController @玩家角色或玩家PlayerController` | 玩家角色或玩家PlayerController |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `int` | 座位索引(0为驾驶位，-1表示尝试进入任意空位置)。可缺省，默认-1。 |
| IsForce | `bool` | 是否无视距离和阻挡(仅服务器调用支持此项)。可缺省，默认 false |

**Return**

- Type: 
- Description: _None_

### LeaveVehicle

玩家角色离开载具
生效范围：服务器&客户端(客户端仅能操作自己的玩家角色)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `PlayerPawn \| PlayerController @玩家角色或玩家PlayerController` | 玩家角色或玩家PlayerController |
| IsForce | `bool` | 是否需要强制离开载具(仅服务器调用支持此项)。可缺省，默认 false |

**Return**

- Type: 
- Description: _None_

### GetVehicleType

获取载具类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### CanDrive

驾驶员是否可以操控载具
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### MoveForward

操作载具前进/后退
需要在驾驶员所在客户端每帧调用
当地面载具处于前进状态时，输入后退操作，将执行刹车逻辑，受刹车力量系数(BrakeTorqueCoefficient)影响。
当地面载具处于后退状态时，输入前进操作，也将执行刹车逻辑。
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Throttle | `float` | 取值范围[-1,1]，负值代表后退，正值代表前进 |

**Return**

_None_

### MoveTurn

操作载具打右方向/左方向
需要在驾驶员所在客户端每帧调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Throttle | `float` | 取值范围[-1,1]，负值代表左方向，正值代表右方向 |

**Return**

_None_

### CanHandBrake

获得载具是否支持(急刹)手刹
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### SetHandBrake

操作载具(急刹)手刹
需要在驾驶员所在客户端调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| BrakeScale | `float` | 刹车倍率，取值范围[0,1]，0为无刹车，1为最强刹车 |

**Return**

_None_

### CanBoosting

获得载具能否加速
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### SetBoosting

开关载具加速
需要在驾驶员所在客户端调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Open | `bool` | true开启加速，false关闭加速 |

**Return**

_None_

### CanHorn

获得载具能否按喇叭
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### SetHorn

按下/抬起载具喇叭
需要在驾驶员所在客户端调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| Open | `bool` | true按下喇叭，false抬起喇叭 |

**Return**

_None_

### GetVelocity

获得载具当前速度(单位是cm/s)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetVehicleHealthState

获得当前载具健康状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### CanDamage

获得载具是否能受到伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### SetCanDamage

设置载具是否能受到伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| CanDamage | `bool` | 能否受到伤害 |

**Return**

_None_

### GetSeatNum

获取座位数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### GetSeatDataByIndex

获取座位数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |
| SeatIndex | `int` | 座位索引 |

**Return**

- Type: 
- Description: _None_

### GetAllSeatDatas

获取所有座位数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

- Type: 
- Description: _None_

### ChangePassengerSeat

改变玩家乘客的座位
生效范围：服务器&客户端 (客户端执行只能指定空位，否则会失败。服务端执行可以指定有乘客的座位，两人互相交换位置。)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `PlayerPawn \| PlayerController @玩家角色或玩家PlayerController` | 玩家角色或玩家PlayerController |
| SeatIndex | `number` | 目标座位 ID |

**Return**

- Type: 
- Description: _None_

### StartFireVehicleWeapon

车载武器开始攻击
仅限驾驶位车载武器生效
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Vehicle | [ASTExtraVehicleBase](../和平类事件/载具基类/ASTExtraVehicleBase.md) | 载具 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

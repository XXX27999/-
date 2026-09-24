# UGCPawnAttrSystem

【废弃】角色属性系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### SetHealth

【废弃】请使用 UGCAttributeSystem
设置血量(不会超过最大血量)
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| Health | `number` | 血量 |

**Return**

_None_

### GetHealth

【废弃】请使用 UGCAttributeSystem
获取当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetHealthMax

【废弃】请使用 UGCAttributeSystem
设置血量上限（当前血量不会变化）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| HealthMax | `number` | 最大血量 |

**Return**

_None_

### GetHealthMax

【废弃】请使用 UGCAttributeSystem
获取血量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetSignal

【废弃】请使用 UGCAttributeSystem
设置信号值（不会超过最大值）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| Signal | `number` | 信号值 |

**Return**

_None_

### GetSignal

【废弃】请使用 UGCAttributeSystem
获取信号值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetSignalMax

【废弃】请使用 UGCAttributeSystem
获取信号值上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetEnergy

【废弃】请使用 UGCAttributeSystem
设置能量值（设置的值不能超过能量值上限[默认100]）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| Energy | `number` | 能量值 |

**Return**

_None_

### GetEnergy

【废弃】请使用 UGCAttributeSystem
获取能量值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetEnergyMax

【废弃】请使用 UGCAttributeSystem
获取能量值上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetSpeedScale

【废弃】请使用 UGCAttributeSystem
设置移动速度总系数，影响走路、冲刺、蹲下、趴下与游泳速度
注：该接口已废弃，请改用其他各移动状态的速度修改接口
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| SpeedScale | `number` | 移动速度总系数 |

**Return**

_None_

### GetSpeedScale

【废弃】请使用 UGCAttributeSystem
获取移动速度总系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetWalkSpeedScale

【废弃】请使用 UGCAttributeSystem
获取走路移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetWalkSpeedScale

【废弃】请使用 UGCAttributeSystem
设置走路移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| WalkSpeedScale | `number` | 走路移动速度系数 |

**Return**

_None_

### GetSprintSpeedScale

【废弃】请使用 UGCAttributeSystem
获取疾跑移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetSprintSpeedScale

【废弃】请使用 UGCAttributeSystem
设置疾跑移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| SprintSpeedScale | `number` | 疾跑移动速度系数 |

**Return**

_None_

### GetCrouchSpeedScale

【废弃】请使用 UGCAttributeSystem
获取蹲下移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetCrouchSpeedScale

【废弃】请使用 UGCAttributeSystem
设置蹲下移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| CrouchSpeedScale | `number` | 蹲下移动速度系数 |

**Return**

_None_

### GetProneSpeedScale

【废弃】请使用 UGCAttributeSystem
获取趴下移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetProneSpeedScale

【废弃】请使用 UGCAttributeSystem
设置趴下移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ProneSpeedScale | `number` | 趴下移动速度系数 |

**Return**

_None_

### GetSwimSpeedScale

【废弃】请使用 UGCAttributeSystem
获取游泳移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetSwimSpeedScale

【废弃】请使用 UGCAttributeSystem
设置游泳移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| SwimSpeedScale | `number` | 游泳移动速度系数 |

**Return**

_None_

### GetCurrentFOVTPP

【废弃】请使用 UGCAttributeSystem
获取当前第三人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetCurrentFOVTPP

【废弃】请使用 UGCAttributeSystem
设置当前第三人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| CurrentFOV | `number` | FOV |

**Return**

_None_

### GetCanSwitchFPP

【废弃】请使用 UGCAttributeSystem
获取是否可以切换至第一人称视角
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetCanSwitchFPP

【废弃】请使用 UGCAttributeSystem
设置是否可以切换至第一人称视角
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| CanSwitchFPP | `boolean` | 是否可切换至第一人称 |

**Return**

_None_

### GetCurrentFOVFPP

【废弃】请使用 UGCAttributeSystem
获取当前第一人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetCurrentFOVFPP

【废弃】请使用 UGCAttributeSystem
设置当前第一人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| CurrentFOV_FPP | `number` | FOV |

**Return**

_None_

### GetHearRadius

【废弃】请使用 UGCAttributeSystem
获取听觉半径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetPickUpRadius

【废弃】请使用 UGCAttributeSystem
获取拾取半径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetShowPlayerName

【废弃】请使用 UGCAttributeSystem
获取是否显示玩家名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetShowPlayerName

【废弃】请使用 UGCAttributeSystem
设置是否显示玩家名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| ShowPlayerName | `boolean` | 显示玩家名称 |

**Return**

_None_

### GetIsAI

【废弃】请使用 UGCAttributeSystem
获取是否AI
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetPlayerName

【废弃】请使用 UGCAttributeSystem
获取玩家名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetPlayerKey

【废弃】请使用 UGCAttributeSystem
获取字符串玩家PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyInt64

【废弃】请使用 UGCAttributeSystem
获取64位玩家Key
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetPlayerUID

【废弃】请使用 UGCAttributeSystem
获取玩家UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetPlayerTeamIndex

【废弃】请使用 UGCAttributeSystem
获取玩家队伍中序号（非TeamID，而是玩家在队伍中的序号）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetJumpType

【废弃】请使用 UGCAttributeSystem
获取跳跃类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetJumpHeight

【废弃】请使用 UGCAttributeSystem
获取跳跃高度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetJumpZVelocity

【废弃】请使用 UGCAttributeSystem
获取跳跃时的初速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetJumpZVelocity

【废弃】请使用 UGCAttributeSystem
设置跳跃时的初速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| JumpZVelocity | `number` | 跳跃时的初速度 |

**Return**

_None_

### GetStandHalfHeight

【废弃】请使用 UGCAttributeSystem
获取站立半高
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetStandRadius

【废弃】请使用 UGCAttributeSystem
获取站立半径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetCrouchHalfHeight

【废弃】请使用 UGCAttributeSystem
获取蹲伏半高
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetProneHalfHeight

【废弃】请使用 UGCAttributeSystem
获取匍匐半高
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetTeamID

【废弃】请使用 UGCAttributeSystem
获取TeamID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

# UGCWeaponManagerSystem

武器管理系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetWeaponManagerComponent

获取武器管理组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetWeaponBySlot

获取对应插槽的武器实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| Slot | [ESurviveWeaponPropSlot](../../../cppenum/E/ES/ESurviveWeaponPropSlot.md) | 武器槽位 |

**Return**

- Type: 
- Description: _None_

### GetCurrentWeapon

获取当前使用的武器实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetLastUsedWeapon

获取上一把武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### GetCurrentWeaponSlot

获取当前使用武器插槽
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SwitchWeaponBySlot

切换对应槽位的武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| Slot | [ESurviveWeaponPropSlot](../../../cppenum/E/ES/ESurviveWeaponPropSlot.md) | 武器槽位 |
| IsUseAnimation | `boolean` | 是否播放使用动画 |

**Return**

_None_

### CurrentWeaponAttachToBack

收起武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

_None_

### GetWeaponItemID

获取武器ItemID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Weapon | [ASTExtraWeapon](../../和平类事件/武器/ASTExtraWeapon.md) | 武器 |

**Return**

- Type: 
- Description: _None_

### GetWeaponName

获取武器名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Weapon | [ASTExtraWeapon](../../和平类事件/武器/ASTExtraWeapon.md) | 武器 |

**Return**

- Type: 
- Description: _None_

### GetCurrentUsingAmmoID

获取当前消耗弹药
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetWeaponSlotVisible

设置武器的可见性
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| WeaponSlot | [ESurviveWeaponPropSlot](../../../cppenum/E/ES/ESurviveWeaponPropSlot.md) | 武器槽位 |
| bVisible | `boolean` | 是否可见 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

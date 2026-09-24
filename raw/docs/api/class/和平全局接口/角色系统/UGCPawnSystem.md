# UGCPawnSystem

角色系统接口库（废弃，已迁移到 UGCPlayerPawnSystem）

## Parents

_None_

## Variables

_None_

## Functions

### HasPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
是否在指定状态下
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### AllowPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
是否允许进入指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### SwitchPoseState

【废弃】已迁移到 UGCPlayerPawnSystem
切换 Pose 状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PoseState | [ESTEPoseState](../../../cppenum/E/ES/ESTEPoseState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### EnterPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
进入指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### LeavePawnState

【废弃】已迁移到 UGCPlayerPawnSystem
离开指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../../cppenum/E/EP/EPawnState.md) | 角色状态 |

**Return**

- Type: 
- Description: _None_

### DisabledPawnState

【废弃】已迁移到 UGCPlayerPawnSystem
禁用指定状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| PawnState | [EPawnState](../../../cppenum/E/EP/EPawnState.md) | 角色状态 |
| IsDisabled | `bool` | 是否禁用 |

**Return**

_None_

### GetIsFPP

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否第一人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` |  |

**Return**

- Type: 
- Description: _None_

### SetIsFPP

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否第一人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| IsFPP | `bool` | 是否第一人称 |
| bForce | `bool` | 强制设置人称 |

**Return**

- Type: 
- Description: _None_

### GetIsTPP

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否第三人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` |  |

**Return**

- Type: 
- Description: _None_

### SetIsTPP

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否第三人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| IsTPP | `bool` | 是否第三人称 |
| bForce | `bool` | 强制设置 TPP 模式 |

**Return**

- Type: 
- Description: _None_

### GetIsInvincible

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

- Type: 
- Description: _None_

### SetIsInvincible

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| IsInvincible | `bool` | 是否无敌 |

**Return**

_None_

### TryEnterParachuteState

【废弃】已迁移到 UGCPlayerPawnSystem
尝试进入跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| CheckPawnState | `EPawnState[]` | 不允许进入跳伞的角色状态 |
| CanOpenParachuteHeight | `float` | 允许开伞高度 |
| ForceOpenParachuteHeight | `float` | 强制开伞高度 |
| CloseParachuteHeight | `float` | 关伞高度 |
| bParachuteAvatarNotShown | `bool` | 是否不显示伞包 |

**Return**

_None_

### ExitParachuteState

【废弃】已迁移到 UGCPlayerPawnSystem
退出跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

_None_

### HideBoneByBoneName

【废弃】已迁移到 UGCPlayerPawnSystem
根据玩家角色的骨骼名称修改骨骼的显隐性
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BoneName | `FName` | 骨骼名称 |
| bHide | `bool` | true隐藏，false显示 |

**Return**

_None_

### ChangeAvatarMesh

【废弃】已迁移到 UGCPlayerPawnSystem
切换玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| SkeletalMeshPath | `string` | 全身骨骼体路径 |

**Return**

_None_

### RecoverAvatarMesh

【废弃】已迁移到 UGCPlayerPawnSystem
恢复玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |

**Return**

_None_

### SkipSpawnDeadTombBox

【废弃】已迁移到 UGCPlayerPawnSystem
玩家死亡取消生成盒子
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| bIsSkip | `bool` | 玩家是否取消生成死亡盒子 |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

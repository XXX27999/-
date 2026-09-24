# UGCPlayerStateSystem

玩家数据/状态系统接口库

## Parents

_None_

## Variables

| Name | Type | Description |
| --- | --- | --- |
| UGCPlayerStateSystem._CrossPlayerChunkDataCallbacks |  |  |
| UGCPlayerStateSystem._CrossPlayerChunkDataRequestID |  |  |

## Functions

### IsAlive

是否存活
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` |  |

**Return**

- Type: 
- Description: _None_

### IsExit

是否离开游戏（主动退出，非断线）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetUGCVIPLevel

获取 VIP Level
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerAccountInfo

获取玩家的账号数据
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerBattleInfo

获取玩家的战斗数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` |  |

**Return**

- Type: 
- Description: _None_

### SavePlayerArchiveData

保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）!!!!注意，不能在对局结算之后保存存档数据，在对局结算后调用此接口无法成功保存存档数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |
| ArchiveData | `table` | 存档数据 |

**Return**

- Type: 
- Description: _None_

### SavePlayerArchiveDataByKey

按key保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |
| Key | `string` | 要保存的键名 |
| Value | `any` | 要保存的值 |

**Return**

- Type: 
- Description: _None_

### GetPlayerArchiveData

获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |

**Return**

- Type: 
- Description: _None_

### GetPlayerArchiveDataByKey

按key获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |
| Key | `string` | 要获取的键名 |

**Return**

- Type: 
- Description: _None_

### GetTableDataSize

计算Lua table序列化后的字节大小
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Data | `table` | 要计算大小的table |

**Return**

- Type: 
- Description: _None_

### GetPlayerDataSize

获取玩家存档数据的总字节大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 玩家 UID |

**Return**

- Type: 
- Description: _None_

### ClearPlayerArchiveData

清理玩家存档数据（GM 指令，仅开发环境生效）
生效范围：客户端

**Parameters**

_None_

**Return**

_None_

### GetPlayerPlatformGender

获取玩家账号性别
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlatformGender | `number` | 从DS获取的玩家性别 |
| UID | `number` | 玩家UID |

**Return**

- Type: 
- Description: _None_

### GetTeamID

获取 TeamID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerKeyInt64

获取 64 位玩家 PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `PlayerState` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerKey

获取字符串玩家 PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerState | `PlayerState` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

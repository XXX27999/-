# UGCBuffSystem

【废弃】Buff 系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### GetBuffSystemComponent

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色。所有的接口里的 PlayerPawn 都可以扩展成任意的 Actor，只要这个 Actor 有一个名字叫 BuffSystemComponent 的 Buff 组件即可。 |

**Return**

- Type: 
- Description: _None_

### AddBuff

【废弃】请使用 UGCPersistEffectSystem
为玩家添加 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色。所有的接口里的 PlayerPawn 都可以扩展成任意的 Actor，只要这个 Actor 有一个名字叫 BuffSystemComponent 的 Buff 组件即可。 |
| BuffName | `string` | Buff 名 |
| LayerCount | `number` | 层数 |
| BuffCauser | `Controller` | 施加 Buff 的玩家或 AI 的控制器 |
| CauserActor | `Actor` | 施加 Buff 的 Actor，比如说 PlayerPawn、燃烧瓶 Actor 等等 |

**Return**

- Type: 
- Description: _None_

### RemoveBuff

【废弃】请使用 UGCPersistEffectSystem
为玩家移除 Buff,本帧内不即时移除
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BuffName | `string` | Buff 名 |
| LayerCount | `number` | 层数 |

**Return**

_None_

### RemoveBuffByInstanceID

【废弃】请使用 UGCPersistEffectSystem
使用唯一 ID 移除 Buff，本帧内不即时移除
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| InstanceID | `number` | Buff 唯一 ID |
| LayerCount | `number` | 层数 |

**Return**

_None_

### HasBuff

【废弃】请使用 UGCPersistEffectSystem
是否存在该 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BuffName | `string` | Buff 名 |

**Return**

- Type: 
- Description: _None_

### GetCurLayer

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 当前层数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BuffName | `string` | Buff 名 |

**Return**

- Type: 
- Description: _None_

### GetMaxLayer

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 最大层数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BuffName | `string` | Buff 名 |

**Return**

- Type: 
- Description: _None_

### GetLeftTime

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 剩余持续时间
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | 玩家角色 |
| BuffName | `string` | Buff 名 |

**Return**

- Type: 
- Description: _None_

### GetBuffCauserActor

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 的施加者
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerPawn | `PlayerPawn` | Buff |
| InstanceID | `number` | Buff 唯一 ID |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

lua

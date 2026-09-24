# UGCMessageSystem

游戏聊天通用接口库

## Parents

_None_

## Variables

_None_

## Functions

### JoinCampMessageChannel

阵营聊天 开局分阵营或阵营变更时同步阵营信息，创建阵营的聊天室
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家的 PlayerKey |
| CampID | `number` | 阵营 ID（传入0为无阵营） |

**Return**

_None_

### SendSystemMessageToPlayer

给单独玩家发送系统消息
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerKey | `number` | 玩家 PlayerKey |
| MessageTag | `string` | 消息标题 |
| MessageContent | `string` | 消息内容 |
| Level | `number` | 消息等级 |

**Return**

- Type: 
- Description: _None_

### SendSystemMessageToAll

给所有玩家发送系统消息
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MessageTag | `string` | 消息标题 |
| MessageContent | `string` | 消息内容 |
| Level | `number` | 消息等级 |

**Return**

- Type: 
- Description: _None_

### OpenPrivateChat

打开与指定玩家的私聊界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UID | `number` | 目标玩家 UID |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

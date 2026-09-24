# UGCLevelFlowSystem

关卡流程系统接口库

## Parents

_None_

## Variables

_None_

## Functions

### EnableLevelFlow

启用关卡流程
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMgrPath | `string` | 需要注册的 GameModeActorMgr 的路径 |

**Return**

_None_

### GoToNextLevelForAllPlayers

当前关卡所有玩家直接跳转到下个关卡，需所有玩家都已达到通关条件
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GoToNextLevelForOnePlayer

单个玩家直接跳转到下个关卡，需当前玩家已达到通关条件，当前队伍其他玩家仍停留在当前关卡
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) | 玩家 |

**Return**

- Type: 
- Description: _None_

### LevelAddScore

给指定队伍关卡加分
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |
| Score | `number` | 加分的分数 |

**Return**

_None_

### LevelSettle

队伍所在关卡立即结算
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 结算的队伍 |
| IsFinish | `boolean` | 是否通关 |

**Return**

_None_

### GetCurrentLevelStage

获取当前玩家处于第几关
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | [ASTExtraPlayerController](../../和平类事件/角色控制类（PlayerController）/ASTExtraPlayerController.md) | 玩家 |

**Return**

- Type: 
- Description: _None_

### GetTotalLevelCount

获取总关卡数，随机切换关卡暂时不支持获取总关卡数，需要自定义逻辑
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GameAddScore

给指定队伍游戏加分
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TeamID | `number` | 队伍 ID |
| Score | `number` | 加分的分数 |

**Return**

_None_

### GameSettle

游戏立即结算
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsFinish | `boolean` | 是否通关 |

**Return**

_None_

### GetAllPlayerControllerInCurrentLevel

获取关卡里的所有玩家
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentLevelActor

获取当前副本
生效范围：服务器

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

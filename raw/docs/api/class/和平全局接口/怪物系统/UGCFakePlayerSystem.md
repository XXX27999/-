# UGCFakePlayerSystem

假人玩家系统

## Parents

_None_

## Variables

_None_

## Functions

### SpawnFakePlayer

生成假人玩家， GameMode 中 DataManager，AIProbe 数据中配置 AIController
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AIPlayerKey | `number` | AIPlayerKey，建议使用 UGCFakePlayerSystem.GetRandomAIPlayerKey 生成 |
| TeamID | `number` | 队伍 ID |
| InFakePlayerClass | `UClass` | 假人玩家的控制器类 |

**Return**

_None_

### GetRandomAIPlayerKey

生成随机AIPlayerKey，用于UGCFakePlayerSystem.SpawnFakePlayer接口参数
生效范围：服务器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DestroyFakePlayer

销毁假人玩家
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AIPlayerKey | `number` | AIPlayerKey |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

# UGCCampSystem

阵营接口库

## Parents

_None_

## Variables

_None_

## Functions

### AddCamp

增加阵营
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCampName | `string` | 阵营名称 |

**Return**

- Type: 
- Description: _None_

### SetCampForActor

设置非玩家Actor所属阵营，例如设置怪物的阵营
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | AActor |
| InCampID | `number` | 阵营ID |

**Return**

_None_

### SetCampForTeam

设置队伍所属阵营
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTeamID | `number` | 队伍ID |
| InCampID | `number` | 阵营ID |

**Return**

- Type: 
- Description: _None_

### GetCampIDByActor

通过非玩家Actor获取阵营ID，获取失败的时候返回-1
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | AActor |

**Return**

- Type: 
- Description: _None_

### GetCampNameByActor

通过非玩家Actor获取阵营名称，获取失败的时候返回空字符串
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActor | [AActor](../../Others/AActor.md) | AActor |

**Return**

- Type: 
- Description: _None_

### GetCampIDByTeamID

通过队伍ID获取阵营ID，获取失败的时候返回-1
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTeamID | `number` | 队伍ID |

**Return**

- Type: 
- Description: _None_

### GetCampNameByTeamID

通过队伍ID获取阵营名称，获取失败的时候返回空字符串
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTeamID | `number` | 队伍ID |

**Return**

- Type: 
- Description: _None_

### SetDefaultCampRelation

设置默认阵营关系
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCampRelation | [ECampRelation](../../../cppenum/E/EC/ECampRelation.md) | 阵营关系,1:友好,2:中立,3:敌对 |

**Return**

_None_

### SetCampRelation

设置两个阵营之间的阵营关系
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCampA_ID | `number` | 阵营A ID |
| InCampB_ID | `number` | 阵营B ID |
| InCampRelation | [ECampRelation](../../../cppenum/E/EC/ECampRelation.md) | 阵营关系,0:友好,1:中立,2:敌对 |

**Return**

_None_

### GetCampRelation

获取两个阵营之间的阵营关系，获取失败默认返回中立
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCampA_ID | `number` | 阵营A ID |
| InCampB_ID | `number` | 阵营B ID |

**Return**

- Type: 
- Description: _None_

### GetCampRelationWithActor

获取两个Actor之间的阵营关系，获取失败默认返回中立
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InActorA | [AActor](../../Others/AActor.md) | AActor |
| InActorB | [AActor](../../Others/AActor.md) | AActor |

**Return**

- Type: 
- Description: _None_

### SetCampDefaultSpawnMethod

设置阵营出生方式
生效范围：服务器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCampID | `number` | 阵营ID |
| SpawnPointSelectionMethod | [EUGCCampSpawnPointSelectionMethod](../../../cppenum/E/EU/EUGCCampSpawnPointSelectionMethod.md) | 阵营出生方式 |
| SpawnMethodInfo | `FVector\|uint8` | 指定PlayerStartID或者世界坐标 |
| PlayerStartInfo | `boolean` | 是否随机出生点ID |

**Return**

_None_


## Event

_None_

## Delegate

_None_

## Language

lua

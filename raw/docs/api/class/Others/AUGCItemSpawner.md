# AUGCItemSpawner

物资刷新系统：物资刷新器

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ItemConfig | [FUGCItemSpawnerItemConfig](../../cppstruct/F/FU/FUGCItemSpawnerItemConfig.md) | 配置刷出的物资类别和数量 |
| bNeedSpawnerManager | `bool` | 物资刷新点是否能独立运作，还是依赖于物资刷新管理器 |
| bLoopSpawn | `bool` | 独立运作模式时，物资被拾取后是否会自动生成 |
| SpawnCD | `float` | 开启循环生成后，物资被拾取后间隔重新刷新 |
| bTraceGround | `bool` | 物资是否一定刷新在地面上 |
| bRandomRotator | `bool` | 物资方向是否随机 |
| StartRadius | `int32` | 物资刷新位置到刷新点的最小距离 |
| EndRadius | `int32` | 物资刷新位置到刷新点的最大距离 |

## Functions

### SpawnItem

生效范围 服务器
	  刷物资

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ItemID | `int32` | 物资ID |
| ItemCount | `int32` | 物资数量 |

**Return**

- Type: 
- Description: _None_

### SetItemConfig

生效范围 服务器
	  修改物资刷新配置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InItemConfig | [FUGCItemSpawnerItemConfig](../../cppstruct/F/FU/FUGCItemSpawnerItemConfig.md) | 新的物资刷新配置 |

**Return**

- Type: 
- Description: _None_

### CleanItems

生效范围 服务器
	  清除刷出的物资

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnItemsSpawn |  | 生效范围 服务器<br>	  物资刷出事件 |
| OnAllItemsArePick |  | 生效范围 服务器<br>	  所有物资都被拾取 |
| CustomSpawnItem |  | 生效范围 服务器<br>	  覆写该事件来自定义物资刷出流程 |

## Delegate

_None_

## Language

cpp

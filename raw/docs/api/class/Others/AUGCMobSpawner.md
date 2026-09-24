# AUGCMobSpawner

刷怪系统：刷怪器

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bNeedSpawnerManager | `bool` | 是否刷怪点是否能独立运行，还是必须依赖刷怪管理器. 废弃, 请使用SpawnerContrMode |
| SpawnerContrMode | [EUGCMobSpawnerContrMode](../../cppenum/E/EU/EUGCMobSpawnerContrMode.md) | 刷怪器控制模式. |
| MobConfig | [FUGCMobSpawnerMobConfig](../../cppstruct/F/FU/FUGCMobSpawnerMobConfig.md) | 配置刷出的怪物 |
| bUseNavMesh | `bool` | 是否优先在有移动网格的地面上刷新 |
| Range | `float` | 配置怪物的生成范围的半径 |
| Height | `float` | 配置刷新点位置与实际生成位置的最大高度差 |
| RandomRotYaw | `bool` | 怪物的出生面向是否随机，否则使用刷新点的朝向 |
| MinSpawnCount | `int32` | 配置总的最小刷怪数量 |
| MaxSpawnCount | `int32` | 配置总的最大刷怪数量 |
| SpawnCD | `float` | 配置两次刷怪之间的时间间隔 |
| MobCountPerSpawn | `int32` | 配置单次刷怪的数量 |
| bTraceGround | `bool` | 是否保证怪物刷到地面上 |

## Functions

### SpawnMob

生效范围 服务器
	  刷出指定怪物

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MobClass | `UClass *` | 怪物的类 |

**Return**

- Type: 
- Description: _None_

### SetMobConfig

生效范围 服务器
	  修改怪物刷新配置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMobConfig | [FUGCMobSpawnerMobConfig](../../cppstruct/F/FU/FUGCMobSpawnerMobConfig.md) | 修改后的刷新配置 |

**Return**

- Type: 
- Description: _None_

### ModifyMinMaxSpawnCount

生效范围 服务器
	  修改最小最大刷怪数量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMinSpawnCount | `int32` | 修改后的最小刷怪数量 |
| InMaxSpawnCount | `int32` | 修改后的最大刷怪数量 |

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnMobSpawn |  | 生效范围 服务器<br>	  怪物刷出事件 |
| CustomSpawnMob |  | 生效范围 服务器<br>	  覆写该事件可实现自定义怪物刷出流程 |

## Delegate

_None_

## Language

cpp

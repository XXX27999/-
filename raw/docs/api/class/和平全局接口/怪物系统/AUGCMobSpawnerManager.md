# AUGCMobSpawnerManager

刷怪系统：刷怪管理器

## Parents

- [AActor](../../Others/AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StartCondition | [EUGCMobSpawnerManagerStartCondition](../../../cppenum/E/EU/EUGCMobSpawnerManagerStartCondition.md) | 配置刷怪管理器的启动方式 |
| EventName | `FString` | 启动方式使用事件触发时，监听的GMP名 |
| MaxSpawnPerFrame | `int32` | 配置刷怪管理器每帧刷怪的上限 |
| AliveMobsCheckDeltaTime | `float` | 配置刷怪管理器检查当前怪物存活情况的间隔 |
| SpawnWaves | `TArray < FUGCSpawnWave >` | 配置刷怪的波次 |

## Functions

### StartSpawnerManager

生效范围 服务器
	  启动刷怪管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetSpawnerManager

生效范围 服务器
	  重置刷怪管理器

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDeleteAllMobs | `bool` | 是否清除所有刷出的怪物 |

**Return**

- Type: 
- Description: _None_

### CleanAllMobs

生效范围 服务器
	  清理对刷出怪物的引用

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bDelete | `bool` | 是否清除怪物 |

**Return**

- Type: 
- Description: _None_

### PauseSpawnerManager

生效范围 服务器
	  暂停刷怪管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResumeSpawnerManager

生效范围 服务器
	  恢复刷怪管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSpawner

生效范围 服务器
	  获取波次中特定编号的刷怪点

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WaveIndex | `int32` | 波次编号 |
| SpawnerIndex | `int32` | 刷新点编号 |

**Return**

- Type: 
- Description: _None_

### GetCurrentWaveIndex

生效范围 服务器
	  获取当前波的波次编号

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetWaveSpawnerNum

生效范围 服务器
	  获取对应波次的刷新点数量

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WaveIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetWaveNum

生效范围 服务器
	  获取波次的数量

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMobConfigOverrideForSpawner

生效范围 服务器
	  修改特定波次中特定刷新点的怪物配置覆盖

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMobConfig | [FUGCMobSpawnerMobConfig](../../../cppstruct/F/FU/FUGCMobSpawnerMobConfig.md) | 新的怪物配置 |
| WaveIndex | `int32` | 波次编号 |
| SpawnerIndex | `int32` | 刷新点编号 |

**Return**

- Type: 
- Description: _None_

### SetMobConfigOverrideForWave

生效范围 服务器
	  修改特定波次中所有刷新点的怪物配置覆盖

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMobConfig | [FUGCMobSpawnerMobConfig](../../../cppstruct/F/FU/FUGCMobSpawnerMobConfig.md) | 新的怪物配置 |
| WaveIndex | `int32` | 波次编号 |

**Return**

- Type: 
- Description: _None_

### SetMobConfigOverride

生效范围 服务器
	  修改所有波次的怪物配置覆盖

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMobConfig | [FUGCMobSpawnerMobConfig](../../../cppstruct/F/FU/FUGCMobSpawnerMobConfig.md) | 新的怪物配置 |

**Return**

- Type: 
- Description: _None_

### CleanAllMobConfigOverride

生效范围 服务器
	  清除管理器所有的怪物配置覆盖

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### JumpToWave

生效范围 服务器
	  跳转到指定波次

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WaveIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnMobSpawn |  | 生效范围 服务器<br>	  怪物刷出事件 |
| OnWaveStart |  | 生效范围 服务器<br>	  刷怪波次开始事件 |
| OnWaveEnd |  | 生效范围 服务器<br>	  刷怪波次结束事件 |
| OnAllWaveEnd |  | 生效范围 服务器<br>	  所有波次结束事件 |
| OnAllMobDie |  | 生效范围 服务器<br>	  所以波次怪物都已刷新并死亡事件 |

## Delegate

_None_

## Language

cpp

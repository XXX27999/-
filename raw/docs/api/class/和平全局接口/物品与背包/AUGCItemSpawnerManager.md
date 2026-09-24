# AUGCItemSpawnerManager

生成系统：物资生成管理器

## Parents

- [AActor](../../Others/AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StartCondition | [EUGCItemSpawnerManagerStartCondition](../../../cppenum/E/EU/EUGCItemSpawnerManagerStartCondition.md) | 管理器的启动方式 |
| EventName | `FString` | 启动方式选择事件触发时，监听的GMP事件名 |
| ItemSpawners | `TArray < FUGCItemSpawnerInfo >` | 配置刷新点 |
| MaxWaveInternalTime | `float` | 配置两次刷新之间的最大时间间隔 |
| MinWaveInternalTime | `float` | 配置两次刷新之间的最小时间间隔 |
| MaxSpawnerNumPerWave | `int32` | 配置同一时间有物资刷出的刷新点的最大数量 |
| MinSpawnerNumPerWave | `int32` | 配置同一时间有物资刷出的刷新点的最小数量 |
| TotalSpawnWaveCount | `int32` | 物资刷新的总轮数，设为-1则无限刷新 |
| bOverrideItemConfig | `bool` | 是否覆盖所有刷新点上的物资配置 |
| ItemConfig | [FUGCItemSpawnerItemConfig](../../../cppstruct/F/FU/FUGCItemSpawnerItemConfig.md) | 配置所有刷新点上的物资配置 |

## Functions

### StartSpawnerManager

生效范围 服务器
	  启动管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetSpawnerManager

生效范围 服务器
	  重置管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CleanAllItem

生效范围 服务器
	  清理刷出的物资

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PauseSpawnerManager

生效范围 服务器
	  暂停物资刷新管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResumeSpawnerManager

生效范围 服务器
	  恢复物资刷新管理器

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetItemConfigOverrideForSpawner

生效范围 服务器
	  修改特定刷新点的物资配置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InItemConfig | [FUGCItemSpawnerItemConfig](../../../cppstruct/F/FU/FUGCItemSpawnerItemConfig.md) | 新的物资刷新配置 |
| SpawnerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetItemConfigOverride

生效范围 服务器
	  修改所有刷新点的物资配置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InItemConfig | [FUGCItemSpawnerItemConfig](../../../cppstruct/F/FU/FUGCItemSpawnerItemConfig.md) | 新的物资刷新配置 |

**Return**

- Type: 
- Description: _None_

### CleanAllItemConfigOverride

生效范围 服务器
	  清除刷新点的物资配置设置，调用后将使用刷新点本身的配置

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

| Name | Type | Description |
| --- | --- | --- |
| OnItemsSpawn |  | 生效范围 服务器<br>	  物品刷新 |

## Delegate

_None_

## Language

cpp

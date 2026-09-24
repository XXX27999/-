# FUGCMobSpawnerMobConfig

刷怪系统：怪物刷新配置

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ConfigMode | [EUGCMobSpawnerConfigMode](../../../cppenum/E/EU/EUGCMobSpawnerConfigMode.md) | 刷出怪物类型的配置方式 |
| MobClass | `TSubclassOf < AGenericCharacter >` | 使用蓝图配置时，刷出的怪物类 |
| MobGroupID | `int32` | 使用怪物组表时，怪物组表的ID |
| CustomParam | `TMap < FString , FString >` | 使用自定义模式时，自定义参数列表 |

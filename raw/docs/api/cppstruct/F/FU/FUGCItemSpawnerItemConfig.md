# FUGCItemSpawnerItemConfig

物资配置

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ConfigMode | [EUGCItemSpawnerConfigMode](../../../cppenum/E/EU/EUGCItemSpawnerConfigMode.md) | 刷出物资的配置方式 |
| ItemID | `int32` | 使用物资ID模式时，物资的ID |
| ItemCount | `int32` | 使用物资ID模式时，物资的数量 |
| DropID | `int32` | 使用掉落表模式时，掉落表的ID |
| DropGroupID | `int32` | 使用掉落组表模式时，掉落组表的ID |
| CustomParam | `TMap < FString , FString >` | 使用自定义模式时，用于自定义的ID |

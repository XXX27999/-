# FUGCRankingListData

排行榜表格结构体

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ID | `int32` | 排行榜索引ID |
| PeopleNum | `int32` | 排行榜最大上榜人数 |
| PeriodType | [ERankListPeriodType](../../../cppenum/E/ER/ERankListPeriodType.md) | 排行榜周期类型 |
| BeginDate | `FDateTime` | 排行榜开始时间 |
| SettleDate | `FDateTime` | 非周期榜结算时间 |
| EndDate | `FDateTime` | 排行榜结束时间 |
| SortPropertyName | `FString` | 排序属性名称 |
| SortType | [ERankListSortType](../../../cppenum/E/ER/ERankListSortType.md) | 排序类型 |
| RankAward | `TArray < FRankListAward >` | 排行榜奖励列表 |
| TabName | `FString` | 排行榜页签名称 |
| EnableType | [ERankListEnableType](../../../cppenum/E/ER/ERankListEnableType.md) | 是否启用排行榜 |
| ShowInGame | [ERankListDisplayType](../../../cppenum/E/ER/ERankListDisplayType.md) | 是否在玩法内展示 |
| ShowInDetails | [ERankListDisplayType](../../../cppenum/E/ER/ERankListDisplayType.md) | 是否在玩法详情页展示 |
| Desc | `FString` | 排行榜说明 |
| ScoreFormatType | [ERankListScoreFormatType](../../../cppenum/E/ER/ERankListScoreFormatType.md) | 分数显示格式 |
| EnableFriendRank | [EFriendRankListEnableType](../../../cppenum/E/EF/EFriendRankListEnableType.md) | 是否启用好友榜 |

# FUGCTaskConfig

任务结构体

## Fields

| Name | Type | Description |
| --- | --- | --- |
| TaskID | `int32` | 任务ID |
| TaskName | `FString` | 任务名称 |
| TaskType | `UUGCTaskTypeBase *` | 任务类型 |
| TaskDesc | `FString` | 任务说明 |
| TaskAwardList | `TArray < FUGCRankingListAwardItem >` | 任务奖励列表 |
| BeginDate | `FDateTime` | 开始时间 |
| EndDate | `FDateTime` | 结束时间 |
| IsShowOutDate | `bool` | 过期后是否显示 |
| IsShowGotoBtn | `bool` | 是否显示任务的前往按钮 |

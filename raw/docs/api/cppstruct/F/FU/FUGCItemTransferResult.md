# FUGCItemTransferResult

物品转移结果

## Fields

| Name | Type | Description |
| --- | --- | --- |
| CanTransfer | `bool` | 转移是否成功 |
| TransferErrorReason | `TArray < FName >` | 如果转移失败，失败原因来自于转移者 |
| ItemErrorReason | `TMap < FItemDefineID , FName >` | 如果转移失败，失败原因来自于物品 |

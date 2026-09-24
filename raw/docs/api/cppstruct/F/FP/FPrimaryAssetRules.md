# FPrimaryAssetRules

Structure defining rules for what to do with assets, this is defined per type and can be overridden per asset

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Priority | `int32` | Primary Assets with a higher priority will take precedence over lower priorities when assigning management for referenced assets. If priorities match, both will manage the same Secondary Asset. |
| bApplyRecursively | `bool` | If true, this rule will apply to all referenced Secondary Assets recursively, as long as they are not managed by a higher-priority Primary Asset. |
| PriorityRule | [EPrimaryAssetPriorityRule](../../../cppenum/E/EP/EPrimaryAssetPriorityRule.md) | SetManageReferences时优先级规则. |
| ChunkId | `int32` | Assets will be put into this Chunk ID specifically, if set to something other than -1. The default Chunk is Chunk 0. |
| CookRule | [EPrimaryAssetCookRule](../../../cppenum/E/EP/EPrimaryAssetCookRule.md) | Rule describing when this asset should be cooked. |
| ManagementRules | `TArray < FManagementRule >` |  |

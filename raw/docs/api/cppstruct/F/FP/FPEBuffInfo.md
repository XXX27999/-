# FPEBuffInfo

包含了Buff的所有配置信息

## Fields

| Name | Type | Description |
| --- | --- | --- |
| UIInfo | [FPEBuffUIInfo](./FPEBuffUIInfo.md) | Buff的UI信息 |
| ApplyTagGroup | `FGameplayTagGroups` | Tag的配置组，包含该Buff与各个Tag的互斥关系 |
| MergeConditionType | [EPEBuffMergeConditionType](../../../cppenum/E/EP/EPEBuffMergeConditionType.md) | 配置另一个Buff能够与当前Buff合并的判断条件，可以通过CanMerge_BP扩展这个条件，CanMerge_BP与当前条件是“与”的关系 |
| MergeTypeMask | `uint32` | 配置另一个Buff合并到当前后的行为，可通过OnMerge_BP扩展这些行为 |
| MaxStackNum | `int32` | 最大堆叠次数 |
| DurationStrategy | [EPEBuffDurationType](../../../cppenum/E/EP/EPEBuffDurationType.md) | 堆叠持续时长计算方式 |
| BuffEffects | `TArray < UPEBuffEffectBase * >` | 触发效果 |

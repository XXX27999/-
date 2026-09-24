# FDataDrivenPESkillCDWapper

技能CD信息（DataDriven 版本，带 CustomizedSerialize）
  用于 Mobile 序列化，不影响主干逻辑

## Fields

| Name | Type | Description |
| --- | --- | --- |
| CDType | [EPESkillCDType](../../../cppenum/E/EP/EPESkillCDType.md) | 技能CD类型 |
| CDRecoveryTime | `float` | CD能量充能时间 |
| AllowRecoveryDuringActivation | `bool` | 技能激活期间恢复CD能量 |
| MaxLayer | `int` | 最大充能次数 |
| CDEnergyConsume | `float` | 持续消耗型每秒扣除速率 |
| AllowConsumeMinEnergy | `float` | 能开始消耗能量的最小百分比 |
| ConsumeTimeType | [EPESkillConsumeTimeType](../../../cppenum/E/EP/EPESkillConsumeTimeType.md) | CD能量和消耗扣除时机 |

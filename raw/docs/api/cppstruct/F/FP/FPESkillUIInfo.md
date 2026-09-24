# FPESkillUIInfo

技能UI信息

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SkillName | `FName` | 技能名字 |
| OverwriteSkillName | `FName` | 覆盖的技能名字，该字段不为空时UI优先显示覆盖的技能名字 |
| SkillDetail | `FString` | 技能描述 |
| OverwriteSkillDetail | `FString` | 覆盖的技能描述，该字段不为空时UI优先显示覆盖的技能描述 |
| SkillIcon | [FSoftObjectPath](../FS/FSoftObjectPath.md) | 技能图标 |
| OverwriteSkillIcon | [FSoftObjectPath](../FS/FSoftObjectPath.md) | 覆盖的技能图标，该字段不为空时UI优先显示覆盖的技能图标 |
| bUseSkillUISlot | `bool` | 是否使用技能预设UI槽位，勾了这个选项的话，则会走createui的逻辑注册到技能槽位上，否则走技能UI绑定技能槽位获取技能的逻辑 |
| PESkillUIAsset | `FSoftClassPath` | 默认技能UI |
| SkillUISlot | [FGameplayTag](../FG/FGameplayTag.md) | 预设技能UI插槽 |

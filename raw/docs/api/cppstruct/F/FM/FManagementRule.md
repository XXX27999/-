# FManagementRule

ManagementRule逻辑规则的运行时版本

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |
| SetResult | [EAssetSetManagerResult](../../../cppenum/E/EA/EAssetSetManagerResult.md) |  |
| CheckTargetDirectories | [FManagementRuleFStringArrayCheck](./FManagementRuleFStringArrayCheck.md) |  |
| CheckTargetAssets | [FManagementRuleFNameArrayCheck](./FManagementRuleFNameArrayCheck.md) |  |
| CheckTargetAssetClassTypes | [FManagementRuleFNameArrayCheck](./FManagementRuleFNameArrayCheck.md) |  |
| CheckTargetAssetTags | [FManagementRuleFNameArrayCheck](./FManagementRuleFNameArrayCheck.md) |  |
| CheckSourcePackages | [FManagementRuleFNameArrayCheck](./FManagementRuleFNameArrayCheck.md) |  |
| CheckSourcePackageClassTypes | [FManagementRuleFNameArrayCheck](./FManagementRuleFNameArrayCheck.md) |  |
| bOnlySoftReferences | `bool` |  |
| CheckOrMask | `uint8` | 控制7个检查条件之间的或与非逻辑，每一位对应一个检查条件（见EManagementRuleCheckOrMask）。<br>	  置1的位参与\|\|组合（OrGroup），置0的位参与&&组合（AndGroup）。<br>	  最终结果 = AndGroup全部为true && (OrGroup为空 \|\| OrGroup至少一个为true)。<br>	  默认值0x00，即全部&&，保持原有行为。 |

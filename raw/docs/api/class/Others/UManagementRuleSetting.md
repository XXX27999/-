# UManagementRuleSetting

ManagementRule逻辑规则的.ini文件配置版本，减少结构体和容器嵌套，方便.ini配置和阅读

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |
| SetResult | [EAssetSetManagerResult](../../cppenum/E/EA/EAssetSetManagerResult.md) |  |
| CheckTargetDirectoriesSwitch | [FManagementRuleSwitch](../../cppstruct/F/FM/FManagementRuleSwitch.md) |  |
| CheckTargetDirectories | `TArray < FManagementRuleFStringCheck >` |  |
| CheckTargetAssetsSwitch | [FManagementRuleSwitch](../../cppstruct/F/FM/FManagementRuleSwitch.md) |  |
| CheckTargetAssets | `TArray < FManagementRuleFNameCheck >` |  |
| CheckTargetAssetClassSwitch | [FManagementRuleSwitch](../../cppstruct/F/FM/FManagementRuleSwitch.md) |  |
| CheckTargetAssetClassTypes | `TArray < FManagementRuleFNameCheck >` |  |
| CheckSourcePackagesSwitch | [FManagementRuleSwitch](../../cppstruct/F/FM/FManagementRuleSwitch.md) |  |
| CheckSourcePackages | `TArray < FManagementRuleFNameCheck >` |  |
| CheckSourcePackageClassTypes | `TArray < FManagementRuleFNameCheck >` |  |
| CheckSourcePackageClassSwitch | [FManagementRuleSwitch](../../cppstruct/F/FM/FManagementRuleSwitch.md) |  |
| CheckTargetAssetTagSwitch | [FManagementRuleSwitch](../../cppstruct/F/FM/FManagementRuleSwitch.md) |  |
| CheckTargetAssetTags | `TArray < FManagementRuleFNameCheck >` |  |
| bOnlySoftReferences | `bool` |  |
| CheckOrMask | `uint8` | 对应FManagementRule::CheckOrMask，控制6个检查条件之间的或与非逻辑，见EManagementRuleCheckOrMask |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

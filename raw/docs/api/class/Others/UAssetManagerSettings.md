# UAssetManagerSettings

Settings for the Asset Management framework, which can be used to discover, load, and audit game-specific asset types

## Parents

- UDeveloperSettings

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PrimaryAssetTypesToScan | `TArray < FPrimaryAssetTypeInfo >` | List of asset types to scan at startup |
| DirectoriesToExclude | `TArray < FDirectoryPath >` | List of directories to exclude from scanning for Primary Assets, useful to exclude test assets |
| PrimaryAssetRules | `TArray < FPrimaryAssetRulesOverride >` | List of specific asset rule overrides |
| bOnlyCookProductionAssets | `bool` | If true, DevelopmentCook assets will error when they are cooked |
| bShouldGuessTypeAndNameInEditor | `bool` | If true, PrimaryAsset TypeName will be implied for assets in the editor (cooked builds always must be explicit). This allows guessing for content that hasn't been resaved yet |
| bShouldAcquireMissingChunksOnLoad | `bool` | If true, this will query the platform chunk install interface to request missing chunks for any requested primary asset loads |
| IndexOfUsingAutoChunkName | `int32` |  |
| PrimaryAssetIdRedirects | `TArray < FAssetManagerRedirect >` | Redirect from Type:Name to Type:NameNew |
| PrimaryAssetTypeRedirects | `TArray < FAssetManagerRedirect >` | Redirect from Type to TypeNew |
| AssetPathRedirects | `TArray < FAssetManagerRedirect >` | Redirect from gameassetpath to gameassetpathnew |
| MetaDataTagsForAssetRegistry | `TSet < FName >` | The metadata tags to be transferred to the Asset Registry. |
| bParsePAWhenDroped | `bool` | Asset Audit解析拖拽的PA. |
| DefaultChunkName | `FString` | 默认Core包名. |
| BlacklistFilePath | [FFilePath](../../cppstruct/F/FF/FFilePath.md) | 编辑器检查用黑名单文件路径. |
| BlacklistForPackageFilePath | [FFilePath](../../cppstruct/F/FF/FFilePath.md) | 打包用黑名单文件路径. |
| bAlwaysReloadCSVConfig | `bool` | 是否每次检查都重新读取黑名单配置. |
| bUseBlacklistMap | `bool` | 构造所有黑名单文件夹的文件Map来查找. |
| bEnableCheckBlacklist | `bool` | Whether check the asset depend on blacklist asset in content browser. |
| SearchingDepth | `int32` | The depth of searching blacklist asset tree in content browser. |
| ManagementRuleConfigPath | `FString` |  |
| bUseAllMetaDataTagsForAssetRegistry | `bool` |  |
| bEnableModelStage | `bool` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

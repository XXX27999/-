# UPrimaryAssetLabel

A seed file that is created to mark referenced assets as part of this primary asset

## Parents

- [UPrimaryDataAsset](./UPrimaryDataAsset.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Rules | [FPrimaryAssetRules](../../cppstruct/F/FP/FPrimaryAssetRules.md) | Management rules for this specific asset, if set it will override the type rules |
| LogicChunkName | `FString` | Pak file name |
| FinalChunkName | `FString` |  |
| ChunkOutputPath | `FString` |  |
| bLabelAssetsInMyDirectory | `uint32` | True to Label everything in this directory and sub directories |
| AssignedDirectories | `TArray < FDirectoryPath >` | True to Label everything in this directory and sub directories |
| ExcludeDirectories | `TArray < FDirectoryPath >` |  |
| ExcludeAssets | `TSet < FName >` |  |
| bIsRuntimeLabel | `uint32` | Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule |
| ExplicitAssets | `TArray < TSoftObjectPtr < UObject > >` | List of manually specified assets to label |
| ExplicitBlueprints | `TArray < TSoftClassPtr < UObject > >` | List of manually specified blueprint assets to label |
| AssetCollection | [FCollectionReference](../../cppstruct/F/FC/FCollectionReference.md) | Collection to load asset references out of |
| Key | `FString` |  |
| IV | `FString` |  |
| DataTableAsExplicitAssets | `TSoftObjectPtr < UDataTable >` | List of manually specified assets to label |
| ManagerRuleNames | `TArray < FString >` |  |
| bTriggerUpdateManagerRules | `bool` |  |
| bUpdateManagerRulesWhenSaved | `bool` |  |
| bForceReloadManagerRule | `bool` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

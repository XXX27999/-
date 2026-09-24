# UChunkLabel

## Parents

- [UPrimaryDataAsset](./UPrimaryDataAsset.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Rules | [FPrimaryAssetRules](../../cppstruct/F/FP/FPrimaryAssetRules.md) | Management rules for this specific asset, if set it will override the type rules |
| LogicChunkName | `FString` | True to Label everything in this directory and sub directories |
| FinalChunkName | `FString` |  |
| ChunkOutputPath | `FString` |  |
| bIsRuntimeLabel | `uint32` | Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule |
| Key | `FString` |  |
| IV | `FString` |  |
| ManagerRuleNames | `TArray < FString >` |  |
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

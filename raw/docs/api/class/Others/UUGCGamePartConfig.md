# UUGCGamePartConfig

GamePart配置基类

## Parents

- [UPrimaryDataAsset](./UPrimaryDataAsset.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| GamePartName | `FName` | GamePart名称 |
| DependentGameParts | `TArray < FName >` | 依赖的的GamePart列表 |
| GlobalActorClass | `TSubclassOf < AActor >` | GlobalActor类配置 |
| PlayerComponentConfigs | `TArray < FUGCGamePartPlayerComponentConfig >` | GamePart PlayerComponent配置列表 |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

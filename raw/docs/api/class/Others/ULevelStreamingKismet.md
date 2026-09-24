# ULevelStreamingKismet

## Parents

- [ULevelStreaming](./ULevelStreaming.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bInitiallyLoaded | `uint32` | Whether the level should be loaded at startup |
| bInitiallyVisible | `uint32` | Whether the level should be visible at startup if it is loaded |

## Functions

### LoadLevelInstance

Stream in a level with a specific location and rotation. You can create multiple instances of the same level!

 	 The level to be loaded does not have to be in the persistent map's Levels list, however to ensure that the .umap does get
 	 packaged, please be sure to include the .umap in your Packaging Settings:

 	   Project Settings -> Packaging -> List of Maps to Include in a Packaged Build (you may have to show advanced or type in filter)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| LevelName | `FString &` | - Level package name, ex: GameMapsMyMapName, specifying short name like MyMapName will force very slow search on disk |
| Location | `FVector &` | - World space location where the level should be spawned |
| Rotation | `FRotator &` | - World space rotation for rotating the entire level |
| bOutSuccess | `bool &` | - Whether operation was successful (map was found and added to the sub-levels list) |

**Return**

- Type: 
- Description: _None_

### CreateLevelInstanceWithLevelName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| LevelName | `FString &` |  |
| UniqueName | `FString &` |  |
| Trans | `FTransform &` |  |
| bOutSuccess | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### CreateLevelInstanceWithLevel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OriStreamingLevel | `ULevelStreaming *` |  |
| UniqueName | `FString &` |  |
| Trans | `FTransform &` |  |
| bOutSuccess | `bool &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

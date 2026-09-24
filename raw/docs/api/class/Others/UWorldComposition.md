# UWorldComposition

WorldComposition represents world structure:
 	- Holds list of all level packages participating in this world and theirs base parameters (bounding boxes, offset from origin)
 	- Holds list of streaming level objects to stream in and out based on distance from current view point
   - Handles properly levels repositioning during level loading and saving

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Package2WorldTileExtraInfo | `TMap < FName , FWorldTileExtraInfo >` |  |
| LODStealConfigs | `TArray < FLODStealConfig >` |  |
| TilesStreaming | `TArray < ULevelStreaming * >` |  |
| TilesStreamingTimeThreshold | `double` |  |
| bLoadAllTilesDuringCinematic | `bool` |  |
| bRebaseOriginIn3DSpace | `bool` |  |
| RebaseOriginDistance | `float` |  |
| TileBoundsVerifyScale | `float` |  |
| bFlushPool | `bool` |  |
| ServerExcludedLevels | `TArray < FString >` |  |
| ClientExcludedLevels | `TArray < FString >` |  |
| UGCPIEMapBlackList | `TArray < FString >` |  |
| UGCWhiteListSubLevelPaths | `TArray < FString >` |  |
| DeviceExcludedLevels | `TArray < FString >` |  |
| DynamicSubLevelPaths | `TArray < FString >` |  |
| BlackLevelPaths | `TArray < FString >` |  |
| SpecifiedBuildingLevels | `TArray < FString >` |  |
| ClientLoadRadiusFactor | `float` |  |

## Functions

### CheckBisNeedSavedLevelToFileInServer

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

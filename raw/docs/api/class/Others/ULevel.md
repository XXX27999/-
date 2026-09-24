# ULevel

A Level is a collection of Actors (lights, volumes, mesh instances etc.).
  Multiple Levels can be loaded and unloaded into the World to create a streaming experience.

  @see UActor

## Parents

- [UObject](./UObject.md)
- IInterface_AssetUserData

## Variables

| Name | Type | Description |
| --- | --- | --- |
| OwningWorld | `UWorld *` | The World that has this level in its Levels array.<br>	  This is not the same as GetOuter(), because GetOuter() for a streaming level is a vestigial world that is not used.<br>	  It should not be accessed during BeginDestroy(), just like any other UObject references, since GC may occur in any order. |
| Model | `UModel *` | BSP UModel. |
| ModelComponents | `TArray < UModelComponent * >` | BSP Model components used for rendering. |
| ActorCluster | `ULevelActorContainer *` |  |
| NumTextureStreamingUnbuiltComponents | `int32` | Num of components missing valid texture streaming data. Updated in map check. |
| NumTextureStreamingDirtyResources | `int32` | Num of resources that have changed since the last texture streaming build. Updated in map check. |
| LevelScriptActor | `ALevelScriptActor *` | The level scripting actor, created by instantiating the class from LevelScriptBlueprint.  This handles all level scripting |
| NavListStart | `ANavigationObjectBase *` | Start and end of the navigation list for this level, used for quickly fixing up<br>	  when streaming this level inout. @TODO DEPRECATED - DELETE |
| NavListEnd | `ANavigationObjectBase *` |  |
| NavDataChunks | `TArray < UNavigationDataChunk * >` | Navigation related data that can be stored per level |
| LightmapTotalSize | `float` | Total number of KB used for lightmap textures in the level. |
| ShadowmapTotalSize | `float` | Total number of KB used for shadowmap textures in the level. |
| StaticNavigableGeometry | `TArray < FVector >` | threes of triangle vertices - AABB filtering friendly. Stored if there's a runtime need to rebuild navigation that accepts BSPs<br>	 	as well - it's a lot easier this way than retrieve this data at runtime |
| StreamingTextureGuids | `TArray < FGuid >` | The Guid of each texture refered by FStreamingTextureBuildInfo::TextureLevelIndex |
| LevelVolumeProbeGIBakedStreamingData | `ULevelVolumeProbeGIBakedStreamingData *` |  |
| PVSHandlerHash | `FString` |  |
| PrecomputedVisibilityDataRegistry | `UPrecomputedVisibilityDataRegistry *` |  |
| bIsLightingScenario | `bool` | Whether the level is a lighting scenario.  Lighting is built separately for each lighting scenario level with all other scenario levels hidden.<br>	  Only one lighting scenario level should be visible at a time for correct rendering, and lightmaps from that level will be used on the rest of the world.<br>	  Note: When a lighting scenario level is present, lightmaps for all streaming levels are placed in the scenario's _BuildData package.<br>	 		This means that lightmaps for those streaming levels will not be streamed with them. |
| LevelBuildDataId | [FGuid](../../cppstruct/F/FG/FGuid.md) | Identifies map build data specific to this level, eg lighting volume samples. |
| LightBuildLevelOffset | [FIntVector](../../cppstruct/F/FI/FIntVector.md) | Level offset at time when lighting was built |
| bTextureStreamingRotationChanged | `uint8` | Whether a level transform rotation was applied since the texture streaming builds. Invalidates the precomputed streaming bounds. |
| bIsVisible | `uint8` | Whether the level is currently visible associated with the world |
| bLocked | `uint8` | Whether this level is locked; that is, its actors are read-only<br>	 	Used by WorldBrowser to lock a level when corresponding ULevelStreaming does not exist |
| bPVSDirty | `uint8` |  |
| WorldSettings | `AWorldSettings *` |  |
| MapBuildData | `UMapBuildDataRegistry *` | Registry for data from the map build.  This is stored in a separate package from the level to speed up saving  autosaving.<br>	  ReleaseRenderingResources must be called before changing what is referenced, to update the rendering thread state. |
| RCRCommunicatorClassName | `FSoftClassPath` |  |
| RCRCommunicator | `URCRCommunicator *` |  |
| MeshRefCounter | `TMap < UStaticMesh * , int32 >` |  |
| Level_RCR | `ULevel_RCR *` |  |
| AssetUserData | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| LevelScriptBlueprint | `ULevelScriptBlueprint *` | Reference to the blueprint for level scripting |
| TextureStreamingResourceGuids | `TArray < FGuid >` | The Guid list of all materials and meshes Guid used in the last texture streaming build. Used to know if the streaming data needs rebuild. Only used for the persistent level. |
| LevelSimplification | [FLevelSimplificationDetails](../../cppstruct/F/FL/FLevelSimplificationDetails.md) | Level simplification settings for each LOD |
| PlatformLevelSimplification | `TArray < FLevelSimplificationDetails >` |  |
| LevelColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | The level color used for visualization. (Show -> Advanced -> Level Coloration)<br>	  Used only in world composition mode |
| CurrentTieredMapBuildData | `UMapBuildDataRegistry *` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

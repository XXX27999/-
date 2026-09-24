# AWorldSettings

Actor containing all script accessible world properties.

## Parents

- [AInfo](./AInfo.md)
- IInterface_AssetUserData

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BlueprintContainer | `TSubclassOf < AActor >` |  |
| SaveLocOffset | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| bEnableFOVDistanceCulling | `uint32` | FOV Distance Culling |
| FOVCulling | `TArray < FVector2D >` |  |
| bEnableWorldBoundsChecks | `uint32` | DEFAULT BASIC PHYSICS SETTINGS<br>	 If true, enables CheckStillInWorld checks |
| bEnableNavigationSystem | `uint32` | if set to false navigation system will not get created (and all navigation functionality won't be accessible) |
| bEnableAISystem | `uint32` | if set to false AI system will not get created. Use it to disable all AI-related activity on a map |
| bEnalbeLevelLoadConditionControl | `uint32` |  |
| bEnableWorldComposition | `uint32` | Enables tools for composing a tiled world.<br>	  Level has to be saved and all sub-levels removed before enabling this option. |
| bWorldCompositionPIESupportLevelRotation | `uint32` |  |
| bPIECloseFixupLazyPointers | `uint32` |  |
| bEnableRescanRestriction | `uint32` |  |
| bOnlyIncludeWhiteList | `uint32` |  |
| bAlwaysExcludeBlackList | `uint32` |  |
| WhiteListRescanFolders | `TArray < FString >` |  |
| WhiteListRescanLevelPaths | `TArray < FString >` |  |
| BlackListRescanFolders | `TArray < FString >` |  |
| BlackListRescanLevelPaths | `TArray < FString >` |  |
| bEnableAdditionalRescanRoots | `uint32` | Master switch for cross-folder sub-levels. When enabled, AdditionalRescanRoots is<br>	  consumed by UWorldComposition::Rescan() to scan extra mounted content roots in<br>	  addition to the persistent map's own folder.<br><br>	  Orthogonal to bEnableRescanRestriction (WhiteListBlackList): both can be combined. |
| AdditionalRescanRoots | `TArray < FAdditionalRescanRootEntry >` | Per-root scan and filter configuration. See FAdditionalRescanRootEntry.<br><br>	  Example:<br>	    [0] RootPath     = GameCommonSharedTiles<br>	        IncludeTiles = ["Forest", "PlainTile_X0_Y0"]<br>	        ExcludeTiles = ["ForestDebug_Tile"]<br>	    [1] RootPath     = GameCommonSharedBuildings<br>	        ExcludeTiles = ["Office_LowPoly"]<br><br>	  Notes:<br>	    - LOD tiles (_LOD1.._LOD4) must still sit next to their owning tile.<br>	    - Filters in this struct are independent of the global WhiteListBlackList Rescan settings. |
| bUseClientSideLevelStreamingVolumes | `uint32` | Enables client-side streaming volumes instead of server-side.<br>	  Expected usage scenario: server has all streaming levels always loaded, clients independently stream levels inout based on streaming volumes. |
| bEnableWorldOriginRebasing | `uint32` | World origin will shift to a camera position when camera goes far away from current origin |
| bWorldGravitySet | `uint32` | if set to true, when we call GetGravityZ we assume WorldGravityZ has already been initialized and skip the lookup of DefaultGravityZ and GlobalGravityZ |
| bGlobalGravitySet | `uint32` | If set to true we will use GlobalGravityZ instead of project setting DefaultGravityZ |
| KillZ | `float` |  |
| KillZDamageType | `TSubclassOf < UDamageType >` |  |
| WorldGravityZ | `float` |  |
| GlobalGravityZ | `float` |  |
| DefaultPhysicsVolumeClass | `TSubclassOf < ADefaultPhysicsVolume >` |  |
| PhysicsCollisionHandlerClass | `TSubclassOf < UPhysicsCollisionHandler >` |  |
| DefaultGameMode | `TSubclassOf < AGameModeBase >` | GAMEMODE SETTINGS<br>	 The default GameMode to use when starting this map in the game. If this value is NULL, the INI setting for default game type is used. |
| GameNetworkManagerClass | `TSubclassOf < AGameNetworkManager >` | Class of GameNetworkManager to spawn for network games |
| StreamVolumeExManagerClass | `TSubclassOf < AStreamVolumeExManager >` |  |
| PackedLightAndShadowMapTextureSize | `int32` | RENDERING SETTINGS<br>	 Maximum size of textures for packed light and shadow maps |
| bMinimizeBSPSections | `uint32` | Causes the BSP build to generate as few sections as possible.<br>	  This is useful when you need to reduce draw calls but can reduce texture streaming efficiency and effective lightmap resolution.<br>	  Note - changes require a rebuild to propagate.  Also, be sure to select all surfaces and make sure they all have the same flags to minimize section count. |
| DefaultColorScale | [FVector](../../cppstruct/F/FV/FVector.md) | Default color scale for the level |
| DefaultMaxDistanceFieldOcclusionDistance | `float` | Max occlusion distance used by mesh distance fields, overridden if there is a movable skylight. |
| GlobalDistanceFieldViewDistance | `float` | Distance from the camera that the global distance field should cover. |
| bEnableUpdateTransformViewTranslated | `uint32` |  |
| bEnableWorldComposition2DLoading | `uint32` |  |
| MaxWorldSize | `float` |  |
| RegionSizeNear | `int32` |  |
| RegionSizeFar | `int32` |  |
| RegionXAdd | `bool` |  |
| RegionYAdd | `bool` |  |
| UnlimitedRegionZ | `bool` |  |
| Graduation | `int32` |  |
| CompositionSize | `int32` |  |
| DynamicIndirectShadowsSelfShadowingIntensity | `float` | Controls the intensity of self-shadowing from capsule indirect shadows.<br>	  These types of shadows use approximate occluder representations, so reducing self-shadowing intensity can hide those artifacts. |
| bPrecomputeVisibility | `uint32` | PRECOMPUTED VISIBILITY SETTINGS<br><br>	  Whether to place visibility cells inside Precomputed Visibility Volumes and along camera tracks in this level.<br>	  Precomputing visibility reduces rendering thread time at the cost of some runtime memory and somewhat increased lighting build times. |
| bPlaceCellsOnlyAlongCameraTracks | `uint32` | Whether to place visibility cells only along camera tracks or only above shadow casting surfaces. |
| VisibilityCellSize | `int32` | World space size of precomputed visibility cells in x and y.<br>	  Smaller sizes produce more effective occlusion culling at the cost of increased runtime memory usage and lighting build times. |
| PlayAreaHeight | `float` | Play Area Height ( Cell Z |
| DynamicCellSize | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | Dynamic Cell Size ( Dynamic Cell XY, Z |
| PrecomputedVisibilitySettings | [FLightmassPrecomputedVisibilitySettings](../../cppstruct/F/FL/FLightmassPrecomputedVisibilitySettings.md) |  |
| VisibilityAggressiveness | `TEnumAsByte < enum EVisibilityAggressiveness >` | Determines how aggressive precomputed visibility should be.<br>	  More aggressive settings cull more objects but also cause more visibility errors like popping. |
| bForceNoPrecomputedLighting | `uint32` | LIGHTMASS RELATED SETTINGS<br><br>	  Whether to force lightmaps and other precomputed lighting to not be created even when the engine thinks they are needed.<br>	  This is useful for improving iteration in levels with fully dynamic lighting and shadowing.<br>	  Note that any lighting and shadowing interactions that are usually precomputed will be lost if this is enabled. |
| bUseTieredBuildData | `uint32` |  |
| LightmassSettings | [FLightmassWorldInfoSettings](../../cppstruct/F/FL/FLightmassWorldInfoSettings.md) |  |
| LightmassSettingsHigh | [FLightmassWorldInfoSettings](../../cppstruct/F/FL/FLightmassWorldInfoSettings.md) |  |
| LightmassSettingsHighPlus | [FLightmassWorldInfoSettings](../../cppstruct/F/FL/FLightmassWorldInfoSettings.md) |  |
| IdeaBakingSettings | [FIdeaBakingWorldInfoSettings](../../cppstruct/F/FI/FIdeaBakingWorldInfoSettings.md) |  |
| SurfelRayTracingSettings | [FSurfelRayTracingSettings](../../cppstruct/F/FS/FSurfelRayTracingSettings.md) |  |
| DefaultReverbSettings | [FReverbSettings](../../cppstruct/F/FR/FReverbSettings.md) | AUDIO SETTINGS<br>	 Default reverb settings used by audio volumes. |
| DefaultAmbientZoneSettings | [FInteriorSettings](../../cppstruct/F/FI/FInteriorSettings.md) | Default interior settings used by audio volumes. |
| DefaultBaseSoundMix | `USoundMix *` | Default Base SoundMix. |
| WorldToMeters | `float` | DEFAULT SETTINGS<br>	 scale of 1uu to 1m in real world measurements, for HMD and other physically tracked devices (e.g. 1uu = 1cm would be 100.0) |
| MonoCullingDistance | `float` | Distance from the player after which content will be rendered in mono if monoscopic far field rendering is activated |
| BookMarks | `UBookMark *` | EDITOR ONLY SETTINGS<br>	 Level Bookmarks: 10 should be MAX_BOOKMARK_NUMBER @fixmeconst |
| TimeDilation | `float` | Normally 1 - scales real time passage.<br>	  Warning - most use cases should use GetEffectiveTimeDilation() instead of reading from this directly |
| MatineeTimeDilation | `float` |  |
| DemoPlayTimeDilation | `float` |  |
| MinGlobalTimeDilation | `float` | Lowest acceptable global time dilation. |
| MaxGlobalTimeDilation | `float` | Highest acceptable global time dilation. |
| MinUndilatedFrameTime | `float` | Smallest possible frametime, not considering dilation. Equiv to 1FastestFPS. |
| MaxUndilatedFrameTime | `float` | Largest possible frametime, not considering dilation. Equiv to 1SlowestFPS. |
| Pauser | `APlayerState *` |  |
| bHighPriorityLoading | `uint32` | when this flag is set, more time is allocated to background loading (replicated) |
| bHighPriorityLoadingLocal | `uint32` | copy of bHighPriorityLoading that is not replicated, for clientside-only loading operations |
| ReplicationViewers | `TArray < struct FNetViewer >` | valid only during replication - information about the player(s) being replicated to<br>	  (there could be more than one in the case of a splitscreen client) |
| AssetUserData | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| LODRelativeDistances | `TArray < float >` |  |
| bEnablestreamingLevelLOD | `bool` |  |
| WorldCompositionNums | `int32` |  |
| CompositionBlockLength | `int32` |  |
| OriginOfTheRegion | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| bEnableObjectPool | `bool` |  |
| LevelReorganizationData | `UDataAsset *` |  |
| bEnableParticleSignificance | `bool` |  |
| bEnableHierarchicalLODSystem | `uint32` | if set to true, hierarchical LODs will be built, which will create hierarchical LODActors |
| HLODSetupAsset | `TSoftClassPtr < UHierarchicalLODSetup >` | If set overrides the level settings and global project settings |
| OverrideBaseMaterial | `TSoftObjectPtr < UMaterialInterface >` | If set overrides the project-wide base material used for Proxy Materials |
| HierarchicalLODSetup | `TArray < struct FHierarchicalSimplification >` | Hierarchical LOD Setup |
| NumHLODLevels | `int32` |  |
| bGenerateSingleClusterForLevel | `uint32` | if set to true, all eligible actors in this level will be added to a single cluster representing the entire level (used for small sublevels) |

## Functions

### SaveEntireWorld

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_WorldGravityZ

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

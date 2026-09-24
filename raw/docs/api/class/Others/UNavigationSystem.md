# UNavigationSystem

## Parents

- UBlueprintFunctionLibrary

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MainNavData | `ANavigationData *` |  |
| AbstractNavData | `ANavigationData *` | special navigation data for managing direct paths, not part of NavDataSet! |
| CrowdManagerClass | `TSubclassOf < UCrowdManagerBase >` |  |
| bAutoCreateNavigationData | `uint32` | Should navigation system spawn default Navigation Data when there's none and there are navigation bounds present? |
| bAllowClientSideNavigation | `uint32` |  |
| bSupportRebuilding | `uint32` | gets set to true if gathering navigation data (like in navoctree) is required due to the need of navigation generation<br>	 	Is always true in Editor Mode. In other modes it depends on bRebuildAtRuntime of every required NavigationData class' CDO |
| ObstacleManagerClassPath | `FSoftClassPath` |  |
| bInitialBuildingLocked | `uint32` | if set to true will result navigation system not rebuild navigation until<br>	 	a call to ReleaseInitialBuildingLock() is called. Does not influence<br>	 	editor-time generation (i.e. does influence PIE and Game).<br>	 	Defaults to false. |
| bWholeWorldNavigable | `uint32` | If set to true (default) navigation will be generated only within special navigation<br>	 	bounds volumes (like ANavMeshBoundsVolume). Set to false means navigation should be generated<br>	 	everywhere. |
| bSkipAgentHeightCheckWhenPickingNavData | `uint32` | false by default, if set to true will result in not caring about nav agent height<br>	 	when trying to match navigation data to passed in nav agent |
| DataGatheringMode | [ENavDataGatheringModeConfig](../../cppenum/E/EN/ENavDataGatheringModeConfig.md) |  |
| bGenerateNavigationOnlyAroundNavigationInvokers | `uint32` | If set to true navigation will be generated only around registered "navigation enforcers"<br>		This has a range of consequences (including how navigation octree operates) so it needs to<br>		be a conscious decision.<br>		Once enabled results in whole world being navigable.<br>		@see RegisterNavigationInvoker |
| ActiveTilesUpdateInterval | `float` | Minimal time, in seconds, between active tiles set update |
| SupportedAgents | `TArray < FNavDataConfig >` |  |
| DirtyAreasUpdateFreq | `float` | update frequency for dirty areas on navmesh |
| NavDataSet | `TArray < ANavigationData * >` |  |
| NavDataRegistrationQueue | `TArray < ANavigationData * >` |  |
| OperationMode | [FNavigationSystemRunMode](../../cppenum/F/FN/FNavigationSystemRunMode.md) |  |

## Functions

### BP_ChangeRecastPartitioning

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |
| High | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BP_BuildOne

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### BP_DynamicBuildOne

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### BP_Build

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BP_AddDynamicNavAffect

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |
| InBounds | `FBox &` |  |

**Return**

- Type: 
- Description: _None_

### BP_IncrementalBuild

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### BP_CancelBuild

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### BP_GetNavigationData

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AgentName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetNavigationSystem

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### K2_ProjectPointToNavigation

Project a point onto the NavigationData

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Point | `FVector &` |  |
| ProjectedLocation | `FVector &` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |
| QueryExtent | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### K2_GetRandomReachablePointInRadius

Generates a random location reachable from given Origin location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Origin | `FVector &` |  |
| RandomLocation | `FVector &` |  |
| Radius | `float` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |
| ExtentRadius | `float` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetRandomPointInNavigableRadius

Generates a random location in navigable space within given radius of Origin.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Origin | `FVector &` |  |
| RandomLocation | `FVector &` |  |
| Radius | `float` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### GetPathCost

Potentially expensive. Use with caution. Consider using UPathFollowingComponent::GetRemainingPathCost instead

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PathStart | `FVector &` |  |
| PathEnd | `FVector &` |  |
| PathCost | `float &` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### GetPathLength

Potentially expensive. Use with caution

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PathStart | `FVector &` |  |
| PathEnd | `FVector &` |  |
| PathLength | `float &` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### IsNavigationBeingBuilt

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsNavigationBeingBuiltOrLocked

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SimpleMoveToActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AController *` |  |
| Goal | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### SimpleMoveToLocation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Controller | `AController *` |  |
| Goal | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### FindPathToLocationSynchronously

Finds path instantly, in a FindPath Synchronously.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PathStart | `FVector &` |  |
| PathEnd | `FVector &` |  |
| PathfindingContext | `AActor *` | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### FindPathToActorSynchronously

Finds path instantly, in a FindPath Synchronously. Main advantage over FindPathToLocationSynchronously is that
	 	the resulting path will automatically get updated if goal actor moves more than TetherDistance away from last path node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PathStart | `FVector &` |  |
| GoalActor | `AActor *` |  |
| TetherDistance | `float` |  |
| PathfindingContext | `AActor *` | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### NavigationRaycast

Performs navigation raycast on NavigationData appropriate for given Querier.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| RayStart | `FVector &` |  |
| RayEnd | `FVector &` |  |
| HitLocation | `FVector &` | if line was obstructed this will be set to hit location. Otherwise it contains SegmentEnd |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |
| Querier | `AController *` | if not passed default navigation data will be used |

**Return**

- Type: 
- Description: _None_

### SetMaxSimultaneousTileGenerationJobsCount

will limit the number of simultaneously running navmesh tile generation jobs to specified number.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MaxNumberOfJobs | `int32` | gets trimmed to be at least 1. You cannot use this function to pause navmesh generation |

**Return**

- Type: 
- Description: _None_

### ResetMaxSimultaneousTileGenerationJobsCount

Brings limit of simultaneous navmesh tile generation jobs back to Project Setting's default value

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RegisterNavigationInvoker

Registers given actor as a "navigation enforcer" which means navigation system will
	 	make sure navigation is being generated in specified radius around it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Invoker | `AActor *` |  |
| TileGenerationRadius | `float` |  |
| TileRemovalRadius | `float` |  |

**Return**

- Type: 
- Description: _None_

### UnregisterNavigationInvoker

Removes given actor from the list of active navigation enforcers.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Invoker | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### SetGeometryGatheringMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMode | [ENavDataGatheringModeConfig](../../cppenum/E/EN/ENavDataGatheringModeConfig.md) |  |

**Return**

- Type: 
- Description: _None_

### OnNavigationBoundsUpdated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NavVolume | `ANavMeshBoundsVolume *` |  |

**Return**

- Type: 
- Description: _None_

### ProjectPointToNavigation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Point | `FVector &` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |
| QueryExtent | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetRandomReachablePointInRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Origin | `FVector &` |  |
| Radius | `float` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### GetRandomPointInNavigableRadius

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Origin | `FVector &` |  |
| Radius | `float` |  |
| NavData | `ANavigationData *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` |  |

**Return**

- Type: 
- Description: _None_

### UpdateDynamicGenerateTargetNav

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsAdd | `bool` |  |
| GenerateTargetNav | [FDynamicGenerateTargetNavigation](../../cppstruct/F/FD/FDynamicGenerateTargetNavigation.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnNavDataRegisteredEvent |  | UPROPERTY(BlueprintAssignable, Transient) |
| OnNavigationGenerationFinishedDelegate |  |  |

## Language

cpp

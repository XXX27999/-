# ANavigationData

Represents abstract Navigation Data (sub-classed as NavMesh, NavGraph, etc)
 	Used as a common interface for all navigation types handled by NavigationSystem

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| RenderingComp | `UPrimitiveComponent *` |  |
| NavDataConfig | [FNavDataConfig](../../cppstruct/F/FN/FNavDataConfig.md) |  |
| bEnableDrawing | `uint32` | if set to true then this navigation data will be drawing itself when requested as part of "show navigation" |
| bForceRebuildOnLoad | `uint32` | By default navigation will skip the first update after being successfully loaded<br>	  setting bForceRebuildOnLoad to false can override this behavior |
| bCanBeMainNavData | `uint32` | If set, navigation data can act as default one in navigation system's queries |
| bCanSpawnOnRebuild | `uint32` | If set, navigation data will be spawned in persistent level during rebuild if actor doesn't exist |
| bRebuildAtRuntime_DEPRECATED | `uint32` | If true, the NavMesh can be dynamically rebuilt at runtime. |
| RuntimeGeneration | [ERuntimeGenerationType](../../cppenum/E/ER/ERuntimeGenerationType.md) | Navigation data runtime generation options |
| ObservedPathsTickInterval | `float` | all observed paths will be processed every ObservedPathsTickInterval seconds |
| AgentType | `int32` | AgentType for quick match |
| DataVersion | `uint32` | Navigation data versioning. |
| SupportedAreas | `TArray < FSupportedAreaData >` | serialized area class - ID mapping |

## Functions

_None_

## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| BuildTileSortSeedLocationDelegate |  |  |

## Language

cpp

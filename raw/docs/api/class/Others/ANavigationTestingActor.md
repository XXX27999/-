# ANavigationTestingActor

## Parents

- [AActor](./AActor.md)
- INavAgentInterface
- INavPathObserverInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CapsuleComponent | `UCapsuleComponent *` |  |
| InvokerComponent | `UNavigationInvokerComponent *` |  |
| bActAsNavigationInvoker | `uint32` |  |
| NavAgentProps | [FNavAgentProperties](../../cppstruct/F/FN/FNavAgentProperties.md) | @todo document |
| QueryingExtent | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| MyNavData | `ANavigationData *` |  |
| ProjectedLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| ProjectedTile | [FIntVector](../../cppstruct/F/FI/FIntVector.md) |  |
| ProjectedPloyId | `int32` |  |
| bProjectedLocationValid | `uint32` |  |
| bSearchStart | `uint32` |  |
| bUseHierarchicalPathfinding | `uint32` |  |
| bGatherDetailedInfo | `uint32` | if set, all steps of A algorithm will be accessible for debugging |
| bDrawDistanceToWall | `uint32` |  |
| bShowNodePool | `uint32` | show polys from open (orange) and closed (yellow) sets |
| bShowBestPath | `uint32` | show current best path |
| bShowDiffWithPreviousStep | `uint32` | show which nodes were modified in current A step |
| bShouldBeVisibleInGame | `uint32` |  |
| CostDisplayMode | `TEnumAsByte < ENavCostDisplay :: Type >` | determines which cost will be shown |
| TextCanvasOffset | [FVector2D](../../cppstruct/F/FV/FVector2D.md) | text canvas offset to apply |
| bPathExist | `uint32` |  |
| bPathIsPartial | `uint32` |  |
| bPathSearchOutOfNodes | `uint32` |  |
| PathfindingTime | `float` | Time in micro seconds |
| PathCost | `float` |  |
| PathfindingSteps | `int32` |  |
| OtherActor | `ANavigationTestingActor *` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |
| ShowStepIndex | `int32` |  |
| OffsetFromCornersDistance | `float` |  |
| EdRenderComp | `UNavTestRenderingComponent *` | Editor Preview |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

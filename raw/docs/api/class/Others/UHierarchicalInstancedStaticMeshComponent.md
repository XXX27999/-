# UHierarchicalInstancedStaticMeshComponent

## Parents

- [UInstancedStaticMeshComponent](./UInstancedStaticMeshComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SortedInstances | `TArray < int32 >` |  |
| NumBuiltInstances | `int32` |  |
| BuiltInstanceBounds | [FBox](../../cppstruct/F/FB/FBox.md) |  |
| UnbuiltInstanceBounds | [FBox](../../cppstruct/F/FB/FBox.md) |  |
| UnbuiltInstanceBoundsList | `TArray < FBox >` |  |
| UnbuiltInstanceIndexList | `TArray < int32 >` |  |
| bEnableDensityScaling | `uint32` |  |
| OcclusionLayerNumNodes | `int32` |  |
| CacheMeshExtendedBounds | [FBoxSphereBounds](../../cppstruct/F/FB/FBoxSphereBounds.md) |  |
| bDisableCollision | `bool` |  |
| MinInstancesToSplitNode | `int32` | Culling by Num |
| OptimiMinInstancesToSplitNode | `int32` | Culling by Num For Optimization FClusterTree |
| IsOpenTreeOptimi | `bool` | Mark Use OptimiMinInstancesToSplitNode With FClusterTree |
| InstanceCullDistanceByVolume | `float` | Instance Culling by CullDistanceVolume |
| bEnableScaleOpt | `bool` |  |
| AverageScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |

## Functions

### RemoveInstances

Removes all the instances with indices specified in the InstancesToRemove array. Returns true on success.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InstancesToRemove | `TArray < int32 > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UNavLocalGridManager

Manager for local navigation grids

   Builds non overlapping grid from multiple sources, that can be used later for pathfinding.
   Check also: UGridPathFollowingComponent, FNavLocalGridData

## Parents

- [UObject](./UObject.md)

## Variables

_None_

## Functions

### SetLocalNavigationGridDensity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| CellSize | `float` |  |

**Return**

- Type: 
- Description: _None_

### AddLocalNavigationGridForPoint

creates new grid data for single point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Location | `FVector &` |  |
| Radius2D | `int32` |  |
| Height | `float` |  |
| bRebuildGrids | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddLocalNavigationGridForPoints

creates single grid data for set of points

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Locations | `TArray < FVector > &` |  |
| Radius2D | `int32` |  |
| Height | `float` |  |
| bRebuildGrids | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddLocalNavigationGridForBox

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Location | `FVector &` |  |
| Extent | `FVector` |  |
| Rotation | `FRotator` |  |
| Radius2D | `int32` |  |
| Height | `float` |  |
| bRebuildGrids | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddLocalNavigationGridForCapsule

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Location | `FVector &` |  |
| CapsuleRadius | `float` |  |
| CapsuleHalfHeight | `float` |  |
| Radius2D | `int32` |  |
| Height | `float` |  |
| bRebuildGrids | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RemoveLocalNavigationGrid

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| GridId | `int32` |  |
| bRebuildGrids | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FindLocalNavigationGridPath

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Start | `FVector &` |  |
| End | `FVector &` |  |
| PathPoints | `TArray < FVector > &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

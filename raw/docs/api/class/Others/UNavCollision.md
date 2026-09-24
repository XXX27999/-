# UNavCollision

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CylinderCollision | `TArray < FNavCollisionCylinder >` | list of nav collision cylinders |
| BoxCollision | `TArray < FNavCollisionBox >` | list of nav collision boxes |
| AreaClass | `TSubclassOf < UNavArea >` | navigation area type (empty = default obstacle) |
| bIsDynamicObstacle | `uint32` | If set, mesh will be used as dynamic obstacle (don't create navmesh on top, much faster addingremoving) |
| bGatherConvexGeometry | `uint32` | If set, convex collisions will be exported offline for faster runtime navmesh building (increases memory usage) |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UShapeComponent

ShapeComponent is a PrimitiveComponent that is represented by a simple geometrical shape (sphere, capsule, box, etc).

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ShapeColor | [FColor](../../cppstruct/F/FC/FColor.md) | Color used to draw the shape. |
| ShapeBodySetup | `UBodySetup *` | Description of collision |
| bDrawOnlyIfSelected | `uint8` | Only show this component if the actor is selected |
| bShouldCollideWhenPlacing | `uint8` | If true it allows Collision when placing even if collision is not enabled |
| bDynamicObstacle | `uint8` | If set, shape will be exported for navigation as dynamic modifier instead of using regular collision data |
| AreaClass | `TSubclassOf < UNavArea >` | Navigation area type (empty = default obstacle) |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

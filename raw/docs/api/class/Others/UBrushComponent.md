# UBrushComponent

A brush component defines a shape that can be modified within the editor. They are used both as part of BSP building, and for volumes.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Brush | `UModel *` |  |
| BrushBodySetup | `UBodySetup *` | Description of collision |
| PrePivot_DEPRECATED | [FVector](../../cppstruct/F/FV/FVector.md) | Local space translation |
| MeshCollisionProvider | `UStaticMesh *` |  |

## Functions

### SetMeshCollisionProvider

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Mesh | `UStaticMesh *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# AStaticMeshActor

StaticMeshActor is an instance of a UStaticMesh in the world.
  Static meshes are geometry that do not animate or otherwise deform, and are more efficient to render than other types of geometry.
  Static meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.

  @see UStaticMesh

## Parents

- [AActor](./AActor.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| StaticMeshComponent | `UStaticMeshComponent *` |  |
| bStaticMeshReplicateMovement | `bool` | This static mesh should replicate movement. Automatically sets the RemoteRole and bReplicateMovement flags. Meant to be edited on placed actors (those other two properties are not) |
| NavigationGeometryGatheringMode | [ENavDataGatheringMode](../../cppenum/E/EN/ENavDataGatheringMode.md) |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

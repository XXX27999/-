# ASkeletalMeshActor

SkeletalMeshActor is an instance of a USkeletalMesh in the world.
  Skeletal meshes are deformable meshes that can be animated and change their geometry at run-time.
  Skeletal meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.

  @see USkeletalMesh

## Parents

- [AActor](./AActor.md)
- IMatineeAnimInterface
- IObjectPoolInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bShouldDoAnimNotifies | `uint32` | Whether or not this actor should respond to anim notifies - CURRENTLY ONLY AFFECTS PlayParticleEffect NOTIFIES |
| bWakeOnLevelStart_DEPRECATED | `uint32` |  |
| bSupportObjectPool | `uint32` |  |
| SkeletalMeshComponent | `USkeletalMeshComponent *` |  |
| ReplicatedMesh | `USkeletalMesh *` | Used to replicate mesh to clients |
| ReplicatedPhysAsset | `UPhysicsAsset *` | Used to replicate physics asset to clients |
| ReplicatedMaterial0 | `UMaterialInterface *` | used to replicate the material in index 0 |
| ReplicatedMaterial1 | `UMaterialInterface *` |  |

## Functions

### OnRep_ReplicatedMesh

Replication Notification Callbacks

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedPhysAsset

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedMaterial0

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedMaterial1

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

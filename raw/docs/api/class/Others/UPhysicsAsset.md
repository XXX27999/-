# UPhysicsAsset

PhysicsAsset contains a set of rigid bodies and constraints that make up a single ragdoll.
  The asset is not limited to human ragdolls, and can be used for any physical simulation using bodies and constraints.
  A SkeletalMesh has a single PhysicsAsset, which allows for easily turning ragdoll physics on or off for many SkeletalMeshComponents
  The asset can be configured inside the Physics Asset Editor.

  @see USkeletalMesh

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BoundsBodies | `TArray < int32 >` | Index of bodies that are marked bConsiderForBounds |
| SkeletalBodySetups | `TArray < USkeletalBodySetup * >` | Array of SkeletalBodySetup objects. Stores information about collision shape etc. for each body.<br>		Does not include body position - those are taken from mesh. |
| ConstraintSetup | `TArray < UPhysicsConstraintTemplate * >` | Array of RB_ConstraintSetup objects.<br>	 	Stores information about a joint between two bodies, such as position relative to each body, joint limits etc. |
| bUseAsyncScene | `uint8` | If true, bodies of the physics asset will be put into the asynchronous physics scene. If false, they will be put into the synchronous physics scene. |
| ThumbnailInfo | `UThumbnailInfo *` | Information for thumbnail rendering |
| BodySetup_DEPRECATED | `TArray < UBodySetup * >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

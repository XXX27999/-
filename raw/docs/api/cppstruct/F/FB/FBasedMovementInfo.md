# FBasedMovementInfo

Struct to hold information about the "base" object the character is standing on.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| MovementBaseActor | `AActor *` |  |
| BoneName | `FName` | Bone name on component, for skeletal meshes. NAME_None if not a skeletal mesh or if bone is invalid. |
| Location | `FVector_NetQuantize100` | Location relative to MovementBase. Only valid if HasRelativeLocation() is true. |
| Rotation | [FRotator](../FR/FRotator.md) | Rotation: relative to MovementBase if HasRelativeRotation() is true, absolute otherwise. |
| bServerHasBaseComponent | `bool` | Whether the server says that there is a base. On clients, the component may not have resolved yet. |
| bRelativeRotation | `bool` | Whether rotation is relative to the base or absolute. It can only be relative if location is also relative. |
| bServerHasVelocity | `bool` | Whether there is a velocity on the server. Used for forcing replication when velocity goes to zero. |
| MovementBase | `TWeakObjectPtr < UPrimitiveComponent >` | Component we are based on |

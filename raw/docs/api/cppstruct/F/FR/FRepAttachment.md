# FRepAttachment

Handles attachment replication to clients. Movement replication will not happen while AttachParent is non-nullptr

## Fields

| Name | Type | Description |
| --- | --- | --- |
| AttachParent | `AActor *` |  |
| LocationOffset | `FVector_NetQuantize100` |  |
| RelativeScale3D | `FVector_NetQuantize100` |  |
| RotationOffset | [FRotator](./FRotator.md) |  |
| AttachSocket | `FName` |  |
| AttachComponent | `USceneComponent *` |  |
| AttachParent_Direct | `AActor *` |  |
| bHasValidParent | `bool` |  |

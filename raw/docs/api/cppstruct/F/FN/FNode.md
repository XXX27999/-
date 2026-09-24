# FNode

Rig Controller for bone transform

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Name | `FName` | Name of the original node. We don't allow to change this. This is used for identity. |
| ParentName | `FName` | We save Parent Node but if the parent node is removed, it will reset to root |
| Transform | [FTransform](../FT/FTransform.md) | Absolute transform of the node. Hoping to use this data in the future to render |
| DisplayName | `FString` | This is Display Name where it will be used to display in Retarget Manager. This name has to be unique. |
| bAdvanced | `bool` |  |

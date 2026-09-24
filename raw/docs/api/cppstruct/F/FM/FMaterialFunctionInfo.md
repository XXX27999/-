# FMaterialFunctionInfo

Stores information about a function that this material references, used to know when the material needs to be recompiled.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| StateId | [FGuid](../FG/FGuid.md) | Id that the function had when this material was last compiled. |
| Function | `UMaterialFunction *` | The function which this material has a dependency on. |

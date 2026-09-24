# FMaterialParameterCollectionInfo

Stores information about a parameter collection that this material references, used to know when the material needs to be recompiled.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| StateId | [FGuid](../FG/FGuid.md) | Id that the collection had when this material was last compiled. |
| ParameterCollection | `UMaterialParameterCollection *` | The collection which this material has a dependency on. |

# FCollectionParameterBase

Base struct for collection parameters

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` | The name of the parameter.  Changing this name will break any blueprints that reference the parameter. |
| Id | [FGuid](../FG/FGuid.md) | Uniquely identifies the parameter, used for fixing up materials that reference this parameter when renaming. |

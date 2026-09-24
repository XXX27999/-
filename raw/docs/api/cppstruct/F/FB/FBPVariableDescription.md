# FBPVariableDescription

Struct indicating a variable in the generated class

## Fields

| Name | Type | Description |
| --- | --- | --- |
| VarName | `FName` | Name of the variable |
| VarGuid | [FGuid](../FG/FGuid.md) | A Guid that will remain constant even if the VarName changes |
| VarType | [FEdGraphPinType](../FE/FEdGraphPinType.md) | Type of the variable |
| FriendlyName | `FString` | Friendly name of the variable |
| Category | `FText` | Category this variable should be in |
| PropertyFlags | `uint64` | Property flags for this variable - Changed from int32 to uint64 |
| RepNotifyFunc | `FName` |  |
| ReplicationCondition | `TEnumAsByte < ELifetimeCondition >` |  |
| MetaDataArray | `TArray < struct FBPVariableMetaDataEntry >` | Metadata information for this variable |
| DefaultValue | `FString` | Optional new default value stored as string |

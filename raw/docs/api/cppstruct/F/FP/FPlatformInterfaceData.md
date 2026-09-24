# FPlatformInterfaceData

Struct that encompasses the most common types of data. This is the data payload
  of PlatformInterfaceDelegateResult.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| DataName | `FName` | An optional tag for this data |
| Type | `TEnumAsByte < enum EPlatformInterfaceDataType >` | Specifies which value is valid for this structure |
| IntValue | `int32` | Various typed result values |
| FloatValue | `float` |  |
| StringValue | `FString` |  |
| ObjectValue | `UObject *` |  |

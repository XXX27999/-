# FExpressionInput

## Fields

| Name | Type | Description |
| --- | --- | --- |
| OutputIndex | `int32` | Index into Expression's outputs array that this input is connected to. |
| InputName | `FString` | optional FName of the input.<br>	  Note that this is the only member which is not derived from the output currently connected. |
| Mask | `int32` |  |
| MaskR | `int32` |  |
| MaskG | `int32` |  |
| MaskB | `int32` |  |
| MaskA | `int32` |  |
| ExpressionName | `FName` | Material expression name that this input is connected to, or None if not connected. Used only in cooked builds |
| Expression | `UMaterialExpression *` | UMaterial expression that this input is connected to, or NULL if not connected. |

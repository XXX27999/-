# FDelegateRuntimeBinding

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ObjectName | `FString` | The widget that will be bound to the live data. |
| PropertyName | `FName` | The property on the widget that will have a binding placed on it. |
| FunctionName | `FName` | The function or property we're binding to on the source object. |
| SourcePath | [FDynamicPropertyPath](./FDynamicPropertyPath.md) |  |
| Kind | [EBindingKind](../../../cppenum/E/EB/EBindingKind.md) | The kind of binding we're performing, are we binding to a property or a function. |

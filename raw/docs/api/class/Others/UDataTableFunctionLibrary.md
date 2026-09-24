# UDataTableFunctionLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### EvaluateCurveTableRow

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CurveTable | `UCurveTable *` |  |
| RowName | `FName` |  |
| InXY | `float` |  |
| OutResult | `TEnumAsByte < EEvaluateCurveTableResult :: Type > &` |  |
| OutXY | `float &` |  |
| ContextString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetDataTableRowNames

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Table | `UDataTable *` |  |
| OutRowNames | `TArray < FName > &` |  |

**Return**

- Type: 
- Description: _None_

### GetDataTableRowFromName

Get a Row from a DataTable given a RowName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Table | `UDataTable *` |  |
| RowName | `FName` |  |
| OutRow | `FTableRowBase &` |  |

**Return**

- Type: 
- Description: _None_

### FillDataTableFromCSVString

Empty and fill a Data Table from CSV string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DataTable | `UDataTable *` |  |
| CSVString | `FString &` | The Data that representing the contents of a CSV file. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

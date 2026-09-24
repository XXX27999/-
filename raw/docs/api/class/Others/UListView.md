# UListView

Allows thousands of items to be displayed in a list.  Generates widgets dynamically for each item.

## Parents

- UTableViewBase

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ItemHeight | `float` | The height of each widget |
| Items | `TArray < UObject * >` | The list of items to generate widgets for |
| SelectionMode | `TEnumAsByte < ESelectionMode :: Type >` | The selection method for the list |
| OnGenerateRowEvent | `FOnGenerateRowUObject` | Called when a widget needs to be generated |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

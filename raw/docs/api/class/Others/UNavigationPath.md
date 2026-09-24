# UNavigationPath

UObject wrapper for FNavigationPath

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PathPoints | `TArray < FVector >` |  |
| RecalculateOnInvalidation | `TEnumAsByte < ENavigationOptionFlag :: Type >` |  |

## Functions

### GetDebugString

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableDebugDrawing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bShouldDrawDebugData | `bool` |  |
| PathColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### EnableRecalculationOnInvalidation

if enabled path will request recalculation if it gets invalidated due to a change to underlying navigation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DoRecalculation | `TEnumAsByte < ENavigationOptionFlag :: Type >` |  |

**Return**

- Type: 
- Description: _None_

### GetPathLength

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPathCost

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPartial

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsValid

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsStringPulled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| PathUpdatedNotifier |  |  |

## Language

cpp

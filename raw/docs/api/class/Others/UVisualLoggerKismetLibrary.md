# UVisualLoggerKismetLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### LogText

Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Text | `FString` |  |
| LogCategory | `FName` |  |

**Return**

- Type: 
- Description: _None_

### LogLocation

Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Location | `FVector` |  |
| Text | `FString` |  |
| ObjectColor | `FLinearColor` |  |
| Radius | `float` |  |
| LogCategory | `FName` |  |

**Return**

- Type: 
- Description: _None_

### LogBox

Logs box shape - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| BoxShape | `FBox` |  |
| Text | `FString` |  |
| ObjectColor | `FLinearColor` |  |
| LogCategory | `FName` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

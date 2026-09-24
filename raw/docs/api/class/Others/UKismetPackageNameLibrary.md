# UKismetPackageNameLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### IsValidLongPackageName

Helper function for converting short to long script package name (InputCore -> ScriptInputCore)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLongPackageName | `FString &` | Long Package Name |
| bIncludeReadOnlyRoots | `bool` | If true, will include roots that you should not save to. (Temp, Script) |
| OutReason | `FText &` | When returning false, this will provide a description of what was wrong with the name. |

**Return**

- Type: 
- Description: _None_

### IsValidObjectPath

Returns true if the path starts with a valid root (i.e. Game, Engine, etc) and contains no illegal characters.
	  This validates that the packagename is valid, and also makes sure the object after package name is also correct.
	  This will return false if passed a path starting with Classname'

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObjectPath | `FString &` | The object path to test |
| OutReason | `FText &` | When returning false, this will provide a description of what was wrong with the name. |

**Return**

- Type: 
- Description: _None_

### DoesPackageExist

Checks if the given string is a long package name or not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LongPackageName | `FString &` | Package name. |
| Guid | `FGuid &` |  |
| OutFilename | `FString &` | Package filename on disk. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

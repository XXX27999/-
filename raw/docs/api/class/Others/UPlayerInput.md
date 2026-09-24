# UPlayerInput

end: 单条记录，滑屏轨迹中的一个点

  Object within PlayerController that processes player input.
  Only exists on the client in network games.

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bEnableKeyInput | `bool` |  |
| InputTouchCacheDataList | `TArray < FInputTouchCacheData >` |  |
| DebugExecBindings | `TArray < struct FKeyBind >` | Generic bindings of keys to Exec()-compatible strings for development purposes only |
| InvertedAxis | `TArray < FName >` | List of Axis Mappings that have been inverted |

## Functions

### SetMouseSensitivity

Exec function to change the mouse sensitivity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Sensitivity | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetBind

Exec function to add a debug exec command

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BindName | `FName` |  |
| Command | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### InvertAxisKey

Exec function to invert an axis key

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AxisKey | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### InvertAxis

Exec function to invert an axis mapping

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AxisName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ClearSmoothing

Exec function to reset mouse smoothing values

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

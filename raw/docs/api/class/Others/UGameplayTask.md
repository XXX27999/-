# UGameplayTask

## Parents

- [UObject](./UObject.md)
- IGameplayTaskOwnerInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InstanceName | `FName` | This name allows us to find the task later so that we can end it. |
| ResourceOverlapPolicy | [ETaskResourceOverlapPolicy](../../cppenum/E/ET/ETaskResourceOverlapPolicy.md) |  |
| ChildTask | `UGameplayTask *` | child task instance |

## Functions

### ReadyForActivation

Called to trigger the actual task once the delegates have been set up

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EndTask

Called explicitly to end the task (usually by the task itself). Calls OnDestroy.

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

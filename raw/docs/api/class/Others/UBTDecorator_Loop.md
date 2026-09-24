# UBTDecorator_Loop

Loop decorator node.
  A decorator node that bases its condition on whether its loop counter has been exceeded.

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NumLoops | `int32` | number of executions |
| bInfiniteLoop | `bool` | infinite loop |
| InfiniteLoopTimeoutTime | `float` | timeout (when looping infinitely, when we finish a loop we will check whether we have spent this time looping, if we have we will stop looping). A negative value means loop forever. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

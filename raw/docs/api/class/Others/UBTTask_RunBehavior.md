# UBTTask_RunBehavior

RunBehavior task allows pushing subtrees on execution stack.
  Subtree asset can't be changed in runtime!

  This limitation is caused by support for subtree's root level decorators,
  which are injected into parent tree, and structure of running tree
  cannot be modified in runtime (see: BTNode: ExecutionIndex, MemoryOffset)

  Use RunBehaviorDynamic task for subtrees that need to be changed in runtime.

## Parents

- [UBTTaskNode](./UBTTaskNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BehaviorAsset | `UBehaviorTree *` | behavior to run |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

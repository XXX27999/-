# UBTTaskNode

Task are leaf nodes of behavior tree, which perform actual actions

  Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
   - ExecuteTask
   - AbortTask
   - TickTask
   - OnMessage

  If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
  Template nodes are shared across all behavior tree components using the same tree asset and must store
  their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## Parents

- [UBTNode](./UBTNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Services | `TArray < UBTService * >` | service nodes |
| bIgnoreRestartSelf | `uint32` | if set, task search will be discarded when this task is selected to execute but is already running |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

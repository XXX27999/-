# UBTTask_GameplayTaskBase

Base class for managing gameplay tasks
  Since AITask doesn't have any kind of successfailed results, default implemenation will only return EBTNode::Succeeded

  In your ExecuteTask:
  - use NewBTAITask() helper to create task
  - initialize task with values if needed
  - use StartGameplayTask() helper to execute and get node result

## Parents

- [UBTTaskNode](./UBTTaskNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bWaitForGameplayTask | `uint32` | if set, behavior tree task will wait until gameplay tasks finishes |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

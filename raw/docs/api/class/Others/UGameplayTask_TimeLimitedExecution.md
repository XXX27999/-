# UGameplayTask_TimeLimitedExecution

Adds time limit for running a child task
  - child task needs to be created with UGameplayTask_TimeLimitedExecution passed as TaskOwner
  - activations are tied together and when either UGameplayTask_TimeLimitedExecution or child task is activated, other one starts as well
  - OnFinished and OnTimeExpired are mutually exclusive

## Parents

- [UGameplayTask](./UGameplayTask.md)

## Variables

_None_

## Functions

_None_

## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnFinished |  | called when child task finishes execution before time runs out |
| OnTimeExpired |  | called when time runs out |

## Language

cpp

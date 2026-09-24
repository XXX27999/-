# UBTTask_SetTagCooldown

Cooldown task node.
  Sets a cooldown tag value.  Use with cooldown tag decorators to prevent behavior tree execution.

## Parents

- [UBTTaskNode](./UBTTaskNode.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CooldownTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | Gameplay tag that will be used for the cooldown. |
| bAddToExistingDuration | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |
| CooldownDuration | `float` | Value we will add or set to the Cooldown tag when this task runs. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UBTDecorator_TagCooldown

Cooldown decorator node.
  A decorator node that bases its condition on whether a cooldown timer based on a gameplay tag has expired.

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CooldownTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | Gameplay tag that will be used for the cooldown. |
| CooldownDuration | `float` | Value we will add or set to the Cooldown tag when this node is deactivated. |
| bAddToExistingDuration | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |
| bActivatesCooldown | `bool` | Whether or not we are addingsetting to the cooldown tag's value when the decorator deactivates. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

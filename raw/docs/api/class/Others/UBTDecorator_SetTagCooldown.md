# UBTDecorator_SetTagCooldown

Set tag cooldown decorator node.
  A decorator node that sets a gameplay tag cooldown.

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CooldownTag | [FGameplayTag](../../cppstruct/F/FG/FGameplayTag.md) | Gameplay tag that will be used for the cooldown. |
| CooldownDuration | `float` | Value we will add or set to the Cooldown tag when this task runs. |
| bAddToExistingDuration | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

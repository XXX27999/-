# UBTDecorator_ConeCheck

Cone check decorator node.
  A decorator node that bases its condition on a cone check, using Blackboard entries to form the parameters of the check.

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ConeHalfAngle | `float` | Angle between cone direction and code cone edge, or a half of the total cone angle |
| ConeOrigin | `FBlackboardKeySelector` | blackboard key selector |
| ConeDirection | `FBlackboardKeySelector` | "None" means "use ConeOrigin's direction" |
| Observed | `FBlackboardKeySelector` | blackboard key selector |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

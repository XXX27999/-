# UBTDecorator_KeepInCone

Cooldown decorator node.
  A decorator node that bases its condition on whether the observed position is still inside a cone. The cone's direction is calculated when the node first becomes relevant.

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ConeHalfAngle | `float` | max allowed time for execution of underlying node |
| ConeOrigin | `FBlackboardKeySelector` | blackboard key selector |
| Observed | `FBlackboardKeySelector` | blackboard key selector |
| bUseSelfAsOrigin | `uint32` |  |
| bUseSelfAsObserved | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

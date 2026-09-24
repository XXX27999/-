# UBTDecorator_DoesPathExist

Cooldown decorator node.
  A decorator node that bases its condition on whether a path exists between two points from the Blackboard.

## Parents

- [UBTDecorator](./UBTDecorator.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| BlackboardKeyA | `FBlackboardKeySelector` | blackboard key selector |
| BlackboardKeyB | `FBlackboardKeySelector` | blackboard key selector |
| bUseSelf | `uint32` |  |
| PathQueryType | `TEnumAsByte < EPathExistanceQueryType :: Type >` |  |
| FilterClass | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

# UBTDecorator_IsAtLocation

Is At Location decorator node.
  A decorator node that checks if AI controlled pawn is at given location.

## Parents

- [UBTDecorator_BlackboardBase](./UBTDecorator_BlackboardBase.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AcceptableRadius | `float` | distance threshold to accept as being at location |
| ParametrizedAcceptableRadius | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) |  |
| GeometricDistanceType | [FAIDistanceType](../../cppenum/F/FA/FAIDistanceType.md) |  |
| bUseParametrizedRadius | `uint32` |  |
| bUseNavAgentGoalLocation | `uint32` | if moving to an actor and this actor is a nav agent, then we will move to their nav agent location |
| bPathFindingBasedTest | `uint32` | If true the result will be consistent with tests done while following paths.<br>	 	Set to false to use geometric distance as configured with DistanceType |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

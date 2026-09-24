# UEnvQueryGenerator_OnCircle

## Parents

- [UEnvQueryGenerator_ProjectedPoints](./UEnvQueryGenerator_ProjectedPoints.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CircleRadius | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | max distance of path between point and context |
| SpaceBetween | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | items will be generated on a circle this much apart |
| NumberOfPoints | [FAIDataProviderIntValue](../../cppstruct/F/FA/FAIDataProviderIntValue.md) | this many items will be generated on a circle |
| PointOnCircleSpacingMethod | [EPointOnCircleSpacingMethod](../../cppenum/E/EP/EPointOnCircleSpacingMethod.md) | how we are choosing where the points are in the circle |
| ArcDirection | `FEnvDirection` | If you generate items on a piece of circle you define direction of Arc cut here |
| ArcAngle | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | If you generate items on a piece of circle you define angle of Arc cut here |
| AngleRadians | `float` |  |
| CircleCenter | `TSubclassOf < UEnvQueryContext >` | context |
| bIgnoreAnyContextActorsWhenGeneratingCircle | `bool` | ignore tracing into context actors when generating the circle |
| CircleCenterZOffset | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | context offset |
| TraceData | `FEnvTraceData` | horizontal trace for nearest obstacle |
| bDefineArc | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

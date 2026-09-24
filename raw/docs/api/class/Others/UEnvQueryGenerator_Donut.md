# UEnvQueryGenerator_Donut

## Parents

- [UEnvQueryGenerator_ProjectedPoints](./UEnvQueryGenerator_ProjectedPoints.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InnerRadius | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | min distance between point and context |
| OuterRadius | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | max distance between point and context |
| NumberOfRings | [FAIDataProviderIntValue](../../cppstruct/F/FA/FAIDataProviderIntValue.md) | number of rings to generate |
| PointsPerRing | [FAIDataProviderIntValue](../../cppstruct/F/FA/FAIDataProviderIntValue.md) | number of items to generate for each ring |
| ArcDirection | `FEnvDirection` | If you generate items on a piece of circle you define direction of Arc cut here |
| ArcAngle | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | If you generate items on a piece of circle you define angle of Arc cut here |
| bUseSpiralPattern | `bool` | If true, the rings of the wheel will be rotated in a spiral pattern.  If false, they will all be at a zero<br>	   rotation, looking more like the spokes on a wheel. |
| Center | `TSubclassOf < UEnvQueryContext >` | context |
| bDefineArc | `uint32` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

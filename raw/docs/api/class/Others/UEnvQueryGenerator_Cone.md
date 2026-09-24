# UEnvQueryGenerator_Cone

## Parents

- [UEnvQueryGenerator_ProjectedPoints](./UEnvQueryGenerator_ProjectedPoints.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AlignedPointsDistance | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Distance between each point of the same angle |
| ConeDegrees | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Maximum degrees of the generated cone |
| AngleStep | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | The step of the angle increase. Angle step must be >=1<br>	   Smaller values generate less items |
| Range | [FAIDataProviderFloatValue](../../cppstruct/F/FA/FAIDataProviderFloatValue.md) | Generation distance |
| CenterActor | `TSubclassOf < UEnvQueryContext >` | The actor (or actors) that will generate a cone in their facing direction |
| bIncludeContextLocation | `uint8` | Whether to include CenterActors' locations when generating items.<br>	 	Note that this option skips the MinAngledPointsDistance parameter. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

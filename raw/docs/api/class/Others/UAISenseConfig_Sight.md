# UAISenseConfig_Sight

## Parents

- [UAISenseConfig](./UAISenseConfig.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Implementation | `TSubclassOf < UAISense_Sight >` |  |
| SightRadius | `float` | Maximum sight distance to notice a target. |
| LoseSightRadius | `float` | Maximum sight distance to see target that has been already seen. |
| PeripheralVisionAngleDegrees | `float` | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime.<br>	 	The value represents the angle measured in relation to the forward vector, not the whole range. |
| DetectionByAffiliation | [FAISenseAffiliationFilter](../../cppstruct/F/FA/FAISenseAffiliationFilter.md) |  |
| AutoSuccessRangeFromLastSeenLocation | `float` | If not an InvalidRange (which is the default), we will always be able to see the target that has already been seen if they are within this range of their last seen location. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

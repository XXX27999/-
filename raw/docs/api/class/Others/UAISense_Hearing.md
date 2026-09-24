# UAISense_Hearing

## Parents

- [UAISense](./UAISense.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| NoiseEvents | `TArray < FAINoiseEvent >` |  |
| SpeedOfSoundSq | `float` | Defaults to 0 to have instant notification. Setting to > 0 will result in delaying<br>	 	when AI hears the sound based on the distance from the source |

## Functions

### ReportNoiseEvent

Report a noise event.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| NoiseLocation | `FVector` | Location of the noise. |
| Loudness | `float` | Loudness of the noise. If MaxRange is non-zero, modifies MaxRange, otherwise modifies the squared distance of the sensor's range. |
| Instigator | `AActor *` | Actor that triggered the noise. |
| MaxRange | `float` | Max range at which the sound can be heard, multiplied by Loudness. Values <= 0 mean no limit (still limited by listener's range however). |
| Tag | `FName` | Identifier for the event. |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

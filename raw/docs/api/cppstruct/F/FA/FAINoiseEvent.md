# FAINoiseEvent

## Fields

| Name | Type | Description |
| --- | --- | --- |
| NoiseLocation | [FVector](../FV/FVector.md) | if not set Instigator's location will be used |
| Loudness | `float` | Loudness modifier of the sound.<br>	  If MaxRange is non-zero, this modifies the range (by multiplication).<br>	  If there is no MaxRange, then if Square(DistanceToSound) <= Square(HearingRange)  Loudness, the sound is heard, false otherwise. |
| MaxRange | `float` | Max range at which the sound can be heard. Multiplied by Loudness.<br>	  A value of 0 indicates that there is no range limit, though listeners are still limited by their own hearing range. |
| Instigator | `AActor *` | Actor triggering the sound. |
| Tag | `FName` | Named identifier for the noise. |

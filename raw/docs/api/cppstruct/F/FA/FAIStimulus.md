# FAIStimulus

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Age | `float` |  |
| ExpirationAge | `float` |  |
| Strength | `float` |  |
| StimulusLocation | [FVector](../FV/FVector.md) |  |
| ReceiverLocation | [FVector](../FV/FVector.md) |  |
| Tag | `FName` |  |
| bSuccessfullySensed | `uint32` |  |
| bExpired | `uint32` | this means the stimulus was originally created with a "time limit" and this time has passed.<br>	 	Expiration also results in calling MarkNoLongerSensed |

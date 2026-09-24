# FAudioComponentParam

Struct used for storing one per-instance named parameter for this AudioComponent.
 	Certain nodes in the SoundCue may reference parameters by name so they can be adjusted per-instance.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ParamName | `FName` |  |
| FloatParam | `float` |  |
| BoolParam | `bool` |  |
| IntParam | `int32` |  |
| SoundWaveParam | `USoundWave *` |  |

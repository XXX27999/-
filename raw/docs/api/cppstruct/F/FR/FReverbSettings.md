# FReverbSettings

Struct encapsulating settings for reverb effects.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bApplyReverb | `uint32` | Whether to apply the reverb settings below. |
| ReverbType_DEPRECATED | `TEnumAsByte < enum ReverbPreset >` | The reverb preset to employ. |
| ReverbEffect | `UReverbEffect *` | The reverb asset to employ. |
| Volume | `float` | Volume level of the reverb affect. |
| FadeTime | `float` | Time to fade from the current reverb settings into this setting, in seconds. |

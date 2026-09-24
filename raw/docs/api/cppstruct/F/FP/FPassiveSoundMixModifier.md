# FPassiveSoundMixModifier

Structure containing information on a SoundMix to activate passively.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SoundMix | `USoundMix *` | The SoundMix to activate |
| MinVolumeThreshold | `float` | Minimum volume level required to activate SoundMix. Below this value the SoundMix will not be active. |
| MaxVolumeThreshold | `float` | Maximum volume level required to activate SoundMix. Above this value the SoundMix will not be active. |

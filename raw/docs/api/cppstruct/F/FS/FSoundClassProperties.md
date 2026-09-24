# FSoundClassProperties

Structure containing configurable properties of a sound class.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Volume | `float` | Volume multiplier. |
| Pitch | `float` | Pitch multiplier. |
| StereoBleed | `float` | The amount of stereo sounds to bleed to the rear speakers |
| LFEBleed | `float` | The amount of a sound to bleed to the LFE channel |
| VoiceCenterChannelVolume | `float` | Voice center channel volume - Not a multiplier (no propagation) |
| RadioFilterVolume | `float` | Volume of the radio filter effect |
| RadioFilterVolumeThreshold | `float` | Volume at which the radio filter kicks in |
| bApplyEffects | `uint32` | Sound mix voice - whether to apply audio effects |
| bAlwaysPlay | `uint32` | Whether to artificially prioritise the component to play |
| bIsUISound | `uint32` | Whether or not this sound plays when the game is paused in the UI |
| bIsMusic | `uint32` | Whether or not this is music (propagates only if parent is true) |
| bReverb | `uint32` | Whether or not this sound class has reverb applied |
| Default2DReverbSendAmount | `float` | Amount of audio to send to master reverb effect for 2D sounds played with this sound class. |
| bCenterChannelOnly | `uint32` | Whether or not this sound class forces sounds to the center channel |
| bApplyAmbientVolumes | `uint32` | Whether the InteriorExterior volume and LPF modifiers should be applied |
| OutputTarget | `TEnumAsByte < EAudioOutputTarget :: Type >` | Which output target the sound should be played through |

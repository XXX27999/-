# FSoundAttenuationSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bAttenuate | `uint32` | Allows distance-based volume attenuation. |
| bSpatialize | `uint32` | Allows the source to be 3D spatialized. |
| bAttenuateWithLPF | `uint32` | Allows simulation of air absorption by applying a filter with a cutoff frequency as a function of distance. |
| bEnableListenerFocus | `uint32` | Enable listener focus-based adjustments. |
| bEnableFocusInterpolation | `uint32` | Enables focus interpolation to smooth transition in and and of focus. |
| bEnableOcclusion | `uint32` | Enables realtime occlusion tracing. |
| bUseComplexCollisionForOcclusion | `uint32` | Enables tracing against complex collision when doing occlusion traces. |
| bEnableReverbSend | `uint32` | Enables adjusting reverb sends based on distance. |
| bApplyNormalizationToStereoSounds | `uint32` | Enables applying a -6 dB attenuation to stereo assets which are 3d spatialized. Avoids clipping when assets have spread of 0.0 due to channel summing. |
| bEnableLogFrequencyScaling | `uint32` | Enables applying a log scale to frequency values (so frequency sweeping is perceptually linear). |
| DistanceType_DEPRECATED | `TEnumAsByte < enum ESoundDistanceCalc >` |  |
| OmniRadius | `float` | The distance below which a sound is non-spatialized (2D). This prevents near-field audio from flipping as audio crosses the listener's position. |
| StereoSpread | `float` | The world-space absolution distance between left and right stereo channels when stereo assets are 3D spatialized. |
| SpatializationAlgorithm | `TEnumAsByte < enum ESoundSpatializationAlgorithm >` | What method we use to spatialize the sound. |
| SpatializationPluginSettings | `USpatializationPluginSourceSettingsBase *` | Settings to use with occlusion audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. |
| RadiusMin_DEPRECATED | `float` |  |
| RadiusMax_DEPRECATED | `float` |  |
| LPFRadiusMin | `float` | The distance min range at which to apply an absorption LPF filter. |
| LPFRadiusMax | `float` | The max distance range at which to apply an absorption LPF filter. Absorption freq cutoff interpolates between filter frequency ranges between these distance values. |
| AbsorptionMethod | [EAirAbsorptionMethod](../../../cppenum/E/EA/EAirAbsorptionMethod.md) | What method to use to map distance values to frequency absorption values. |
| CustomLowpassAirAbsorptionCurve | [FRuntimeFloatCurve](../FR/FRuntimeFloatCurve.md) | The normalized custom curve to use for the air absorption lowpass frequency values. Does a mapping from defined distance values (x-axis) and defined frequency values (y-axis) |
| CustomHighpassAirAbsorptionCurve | [FRuntimeFloatCurve](../FR/FRuntimeFloatCurve.md) | The normalized custom curve to use for the air absorption highpass frequency values. Does a mapping from defined distance values (x-axis) and defined frequency values (y-axis) |
| LPFFrequencyAtMin | `float` | The range of the cutoff frequency (in hz) of the lowpass absorption filter. |
| LPFFrequencyAtMax | `float` | The range of the cutoff frequency (in hz) of the lowpass absorption filter. |
| HPFFrequencyAtMin | `float` | The range of the cutoff frequency (in hz) of the highpass absorption filter. |
| HPFFrequencyAtMax | `float` | The range of the cutoff frequency (in hz) of the highpass absorption filter. |
| FocusAzimuth | `float` | Azimuth angle (in degrees) relative to the listener forward vector which defines the focus region of sounds. Sounds playing at an angle less than this will be in focus. |
| NonFocusAzimuth | `float` | Azimuth angle (in degrees) relative to the listener forward vector which defines the non-focus region of sounds. Sounds playing at an angle greater than this will be out of focus. |
| FocusDistanceScale | `float` | Amount to scale the distance calculation of sounds that are in-focus. Can be used to make in-focus sounds appear to be closer or further away than they actually are. |
| NonFocusDistanceScale | `float` | Amount to scale the distance calculation of sounds that are not in-focus. Can be used to make in-focus sounds appear to be closer or further away than they actually are. |
| FocusPriorityScale | `float` | Amount to scale the priority of sounds that are in focus. Can be used to boost the priority of sounds that are in focus. |
| NonFocusPriorityScale | `float` | Amount to scale the priority of sounds that are not in-focus. Can be used to reduce the priority of sounds that are not in focus. |
| FocusVolumeAttenuation | `float` | Amount to attenuate sounds that are in focus. Can be overridden at the sound-level. |
| NonFocusVolumeAttenuation | `float` | Amount to attenuate sounds that are not in focus. Can be overridden at the sound-level. |
| FocusAttackInterpSpeed | `float` | Scalar used to increase interpolation speed upwards to the target Focus value |
| FocusReleaseInterpSpeed | `float` | Scalar used to increase interpolation speed downwards to the target Focus value |
| OcclusionTraceChannel | `TEnumAsByte < enum ECollisionChannel >` | Which trace channel to use for audio occlusion checks. |
| OcclusionLowPassFilterFrequency | `float` | The low pass filter frequency (in hertz) to apply if the sound playing in this audio component is occluded. This will override the frequency set in LowPassFilterFrequency. A frequency of 0.0 is the device sample rate and will bypass the filter. |
| OcclusionVolumeAttenuation | `float` | The amount of volume attenuation to apply to sounds which are occluded. |
| OcclusionInterpolationTime | `float` | The amount of time in seconds to interpolate to the target OcclusionLowPassFilterFrequency when a sound is occluded. |
| OcclusionPluginSettings | `UOcclusionPluginSourceSettingsBase *` | Settings to use with occlusion audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. |
| ReverbSendMethod | [EReverbSendMethod](../../../cppenum/E/ER/EReverbSendMethod.md) | What method to use to control master reverb sends |
| ReverbPluginSettings | `UReverbPluginSourceSettingsBase *` | Settings to use with reverb audio plugin. These are defined by the plugin creator. Not all audio plugins utilize this feature. |
| ReverbWetLevelMin | `float` | The amount to send to master reverb when sound is located at a distance equal to value specified in the reverb min send distance. |
| ReverbWetLevelMax | `float` | The amount to send to master reverb when sound is located at a distance equal to value specified in the reverb max send distance. |
| ReverbDistanceMin | `float` | The min distance to send to the master reverb. |
| ReverbDistanceMax | `float` | The max distance to send to the master reverb. |
| CustomReverbSendCurve | [FRuntimeFloatCurve](../FR/FRuntimeFloatCurve.md) | The custom reverb send curve to use for distance-based send level. |
| ManualReverbSendLevel | `float` | The manual master reverb send level to use. Doesn't change as a function of distance. |

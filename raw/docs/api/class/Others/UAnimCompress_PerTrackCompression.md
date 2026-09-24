# UAnimCompress_PerTrackCompression

## Parents

- [UAnimCompress_RemoveLinearKeys](./UAnimCompress_RemoveLinearKeys.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxZeroingThreshold | `float` | Maximum threshold to use when replacing a component with zero. Lower values retain more keys, but yield less compression. |
| MaxPosDiffBitwise | `float` | Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| MaxAngleDiffBitwise | `float` | Maximum angle difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| MaxScaleDiffBitwise | `float` | Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| AllowedRotationFormats | `TArray < TEnumAsByte < enum AnimationCompressionFormat > >` | Which encoding formats is the per-track compressor allowed to try on rotation keys |
| AllowedTranslationFormats | `TArray < TEnumAsByte < enum AnimationCompressionFormat > >` | Which encoding formats is the per-track compressor allowed to try on translation keys |
| AllowedScaleFormats | `TArray < TEnumAsByte < enum AnimationCompressionFormat > >` | Which encoding formats is the per-track compressor allowed to try on scale keys |
| bResampleAnimation | `uint32` | If true, resample the animation to ResampleFramerate frames per second |
| ResampledFramerate | `float` | When bResampleAnimation is true, this defines the desired framerate |
| MinKeysForResampling | `int32` | Animations with fewer keys than MinKeysForResampling will not be resampled. |
| bUseAdaptiveError | `uint32` | If true, adjust the error thresholds based on the 'height' within the skeleton |
| bUseOverrideForEndEffectors | `uint32` | If true, uses MinEffectorDiff as the threhsold for end effectors |
| TrackHeightBias | `int32` | A bias added to the track height before using it to calculate the adaptive error |
| ParentingDivisor | `float` | Reduces the error tolerance the further up the tree that a key occurs<br>	  EffectiveErrorTolerance = Max(BaseErrorTolerance  Power(ParentingDivisor, Max(Height+Bias,0)  ParentingDivisorExponent), ZeroingThreshold)<br>	  Only has an effect bUseAdaptiveError is true |
| ParentingDivisorExponent | `float` | Reduces the error tolerance the further up the tree that a key occurs<br>	  EffectiveErrorTolerance = Max(BaseErrorTolerance  Power(ParentingDivisor, Max(Height+Bias,0)  ParentingDivisorExponent), ZeroingThreshold)<br>	  Only has an effect bUseAdaptiveError is true |
| bUseAdaptiveError2 | `uint32` | If true, the adaptive error system will determine how much error to allow for each track, based on the<br>	  error introduced in end effectors due to errors in the track. |
| RotationErrorSourceRatio | `float` | This ratio determines how much error in end effector rotation can come from a given track's rotation error or translation error.<br>	  If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from translation error. |
| TranslationErrorSourceRatio | `float` | This ratio determines how much error in end effector translation can come from a given track's rotation error or translation error.<br>	  If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from translation error. |
| ScaleErrorSourceRatio | `float` | This ratio determines how much error in end effector scale can come from a given track's rotation error or scale error.<br>	  If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from scale error. |
| MaxErrorPerTrackRatio | `float` | A fraction that determines how much of the total error budget can be introduced by any particular track |
| PerturbationProbeSize | `float` | How big of a perturbation should be made when probing error propagation |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

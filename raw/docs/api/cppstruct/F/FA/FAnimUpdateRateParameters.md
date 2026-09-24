# FAnimUpdateRateParameters

Container for Animation Update Rate parameters.
  They are shared for all components of an Actor, so they can be updated in sync.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| UpdateRate | `int32` | How often animation will be updatedticked. 1 = every frame, 2 = every 2 frames, etc. |
| EvaluationRate | `int32` | How often animation will be evaluated. 1 = every frame, 2 = every 2 frames, etc.<br>	   has to be a multiple of UpdateRate. |
| bInterpolateSkippedFrames | `uint32` | When skipping a frame, should it be interpolated or frozen? |
| bShouldUseLodMap | `uint32` | Whether or not to use the defined LODFrameskip map instead of separate distance factor thresholds |
| bShouldUseMinLod | `uint32` | If set, LODFrameskip map will be queried with mesh's MinLodModel instead of current LOD (PredictedLODLevel) |
| bSkipUpdate | `uint32` | (This frame) animation update should be skipped. |
| bSkipEvaluation | `uint32` | (This frame) animation evaluation should be skipped. |
| TickedPoseOffestTime | `float` | Track time we have lost via skipping |
| AdditionalTime | `float` | Total time of the last series of skipped updates |
| BaseNonRenderedUpdateRate | `int32` | Rate of animation evaluation when non rendered (off screen and dedicated servers).<br>	  a value of 4 means evaluated 1 frame, then 3 frames skipped |
| BaseNonRenderedUpdateRateHigh | `int32` |  |
| MaxDistFromMainChar | `float` |  |
| BaseVisibleDistanceFactorThesholds | `TArray < float >` | Array of MaxDistanceFactor to use for AnimUpdateRate when mesh is visible (rendered).<br>	  MaxDistanceFactor is size on screen, as used by LODs<br>	  Example:<br>	 		BaseVisibleDistanceFactorThesholds.Add(0.4f)<br>	 		BaseVisibleDistanceFactorThesholds.Add(0.2f)<br>	  means:<br>	 		0 frame skip, MaxDistanceFactor > 0.4f<br>	 		1 frame skip, MaxDistanceFactor > 0.2f<br>	 		2 frame skip, MaxDistanceFactor > 0.0f |
| BaseVisibleDistanceFactorSkipNum | `int32` |  |
| MinEvaluationRate | `int32` |  |
| LockAnimUpdateRate | `int32` |  |
| EnableUROInterpolation | `bool` |  |
| LODToFrameSkipMap | `TMap < int32 , int32 >` | Map of LOD levels to frame skip amounts. if bShouldUseLodMap is set these values will be used for<br>	  the frameskip amounts and the distance factor thresholds will be ignored. The flag and these values<br>	  should be configured using the customization callback when parameters are created for a component.<br><br>	  Note that this is # of frames to skip, so if you have 20, that means every 21th frame, it will update, and evaluate. |
| MaxEvalRateForInterpolation | `int32` | Max Evaluation Rate allowed for interpolation to be enabled. Beyond, interpolation will be turned off. |
| ShiftBucket | [EUpdateRateShiftBucket](../../../cppenum/E/EU/EUpdateRateShiftBucket.md) | The bucket to use when deciding which counter to use to calculate shift values |

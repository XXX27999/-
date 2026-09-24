# UAnimationSettings

Default animation settings.

## Parents

- UDeveloperSettings

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CompressCommandletVersion | `int32` |  |
| KeyEndEffectorsMatchNameArray | `TArray < FString >` |  |
| DefaultCompressionAlgorithm | `TSubclassOf < UAnimCompress >` |  |
| RotationCompressionFormat | `TEnumAsByte < AnimationCompressionFormat >` |  |
| TranslationCompressionFormat | `TEnumAsByte < AnimationCompressionFormat >` |  |
| MaxCurveError | `float` | Max error for compression of curves using remove redundant keys |
| AlternativeCompressionThreshold | `float` | The alternate error threshold (0.0 means don't try anything other than the current  default scheme)<br><br>	 Determines the current setting for world-space error tolerance in the animation compressor.<br>	 When requested, animation being compressed will also consider an alternative compression<br>	 method if the end result of that method produces less error than the AlternativeCompressionThreshold.<br>	 Also known as "Max End Effector Error" |
| ForceRecompression | `bool` |  |
| bOnlyCheckForMissingSkeletalMeshes | `bool` |  |
| bForceBelowThreshold | `bool` | If true and the existing compression error is greater than Alternative Compression Threshold, then any compression technique (even one that increases the size) with a lower error will be used until it falls below the threshold |
| bFirstRecompressUsingCurrentOrDefault | `bool` | If true, then the animation will be first recompressed with it's current compressor if non-NULL, or with the global default compressor (specified in the engine ini)<br>	 Also known as "Run Current Default Compressor" |
| bRaiseMaxErrorToExisting | `bool` | If true and the existing compression error is greater than Alternative Compression Threshold, then Alternative Compression Threshold will be effectively raised to the existing error level |
| bTryFixedBitwiseCompression | `bool` | If true, the uniform bitwise techniques will be tried |
| bTryPerTrackBitwiseCompression | `bool` | If true, the per-track compressor techniques will be tried |
| bTryLinearKeyRemovalCompression | `bool` | If true, the linear key removal techniques will be tried |
| bTryIntervalKeyRemoval | `bool` | If true, the resampling techniques will be tried |
| bEnablePerformanceLog | `bool` |  |
| bStripAnimationDataOnDedicatedServer | `bool` | If true, animation track data will be stripped from dedicated server cooked data |
| AnimUpdateRateDistanceFactorThesholdsBelow60FPS | `TArray < float >` |  |
| AnimUpdateRateDistanceFactorThesholdsIn60FPS | `TArray < float >` |  |
| AnimUpdateRateDistanceFactorThesholdsIn90FPS | `TArray < float >` |  |
| AnimUpdateRateDistanceFactorThesholdsIn120FPS | `TArray < float >` |  |
| AnimUpdateRateDistanceFactorThesholdsInPC | `TArray < float >` |  |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

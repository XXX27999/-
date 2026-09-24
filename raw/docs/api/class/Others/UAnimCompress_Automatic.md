# UAnimCompress_Automatic

## Parents

- [UAnimCompress](./UAnimCompress.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| MaxEndEffectorError | `float` | Maximum amount of error that a compression technique can introduce in an end effector<br>	 Determines the current setting for world - space error tolerance in the animation compressor.<br>	 When requested, animation being compressed will also consider an alternative compression<br>	 method if the end result of that method produces less error than the AlternativeCompressionThreshold.<br>	 Also known as "Alternative Compression Threshold" |
| bTryFixedBitwiseCompression | `uint32` | If true, the uniform bitwise techniques will be tried |
| bTryPerTrackBitwiseCompression | `uint32` | If true, the per-track compressor techniques will be tried |
| bTryLinearKeyRemovalCompression | `uint32` | If true, the linear key removal techniques will be tried |
| bTryIntervalKeyRemoval | `uint32` | If true, the resampling techniques will be tried |
| bRunCurrentDefaultCompressor | `uint32` | If true, then the animation will be first recompressed with it's current compressor if non-NULL, or with the global default compressor (specified in the engine ini)<br>	 Also known as "First Recompress Using Current Or Default" |
| bAutoReplaceIfExistingErrorTooGreat | `uint32` | If true and the existing compression error is greater than Max End Effector Error, then any compression technique (even one that increases the size) with a lower error will be used until it falls below the threshold<br>	 Also known as "force below threshold" |
| bRaiseMaxErrorToExisting | `uint32` | If true and the existing compression error is greater than Max End Effector Error, then Max End Effector Error will be effectively raised to the existing error level |
| bTryPerTrackVarBitCompression | `uint32` | If true, the per-track variable bit compressor techniques will be tried |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

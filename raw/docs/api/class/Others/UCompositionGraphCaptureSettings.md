# UCompositionGraphCaptureSettings

## Parents

- UMovieSceneCaptureProtocolSettings

## Variables

| Name | Type | Description |
| --- | --- | --- |
| IncludeRenderPasses | [FCompositionGraphCapturePasses](../../cppstruct/F/FC/FCompositionGraphCapturePasses.md) | A list of render passes to include in the capture. Leave empty to export all available passes. |
| bCaptureFramesInHDR | `bool` | Whether to capture the frames as HDR textures (.exr format) |
| HDRCompressionQuality | `int32` | Compression Quality for HDR Frames (0 for no compression, 1 for default compression which can be slow) |
| CaptureGamut | `TEnumAsByte < enum EHDRCaptureGamut >` | The color gamut to use when storing HDR captured data. The gamut depends on whether the bCaptureFramesInHDR option is enabled. |
| PostProcessingMaterial | [FSoftObjectPath](../../cppstruct/F/FS/FSoftObjectPath.md) | Custom post processing material to use for rendering |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

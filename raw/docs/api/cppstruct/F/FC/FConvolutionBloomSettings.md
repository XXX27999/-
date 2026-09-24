# FConvolutionBloomSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Texture | `UTexture2D *` | Texture to replace default convolution bloom kernel |
| Size | `float` | Relative size of the convolution kernel image compared to the minor axis of the viewport |
| CenterUV | [FVector2D](../FV/FVector2D.md) | The UV location of the center of the kernel.  Should be very close to (.5,.5) |
| PreFilterMin | `float` | Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables |
| PreFilterMax | `float` | Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables |
| PreFilterMult | `float` | Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables |
| BufferScale | `float` | Implicit buffer region as a fraction of the screen size to insure the bloom does not wrap across the screen.  Larger sizes have perf impact. |

# FGaussianSumBloomSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Intensity | `float` | Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter |
| Threshold | `float` | minimum brightness the bloom starts having effect<br>	  -1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter |
| SizeScale | `float` | Scale for all bloom sizes |
| Filter1Size | `float` | Diameter size for the Bloom1 in percent of the screen width<br>	  (is done in 12 resolution, larger values cost more performance, good for high frequency details)<br>	  >=0: can be clamped because of shader limitations |
| Filter2Size | `float` | Diameter size for Bloom2 in percent of the screen width<br>	  (is done in 14 resolution, larger values cost more performance)<br>	  >=0: can be clamped because of shader limitations |
| Filter3Size | `float` | Diameter size for Bloom3 in percent of the screen width<br>	  (is done in 18 resolution, larger values cost more performance)<br>	  >=0: can be clamped because of shader limitations |
| Filter4Size | `float` | Diameter size for Bloom4 in percent of the screen width<br>	  (is done in 116 resolution, larger values cost more performance, best for wide contributions)<br>	  >=0: can be clamped because of shader limitations |
| Filter5Size | `float` | Diameter size for Bloom5 in percent of the screen width<br>	  (is done in 132 resolution, larger values cost more performance, best for wide contributions)<br>	  >=0: can be clamped because of shader limitations |
| Filter6Size | `float` | Diameter size for Bloom6 in percent of the screen width<br>	  (is done in 164 resolution, larger values cost more performance, best for wide contributions)<br>	  >=0: can be clamped because of shader limitations |
| Filter1Tint | [FLinearColor](../FL/FLinearColor.md) | Bloom1 tint color |
| Filter2Tint | [FLinearColor](../FL/FLinearColor.md) | Bloom2 tint color |
| Filter3Tint | [FLinearColor](../FL/FLinearColor.md) | Bloom3 tint color |
| Filter4Tint | [FLinearColor](../FL/FLinearColor.md) | Bloom4 tint color |
| Filter5Tint | [FLinearColor](../FL/FLinearColor.md) | Bloom5 tint color |
| Filter6Tint | [FLinearColor](../FL/FLinearColor.md) | Bloom6 tint color |

# FCameraExposureSettings

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Method | `TEnumAsByte < enum EAutoExposureMethod >` | Luminance computation method |
| LowPercent | `float` | The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.<br>	  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority<br>	  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of<br>	  bright spots.<br>	  >0, <100, good values are in the range 70 .. 80 |
| HighPercent | `float` | The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.<br>	  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority<br>	  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of<br>	  bright spots.<br>	  >0, <100, good values are in the range 80 .. 95 |
| MinBrightness | `float` | A good value should be positive near 0. This is the minimum brightness the auto exposure can adapt to.<br>	  It should be tweaked in a dark lighting situation (too small: image appears too bright, too large: image appears too dark).<br>	  Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global<br>	  effect and defined the HDR range - you don't want to change that late in the project development.<br>	  Eye Adaptation is disabled if MinBrightness = MaxBrightness |
| MaxBrightness | `float` | A good value should be positive (2 is a good value). This is the maximum brightness the auto exposure can adapt to.<br>	  It should be tweaked in a bright lighting situation (too small: image appears too bright, too large: image appears too dark).<br>	  Note: Tweaking emissive materials and lights or tweaking auto exposure can look the same. Tweaking auto exposure has global<br>	  effect and defined the HDR range - you don't want to change that late in the project development.<br>	  Eye Adaptation is disabled if MinBrightness = MaxBrightness |
| SpeedUp | `float` | >0 |
| SpeedDown | `float` | >0 |
| Bias | `float` | Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.<br>	  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ... |
| HistogramLogMin | `float` | temporary exposed until we found good values, -8: 1256, -10: 11024 |
| HistogramLogMax | `float` | temporary exposed until we found good values 4: 16, 8: 256 |

# FSlateSound

An intermediary to make UBaseSound available for Slate to play sounds

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ResourceObject | `UObject *` | Pointer to the USoundBase. Holding onto it as a UObject because USoundBase is not available in Slate core.<br>	  Edited via FSlateSoundStructCustomization to ensure you can only set USoundBase assets on it. |

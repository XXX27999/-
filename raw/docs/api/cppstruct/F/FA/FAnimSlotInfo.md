# FAnimSlotInfo

Struct used for passing information from Matinee to an Actor for blending animations during a sequence.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FName` | Name of slot that we want to play the animtion in. |
| ChannelWeights | `TArray < float >` | Strength of each Channel within this Slot. Channel indexs are determined by track order in Matinee. |

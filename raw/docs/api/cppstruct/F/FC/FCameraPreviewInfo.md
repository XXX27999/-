# FCameraPreviewInfo

Preview APawn class for this track

## Fields

| Name | Type | Description |
| --- | --- | --- |
| PawnClass | `TSubclassOf < APawn >` |  |
| AnimSeq | `UAnimSequence *` |  |
| Location | [FVector](../FV/FVector.md) | for now this is read-only. It has maintenance issue to be resolved if I enable this. |
| Rotation | [FRotator](../FR/FRotator.md) |  |
| PawnInst | `APawn *` | APawn Inst - CameraAnimInst doesn't really exist in editor |

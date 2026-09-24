# FTViewTarget

A ViewTarget is the primary actor the camera is associated with.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Target | `AActor *` | Target Actor used to compute POV |
| POV | [FMinimalViewInfo](../FM/FMinimalViewInfo.md) | Computed point of view |
| PlayerState | `APlayerState *` | PlayerState (used to follow same player through pawn transitions, etc., when spectating) |

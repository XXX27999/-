# FCameraTrackingFocusSettings

Settings to control tracking-focus mode.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| ActorToTrack | `AActor *` | Focus distance will be tied to this actor's location. |
| RelativeOffset | [FVector](../FV/FVector.md) | Offset from actor position to track. Relative to actor if tracking an actor, relative to world otherwise. |
| bDrawDebugTrackingFocusPoint | `uint8` | True to draw a debug representation of the tracked position. |

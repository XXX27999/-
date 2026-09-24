# FScreenMessageString

On-screen debug message handling
 Helper struct for tracking on screen messages.

## Fields

| Name | Type | Description |
| --- | --- | --- |
| Key | `uint64` | The 'key' for this message. |
| ScreenMessage | `FString` | The message to display. |
| DisplayColor | [FColor](../FC/FColor.md) | The color to display the message in. |
| TimeToDisplay | `float` | The number of frames to display it. |
| CurrentTimeDisplayed | `float` | The number of frames it has been displayed so far. |
| TextScale | [FVector2D](../FV/FVector2D.md) | Scale of text |
| IsUGCMsg | `bool` | Is ugc message |

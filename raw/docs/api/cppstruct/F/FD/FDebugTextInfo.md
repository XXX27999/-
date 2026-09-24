# FDebugTextInfo

Single entry of a debug text item to render.

  @see AHud
  @see AddDebugText(), RemoveDebugText() and DrawDebugTextList()

## Fields

| Name | Type | Description |
| --- | --- | --- |
| SrcActor | `AActor *` | AActor related to text item |
| SrcActorOffset | [FVector](../FV/FVector.md) | Offset from SrcActor.Location to apply |
| SrcActorDesiredOffset | [FVector](../FV/FVector.md) | Desired offset to interpolate to |
| DebugText | `FString` | Text to display |
| TimeRemaining | `float` | Time remaining for the debug text, -1.f == infinite |
| Duration | `float` | Duration used to lerp desired offset |
| TextColor | [FColor](../FC/FColor.md) | Text color |
| bAbsoluteLocation | `uint32` | whether the offset should be treated as absolute world location of the string |
| bKeepAttachedToActor | `uint32` | If the actor moves does the text also move with it? |
| bDrawShadow | `uint32` | Whether to draw a shadow for the text |
| OrigActorLocation | [FVector](../FV/FVector.md) | When we first spawn store off the original actor location for use with bKeepAttachedToActor |
| Font | `UFont *` | The Font which to display this as.  Will Default to GetSmallFont() |
| FontScale | `float` | Scale to apply to font when rendering |

# FCameraLookatTrackingSettings

Settings to control the camera's lookat feature

## Fields

| Name | Type | Description |
| --- | --- | --- |
| bEnableLookAtTracking | `uint8` | True to enable lookat tracking, false otherwise.<br>	UPROPERTY(Interp, EditAnywhere, BlueprintReadWrite, Category = "LookAt") |
| bDrawDebugLookAtTrackingPosition | `uint8` | True to draw a debug representation of the lookat location |
| LookAtTrackingInterpSpeed | `float` | Controls degree of smoothing. 0.f for no smoothing, higher numbers for fastertighter tracking. |
| ActorToTrack | `AActor *` | If set, camera will track this actor's location |
| RelativeOffset | [FVector](../FV/FVector.md) | Offset from actor position to look at. Relative to actor if tracking an actor, relative to world otherwise. |
| bAllowRoll | `uint8` | True to allow user-defined roll, false otherwise. |

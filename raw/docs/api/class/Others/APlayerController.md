# APlayerController

PlayerControllers are used by human players to control Pawns.

  ControlRotation (accessed via GetControlRotation()), determines the aiming
  orientation of the controlled Pawn.

  In networked games, PlayerControllers exist on the server for every player-controlled pawn,
  and also on the controlling client's machine. They do NOT exist on a client's
  machine for pawns controlled by remote players elsewhere on the network.

## Parents

- [AController](./AController.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Player | `UPlayer *` | UPlayer associated with this PlayerController.  Could be a local player or a net connection. |
| AcknowledgedPawn | `APawn *` | Used in net games so client can acknowledge it possessed a specific pawn. |
| ControllingDirTrackInst | `UInterpTrackInstDirector *` | Director track that's currently possessing this player controller, or none if not possessed. |
| MyHUD | `AHUD *` | Heads up display associated with this PlayerController. |
| PlayerCameraManager | `APlayerCameraManager *` | Camera manager associated with this Player Controller. |
| PlayerCameraManagerClass | `TSubclassOf < APlayerCameraManager >` | PlayerCamera class should be set for each game, otherwise Engine.PlayerCameraManager is used |
| bAutoManageActiveCameraTarget | `bool` | True to allow this player controller to manage the camera target for you,<br>	  typically by using the possessed pawn as the camera target. Set to false<br>	  if you want to manually control the camera target. |
| SmoothTargetViewRotationSpeed | `float` | Interp speed for blending remote view rotation for smoother client updates |
| HiddenActors | `TArray < AActor * >` | The actors which the camera shouldn't see - e.g. used to hide actors which the camera penetrates |
| HiddenPrimitiveComponents | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | Explicit components the camera shouldn't see (helpful for external systems to hide a component from a single player) |
| LastSpectatorStateSynchTime | `float` | Used to make sure the client is kept synchronized when in a spectator state |
| LastSpectatorSyncLocation | [FVector](../../cppstruct/F/FV/FVector.md) | Last location synced on the server for a spectator. |
| LastSpectatorSyncRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | Last rotation synced on the server for a spectator. |
| ClientCap | `int32` | Cap set by server on bandwidth from client to server in bytessec (only has impact if >=2600) |
| CheatManager | `UCheatManager *` | Object that manages "cheat" commands.  Not instantiated in shipping builds. |
| CheatClass | `TSoftClassPtr < UCheatManager >` | Class of my CheatManager.  The Cheat Manager is not created in shipping builds |
| CheatManagerExtras | `TArray < UCheatManager * >` | Object that manages "cheat" commands.  Not instantiated in shipping builds. |
| CheatClassExtras | `TArray < TSoftClassPtr < UCheatManager > >` | Class of my CheatManager.  The Cheat Manager is not created in shipping builds |
| PlayerInput | `UPlayerInput *` | Object that manages player input. |
| ActiveForceFeedbackEffects | `TArray < FActiveForceFeedbackEffect >` |  |
| bPlayerIsWaiting | `uint32` | True if PlayerController is currently waiting for the match to start or to respawn. Only valid in Spectating state. |
| NetPlayerIndex | `uint8` | index identifying players using the same base connection (splitscreen clients)<br>	  Used by netcode to match replicated PlayerControllers to the correct splitscreen viewport and child connection<br>	  replicated via special internal code, not through normal variable replication |
| PendingSwapConnection | `UNetConnection *` | this is set on the OLD PlayerController when performing a swap over a network connection<br>	  so we know what connection we're waiting on acknowledgment from to finish destroying this PC<br>	  (or when the connection is closed)<br>	  @see GameModeBase::SwapPlayerControllers() |
| NetConnection | `UNetConnection *` | The net connection this controller is communicating on, NULL for local players on server |
| RotationInput | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| InputYawScale | `float` | Yaw input speed scaling |
| InputPitchScale | `float` | Pitch input speed scaling |
| InputRollScale | `float` | Roll input speed scaling |
| bShowMouseCursor | `uint32` | Whether the mouse cursor should be displayed. |
| bEnableClickEvents | `uint32` | Whether actorcomponent click events should be generated. |
| bEnableTouchEvents | `uint32` | Whether actorcomponent touch events should be generated. |
| bEnableMouseOverEvents | `uint32` | Whether actorcomponent mouse over events should be generated. |
| bEnableTouchOverEvents | `uint32` | Whether actorcomponent touch over events should be generated. |
| bForceFeedbackEnabled | `uint32` |  |
| ForceFeedbackScale | `float` | Scale applied to force feedback values |
| ClickEventKeys | `TArray < FKey >` |  |
| DefaultMouseCursor | `TEnumAsByte < EMouseCursor :: Type >` |  |
| CurrentMouseCursor | `TEnumAsByte < EMouseCursor :: Type >` |  |
| DefaultClickTraceChannel | `TEnumAsByte < ECollisionChannel >` | Default trace channel used for determining what world object was clicked on. |
| CurrentClickTraceChannel | `TEnumAsByte < ECollisionChannel >` | Trace channel currently being used for determining what world object was clicked on. |
| HitResultTraceDistance | `float` |  |
| bPauseUpdateStreamingState | `uint32` |  |
| bActiveReplayViewer | `uint8` | true means this controller is active now as a replay viewer |
| bEnableReplayRecord | `uint8` | true means this controller is enable to record for replay |
| IsBlockingInput | `bool` |  |
| InputWhiteListWhenBlocked | `TSet < FName >` |  |
| InputBlackList | `TSet < FName >` |  |
| PriorityActionSet | `TSet < FName >` |  |
| PriorityActionClusters | `TArray < FActionCluster >` |  |
| ActionExecuteState | `int32` |  |
| InactiveStateInputComponent | `UInputComponent *` | InputComponent we use when player is in Inactive state. |
| bShouldPerformFullTickWhenPaused | `uint32` | Whether we fully tick when the game is paused, if our tick function is allowed to do so. If false, we do a minimal update during the tick. |
| CurrentTouchInterface | `UTouchInterface *` | The currently set touch interface |
| SpectatorPawn | `ASpectatorPawn *` | The pawn used when spectating (NULL if not spectating). |
| SpawnLocation | [FVector](../../cppstruct/F/FV/FVector.md) | The location used internally when there is no pawn or spectator, to know where to spawn the spectator or focus the camera on death. |
| bIsActorChannelOpen | `bool` |  |
| bIsDemoViewController | `bool` |  |
| bIsLocalPlayerController | `bool` | Set during SpawnActor once and never again to indicate the intent of this controller instance (SERVER ONLY) |
| SeamlessTravelCount | `uint16` | Counter for this players seamless travels (used along with the below value, to restrict ServerNotifyLoadedWorld) |
| LastCompletedSeamlessTravelCount | `uint16` | The value of SeamlessTravelCount, upon the last call to GameModeBase::HandleSeamlessTravelPlayer; used to detect seamless travel |
| bNeedResetCameraOnPossess | `bool` | Restart Player by plane do not reset camera!  Engine Modification by czcheng, 2021.6.8 |
| bNeedResetControlRotator | `bool` |  |
| LevelVisibilityInfoList | `TArray < FLevelVisibilityInfo >` |  |
| bClientRetryClientRestartFailedProcess | `bool` |  |

## Functions

### ServerSetSpectatorWaiting

Indicate that the Spectator is waiting to joinrespawn.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bWaiting | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientSetSpectatorWaiting

Indicate that the Spectator is waiting to joinrespawn.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bWaiting | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetActionExecuteState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bSuccess | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetActionExecuteState

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableCheats

Enables cheats within the game

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FOV

Set the field of view to NewFOV

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewFOV | `float` |  |

**Return**

- Type: 
- Description: _None_

### RestartLevel

Restarts the current level

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LocalTravel

Causes the client to travel to the given URL

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ClientReturnToMainMenu

Return the client to the main menu gracefully

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ReturnReason | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ClientRepObjRef

Development RPC for testing object reference replication

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### Pause

Command to try to pause the game.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPauseByBlueprint

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bPaused | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetName

Trys to set the player's name to the given name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| S | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### SwitchLevel

SwitchLevel to the given MapURL.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetHitResultUnderCursor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TraceChannel | `ECollisionChannel` |  |
| bTraceComplex | `bool` |  |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### GetHitResultUnderCursorByChannel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TraceChannel | `ETraceTypeQuery` |  |
| bTraceComplex | `bool` |  |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### GetHitResultUnderCursorForObjects

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` |  |
| bTraceComplex | `bool` |  |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### GetHitResultUnderFinger

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |
| TraceChannel | `ECollisionChannel` |  |
| bTraceComplex | `bool` |  |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### GetHitResultUnderFingerByChannel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |
| TraceChannel | `ETraceTypeQuery` |  |
| bTraceComplex | `bool` |  |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### GetHitResultUnderFingerForObjects

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` |  |
| bTraceComplex | `bool` |  |
| HitResult | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### DeprojectMousePositionToWorld

Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| WorldDirection | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### DeprojectScreenPositionToWorld

Convert 2D screen position to World Space 3D position and direction. Returns false if unable to determine value.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ScreenX | `float` |  |
| ScreenY | `float` |  |
| WorldLocation | `FVector &` |  |
| WorldDirection | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### ProjectWorldLocationToScreen

Convert a World Space 3D position into a 2D Screen Space position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector` |  |
| ScreenLocation | `FVector2D &` |  |
| bPlayerViewportRelative | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetMouseLocation

Positions the mouse cursor in screen space, in pixels.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| X | `int` |  |
| Y | `int` |  |

**Return**

- Type: 
- Description: _None_

### StartFire

Fire the player's currently selected weapon with the optional fire mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FireModeNum | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### ClientEnableNetworkVoice

Tell the client to enable or disable voice chat (not muting)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` | enable or disable voice chat |

**Return**

- Type: 
- Description: _None_

### ToggleSpeaking

Toggle voice chat on and off

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInSpeaking | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientVoiceHandshakeComplete

Tells the client that the server has all the information it needs and that it
	  is ok to start sending voice packets. The server will already send voice packets
	  when this function is called, since it is set server side and then forwarded

	  NOTE: This is done as an RPC instead of variable replication because ordering matters

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerMutePlayer

Tell the server to mute a player for this controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerId | `FUniqueNetIdRepl` | player id to mute |

**Return**

- Type: 
- Description: _None_

### ServerUnmutePlayer

Tell the server to unmute a player for this controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerId | `FUniqueNetIdRepl` | player id to unmute |

**Return**

- Type: 
- Description: _None_

### ClientMutePlayer

Tell the client to mute a player for this controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerId | `FUniqueNetIdRepl` | player id to mute |

**Return**

- Type: 
- Description: _None_

### ClientUnmutePlayer

Tell the client to unmute a player for this controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerId | `FUniqueNetIdRepl` | player id to unmute |

**Return**

- Type: 
- Description: _None_

### ConsoleKey

Console control commands, useful when remote debugging so you can't touch the console the normal way

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### SendToConsole

Sends a command to the console to execute if not shipping version

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Command | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ClientAddTextureStreamingLoc

Adds a location to the texture streaming system for the specified duration.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLoc | `FVector` |  |
| Duration | `float` |  |
| bOverrideLocation | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientCancelPendingMapChange

Tells client to cancel any pending map change.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientCapBandwidth

Set CurrentNetSpeed to the lower of its current value and Cap.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Cap | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ClientCommitMapChange

Actually performs the level transition prepared by PrepareMapChange().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientFlushLevelStreaming

Tells the client to block until all pending level streaming actions are complete
	  happens at the end of the tick
	  primarily used to force update the client ASAP at join time

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientForceGarbageCollection

Forces GC at the end of the tick on the client

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientGameEnded

Replicated function called by GameHasEnded().

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndGameFocus | `AActor *` | - actor to view with camera |
| bIsWinner | `bool` | - true if this controller is on winning team |

**Return**

- Type: 
- Description: _None_

### ClientGotoState

Server uses this to force client into NewState .

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewState | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ClientIgnoreLookInput

calls IgnoreLookInput on client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIgnore | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientIgnoreMoveInput

calls IgnoreMoveInput on client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIgnore | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientMessage

Outputs a message to HUD

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| S | `FString &` | - message to display |
| Type | `FName` | - @todo document |
| MsgLifeTime | `float` | - Optional length of time to display 0 = default time |

**Return**

- Type: 
- Description: _None_

### ClientPlayCameraAnim

Play the indicated CameraAnim on this camera.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AnimToPlay | `UCameraAnim *` | - Camera animation to play |
| Scale | `float` | - "Intensity" scalar. This is the scale at which the anim was first played. |
| Rate | `float` | - Multiplier for playback rate. 1.0 = normal. |
| BlendInTime | `float` | - Time to interpolate in from zero, for smooth starts |
| BlendOutTime | `float` | - Time to interpolate out to zero, for smooth finishes |
| bLoop | `bool` | - True if the animation should loop, false otherwise |
| bRandomStartTime | `bool` | - Whether or not to choose a random time to start playing. Only really makes sense for bLoop = true |
| Space | `ECameraAnimPlaySpace :: Type` | - Animation play area |
| CustomPlaySpace | [FRotator](../../cppstruct/F/FR/FRotator.md) | - Matrix used when Space = CAPS_UserDefined |

**Return**

- Type: 
- Description: _None_

### ClientPlayCameraShake

Play Camera Shake

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Shake | `TSubclassOf < UCameraShake >` | - Camera shake animation to play |
| Scale | `float` | - Scalar defining how "intense" to play the anim |
| PlaySpace | `ECameraAnimPlaySpace :: Type` | - Which coordinate system to play the shake in (used for CameraAnims within the shake). |
| UserPlaySpaceRot | [FRotator](../../cppstruct/F/FR/FRotator.md) | - Matrix used when PlaySpace = CAPS_UserDefined |

**Return**

- Type: 
- Description: _None_

### ClientPlayCameraShakeWithWorldLocation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Shake | `TSubclassOf < UCameraShake >` |  |
| WorldLocation | `FVector` |  |
| Scale | `float` |  |
| PlaySpace | `ECameraAnimPlaySpace :: Type` |  |
| UserPlaySpaceRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### ClientPlaySound

Play sound client-side (so only the client will hear it)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Sound | `USoundBase *` | - Sound to play |
| VolumeMultiplier | `float` | - Volume multiplier to apply to the sound |
| PitchMultiplier | `float` | - Pitch multiplier to apply to the sound |

**Return**

- Type: 
- Description: _None_

### ClientPlaySoundAtLocation

Play sound client-side at the specified location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Sound | `USoundBase *` | - Sound to play |
| Location | `FVector` | - Location to play the sound at |
| VolumeMultiplier | `float` | - Volume multiplier to apply to the sound |
| PitchMultiplier | `float` | - Pitch multiplier to apply to the sound |

**Return**

- Type: 
- Description: _None_

### ClientPrepareMapChange

Asynchronously loads the given level in preparation for a streaming map transition.
	  the server sends one function per level name since dynamic arrays can't be replicated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LevelName | `FName` |  |
| bFirst | `bool` | - whether this is the first item in the list (so clear the list first) |
| bLast | `bool` | - whether this is the last item in the list (so start preparing the change after receiving it) |

**Return**

- Type: 
- Description: _None_

### ClientPrestreamTextures

Forces the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by the specified actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ForcedActor | `AActor *` | - The actor whose textures should be forced into memory. |
| ForceDuration | `float` | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. |
| bEnableStreaming | `bool` | - Whether to start (true) or stop (false) streaming |
| CinematicTextureGroups | `int32` | - Bitfield indicating which texture groups that use extra high-resolution mips |

**Return**

- Type: 
- Description: _None_

### ClientReset

Tell client to reset the PlayerController

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientRestart

Tell client to restart the level

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ClientSetBlockOnAsyncLoading

Tells the client to block until all pending level streaming actions are complete.
	  Happens at the end of the tick primarily used to force update the client ASAP at join time.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientSetCameraFade

Tell client to fade camera

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableFading | `bool` |  |
| FadeColor | `FColor` |  |
| FadeAlpha | `FVector2D` |  |
| FadeTime | `float` |  |
| bFadeAudio | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientSetCameraMode

Replicated function to set camera style on client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewCamMode | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ClientSetCinematicMode

Called by the server to synchronize cinematic transitions with the client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInCinematicMode | `bool` |  |
| bAffectsMovement | `bool` |  |
| bAffectsTurning | `bool` |  |
| bAffectsHUD | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientSetForceMipLevelsToBeResident

Forces the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by the specified material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` | - The material whose textures should be forced into memory. |
| ForceDuration | `float` | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. |
| CinematicTextureGroups | `int32` | - Bitfield indicating which texture groups that use extra high-resolution mips |

**Return**

- Type: 
- Description: _None_

### ClientSetHUD

Set the client's class of HUD and spawns a new instance of it. If there was already a HUD active, it is destroyed.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewHUDClass | `TSubclassOf < AHUD >` |  |

**Return**

- Type: 
- Description: _None_

### GetViewportSize

Helper to get the size of the HUD canvas for this player controller.  Returns 0 if there is no HUD

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SizeX | `int32 &` |  |
| SizeY | `int32 &` |  |

**Return**

- Type: 
- Description: _None_

### GetHUD

Gets the HUD currently being used by this player controller

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMouseCursorWidget

Sets the Widget for the Mouse Cursor to display

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Cursor | `EMouseCursor :: Type` | - the cursor to set the widget for |
| CursorWidget | `UUserWidget *` | - the widget to set the cursor to |

**Return**

- Type: 
- Description: _None_

### ClientSetViewTarget

Set the view target

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| A | `AActor *` | - new actor to set as view target |
| TransitionParams | [FViewTargetTransitionParams](../../cppstruct/F/FV/FViewTargetTransitionParams.md) | - parameters to use for controlling the transition |

**Return**

- Type: 
- Description: _None_

### ClientSpawnCameraLensEffect

Spawn a camera lens effect (e.g. blood).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LensEffectEmitterClass | `TSubclassOf < AEmitterCameraLensEffectBase >` |  |

**Return**

- Type: 
- Description: _None_

### ClientClearCameraLensEffects

Removes all Camera Lens Effects.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientStopCameraAnim

Stop camera animation on client.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AnimToStop | `UCameraAnim *` |  |

**Return**

- Type: 
- Description: _None_

### ClientStopCameraShake

Stop camera shake on client.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Shake | `TSubclassOf < UCameraShake >` |  |
| bImmediately | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClientPlayForceFeedback

Play a force feedback pattern on the player's controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ForceFeedbackEffect | `UForceFeedbackEffect *` | The force feedback pattern to play |
| bLooping | `bool` | Whether the pattern should be played repeatedly or be a single one shot |
| bIgnoreTimeDilation | `bool` | Whether the pattern should ignore time dilation |
| Tag | `FName` | A tag that allows stopping of an effect. If another effect with this Tag is playing, it will be stopped and replaced |

**Return**

- Type: 
- Description: _None_

### ClientStopForceFeedback

Stops a playing force feedback pattern

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ForceFeedbackEffect | `UForceFeedbackEffect *` | If set only patterns from that effect will be stopped |
| Tag | `FName` | If not none only the pattern with this tag will be stopped |

**Return**

- Type: 
- Description: _None_

### PlayDynamicForceFeedback

Latent action that controls the playing of force feedback
	  Begins playing when Start is called.  Calling Update or Stop if the feedback is not active will have no effect.
	  Completed will execute when Stop is called or the duration ends.
	  When Update is called the Intensity, Duration, and affect values will be updated with the current inputs

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Intensity | `float` | How strong the feedback should be. Valid values are between 0.0 and 1.0 |
| Duration | `float` | How long the feedback should play for. If the value is negative it will play until stopped |
| bAffectsLeftLarge | `bool` |  |
| bAffectsLeftSmall | `bool` |  |
| bAffectsRightLarge | `bool` |  |
| bAffectsRightSmall | `bool` |  |
| Action | `TEnumAsByte < EDynamicForceFeedbackAction :: Type >` |  |
| LatentInfo | [FLatentActionInfo](../../cppstruct/F/FL/FLatentActionInfo.md) |  |

**Return**

- Type: 
- Description: _None_

### PlayHapticEffect

Play a haptic feedback curve on the player's controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HapticEffect | `UHapticFeedbackEffect_Base *` | The haptic effect to play |
| Hand | `EControllerHand` | Which hand to play the effect on |
| Scale | `float` | Scale between 0.0 and 1.0 on the intensity of playback |
| bLoop | `bool` |  |

**Return**

- Type: 
- Description: _None_

### StopHapticEffect

Stops a playing haptic feedback curve

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hand | [EControllerHand](../../cppenum/E/EC/EControllerHand.md) | Which hand to stop the effect for |

**Return**

- Type: 
- Description: _None_

### SetHapticsByValue

Sets the value of the haptics for the specified hand directly, using frequency and amplitude.  NOTE:  If a curve is already
	 playing for this hand, it will be cancelled in favour of the specified values.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Frequency | `float` | The normalized frequency [0.0, 1.0] to play through the haptics system |
| Amplitude | `float` | The normalized amplitude [0.0, 1.0] to set the haptic feedback to |
| Hand | [EControllerHand](../../cppenum/E/EC/EControllerHand.md) | Which hand to play the effect on |

**Return**

- Type: 
- Description: _None_

### SetControllerLightColor

Sets the light color of the player's controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Color | [FColor](../../cppstruct/F/FC/FColor.md) | The color for the light to be |

**Return**

- Type: 
- Description: _None_

### ClientTravel

Travel to a different map or IP address. Calls the PreClientTravel event before doing anything.
	  NOTE: This is implemented as a locally executed wrapper for ClientTravelInternal, to avoid API compatability breakage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` | A string containing the mapname (or IP address) to travel to, along with option keyvalue pairs |
| TravelType | `ETravelType` | specifies whether the client should append URL options used in previous travels; if true is specified |
| bSeamless | `bool` | Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative) |
| MapPackageGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) | The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded, |

**Return**

- Type: 
- Description: _None_

### ClientTravelInternal

Internal clientside implementation of ClientTravel - use ClientTravel to call this

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| URL | `FString &` | A string containing the mapname (or IP address) to travel to, along with option keyvalue pairs |
| TravelType | `ETravelType` | specifies whether the client should append URL options used in previous travels; if true is specified |
| bSeamless | `bool` | Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative) |
| MapPackageGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) | The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded, |

**Return**

- Type: 
- Description: _None_

### ClientUpdateLevelStreamingStatus

Replicated Update streaming status

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageName | `FName` | - Name of the level package name used for loading. |
| bNewShouldBeLoaded | `bool` | - Whether the level should be loaded |
| bNewShouldBeVisible | `bool` | - Whether the level should be visible if it is loaded |
| bNewShouldBlockOnLoad | `bool` | - Whether we want to force a blocking load |
| LODIndex | `int32` | - Current LOD index for a streaming level |

**Return**

- Type: 
- Description: _None_

### ClientWasKicked

Notify client they were kicked from the server

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| KickReason | `FText &` |  |

**Return**

- Type: 
- Description: _None_

### ClientStartOnlineSession

Notify client that the session is starting

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientEndOnlineSession

Notify client that the session is about to start

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientRetryClientRestart

Assign Pawn to player, but avoid calling ClientRestart if we have already accepted this pawn

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewPawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ClientReceiveLocalizedMessage

send client localized message id

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Message | `TSubclassOf < ULocalMessage >` |  |
| Switch | `int32` |  |
| RelatedPlayerState_1 | `APlayerState *` |  |
| RelatedPlayerState_2 | `APlayerState *` |  |
| OptionalObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### ServerAcknowledgePossession

acknowledge possession of pawn

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| P | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### ServerCamera

change mode of camera

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMode | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ServerChangeName

Change name of server

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| S | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### ServerNotifyLoadedWorld

Called to notify the server when the client has loaded a new world via seamless traveling

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldPackageName | `FName` | the name of the world package that was loaded |

**Return**

- Type: 
- Description: _None_

### ServerNotifyStreamLevelDisFactor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFactor | `float` |  |

**Return**

- Type: 
- Description: _None_

### ServerPause

Replicate pause request to the server

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerRestartPlayer

Attempts to restart this player, generally called from the client upon respawn request.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerSetSpectatorLocation

When spectating, updates spectator locationrotation and pings the server to make sure spectating should continue.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLoc | `FVector` |  |
| NewRot | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### ServerCheckClientPossession

Tells the server to make sure the possessed pawn is in sync with the client.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerCheckClientPossessionReliable

Reliable version of ServerCheckClientPossession to be used when there is no likely danger of spamming the network.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerShortTimeout

Notifies the server that the client has ticked gameplay code, and should no longer get the extended "still loading" timeout grace period

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerUpdateCamera

If PlayerCamera.bUseClientSideCameraUpdates is set, client will replicate camera positions to the server.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CamLoc | `FVector_NetQuantize` |  |
| CamPitchAndYaw | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ServerUpdateCameraLocation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CamLoc | `FVector_NetQuantize` |  |

**Return**

- Type: 
- Description: _None_

### ServerUpdateLevelVisibility

Called when the client addsremoves a streamed level
	  the server will only replicate references to Actors in visible levels so that it's impossible to send references to
	  Actors the client has not initialized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageName | `FName` | the name of the package for the level whose status changed |
| bIsVisible | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ServerUpdateLevelListVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageNames | `TArray < FName > &` |  |
| bIsVisible | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ServerUpdateLevelListPackageVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageInfo | `TArray < FLevelVisibilityInfo > &` |  |

**Return**

- Type: 
- Description: _None_

### ServerUpdateLevelIndexListPackageVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PackageInfo | `TArray < FLevelIndexVisibilityInfo > &` |  |

**Return**

- Type: 
- Description: _None_

### ServerVerifyViewTarget

Used by client to request server to confirm current viewtarget (server will respond with ClientSetViewTarget() ).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerViewNextPlayer

Move camera to next player on round ended or spectating

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerViewPrevPlayer

Move camera to previous player on round ended or spectating

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ServerViewSelf

Move camera to current user

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TransitionParams | [FViewTargetTransitionParams](../../cppstruct/F/FV/FViewTargetTransitionParams.md) |  |

**Return**

- Type: 
- Description: _None_

### ClientTeamMessage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SenderPlayerState | `APlayerState *` |  |
| S | `FString &` |  |
| Type | `FName` |  |
| MsgLifeTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### ServerToggleAILogging

Used by UGameplayDebuggingControllerComponent to replicate messages for AI debugging in network games.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddPitchInput

Add Pitch (look up) input. This value is multiplied by InputPitchScale.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Val | `float` | Amount to add to Pitch. This value is multiplied by InputPitchScale. |

**Return**

- Type: 
- Description: _None_

### AddYawInput

Add Yaw (turn) input. This value is multiplied by InputYawScale.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Val | `float` | Amount to add to Yaw. This value is multiplied by InputYawScale. |

**Return**

- Type: 
- Description: _None_

### AddRollInput

Add Roll input. This value is multiplied by InputRollScale.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Val | `float` | Amount to add to Roll. This value is multiplied by InputRollScale. |

**Return**

- Type: 
- Description: _None_

### IsInputKeyDown

Returns true if the given keybutton is pressed on the input of the controller (if present)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### WasInputKeyJustPressed

Returns true if the given keybutton was up last frame and down this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### WasInputKeyJustReleased

Returns true if the given keybutton was down last frame and up this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetInputAnalogKeyState

Returns the analog value for the given keybutton.  If analog isn't supported, returns 1 for down and 0 for up.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetInputVectorKeyState

Returns the vector value for the given keybutton.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetInputTouchState

Retrieves the X and Y screen coordinates of the specified touch key. Returns false if the touch index is not down

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |
| LocationX | `float &` |  |
| LocationY | `float &` |  |
| bIsCurrentlyPressed | `bool &` |  |

**Return**

- Type: 
- Description: _None_

### GetInputMotionState

Retrieves the current motion state of the player's input device

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tilt | `FVector &` |  |
| RotationRate | `FVector &` |  |
| Gravity | `FVector &` |  |
| Acceleration | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### GetMousePosition

Retrieves the X and Y screen coordinates of the mouse cursor. Returns false if there is no associated mouse device

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LocationX | `float &` |  |
| LocationY | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetInputKeyTimeDown

Returns how long the given keybutton has been down.  Returns 0 if it's up or it just went down this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Key | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetInputMouseDelta

Retrieves how far the mouse moved this frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaX | `float &` |  |
| DeltaY | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetInputAnalogStickState

Retrieves the X and Y displacement of the given analog stick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WhichStick | `EControllerAnalogStick :: Type` |  |
| StickX | `float &` |  |
| StickY | `float &` |  |

**Return**

- Type: 
- Description: _None_

### ActivateTouchInterface

Activates a new touch interface for this player controller

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTouchInterface | `UTouchInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetVirtualJoystickVisibility

Set the virtual joystick visibility.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bVisible | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FadeInVirtualJoystick

Fade in the virtual joystick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FadeDuration | `float` |  |

**Return**

- Type: 
- Description: _None_

### FadeOutVirtualJoystick

Fade out the virtual joystick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FadeDuration | `float` |  |

**Return**

- Type: 
- Description: _None_

### InitVirtualJoystickBySetting

Set the virtual joystick visibility.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetViewportCacheGeometryScale

获取Viewport的缓存几何缩放

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Camera

Change Camera mode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewMode | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetViewTargetWithBlend

Set the view target blending with variable control

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewViewTarget | `AActor *` | - new actor to set as view target |
| BlendTime | `float` | - time taken to blend |
| BlendFunc | `EViewTargetBlendFunction` | - Cubic, Linear etc functions for blending |
| BlendExp | `float` | - Exponent, used by certain blend functions to control the shape of the curve. |
| bLockOutgoing | `bool` | - If true, lock outgoing viewtarget to last frame's camera position for the remainder of the blend. |

**Return**

- Type: 
- Description: _None_

### FlushPressedKeys

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FlushPressedKeysImmediate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FlushPressedMouseKeys

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### FlushPressedMouseKeysImmediate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAudioListenerOverride

Used to override the default positioning of the audio listener

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AttachToComponent | `USceneComponent *` | Optional component to attach the audio listener to |
| Location | `FVector` | Depending on whether Component is attached this is either an offset from its location or an absolute position |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | Depending on whether Component is attached this is either an offset from its rotation or an absolute rotation |

**Return**

- Type: 
- Description: _None_

### ClearAudioListenerOverride

Clear any overrides that have been applied to audio listener

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConsumeResidualNonAxisInput

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCinematicMode

ServerSP only function for changing whether the player is in cinematic mode.  Updates values of various state variables, then replicates the call to the client
	  to sync the current cinematic mode.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInCinematicMode | `bool` | specify true if the player is entering cinematic mode; false if the player is leaving cinematic mode. |
| bHidePlayer | `bool` | specify true to hide the player's pawn (only relevant if bInCinematicMode is true) |
| bAffectsHUD | `bool` | specify true if we should showhide the HUD to match the value of bCinematicMode |
| bAffectsMovement | `bool` | specify true to disable movement in cinematic mode, enable it when leaving |
| bAffectsTurning | `bool` | specify true to disable turning in cinematic mode or enable it when leaving |

**Return**

- Type: 
- Description: _None_

### OnServerStartedVisualLogger

Notify from server that Visual Logger is recording, to show that information on client about possible performance issues

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsLogging | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetSpectatorPawn

Get the Pawn used when spectating. NULL when not spectating.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetFocalLocation

Returns the location the PlayerController is focused on.
	   If there is a possessed Pawn, returns the Pawn's location.
	   If there is a spectator Pawn, returns that Pawn's location.
	   Otherwise, returns the PlayerController's spawn location (usually the last known Pawn location after it has died).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StartTouchEventRecord

开始记录Touch事件，将信息保存在TouchEventRecordData中，给定一个文件名存盘

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RecordFileName | `FString &` | 记录保存到的文件名 |

**Return**

- Type: 
- Description: _None_

### StopTouchEventRecord

停止记录Touch事件，将TouchEventRecordData中的数据保存到文件

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReplayTouchEventRecord

从文件中加载Touch事件，并进行重放

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| RecordFileName | `FString &` | 记录文件名 |

**Return**

- Type: 
- Description: _None_

### GetTouchRecordStartAndEndRotation

获取Touch记录中保存的起始和终止旋转角

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartRotation | `FRotator &` | 起始旋转角，引用，在函数内赋值 |
| EndRotation | `FRotator &` | 终止旋转角，引用，在函数内赋值 |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

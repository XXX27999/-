# ACharacter

Characters are Pawns that have a mesh, collision, and built-in movement logic.
  They are responsible for all physical interaction between the player or AI and the world, and also implement basic networking and input models.
  They are designed for a vertically-oriented player representation that can walk, jump, fly, and swim through the world using CharacterMovementComponent.

  @see APawn, UCharacterMovementComponent

## Parents

- [APawn](./APawn.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Mesh | `USkeletalMeshComponent *` | The main skeletal mesh associated with this Character (optional sub-object). |
| CharacterMovement | `UCharacterMovementComponent *` | Movement component used for movement logic in various movement modes (walking, falling, etc), containing relevant settings and functions to control movement. |
| CapsuleComponent | `UCapsuleComponent *` | The CapsuleComponent being used for movement collision (by CharacterMovement). Always treated as being vertically aligned in simple collision check functions. |
| BasedMovement | [FBasedMovementInfo](../../cppstruct/F/FB/FBasedMovementInfo.md) | Info about our current movement base (object we are standing on). |
| ReplicatedBasedMovement | [FBasedMovementInfo](../../cppstruct/F/FB/FBasedMovementInfo.md) | Replicated version of relative movement. Read-only on simulated proxies! |
| AnimRootMotionTranslationScale | `float` | Scale to apply to root motion translation on this Character |
| NetworkPredictionInterface | `TScriptInterface < INetworkPredictionInterface >` |  |
| BaseTranslationOffset | [FVector](../../cppstruct/F/FV/FVector.md) | Saved translation offset of mesh. |
| BaseRotationOffset | [FQuat](../../cppstruct/F/FQ/FQuat.md) | Saved rotation offset of mesh. |
| ReplicatedServerLastTransformUpdateTimeStamp | `float` | CharacterMovement ServerLastTransformUpdateTimeStamp value, replicated to simulated proxies. |
| ReplicatedMovementMode | `uint8` | Flag that we are receiving replication of the based movement. |
| bInBaseReplication | `bool` | Flag that we are receiving replication of the based movement. |
| CrouchedEyeHeight | `float` | Default crouched eye height |
| bIsCrouched | `uint32` | Set by character movement to specify that this Character is currently crouched. |
| bPressedJump | `uint32` | When true, player wants to jump |
| bClientUpdating | `uint32` | When true, applying updates to network client (replaying saved moves for a locally controlled character) |
| bClientWasFalling | `uint32` | True if Pawn was initially falling when started to replay network moves. |
| bClientResimulateRootMotion | `uint32` | If server disagrees with root motion track position, client has to resimulate root motion from last AckedMove. |
| bClientResimulateRootMotionSources | `uint32` | If server disagrees with root motion state, client has to resimulate root motion from last AckedMove. |
| bSimGravityDisabled | `uint32` | Disable simulated gravity (set when character encroaches geometry on client, to keep him from falling through floors) |
| bClientCheckEncroachmentOnNetUpdate | `uint32` |  |
| bServerMoveIgnoreRootMotion | `uint32` | Disable root motion on the server. When receiving a DualServerMove, where the first move is not root motion and the second is. |
| JumpKeyHoldTime | `float` | Jump key Held Time.<br>	  This is the time that the player has held the jump key, in seconds. |
| JumpMaxHoldTime | `float` | The max time the jump key can be held.<br>	  Note that if StopJumping() is not called before the max jump hold time is reached,<br>	  then the character will carry on receiving vertical velocity. Therefore it is usually<br>	  best to call StopJumping() when jump input has ceased (such as a button up event). |
| JumpMaxCount | `int32` | The max number of jumps the character can perform.<br>      Note that if JumpMaxHoldTime is non zero and StopJumping is not called, the player<br>      may be able to perform and unlimited number of jumps. Therefore it is usually<br>      best to call StopJumping() when jump input has ceased (such as a button up event). |
| JumpCurrentCount | `int32` | Tracks the current number of jumps performed.<br>      This is incremented in CheckJumpInput, used in CanJump_Implementation, and reset in OnMovementModeChanged.<br>      When providing overrides for these methods, it's recommended to either manually<br>      increment  reset this value, or call the Super:: method. |
| bWasJumping | `uint32` |  |
| bUseReplaySampleRot | `uint32` |  |
| SavedRootMotion | [FRootMotionSourceGroup](../../cppstruct/F/FR/FRootMotionSourceGroup.md) | For LocallyControlled Autonomous clients.<br>	   During a PerformMovement() after root motion is prepared, we save it off into this and<br>	   then record it into our SavedMoves.<br>	   During SavedMove playback we use it as our "Previous Move" SavedRootMotion which includes<br>	   last received root motion from the Server |
| ClientRootMotionParams | [FRootMotionMovementParams](../../cppstruct/F/FR/FRootMotionMovementParams.md) | For LocallyControlled Autonomous clients. Saved root motion data to be used by SavedMoves. |
| RootMotionRepMoves | `TArray < FSimulatedRootMotionReplicatedMove >` | Array of previously received root motion moves from the server. |
| RepRootMotion | [FRepRootMotionMontage](../../cppstruct/F/FR/FRepRootMotionMontage.md) | Replicated Root Motion montage |
| bReplicateBasedMovement | `uint8` |  |
| DisableParticleNames | `TArray < FString >` |  |
| GeneralCampID | `int32` |  |
| EnableApplyMomentumInRadialDamage | `bool` |  |
| bEnableAsyncAnimInstance | `bool` |  |
| bAsyncNewAnimInstance | `bool` |  |
| AsyncAnimInstances | `TMap < UAnimInstance * , bool >` |  |
| bMarkScopeIn | `bool` |  |
| ArrowComponent | `UArrowComponent *` |  |

## Functions

### CacheInitialMeshOffset

Cache mesh offset from capsule. This is used as the target for network smoothing interpolation, when the mesh is offset with lagged smoothing.
	  This is automatically called during initialization; call this at runtime if you intend to change the default mesh offset from the capsule.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MeshRelativeLocation | `FVector` |  |
| MeshRelativeRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedBasedMovement

Rep notify for ReplicatedBasedMovement

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetReplicateMovement

Set whether this actor's movement replicates to network clients.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInReplicateMovement | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedMovementMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LastReplicatedMovementMode | `uint8` |  |

**Return**

- Type: 
- Description: _None_

### GetReplicatedMovementMode

Returns ReplicatedMovementMode

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBaseTranslationOffset

Get the saved translation offset of mesh. This is how much extra offset is applied from the center of the capsule.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBaseRotationOffsetRotator

Get the saved rotation offset of mesh. This is how much extra rotation is applied from the capsule rotation.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_IsCrouched

Handle Crouching replicated from server

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMovementBase

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetReplicatedMovementBase

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Jump

Make the character jump on the next update.
	  If you want your character to jump according to the time that the jump key is held,
	  then you can set JumpKeyHoldTime to some non-zero value. Make sure in this case to
	  call StopJumping() when you want the jump's z-velocity to stop being applied (such
	  as on a button up event), otherwise the character will carry on receiving the
	  velocity until JumpKeyHoldTime is reached.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopJumping

Stop the character from jumping on the next update.
	  Call this from an input event (such as a button 'up' event) to cease applying
	  jump Z-velocity. If this is not called, then jump z-velocity will be applied
	  until JumpMaxHoldTime is reached.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanJump

Check if the character can jump in the current state.

	  The default implementation may be overridden or extended by implementing the custom CanJump event in Blueprints.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CanJumpInternal

Customizable event to check if the character can jump in the current state.
	  Default implementation returns true if the character is on the ground and not crouching,
	  has a valid CharacterMovementComponent and CanEverJump() returns true.
	  Default implementation also allows for 'hold to jump higher' functionality:
	  As well as returning true when on the ground, it also returns true when GetMaxJumpTime is more
	  than zero and IsJumping returns true.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsJumpProvidingForce

True if jump is actively providing a force, such as when the jump key is held and the time it has been held is less than JumpMaxHoldTime.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PlayAnimMontage

Play Animation Montage on the character mesh

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AnimMontage | `UAnimMontage *` |  |
| InPlayRate | `float` |  |
| StartSectionName | `FName` |  |
| TPP | `bool` |  |
| FPP | `bool` |  |
| NewFPP | `bool` |  |

**Return**

- Type: 
- Description: _None_

### StopAnimMontage

Stop Animation Montage. If NULL, it will stop what's currently active. The Blend Out Time is taken from the montage asset that is being stopped.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AnimMontage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentMontage

Return current playing Montage

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsVelocitySimulated

是否正在速度场模拟中(实际生效)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAdditiveVelocity

获取速度场的叠加速度

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSimulatedVelocity

获取速度场中的模拟速度(原有速度+叠加速度)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LaunchCharacter

Set a pending launch velocity on the Character. This velocity will be processed on the next CharacterMovementComponent tick,
	   and will set it to the "falling" state. Triggers the OnLaunched event.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LaunchVelocity | `FVector &` |  |
| bXYOverride | `bool` |  |
| bZOverride | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnLaunched

Let blueprint know that we were launched

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LaunchVelocity | `FVector &` |  |
| bXYOverride | `bool` |  |
| bZOverride | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnJumped

Event fired when the character has just started jumping

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnLanded

Called upon landing when falling, to perform actions based on the Hit result.
	 Note that movement mode is still "Falling" during this event. Current Velocity value is the velocity at the time of landing.
	 Consider OnMovementModeChanged() as well, as that can be used once the movement mode changes to the new mode (most likely Walking).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | `FHitResult &` | Result describing the landing that resulted in a valid landing spot. |

**Return**

- Type: 
- Description: _None_

### OnWalkingOffLedge

Event fired when the Character is walking off a surface and is about to fall because CharacterMovement->CurrentFloor became unwalkable.
	  If CharacterMovement->MovementMode does not change during this event then the character will automatically start falling afterwards.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PreviousFloorImpactNormal | `FVector &` | Normal of the previous walkable floor. |
| PreviousFloorContactNormal | `FVector &` | Normal of the contact with the previous walkable floor. |
| PreviousLocation | `FVector &` | Previous character location before movement off the ledge. |
| TimeDelta | `float` |  |

**Return**

- Type: 
- Description: _None_

### Crouch

Request the character to start crouching. The request is processed on the next update of the CharacterMovementComponent.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bClientSimulation | `bool` |  |

**Return**

- Type: 
- Description: _None_

### UnCrouch

Request the character to stop crouching. The request is processed on the next update of the CharacterMovementComponent.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bClientSimulation | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnEndCrouch

Event when Character stops crouching.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HalfHeightAdjust | `float` | difference between default collision half-height, and actual crouched capsule half-height. |
| ScaledHalfHeightAdjust | `float` | difference after component scale is taken in to account. |

**Return**

- Type: 
- Description: _None_

### K2_OnStartCrouch

Event when Character crouches.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| HalfHeightAdjust | `float` | difference between default collision half-height, and actual crouched capsule half-height. |
| ScaledHalfHeightAdjust | `float` | difference after component scale is taken in to account. |

**Return**

- Type: 
- Description: _None_

### K2_OnMovementModeChanged

Called from CharacterMovementComponent to notify the character that the movement mode has changed.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrevMovementMode | `EMovementMode` | Movement mode before the change |
| NewMovementMode | `EMovementMode` | New movement mode |
| PrevCustomMode | `uint8` | Custom mode before the change (applicable if PrevMovementMode is Custom) |
| NewCustomMode | `uint8` | New custom mode (applicable if NewMovementMode is Custom) |

**Return**

- Type: 
- Description: _None_

### K2_UpdateCustomMovement

Event for implementing custom character movement mode. Called by CharacterMovement if MovementMode is set to Custom.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClientCheatWalk

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientCheatFly

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClientCheatGhost

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RootMotionDebugClientPrintOnScreen

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InString | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_RootMotion

Handles replicated root motion properties on simulated proxies and position correction.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlayingRootMotion

true if we are playing Root Motion right now

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlayingNetworkedRootMotionMontage

true if we are playing Root Motion right now, through a Montage with RootMotionMode == ERootMotionMode::RootMotionFromMontagesOnly.
	  This means code path for networked root motion is enabled.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAnimRootMotionTranslationScale

Returns current value of AnimRootMotionScale

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetReplicateBasedMovement

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInReplicateBasedMovement | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_GeneralCampID

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnReachedJumpApex |  | Broadcast when Character's jump reaches its apex. Needs CharacterMovement->bNotifyApex = true |
| MovementModeChangedDelegate |  | Multicast delegate for MovementMode changing. |
| OnCharacterMovementUpdated |  | Event triggered at the end of a CharacterMovementComponent movement update.<br>	  This is the preferred event to use rather than the Tick event when performing custom updates to CharacterMovement properties based on the current state.<br>	  This is mainly due to the nature of network updates, where client corrections in position from the server can cause multiple iterations of a movement update,<br>	  which allows this event to update as well, while a Tick event would not. |

## Language

cpp

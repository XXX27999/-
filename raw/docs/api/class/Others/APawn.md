# APawn

Pawn is the base class of all actors that can be possessed by players or AI.
  They are the physical representations of players and creatures in a level.

## Parents

- [AActor](./AActor.md)
- INavAgentInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bUseControllerRotationPitch | `bool` | If true, this Pawn's pitch will be updated to match the Controller's ControlRotation pitch, if controlled by a PlayerController. |
| bUseControllerRotationYaw | `bool` | If true, this Pawn's yaw will be updated to match the Controller's ControlRotation yaw, if controlled by a PlayerController. |
| bUseControllerRotationRoll | `bool` | If true, this Pawn's roll will be updated to match the Controller's ControlRotation roll, if controlled by a PlayerController. |
| bCanAffectNavigationGeneration | `uint32` | If set to false (default) given pawn instance will never affect navigation generation.<br>	 	Setting it to true will result in using regular AActor's navigation relevancy<br>	 	calculation to check if this pawn instance should affect navigation generation<br>	 	Use SetCanAffectNavigationGeneration to change this value at runtime.<br>	 	Note that modifying this value at runtime will result in any navigation change only if runtime navigation generation is enabled. |
| bUseViewTranslatedTransform | `uint8` |  |
| BaseEyeHeight | `float` | Base eye height above collision center. |
| AutoPossessPlayer | `TEnumAsByte < EAutoReceiveInput :: Type >` | Determines which PlayerController, if any, should automatically possess the pawn when the level starts or when the pawn is spawned.<br>	  @see AutoPossessAI |
| AutoPossessAI | [EAutoPossessAI](../../cppenum/E/EA/EAutoPossessAI.md) | Determines when the Pawn creates and is possessed by an AI Controller (on level start, when spawned, etc).<br>	  Only possible if AIControllerClass is set, and ignored if AutoPossessPlayer is enabled.<br>	  @see AutoPossessPlayer |
| AIControllerClass | `TSubclassOf < AController >` | Default class to use when pawn is controlled by AI. |
| PlayerState | `APlayerState *` | If Pawn is possessed by a player, points to his playerstate.  Needed for network play as controllers are not replicated to clients. |
| RemoteViewPitch | `uint8` | Replicated so we can see where remote clients are looking. |
| LastHitBy | `AController *` | Controller of the last Actor that caused us damage. |
| Controller | `AController *` | Controller currently possessing this Actor |
| ControlInputVector | [FVector](../../cppstruct/F/FV/FVector.md) | Accumulated control input vector, stored in world space. This is the pending input, which is cleared (zeroed) once consumed.<br>	  @see GetPendingMovementInputVector(), AddMovementInput() |
| LastControlInputVector | [FVector](../../cppstruct/F/FV/FVector.md) | The last control input vector that was processed by ConsumeMovementInputVector().<br>	  @see GetLastMovementInputVector() |

## Functions

### GetMovementComponent

Return our PawnMovementComponent, if we have one. By default, returns the first PawnMovementComponent found. Native classes that create their own movement component should override this method for more efficiency.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMeshComponent

Return our Mesh, if we have one. By default, returns the first MeshComponent found. Native classes that create their own mesh component should override this method for more efficiency.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetUseViewTranslatedTransform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewUseViewTranslatedTransform | `bool` |  |

**Return**

- Type: 
- Description: _None_

### PawnMakeNoise

Inform AIControllers that you've made a noise they might hear (they are sent a HearNoise message if they have bHearNoises==true)
	  The instigator of this sound is the pawn which is used to call MakeNoise.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Loudness | `float` | - is the relative loudness of this noise (range 0.0 to 1.0). Directly affects the hearing range specified by the AI's HearingThreshold. |
| NoiseLocation | `FVector` | - Position of noise source. If zero vector, use the actor's location. |
| bUseNoiseMakerLocation | `bool` | - If true, use the location of the NoiseMaker rather than NoiseLocation. If false, use NoiseLocation. |
| NoiseMaker | `AActor *` | - Which actor is the source of the noise. Not to be confused with the Noise Instigator, which is responsible for the noise (and is the pawn on which this function is called). If not specified, the pawn instigating the noise will be used as the NoiseMaker |

**Return**

- Type: 
- Description: _None_

### GetMovementBaseActor

Gets the owning actor of the Movement Base Component on which the pawn is standing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Pawn | `APawn *` |  |

**Return**

- Type: 
- Description: _None_

### IsControlled

See if this actor is currently being controlled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetController

Returns controller for this actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetControlRotation

Get the rotation of the Controller, often the 'view' rotation of this Pawn.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Controller

Called when Controller is replicated

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UseControllerRotationYaw

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_PlayerState

PlayerState Replication Notification Callback

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetCanAffectNavigationGeneration

Use SetCanAffectNavigationGeneration to change this value at runtime.
	 	Note that calling this function at runtime will result in any navigation change only if runtime navigation generation is enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewValue | `bool` |  |
| bForceUpdate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetNavAgentLocation

Basically retrieved pawn's location on navmesh

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceivePossessed

Event called when the Pawn is possessed by a Controller (normally only occurs on the serverstandalone).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewController | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveUnpossessed

Event called when the Pawn is no longer possessed by a Controller.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OldController | `AController *` |  |

**Return**

- Type: 
- Description: _None_

### IsLocallyControlled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlayerControlled

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetBaseAimRotation

Return the aim rotation for the Pawn.
	  If we have a controller, by default we aim at the player's 'eyes' direction
	  that is by default the Pawn rotation for AI, and camera (crosshair) rotation for human players.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DetachFromControllerPendingDestroy

Call this function to detach safely pawn from its controller, knowing that we will be destroyed soon.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SpawnDefaultController

Spawn default controller for this Pawn, and get possessed by it.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddMovementInput

Add movement input along the given world direction vector (usually normalized) scaled by 'ScaleValue'. If ScaleValue < 0, movement will be in the opposite direction.
	  Base Pawn classes won't automatically apply movement, it's up to the user to do so in a Tick event. Subclasses such as Character and DefaultPawn automatically handle this input and move.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldDirection | `FVector` | Direction in world space to apply input |
| ScaleValue | `float` | Scale to apply to input. This can be used for analog input, ie a value of 0.5 applies half the normal value, while -1.0 would reverse the direction. |
| bForce | `bool` | If true always add the input, ignoring the result of IsMoveInputIgnored(). |

**Return**

- Type: 
- Description: _None_

### GetPendingMovementInputVector

Return the pending input vector in world space. This is the most up-to-date value of the input vector, pending ConsumeMovementInputVector() which clears it,
	  Usually only a PawnMovementComponent will want to read this value, or the Pawn itself if it is responsible for movement.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLastMovementInputVector

Return the last input vector in world space that was processed by ConsumeMovementInputVector(), which is usually done by the Pawn or PawnMovementComponent.
	  Any user that needs to know about the input that last affected movement should use this function.
	  For example an animation update would want to use this, since by default the order of updates in a frame is:
	  PlayerController (device input) -> MovementComponent -> Pawn -> Mesh (animations)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ConsumeMovementInputVector

Returns the pending input vector and resets it to zero.
	  This should be used during a movement update (by the Pawn or PawnMovementComponent) to prevent accumulation of control input between frames.
	  Copies the pending input vector to the saved input vector (GetLastMovementInputVector()).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddControllerPitchInput

Add input (affecting Pitch) to the Controller's ControlRotation, if it is a local PlayerController.
	  This value is multiplied by the PlayerController's InputPitchScale value.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Val | `float` | Amount to add to Pitch. This value is multiplied by the PlayerController's InputPitchScale value. |

**Return**

- Type: 
- Description: _None_

### AddControllerYawInput

Add input (affecting Yaw) to the Controller's ControlRotation, if it is a local PlayerController.
	  This value is multiplied by the PlayerController's InputYawScale value.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Val | `float` | Amount to add to Yaw. This value is multiplied by the PlayerController's InputYawScale value. |

**Return**

- Type: 
- Description: _None_

### AddControllerRollInput

Add input (affecting Roll) to the Controller's ControlRotation, if it is a local PlayerController.
	  This value is multiplied by the PlayerController's InputRollScale value.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Val | `float` | Amount to add to Roll. This value is multiplied by the PlayerController's InputRollScale value. |

**Return**

- Type: 
- Description: _None_

### IsMoveInputIgnored

Helper to see if move input is ignored. If our controller is a PlayerController, checks Controller->IsMoveInputIgnored().

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### LaunchPawn

(Deprecated) Launch Character with LaunchVelocity

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LaunchVelocity | `FVector` |  |
| bXYOverride | `bool` |  |
| bZOverride | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetMovementInputVector

(Deprecated) Return the input vector in world space.

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
| OnControllerArrived |  |  |
| OnPawnClientRestart |  |  |

## Language

cpp

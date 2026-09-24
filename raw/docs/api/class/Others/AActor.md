# AActor

Actor is the base class for an Object that can be placed or spawned in a level.
  Actors may contain a collection of ActorComponents, which can be used to control how actors move, how they are rendered, etc.
  The other main function of an Actor is the replication of properties and function calls across the network during play.

  @see UActorComponent

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PrimaryActorTick | `FActorTickFunction` | Primary Actor tick function, which calls TickActor().<br>	  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.<br>	  @see AddTickPrerequisiteActor(), AddTickPrerequisiteComponent() |
| CustomTimeDilation | `float` | Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick. |
| bAllowBPReceiveTickEvent | `bool` | If true, bp tick will be called , otherwise skipped |
| TickAdapterInterval | `uint8` |  |
| bTickAdapterRqrMainFrame | `uint8` |  |
| bEnableTickAdapter | `uint8` |  |
| bSupportSuspendTick | `uint8` |  |
| bEnableFirstTickGroup | `uint8` |  |
| bHidden | `uint8` | Allows us to only see this Actor in the Editor, and not in the actual game.<br>	  @see SetActorHiddenInGame() |
| bConsideredHidden | `uint8` |  |
| bNetTemporary | `uint8` | If true, when the actor is spawned it will be sent to the client but receive no further replication updates from the server afterwards. |
| bNetStartup | `uint8` | If true, this actor was loaded directly from the map, and for networking purposes can be addressed by its full path name |
| bOnlyRelevantToOwner | `uint8` | If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed. |
| bOwningSpecificNetConsideration | `uint8` | If true, this actor is considered for replication in an owning-specific semantics. |
| bRegionBasedNetConsideration | `uint8` | If true, this actor is considered for replication in region-based semantics. |
| bMRegionBasedNetConsideration | `uint8` | If true, this actor is considered for replication in Mregion-based semantics. |
| bMRegionStatic | `uint8` |  |
| bFastDistBasedNetRelevancy | `uint8` | If true, this actor is checked for relevancy by fast distance-based calculation. |
| bGroupBasedNetRelevancy | `uint8` | If true, this actor is checked for relevancy by relevancy group first. |
| bLazyNetReplication | `uint8` | If true, this actor is only replicated by calling ForceNetUpdate. |
| bClientSimulatedRelevancy | `uint8` | NOTE: Mark "Client Simulated Relevancy" for ob  replay<br>	 @see SetActorSimulatedRelevancy()<br>	 @see OnActorSimulatedRelevant() |
| bCheckAllRelyOnAttachment | `uint8` |  |
| bAlwaysRelevant | `uint8` | Always relevant for network (overrides bOnlyRelevantToOwner). |
| bForceOwnedMeshAlwaysRefreshBones | `uint8` |  |
| bTearOff | `uint8` | If true, this actor is no longer replicated to new clients, and is "torn off" (becomes a ROLE_Authority) on clients to which it was being replicated.<br>	  @see TornOff() |
| bExchangedRoles | `uint8` | Whether we have already exchanged RoleRemoteRole on the client, as when removing then re-adding a streaming level.<br>	  Causes all initialization to be performed again even though the actor may not have actually been reloaded. |
| bNetLoadOnClient | `uint8` | This actor will be loaded on network clients during map load |
| bNetUseOwnerRelevancy | `uint8` | If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority |
| bBlockInput | `uint8` | If true, all input on the stack below this actor will not be considered |
| bCanBeBaseForCharacter | `uint8` | If true, all input on the stack below this actor will not be considered |
| bAllowTickBeforeBeginPlay | `uint8` | Whether we allow this Actor to tick before it receives the BeginPlay event.<br>	  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.<br>	  This Actor must be able to tick for this setting to be relevant. |
| bCustomHandlingNetworkSubobjectDeletion | `uint8` |  |
| bReplicates | `uint8` | If true, this actor will replicate to remote machines<br>	  @see SetReplicates() |
| RemoteRole | `TEnumAsByte < enum ENetRole >` | Describes how much control the remote machine has over the actor. |
| Owner | `AActor *` | Owner of this Actor, used primarily for replication (bNetUseOwnerRelevancy & bOnlyRelevantToOwner) and visibility (PrimitiveComponent bOwnerNoSee and bOnlyOwnerSee)<br>	  @see SetOwner(), GetOwner() |
| bReplicateMovement | `uint8` | If true, replicate movementlocation related properties.<br>	  Actor must also be set to replicate.<br>	  @see SetReplicates() |
| bActorEnableCollision | `uint8` | Enables any collision on this actor.<br>	  @see SetActorEnableCollision(), GetActorEnableCollision() |
| bDoNotNetAsyncDestroy | `uint8` |  |
| bEnableDeferredConstructComponent | `uint8` |  |
| bUseSpawnReplicatedActorMaxFrameDelayFromConfig | `uint8` |  |
| PendingConstructComponents | `TArray < FDeferedComponentUnit >` |  |
| PreSCSComponentsBeforeDeferContruction | `TArray < UActorComponent * >` |  |
| AsyncReplicatedActorSpawnDistA | `float` |  |
| AsyncReplicatedActorSpawnDistB | `float` |  |
| SpawnReplicatedActorMaxFrameDelayFromConfig | `int32` |  |
| ScriptNetworkReplicatedPropertyWrapper | `FScriptNetworkReplicatedPropertyWrapper` |  |
| NetDriverName | `FName` | Used to specify the net driver to replicate on (NAME_None \|\| NAME_GameNetDriver is the default net driver) |
| ReplicatedMovement | [FRepMovement](../../cppstruct/F/FR/FRepMovement.md) | Used for replication of our RootComponent's position and velocity |
| InitialLifeSpan | `float` | How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun. |
| AttachmentReplication | [FRepAttachment](../../cppstruct/F/FR/FRepAttachment.md) | Used for replicating attachment of this actor's RootComponent to another actor.<br>	  This is filled in via GatherCurrentMovement() when the RootComponent has an AttachParent. |
| Role | `TEnumAsByte < enum ENetRole >` | Describes how much control the local machine has over the actor. |
| NetDormancy | `TEnumAsByte < enum ENetDormancy >` | Dormancy setting for actor to take itself off of the replication list without being destroyed on clients. |
| AutoReceiveInput | `TEnumAsByte < EAutoReceiveInput :: Type >` | Automatically registers this actor to receive input from a player. |
| InputPriority | `int32` | The priority of this input component when pushed in to the stack. |
| InputComponent | `UInputComponent *` | Component that handles input for this actor, if input is enabled. |
| NetCullDistanceSquared | `float` | Square of the max distance from the client's viewpoint that this actor is relevant and will be replicated. |
| NetCullFactorSquared | `float` | NetCullDistanceSquared Factor for Connection |
| OBRelevantFactor | `float` |  |
| NetTag | `int32` | Internal - used by UWorld::ServerTickClients() |
| NetConsiderFrequency | `float` | How often (per second) this actor enters consider list, should be greater than or equal to NetUpdateFrequency |
| NetUpdateFrequency | `float` | How often (per second) this actor will be checked for replication, used to determine NetUpdateTime |
| MinNetUpdateFrequency | `float` | Used to determine what rate to throttle down to when replicated properties are changing infrequently |
| NetUpdateJumpFrame | `int32` |  |
| NetPriority | `float` | Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate |
| bAutoDestroyWhenFinished | `uint8` | If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight. |
| bCanBeDamaged | `uint8` | Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.<br>	  @see TakeDamage(), ReceiveDamage() |
| bCanNotifyDamager | `uint8` | Whether this actor can Notify damager. Must be true for notify damager events (PreDamageOther) to be called.<br>	  @see TakeDamage(), PreDamageOther() |
| bRepParentUpdatePhx | `uint8` |  |
| bActorIsBeingDestroyed | `uint8` | Set when actor is about to be deleted. |
| bCollideWhenPlacing | `uint8` | This actor collides with the world when placing in the editor, even if RootComponent collision is disabled. Does not affect spawning, @see SpawnCollisionHandlingMethod |
| bFindCameraComponentWhenViewTarget | `uint8` | If true, this actor should search for an owned camera component to view through when used as a view target. |
| bRelevantForNetworkReplays | `uint8` | If true, this actor will be replicated to network replays (default is true) |
| bForcedRelevancyCheckForReplay | `uint8` |  |
| bLowUpdateRateForReplay | `uint8` |  |
| bGenerateOverlapEventsDuringLevelStreaming | `uint8` | If true, this actor will generate overlap events when spawned as part of level streaming. You might enable this is in the case where a streaming level loads around an actor and you want overlaps to trigger. |
| bCanCachedInWorldSpecialActorList | `uint8` |  |
| bShouldDumpCallstackWhenMovingfast | `uint8` |  |
| bCanBeInCluster | `uint8` | If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance |
| bAllowReceiveTickEventOnDedicatedServer | `uint8` | If false, the Blueprint ReceiveTick() event will be disabled on dedicated servers.<br>	  @see AllowReceiveTickEventOnDedicatedServer() |
| bActorSeamlessTraveled | `uint8` | Indicates the actor was pulled through a seamless travel. |
| bIgnoresOriginShifting | `uint8` | Whether this actor should not be affected by world origin shifting. |
| bEnableAutoLODGeneration | `uint8` | If true, and if World setting has bEnableHierarchicalLOD equal to true, then it will generate LODActor from groups of clustered Actor |
| SpawnCollisionHandlingMethod | [ESpawnActorCollisionHandlingMethod](../../cppenum/E/ES/ESpawnActorCollisionHandlingMethod.md) | Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here. |
| CollisionCheckMoveDisStep | `float` |  |
| CollisionCheckMoveDegreeStep | `float` |  |
| CollisionCheckCircleRadius | `float` |  |
| Instigator | `APawn *` | Pawn responsible for damage caused by this actor. |
| Children | `TArray < AActor * >` | Array of Actors whose Owner is this actor |
| RootComponent | `USceneComponent *` | Collision primitive that defines the transform (location, rotation, scale) of this Actor. |
| ControllingMatineeActors | `TArray < AMatineeActor * >` | The matinee actors that control this actor. |
| Layers | `TArray < FName >` | Layer's the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling. |
| ParentComponent | `TWeakObjectPtr < UChildActorComponent >` | The UChildActorComponent that owns this Actor. |
| Tags | `TArray < FName >` | Array of tags that can be used for grouping and categorizing. |
| DynamicTags | `TArray < FName >` |  |
| BlueprintCreatedComponents | `TArray < UActorComponent * >` | Array of ActorComponents that are created by blueprints and serialized per-instance. |
| InstanceComponents | `TArray < UActorComponent * >` | Array of ActorComponents that have been added by the user on a per-instance basis. |
| BackupRestoreIdentifier | `int64` |  |
| NeedsBackupStates | `uint8` |  |
| bSkipNewDuplicateOwnedComponents | `uint8` | If you call CreateComponentFromTemplate on an actor which already owns a component with the same name, problem comes out<br>	  Optimized version will return the existing component, but not duplicate a new one, in this case, setting this switch to true is necessary |
| bCanBeNetContainer | `uint8` |  |
| bDonotAsSubActor | `uint8` |  |
| DeformEffectType | `TEnumAsByte < enum EDeformEffectType >` |  |
| bBlockLandscapeDeform | `bool` | If this actor will block any overlap deform. |
| bRemoveStaticChildActorComp | `bool` |  |
| InputConsumeOption_DEPRECATED | `TEnumAsByte < enum EInputConsumeOptions >` |  |
| ExportActorInLevel | `bool` | 在编辑器获取level里面actor的位置和朝向, 通过命令行方式导出到一个lua表格. feishen, 20210406 |
| PivotOffset | [FVector](../../cppstruct/F/FV/FVector.md) | Local space pivot offset for the actor |
| ParentComponentActor_DEPRECATED | `TWeakObjectPtr < AActor >` | The Actor that owns the UChildActorComponent that owns this Actor. |
| GroupActor | `AActor *` | The group this actor is a part of. |
| SpriteScale | `float` | The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games). |
| ActorLabel | `FString` | The friendly name for this actor, displayed in the editor.  You should always use AActor::GetActorLabel() to access the actual label to display,<br>	  and call AActor::SetActorLabel() or FActorLabelUtilities::SetActorLabelUnique() to change the label.  Never set the label directly. |
| FolderPath | `FName` | The folder path of this actor in the world (empty=root,  separated) |
| bActorLabelEditable | `uint8` |  |
| bHiddenEd | `uint8` | Whether this actor is hidden within the editor viewport. |
| bEditable | `uint8` | Whether the actor can be manipulated by editor operations. |
| bListedInSceneOutliner | `uint8` | Whether this actor should be listed in the scene outliner. |
| bIsEditorPreviewActor | `uint8` | True if this actor is the preview actor dragged out of the content browser |
| bHiddenEdLayer | `uint8` | Whether this actor is hidden by the layer browser. |
| bHiddenEdTemporary | `uint8` | Whether this actor is temporarily hidden within the editor; used for showhideetc functionality wo dirtying the actor. |
| bHiddenEdLevel | `uint8` | Whether this actor is hidden by the level browser. |
| bLockLocation | `uint8` | If true, prevents the actor from being moved in the editor viewport. |
| ReorganizationTags | [FReorganizationTagsContainer](../../cppstruct/F/FR/FReorganizationTagsContainer.md) | Reorganization tags for Level Partition system |
| HiddenEditorViews | `uint64` | Bitflag to represent which views this actor is hidden in, via per-view layer visibility. |
| bActorCoastline | `uint8` |  |

## Functions

### GetToString

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForceOwnedMeshAlwaysRefreshBones

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bAlwaysRefreshBones | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicateMovement

Called on client when updated bReplicateMovement value is received for this actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TearOff

Networking - Server - TearOff this actor to stop replication to clients. Will set bTearOff to true.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Role

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_RemoteRole

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Hidden

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_TearOff

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_CanBeDamaged

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Owner

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TickConstructComponentWithTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OneFrameConstructTimeMS | `float` |  |
| bCreateImmediately | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnRep_ScriptNetworkReplicatedPropertyWrapper

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CallSubObjectLuaOnRep

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### ServerSendScriptNetworkRemoteContent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `FScriptNetworkRemoteContent &` |  |

**Return**

- Type: 
- Description: _None_

### ServerSendScriptNetworkRemoteContent_Unreliable

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `FScriptNetworkRemoteContent &` |  |

**Return**

- Type: 
- Description: _None_

### ClientSendScriptNetworkRemoteContent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `FScriptNetworkRemoteContent &` |  |

**Return**

- Type: 
- Description: _None_

### ClientSendScriptNetworkRemoteContent_Unreliable

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `FScriptNetworkRemoteContent &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveScriptNetworkRemoteContent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Content | `FScriptNetworkRemoteContent &` |  |

**Return**

- Type: 
- Description: _None_

### SetReplicates

Set whether this actor replicates to network clients. When this actor is spawned on the server it will be sent to clients as well.
	  Properties flagged for replication will update on clients if they change on the server.
	  Internally changes the RemoteRole property and handles the cases where the actor needs to be added to the network actor list.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInReplicates | `bool` | Whether this Actor replicates to network clients. |

**Return**

- Type: 
- Description: _None_

### SetEncSceneActor

Set whether this Actor is an encrypted scene Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInEncSceneActor | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsEncSceneActor

Get whether this Actor is an encrypted scene Actor

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
| bInReplicateMovement | `bool` | Whether this Actor's movement replicates to clients. |

**Return**

- Type: 
- Description: _None_

### GetLocalRole

Returns how much control the local machine has over this actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRemoteRole

Returns how much control the remote machine has over this actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetRole

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_AttachmentReplication

Called on client when updated AttachmentReplication value is received for this actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Instigator

Called on clients when Instigator is replicated.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddDynamicTag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | `FName` |  |

**Return**

- Type: 
- Description: _None_

### RemoveDynamicTag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | `FName` |  |

**Return**

- Type: 
- Description: _None_

### EnableInput

Pushes this actor on to the stack of input being handled by a PlayerController.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` | The PlayerController whose input events we want to receive. |

**Return**

- Type: 
- Description: _None_

### GetInputAxisValue

Gets the value of the input axis if input is enabled for this actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InputAxisName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### DisableInput

Removes this actor from the stack of input being handled by a PlayerController.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PlayerController | `APlayerController *` | The PlayerController whose input events we no longer want to receive. If null, this actor will stop receiving input from all PlayerControllers. |

**Return**

- Type: 
- Description: _None_

### GetInputAxisKeyValue

Gets the value of the input axis key if input is enabled for this actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InputAxisKey | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetInputVectorAxisValue

Gets the value of the input axis key if input is enabled for this actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InputAxisKey | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### GetInstigator

Returns the instigator for this actor, or NULL if there is none.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetInstigatorController

Returns the instigator's controller for this actor, or NULL if there is none.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetTransform

Get the actor-to-world transform.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_GetActorLocation

Returns the location of the RootComponent of this Actor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_SetActorLocation

Move the Actor to the specified location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` | The new location to move the Actor to. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | The hit result from the move if swept. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_GetActorRotation

Returns rotation of the RootComponent of this Actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActorForwardVector

Get the forward (X) vector (length 1.0) from this Actor, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActorUpVector

Get the up (Z) vector (length 1.0) from this Actor, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActorRightVector

Get the right (Y) vector (length 1.0) from this Actor, in world space.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetActorBounds

Returns the bounding box of all components that make up this Actor (excluding ChildActorComponents).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bOnlyCollidingComponents | `bool` | If true, will only return the bounding box for components with collision enabled. |
| Origin | `FVector &` |  |
| BoxExtent | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### K2_GetRootComponent

Returns the RootComponent of this Actor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetVelocity

Returns velocity (in cms (Unreal Unitssecond) of the rootcomponent if it is either using physics or has an associated MovementComponent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_SetActorRotation

Set the Actor's rotation instantly to the specified rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRotation | `FRotator` | The new rotation for the Actor. |
| bTeleportPhysics | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetActorLocationAndRotation

Move the actor instantly to the specified location and rotation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` | The new location to teleport the Actor to. |
| NewRotation | `FRotator` | The new rotation for the Actor. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | The hit result from the move if swept. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### SetActorScale3D

Set the Actor's world-space scale.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewScale3D | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetActorScale3D

Returns the Actor's world-space scale.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDistanceTo

Returns the distance from this Actor to OtherActor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetSquaredDistanceTo

Returns the squared distance from this Actor to OtherActor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetHorizontalDistanceTo

Returns the distance from this Actor to OtherActor, ignoring Z.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetVerticalDistanceTo

Returns the distance from this Actor to OtherActor, ignoring XY.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetDotProductTo

Returns the dot product from this Actor to OtherActor. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### GetHorizontalDotProductTo

Returns the dot product from this Actor to OtherActor, ignoring Z. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### K2_AddActorWorldOffset

Adds a delta to the location of this actor in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaLocation | `FVector` | The change in location. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` | The hit result from the move if swept. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddActorWorldRotation

Adds a delta to the rotation of this actor in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaRotation | `FRotator` | The change in rotation. |
| bSweep | `bool` | Whether to sweep to the target rotation (not currently supported for rotation). |
| SweepHitResult | `FHitResult &` | The hit result from the move if swept. |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddActorWorldTransform

Adds a delta to the transform of this actor in world space. Scale is unchanged.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTransform | `FTransform &` |  |
| bSweep | `bool` |  |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_SetActorTransform

Set the Actors transform to the specified one.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTransform | `FTransform &` | The new transform. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddActorLocalOffset

Adds a delta to the location of this component in its local reference frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaLocation | `FVector` |  |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddActorLocalRotation

Adds a delta to the rotation of this component in its local reference frame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaRotation | `FRotator` | The change in rotation in local space. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_AddActorLocalTransform

Adds a delta to the transform of this component in its local reference frame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTransform | `FTransform &` | The change in transform in local space. |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetActorRelativeLocation

Set the actor's RootComponent to the specified relative location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRelativeLocation | `FVector` | New relative location of the actor's root component |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetActorRelativeRotation

Set the actor's RootComponent to the specified relative rotation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRelativeRotation | `FRotator` | New relative rotation of the actor's root component |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### K2_SetActorRelativeTransform

Set the actor's RootComponent to the specified relative transform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRelativeTransform | `FTransform &` | New relative transform of the actor's root component |
| bSweep | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| SweepHitResult | `FHitResult &` |  |
| bTeleport | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Return**

- Type: 
- Description: _None_

### SetActorRelativeScale3D

Set the actor's RootComponent to the specified relative scale 3d

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewRelativeScale | [FVector](../../cppstruct/F/FV/FVector.md) | New scale to set the actor's RootComponent to |

**Return**

- Type: 
- Description: _None_

### GetActorRelativeScale3D

Return the actor's relative scale 3d

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActorHiddenInGame

Sets the actor to be hidden in the game

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewHidden | `bool` | Whether or not to hide the actor and all its components |

**Return**

- Type: 
- Description: _None_

### SetActorConsideredHidden

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewHidden | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetActorSimulatedRelevancy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsRelevant | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnActorSimulatedRelevant

NOTE : Callback of Check Actor Relevancy in Client for ob or replay

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsRelevant | `bool` | : Whether or not relevant for replay view target |

**Return**

- Type: 
- Description: _None_

### SetActorEnableCollision

Allows enablingdisabling collision for the whole actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewActorEnableCollision | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetActorEnableCollision

Get current state of collision for the whole actor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_DestroyActor

Destroy the actor

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasAuthority

Returns whether this actor has network authority

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddComponent

Creates a new component and assigns ownership to the Actor this is
	  called for. Automatic attachment causes the first component created to
	  become the root, and all subsequent components to be attached under that
	  root. When bManualAttachment is set, automatic attachment is
	  skipped and it is up to the user to attach the resulting component (or
	  set it up as the root) themselves.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TemplateName | `FName` | The name of the Component Template to use. |
| bManualAttachment | `bool` | Whether manual or automatic attachment is to be used |
| RelativeTransform | `FTransform &` | The relative transform between the new component and its attach parent (automatic only) |
| ComponentTemplateContext | `UObject *` | Optional UBlueprintGeneratedClass reference to use to find the template in. If null (or not a BPGC), component is sought in this Actor's class |

**Return**

- Type: 
- Description: _None_

### K2_DestroyComponent

DEPRECATED - Use Component::DestroyComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Component | `UActorComponent *` |  |

**Return**

- Type: 
- Description: _None_

### K2_AttachRootComponentTo

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InParent | `USceneComponent *` |  |
| InSocketName | `FName` |  |
| AttachLocationType | `EAttachLocation :: Type` | Type of attachment, AbsoluteWorld to keep its world position, RelativeOffset to keep the object's relative offset and SnapTo to snap to the new parent. |
| bWeldSimulatedBodies | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_AttachToComponent

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Parent | `USceneComponent *` | Parent to attach to. |
| SocketName | `FName` | Optional socket to attach to on the parent. |
| LocationRule | `EAttachmentRule` |  |
| RotationRule | `EAttachmentRule` |  |
| ScaleRule | `EAttachmentRule` |  |
| bWeldSimulatedBodies | `bool` | Whether to weld together simulated physics bodies. |

**Return**

- Type: 
- Description: _None_

### K2_AttachRootComponentToActor

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InParentActor | `AActor *` |  |
| InSocketName | `FName` |  |
| AttachLocationType | `EAttachLocation :: Type` | Type of attachment, AbsoluteWorld to keep its world position, RelativeOffset to keep the object's relative offset and SnapTo to snap to the new parent. |
| bWeldSimulatedBodies | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_AttachToActor

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParentActor | `AActor *` | Actor to attach this actor's RootComponent to |
| SocketName | `FName` | Socket name to attach to, if any |
| LocationRule | `EAttachmentRule` | How to handle translation when attaching. |
| RotationRule | `EAttachmentRule` | How to handle rotation when attaching. |
| ScaleRule | `EAttachmentRule` | How to handle scale when attaching. |
| bWeldSimulatedBodies | `bool` | Whether to weld together simulated physics bodies. |

**Return**

- Type: 
- Description: _None_

### SnapRootComponentTo

Snap the RootComponent of this Actor to the supplied Actor's root component, optionally at a named socket. It is not valid to call this on components that are not Registered.
	   If InSocketName == NAME_None, it will attach to origin of the InParentActor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InParentActor | `AActor *` |  |
| InSocketName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### DetachRootComponentFromParent

Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bMaintainWorldPosition | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_DetachFromActor

Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LocationRule | `EDetachmentRule` | How to handle translation when detaching. |
| RotationRule | `EDetachmentRule` | How to handle rotation when detaching. |
| ScaleRule | [EDetachmentRule](../../cppenum/E/ED/EDetachmentRule.md) | How to handle scale when detaching. |

**Return**

- Type: 
- Description: _None_

### ActorHasTag

See if this actor contains the supplied tag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetActorTimeDilation

Get CustomTimeDilation - this can be used for input control or speed control for slomo.
	  We don't want to scale input globally because input can be used for UI, which do not care for TimeDilation.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddTickPrerequisiteActor

Make this actor tick after PrerequisiteActor. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrerequisiteActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### AddTickPrerequisiteComponent

Make this actor tick after PrerequisiteComponent. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrerequisiteComponent | `UActorComponent *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveTickPrerequisiteActor

Remove tick dependency on PrerequisiteActor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrerequisiteActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveTickPrerequisiteComponent

Remove tick dependency on PrerequisiteComponent.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrerequisiteComponent | `UActorComponent *` |  |

**Return**

- Type: 
- Description: _None_

### GetTickableWhenPaused

Gets whether this actor can tick when paused.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTickableWhenPaused

Sets whether this actor can tick when paused.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bTickableWhenPaused | `bool` |  |

**Return**

- Type: 
- Description: _None_

### MakeMIDForMaterial

Allocate a MID for a given parent material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Parent | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### GetGameTimeSinceCreation

The number of seconds (in game time) since this Actor was created, relative to Get Game Time In Seconds.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MakeNoise

Trigger a noise caused by a given Pawn, at a given location.
	  Note that the NoiseInstigator Pawn MUST have a PawnNoiseEmitterComponent for the noise to be detected by a PawnSensingComponent.
	  Senders of MakeNoise should have an Instigator if they are not pawns, or pass a NoiseInstigator.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Loudness | `float` | The relative loudness of this noise. Usual range is 0 (no noise) to 1 (full volume). If MaxRange is used, this scales the max range, otherwise it affects the hearing range specified by the sensor. |
| NoiseInstigator | `APawn *` | Pawn responsible for this noise. Uses the actor's Instigator if NoiseInstigator=NULL |
| NoiseLocation | `FVector` | Position of noise source. If zero vector, use the actor's location. |
| MaxRange | `float` | Max range at which the sound may be heard. A value of 0 indicates no max range (though perception may have its own range). Loudness scales the range. (Note: not supported for legacy PawnSensingComponent, only for AIPerception) |
| Tag | `FName` | Identifier for the noise. |

**Return**

- Type: 
- Description: _None_

### ReceiveBeginPlay

Event when play begins for this actor.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveReInitForReplay

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveFastForwardFinishedForReplay

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveActorSimulatedRelevant

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsRelevant | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsActorBeingDestroyed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveAnyDamage

Event when this actor takes ANY damage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Damage | `float` |  |
| DamageType | `UDamageType *` |  |
| InstigatedBy | `AController *` |  |
| DamageCauser | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveRadialDamage

Event when this actor takes RADIAL damage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamageReceived | `float` |  |
| DamageType | `UDamageType *` |  |
| Origin | `FVector` |  |
| HitInfo | `FHitResult &` |  |
| InstigatedBy | `AController *` |  |
| DamageCauser | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceivePointDamage

Event when this actor takes POINT damage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Damage | `float` |  |
| DamageType | `UDamageType *` |  |
| HitLocation | `FVector` |  |
| HitNormal | `FVector` |  |
| HitComponent | `UPrimitiveComponent *` |  |
| BoneName | `FName` |  |
| ShotFromDirection | `FVector` |  |
| InstigatedBy | `AController *` |  |
| DamageCauser | `AActor *` |  |
| HitInfo | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveTick

Event called every frame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorBeginOverlap

Event when this actor overlaps another actor, for example a player walking into a trigger.
	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorEndOverlap

Event when an actor no longer overlaps another actor, and they have separated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OtherActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorBeginCursorOver

Event when this actor has the mouse moved over it with the clickable interface.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveActorEndCursorOver

Event when this actor has the mouse moved off of it with the clickable interface.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveActorOnClicked

Event when this actor is clicked by the mouse when using the clickable interface.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ButtonPressed | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorOnReleased

Event when this actor is under the mouse when left mouse button is released while using the clickable interface.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ButtonReleased | `FKey` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorOnInputTouchBegin

Event when this actor is touched when click events are enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorOnInputTouchEnd

Event when this actor is under the finger when untouched when click events are enabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorOnInputTouchEnter

Event when this actor has a finger moved over it with the clickable interface.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveActorOnInputTouchLeave

Event when this actor has a finger moved off of it with the clickable interface.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FingerIndex | `ETouchIndex :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetOverlappingActors

Returns list of actors this actor is overlapping (any component overlapping any component). Does not return itself.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OverlappingActors | `TArray < AActor * > &` | [out] Returned list of overlapping actors |
| ClassFilter | `TSubclassOf < AActor >` | [optional] If set, only returns actors of this class or subclasses |

**Return**

- Type: 
- Description: _None_

### GetOverlappingComponents

Returns list of components this actor is overlapping.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OverlappingComponents | `TArray < UPrimitiveComponent * > &` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveHit

Event when this actor bumps into a blocking object, or blocks another actor that bumps into it.
	  This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
	  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MyComp | `UPrimitiveComponent *` |  |
| Other | `AActor *` |  |
| OtherComp | `UPrimitiveComponent *` |  |
| bSelfMoved | `bool` |  |
| HitLocation | `FVector` |  |
| HitNormal | `FVector` |  |
| NormalImpulse | `FVector` |  |
| Hit | `FHitResult &` |  |

**Return**

- Type: 
- Description: _None_

### SetLifeSpan

Set the lifespan of this actor. When it expires the object will be destroyed. If requested lifespan is 0, the timer is cleared and the actor will not be destroyed.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InLifespan | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetLifeSpan

Get the remaining lifespan of this actor. If zero is returned the actor lives forever.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UserConstructionScript

Construction script, the place to spawn components and do other setup.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveDestroyed

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveEndPlay

Event to notify blueprints this actor is about to be deleted.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndPlayReason | `EEndPlayReason :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetActorTickEnabled

Set this actor's tick functions to be enabled or disabled. Only has an effect if the function is registered
	  This only modifies the tick function on actor itself

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` | Whether it should be enabled or not |

**Return**

- Type: 
- Description: _None_

### IsActorTickEnabled

Returns whether this actor has tick enabled or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActorTickInterval

Sets the tick interval of this actor's primary tick function. Will not enable a disabled tick function. Takes effect on next tick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TickInterval | `float` | The rate at which this actor should be ticking |

**Return**

- Type: 
- Description: _None_

### GetActorTickInterval

Returns the tick interval of this actor's primary tick function

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_ReplicatedMovement

ReplicatedMovement struct replication event

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetOwner

Set the owner of this Actor, used primarily for network replication.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewOwner | `AActor *` | The Actor whom takes over ownership of this Actor |

**Return**

- Type: 
- Description: _None_

### GetOwner

Get the owner of this Actor, used primarily for network replication.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsOverlappingActor

Check whether any component of this Actor is overlapping any component of another Actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Other | `AActor *` | The other Actor to test against |

**Return**

- Type: 
- Description: _None_

### SetNetDormancy

Puts actor in dormant networking state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewDormancy | [ENetDormancy](../../cppenum/E/EN/ENetDormancy.md) |  |

**Return**

- Type: 
- Description: _None_

### FlushNetDormancy

Forces dormant actor to replicate but doesn't change NetDormancy state (i.e., they will go dormant again if left dormant)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsChildActor

Returns whether this Actor was spawned by a child actor component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAllChildActors

Returns a list of all child actors, including children of children

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ChildActors | `TArray < AActor * > &` |  |
| bIncludeDescendants | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetParentComponent

If this Actor was created by a Child Actor Component returns that Child Actor Component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetParentActor

If this Actor was created by a Child Actor Component returns the Actor that owns that Child Actor Component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_TeleportTo

Teleport this actor to a new location. If the actor doesn't fit exactly at the location specified, tries to slightly move it out of walls and such.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DestLocation | `FVector` | The target destination point |
| DestRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | The target rotation at the destination |

**Return**

- Type: 
- Description: _None_

### GetLevelName

Return the ULevel name that this Actor is part of.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAttachParentActor

Walk up the attachment chain from RootComponent until we encounter a different actor, and return it. If we are not attached to a component in a different actor, returns NULL

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAttachParentSocketName

Walk up the attachment chain from RootComponent until we encounter a different actor, and return the socket name in the component. If we are not attached to a component in a different actor, returns NAME_None

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAttachedActors

Find all Actors which are attached directly to a component in this actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutActors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### SetTickGroup

Sets the ticking group for this actor.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTickGroup | [ETickingGroup](../../cppenum/E/ET/ETickingGroup.md) | the new value to assign |

**Return**

- Type: 
- Description: _None_

### CanBeBaseForCharacter

Return true if the given Pawn can be "based" on this actor (ie walk on it).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Pawn | `APawn *` | - The pawn that wants to be based on this actor |

**Return**

- Type: 
- Description: _None_

### GetAnimNotifyStateBoneRetargetAdaptInfoObj

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TryGetBoneRetargetObj

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSourceObj | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### TryGetBoneRetargetObjForNotifyState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetNotifyState | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### InitAnimNotifyStateBoneRetargetInfo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetNotifyState | `UObject *` |  |
| InBoneRetargetObj | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### ClearAnimNotifyStateBoneRetargetAdaptState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetNotifyState | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsAnimNotifyStateBoneRetargetAdaptInitDone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetNotifyState | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### OverrideNotifyAttachMesh

For Bone Retarget Feature End

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetNotifyState | `UObject *` |  |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |
| HasRetarget | `bool` |  |
| IgnoreNewFPPState | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnBecomeViewTarget

Event called when this Actor becomes the view target for the given PlayerController.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PC | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnEndViewTarget

Event called when this Actor is no longer the view target for the given PlayerController.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PC | `APlayerController *` |  |

**Return**

- Type: 
- Description: _None_

### K2_OnReset

Event called when this Actor is reset to its initial state - used when restarting level without reloading.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### WasRecentlyRendered

Returns true if this actor has been rendered "recently", with a tolerance in seconds to define what "recent" means.
	  e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tolerance | `float` | How many seconds ago the actor last render time can be and still count as having been "recently" rendered. |

**Return**

- Type: 
- Description: _None_

### ForceNetRelevant

Forces this actor to be net relevant if it is not already by default

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ForceNetConsider

Force actor enter consider list

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ForceNetComponentUpdate

Force actor's component to be updated to client

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponent | `UActorComponent *` |  |

**Return**

- Type: 
- Description: _None_

### ForceNetUpdate

Force actor to be updated to clients

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PrestreamTextures

Calls PrestreamTextures() for all the actor's meshcomponents.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Seconds | `float` | - Number of seconds to force all mip-levels to be resident |
| bEnableStreaming | `bool` | - Whether to start (true) or stop (false) streaming |
| CinematicTextureGroups | `int32` | - Bitfield indicating which texture groups that use extra high-resolution mips |

**Return**

- Type: 
- Description: _None_

### SetTextureForceResidentFlag

Calls SetTextureForceResidentFlag() for all the actor's meshcomponents.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bForceMiplevelsToBeResident | `bool` | Whether textures should be forced to be resident or not. |

**Return**

- Type: 
- Description: _None_

### GetActorEyesViewPoint

Returns the point of view of the actor.
	  Note that this doesn't mean the camera, but the 'eyes' of the actor.
	  For example, for a Pawn, this would define the eye height location,
	  and view rotation (which is different from the pawn rotation which has a zeroed pitch component).
	  A camera first person view will typically use this view point. Most traces (weapon, AI) will be done from this view point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OutLocation | `FVector &` | - location of view point |
| OutRotation | `FRotator &` | - view rotation of actor. |

**Return**

- Type: 
- Description: _None_

### GetComponentByClass

Script exposed version of FindComponentByClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComponentClass | `TSubclassOf < UActorComponent >` |  |

**Return**

- Type: 
- Description: _None_

### GetComponentsByClass

Gets all the components that inherit from the given class.
	Currently returns an array of UActorComponent which must be cast to the correct type.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComponentClass | `TSubclassOf < UActorComponent >` |  |

**Return**

- Type: 
- Description: _None_

### GetComponentsByTag

Gets all the components that inherit from the given class with a given tag.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ComponentClass | `TSubclassOf < UActorComponent >` |  |
| Tag | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetGeneralCampID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCampID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetGeneralCampID

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGeneralCampName

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetGeneralCampRelationWithCampID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CampID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetGeneralCampRelationWithActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### AllowTriggerDeformEffect

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `FVector &` |  |
| EffectRange | `float` |  |

**Return**

- Type: 
- Description: _None_

### TriggerDeformEffect

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Origin | `FVector &` |  |
| EffectRange | `float` |  |

**Return**

- Type: 
- Description: _None_

### DisableDeformEffect

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MarkSubObjectDeleteDirty

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsHiddenEdAtStartup

Simple accessor to check if the actor is hidden upon editor startup

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsHiddenEd

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetIsTemporarilyHiddenInEditor

Sets whether or not this actor is hidden in the editor for the duration of the current editor session

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsHidden | `bool` | True if the actor is hidden |

**Return**

- Type: 
- Description: _None_

### IsTemporarilyHiddenInEditor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIncludeParent | `bool` | - Whether to recurse up child actor hierarchy or not |

**Return**

- Type: 
- Description: _None_

### IsEditable

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsSelectable

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
| OnTakeAnyDamage |  | Called when the actor is damaged in any way. |
| OnTakePointDamage |  | Called when the actor is damaged by point damage. |
| OnActorBeginOverlap |  | Called when another actor begins to overlap this actor, for example a player walking into a trigger.<br>	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events. |
| OnActorEndOverlap |  | Called when another actor stops overlapping this actor. |
| OnBeginCursorOver |  | Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller. |
| OnEndCursorOver |  | Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller. |
| OnClicked |  | Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller. |
| OnReleased |  | Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller. |
| OnInputTouchBegin |  | Called when a touch input is received over this actor when touch events are enabled in the player controller. |
| OnInputTouchEnd |  | Called when a touch input is received over this component when touch events are enabled in the player controller. |
| OnInputTouchLeave |  | Called when a finger is moved off this actor when touch over events are enabled in the player controller. |
| OnInputTouchEnter |  | Called when a finger is moved over this actor when touch over events are enabled in the player controller. |
| OnActorHit |  | Called when this Actor hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.<br>	 	For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event. |
| OnActorHitNew |  | same as OnActorHit, but will Recivie StartPenetrating Hits |
| OnDestroyed |  | Event triggered when the actor is destroyed. |
| OnEndPlay |  | Event triggered when the actor is being removed from a level. |
| OnBecomeViewTargetEvent |  |  |
| OnEndViewTargetEvent |  |  |
| OnEndBlendViewTargetEvent |  |  |
| ActorOnVaultEvent |  |  |

## Language

cpp

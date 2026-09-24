# UParticleSystemComponent

A particle emitter.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)
- IWTACAggregateInterface
- IObjectPoolInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| TemplateBindingType | [EParticleTemplateBindingType](../../cppenum/E/EP/EParticleTemplateBindingType.md) |  |
| Template | `UParticleSystem *` |  |
| SoftTemplate | `TSoftObjectPtr < UParticleSystem >` |  |
| EmitterMaterials | `TArray < UMaterialInterface * >` |  |
| SkelMeshComponents | `TArray < USkeletalMeshComponent * >` | The skeletal mesh components used with the socket location module.<br>	 	This is to prevent them from being garbage collected. |
| bResetOnDetach | `uint8` |  |
| bUpdateOnDedicatedServer | `uint8` | whether to update the particle system on dedicated servers |
| bAllowRecycling | `uint8` | If true, this Particle System will be available for recycling after it has completed. Auto-destroyed systems cannot be recycled.<br>	  Some systems (currently particle trail effects) can recycle components to avoid respawning them to play new effects.<br>	  This is only an optimization and does not change particle system behavior, aside from not triggering normal component initialization events more than once. |
| bAutoManageAttachment | `uint8` | True if we should automatically attach to AutoAttachParent when activated, and detach from our parent when completed.<br>	  This overrides any current attachment that may be present at the time of activation (deferring initial attachment until activation, if AutoAttachParent is null).<br>	  When enabled, detachment occurs regardless of whether AutoAttachParent is assigned, and the relative transform from the time of activation is restored.<br>	  This also disables attachment on dedicated servers, where we don't actually activate even if bAutoActivate is true.<br>	  @see AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType |
| bWarmingUp | `uint8` |  |
| bOverrideLODMethod | `uint8` | indicates that the component's LODMethod overrides the Template's |
| bSkipUpdateDynamicDataDuringTick | `uint8` | Flag indicating that dynamic updating of render data should NOT occur during Tick.<br>	 	This is used primarily to allow for warming up and simulated effects to a certain state. |
| LODMethod | `TEnumAsByte < enum ParticleSystemLODMethod >` | The method of LOD level determination to utilize for this particle system |
| RequiredSignificance | [EParticleSignificanceLevel](../../cppenum/E/EP/EParticleSignificanceLevel.md) | The significance this component requires of it's emitters for them to be enabled. |
| bShouldUseTagGetSkeletalMesh | `bool` | Array holding name instance parameters for this ParticleSystemComponent.<br>	 	Parameters can be used in Cascade using DistributionFloatVectorParticleParameters. |
| SkeletalMeshTagName | `FName` |  |
| InstanceParameters | `TArray < FParticleSysParam >` |  |
| OnParticleSpawn | `FParticleSpawnSignature` |  |
| OnParticleBurst | `FParticleBurstSignature` |  |
| OnParticleDeath | `FParticleDeathSignature` |  |
| OnParticleCollide | `FParticleCollisionSignature` |  |
| OldPosition | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| PartSysVelocity | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| WarmupTime | `float` |  |
| WarmupTickRate | `float` |  |
| OverrideEmitterMeshDataMap | `TMap < FName , UStaticMesh * >` |  |
| SecondsBeforeInactive | `float` | Number of seconds of emitter not being rendered that need to pass before it<br>	  no longer gets ticked becomes inactive. |
| MaxTimeBeforeForceUpdateTransform | `float` | Time between forced UpdateTransforms for systems that use dynamically calculated bounds,<br>	  Which is effectively how often the bounds are shrunk. |
| ReplayClips | `TArray < UParticleSystemReplay * >` | Array of replay clips for this particle system component.  These are serialized to disk.  You really should never add anything to this in the editor.  It's exposed so that you can delete clips if you need to, but be careful when doing so! |
| CustomTimeDilation | `float` | Scales DeltaTime in UParticleSystemComponent::Tick(...) |
| bIsPCPlatformResource | `bool` | Is PC Redirect Particle Resource |
| AutoAttachParent | `TWeakObjectPtr < USceneComponent >` | Component we automatically attach to when activated, if bAutoManageAttachment is true.<br>	  If null during registration, we assign the existing AttachParent and defer attachment until we activate.<br>	  @see bAutoManageAttachment |
| AutoAttachSocketName | `FName` | Socket we automatically attach to on the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment |
| AutoAttachLocationRule | [EAttachmentRule](../../cppenum/E/EA/EAttachmentRule.md) | Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| AutoAttachRotationRule | [EAttachmentRule](../../cppenum/E/EA/EAttachmentRule.md) | Options for how we handle our rotation when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| AutoAttachScaleRule | [EAttachmentRule](../../cppenum/E/EA/EAttachmentRule.md) | Options for how we handle our scale when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| bForceNoAsync | `bool` |  |
| SystemFixedWorldBounds | [FBox](../../cppstruct/F/FB/FBox.md) |  |
| SystemFixedLocalBounds | [FBox](../../cppstruct/F/FB/FBox.md) |  |
| CollisionIgnoreActorList | `TArray < AActor * >` |  |
| CollisionIgnoreComponentList | `TArray < UPrimitiveComponent * >` |  |
| CollisionIgnoreInfoLastClearTime | `float` |  |
| EditorLODLevel | `int32` | INTERNAL. Used by the editor to set the LODLevel |
| EditorDetailMode | `int32` | Used for applying Cascade's detail mode setting to in-level particle systems |
| AutoAttachLocationType_DEPRECATED | `TEnumAsByte < EAttachLocation :: Type >` | DEPRECATED: Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachLocation::Type |

## Functions

### GetDuration

Returns duration

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSystemFixedWorldBounds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldBounds | [FBox](../../cppstruct/F/FB/FBox.md) |  |

**Return**

- Type: 
- Description: _None_

### SetSystemFixedLocalBounds

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LocalBounds | [FBox](../../cppstruct/F/FB/FBox.md) |  |

**Return**

- Type: 
- Description: _None_

### ClearSystemFixedBounds

Clear any previously set fixed bounds for the system instance.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetWarmUp

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WarmUpTime | `float` |  |
| WarmUpRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetAutoAttachParams

DEPRECATED: Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Parent | `USceneComponent *` | Component to attach to. |
| SocketName | `FName` | Socket on Parent to attach to. |
| LocationType | `EAttachLocation :: Type` | Option for how we handle our location when we attach to Parent. |

**Return**

- Type: 
- Description: _None_

### SetAutoAttachmentParameters

Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationRule, AutoAttachRotationRule, AutoAttachScaleRule to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Parent | `USceneComponent *` | Component to attach to. |
| SocketName | `FName` | Socket on Parent to attach to. |
| LocationRule | `EAttachmentRule` | Option for how we handle our location when we attach to Parent. |
| RotationRule | `EAttachmentRule` | Option for how we handle our rotation when we attach to Parent. |
| ScaleRule | [EAttachmentRule](../../cppenum/E/EA/EAttachmentRule.md) | Option for how we handle our scale when we attach to Parent. |

**Return**

- Type: 
- Description: _None_

### SetBeamEndPoint

Set the beam end point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewEndPoint | [FVector](../../cppstruct/F/FV/FVector.md) | The value to set it to |

**Return**

- Type: 
- Description: _None_

### SetBeamSourcePoint

Set the beam source point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewSourcePoint | `FVector` | The value to set it to |
| SourceIndex | `int32` | Which beam within the emitter to set it on |

**Return**

- Type: 
- Description: _None_

### SetBeamSourceTangent

Set the beam source tangent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewTangentPoint | `FVector` | The value to set it to |
| SourceIndex | `int32` | Which beam within the emitter to set it on |

**Return**

- Type: 
- Description: _None_

### SetBeamSourceStrength

Set the beam source strength

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewSourceStrength | `float` | The value to set it to |
| SourceIndex | `int32` | Which beam within the emitter to set it on |

**Return**

- Type: 
- Description: _None_

### SetBeamTargetPoint

Set the beam target point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewTargetPoint | `FVector` | The value to set it to |
| TargetIndex | `int32` | Which beam within the emitter to set it on |

**Return**

- Type: 
- Description: _None_

### SetBeamTargetTangent

Set the beam target tangent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewTangentPoint | `FVector` | The value to set it to |
| TargetIndex | `int32` | Which beam within the emitter to set it on |

**Return**

- Type: 
- Description: _None_

### SetBeamTargetStrength

Set the beam target strength

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to set it on |
| NewTargetStrength | `float` | The value to set it to |
| TargetIndex | `int32` | Which beam within the emitter to set it on |

**Return**

- Type: 
- Description: _None_

### GetBeamEndPoint

Get the beam end point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get the value of |
| OutEndPoint | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### GetBeamSourcePoint

Get the beam source point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get |
| SourceIndex | `int32` | Which beam within the emitter to get |
| OutSourcePoint | `FVector &` | Value of source point |

**Return**

- Type: 
- Description: _None_

### GetBeamSourceTangent

Get the beam source tangent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get |
| SourceIndex | `int32` | Which beam within the emitter to get |
| OutTangentPoint | `FVector &` | Value of source tangent |

**Return**

- Type: 
- Description: _None_

### GetBeamSourceStrength

Get the beam source strength

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get |
| SourceIndex | `int32` | Which beam within the emitter to get |
| OutSourceStrength | `float &` | Value of source tangent |

**Return**

- Type: 
- Description: _None_

### GetBeamTargetPoint

Get the beam target point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get |
| TargetIndex | `int32` | Which beam within the emitter to get |
| OutTargetPoint | `FVector &` | Value of target point |

**Return**

- Type: 
- Description: _None_

### GetBeamTargetTangent

Get the beam target tangent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get |
| TargetIndex | `int32` | Which beam within the emitter to get |
| OutTangentPoint | `FVector &` | Value of target tangent |

**Return**

- Type: 
- Description: _None_

### GetBeamTargetStrength

Get the beam target strength

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterIndex | `int32` | The index of the emitter to get |
| TargetIndex | `int32` | Which beam within the emitter to get |
| OutTargetStrength | `float &` | Value of target tangent |

**Return**

- Type: 
- Description: _None_

### SetEmitterEnable

EnablesDisables a sub-emitter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterName | `FName` | The name of the sub-emitter to set it on |
| bNewEnableState | `bool` | The value to set it to |

**Return**

- Type: 
- Description: _None_

### SetFloatParameter

Change a named float parameter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetVectorParameter

Set a named vector instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### SetColorParameter

Set a named color instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) |  |

**Return**

- Type: 
- Description: _None_

### SetActorParameter

Set a named actor instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### SetMaterialParameter

Set a named material instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### SetTemplate

Change the ParticleSystem used by this ParticleSystemComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTemplate | `UParticleSystem *` |  |

**Return**

- Type: 
- Description: _None_

### GetNumActiveParticles

Get the current number of active particles in this system

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BeginTrails

Begins all trail emitters in this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFirstSocketName | `FName` | The name of the first socket for the trail. |
| InSecondSocketName | `FName` | The name of the second socket for the trail. |
| InWidthMode | `ETrailWidthMode` | How the width value is applied to the trail. |
| InWidth | `float` | The width of the trail. |

**Return**

- Type: 
- Description: _None_

### EndTrails

Ends all trail emitters in this component.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTrailSourceData

Sets the defining data for all trails in this component.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InFirstSocketName | `FName` | The name of the first socket for the trail. |
| InSecondSocketName | `FName` | The name of the second socket for the trail. |
| InWidthMode | `ETrailWidthMode` | How the width value is applied to the trail. |
| InWidth | `float` | The width of the trail. |

**Return**

- Type: 
- Description: _None_

### SetSocketName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSocketName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ManuallyTickComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### K2_Activate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bReset | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_ActivateSystem

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bFlagAsJustAttached | `bool` |  |

**Return**

- Type: 
- Description: _None_

### K2_Deactivate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_DeactivateSystem

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CreateNamedDynamicMaterialInstance

Creates a Dynamic Material Instance for the specified named material override, optionally from the supplied material.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InName | `FName` |  |
| SourceMaterial | `UMaterialInterface *` |  |

**Return**

- Type: 
- Description: _None_

### GetNamedMaterial

Returns a named material. If this named material is not found, returns NULL.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GenerateParticleEvent

Record a kismet event.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InEventName | `FName` | The name of the event that fired. |
| InEmitterTime | `float` | The emitter time when the event fired. |
| InLocation | `FVector` | The location of the particle when the event fired. |
| InDirection | `FVector` |  |
| InVelocity | [FVector](../../cppstruct/F/FV/FVector.md) | The velocity of the particle when the event fired. |

**Return**

- Type: 
- Description: _None_

### SetVectorRandParameter

Set a named random vector instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `FVector &` |  |
| ParamLow | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetFloatRandParameter

Set a named random float instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ParameterName | `FName` |  |
| Param | `float` |  |
| ParamLow | `float` |  |

**Return**

- Type: 
- Description: _None_

### RewindEmitterInstances

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
| OnSystemFinished |  |  |

## Language

cpp

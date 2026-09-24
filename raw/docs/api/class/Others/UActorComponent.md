# UActorComponent

ActorComponent is the base class for components that define reusable behavior that can be added to different types of Actors.
  ActorComponents that have a transform are known as SceneComponents and those that can be rendered are PrimitiveComponents.

  @see USceneComponent
  @see UPrimitiveComponent

## Parents

- [UObject](./UObject.md)
- IInterface_AssetUserData

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PrimaryComponentTick | `FActorComponentTickFunction` | Main tick function for the Actor |
| DSTickInterval | `float` | The frequency in seconds at which this tick function will be executed on DS.  If less than or equal to 0 then it will tick every frame<br>	 If greater than 0 will cover PrimaryComponentTick.TickInterval<br>	 Add by zoranouyang |
| ComponentTags | `TArray < FName >` | Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting. |
| NetUpdateFrequency | `float` |  |
| bAllowBPReceiveTickEvent | `bool` | If true, bp tick will be called , otherwise skipped |
| TickAdapterIntvlOverride | `uint8` |  |
| bSyncOwnerTickAdapter | `uint8` |  |
| bEnableTickAdapter | `uint8` |  |
| ScriptNetworkReplicatedPropertyWrapper | `FScriptNetworkReplicatedPropertyWrapper` |  |
| bSupportSuspendTick | `uint8` |  |
| bDestroyIfOnClientNoLocalControl | `uint8` |  |
| bReplicates | `uint8` | Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first! |
| bNetAddressable | `uint8` | Is this component safe to ID over the network by name? |
| bDeferedConstructComponent | `uint8` |  |
| bSkipNewDuplicateComponent | `uint8` |  |
| bNameStableForBackupRestore | `uint8` |  |
| bNeedBackupRestoreForCustomSerialize | `uint8` |  |
| bEnableTickWhenOutOfRegion | `uint8` | If true, this component will Enale Tick when out of region. |
| bAutoActivate | `uint8` | Whether the component is activated at creation or must be explicitly activated. |
| bIsActive | `uint8` | Whether the component is currently active. |
| bEditableWhenInherited | `uint8` |  |
| bCanEverAffectNavigation | `uint8` | Whether this component can potentially influence navigation |
| bIsEditorOnly | `uint8` | If true, the component will be excluded from non-editor builds |
| bNeedsLoadForClient | `uint8` | If false, the component will be excluded from client builds |
| bNeedsLoadForServer | `uint8` | If false, the component will be excluded from server builds |
| bAllowRenderDataUpdateLag | `uint8` |  |
| CreationMethod | [EComponentCreationMethod](../../cppenum/E/EC/EComponentCreationMethod.md) |  |
| UCSModifiedProperties | `TArray < FSimpleMemberReference >` |  |
| AssetUserData | `TArray < UAssetUserData * >` | Array of user data stored with the component |
| bCreatedByConstructionScript_DEPRECATED | `uint8` | True if this component was created by a construction script, and will be destroyed by DestroyConstructedComponents |
| bInstanceComponent_DEPRECATED | `uint8` | True if this component was created as an instance component |

## Functions

### GetToString

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ForceNetUpdate

**Parameters**

_None_

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

### IsBeingDestroyed

Returns whether the component is in the process of being destroyed.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_Replicates

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRep_IsActive

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOwner

Follow the Outer chain to get the  AActor  that 'Owns' this component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ComponentHasTag

See if this component contains the supplied tag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Tag | `FName` |  |

**Return**

- Type: 
- Description: _None_

### Activate

Activates the SceneComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bReset | `bool` | - The value to assign to HiddenGame. |

**Return**

- Type: 
- Description: _None_

### Deactivate

Deactivates the SceneComponent.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetActive

Sets whether the component is active or not

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewActive | `bool` | - The new active state of the component |
| bReset | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ToggleActive

Toggles the active state of the component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsActive

Returns whether the component is active or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAutoActivate

Sets whether the component should be auto activate or not. Only safe during construction scripts.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewAutoActivate | `bool` | - The new auto activate state of the component |

**Return**

- Type: 
- Description: _None_

### SetTickableWhenPaused

Sets whether this component can tick when paused.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bTickableWhenPaused | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetIsReplicated

Enable or disable replication. This is the equivalent of RemoteRole for actors (only a bool is required for components)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ShouldReplicate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ReceiveBeginPlay

Blueprint implementable event for when the component is beginning play, called before its Owner's BeginPlay on Actor BeginPlay
	  or when the component is dynamically created if the Actor has already BegunPlay.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ReceiveEndPlay

Blueprint implementable event for when the component ends play, generally via destruction or its Actor's EndPlay.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndPlayReason | `EEndPlayReason :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetComponentTickEnabled

Set this component's tick functions to be enabled or disabled. Only has an effect if the function is registered

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` | - Whether it should be enabled or not |

**Return**

- Type: 
- Description: _None_

### IsComponentTickEnabled

Returns whether this component has tick enabled or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsComponentTickEnabledByExternal

Returns whether this component has tick enabled or not,
	  Which set by External business

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetComponentTickInterval

Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect on next tick.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TickInterval | `float` | The duration between ticks for this component's primary tick function |

**Return**

- Type: 
- Description: _None_

### GetComponentTickInterval

Returns whether this component has tick enabled or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### K2_DestroyComponent

Unregister and mark for pending kill a component.  This may not be used to destroy a component that is owned by an actor unless the owning actor is calling the function.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SetTickGroup

Changes the ticking group for this component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewTickGroup | [ETickingGroup](../../cppenum/E/ET/ETickingGroup.md) |  |

**Return**

- Type: 
- Description: _None_

### AddTickPrerequisiteActor

Make this component tick after PrerequisiteActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PrerequisiteActor | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### AddTickPrerequisiteComponent

Make this component tick after PrerequisiteComponent.

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

### ReceiveTick

Event called every frame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnComponentActivated |  |  |
| OnComponentDeactivated |  |  |

## Language

cpp

# UGameplayStatics

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### SpawnObject

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectClass | `TSubclassOf < UObject >` |  |
| Outer | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### BeginSpawningActorFromBlueprint

生成指定蓝图类的实例，但不自动执行构造函数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| Blueprint | `UBlueprint *` | 蓝图类 |
| SpawnTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) | 生成Actor的Transform |
| bNoCollisionFail | `bool` |  |

**Return**

- Type: 
- Description: _None_

### BeginSpawningActorFromClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ActorClass | `TSubclassOf < AActor >` |  |
| SpawnTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) |  |
| bNoCollisionFail | `bool` |  |
| Owner | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### BeginDeferredActorSpawnFromClass

Spawns an instance of an actor class, but does not automatically run its construction script.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ActorClass | `TSubclassOf < AActor >` |  |
| SpawnTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) |  |
| CollisionHandlingOverride | `ESpawnActorCollisionHandlingMethod` |  |
| Owner | `AActor *` |  |

**Return**

- Type: 
- Description: _None_

### FinishSpawningActor

结束生成Actor，执行Actor的构造函数

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actor | `AActor *` | Actor实例 |
| SpawnTransform | [FTransform &](../../../cppstruct/F/FT/FTransform.md) | 生成Actor的Transform |

**Return**

- Type: 
- Description: _None_

### GetActorArrayAverageLocation

Find the average location (centroid) of an array of Actors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actors | `TArray < AActor * > &` |  |

**Return**

- Type: 
- Description: _None_

### GetActorArrayBounds

Bind the bounds of an array of Actors

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Actors | `TArray < AActor * > &` |  |
| bOnlyCollidingComponents | `bool` |  |
| Center | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |
| BoxExtent | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetAllActorsOfClass

Find all Actors in the world of the specified class.
	 	This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ActorClass | `TSubclassOf < AActor >` | Class of Actor to find. Must be specified or result array will be empty. |
| OutActors | `TArray < AActor * > &` | Output array of Actors of the specified class. |

**Return**

- Type: 
- Description: _None_

### GetFirstActorOfClass

Find one Actor in the world of the specified class.
		This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ActorClass | `TSubclassOf < AActor >` | Class of Actor to find. Must be specified or result array will be empty. |

**Return**

- Type: 
- Description: _None_

### GetAllActorsWithInterface

Find all Actors in the world with the specified interface.
	 	This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Interface | `TSubclassOf < UInterface >` | Interface to find. Must be specified or result array will be empty. |
| OutActors | `TArray < AActor * > &` | Output array of Actors of the specified interface. |

**Return**

- Type: 
- Description: _None_

### GetAllActorsWithTag

获取拥有指定Tag的所有Actor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| Tag | `FName` | Tag名称 |
| OutActors | `TArray < AActor * > &` | 输出的Actor列表 |

**Return**

- Type: 
- Description: _None_

### GetGameInstance

获取GameInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetCurrentGameInstance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetPlayerController

获取PlayerController

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| PlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerPawn

获取PlayerPawn

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| PlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerCharacter

获取PlayerCharacter

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| PlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayerCameraManager

获取PlayerCameraManager

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| PlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### CreatePlayer

Create a new player for this game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ControllerId | `int32` | The ID of the controller that the should control the newly created player. A value of -1 specifies to use the next available ID |
| bSpawnPawn | `bool` | Whether a pawn should be spawned immediately. If false a pawn will not be created until transition to the next map. |

**Return**

- Type: 
- Description: _None_

### RemovePlayer

Removes a player from this game.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` | The player controller of the player to be removed |
| bDestroyPawn | `bool` | Whether the controlled pawn should be deleted as well |

**Return**

- Type: 
- Description: _None_

### GetPlayerControllerID

Gets what controller ID a Player is using

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` | The player controller of the player to get the ID of |

**Return**

- Type: 
- Description: _None_

### SetPlayerControllerID

Sets what controller ID a Player should be using

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` | The player controller of the player to change the controller ID of |
| ControllerId | `int32` | The controller ID to assign to this player |

**Return**

- Type: 
- Description: _None_

### LoadStreamLevel

加载子关卡

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| LevelName | `FName` | 子关卡名称 |
| bMakeVisibleAfterLoad | `bool` | 加载后是否显示 |
| bShouldBlockOnLoad | `bool` | 加载时是否阻塞 |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | 回调信息结构 |

**Return**

- Type: 
- Description: _None_

### UnloadStreamLevel

加载子关卡

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| LevelName | `FName` | 子关卡名称 |
| LatentInfo | [FLatentActionInfo](../../../cppstruct/F/FL/FLatentActionInfo.md) | 回调信息结构 |

**Return**

- Type: 
- Description: _None_

### GetStreamingLevel

Returns level streaming object with specified level package name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PackageName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### FlushLevelStreaming

刷新关卡流，直到所有子关卡加载完毕时返回

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### FlushLevelStreamingBasedOnCharacterLocation

更新玩家的位置，触发LevelBounds，然后加载所有关卡

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| CharacterLocation | [FVector](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### FlushAllStreamingResource

触发TextureStreaming， 将贴图全部加载完毕

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### CancelAsyncLoading

Cancels all currently queued streaming packages

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OpenLevel

Travel to another level

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| LevelName | `FName` | the level to open |
| bAbsolute | `bool` | if true options are reset, if false options are carried over from current level |
| Options | `FString` | a string of options to use for the travel URL |

**Return**

- Type: 
- Description: _None_

### OpenShaderLibrary

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Name | `FString &` |  |
| VersionNum | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### CloseShaderLibrary

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Name | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### EnableShaderGroup

Enable a new ShaderGroup for all opened ShaderCodeLibrary

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupName | `FString &` |  |
| ShaderPlatform | `int32` |  |

**Return**

- Type: 
- Description: _None_

### EnableShaderLevel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ShaderLevelName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### EnableShaderPak

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ShaderPakName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### DisableShaderLevel

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ShaderLevelName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### DisableShaderPak

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ShaderPakName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### RestartShaderPrecompile

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OpenShaderCodeLibrary

OpenShaderCodeLibrary in Saved Folder

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Version | `FString &` |  |
| bUseContentShaders | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentLevelName

获得当前关卡名称

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| bRemovePrefixString | `bool` | 是否移除prefix的字符串 |

**Return**

- Type: 
- Description: _None_

### GetGameMode

获得当前GameMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetGameState

获得当前GameState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetGameStateByWorldContext

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### GetObjectClass

获得对象的类型

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | 指定对象 |

**Return**

- Type: 
- Description: _None_

### GetGlobalTimeDilation

获得当前时间膨胀

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### SetGlobalTimeDilation

设置时间膨胀

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| TimeDilation | `float` | 世界的时间膨胀 |

**Return**

- Type: 
- Description: _None_

### SetGamePaused

设置游戏是否暂停

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| bPaused | `bool` | 是否暂停 |

**Return**

- Type: 
- Description: _None_

### IsGamePaused

判断游戏是否暂停

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### ApplyRadialDamage

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| BaseDamage | `float` | - The base damage to apply, i.e. the damage at the origin. |
| Origin | [FVector &](../../../cppstruct/F/FV/FVector.md) | - Epicenter of the damage area. |
| DamageRadius | `float` | - Radius of the damage area, from Origin |
| DamageTypeClass | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| IgnoreActors | `TArray < AActor * > &` |  |
| DamageCauser | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded). This actor will not be damaged and it will not block damage. |
| InstigatedByController | `AController *` | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |
| bDoFullDamage | `bool` |  |
| DamagePreventionChannel | `ECollisionChannel` | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |
| DamageTag | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ApplyRadialDamageWithFalloff

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| BaseDamage | `float` | - The base damage to apply, i.e. the damage at the origin. |
| MinimumDamage | `float` |  |
| Origin | [FVector &](../../../cppstruct/F/FV/FVector.md) | - Epicenter of the damage area. |
| DamageInnerRadius | `float` | - Radius of the full damage area, from Origin |
| DamageOuterRadius | `float` | - Radius of the minimum damage area, from Origin |
| DamageFalloff | `float` | - Falloff exponent of damage from DamageInnerRadius to DamageOuterRadius |
| DamageTypeClass | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| IgnoreActors | `TArray < AActor * > &` |  |
| DamageCauser | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| InstigatedByController | `AController *` | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |
| DamagePreventionChannel | `ECollisionChannel` | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |
| DamageTag | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ApplyPointDamage

Hurts the specified actor with the specified impact.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamagedActor | `AActor *` | - Actor that will be damaged. |
| BaseDamage | `float` | - The base damage to apply. |
| HitFromDirection | [FVector &](../../../cppstruct/F/FV/FVector.md) | - Direction the hit came FROM |
| HitInfo | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | - Collision or trace result that describes the hit |
| EventInstigator | `AController *` | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |
| DamageCauser | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| DamageTypeClass | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| DamageTag | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ApplyDamage

Hurts the specified actor with generic damage.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DamagedActor | `AActor *` | - Actor that will be damaged. |
| BaseDamage | `float` | - The base damage to apply. |
| EventInstigator | `AController *` | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |
| DamageCauser | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| DamageTypeClass | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| DamageTag | `int32` |  |

**Return**

- Type: 
- Description: _None_

### PlayWorldCameraShake

Plays an in-world camera shake that affects all nearby local players, with distance-based attenuation. Does not replicate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | - Object that we can obtain a world context from |
| Shake | `TSubclassOf < UCameraShake >` | - Camera shake asset to use |
| Epicenter | [FVector](../../../cppstruct/F/FV/FVector.md) | - location to place the effect in world space |
| InnerRadius | `float` | - Cameras inside this radius are ignored |
| OuterRadius | `float` | - Cameras outside of InnerRadius and inside this are effected |
| Falloff | `float` | - Affects falloff of effect as it nears OuterRadius |
| bOrientShakeTowardsEpicenter | `bool` | - Changes the rotation of shake to point towards epicenter instead of forward |

**Return**

- Type: 
- Description: _None_

### SpawnEmitterAtLocation

Plays the specified effect at the given location and rotation, fire and forget. The system will go away when the effect is complete. Does not replicate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | - Object that we can obtain a world context from |
| EmitterTemplate | `UParticleSystem *` | - particle system to create |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - location to place the effect in world space |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - rotation to place the effect in world space |
| Scale | [FVector](../../../cppstruct/F/FV/FVector.md) | - scale to create the effect at |
| bAutoDestroy | `bool` | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SpawnEmitterAttached

Plays the specified effect attached to and following the specified component. The system will go away when the effect is complete. Does not replicate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterTemplate | `UParticleSystem *` | - particle system to create |
| AttachToComponent | `USceneComponent *` |  |
| AttachPointName | `FName` | - Optional named point within the AttachComponent to spawn the emitter at |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world location that will be translated to a relative offset (if LocationType is KeepWorldPosition). |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset (if LocationType is KeepWorldPosition). |
| Scale | [FVector](../../../cppstruct/F/FV/FVector.md) | - Depending on the value of LocationType this is either a relative scale from the attach component or an absolute world scale that will be translated to a relative scale (if LocationType is KeepWorldPosition). |
| LocationType | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| bAutoDestroy | `bool` | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SpawnEmitterAttachedToActor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EmitterTemplate | `UParticleSystem *` |  |
| AttachToComponent | `USceneComponent *` |  |
| AttachPointName | `FName` |  |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) |  |
| Scale | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| LocationType | `EAttachLocation :: Type` |  |
| bAutoDestroy | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AreAnyListenersWithinRange

Determines if any audio listeners are within range of the specified location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | The location to potentially play a sound at |
| MaximumRange | `float` | The maximum distance away from Location that a listener can be |

**Return**

- Type: 
- Description: _None_

### SetGlobalPitchModulation

Sets a global pitch modulation scalar that will apply to all non-UI sounds

	  Fire and Forget.
	  Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PitchModulation | `float` | - A pitch modulation value to globally set. |
| TimeSec | `float` | - A time value to linearly interpolate the global modulation pitch over from it's current value. |

**Return**

- Type: 
- Description: _None_

### SetGlobalListenerFocusParameters

Sets the global listener focus parameters which will scale focus behavior of sounds based on their focus azimuth settings in their attenuation settings.

	  Fire and Forget.
	  Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| FocusAzimuthScale | `float` | - An angle scale value used to scale the azimuth angle that defines where sounds are in-focus. |
| NonFocusAzimuthScale | `float` |  |
| FocusDistanceScale | `float` | - A distance scale value to use for sounds which are in-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |
| NonFocusDistanceScale | `float` | - A distance scale value to use for sounds which are out-of-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |
| FocusVolumeScale | `float` |  |
| NonFocusVolumeScale | `float` |  |
| FocusPriorityScale | `float` | - A priority scale value (> 0.0) to use for sounds which are in-focus. Values < 1.0 will reduce the priority of in-focus sounds, values > 1.0 will increase the priority of in-focus sounds. |
| NonFocusPriorityScale | `float` | - A priority scale value (> 0.0) to use for sounds which are out-of-focus. Values < 1.0 will reduce the priority of sounds out-of-focus sounds, values > 1.0 will increase the priority of out-of-focus sounds. |

**Return**

- Type: 
- Description: _None_

### PlaySound2D

Plays a sound directly with no attenuation, perfect for UI sounds.

	   Fire and Forget.
	   Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Sound | `USoundBase *` | - Sound to play. |
| VolumeMultiplier | `float` | - Multiplied with the volume to make the sound louder or softer. |
| PitchMultiplier | `float` | - Multiplies the pitch. |
| StartTime | `float` | - How far in to the sound to begin playback at |
| ConcurrencySettings | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| OwningActor | `AActor *` | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |

**Return**

- Type: 
- Description: _None_

### SpawnSound2D

Spawns a sound with no attenuation, perfect for UI sounds.

	   Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Sound | `USoundBase *` | - Sound to play. |
| VolumeMultiplier | `float` | - Multiplied with the volume to make the sound louder or softer. |
| PitchMultiplier | `float` | - Multiplies the pitch. |
| StartTime | `float` | - How far in to the sound to begin playback at |
| ConcurrencySettings | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| bPersistAcrossLevelTransition | `bool` |  |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### CreateSound2D

Creates a sound with no attenuation, perfect for UI sounds. This does NOT play the sound

	   Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Sound | `USoundBase *` | - Sound to create. |
| VolumeMultiplier | `float` | - Multiplied with the volume to make the sound louder or softer. |
| PitchMultiplier | `float` | - Multiplies the pitch. |
| StartTime | `float` | - How far in to the sound to begin playback at |
| ConcurrencySettings | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| bPersistAcrossLevelTransition | `bool` |  |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### PlaySoundAtLocation

Plays a sound at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Sound | `USoundBase *` | - sound to play |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - World position to play sound at |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - World rotation to play sound at |
| VolumeMultiplier | `float` | - Volume multiplier |
| PitchMultiplier | `float` | - PitchMultiplier |
| StartTime | `float` | - How far in to the sound to begin playback at |
| AttenuationSettings | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| ConcurrencySettings | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| OwningActor | `AActor *` | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |

**Return**

- Type: 
- Description: _None_

### SpawnSoundAtLocation

Spawns a sound at the given location. This does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Sound | `USoundBase *` | - sound to play |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - World position to play sound at |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - World rotation to play sound at |
| VolumeMultiplier | `float` | - Volume multiplier |
| PitchMultiplier | `float` | - PitchMultiplier |
| StartTime | `float` | - How far in to the sound to begin playback at |
| AttenuationSettings | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| ConcurrencySettings | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SpawnSoundAttached

Plays a sound attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Sound | `USoundBase *` | - sound to play |
| AttachToComponent | `USceneComponent *` |  |
| AttachPointName | `FName` | - Optional named point within the AttachComponent to play the sound at |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| LocationType | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| bStopWhenAttachedToDestroyed | `bool` | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |
| VolumeMultiplier | `float` | - Volume multiplier |
| PitchMultiplier | `float` | - PitchMultiplier |
| StartTime | `float` | - How far in to the sound to begin playback at |
| AttenuationSettings | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| ConcurrencySettings | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### PlayDialogue2D

Plays a dialogue directly with no attenuation, perfect for UI.

	   Fire and Forget.
	   Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Dialogue | `UDialogueWave *` | - dialogue to play |
| Context | [FDialogueContext &](../../../cppstruct/F/FD/FDialogueContext.md) | - context the dialogue is to play in |
| VolumeMultiplier | `float` | - Multiplied with the volume to make the sound louder or softer. |
| PitchMultiplier | `float` | - Multiplies the pitch. |
| StartTime | `float` | - How far in to the dialogue to begin playback at |

**Return**

- Type: 
- Description: _None_

### SpawnDialogue2D

Spawns a dialogue with no attenuation, perfect for UI.

	   Not Replicated.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Dialogue | `UDialogueWave *` | - dialogue to play |
| Context | [FDialogueContext &](../../../cppstruct/F/FD/FDialogueContext.md) | - context the dialogue is to play in |
| VolumeMultiplier | `float` | - Multiplied with the volume to make the sound louder or softer. |
| PitchMultiplier | `float` | - Multiplies the pitch. |
| StartTime | `float` | - How far in to the dialogue to begin playback at |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### PlayDialogueAtLocation

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Dialogue | `UDialogueWave *` | - dialogue to play |
| Context | [FDialogueContext &](../../../cppstruct/F/FD/FDialogueContext.md) | - context the dialogue is to play in |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - World position to play dialogue at |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - World rotation to play dialogue at |
| VolumeMultiplier | `float` | - Volume multiplier |
| PitchMultiplier | `float` | - Pitch multiplier |
| StartTime | `float` | - How far in to the dialogue to begin playback at |
| AttenuationSettings | `USoundAttenuation *` | - Override attenuation settings package to play sound with |

**Return**

- Type: 
- Description: _None_

### SpawnDialogueAtLocation

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Dialogue | `UDialogueWave *` | - dialogue to play |
| Context | [FDialogueContext &](../../../cppstruct/F/FD/FDialogueContext.md) | - context the dialogue is to play in |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - World position to play dialogue at |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - World rotation to play dialogue at |
| VolumeMultiplier | `float` | - Volume multiplier |
| PitchMultiplier | `float` | - PitchMultiplier |
| StartTime | `float` | - How far in to the dialogue to begin playback at |
| AttenuationSettings | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SpawnDialogueAttached

Spawns a dialogue attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Dialogue | `UDialogueWave *` | - dialogue to play |
| Context | [FDialogueContext &](../../../cppstruct/F/FD/FDialogueContext.md) | - context the dialogue is to play in |
| AttachToComponent | `USceneComponent *` |  |
| AttachPointName | `FName` | - Optional named point within the AttachComponent to play the sound at |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| LocationType | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| bStopWhenAttachedToDestroyed | `bool` | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |
| VolumeMultiplier | `float` | - Volume multiplier |
| PitchMultiplier | `float` | - PitchMultiplier |
| StartTime | `float` | - How far in to the dialogue to begin playback at |
| AttenuationSettings | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| bAutoDestroy | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SpawnForceFeedbackAtLocation

Plays a force feedback effect at the given location. This is a fire and forget effect and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ForceFeedbackEffect | `UForceFeedbackEffect *` | - effect to play |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - World position to center the effect at |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - World rotation to center the effect at |
| bLooping | `bool` |  |
| IntensityMultiplier | `float` | - Intensity multiplier |
| StartTime | `float` | - How far in to the feedback effect to begin playback at |
| AttenuationSettings | `UForceFeedbackAttenuation *` | - Override attenuation settings package to play effect with |
| bAutoDestroy | `bool` | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SpawnForceFeedbackAttached

Plays a force feedback effect attached to and following the specified component. This is a fire and forget effect. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ForceFeedbackEffect | `UForceFeedbackEffect *` | - effect to play |
| AttachToComponent | `USceneComponent *` |  |
| AttachPointName | `FName` | - Optional named point within the AttachComponent to attach to |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| LocationType | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| bStopWhenAttachedToDestroyed | `bool` | - Specifies whether the feedback effect should stop playing when the owner of the attach to component is destroyed. |
| bLooping | `bool` |  |
| IntensityMultiplier | `float` | - Intensity multiplier |
| StartTime | `float` | - How far in to the feedback effect to begin playback at |
| AttenuationSettings | `UForceFeedbackAttenuation *` | - Override attenuation settings package to play effect with |
| bAutoDestroy | `bool` | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |

**Return**

- Type: 
- Description: _None_

### SetSubtitlesEnabled

Will set subtitles to be enabled or disabled.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` | will enable subtitle drawing if true, disable if false. |

**Return**

- Type: 
- Description: _None_

### AreSubtitlesEnabled

Returns whether or not subtitles are currently enabled.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBaseSoundMix

Set the sound mix of the audio system for special EQing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InSoundMix | `USoundMix *` |  |

**Return**

- Type: 
- Description: _None_

### SetSoundMixClassOverride

Overrides the sound class adjuster in the given sound mix. If the sound class does not exist in the input sound mix, the sound class adjustment will be added to the sound mix.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InSoundMixModifier | `USoundMix *` | The sound mix to modify. |
| InSoundClass | `USoundClass *` | The sound class to override (or add) in the sound mix. |
| Volume | `float` | The volume scale to set the sound class adjuster to. |
| Pitch | `float` | The pitch scale to set the sound class adjuster to. |
| FadeInTime | `float` | The interpolation time to use to go from the current sound class adjuster values to the new values. |
| bApplyToChildren | `bool` | Whether or not to apply this override to the sound class' children or to just the specified sound class. |

**Return**

- Type: 
- Description: _None_

### ClearSoundMixClassOverride

Clears the override of the sound class adjuster in the given sound mix. If the override did not exist in the sound mix, this will do nothing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InSoundMixModifier | `USoundMix *` | The sound mix to modify. |
| InSoundClass | `USoundClass *` | The sound class to override (or add) in the sound mix. |
| FadeOutTime | `float` | The interpolation time to use to go from the current sound class adjuster override values to the non-override values. |

**Return**

- Type: 
- Description: _None_

### PushSoundMixModifier

Push a sound mix modifier onto the audio system

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InSoundMixModifier | `USoundMix *` |  |

**Return**

- Type: 
- Description: _None_

### PopSoundMixModifier

Pop a sound mix modifier from the audio system

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| InSoundMixModifier | `USoundMix *` |  |

**Return**

- Type: 
- Description: _None_

### ClearSoundMixModifiers

Clear all sound mix modifiers from the audio system

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### ActivateReverbEffect

Activates a Reverb Effect without the need for a volume

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| ReverbEffect | `UReverbEffect *` | Reverb Effect to use |
| TagName | `FName` | Tag to associate with Reverb Effect |
| Priority | `float` | Priority of the Reverb Effect |
| Volume | `float` | Volume level of Reverb Effect |
| FadeTime | `float` | Time before Reverb Effect is fully active |

**Return**

- Type: 
- Description: _None_

### DeactivateReverbEffect

Deactivates a Reverb Effect not applied by a volume

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| TagName | `FName` | Tag associated with Reverb Effect to remove |

**Return**

- Type: 
- Description: _None_

### GetCurrentReverbEffect

Returns the highest priority reverb settings currently active from any source (volumes or manual setting).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### SpawnDecalAtLocation

Spawns a decal at the given location and rotation, fire and forget. Does not replicate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| DecalMaterial | `UMaterialInterface *` | - decal's material |
| DecalSize | [FVector](../../../cppstruct/F/FV/FVector.md) | - size of decal |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - location to place the decal in world space |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - rotation to place the decal in world space |
| LifeSpan | `float` | - destroy decal component after time runs out (0 = infinite) |

**Return**

- Type: 
- Description: _None_

### SpawnDecalAttached

Spawns a decal attached to and following the specified component. Does not replicate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DecalMaterial | `UMaterialInterface *` | - decal's material |
| DecalSize | [FVector](../../../cppstruct/F/FV/FVector.md) | - size of decal |
| AttachToComponent | `USceneComponent *` |  |
| AttachPointName | `FName` | - Optional named point within the AttachComponent to spawn the emitter at |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| Rotation | [FRotator](../../../cppstruct/F/FR/FRotator.md) | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a realative offset |
| LocationType | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| LifeSpan | `float` | - destroy decal component after time runs out (0 = infinite) |

**Return**

- Type: 
- Description: _None_

### BreakHitResult

Extracts data from a HitResult.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | The source HitResult. |
| bBlockingHit | `bool &` | True if there was a blocking hit, false otherwise. |
| bInitialOverlap | `bool &` | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |
| Time | `float &` | 'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |
| Distance | `float &` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| Location | [FVector &](../../../cppstruct/F/FV/FVector.md) | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. |
| ImpactPoint | [FVector &](../../../cppstruct/F/FV/FVector.md) | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. |
| Normal | [FVector &](../../../cppstruct/F/FV/FVector.md) | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. |
| ImpactNormal | [FVector &](../../../cppstruct/F/FV/FVector.md) | Normal of the hit in world space, for the object that was hit by the sweep. |
| PhysMat | `UPhysicalMaterial * &` | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |
| HitActor | `AActor * &` | Actor hit by the trace. |
| HitComponent | `UPrimitiveComponent * &` | PrimitiveComponent hit by the trace. |
| HitBoneName | `FName &` | Name of the bone hit (valid only if we hit a skeletal mesh). |
| HitItem | `int32 &` | Primitive-specific data recording which item in the primitive was hit |
| FaceIndex | `int32 &` | If colliding with trimesh or landscape, index of face that was hit. |
| TraceStart | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |
| TraceEnd | [FVector &](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### MakeHitResult

Create a HitResult struct

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bBlockingHit | `bool` | True if there was a blocking hit, false otherwise. |
| bInitialOverlap | `bool` | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |
| Time | `float` | 'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |
| Distance | `float` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| Location | [FVector](../../../cppstruct/F/FV/FVector.md) | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. |
| ImpactPoint | [FVector](../../../cppstruct/F/FV/FVector.md) | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. |
| Normal | [FVector](../../../cppstruct/F/FV/FVector.md) | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. |
| ImpactNormal | [FVector](../../../cppstruct/F/FV/FVector.md) | Normal of the hit in world space, for the object that was hit by the sweep. |
| PhysMat | `UPhysicalMaterial *` | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |
| HitActor | `AActor *` | Actor hit by the trace. |
| HitComponent | `UPrimitiveComponent *` | PrimitiveComponent hit by the trace. |
| HitBoneName | `FName` | Name of the bone hit (valid only if we hit a skeletal mesh). |
| HitItem | `int32` | Primitive-specific data recording which item in the primitive was hit |
| FaceIndex | `int32` | If colliding with trimesh or landscape, index of face that was hit. |
| TraceStart | [FVector](../../../cppstruct/F/FV/FVector.md) |  |
| TraceEnd | [FVector](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GetSurfaceType

Returns the EPhysicalSurface type of the given Hit.
	  To edit surface type for your project, use ProjectSettingsPhysicsPhysicalSurface section

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) |  |

**Return**

- Type: 
- Description: _None_

### FindCollisionUV

Try and find the UV for a collision impact. Note this ONLY works if 'Support UV From Hit Results' is enabled in Physics Settings.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Hit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) |  |
| UVChannel | `int32` |  |
| UV | [FVector2D &](../../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### CreateSaveGameObject

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SaveGameClass | `TSubclassOf < USaveGame >` | Class of SaveGame to create |

**Return**

- Type: 
- Description: _None_

### CreateSaveGameObjectFromBlueprint

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SaveGameBlueprint | `UBlueprint *` | Blueprint of SaveGame to create |

**Return**

- Type: 
- Description: _None_

### SaveGameToSlot

Save the contents of the SaveGameObject to a slot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SaveGameObject | `USaveGame *` | Object that contains data about the save game that we want to write out |
| SlotName | `FString &` | Name of save game slot to save to. |
| UserIndex | `int32` | For some platforms, master user index to identify the user doing the saving. |

**Return**

- Type: 
- Description: _None_

### DoesSaveGameExist

See if a save game exists with the specified name.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FString &` | Name of save game slot. |
| UserIndex | `int32` | For some platforms, master user index to identify the user doing the saving. |

**Return**

- Type: 
- Description: _None_

### BindLoadGameGuardEntranceCheckDelegate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Obj | `UObject *` |  |
| FuncName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### BindLoadGameGuardExitCheckDelegate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Obj | `UObject *` |  |
| FuncName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### LoadGameFromSlot

Load the contents from a given slot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FString &` | Name of the save game slot to load from. |
| UserIndex | `int32` | For some platforms, master user index to identify the user doing the loading. |

**Return**

- Type: 
- Description: _None_

### LoadGameFromSlotWithSizeLimit

Load the contents from a given slot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FString &` | Name of the save game slot to load from. |
| UserIndex | `int32` | For some platforms, master user index to identify the user doing the loading. |
| MaxSerSize | `int32` | Specify the maxserializesize of archive, just working for fstring. |

**Return**

- Type: 
- Description: _None_

### LoadGameFromMemory

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectBytes | `TArray < uint8 > &` |  |
| MaxSerSize | `int32` |  |

**Return**

- Type: 
- Description: _None_

### LoadGameFromMemoryWithSizeLimit

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ObjectBytes | `TArray < uint8 > &` |  |
| MaxSerSize | `int32` |  |

**Return**

- Type: 
- Description: _None_

### DeleteGameInSlot

Delete a save game in a particular slot.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FString &` | Name of save game slot to delete. |
| UserIndex | `int32` | For some platforms, master user index to identify the user doing the deletion. |

**Return**

- Type: 
- Description: _None_

### GetWorldDeltaSeconds

获得当前每帧的delta time，单位秒

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetTimeSeconds

获得当前游戏开始之后的时间，单位秒，受时间膨胀和游戏暂停影响

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetUnpausedTimeSeconds

获得当前游戏开始之后的时间，单位秒，受时间膨胀影响，但不受游戏暂停影响

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetRealTimeSeconds

获得当前游戏开始之后的真实时间，单位秒，不受时间膨胀和游戏暂停影响

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetAudioTimeSeconds

获得当前游戏开始之后的时间，单位秒，不受时间膨胀影响，但受时间暂停影响

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### GetAccurateRealTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| Seconds | `int32 &` |  |
| PartialSeconds | `float &` |  |

**Return**

- Type: 
- Description: _None_

### EnableLiveStreaming

~ DVRStreaming API

	  Toggle live DVR streaming.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Enable | `bool` | If true enable streaming, otherwise disable. |

**Return**

- Type: 
- Description: _None_

### GetPlatformName

Returns the string name of the current platform, to perform different behavior based on platform.
	  (Platform names include Windows, Mac, IOS, Android, PS4, XboxOne, HTML5, Linux)

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BlueprintSuggestProjectileVelocity

Calculates an launch velocity for a projectile to hit a specified point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| TossVelocity | [FVector &](../../../cppstruct/F/FV/FVector.md) | (output) Result launch velocity. |
| StartLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | Intended launch location |
| EndLocation | [FVector](../../../cppstruct/F/FV/FVector.md) | Desired landing location |
| LaunchSpeed | `float` | Desired launch speed |
| OverrideGravityZ | `float` | Optional gravity override. 0 means "do not override". |
| TraceOption | `ESuggestProjVelocityTraceOption :: Type` | Controls whether or not to validate a clear path by tracing along the calculated arc |
| CollisionRadius | `float` | Radius of the projectile (assumed spherical), used when tracing |
| bFavorHighArc | `bool` | If true and there are 2 valid solutions, will return the higher arc. If false, will favor the lower arc. |
| bDrawDebug | `bool` | When true, a debug arc is drawn (red for an invalid arc, green for a valid arc) |

**Return**

- Type: 
- Description: _None_

### Blueprint_PredictProjectilePath_ByObjectType

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | Predicted hit result, if the projectile will hit something |
| OutPathPositions | `TArray < FVector > &` | Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |
| OutLastTraceDestination | [FVector &](../../../cppstruct/F/FV/FVector.md) | Goal position of the final trace it did. Will not be in the path if there is a hit. |
| StartPos | [FVector](../../../cppstruct/F/FV/FVector.md) | First start trace location |
| LaunchVelocity | [FVector](../../../cppstruct/F/FV/FVector.md) | Velocity the "virtual projectile" is launched at |
| bTracePath | `bool` | Trace along the entire path to look for blocking hits |
| ProjectileRadius | `float` | Radius of the virtual projectile to sweep against the environment |
| ObjectTypes | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | ObjectTypes to trace against, if bTracePath is true. |
| bTraceComplex | `bool` | Use TraceComplex (trace against triangles not primitives) |
| ActorsToIgnore | `TArray < AActor * > &` | Actors to exclude from the traces |
| DrawDebugType | `EDrawDebugTrace :: Type` | Debug type (one-frame, duration, persistent) |
| DrawDebugTime | `float` | Duration of debug lines (only relevant for DrawDebugType::Duration) |
| SimFrequency | `float` | Determines size of each sub-step in the simulation (chopping up MaxSimTime) |
| MaxSimTime | `float` | Maximum simulation time for the virtual projectile. |
| OverrideGravityZ | `float` | Optional override of Gravity (if 0, uses WorldGravityZ) |

**Return**

- Type: 
- Description: _None_

### Blueprint_PredictProjectilePath_ByTraceChannel

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something (if tracing with collision).

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| OutHit | [FHitResult &](../../../cppstruct/F/FH/FHitResult.md) | Predicted hit result, if the projectile will hit something |
| OutPathPositions | `TArray < FVector > &` | Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |
| OutLastTraceDestination | [FVector &](../../../cppstruct/F/FV/FVector.md) | Goal position of the final trace it did. Will not be in the path if there is a hit. |
| StartPos | [FVector](../../../cppstruct/F/FV/FVector.md) | First start trace location |
| LaunchVelocity | [FVector](../../../cppstruct/F/FV/FVector.md) | Velocity the "virtual projectile" is launched at |
| bTracePath | `bool` | Trace along the entire path to look for blocking hits |
| ProjectileRadius | `float` | Radius of the virtual projectile to sweep against the environment |
| TraceChannel | `TEnumAsByte < ECollisionChannel >` | TraceChannel to trace against, if bTracePath is true. |
| bTraceComplex | `bool` | Use TraceComplex (trace against triangles not primitives) |
| ActorsToIgnore | `TArray < AActor * > &` | Actors to exclude from the traces |
| DrawDebugType | `EDrawDebugTrace :: Type` | Debug type (one-frame, duration, persistent) |
| DrawDebugTime | `float` | Duration of debug lines (only relevant for DrawDebugType::Duration) |
| SimFrequency | `float` | Determines size of each sub-step in the simulation (chopping up MaxSimTime) |
| MaxSimTime | `float` | Maximum simulation time for the virtual projectile. |
| OverrideGravityZ | `float` | Optional override of Gravity (if 0, uses WorldGravityZ) |

**Return**

- Type: 
- Description: _None_

### Blueprint_PredictProjectilePath_Advanced

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc.
	 Returns true if it hit something.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| PredictParams | [FPredictProjectilePathParams &](../../../cppstruct/F/FP/FPredictProjectilePathParams.md) | Input params to the trace (start location, velocity, time to simulate, etc). |
| PredictResult | [FPredictProjectilePathResult &](../../../cppstruct/F/FP/FPredictProjectilePathResult.md) | Output result of the trace (Hit result, array of locationvelocitytimes for each trace step, etc). |

**Return**

- Type: 
- Description: _None_

### SuggestProjectileVelocity_CustomArc

Returns the launch velocity needed for a projectile at rest at StartPos to land on EndPos.
	 Assumes a medium arc (e.g. 45 deg on level ground). Projectile velocity is variable and unconstrained.
	 Does no tracing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| OutLaunchVelocity | [FVector &](../../../cppstruct/F/FV/FVector.md) | Returns the launch velocity required to reach the EndPos |
| StartPos | [FVector](../../../cppstruct/F/FV/FVector.md) | Start position of the simulation |
| EndPos | [FVector](../../../cppstruct/F/FV/FVector.md) | Desired end location for the simulation |
| OverrideGravityZ | `float` | Optional override of WorldGravityZ |
| ArcParam | `float` | Change height of arc between 0.0-1.0 where 0.5 is the default medium arc |

**Return**

- Type: 
- Description: _None_

### GetWorldOriginLocation

获取世界原点位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |

**Return**

- Type: 
- Description: _None_

### SetWorldOriginLocation

设置世界原点位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| NewLocation | [FIntVector](../../../cppstruct/F/FI/FIntVector.md) | 世界原点 |

**Return**

- Type: 
- Description: _None_

### SetWorldOriginLocationByLua

设置世界原点位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| X | `int32` |  |
| Y | `int32` |  |
| Z | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SyncSetNewWorldOrigin

同步设置世界原点位置

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| X | `int32` |  |
| Y | `int32` |  |
| Z | `int32` |  |

**Return**

- Type: 
- Description: _None_

### RebaseLocalOriginOntoZero

返回基于原点坐标的local坐标

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| WorldLocation | [FVector](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### RebaseZeroOriginOntoLocal

返回local坐标基于原点的坐标

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` | world上下文对象 |
| WorldLocation | [FVector](../../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_

### GrassOverlappingSphereCount

Counts how many grass foliage instances overlap a given sphere.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| StaticMesh | `UStaticMesh *` |  |
| CenterPosition | [FVector](../../../cppstruct/F/FV/FVector.md) | The center position of the sphere. |
| Radius | `float` | The radius of the sphere. |

**Return**

- Type: 
- Description: _None_

### DeprojectScreenToWorld

获取给定2D屏幕空间中的坐标投影到3D世界空间中的坐标

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` | 玩家的PlayerController |
| ScreenPosition | [FVector2D &](../../../cppstruct/F/FV/FVector2D.md) | 屏幕空间中的坐标 |
| WorldPosition | [FVector &](../../../cppstruct/F/FV/FVector.md) | 输出的世界空间坐标 |
| WorldDirection | [FVector &](../../../cppstruct/F/FV/FVector.md) | 输出的方向向量，世界空间中，给定点远离相机方向的方向向量 |

**Return**

- Type: 
- Description: _None_

### ProjectWorldToScreen

获取给定3D世界空间中的坐标投影到2D屏幕空间中的坐标

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Player | `APlayerController *` | 玩家的PlayerController |
| WorldPosition | [FVector &](../../../cppstruct/F/FV/FVector.md) | 世界空间中的坐标 |
| ScreenPosition | [FVector2D &](../../../cppstruct/F/FV/FVector2D.md) | 输出的屏幕空间坐标 |
| bPlayerViewportRelative | `bool` | 是否与玩家视口相关 |

**Return**

- Type: 
- Description: _None_

### MarkNetPropertyDirtyFromName

Mark a particular net property of an UObject as dirty (for networking), thus it will be take into consideration in next replication

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Object | `UObject *` | UObject to be marked dirty |
| PropertyName | `FName` | Name of the particular net property to be marked dirty |
| LifetimeCondition | [ELifetimeCondition](../../../cppenum/E/EL/ELifetimeCondition.md) |  |

**Return**

- Type: 
- Description: _None_

### GetKeyValue

Break up a key=value pair into its key and value.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Pair | `FString &` | The string containing a pair to split apart. |
| Key | `FString &` | (out) Key portion of Pair. If no = in string will be the same as Pair. |
| Value | `FString &` | (out) Value portion of Pair. If no = in string will be empty. |

**Return**

- Type: 
- Description: _None_

### ParseOption

Find an option in the options string and return it.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Options | `FString` | The string containing the options. |
| Key | `FString &` | The key to find the value of in Options. |

**Return**

- Type: 
- Description: _None_

### HasOption

Returns whether a key exists in an options string.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Options | `FString` | The string containing the options. |
| InKey | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetIntOption

Find an option in the options string and return it as an integer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Options | `FString &` | The string containing the options. |
| Key | `FString &` | The key to find the value of in Options. |
| DefaultValue | `int32` |  |

**Return**

- Type: 
- Description: _None_

### HasLaunchOption

Checks the commandline to see if the desired option was specified on the commandline (e.g. -demobuild)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| OptionToCheck | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### GetDeviceQualityLevel

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDeviceTCQualityGrade

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDeviceMemoryLevel

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDeviceMemorySize

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EnableObjArrayAutoResize

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnabled | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetConsoleIntVariable

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Name | `FString &` |  |
| Value | `int32` |  |

**Return**

- Type: 
- Description: _None_

### UpdateComponentToWorld

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ActorComponent | `UActorComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsLongScreen

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### IsWinReleaseBuild

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RecordDSLaunchState

record ds launch state, collect for ds shutdown error report, add by czcheng

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| state | `int32` | launch state, see details in EDSLaunchState |

**Return**

- Type: 
- Description: _None_

### RecordDSShutdownErrorInfo

record ds shutdown error info, collect for ds shutdown error report, add by czcheng

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ErrorCode | `int32` | shutdown error code, see details in EDSShutdownErrorCode |
| ErrMsg | `FString &` | error message |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

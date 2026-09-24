# UAnimInstance

## Parents

- [UObject](./UObject.md)
- IObjectPoolInterface

## Variables

| Name | Type | Description |
| --- | --- | --- |
| CurrentSkeleton | `USkeleton *` | This is used to extract animation. If Mesh exists, this will be overwritten by Mesh->Skeleton |
| RootMotionMode | `TEnumAsByte < ERootMotionMode :: Type >` |  |
| bRunUpdatesInWorkerThreads_DEPRECATED | `bool` | DEPRECATED: No longer used.<br>	  Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. this requires certain conditions to be met:<br>	  - All access of variables in the blend tree should be a direct access of a member variable<br>	  - No BlueprintUpdateAnimation event should be used (i.e. the event graph should be empty). Only native update is permitted. |
| bCanUseParallelUpdateAnimation_DEPRECATED | `bool` | DEPRECATED: No longer used.<br>	  Whether we can use parallel updates for our animations.<br>	  Conditions affecting this include:<br>	  - Use of BlueprintUpdateAnimation<br>	  - Use of non 'fast-path' EvaluateGraphExposedInputs in the node graph |
| bUseMultiThreadedAnimationUpdate | `bool` | Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. This flag is propagated from the UAnimBlueprint to this instance by the compiler.<br>	  The compiler will attempt to pick up any issues that may occur with threaded update.<br>	  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded<br>	  Animation Update" should be set. |
| bWarnAboutBlueprintUsage_DEPRECATED | `bool` | Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint<br>	  is made from the animation graph. This can help track down optimizations that need to be made. |
| bBlueprintSkipUpdate | `bool` |  |
| bUseBlueprintUpdateAnimation | `uint8` |  |
| bUseBlueprintPostEvaluateAnimation | `uint8` |  |
| AnimAssets_NoGCRef | `TMap < int64 , UAnimationAsset * >` |  |
| bQueueMontageEvents | `bool` | True when Montages are being ticked, and Montage Events should be queued.<br>	  When Montage are being ticked, we queue AnimNotifies and Events. We trigger notifies first, then Montage events. |
| ForbiddenPlayMontageSlot | `TArray < FString >` |  |
| ActiveAnimNotifyState | `TArray < FAnimNotifyEvent >` | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |
| bNeedUpdateNotAttributeCurve | `bool` | 此动画蓝图是否需要更新非Attribute的Curve数据 |
| RefCachedSubAnimInstances | `TArray < UAnimInstance * >` |  |
| bIsOnlyMasterTriggerNotify | `bool` |  |
| bIsMaster | `bool` |  |
| bDynamicDisableBoneRetarget | `bool` |  |
| CopyPoseFromSkelComp | `USkeletalMeshComponent *` |  |
| BoneRetargetSource | `FName` |  |
| bUseBoneStateDirtyFeature | `bool` |  |
| bBoneStateDirty | `bool` |  |
| C_InverseRetargetIgnoreBoneList | `TArray < int32 >` |  |
| C_IgnoreRetargetBoneList | `TArray < FName >` |  |
| FollowedAnimInstance | `UAnimInstance *` | 记录被跟随者的动画实例   当该指针为nullptr时，代表启用了自身 Proxy 的 Follow 轨道(即FollowGroupArrays开始记录) |
| FollowerAnimInstances | `TArray < TWeakObjectPtr < UAnimInstance > >` |  |
| ParentAnimInstance | `TWeakObjectPtr < UAnimInstance >` |  |
| SubAnimInstances | `TArray < TWeakObjectPtr < UAnimInstance > >` |  |
| SubAnimInstancesTempRef | `TArray < UAnimInstance * >` |  |
| CachedSwitchNotifySequence | `TArray < UAnimSequenceBase * >` |  |
| CachedBoneTransformInfoIndex | `int64` |  |
| CachedBoneTransformMapAsync | `TMap < FName , FCachedBoneTransformInfo >` |  |
| CachedBoneTransformMapInGame | `TMap < FName , FCachedBoneTransformInfo >` |  |
| bIsInPoseUpdate | `bool` |  |
| bEnableBoneCacheInGameThread | `bool` |  |
| bEnableFastPathExposedNodeTree | `bool` |  |
| UpdateConditions | `TArray < UAnimInstanceUpdateCondition * >` |  |
| bCheckUpdateConditionResult | `bool` |  |
| bEnableAnimBlueprintSkeletonDifferFromMeshSkeleton | `bool` |  |
| bEnableFilterForceTriggerNotifyWhenMontageJumpTick | `bool` |  |
| MultiSubInstanceTransferDefaultPoseIndex | `int32` |  |
| bEnableTriggerAnimNotify | `bool` |  |
| InitNodeSourcePropertyLookupTable | `TMap < FName , UProperty * >` |  |
| bParentPoseOverride | `bool` |  |
| bAutoCopyPose | `bool` |  |
| bHasAvatarSlotEvent | `bool` |  |
| bRestoreSlotVar | `bool` |  |
| bSkipSlotRelevanceCheckForNotifies | `bool` |  |
| bEnableAsyncAnimInstance | `bool` |  |
| bCanCopyRequiredBones | `bool` |  |
| RecordFileName | `FString` | 回放的录制文件名 |
| TotalFrames | `int32` | 总帧数 |
| CurrentFrame | `int32` | 当前帧号 |
| bIsPaused | `bool` | 暂停 |
| bRestoreErrorPending | `bool` | 是否有待游戏线程处理的回放错误（由 ParallelRestoreAnimation 在工作线程设置） |
| PostCompileValidationClassName | `FSoftClassPath` | Name of Class to do Post Compile Validation.<br>	 See Class UAnimBlueprintPostCompileValidation. |
| BoneRetargetBaseRefMesh | `USkeletalMesh *` |  |

## Functions

### TryGetPawnOwner

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SavePoseSnapshot

Takes a snapshot of the current skeletal mesh component pose & saves it internally.
	  This snapshot can then be retrieved by name in the animation blueprint for blending.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1 and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SnapshotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SnapshotPose

Takes a snapshot of the current skeletal mesh component pose and saves it to the specified snapshot.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
	  and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Snapshot | `FPoseSnapshot &` |  |

**Return**

- Type: 
- Description: _None_

### GetOwningActor

Returns the owning actor of this AnimInstance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetOwningComponent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BlueprintShouldSkipUpdateAnimation

Executed before the Animation is updated, Check custom condition, whether to skip update

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTimeX | `float` |  |

**Return**

- Type: 
- Description: _None_

### BlueprintInitializeAnimation

Executed when the Animation is initialized

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BlueprintUnInitializeAnimation

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BlueprintUpdateAnimation

Executed when the Animation is updated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DeltaTimeX | `float` |  |

**Return**

- Type: 
- Description: _None_

### BlueprintPostEvaluateAnimation

Executed after the Animation is evaluated

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BlueprintBeginPlay

Executed when begin play is called on the owning component

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PlaySlotAnimation

SlotAnimation

	 DEPRECATED. Use PlaySlotAnimationAsDynamicMontage instead, it returns the UAnimMontage created instead of time, allowing more control
	 Play normal animation asset on the slot node. You can only play one asset (whether montage or animsequence) at a time.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Asset | `UAnimSequenceBase *` |  |
| SlotNodeName | `FName` |  |
| BlendInTime | `float` |  |
| BlendOutTime | `float` |  |
| InPlayRate | `float` |  |
| LoopCount | `int32` |  |

**Return**

- Type: 
- Description: _None_

### PlaySlotAnimationAsDynamicMontage

Play normal animation asset on the slot node by creating a dynamic UAnimMontage. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Asset | `UAnimSequenceBase *` |  |
| SlotNodeName | `FName` |  |
| BlendInTime | `float` |  |
| BlendOutTime | `float` |  |
| InPlayRate | `float` |  |
| LoopCount | `int32` |  |
| BlendOutTriggerTime | `float` |  |
| InTimeToStartMontageAt | `float` |  |

**Return**

- Type: 
- Description: _None_

### PlaySlotAnimationAsDynamicMontageCustom

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Asset | `UAnimSequenceBase *` |  |
| SlotNodeName | `FName` |  |
| Extra | `FCustomMontageAnimInfo` |  |
| BlendInTime | `float` |  |
| BlendOutTime | `float` |  |
| InPlayRate | `float` |  |
| LoopCount | `int32` |  |
| BlendOutTriggerTime | `float` |  |
| InTimeToStartMontageAt | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetMatineeAnimPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetMontage | `UAnimMontage *` |  |
| InPosition | `float` |  |
| Extra | `FCustomMontageAnimInfo` |  |
| Weight | `float` |  |

**Return**

- Type: 
- Description: _None_

### StopSlotAnimation

Stops currently playing slot animation slot or all

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendOutTime | `float` |  |
| SlotNodeName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsPlayingSlotAnimation

Return true if it's playing the slot animation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Asset | `UAnimSequenceBase *` |  |
| SlotNodeName | `FName` |  |
| bcheckTransientPackage | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ForceTriggerAnimEndedEvent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMontageCustomSectionsPlayInfo

AnimMontage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| InPlayInfo | `TArray < FMontageSectionsPlayInfo > &` |  |

**Return**

- Type: 
- Description: _None_

### ClearMontageCustomSectionsPlayInfo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_Play

Plays an animation montage. Returns the length of the animation montage in seconds. Returns 0.f if failed to play.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MontageToPlay | `UAnimMontage *` |  |
| InPlayRate | `float` |  |
| ReturnValueType | `EMontagePlayReturnType` |  |
| InTimeToStartMontageAt | `float` |  |

**Return**

- Type: 
- Description: _None_

### Montage_CustomPlay

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MontageToPlay | `UAnimMontage *` |  |
| Extra | `FCustomMontageAnimInfo` |  |
| InPlayRate | `float` |  |
| ReturnValueType | `EMontagePlayReturnType` |  |
| InTimeToStartMontageAt | `float` |  |

**Return**

- Type: 
- Description: _None_

### Montage_Stop

Stops the animation montage. If reference is NULL, it will stop ALL active montages.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendOutTime | `float` |  |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_StopBySlot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendOutTime | `float` |  |
| SlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### Montage_CustomStop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBlendOutTime | `float` |  |
| Extra | `FCustomMontageAnimInfo` |  |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_Pause

Pauses the animation montage. If reference is NULL, it will pause ALL active montages.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_Resume

Resumes a paused animation montage. If reference is NULL, it will resume ALL active montages.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_JumpToSection

Makes a montage jump to a named section. If Montage reference is NULL, it will do that to all active montages.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SectionName | `FName` |  |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_JumpToSectionsEnd

Makes a montage jump to the end of a named section. If Montage reference is NULL, it will do that to all active montages.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SectionName | `FName` |  |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_SetNextSection

Relink new next section AFTER SectionNameToChange in run-time
	 	You can link section order the way you like in editor, but in run-time if you'd like to change it dynamically,
	 	use this function to relink the next section
	 	For example, you can have Start->Loop->Loop->Loop.... but when you want it to end, you can relink
	 	next section of Loop to be End to finish the montage, in which case, it stops looping by Loop->End.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SectionNameToChange | `FName` | : This should be the name of the Montage Section after which you want to insert a new next section |
| NextSection | `FName` | : new next section |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_SetPlayRate

Change AnimMontage play rate. NewPlayRate = 1.0 is the default playback rate.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| NewPlayRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### Montage_ReversePlayByAbsRateAndSlot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FName` |  |
| AbsPlayRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### Montage_SetDelayFrame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| DelayFrame | `int32` |  |

**Return**

- Type: 
- Description: _None_

### Montage_IsActive

Returns true if the animation montage is active. If the Montage reference is NULL, it will return true if any Montage is active.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_IsPlaying

Returns true if the animation montage is currently active and playing.
	If reference is NULL, it will return true is ANY montage is currently active and playing.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_IsExisting

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### MontageGroup_IsPlaying

判断有无某个组下的蒙太奇正在播放

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GroupName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### Montage_GetCurrentSection

Returns the name of the current animation montage section.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_GetPosition

Get Current Montage Position

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_SetPosition

Set position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| NewPosition | `float` |  |

**Return**

- Type: 
- Description: _None_

### Montage_GetIsStopped

return true if Montage is not currently active. (not valid or blending out)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_GetBlendTime

Get the current blend time of the Montage.
	If Montage reference is NULL, it will return the current blend time on the first active Montage found.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### Montage_GetPlayRate

Get PlayRate for Montage.
	If Montage is not playing, 0 is returned.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |

**Return**

- Type: 
- Description: _None_

### IsAnyMontagePlaying

Returns true if any montage is playing currently. Doesn't mean it's active though, it could be blending out.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentActiveMontage

Get a current Active Montage in this AnimInstance.
		Note that there might be multiple Active at the same time. This will only return the first active one it finds.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurrentActiveMontages

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCurMontageBySlot

Get the UAnimMontage currently running that matches this SlotName.  Will return NULL if no instance is found.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### Montage_GetNextSection

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| SectionName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### AddAnimAssetNoGCRef

添加动画资源到非GC引用列表，返回全局唯一ID

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimAsset | `UAnimationAsset *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveAnimAssetNoGCRef

从非GC引用列表移除动画资源（通过ID）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimAssetNoGCID | `int64` |  |

**Return**

- Type: 
- Description: _None_

### RemoveAllAnimAssetNoGCRef

从非GC引用列表移除所有动画资源（通过资源指针）

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimAsset | `UAnimationAsset *` |  |

**Return**

- Type: 
- Description: _None_

### ClearAnimAssetsNoGCReferences

清空非GC引用列表

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### StopAllMontages

Stop all montages that are active

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BlendOut | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearAllMontages

Stop all montages that are active

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BlendOut | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearStoppedMontageInstances

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bClearSubAnim | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetForbiddenPlayMontageSlot

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForbiddenPlayMontageSlot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bIsAdd | `bool` |  |
| SlotName | `FString` | should be GroupName + SlotName |

**Return**

- Type: 
- Description: _None_

### SetRootMotionMode

Set RootMotionMode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Value | `TEnumAsByte < ERootMotionMode :: Type >` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceAssetPlayerLength

NOTE: Derived anim getters

	  Anim getter functions can be defined for any instance deriving UAnimInstance.
	  To do this the function must be marked BlueprintPure, and have the AnimGetter metadata entry set to
	  "true". Following the instructions below, getters should appear correctly in the blueprint node context
	  menu for the derived classes

	  A context string can be provided in the GetterContext metadata and can contain any (or none) of the
	  following entries separated by a pipe (|)
	  Transition  - Only available in a transition rule
	  AnimGraph   - Only available in an animgraph (also covers state anim graphs)
	  CustomBlend - Only available in a custom blend graph

	  Anim getters support a number of automatic parameters that will be baked at compile time to be passed
	  to the functions. They will not appear as pins on the graph node. They are as follows:
	  AssetPlayerIndex - Index of an asset player node to operate on, one getter will be added to the blueprint action list per asset node available
	  MachineIndex     - Index of a state machine in the animation blueprint, one getter will be added to the blueprint action list per state machine
	  StateIndex       - Index of a state inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per state
	  TransitionIndex  - Index of a transition inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per transition

	  Gets the length in seconds of the asset referenced in an asset player node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceAssetPlayerTime

Get the current accumulated time in seconds for an asset player node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetInstanceAssetPlayerTime

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |
| time | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetNodeIndexWithTag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NodeTag | `FName` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceAssetPlayerTime_BP

Get the current accumulated time in seconds for an asset player node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetInstanceAssetPlayerTime_BP

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |
| time | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceAssetPlayerTimeFraction

Get the current accumulated time as a fraction for an asset player node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceAssetPlayerTimeFromEnd

Get the time in seconds from the end of an animation in an asset player node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceAssetPlayerTimeFromEndFraction

Get the time as a fraction of the asset length of an animation in an asset player node

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| AssetPlayerIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceMachineWeight

Get the blend weight of a specified state machine

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceStateWeight

Get the blend weight of a specified state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| StateIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceCurrentStateElapsedTime

Get the current elapsed time of a state within the specified state machine

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceTransitionCrossfadeDuration

Get the crossfade duration of a specified transition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| TransitionIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceTransitionTimeElapsed

Get the elapsed time in seconds of a specified transition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| TransitionIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetInstanceTransitionTimeElapsedFraction

Get the elapsed time as a fraction of the crossfade duration of a specified transition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| TransitionIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetRelevantAnimTimeRemaining

Get the time remaining in seconds for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| StateIndex | `int32` |  |
| NullAnimDefaultValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetRelevantAnimTimeRemainingFraction

Get the time remaining as a fraction of the duration for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| StateIndex | `int32` |  |
| NullAnimDefaultValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetRelevantAnimLength

Get the length in seconds of the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| StateIndex | `int32` |  |
| NullAnimDefaultValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetRelevantAnimTime

Get the current accumulated time in seconds for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| StateIndex | `int32` |  |
| NullAnimDefaultValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetRelevantAnimTimeFraction

Get the current accumulated time as a fraction of the length of the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |
| StateIndex | `int32` |  |
| NullAnimDefaultValue | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetCurveValue

Returns the value of a named curve.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CurveName | `FName` |  |
| Immediately | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetCurrentStateName

Returns the name of a currently active state in a state machine.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MachineIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetMorphTarget

Sets a morph target to a certain weight.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MorphTargetName | `FName` |  |
| Value | `float` |  |

**Return**

- Type: 
- Description: _None_

### ClearMorphTargets

Clears the current morph targets.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CalculateDirection

Returns degree of the angle betwee velocity and Rotation forward vector
	  The range of return will be from [-180, 180], and this can be used to feed blendspace directional value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Velocity | `FVector &` |  |
| BaseRotation | `FRotator &` |  |

**Return**

- Type: 
- Description: _None_

### LockAIResources

locks indicated AI resources of animated pawn
	 	DEPRECATED. Use LockAIResourcesWithAnimation instead

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bLockMovement | `bool` |  |
| LockAILogic | `bool` |  |

**Return**

- Type: 
- Description: _None_

### UnlockAIResources

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources.
	 	DEPRECATED. Use UnlockAIResourcesWithAnimation instead

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bUnlockMovement | `bool` |  |
| UnlockAILogic | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTimeToClosestMarker

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SyncGroup | `FName` |  |
| MarkerName | `FName` |  |
| OutMarkerTime | `float &` |  |

**Return**

- Type: 
- Description: _None_

### HasMarkerBeenHitThisFrame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SyncGroup | `FName` |  |
| MarkerName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsSyncGroupBetweenMarkers

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSyncGroupName | `FName` |  |
| PreviousMarker | `FName` |  |
| NextMarker | `FName` |  |
| bRespectMarkerOrder | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetSyncGroupPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSyncGroupName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### TriggerAllSequenceSwitchNotify

Trigger AnimNotifies

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### CheckCanTriggerNotify_AnimIsolation_Outer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimNotifyEvent | `FAnimNotifyEvent &` |  |
| InNotify | `UAnimNotify *` |  |

**Return**

- Type: 
- Description: _None_

### CheckCanTriggerNotifyState_AnimIsolation_Outer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimNotifyEvent | `FAnimNotifyEvent &` |  |
| InNotifyState | `UAnimNotifyState *` |  |

**Return**

- Type: 
- Description: _None_

### CheckCanTriggerAnimNotifyFunction_AnimIsolation_Outer

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimNotifyEvent | `FAnimNotifyEvent &` |  |

**Return**

- Type: 
- Description: _None_

### ReplaceSubAnimNodeAnimClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| NewAnimClass | `TSubclassOf < UAnimInstance >` |  |
| BlendTime | `float` |  |
| bEnableNoWaitParallelEvalTask | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ReplaceSubAnimNodeAnimClass_EmptyClassDefaut

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| NewAnimClass | `TSubclassOf < UAnimInstance >` |  |
| BlendTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### ResetSubAnimNodeAnimClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| FilterAnimClass | `TSubclassOf < UAnimInstance >` |  |
| BlendTime | `float` |  |
| bEnableNoWaitParallelEvalTask | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ResetSubAnimNodeAnimClass_EmptyClassDefaut

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| FilterAnimClass | `TSubclassOf < UAnimInstance >` |  |
| BlendTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### ResetAllSubAnimNode

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearAllSubAnimBlendTime

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetAllSubAnimNodePosInertialization

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSubAnimInstanceBySlot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### IsUseSubAnimInstanceBySlot

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetSubAnimNodeEnableBlend

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| bEnable | `bool` |  |
| NewSubAnimBlendTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### AddSubAnimNodeAnimClass

同槽多子动画实例

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| NewAnimClass | `TSubclassOf < UAnimInstance >` |  |
| Priority | `int32` |  |
| BlendTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### RemoveSubAnimNodeAnimClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |
| FilterClass | `TSubclassOf < UAnimInstance >` |  |
| BlendTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### ResetSubAnimNode_MultiInstanceClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SubInstanceSlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### ResetAllSubAnimNode_MultiInstance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddStopTickSubAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Instance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### RemoveCachedStopTickSubAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Instance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### ClearAllStopTickSubAnimInstance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OnRecycleCachedSubAnimInstances

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bToPersistentPool | `bool` |  |

**Return**

- Type: 
- Description: _None_

### MarkBoneStateDirty

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsDirty | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsBoneStateDirty

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsUseBoneStateDirtyFeature

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### HasSlotNode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSlotName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### UpdateAnimSlotRetargetInfo

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMontage | `UAnimMontage *` |  |
| InSlotNameRetargetInfo | `TMap < FName , FName > &` |  |

**Return**

- Type: 
- Description: _None_

### GetInverseRetargetIgnoreBoneList

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetFollowedAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InputFollowedInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### ResetFollowedAnimInstance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsFollowing

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TargetFollowedInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### SetDelayPlay

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| IsDelay | `bool` |  |
| InputDelayFrames | `int` |  |

**Return**

- Type: 
- Description: _None_

### GetParentAnimInstance

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetParentAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InParentAnimInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### GetSubAnimInstances

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAllSubAnimInstances

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SwapCachedBoneTransformMap

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetCachedBoneTransform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName` |  |
| OutTransform | `FTransform &` |  |
| forceSync | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetCachedBoneTransformByFlag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName` |  |
| InCacheFlag | `FName` |  |
| OutTransform | `FTransform &` |  |
| NeedLastFrameCount | `int32` |  |
| forceSync | `bool` |  |

**Return**

- Type: 
- Description: _None_

### CompareCachedBoneTransformByFlag

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName0 | `FName` |  |
| InCacheFlag0 | `FName` |  |
| InBoneName1 | `FName` |  |
| InCacheFlag1 | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SetTriggerAnimNotify

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NeedTrigger | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FilterForceTriggerNotifyWhenMontageJumpTick

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMontage | `UAnimMontage *` |  |
| bPlayingBackwards | `bool` |  |
| CurrentTrackPos | `float` |  |
| CurrentDeltaSeconds | `float` |  |
| InAnimNotifies | `TArray < FAnimNotifyEvent > &` |  |
| OutForceTriggerAnimNotifies | `TArray < FAnimNotifyEvent > &` |  |

**Return**

- Type: 
- Description: _None_

### GetLobbySeqIgnoreNotifyList

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetNotifyQueue

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RestoreAnimation

编辑器调用函数，根据录制文件名进行重放，播放第一帧后暂停

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InRecordName | `FString &` |  |

**Return**

- Type: 
- Description: _None_

### LogPoseDebug

输出当前Pose至Log界面

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PauseOrContinueRestore

暂停或者继续重放

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RestoreNextFrame

重放下一帧

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### JumpToGivenFrame

跳转至指定帧

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RestoreClear

清空当前回放信息

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RestartAnimation

重新开始回放

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SeekToFrame

跳转到指定帧并恢复该帧状态（编辑器调用）
	   要求当前处于 RestoreWait 或 RestoreEnd 状态
	   内部设置 DataAr 位置到 RestoreHeader[FrameIndex-1]，
	   下一帧 ParallelRestoreAnimation 将恢复该帧并更新调试数据

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| FrameIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SeekToTime

根据时间跳转到最近帧（编辑器调用）
	   使用估算帧率计算帧索引后调用 SeekToFrame

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| TimeInSeconds | `float` |  |

**Return**

- Type: 
- Description: _None_

### RestorePreviousFrame

回退到前一帧（编辑器调用）

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
| OnMontageBlendingOut |  | Called when a montage starts blending out, whether interrupted or finished |
| OnMontageStarted |  | Called when a montage has started |
| OnMontageEnded |  | Called when a montage has ended, whether interrupted or finished |
| OnMontageRealEnded |  | Called when a montage real ended, whether interrupted or finished |
| OnAllMontageInstancesEnded |  | Called when all Montage instances have ended. |

## Language

cpp

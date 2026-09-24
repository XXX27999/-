# USkeletalMeshComponent

SkeletalMeshComponent is used to create an instance of an animated SkeletalMesh asset.

  @see USkeletalMesh

## Parents

- [USkinnedMeshComponent](./USkinnedMeshComponent.md)
- IInterface_CollisionDataProvider

## Variables

| Name | Type | Description |
| --- | --- | --- |
| AnimationMode | `TEnumAsByte < EAnimationMode :: Type >` | Animation<br><br>	 @Todo anim: Matinee related data start - this needs to be replaced to new system.<br>	 @Todo anim: Matinee related data end - this needs to be replaced to new system.<br>	 Whether to use Animation Blueprint or play Single Animation Asset. |
| AnimBlueprintGeneratedClass | `UAnimBlueprintGeneratedClass *` |  |
| AnimClass | `TSubclassOf < UAnimInstance >` | The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime. |
| bAutoInitAnimInstance | `bool` | The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime. |
| AnimScriptInstance | `UAnimInstance *` | The active animation graph program instance. |
| SubInstances | `TArray < UAnimInstance * >` | Any running sub anim instances that need to be updates on the game thread |
| NewSubInstances | `TArray < UAnimInstance * >` |  |
| DirtySubInstances | `TArray < UAnimInstance * >` |  |
| StopTickSubInstances | `TArray < UAnimInstance * >` |  |
| PostProcessAnimInstance | `UAnimInstance *` | An instance created from the PostPhysicsBlueprint property of the skeletal mesh we're using,<br>	   Runs after physics has been blended |
| AnimationData | `FSingleAnimationPlayData` |  |
| CachedBoneSpaceTransforms | `TArray < FTransform >` | Cached BoneSpaceTransforms for Update Rate optimization. |
| CachedComponentSpaceTransforms | `TArray < FTransform >` | Cached SpaceBases for Update Rate optimization. |
| GlobalAnimRateScale | `float` | Used to scale speed of all animations on this skeletal mesh. |
| UseAsyncScene | [EDynamicActorScene](../../cppenum/E/ED/EDynamicActorScene.md) | The simulation scene to use for this instance. By default we use what's in the physics asset (which defaults to the sync scene) |
| bHasValidBodies | `uint32` | If true, there is at least one body in the current PhysicsAsset with a valid bone in the current SkeletalMesh |
| KinematicBonesUpdateType | `TEnumAsByte < EKinematicBonesUpdateToPhysics :: Type >` | If we are running physics, should we update non-simulated bones based on the animation bone positions. |
| UpdateKinematicBonesRate | `int32` |  |
| PhysicsTransformUpdateMode | `TEnumAsByte < EPhysicsTransformUpdateMode :: Type >` | Whether physics simulation updates component transform. |
| bBlendPhysics | `uint32` | Enables blending in of physics bodies whether Simulate or not |
| bEnablePhysicsOnDedicatedServer | `uint32` | If true, simulate physics for this component on a dedicated server.<br>	   This should be set if simulating physics and replicating with a dedicated server.<br>	 	Note: This property cannot be changed at runtime. |
| bEnableCreatePhysicsOnDedicatedServer | `uint32` |  |
| bForceBoneTransformUpdateWithPhysics | `uint32` | 当物理模拟激活时，强制在 EndPhysicsTick 中将物理结果写回骨骼 Transform。<br>	  用于 DS 上没有渲染但需要物理驱动骨骼位置更新的场景（如 Active Ragdoll）。<br>	  设置为 true 后，即使 ShouldBlendPhysicsBones() 返回 false，也会调用 FinalizeBoneTransform()。 |
| bNeedUpdatePhysicsTickRegisteredState | `bool` |  |
| bUpdateJointsFromAnimation | `uint32` | If we should pass joint position to joints each frame, so that they can be used by motorized joints to drive the<br>	 	ragdoll based on the animation. |
| bDisableClothSimulation | `uint32` | Disable cloth simulation and play original animation without simulation |
| bAllowAnimCurveEvaluation | `uint32` | Disable animation curves for this component. If this is set true, no curves will be processed |
| bDisableAnimCurves_DEPRECATED | `uint32` | DEPRECATED. Use bAllowAnimCurveEvaluation instead |
| DisallowedAnimCurves | `TArray < FName >` | You can choose to disable certain curves if you prefer.<br>	  This is transient curves that will be ignored by animation system if you choose this |
| bCollideWithEnvironment | `uint32` | can't collide with part of environment if total collision volumes exceed 16 capsules or 32 planes per convex |
| bCollideWithAttachedChildren | `uint32` | can't collide with part of attached children if total collision volumes exceed 16 capsules or 32 planes per convex |
| bLocalSpaceSimulation | `uint32` | It's worth trying this option when you feel that the current cloth simulation is unstable.<br>	  The scale of the actor is maintained during the simulation.<br>	  It is possible to add the inertia effects to the simulation, through the inertiaScale parameter of the clothing material.<br>	  So with an inertiaScale of 1.0 there should be no visible difference between local space and global space simulation.<br>	  Known issues: - Currently there's simulation issues when this feature is used in 3.x (DE4076) So if localSpaceSim is enabled there's no inertia effect when the global pose of the clothing actor changes. |
| bClothMorphTarget | `uint32` | cloth morph target option<br>	  This option will be applied only before playing because should do pre-calculation to reduce computation time for run-time play<br>	  so it's impossible to change this option in run-time |
| bResetAfterTeleport | `uint32` | reset the clothing after moving the clothing position (called teleport) |
| ClothBlendWeight | `float` | weight to blend between simulated results and key-framed positions<br>	  if weight is 1.0, shows only cloth simulation results and 0.0 will show only skinned results |
| RootBoneTranslation | [FVector](../../cppstruct/F/FV/FVector.md) | Offset of the root bone from the reference pose. Used to offset bounding box. |
| bDeferMovementFromSceneQueries | `uint32` | Optimization<br><br>	  Whether animation and world transform updates are deferred. If this is on, the kinematic bodies (scene query data) will not update until the next time the physics simulation is run |
| bNoSkeletonUpdate | `uint32` | Skips Ticking and Bone Refresh. |
| bPauseAnims | `uint32` | pauses this component's animations (doesn't tick them, but still refreshes bones) |
| bUseRefPoseOnInitAnim | `bool` | On InitAnim should we set to ref pose (if false use first tick of animation data) |
| bEnablePerPolyCollision | `uint32` | Uses skinned data for collision data. |
| BodySetup | `UBodySetup *` | Used for per poly collision. In 99% of cases you will be better off using a Physics Asset.<br>	 This BodySetup is per instance because all modification of vertices is done in place |
| bForceRefpose | `bool` | Misc<br><br>	 If true, force the mesh into the reference pose - is an optimization. |
| bOnlyAllowAutonomousTickPose | `uint32` | If true TickPose() will not be called from the Component's TickComponent function.<br>	 It will instead be called from Autonomous networking updates. See ACharacter. |
| bIsAutonomousTickPose | `uint32` | True if calling TickPose() from Autonomous networking updates. See ACharacter. |
| bOldForceRefPose | `uint32` | If bForceRefPose was set last tick. |
| bShowPrePhysBones | `uint32` | Bool that enables debug drawing of the skeleton before it is passed to the physics. Useful for debugging animation-driven physics. |
| bRequiredBonesUpToDate | `uint32` | If false, indicates that on the next call to UpdateSkelPose the RequiredBones array should be recalculated. |
| bAnimTreeInitialised | `uint32` | If true, AnimTree has been initialised. |
| bIncludeComponentLocationIntoBounds | `uint32` | If true, the Location of this Component will be included into its bounds calculation<br>	 (this can be useful when using SMU_OnlyTickPoseWhenRendered on a character that moves away from the root and no bones are left near the origin of the component) |
| bEnableLineCheckWithBounds | `uint32` | If true, line checks will test against the bounding box of this skeletal mesh component and return a hit if there is a collision. |
| CachedAnimCurveUidVersion | `uint16` | Cache AnimCurveUidVersion from Skeleton and this will be used to identify if it needs to be updated |
| LineCheckBoundsScale | [FVector](../../cppstruct/F/FV/FVector.md) | If bEnableLineCheckWithBounds is true, scale the bounds by this value before doing line check. |
| OnConstraintBroken | `FConstraintBrokenSignature` | Notification when constraint is broken. |
| SaveBoneSpaceTransfroms | `TArray < FTransform >` |  |
| ClothingSimulationFactory | `TSubclassOf < UClothingSimulationFactory >` | Class of the object responsible for |
| TeleportDistanceThreshold | `float` | Conduct teleportation if the character's movement is greater than this threshold in 1 frame.<br>	 Zero or negative values will skip the check.<br>	 You can also do force teleport manually using ForceNextUpdateTeleport()  ForceNextUpdateTeleportAndReset(). |
| TeleportRotationThreshold | `float` | Rotation threshold in degrees, ranging from 0 to 180.<br>	 Conduct teleportation if the character's rotation is greater than this threshold in 1 frame.<br>	 Zero or negative values will skip the check. |
| bEnableUpdateOverlapsEvent | `uint8` |  |
| SequenceToPlay_DEPRECATED | `UAnimSequence *` |  |
| AnimToPlay_DEPRECATED | `UAnimationAsset *` |  |
| bDefaultLooping_DEPRECATED | `uint32` |  |
| bDefaultPlaying_DEPRECATED | `uint32` |  |
| DefaultPosition_DEPRECATED | `float` |  |
| DefaultPlayRate_DEPRECATED | `float` |  |
| LastPoseTickFrame | `uint32` |  |
| LastPoseTickTime | `float` | Keep track of when animation has been ticked to ensure it is ticked only once per frame. |
| bNeedsQueuedAnimEventsDispatched | `bool` |  |
| bIsNeedUpdate | `bool` |  |
| bSkeletalMeshDirty | `bool` |  |
| BoneRetargetSource | `FName` |  |
| MeshShiftTransform | [FTransform](../../cppstruct/F/FT/FTransform.md) |  |
| MeshShiftRefBone | `FName` |  |
| MeshShiftAnchorRefBone | `FName` |  |
| bUseMeshShiftFeature | `bool` |  |
| bOnlyPartOfShiftRefBoneAsRoot | `bool` |  |
| MeshShiftCompensationType | [EMeshShiftCompensationType](../../cppenum/E/EM/EMeshShiftCompensationType.md) |  |
| MeshShiftCompensationBaseSkelComp | `TWeakObjectPtr < USkeletalMeshComponent >` |  |
| AnimOverrideMeshShiftParam | [FMeshShiftParam](../../cppstruct/F/FM/FMeshShiftParam.md) |  |
| DynamicBoneScaleFeature_Scale3D | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| DynamicBoneScaleFeature_BoneNameList | `TArray < FName >` |  |
| bUseDynamicBoneScaleFeature | `bool` |  |
| bIsOverrideScale | `bool` |  |
| bIsEnableBatchSection | `bool` | For Dynamic Bone Scale Feature End |
| BatchSectionList | `TArray < FDynamicBatchSectionInfo >` |  |
| OriginalMaterials | `TArray < UMaterialInterface * >` |  |
| bCrossFrameAnimForceSync | `bool` | When true, ShouldUseCrossFrameAnimUpdate() returns false regardless of<br>	    so external modifications during the force-sync period are preserved. |
| bEnableCrossFrameAnimUpdate | `bool` | Whether to enable async anim update for this component |
| AnimationBlueprint_DEPRECATED | `UAnimBlueprint *` | The blueprint for creating an AnimationScript. |
| bUpdateAnimationInEditor | `uint32` | If true, this will Tick until disabled |
| BoneRetargetBaseRefMesh | `USkeletalMesh *` | For Bone Retarget Feature Start |

## Functions

### SetAnimInstanceClass

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewClass | `UClass *` |  |
| bTickAnimationNow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### CopyBoneSpaceTransfroms

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InputTransforms | `TArray < FTransform >` |  |

**Return**

- Type: 
- Description: _None_

### GetBoneSpaceTransfromsForCopy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Other | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### GetAnimInstance

Returns the animation instance that is driving the class (if available). This is typically an instance of
	  the class set as AnimBlueprintGeneratedClass (generated by an animation blueprint)
	  Since this instance is transient, it is not safe to be used during construction script

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetSubAnimInstances

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetNewSubAnimInstances

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

### GetDirtySubAnimInstances

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetStopTickSubAnimInstances

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearDirtySubAnimInstances

清理所有脏标记的SubAnimInstance
	  从SubInstances、NewSubInstances、StopTickSubInstances中移除，并调用UninitializeAnimation、PendingDestroy等清理逻辑

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddNewSubAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### AddDirtySubAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### AddStopTickSubAnimInstance

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### GetPostProcessInstance

Returns the active post process instance is one is available. This is set on the mesh that this
	  component is using, and is evaluated immediately after the main instance.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAnimationMode

Below are the interface to control animation when animation mode, not blueprint mode

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimationMode | `EAnimationMode :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetAnimationMode

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetAnimationPosition

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Animation | `UAnimationAsset *` |  |

**Return**

- Type: 
- Description: _None_

### PlayAnimation

Animation play functions

	  These changes status of animation instance, which is transient data, which means it won't serialize with this component
	  Because of that reason, it is not safe to be used during construction script
	  Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAnimToPlay | `UAnimationAsset *` |  |
| bLooping | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAnimation

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewAnimToPlay | `UAnimationAsset *` |  |

**Return**

- Type: 
- Description: _None_

### Play

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bLooping | `bool` |  |

**Return**

- Type: 
- Description: _None_

### Stop

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsPlaying

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPosition

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPos | `float` |  |
| bFireNotifies | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetPosition

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetPlayRate

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Rate | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetPlayRate

Animation play functions

	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### OverrideAnimationData

This overrides current AnimationData parameter in the SkeletalMeshComponent. This will serialize when the component serialize
	  so it can be used during construction script. However note that this will override current existing data
	  This can be useful if you'd like to make a blueprint with custom default animation per component
	  This sets single player mode, which means you can't use AnimBlueprint with it

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimToPlay | `UAnimationAsset *` |  |
| bIsLooping | `bool` |  |
| bIsPlaying | `bool` |  |
| Position | `float` |  |
| PlayRate | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetMorphTarget

Set Morph Target with Name and Value(0-1)

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MorphTargetName | `FName` |  |
| Value | `float` |  |
| bRemoveZeroWeight | `bool` | : Used by editor code when it should stay in the active list with zero weight |

**Return**

- Type: 
- Description: _None_

### ClearMorphTargets

Clear all Morph Target that are set to this mesh

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetMorphTarget

Get Morph target with given name

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MorphTargetName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### SnapshotPose

Takes a snapshot of this skeletal mesh component's pose and saves it to the specified snapshot.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
	  and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Snapshot | `FPoseSnapshot &` |  |

**Return**

- Type: 
- Description: _None_

### GetClothMaxDistanceScale

GetSet the max distance scale of clothing mesh vertices

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetClothMaxDistanceScale

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Scale | `float` |  |

**Return**

- Type: 
- Description: _None_

### ForceClothNextUpdateTeleport

Used to indicate we should force 'teleport' during the next call to UpdateClothState,
	  This will transform positions and velocities and thus keep the simulation state, just translate it to a new pose.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ForceClothNextUpdateTeleportAndReset

Used to indicate we should force 'teleport and reset' during the next call to UpdateClothState.
	  This can be used to reset it from a bad state or by a teleport where the old state is not important anymore.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SuspendClothingSimulation

Stops simulating clothing, but does not show clothing ref pose. Keeps the last known simulation state

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResumeClothingSimulation

Resumes a previously suspended clothing simulation, teleporting the clothing on the next tick

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsClothingSimulationSuspended

Gets whether or not the clothing simulation is currently suspended

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ResetClothTeleportMode

Reset the teleport mode of a next update to 'Continuous'

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### BindClothToMasterPoseComponent

If this component has a valid MasterPoseComponent then this function makes cloth items on the slave component
	  take the transforms of the cloth items on the master component instead of simulating separately.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### UnbindClothFromMasterPoseComponent

If this component has a valid MasterPoseComponent and has previously had its cloth bound to the
	  MCP, this function will unbind the cloth and resume simulation.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bRestoreSimulationSpace | `bool` | if true and the master pose cloth was originally simulating in world |

**Return**

- Type: 
- Description: _None_

### SetUpdateAnimationInEditor

Sets whether or not to force tick component in order to update animation and refresh transform for this component
	 This is supported only in the editor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewUpdateState | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetDisableAnimCurves

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInDisableAnimCurves | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetDisableAnimCurves

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAllowAnimCurveEvaluation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInAllow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetAllowedAnimCurveEvaluate

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AllowAnimCurveEvaluation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NameOfCurve | `FName` |  |
| bAllow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ResetAllowedAnimCurveEvaluation

By reset, it will allow all the curves to be evaluated

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAllowedAnimCurvesEvaluation

resets, and then only allow the following list to be alloweddisallowed

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| List | `TArray < FName > &` |  |
| bAllow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTeleportRotationThreshold

Gets the teleportation rotation threshold.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTeleportRotationThreshold

Sets the teleportation rotation threshold.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Threshold | `float` | Threshold in degrees. |

**Return**

- Type: 
- Description: _None_

### GetTeleportDistanceThreshold

Gets the teleportation distance threshold.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetTeleportDistanceThreshold

Sets the teleportation distance threshold.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Threshold | `float` | Threshold value. |

**Return**

- Type: 
- Description: _None_

### SetBodyNotifyRigidBodyCollision

Changes the value of bNotifyRigidBodyCollision for a given body

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewNotifyRigidBodyCollision | `bool` | The value to assign to bNotifyRigidBodyCollision |
| BoneName | `FName` | Name of the body to turn hit notifies onoff. None implies root body |

**Return**

- Type: 
- Description: _None_

### SetNotifyRigidBodyCollisionBelow

Changes the value of bNotifyRigidBodyCollision on all bodies below a given bone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewNotifyRigidBodyCollision | `bool` | The value to assign to bNotifyRigidBodyCollision |
| BoneName | `FName` | Name of the body to turn hit notifies on (and below) |
| bIncludeSelf | `bool` | Whether to modify the given body (useful for roots with multiple children) |

**Return**

- Type: 
- Description: _None_

### SetEnableBodyGravity

Enables or disables gravity for the given bone.
	 	NAME_None indicates the root body will be edited.
	 	If the bone name given is otherwise invalid, nothing happens.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableGravity | `bool` | Whether gravity should be enabled or disabled. |
| BoneName | `FName` | The name of the bone to modify. |

**Return**

- Type: 
- Description: _None_

### IsBodyGravityEnabled

Checks whether or not gravity is enabled on the given bone.
	 	NAME_None indicates the root body should be queried.
	 	If the bone name given is otherwise invalid, false is returned.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | The name of the bone to check. |

**Return**

- Type: 
- Description: _None_

### SetEnableGravityOnAllBodiesBelow

Enables or disables gravity to all bodies below the given bone.
	   NAME_None indicates all bodies will be edited.
		In that case, consider using UPrimitiveComponent::EnableGravity.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableGravity | `bool` | Whether gravity should be enabled or disabled. |
| BoneName | `FName` | The name of the top most bone. |
| bIncludeSelf | `bool` | Whether the bone specified should be edited. |

**Return**

- Type: 
- Description: _None_

### K2_GetClosestPointOnPhysicsAsset

Given a world position, find the closest point on the physics asset. Note that this is independent of collision and welding. This is based purely on animation position

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldPosition | `FVector &` | The point we want the closest point to (i.e. for all bodies in the physics asset, find the one that has a point closest to WorldPosition) |
| ClosestWorldPosition | `FVector &` |  |
| Normal | `FVector &` |  |
| BoneName | `FName &` |  |
| Distance | `float &` |  |

**Return**

- Type: 
- Description: _None_

### GetBoneMass

Returns the mass (in kg) of the given bone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` | Name of the body to return. 'None' indicates root body. |
| bScaleMass | `bool` | If true, the mass is scaled by the bone's MassScale. |

**Return**

- Type: 
- Description: _None_

### GetSkeletalCenterOfMass

Returns the center of mass of the skeletal mesh, instead of the root body's location

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### AddForceToAllBodiesBelow

Add a force to all rigid bodies below.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Force | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |
| bAccelChange | `bool` | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |
| bIncludeSelf | `bool` | If false, Force is only applied to bodies below but not given bone name. |

**Return**

- Type: 
- Description: _None_

### AddImpulseToAllBodiesBelow

Add impulse to all single rigid bodies below. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` | Magnitude and direction of impulse to apply. |
| BoneName | `FName` | If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body. |
| bVelChange | `bool` | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |
| bIncludeSelf | `bool` | If false, Force is only applied to bodies below but not given bone name. |

**Return**

- Type: 
- Description: _None_

### IsEnableAnimBoneStateDirtyFeature

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAllBodiesSimulatePhysics

Set bSimulatePhysics to true for all bone bodies. Does not change the component bSimulatePhysics flag.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewSimulate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetPhysicsBlendWeight

This is global set up for setting physics blend weight
	  This does multiple things automatically
	  If PhysicsBlendWeight == 1.f, it will enable Simulation, and if PhysicsBlendWeight == 0.f, it will disable Simulation.
	  Also it will respect each body's setup, so if the body is fixed, it won't simulate. Vice versa
	  So if you'd like all bodies to change manually, do not use this function, but SetAllBodiesPhysicsBlendWeight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PhysicsBlendWeight | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetEnablePhysicsBlending

Disable physics blending of bones

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bNewBlendPhysics | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllBodiesBelowSimulatePhysics

Set all of the bones below passed in bone to be simulated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName &` |  |
| bNewSimulate | `bool` |  |
| bIncludeSelf | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ResetAllBodiesSimulatePhysics

Allows you to reset bodies Simulate state based on where bUsePhysics is set to true in the BodySetup.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetAllBodiesPhysicsBlendWeight

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PhysicsBlendWeight | `float` |  |
| bSkipCustomPhysicsType | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllBodiesBelowPhysicsBlendWeight

Set all of the bones below passed in bone to be simulated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName &` |  |
| PhysicsBlendWeight | `float` |  |
| bSkipCustomPhysicsType | `bool` |  |
| bIncludeSelf | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AccumulateAllBodiesBelowPhysicsBlendWeight

Accumulate AddPhysicsBlendWeight to physics blendweight for all of the bones below passed in bone to be simulated

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName &` |  |
| AddPhysicsBlendWeight | `float` |  |
| bSkipCustomPhysicsType | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllMotorsAngularPositionDrive

Enable or Disable AngularPositionDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableSwingDrive | `bool` |  |
| bEnableTwistDrive | `bool` |  |
| bSkipCustomPhysicsType | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllMotorsAngularVelocityDrive

Enable or Disable AngularVelocityDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnableSwingDrive | `bool` |  |
| bEnableTwistDrive | `bool` |  |
| bSkipCustomPhysicsType | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetAllMotorsAngularDriveParams

Set Angular Drive motors params for all constraint instances

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSpring | `float` |  |
| InDamping | `float` |  |
| InForceLimit | `float` |  |
| bSkipCustomPhysicsType | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetConstraintProfile

Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset. If profile name is not found the joint is set to use the default constraint profile.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| JointName | `FName` |  |
| ProfileName | `FName` |  |
| bDefaultIfNotFound | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetConstraintProfileForAll

Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset for all constraints. If profile name is not found the joint is set to use the default constraint profile.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ProfileName | `FName` |  |
| bDefaultIfNotFound | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FindConstraintBoneName

Find Constraint Name from index

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ConstraintIndex | `int32` | Index of constraint to look for |

**Return**

- Type: 
- Description: _None_

### BreakConstraint

Break a constraint off a Gore mesh.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Impulse | `FVector` | vector of impulse |
| HitLocation | `FVector` | location of the hit |
| InBoneName | `FName` | Name of bone to break constraint for |

**Return**

- Type: 
- Description: _None_

### SetAngularLimits

Sets the Angular Motion Ranges for a named bone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName` | Name of bone to adjust constraint ranges for |
| Swing1LimitAngle | `float` | Size of limit in degrees, 0 means locked, 180 means free |
| TwistLimitAngle | `float` | Size of limit in degrees, 0 means locked, 180 means free |
| Swing2LimitAngle | `float` | Size of limit in degrees, 0 means locked, 180 means free |

**Return**

- Type: 
- Description: _None_

### GetCurrentJointAngles

Gets the current Angular state for a named bone constraint

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoneName | `FName` | Name of bone to get constraint ranges for |
| Swing1Angle | `float &` | current angular state of the constraint |
| TwistAngle | `float &` | current angular state of the constraint |
| Swing2Angle | `float &` | current angular state of the constraint |

**Return**

- Type: 
- Description: _None_

### HandleExistingParallelEvaluationTask

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bBlockOnTask | `bool` |  |
| bPerformPostAnimEvaluation | `bool` |  |
| bBlockOnCrossFrameAnimUpdateTasks | `bool` |  |

**Return**

- Type: 
- Description: _None_

### HandleExistingParallelIMPhysicsEvaluationTask

ImmediatePhysics Evaluation Start

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bBlockOnTask | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetLastPoseTickFrame_BP

Checked whether we have already ticked the pose this frame

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetNeedUpdateChildTransformsOnFinalizeAnimationUpdate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bUpdate | `bool` |  |

**Return**

- Type: 
- Description: _None_

### PauseIMSimulation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InPauseFrameCount | `int32` |  |

**Return**

- Type: 
- Description: _None_

### MarkMeshShiftFeature

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsUseShiftFeature | `bool` |  |
| InIsOnlyPartOfShiftRefBoneAsRoot | `bool` |  |
| InShiftTransform | `FTransform &` |  |
| InShiftRefBone | `FName` |  |
| InAnchorRefBone | `FName` |  |

**Return**

- Type: 
- Description: _None_

### MarkMeshShiftCompensation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InMeshShiftCompensationType | `EMeshShiftCompensationType` |  |
| InCompensationBaseSkelComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### AnimOverrideMeshShiftParam_Start

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimMeshShiftParam | `FMeshShiftParam &` |  |

**Return**

- Type: 
- Description: _None_

### AnimOverrideMeshShiftParam_Stop

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InAnimMeshShiftParam | `FMeshShiftParam &` |  |

**Return**

- Type: 
- Description: _None_

### GetRawCurveValue

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InCurveName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### GetRetargetBoneRelativeTMInBaseRefPose

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetBoneName | `FName &` |  |

**Return**

- Type: 
- Description: _None_

### SingleNodeInstance_ActiveBoneRetargetFeature

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsActive | `bool` |  |
| InTargetSkelComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### SingleNodeInstance_OverrideBoneRetargetParam

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsUseRetargetFeature | `bool` |  |
| InIsConsiderMasterPoseRetarget | `bool` |  |
| InIsForeceUseBaseSkeletonAsRetargetSource | `bool` |  |
| InTargetSkelComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsInitAnimTickDelay

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### IsInitRefreshPoseDelay

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### DelayInitAnimTick

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InInitAnimTickParam | `FDelayInitAnimTickParam &` |  |

**Return**

- Type: 
- Description: _None_

### DelayInitRefreshPose

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PerformDelayedInitAnimTick

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### PerformDelayedInitRefreshPose

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### MarkDynamicBoneScaleFeature

For Bone Retarget Feature End

	  For Dynamic Bone Scale Feature Start

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InIsUseDynamicBoneScaleFeature | `bool` |  |
| InIsOverrideScale | `bool` |  |
| InTargetBoneNameList | `TArray < FName > &` |  |
| InDynamicScale3D | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### IsSectionBatched

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LODIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### BatchSectionsWithAtlas

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LODIdx | `int32` |  |
| IsBatchSection | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AutoBatchSection

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| LODIdx | `int32` |  |
| BatchIndices | `TArray < int32 >` |  |
| IsBatchSection | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClearInterpolateBoneCache

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| DurationTime | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetCrossFrameAnimUpdateEnabled

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bEnable | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnAnimInitialized |  |  |
| OnPreAnimClearScriptInstance |  |  |
| OnCompletePostAnimationEvaluationEnd |  |  |
| DynamicMulticastDelegate_OnFinalizeBoneTransform |  |  |
| OnSkeletalUpdateOverlapsEvent |  |  |
| OnMeshLODChangeDelegate |  |  |

## Language

cpp

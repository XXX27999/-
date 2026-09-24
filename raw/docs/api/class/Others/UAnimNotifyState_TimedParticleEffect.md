# UAnimNotifyState_TimedParticleEffect

## Parents

- [UAnimNotifyState](./UAnimNotifyState.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PSTemplate | `UParticleSystem *` |  |
| bIsPlayInWorld | `bool` |  |
| bIsRelativeToMeshSocketInWorld | `bool` |  |
| SocketName | `FName` |  |
| LocationOffset | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| RotationOffset | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| RotationOffsetDisable | `uint32` |  |
| ScaleDisable | `uint32` |  |
| ScaleMultiplier | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| bDestroyAtEnd | `bool` |  |
| bEnableAttachMeshChangeIgnoreSocketCheck | `bool` |  |
| bAdaptToNewFPP | `bool` |  |
| CacheAttachAdaptMeshComp | `TWeakObjectPtr < USkeletalMeshComponent >` |  |
| SimulatedActivationOfQualityLevel | `int32` |  |
| CurveParamList | `TMap < FName , FCurveParams >` |  |
| ParticleComp | `UParticleSystemComponent *` |  |
| bNotifyControlParticleVisible | `bool` |  |
| bEnableSpawnObjTrackFeature | `bool` |  |
| bAddAnotherBone_Z_Delta | `bool` |  |
| Z_Delta_BoneName | `FName` |  |
| ParticleTag | `FName` |  |
| SpawnedObjCacheMap | `TMap < FName , TWeakObjectPtr < UObject > >` |  |
| bSkipSocketNameCheck | `bool` |  |
| EnableDestoryByUniqueTagAtEnd | `bool` |  |
| PreviousPSTemplates | `TArray < UParticleSystem * >` |  |
| PreviousSocketNames | `TArray < FName >` |  |
| bInDebugMode | `bool` |  |
| CurrentLocationOffset | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| CurrentRotationOffset | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| CurrentScaleMultiplier | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| CachedSpawnedParticleComponent | `UParticleSystemComponent *` |  |

## Functions

### IsEnableSpawnObjTrackFeature

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### TryMarkSpawnObjTracker

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |
| InSpawnedObj | `UObject *` |  |

**Return**

- Type: 
- Description: _None_

### TryClearSpawnObjTracker

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsTrackingObj

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### GetOverrideParticleTemplate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |
| InPSTemplate | `UParticleSystem *` |  |

**Return**

- Type: 
- Description: _None_

### GetOverrideParticleWorldTransform

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |
| TargetTransform | [FTransform](../../cppstruct/F/FT/FTransform.md) |  |

**Return**

- Type: 
- Description: _None_

### InnerCheckParticleParentVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| skComp | `USkeletalMeshComponent *` |  |
| InPSC | `UParticleSystemComponent *` |  |

**Return**

- Type: 
- Description: _None_

### CheckParticleParentVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponent | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsEnableSearchAllDescendants

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### SearchChildrenParticleAndDestroy

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Children | `TArray < USceneComponent * >` |  |
| MeshComp | `USkeletalMeshComponent *` |  |
| AttachAdaptMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

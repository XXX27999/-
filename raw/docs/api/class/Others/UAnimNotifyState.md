# UAnimNotifyState

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| InOldFPPAnimMode_ChangeToNewFPPMesh | `bool` |  |
| bEnableBoneRetargetAdaptFeature | `bool` |  |
| bCheckAnimIsolation | `bool` |  |
| bCheckAnimIsolation_OnlyNewFPP | `bool` |  |
| bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode | `bool` |  |
| bCheckAnimIsolation_OnlyTPP | `bool` | 仅在TPP（第三人称）下生效，开启后此NotifyState只会在TPP AnimInstance中触发 |

## Functions

### GetNotifyName

Implementable event to get a custom name for the notify

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### Received_NotifyBegin

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MeshComp | `USkeletalMeshComponent *` |  |
| Animation | `UAnimSequenceBase *` |  |
| TotalDuration | `float` |  |
| InvokeAnimInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### Received_NotifyTick

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MeshComp | `USkeletalMeshComponent *` |  |
| Animation | `UAnimSequenceBase *` |  |
| FrameDeltaTime | `float` |  |
| InvokeAnimInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### Received_NotifyEnd

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MeshComp | `USkeletalMeshComponent *` |  |
| Animation | `UAnimSequenceBase *` |  |
| InvokeAnimInstance | `UAnimInstance *` |  |

**Return**

- Type: 
- Description: _None_

### TryGetNewFPPAdaptSkelMeshComp

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |
| InIsInitCall | `bool` |  |
| HasRetarget | `bool` |  |
| ForceGetFPPMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### TryGetBoneRetargetAdaptSkelMeshComp

For Bone Retarget Feature Start

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |
| InIsInitCall | `bool` |  |

**Return**

- Type: 
- Description: _None_

### ClearBoneRetargetAdaptState

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsBoneRetargetAdaptInitDone

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### IsEnableBoneRetargetAdaptFeature

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InTargetSkelMeshComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

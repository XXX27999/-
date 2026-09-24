# UPoseableMeshComponent

UPoseableMeshComponent that allows bone transforms to be driven by blueprint.

## Parents

- [USkinnedMeshComponent](./USkinnedMeshComponent.md)

## Variables

_None_

## Functions

### SetBoneTransformByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| InTransform | `FTransform &` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetBoneLocationByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| InLocation | `FVector` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetBoneRotationByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| InRotation | `FRotator` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### SetBoneScaleByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| InScale3D | `FVector` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetBoneTransformByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetBoneLocationByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetBoneRotationByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetBoneScaleByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |
| BoneSpace | `EBoneSpaces :: Type` |  |

**Return**

- Type: 
- Description: _None_

### ResetBoneTransformByName

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| BoneName | `FName` |  |

**Return**

- Type: 
- Description: _None_

### CopyPoseFromSkeletalComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InComponentToCopy | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

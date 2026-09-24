# UPlayMontageCallbackProxy

## Parents

- [UObject](./UObject.md)

## Variables

_None_

## Functions

### CreateProxyObjectForPlayMontage

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSkeletalMeshComponent | `USkeletalMeshComponent *` |  |
| MontageToPlay | `UAnimMontage *` |  |
| PlayRate | `float` |  |
| StartingPosition | `float` |  |
| StartingSection | `FName` |  |

**Return**

- Type: 
- Description: _None_

### OnMontageBlendingOut

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| bInterrupted | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnMontageEnded

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Montage | `UAnimMontage *` |  |
| bInterrupted | `bool` |  |

**Return**

- Type: 
- Description: _None_

### OnNotifyBeginReceived

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotifyName | `FName` |  |
| BranchingPointNotifyPayload | `FBranchingPointNotifyPayload &` |  |

**Return**

- Type: 
- Description: _None_

### OnNotifyEndReceived

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NotifyName | `FName` |  |
| BranchingPointNotifyPayload | `FBranchingPointNotifyPayload &` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

| Name | Type | Description |
| --- | --- | --- |
| OnCompleted |  |  |
| OnBlendOut |  |  |
| OnInterrupted |  |  |
| OnNotifyBegin |  |  |
| OnNotifyEnd |  |  |

## Language

cpp

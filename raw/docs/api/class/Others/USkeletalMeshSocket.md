# USkeletalMeshSocket

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SocketName | `FName` | Defines a named attachment location on the USkeletalMesh.<br>	 	These are set up in editor and used as a shortcut instead of specifying<br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent.<br>	 	The Outer of a SkeletalMeshSocket should always be the USkeletalMesh. |
| BoneName | `FName` |  |
| RelativeLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| RelativeRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| RelativeScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| BaseLocation | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| BaseRotation | [FRotator](../../cppstruct/F/FR/FRotator.md) |  |
| BaseScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| bDynamicCreate | `bool` |  |
| RelativeBoneName | `FName` |  |
| bForceAlwaysAnimated | `bool` | If true then the hierarchy of bones this socket is attached to will always be<br>	    evaluated, even if it had previously been removed due to the current lod setting |

## Functions

### GetSocketLocation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SkelComp | `USkeletalMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_

### InitializeSocketFromLocation

Sets BoneName, RelativeLocation and RelativeRotation based on closest bone to WorldLocation and WorldNormal

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SkelComp | `USkeletalMeshComponent *` |  |
| WorldLocation | `FVector` |  |
| WorldNormal | [FVector](../../cppstruct/F/FV/FVector.md) |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

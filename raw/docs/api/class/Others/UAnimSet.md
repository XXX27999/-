# UAnimSet

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| bAnimRotationOnly | `uint32` | Indicates that only the rotation should be taken from the animation sequence and the translation should come from the USkeletalMesh ref pose.<br>	 	Note that the root bone always takes translation from the animation, even if this flag is set.<br>	 	You can use the UseTranslationBoneNames array to specify other bones that should use translation with this flag set. |
| TrackBoneNames | `TArray < FName >` | Bone name that each track relates to. TrackBoneName.Num() == Number of tracks. |
| LinkupCache | `TArray < struct FAnimSetMeshLinkup >` | Non-serialised cache of linkups between different skeletal meshes and this AnimSet. |
| BoneUseAnimTranslation | `TArray < uint8 >` | Array of booleans that indicate whether or not to read the translation of a bone from animation or ref skeleton.<br>	 	This is basically a cooked down version of UseTranslationBoneNames for speed.<br>	 	Size matches the number of tracks. |
| ForceUseMeshTranslation | `TArray < uint8 >` | Cooked down version of ForceMeshTranslationBoneNames |
| UseTranslationBoneNames | `TArray < FName >` | Names of bones that should use translation from the animation, if bAnimRotationOnly is set. |
| ForceMeshTranslationBoneNames | `TArray < FName >` | List of bones which are ALWAYS going to use their translation from the mesh and not the animation. |
| PreviewSkelMeshName | `FName` | In the AnimSetEditor, when you switch to this AnimSet, it sees if this skeletal mesh is loaded and if so switches to it. |
| BestRatioSkelMeshName | `FName` | Holds the name of the skeletal mesh whose reference skeleton best matches the TrackBoneName array. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

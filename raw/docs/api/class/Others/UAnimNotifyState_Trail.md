# UAnimNotifyState_Trail

## Parents

- [UAnimNotifyState](./UAnimNotifyState.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| PSTemplate | `UParticleSystem *` | The particle system to use for this trail. |
| FirstSocketName | `FName` | Name of the first socket defining this trail. |
| SecondSocketName | `FName` | Name of the second socket defining this trail. |
| FirstSocketRelativeOffset | [FTransform](../../cppstruct/F/FT/FTransform.md) |  |
| SecondSocketRelativeOffset | [FTransform](../../cppstruct/F/FT/FTransform.md) |  |
| WidthScaleMode | `TEnumAsByte < enum ETrailWidthMode >` |  |
| WidthScaleCurve | `FName` | Name of the curve to drive the width scale. |
| bRecycleSpawnedSystems | `uint32` |  |
| bRenderGeometry | `uint32` | If true, render the trail geometry (this should typically be on) |
| bRenderSpawnPoints | `uint32` | If true, render stars at each spawned particle point along the trail |
| bRenderTangents | `uint32` | If true, render a line showing the tangent at each spawned particle point along the trail |
| bRenderTessellation | `uint32` | If true, render the tessellated path between spawned particles |

## Functions

### OverridePSTemplate

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| MeshComp | `USkeletalMeshComponent *` |  |
| Animation | `UAnimSequenceBase *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

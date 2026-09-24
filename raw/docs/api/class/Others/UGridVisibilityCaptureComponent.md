# UGridVisibilityCaptureComponent

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FOVAngle | `float` | Camera field of view (in degrees). |
| CaptureViewSize | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) |  |
| NearClipPlane | `float` |  |
| GridMesh | `UStaticMesh *` |  |
| GridMeshSizeScale | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| GridMeshLocationOffset | [FVector](../../cppstruct/F/FV/FVector.md) |  |
| bForceLowestLOD | `uint32` |  |
| bHiddenFoliage | `uint32` |  |
| OcclusionDepthDiffThreshold | `float` |  |
| bShouldRenderGridMeshInMainPass | `uint32` |  |
| MaxNumProcessWaitingResultCmdsPerFrame | `int32` |  |
| MaxNumProcessWaitingCalculateCmdsPerFrame | `int32` |  |
| GridSize | [FIntPoint](../../cppstruct/F/FI/FIntPoint.md) |  |
| RenderTargetToCreateRenderer | `UTextureRenderTarget2D *` |  |
| GridMeshComp | `UInstancedStaticMeshComponent *` |  |

## Functions

### InitGridIDVisibilityCalculation

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InGridLocations | `TArray < FVector > &` |  |

**Return**

- Type: 
- Description: _None_

### CalculateGridIDVisibility

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| GridID | `int32` |  |
| CameraLocations | `TArray < FGridVisibilityCameraInfo > &` |  |
| PotentialGrids | `TArray < int32 > &` |  |

**Return**

- Type: 
- Description: _None_

### FinishGridIDVisibilityCalculation

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

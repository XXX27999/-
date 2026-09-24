# UUserWidget3D

UUserWidget3D - A UMG widget that can render a 3D StaticMesh directly to the BackBuffer.

  Two rendering modes:
    1. Legacy Slate3D path: Call AddTo3DWidget() to render 2D widget content with 3D rotation via SWindow3D + RT.
    2. Direct Mesh path: Set MeshAsset and the mesh is rendered directly to BackBuffer each frame via ENQUEUE_RENDER_COMMAND.

## Parents

- [UUserWidget](./UUserWidget.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| FOV | `float` |  |
| Brush | `UTextureRenderTarget2D *` |  |
| MeshAsset | `UStaticMesh *` | The StaticMesh asset to render. |
| MeshRotationYaw | `float` | Yaw rotation (degrees). Animatable via UMG Animation. |
| MeshRotationPitch | `float` | Pitch rotation (degrees). Animatable via UMG Animation. |
| MeshScale | [FVector](../../cppstruct/F/FV/FVector.md) | Scale of the mesh. |
| MeshOffset | [FVector](../../cppstruct/F/FV/FVector.md) | Offset of the mesh center (screen pixel coordinates). |
| MeshCameraDistance | `float` | Camera distance from the mesh. Controls apparent size. |

## Functions

### AddTo3DWidget

Legacy: Add this widget to the Slate3D rendering pipeline (renders to RT via SWindow3D).

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetMeshRotation

Set the mesh rotation and refresh the mesh drawer.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewYaw | `float` |  |
| NewPitch | `float` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

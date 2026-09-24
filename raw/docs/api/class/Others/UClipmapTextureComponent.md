# UClipmapTextureComponent

Component used to place a URuntimeVirtualTexture in the world.

## Parents

- [USceneComponent](./USceneComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ClipmapTexture | `UClipmapTexture *` |  |
| bUseForCDLODMatID | `bool` |  |
| BoundsSourceActor | `AActor *` | Actor to copy the bounds from to set up the transform. |
| MipToDis | `TMap < int32 , float >` |  |
| ClipmapInfo | [FVector4](../../cppstruct/F/FV/FVector4.md) |  |

## Functions

### SetTransformToBounds

Set this component transform to include the BoundsSourceActor bounds. Called by our UI details customization.

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### RefreshClipmapInfo

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

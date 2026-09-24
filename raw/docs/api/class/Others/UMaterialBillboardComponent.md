# UMaterialBillboardComponent

A 2d material that will be rendered always facing the camera.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Elements | `TArray < FMaterialSpriteElement >` | Current array of material billboard elements |

## Functions

### SetElements

Set all elements of this material billboard component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewElements | `TArray < FMaterialSpriteElement > &` |  |

**Return**

- Type: 
- Description: _None_

### AddElement

Adds an element to the sprite.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Material | `UMaterialInterface *` |  |
| DistanceToOpacityCurve | `UCurveFloat *` |  |
| bSizeIsInScreenSpace | `bool` |  |
| BaseSizeX | `float` |  |
| BaseSizeY | `float` |  |
| DistanceToSizeCurve | `UCurveFloat *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

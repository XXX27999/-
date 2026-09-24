# UMultiBillBoardComponent

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Elements | `TArray < FBillBoardMaterialSpriteElement >` | Current array of material billboard elements |
| BillboardDatas | `TArray < FBillboardData >` |  |

## Functions

### GetElements

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetElements

Set all elements of this material billboard component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewElements | `TArray < FBillBoardMaterialSpriteElement > &` |  |

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

### K2_AddBillBoard

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| NewLocation | `FVector` |  |
| UV0 | `FVector2D` |  |
| UV1 | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### RemoveBillboard

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `int32` |  |

**Return**

- Type: 
- Description: _None_

### ClearAllBillBoards

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBillboardUV

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| ID | `int32` |  |
| UV0 | `FVector2D` |  |
| UV1 | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |

**Return**

- Type: 
- Description: _None_

### CreateMultiBillboardComponent

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldContextObject | `UObject *` |  |
| MultiBillboardClass | `TSubclassOf < UMultiBillBoardComponent >` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# UMeshVertexPainterKismetLibrary

## Parents

- UBlueprintFunctionLibrary

## Variables

_None_

## Functions

### PaintVerticesSingleColor

Paints vertex colors on a mesh component in a specified color.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StaticMeshComponent | `UStaticMeshComponent *` |  |
| FillColor | `FLinearColor &` |  |
| bConvertToSRGB | `bool` |  |

**Return**

- Type: 
- Description: _None_

### PaintVerticesLerpAlongAxis

Paints vertex colors on a mesh component lerping from the start to the end color along the specified axis.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StaticMeshComponent | `UStaticMeshComponent *` |  |
| StartColor | `FLinearColor &` |  |
| EndColor | `FLinearColor &` |  |
| Axis | `EVertexPaintAxis` |  |
| bConvertToSRGB | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RemovePaintedVertices

Removes vertex colors on a mesh component

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StaticMeshComponent | `UStaticMeshComponent *` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

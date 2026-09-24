# USplineMeshComponent

A Spline Mesh Component is a derivation of a Static Mesh Component which can be deformed using a spline. Only a start and end position (and tangent) can be specified.

## Parents

- [UStaticMeshComponent](./UStaticMeshComponent.md)
- IInterface_CollisionDataProvider

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SplineParams | [FSplineMeshParams](../../cppstruct/F/FS/FSplineMeshParams.md) | Spline that is used to deform mesh |
| SplineUpDir | [FVector](../../cppstruct/F/FV/FVector.md) | Axis (in component space) that is used to determine X axis for co-ordinates along spline |
| bAllowSplineEditingPerInstance | `uint32` | If true, spline keys may be edited per instance in the level viewport. Otherwise, the spline should be initialized in the construction script. |
| bSmoothInterpRollScale | `uint32` | If true, will use smooth interpolation (ease inout) for Scale, Roll, and Offset along this section of spline. If false, uses linear |
| ForwardAxis | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the forward axis for the spline mesh orientation |
| SplineBoundaryMin | `float` | Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds |
| SplineBoundaryMax | `float` | Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds |
| BodySetup | `UBodySetup *` |  |
| CachedMeshBodySetupGuid | [FGuid](../../cppstruct/F/FG/FGuid.md) |  |
| bMeshDirty | `uint32` |  |
| bHasBeenBakedWithLandcape | `uint32` |  |

## Functions

### UpdateMesh

Update the collision and render state on the spline mesh following changes to its geometry

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetStartPosition

Get the start position of spline in local space

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetStartPosition

Set the start position of spline in local space

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartPos | `FVector` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetStartTangent

Get the start tangent vector of spline in local space

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetStartTangent

Set the start tangent vector of spline in local space

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartTangent | `FVector` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEndPosition

Get the end position of spline in local space

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEndPosition

Set the end position of spline in local space

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndPos | `FVector` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEndTangent

Get the end tangent vector of spline in local space

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEndTangent

Set the end tangent vector of spline in local space

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndTangent | `FVector` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetStartAndEnd

Set the start and end, position and tangent, all in local space

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartPos | `FVector` |  |
| StartTangent | `FVector` |  |
| EndPos | `FVector` |  |
| EndTangent | `FVector` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetStartScale

Get the start scaling

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetStartScale

Set the start scaling

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartScale | `FVector2D` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetStartRoll

Get the start roll

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetStartRoll

Set the start roll

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartRoll | `float` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetStartOffset

Get the start offset

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetStartOffset

Set the start offset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| StartOffset | `FVector2D` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEndScale

Get the end scaling

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEndScale

Set the end scaling

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndScale | `FVector2D` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEndRoll

Get the end roll

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEndRoll

Set the end roll

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndRoll | `float` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetEndOffset

Get the end offset

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetEndOffset

Set the end offset

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| EndOffset | `FVector2D` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetForwardAxis

Get the forward axis

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetForwardAxis

Set the forward axis

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InForwardAxis | `ESplineMeshAxis :: Type` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetSplineUpDir

Get the spline up direction

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetSplineUpDir

Set the spline up direction

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InSplineUpDir | `FVector &` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetBoundaryMin

Get the boundary min

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBoundaryMin

Set the boundary min

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoundaryMin | `float` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetBoundaryMax

Get the boundary max

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetBoundaryMax

Set the boundary max

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InBoundaryMax | `float` |  |
| bUpdateMesh | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

# USplineComponent

A spline component is a spline shape which can be used for other purposes (e.g. animating objects). It contains debug rendering capabilities.

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| SplineCurves | [FSplineCurves](../../cppstruct/F/FS/FSplineCurves.md) |  |
| SplineInfo_DEPRECATED | [FInterpCurveVector](../../cppstruct/F/FI/FInterpCurveVector.md) | Deprecated - please use GetSplinePointsPosition() to fetch this FInterpCurve |
| SplineRotInfo_DEPRECATED | [FInterpCurveQuat](../../cppstruct/F/FI/FInterpCurveQuat.md) | Deprecated - please use GetSplinePointsRotation() to fetch this FInterpCurve |
| SplineScaleInfo_DEPRECATED | [FInterpCurveVector](../../cppstruct/F/FI/FInterpCurveVector.md) | Deprecated - please use GetSplinePointsScale() to fetch this FInterpCurve |
| SplineReparamTable_DEPRECATED | [FInterpCurveFloat](../../cppstruct/F/FI/FInterpCurveFloat.md) |  |
| bAllowSplineEditingPerInstance_DEPRECATED | `bool` |  |
| ReparamStepsPerSegment | `int32` | Number of steps per spline segment to place in the reparameterization table |
| Duration | `float` | Specifies the duration of the spline in seconds |
| bStationaryEndpoints | `bool` | Whether the endpoints of the spline are considered stationary when traversing the spline at non-constant velocity.  Essentially this sets the endpoints' tangents to zero vectors. |
| bSplineHasBeenEdited | `bool` | Whether the spline has been edited from its default by the spline component visualizer |
| bModifiedByConstructionScript | `bool` | Whether the UCS has made changes to the spline points |
| bInputSplinePointsToConstructionScript | `bool` | Whether the spline points should be passed to the User Construction Script so they can be further manipulated by it.<br>	  If false, they will not be visible to it, and it will not be able to influence the per-instance positions set in the editor. |
| bDrawDebug | `bool` | If true, the spline will be rendered if the Splines showflag is set. |
| bClosedLoop | `bool` | Whether the spline is to be considered as a closed loop.<br>	  Use SetClosedLoop() to set this property, and IsClosedLoop() to read it. |
| bLoopPositionOverride | `bool` |  |
| LoopPosition | `float` |  |
| DefaultUpVector | [FVector](../../cppstruct/F/FV/FVector.md) | Default up vector in local space to be used when calculating transforms along the spline |
| bUseConfigRotation | `bool` | Engine Modify Start |
| bUseConfigRotationXY | `bool` |  |
| EditorUnselectedSplineSegmentColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Engine Modify End<br><br>	 Color of an unselected spline component segment in the editor |
| EditorSelectedSplineSegmentColor | [FLinearColor](../../cppstruct/F/FL/FLinearColor.md) | Color of a selected spline component segment in the editor |
| bAllowDiscontinuousSpline | `bool` | Whether the spline's leave and arrive tangents can be different |
| bShouldVisualizeScale | `bool` | Whether scale visualization should be displayed |
| ScaleVisualizationWidth | `float` | Width of spline in editor for use with scale visualization |
| PostionModifyer | `USplineComponentEditorModifer *` |  |
| SelectedIndexs | `TSet < int32 >` |  |
| SnappingType | [ESplineSnappingType](../../cppenum/E/ES/ESplineSnappingType.md) |  |
| SnapInterval | `float` |  |
| SnapTopDownRange | [FVector2D](../../cppstruct/F/FV/FVector2D.md) |  |
| TraceLength | `float` |  |

## Functions

### UpdateSpline

Update the spline tangents and SplineReparamTable

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetDistanceAlongSplineAtSplineInputKey

Get distance along the spline at the provided input key value

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| InKey | `float` |  |

**Return**

- Type: 
- Description: _None_

### SetUnselectedSplineSegmentColor

Specify unselected spline component segment color in the editor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SegmentColor | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### SetSelectedSplineSegmentColor

Specify selected spline component segment color in the editor

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| SegmentColor | `FLinearColor &` |  |

**Return**

- Type: 
- Description: _None_

### EditorSnapToGround

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### EditorNormalizeSplineTangent

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetDrawDebug

Specify whether this spline should be rendered when the EditorGame spline show flag is set

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bShow | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetClosedLoop

Specify whether the spline is a closed loop or not. The loop position will be at 1.0 after the last point's input key

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInClosedLoop | `bool` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetClosedLoopAtPosition

Specify whether the spline is a closed loop or not, and if so, the input key corresponding to the loop point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bInClosedLoop | `bool` |  |
| Key | `float` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### IsClosedLoop

Check whether the spline is a closed loop or not

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### ClearSplinePoints

Clears all the points in the spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddPoint

Adds an FSplinePoint to the spline. This contains its input key, position, tangent, rotation and scale.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Point | `FSplinePoint &` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddPoints

Adds an array of FSplinePoints to the spline.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Points | `TArray < FSplinePoint > &` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddSplinePoint

Adds a point to the spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Position | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddSplinePointAtIndex

Adds a point to the spline at the specified index

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Position | `FVector &` |  |
| Index | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### RemoveSplinePoint

Removes point at specified index from the spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Index | `int32` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### AddSplineWorldPoint

Adds a world space point to the spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Position | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### AddSplineLocalPoint

Adds a local space point to the spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Position | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetSplinePoints

Sets the spline to an array of points

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Points | `TArray < FVector > &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetSplineWorldPoints

Sets the spline to an array of world space points

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Points | `TArray < FVector > &` |  |

**Return**

- Type: 
- Description: _None_

### SetSplineLocalPoints

Sets the spline to an array of local space points

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Points | `TArray < FVector > &` |  |

**Return**

- Type: 
- Description: _None_

### SetLocationAtSplinePoint

Move an existing point to a new location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| InLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetWorldLocationAtSplinePoint

Move an existing point to a new world location

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| InLocation | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### SetTangentAtSplinePoint

Specify the tangent at a given spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| InTangent | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetTangentsAtSplinePoint

Specify the tangents at a given spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| InArriveTangent | `FVector &` |  |
| InLeaveTangent | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### SetUpVectorAtSplinePoint

Specify the up vector at a given spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| InUpVector | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetSplinePointType

Get the type of a spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### SetSplinePointType

Specify the type of a spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| Type | `ESplinePointType :: Type` |  |
| bUpdateSpline | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetNumberOfSplinePoints

Get the number of points that make up this spline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### GetLocationAtSplinePoint

Get the location at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldLocationAtSplinePoint

Get the world location at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetDirectionAtSplinePoint

Get the location at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetTangentAtSplinePoint

Get the tangent at spline point. This fetches the Leave tangent of the point.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetArriveTangentAtSplinePoint

Get the arrive tangent at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetLeaveTangentAtSplinePoint

Get the leave tangent at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetRotationAtSplinePoint

Get the rotation at spline point as a rotator

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetUpVectorAtSplinePoint

Get the up vector at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetRightVectorAtSplinePoint

Get the right vector at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetRollAtSplinePoint

Get the amount of roll at spline point, in degrees

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetScaleAtSplinePoint

Get the scale at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetTransformAtSplinePoint

Get the transform at spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseScale | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetLocationAndTangentAtSplinePoint

Get location and tangent at a spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| Location | `FVector &` |  |
| Tangent | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetLocalLocationAndTangentAtSplinePoint

Get local location and tangent at a spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |
| LocalLocation | `FVector &` |  |
| LocalTangent | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### GetDistanceAlongSplineAtSplinePoint

Get the distance along the spline at the spline point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| PointIndex | `int32` |  |

**Return**

- Type: 
- Description: _None_

### GetSplineLength

Returns total length along this spline

**Parameters**

_None_

**Return**

- Type: 
- Description: _None_

### SetDefaultUpVector

Sets the default up vector used by this spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| UpVector | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetDefaultUpVector

Gets the default up vector used by this spline

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetInputKeyAtDistanceAlongSpline

Given a distance along the length of this spline, return the corresponding input key at that point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetTimeAtDistanceAlongSpline

Given a distance along the length of this spline, return the corresponding time at that point

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetLocationAtDistanceAlongSpline

Given a distance along the length of this spline, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldLocationAtDistanceAlongSpline

Given a distance along the length of this spline, return the point in world space where this puts you

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetDirectionAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldDirectionAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there, in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetTangentAtDistanceAlongSpline

Given a distance along the length of this spline, return the tangent vector of the spline there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldTangentAtDistanceAlongSpline

Given a distance along the length of this spline, return the tangent vector of the spline there, in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetRotationAtDistanceAlongSpline

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldRotationAtDistanceAlongSpline

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there, in world space.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetUpVectorAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's up vector there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetRightVectorAtDistanceAlongSpline

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's right vector there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetRollAtDistanceAlongSpline

Given a distance along the length of this spline, return the spline's roll there, in degrees.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### GetScaleAtDistanceAlongSpline

Given a distance along the length of this spline, return the spline's scale there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |

**Return**

- Type: 
- Description: _None_

### GetTransformAtDistanceAlongSpline

Given a distance along the length of this spline, return an FTransform corresponding to that point on the spline.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Distance | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseScale | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetLocationAtTime

Given a time from 0 to the spline duration, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldLocationAtTime

Given a time from 0 to the spline duration, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetDirectionAtTime

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldDirectionAtTime

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTangentAtTime

Given a time from 0 to the spline duration, return the spline's tangent there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetRotationAtTime

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetWorldRotationAtTime

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetUpVectorAtTime

Given a time from 0 to the spline duration, return the spline's up vector there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetRightVectorAtTime

Given a time from 0 to the spline duration, return the spline's right vector there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetTransformAtTime

Given a time from 0 to the spline duration, return the spline's transform at the corresponding position.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |
| bUseScale | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetRollAtTime

Given a time from 0 to the spline duration, return the spline's roll there, in degrees.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### GetScaleAtTime

Given a time from 0 to the spline duration, return the spline's scale there.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| Time | `float` |  |
| bUseConstantVelocity | `bool` |  |

**Return**

- Type: 
- Description: _None_

### FindInputKeyClosestToWorldLocation

Given a location, in world space, return the input key closest to that location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### FindLocationClosestToWorldLocation

Given a location, in world space, return the point on the curve that is closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindDirectionClosestToWorldLocation

Given a location, in world spcae, return a unit direction vector of the spline tangent closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindTangentClosestToWorldLocation

Given a location, in world space, return the tangent vector of the spline closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindRotationClosestToWorldLocation

Given a location, in world space, return rotation corresponding to the spline's rotation closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindUpVectorClosestToWorldLocation

Given a location, in world space, return a unit direction vector corresponding to the spline's up vector closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindRightVectorClosestToWorldLocation

Given a location, in world space, return a unit direction vector corresponding to the spline's right vector closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindRollClosestToWorldLocation

Given a location, in world space, return the spline's roll closest to the location, in degrees.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |

**Return**

- Type: 
- Description: _None_

### FindScaleClosestToWorldLocation

Given a location, in world space, return the spline's scale closest to the location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |

**Return**

- Type: 
- Description: _None_

### FindTransformClosestToWorldLocation

Given a location, in world space, return an FTransform closest to that location.

**Parameters**

| Name | Type | Description |
| --- | --- | --- |
| WorldLocation | `FVector &` |  |
| CoordinateSpace | `ESplineCoordinateSpace :: Type` |  |
| bUseScale | `bool` |  |

**Return**

- Type: 
- Description: _None_


## Event

_None_

## Delegate

_None_

## Language

cpp

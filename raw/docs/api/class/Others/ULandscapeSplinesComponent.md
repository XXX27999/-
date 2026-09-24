# ULandscapeSplinesComponent

## Parents

- [UPrimitiveComponent](./UPrimitiveComponent.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| ControlPoints | `TArray < ULandscapeSplineControlPoint * >` |  |
| Segments | `TArray < ULandscapeSplineSegment * >` |  |
| CookedForeignMeshComponents | `TArray < UMeshComponent * >` |  |
| SplineResolution | `float` | Resolution of the spline, in distance per point |
| SplineColor | [FColor](../../cppstruct/F/FC/FColor.md) | Color to use to draw the splines |
| ControlPointSprite | `UTexture2D *` | Sprite used to draw control points |
| SplineEditorMesh | `UStaticMesh *` | Mesh used to draw splines that have no mesh |
| bShowSplineEditorMesh | `uint32` | Whether we are in-editor and showing spline editor meshes |
| ForeignWorldSplineDataMap | `TMap < TSoftObjectPtr < UWorld > , FForeignWorldSplineData >` |  |
| bOverrideSplineMeshLightmapType | `uint8` | Whether to override the lightmap type for all spline mesh components. |
| SplineMeshLightmapType | `TEnumAsByte < ELightmapType >` | Controls the type of lightmap used for all spline mesh components. Only used if bOverrideSplineMeshLightmapType is true. |
| bOverrideSplineMeshLightmapRes | `uint8` | Whether to override the lightmap resolution for all spline mesh components. |
| OverriddenSplineMeshLightmapRes | `int32` | Light map resolution to use on all spline mesh components, used if bOverrideSplineMeshLightmapRes is true. |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp

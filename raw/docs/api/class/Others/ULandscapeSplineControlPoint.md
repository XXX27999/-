# ULandscapeSplineControlPoint

## Parents

- [UObject](./UObject.md)

## Variables

| Name | Type | Description |
| --- | --- | --- |
| Location | [FVector](../../cppstruct/F/FV/FVector.md) | Location in Landscape-space |
| Rotation | [FRotator](../../cppstruct/F/FR/FRotator.md) | Rotation of tangent vector at this point (in landscape-space) |
| Width | `float` | Width of the spline at this point. |
| SideFalloff | `float` | Falloff at the sides of the spline at this point. |
| EndFalloff | `float` | Falloff at the startend of the spline (if this point is a start or end point, otherwise ignored). |
| ConnectedSegments | `TArray < FLandscapeSplineConnection >` |  |
| Points | `TArray < FLandscapeSplineInterpPoint >` | Spline points |
| Bounds | [FBox](../../cppstruct/F/FB/FBox.md) | Bounds of points |
| LocalMeshComponent | `UControlPointMeshComponent *` | Control point mesh |
| SegmentMeshOffset | `float` | Vertical offset of the spline segment mesh. Useful for a river's surface, among other things. |
| LayerName | `FName` | Name of blend layer to paint when applying spline to landscape<br>	  If "none", no layer is painted |
| bRaiseTerrain | `uint32` | If the spline is above the terrain, whether to raise the terrain up to the level of the spline when applying it to the landscape. |
| bLowerTerrain | `uint32` | If the spline is below the terrain, whether to lower the terrain down to the level of the spline when applying it to the landscape. |
| Mesh | `UStaticMesh *` | Mesh to use on the control point |
| MaterialOverrides | `TArray < UMaterialInterface * >` | Overrides mesh's materials |
| MeshScale | [FVector](../../cppstruct/F/FV/FVector.md) | Scale of the control point mesh |
| bEnableCollision | `uint32` | Whether to enable collision for the Control Point Mesh. |
| bCastShadow | `uint32` | Whether the Control Point Mesh should cast a shadow. |
| LDMaxDrawDistance | `float` | Max draw distance for the mesh used on this control point |
| TranslucencySortPriority | `int32` | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br><br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly. |
| bPlaceSplineMeshesInStreamingLevels | `uint32` | Whether control point mesh should be placed in landscape proxy streaming level (true) or the spline's level (false) |
| bRenderToTerrainVirtualTexture | `uint8` | This spline will be rendered to terrain VT if true |
| TerrainRVTRenderSortPriority | `int32` | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |
| bHiddenInGame | `bool` |  |
| bSelected | `uint32` |  |
| bNavDirty | `uint32` |  |
| ForeignWorld | `TSoftObjectPtr < UWorld >` | World reference for if mesh component is stored in another streaming level |
| ModificationKey | [FGuid](../../cppstruct/F/FG/FGuid.md) | Key for tracking whether this segment has been modified relative to the mesh component stored in another streaming level |

## Functions

_None_

## Event

_None_

## Delegate

_None_

## Language

cpp
